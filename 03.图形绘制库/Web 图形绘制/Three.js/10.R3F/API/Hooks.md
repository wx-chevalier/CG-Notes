# Hooks

Hooks 允许你为你的组件绑定或请求特定的信息。例如，想要参与渲染循环的组件可以使用 useFrame，需要了解 three.js 具体信息的组件可以使用 useThree，等等。一旦组件卸载，所有的 Hooks 都会自己清理掉。

Hooks 只能在 Canvas 元素内使用，因为它们依赖于 Context。

```js
❌ You cannot expect something like this to work:
import { useThree } from '@react-three/fiber'

function App() {
  const { size } = useThree() // This will just crash
  return (
    <Canvas>
      <mesh>

✅ Do this instead:
function Foo() {
  const { size } = useThree()
  ...
}

function App() {
  return (
    <Canvas>
      <Foo />
```

# useThree

这个 Hook 可以让你访问状态模型，其中包含默认的渲染器、场景、你的相机等等。它还会给你提供屏幕和视口坐标中画布的当前尺寸。

```js
import { useThree } from '@react-three/fiber'

function Foo() {
  const state = useThree()
```

这个 Hook 是反应式的，例如，如果你调整浏览器的大小，你会得到新的测量结果，这同样适用于任何可能发生变化的状态对象。

| PROP            | DESCRIPTION                                                                   | TYPE                                                                                                                                                                                                           |
| :-------------- | :---------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| gl              | Renderer                                                                      | `THREE.WebGLRenderer`                                                                                                                                                                                          |
| scene           | Scene                                                                         | `THREE.Scene`                                                                                                                                                                                                  |
| camera          | Camera                                                                        | `THREE.PerspectiveCamera`                                                                                                                                                                                      |
| raycaster       | Default raycaster                                                             | `THREE.Raycaster`                                                                                                                                                                                              |
| pointer         | Contains updated, normalized, centric pointer coordinates                     | `THREE.Vector2`                                                                                                                                                                                                |
| mouse           | Note: this is deprecated, use `pointer` instead! Normalized event coordinates | `THREE.Vector2`                                                                                                                                                                                                |
| clock           | Running system clock                                                          | `THREE.Clock`                                                                                                                                                                                                  |
| linear          | True when the colorspace is linear                                            | `boolean`                                                                                                                                                                                                      |
| flat            | True when no tonemapping is used                                              | `boolean`                                                                                                                                                                                                      |
| legacy          | Disables global color management via `THREE.ColorManagement`                  | `boolean`                                                                                                                                                                                                      |
| frameloop       | Render mode: always, demand, never                                            | `always`, `demand`, `never`                                                                                                                                                                                    |
| performance     | System regression                                                             | `{ current: number, min: number, max: number, debounce: number, regress: () => void }`                                                                                                                         |
| size            | Canvas size in pixels                                                         | `{ width: number, height: number, top: number, left: number, updateStyle?: boolean }`                                                                                                                          |
| viewport        | Viewport size in three.js units                                               | `{ width: number, height: number, initialDpr: number, dpr: number, factor: number, distance: number, aspect: number, getCurrentViewport: (camera?: Camera, target?: THREE.Vector3, size?: Size) => Viewport }` |
| xr              | XR interface, manages WebXR rendering                                         | `{ connect: () => void, disconnect: () => void }`                                                                                                                                                              |
| set             | Allows you to set any state property                                          | `(state: SetState<RootState>) => void`                                                                                                                                                                         |
| get             | Allows you to retrieve any state property non-reactively                      | `() => GetState<RootState>`                                                                                                                                                                                    |
| invalidate      | Request a new render, given that `frameloop === 'demand'`                     | `() => void`                                                                                                                                                                                                   |
| advance         | Advance one tick, given that `frameloop === 'never'`                          | `(timestamp: number, runGlobalEffects?: boolean) => void`                                                                                                                                                      |
| setSize         | Resize the canvas                                                             | `(width: number, height: number, updateStyle?: boolean, top?: number, left?: number) => void`                                                                                                                  |
| setDpr          | Set the pixel-ratio                                                           | `(dpr: number) => void`                                                                                                                                                                                        |
| setFrameloop    | Shortcut to set the current render mode                                       | `(frameloop?: 'always', 'demand', 'never') => void`                                                                                                                                                            |
| setEvents       | Shortcut to setting the event layer                                           | `(events: Partial<EventManager<any>>) => void`                                                                                                                                                                 |
| onPointerMissed | Response for pointer clicks that have missed a target                         | `() => void`                                                                                                                                                                                                   |
| events          | Pointer-event handling                                                        | `{ connected: TargetNode, handlers: Events, connect: (target: TargetNode) => void, disconnect: () => void }`                                                                                                   |

你也可以选择属性，这可以让你避免对那些只对特定内容感兴趣的组件进行不必要的重新渲染。Reactivity 并不包括更深层次的 three.js 内部结构!

```js
// Will only trigger re-render when the default camera is exchanged
const camera = useThree((state) => state.camera);
// Will only re-render on resize changes
const viewport = useThree((state) => state.viewport);
// ❌ You cannot expect reactivity from three.js internals!
const zoom = useThree((state) => state.camera.zoom);

function Foo() {
  const get = useThree((state) => state.get)
  ...
  get() // Get fresh state from anywhere you want

function Foo() {
  const set = useThree((state) => state.set)
  ...
  useEffect(() => {
    set({ camera: new THREE.OrthographicCamera(...) })
  }, [])
```

# useFrame

这个 Hook 允许你在每个渲染的帧上执行代码，比如运行特效、更新控件等等。你会收到状态（与 useThree 相同）和一个时钟 delta。你的回调函数将在一个帧被渲染之前被调用。当组件卸载时，它将自动从渲染循环中取消订阅。

```js
import { useFrame } from '@react-three/fiber'

function Foo() {
  useFrame((state, delta, xrFrame) => {
    // This function runs at the native refresh rate inside of a shared render-loop
  })
```

小心你在 useFrame 里面做的事情！你不应该在里面设置状态。你不应该在里面设置状态。你的计算应该是细小的，而且你应该注意在处理一般的循环时的所有已知的陷阱，比如重复使用变量等等。如果你需要更多的控制，你可以传递一个数字的 renderPriority 值。这将导致 React Three Fiber 完全禁用自动渲染。现在将由你负责渲染，这在你与 effect composers、heads-up displays 等一起工作时很有用。

```js
function Render() {
  // Takes over the render-loop, the user has the responsibility to render
  useFrame(({ gl, scene, camera }) => {
    gl.render(scene, camera)
  }, 1)

function RenderOnTop() {
  // This will execute *after* Render's useframe
  useFrame(({ gl, ... }) => {
    gl.render(...)
  }, 2)
```

回调将按照优先级升值的顺序执行（最低的在前，最高的在后。），类似于 DOM 的 Z-order。使用负指数不会接管渲染循环，但如果你真的必须在组件树上排列 useFrames 的顺序，那么它就会很有用。

```js
function A() {
  // This will execute first
  useFrame(() => ..., -2)

function B() {
  // This useFrame will execute *after* A's
  useFrame(() => ..., -1)
```

# useLoader

这个 Hook 加载 assets 并暂停，以方便回退和错误处理。它可以接受任何 three.js 加载器作为它的第一个参数。GLTFLoader, OBJLoader, TextureLoader, FontLoader, 等等。它是基于 React.Suspense 的，所以回退处理和错误处理发生在父级层面。

```js
import { Suspense } from "react";
import { useLoader } from "@react-three/fiber";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";

function Model() {
  const result = useLoader(GLTFLoader, "/model.glb");
  // You don't need to check for the presence of the result, when we're here
  // the result is guaranteed to be present since useLoader suspends the component
  return <primitive object={result.scene} />;
}

function App() {
  return (
    <Suspense fallback={<FallbackComponent /> /* or null */}>
      <Model />
    </Suspense>
  );
}
```

用 useLoader 加载的资产默认是缓存的。给出的 Url 作为缓存键。这允许你在组件树中的任何地方重新使用加载的数据。在突变或处理加载的资产时要非常小心，特别是当你打算重新使用它们时。如果你需要配置你的加载器，你可以提供一个回调作为第三个参数。

```js
import { DRACOLoader } from "three/examples/jsm/loaders/DRACOLoader";

useLoader(GLTFLoader, url, (loader) => {
  const dracoLoader = new DRACOLoader();
  dracoLoader.setDecoderPath("/draco-gltf/");
  loader.setDRACOLoader(dracoLoader);
});
```

它还可以并行地提出多个请求。

```js
const [bumpMap, specMap, normalMap] = useLoader(TextureLoader, [
  url1,
  url2,
  url2,
]);
```

你可以从你提供的作为第四个参数的回调中获得加载状态。不过可以考虑像 THREE.DefaultLoadingManager 这样的替代品，或者更好的是 Drei 的加载帮助器。

```js
useLoader(loader, url, extensions, (xhr) => {
  console.log((xhr.loaded / xhr.total) * 100 + "% loaded");
});
```

如果发现一个 result.scene prop，Hooks 将自动创建一个对象和材料集合：{ nodes, materials }。这让你可以有选择地建立不可变的场景图。你也可以专门改变数据，而不需要遍历它。GLTFJSX 特别依赖这些数据。

```js
const { nodes, material } = useLoader(GLTFLoader, url);
```

你可以在全局空间中预加载资产，这样模型就可以在组件树中安装之前预期地加载。

```js
useLoader.preload(GLTFLoader, "/model.glb" /* extensions */);
```

# useGraph

方便的钩子，可以从任何 Object3D 中创建一个记忆化的、命名的对象/材料集合。

```js
import { useLoader, useGraph } from "@react-three/fiber";

function Model(url) {
  const scene = useLoader(OBJLoader, url);
  const { nodes, materials } = useGraph(scene);
  return <mesh geometry={nodes.robot.geometry} material={materials.metal} />;
}
```
