# Canvas

Canvas 对象是你开始定义你的 React Three Fiber Scene 的地方。

```js
import React from "react";
import { Canvas } from "@react-three/fiber";

const App = () => (
  <Canvas>
    <pointLight position={[10, 10, 10]} />
    <mesh>
      <sphereGeometry />
      <meshStandardMaterial color="hotpink" />
    </mesh>
  </Canvas>
);
```

| PROP            | DESCRIPTION                                                                                                                                       | DEFAULT                                                           |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------- |
| children        | three.js JSX elements or regular components                                                                                                       |                                                                   |
| gl              | Props that go into the default renderer, or your own renderer. Also accepts a synchronous callback like `gl={canvas => new Renderer({ canvas })}` | `{}`                                                              |
| camera          | Props that go into the default camera, or your own `THREE.Camera`                                                                                 | `{ fov: 75, near: 0.1, far: 1000, position: [0, 0, 5] }`          |
| shadows         | Props that go into `gl.shadowMap`, can also be set true for `PCFsoft`                                                                             | `false`                                                           |
| raycaster       | Props that go into the default raycaster                                                                                                          | `{}`                                                              |
| frameloop       | Render mode: always, demand, never                                                                                                                | `always`                                                          |
| resize          | Resize config, see react-use-measure's options                                                                                                    | `{ scroll: true, debounce: { scroll: 50, resize: 0 } }`           |
| orthographic    | Creates an orthographic camera                                                                                                                    | `false`                                                           |
| dpr             | Pixel-ratio, use `window.devicePixelRatio`, or automatic: [min, max]                                                                              | `[1, 2]`                                                          |
| legacy          | Enables THREE.ColorManagement.legacyMode in three r139 or later                                                                                   | `false`                                                           |
| linear          | Switch off automatic sRGB encoding and gamma correction                                                                                           | `false`                                                           |
| events          | Configuration for the event manager, as a function of state                                                                                       | `import { events } from "@react-three/fiber"`                     |
| eventSource     | The source where events are being subscribed to, HTMLElement                                                                                      | `React.MutableRefObject<HTMLElement>`, `gl.domElement.parentNode` |
| eventPrefix     | The event prefix that is cast into canvas pointer x/y events                                                                                      | `offset`                                                          |
| flat            | Use `THREE.NoToneMapping` instead of `THREE.ACESFilmicToneMapping`                                                                                | `false`                                                           |
| onCreated       | Callback after the canvas has rendered (but not yet committed)                                                                                    | `(state) => {}`                                                   |
| onPointerMissed | Response for pointer clicks that have missed any target                                                                                           | `(event) => {}`                                                   |

# Custom Canvas

R3F 可以渲染到一个根，类似于 react-dom 和所有其他 React 渲染器的工作方式。这允许你减少 react-dom (~40kb)、react-use-measure (~3kb)，如果你不需要它们，还可以减少 pointer-events (~7kb)（否则你需要明确导入事件并将它们添加到配置中）。根的选项和属性与 Canvas 相同，但你要负责调整它的大小。它需要一个现有的 DOM <canvas> 对象，并将其渲染进去。

## CreateRoot

创建一个针对画布的根，渲染 JSX。

```js
import * as THREE from "three";
import { extend, createRoot, events } from "@react-three/fiber";

// Register the THREE namespace as native JSX elements.
// See below for notes on tree-shaking
extend(THREE);

// Create a react root
const root = createRoot(document.querySelector("canvas"));

// Configure the root, inject events optionally, set camera, etc
root.configure({ events, camera: { position: [0, 0, 50] } });

// createRoot by design is not responsive, you have to take care of resize yourself
window.addEventListener("resize", () => {
  root.configure({
    size: { width: window.innerWidth, height: window.innerHeight },
  });
});

// Trigger resize
window.dispatchEvent(new Event("resize"));

// Render entry point
root.render(<App />);

// Unmount and dispose of memory
// root.unmount()
```

# Tree-shaking

v8 的新功能是，底层调和器不再自动拉入 THREE 命名空间。这使得一个细化的目录可以通过扩展 API 实现树形晃动。

```js
import { extend, createRoot } from "@react-three/fiber";
import { Mesh, BoxGeometry, MeshStandardMaterial } from "three";

extend({ Mesh, BoxGeometry, MeshStandardMaterial });

createRoot(canvas).render(
  <>
    <mesh>
      <boxGeometry />
      <meshStandardMaterial />
    </mesh>
  </>
);
```

有一个官方的 babel 插件会自动为你做这个。

```js
// In:

import { createRoot } from "@react-three/fiber";

createRoot(canvasNode).render(
  <mesh>
    <boxGeometry />
    <meshStandardMaterial />
  </mesh>
);

// Out:

import { createRoot, extend } from "@react-three/fiber";
import {
  Mesh as _Mesh,
  BoxGeometry as _BoxGeometry,
  MeshStandardMaterial as _MeshStandardMaterial,
} from "three";

extend({
  Mesh: _Mesh,
  BoxGeometry: _BoxGeometry,
  MeshStandardMaterial: _MeshStandardMaterial,
});

createRoot(canvasNode).render(
  <mesh>
    <boxGeometry />
    <meshStandardMaterial />
  </mesh>
);
```
