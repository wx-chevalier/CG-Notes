# Performance pitfalls

Three.js 中最重要的问题是，创建对象可能很昂贵，在你安装/卸载东西之前要三思而后行 你放到场景中的每一个材质或灯光都要进行编译，你创建的每一个几何体都要进行处理。如果可以的话，可以在全局范围内或本地共享材质和几何体。

```js
const geom = useMemo(() => new BoxGeometry(), [])
const mat = useMemo(() => new MeshBasicMaterial(), [])
return items.map(i => <mesh geometry={geom} material={mat} ...
```

如下面这样尽可能复用：

```js
import * as THREE from "three";
import React, { useRef, useMemo, useState, useEffect } from "react";
import { Canvas, extend, useThree, useFrame } from "@react-three/fiber";
import niceColors from "nice-color-palettes";
import { Effects } from "@react-three/drei";
import { SSAOPass, UnrealBloomPass } from "three-stdlib";

extend({ SSAOPass, UnrealBloomPass });
const tempObject = new THREE.Object3D();
const tempColor = new THREE.Color();
const data = Array.from({ length: 1000 }, () => ({
  color: niceColors[17][Math.floor(Math.random() * 5)],
  scale: 1,
}));

export function App() {
  return (
    <Canvas
      gl={{ antialias: false }}
      camera={{ position: [0, 0, 15], near: 5, far: 20 }}
    >
      <color attach="background" args={["#f0f0f0"]} />
      <Boxes />
      <Post />
    </Canvas>
  );
}

function Boxes() {
  const [hovered, set] = useState();
  const colorArray = useMemo(
    () =>
      Float32Array.from(
        new Array(1000)
          .fill()
          .flatMap((_, i) => tempColor.set(data[i].color).toArray())
      ),
    []
  );
  const meshRef = useRef();
  const prevRef = useRef();
  useEffect(() => void (prevRef.current = hovered), [hovered]);

  useFrame((state) => {
    const time = state.clock.getElapsedTime();
    meshRef.current.rotation.x = Math.sin(time / 4);
    meshRef.current.rotation.y = Math.sin(time / 2);
    let i = 0;
    for (let x = 0; x < 10; x++)
      for (let y = 0; y < 10; y++)
        for (let z = 0; z < 10; z++) {
          const id = i++;
          tempObject.position.set(5 - x, 5 - y, 5 - z);
          tempObject.rotation.y =
            Math.sin(x / 4 + time) +
            Math.sin(y / 4 + time) +
            Math.sin(z / 4 + time);
          tempObject.rotation.z = tempObject.rotation.y * 2;
          if (hovered !== prevRef.Current) {
            (id === hovered
              ? tempColor.setRGB(10, 10, 10)
              : tempColor.set(data[id].color)
            ).toArray(colorArray, id * 3);
            meshRef.current.geometry.attributes.color.needsUpdate = true;
          }
          const scale = (data[id].scale = THREE.MathUtils.lerp(
            data[id].scale,
            id === hovered ? 2.5 : 1,
            0.1
          ));
          tempObject.scale.setScalar(scale);
          tempObject.updateMatrix();
          meshRef.current.setMatrixAt(id, tempObject.matrix);
        }
    meshRef.current.instanceMatrix.needsUpdate = true;
  });

  return (
    <instancedMesh
      ref={meshRef}
      args={[null, null, 1000]}
      onPointerMove={(e) => (e.stopPropagation(), set(e.instanceId))}
      onPointerOut={(e) => set(undefined)}
    >
      <boxGeometry args={[0.6, 0.6, 0.6]}>
        <instancedBufferAttribute
          attach="attributes-color"
          args={[colorArray, 3]}
        />
      </boxGeometry>
      <meshBasicMaterial toneMapped={false} vertexColors />
    </instancedMesh>
  );
}

function Post() {
  const { scene, camera } = useThree();
  return (
    <Effects disableGamma>
      <sSAOPass args={[scene, camera]} kernelRadius={0.5} maxDistance={0.1} />
      <unrealBloomPass threshold={0.9} strength={0.75} radius={0.5} />
    </Effects>
  );
}
```

# Avoid setState in loops

即使 React 可以处理它，你也不会想每秒钟调用 60 或 120 次。抛开性能风险不谈，仅仅是连续设置数值是不够的，你需要有管理的帧延迟，否则你的项目将根据最终用户的系统以不同的速度运行。另外，threejs 中的许多更新都需要与更新标志（.needsUpdate = true）或强制函数（.updateProjectionMatrix()）相匹配。最好习惯于这样的想法：threejs 本身是循环驱动的，而框架是反应式的。你需要两者，状态和道具的反应性，动画的循环。让 React 处理前者，而 Fiber 为后者提供一个出口：useFrame。这个钩子在一个组合的 framelop 中运行，包括 deltas 和更多。

```js
❌ setState in loops is bad
const [x, setX] = useState(0)
useFrame(() => setX((x) => x + 0.1))
return <mesh position-x={x} />

❌ setState in fast intervals is bad
useEffect(() => {
  const interval = setInterval(() => setX((x) => x + 0.1), 1)
  return () => clearInterval(interval)
}, [])

❌ setState in fast events is bad
<mesh onPointerMove={(e) => setX((x) => e.point.x)} />
```

一般来说，你应该倾向于使用 Frame。只要组件是唯一会变动的实体，就可以考虑安全地变动 props。使用 deltas 而不是固定值，这样你的应用程序就可以不受刷新率的影响，在任何地方都能以同样的速度运行。

```js
const ref = useRef();
useFrame((state, delta) => (ref.current.position.x += delta));
return <mesh ref={ref} />;

// Same goes for events, use references.
<mesh onPointerMove={(e) => (ref.current.position.x = e.point.x)} />;

// If you must use intervals, use references as well, but keep in mind that this is not refresh-rate independent.
useEffect(() => {
  const interval = setInterval(() => ref.current.position.x += 0.1), 1)
  return () => clearInterval(interval)
}, [])
```

# Handle animations in loops

帧循环是你应该放置你的动画的地方。例如使用 lerp，或 damp。

```js
function Signal({ active }) {
  const ref = useRef()
  useFrame((state, delta) => {
    ref.current.position.x = THREE.MathUtils.lerp(ref.current.position.x, active ? 100 : 0, 0.1)
  })
  return <mesh ref={ref} />
```

或者，使用动画库。React-spring 有自己的框架-循环，并在 React 之外进行动画。Framer-motion 是另一个流行的选择。

```js
import { a, useSpring } from '@react-spring/three'

function Signal({ active }) {
  const { x } = useSpring({ x: active ? 100 : 0 })
  return <a.mesh position-x={x} />
```

# Do not bind to fast state reactively

使用状态管理程序和选择性状态是可以的，但对于快速发生的更新来说，就不是这样了，原因和上面一样。

```js
❌ Don't bind reactive fast-state
import { useSelector } from 'react-redux'

// Assuming that x gets animated inside the store 60fps
const x = useSelector((state) => state.x)
return <mesh position-x={x} />
```

而应该定期主动获取：

```js
useFrame(() => (ref.current.position.x = api.getState().x));
return <mesh ref={ref} />;
```

# Don't mount indiscriminately

在 threejs 中，完全不重新挂载是很常见的，见 discover-three 中的 ["disposing of things"](https://discoverthreejs.com/tips-and-tricks/) 部分。这是因为缓冲区和材料会被重新初始化/编译，这可能很昂贵。

```js
❌ Avoid mounting runtime
{
  stage === 1 && <Stage1 />
}
{
  stage === 2 && <Stage2 />
}
{
  stage === 3 && <Stage3 />
}

✅ Consider using visibility instead
<Stage1 visible={stage === 1} />
<Stage2 visible={stage === 2} />
<Stage3 visible={stage === 3} />

function Stage1(props) {
  return (
    <group {...props}>
      ...
```

React 18 引入了 startTransition 和 useTransition APIs 来推迟和安排工作和状态更新。使用这些来降低昂贵操作的优先级。自 Fiber canvases 的第 8 版以来，默认使用并发模式，这意味着 React 将安排和推迟昂贵的操作。你不需要做任何事情，但你可以玩玩实验性的调度器，看看用较低的优先级来标记操作是否会有变化。

```js
import { useTransition } from 'react'
import { Points } from '@react-three/drei'

const [isPending, startTransition] = useTransition()
const [radius, setRadius] = useState(1)
const positions = calculatePositions(radius)
const colors = calculateColors(radius)
const sizes = calculateSizes(radius)

<Points
  positions={positions}
  colors={colors}
  sizes={sizes}
  onPointerOut={() => {
    startTransition(() => {
      setRadius(prev => prev + 1)
    })
  }}
>
  <meshBasicMaterial vertexColors />
</Points>
```

# Don't re-create objects in loops

尽量避免给垃圾收集器带来太多麻烦，在可以的情况下对对象进行重新分类。

```js
❌ Bad news for the GC
useFrame(() => {
  ref.current.position.lerp(new THREE.Vector3(x, y, z), 0.1)
})

✅ Better re-use object
function Foo(props)
  const vec = new THREE.Vector()
  useFrame(() => {
    ref.current.position.lerp(vec.set(x, y, z), 0.1)
  })
```

# useLoader instead of plain loaders

Threejs 加载器为你提供了加载异步资产（模型、纹理等）的能力，但如果你不重复使用资产，它很快就会出现问题。

```js
❌ No re-use is bad for perf
function Component() {
  const [texture, set] = useState();
  useEffect(() => void new TextureLoader().load(url, set), []);
  return texture ? (
    <mesh>
      <sphereGeometry />
      <meshBasicMaterial map={texture} />
    </mesh>
  ) : null;
}

✅ Cache and re-use objects
function Component() {
  const texture = useLoader(TextureLoader, url)
  return (
    <mesh>
      <sphereGeometry />
      <meshBasicMaterial map={texture} />
    </mesh>
  )
}
```
