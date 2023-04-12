# 从 WebGL 到 WebGPU，网页图形的全新时代

正在看这篇文章的你，是否也写过 WebGL？或者，是以 WebGL 作为自己的主要工作？十年来，我一直从事 WebGL 相关工作，切身体会到了 WebGL 强大但又弱小的双生像，但 WebGPU 的出现让我看到了曙光，我甚至认为——WebGPU 替代 WebGL 成为未来的网页图形技术已经是不可改变的事实。

看完接下来的内容，你将明白我为什么会有这样的观点，也将认识到从现在就开始学习 WebGPU 的必要性，最后，我还给出了一些学习路径和建议，希望能帮助你更快速地上车。另外，这次演讲的幻灯片也是用 WebGPU 写的，你可以在文末点击「阅读原文」找到幻灯片的代码和线上版。

# WebGL，明日黄花

有人会问，为什么又来一个 WebGPU，是 WebGL 不好用了吗？WebGL 好用还是不好用，这个问题十分复杂，我们先看一看 WebGL 的发展历史，然后再分析它在当前时代下遇到的瓶颈。

可能很多人都不知道 WebGL 最早的“始作俑者”是谁，书里也没有写。大概是 2006 年的时候，一个叫做 Vladimir Vukićević 的美籍塞尔维亚工程师，在即将到来的 HTML 的 Canvas 标签上做了一个个人项目，用 Canvas 标签实现了 OpenGL 的原型，他把这个项目叫做 Canvas3D。这个项目被他的雇主 Mozilla 和很多其他浏览器厂商注意到了，被认为很有前途，于是他们就开始继续往下做这件事情，于是就有了 WebGL。

## WebGL&OpenGL，好一对难兄难弟

在 2011 年的时候，WebGL 1.0 标准被正式推出，随后的故事就进入了一个尴尬的境地。因为 WebGL 1.0 推出之后，大家发现它还有很大的进步空间，于是工作组很快就开始着手制定 WebGL 2.0 标准。但足足过去五六年时间之后，WebGL 2.0 才在 2017 年被正式发布，同时也开启了自己的蹉跎岁月。

在一开始的时候，Google 和 Mozilla 都同步支持了 WebGL 2.0，但是你会发现这里面少了一个非常重要的 Player——Apple，它一直没有宣布对 WebGL 2.0 的支持，直到两个月之前，也就是今年的 9 月 20 号，Apple 才说我们开始支持 WebGL 2.0 了，但这个时候黄花菜都凉了。

所以说，WebGL 经历了一个非常悲催的发展阶段。

WebGL 现在已经很老了，它很老的原因不光是因为它存在的时间长，也是因为它的标准完全是继承自 OpenGL ES 的，而 OpenGL ES 的设计理念可以追溯到 1992 年，甚至更早的一些理念是从 1980 年代的 IRIS GL 时代传下来的，那个时候你们可能都没有出生。

这些古老的理念，WebGL 到现在还在使用，而这些理念其实已经非常不符合今天的 GPU 的工作原理了，然后就造成了一些问题。我们前端开发者用 WebGL 写起来很快乐，大家可以在 Three.js 的官网看到有非常多使用 WebGL 创造的美妙的网页，但是对于那些浏览器的开发者而言，他们就非常头疼，这给他们的工作带来了非常大的不便。

举一个例子，WebGL 至今不可以做并行计算，或者说它做并行计算非常麻烦。大家虽然可能没有做过，但应该也听说过，在今天的人工智能时代，我们要去训练模型，做各种神经网络，都是用 GPU 来进行计算的，但是 WebGL 不支持这种计算，这就很麻烦。曾经业界有公司想要给 WebGL 增加这个功能，但这件事就非常的困难。到底有多困难，我们等一会儿会讲到。

WebGL 过得已经够惨了，它的老大哥 OpenGL 还要更惨一点，这个标准现在基本上已经没有人使用了。在最早的时候，包含 WebGL 在内的 HTML5 为什么能够战胜 Flash？很重要的一个原因是 Apple 掌门人乔布斯的力挺，力挺各种 Open 的标准，他们认为这个是行业的未来。

例如当年在苹果手机上唯一支持的图形框架就是 OpenGL ES，所有早期的苹果设备上的游戏都依赖于 OpenGL ES（比如愤怒的小鸟、切水果）；但在乔布斯去世之后，Apple 就抛弃了 OpenGL，自己开发了全新的图形框架 Metal。

而 WebGL 的拥有者——Khronos Group，也逐渐淡化了 OpenGL 这一 WebGL 标准的的基础。你可能对 Khronos 不熟悉，前端开发一般比较熟悉的是 W3C、TC39。Khronos Group 这个组织是一个图形界的标准组织，WebGL 和 OpenGL 就是它旗下的标准。在抛弃 OpenGL 之后，他们全力打造了现在的明星产品 Vulkan。

所以，几乎现在所有的操作系统都不再把 OpenGL 作为首要支持了，Apple 的 Mac 系统甚至明确表示了这一点，他们所有的 OpenGL 应用都会转成 Metal 运行。

另外还有一点大家可能不知道，我们所写的任何一行 WebGL 代码，在浏览器底层实际上有 99% 的可能并不是由 OpenGL 绘制，而是通过 Angle 这个库转化成本地代码，也就是说，它在 Windows 电脑上是用 DirectX 绘制的，在 Apple 上是用 Metal 绘制的。

今天，OpenGL 已经不适用于高端图形领域，尤其是 AAA 游戏开发，它已经到了可以安享晚年的时候了。不过在其他的一些行业，比如低端和嵌入式图形领域，科研之类的，OpenGL 依旧在发光发热。而 OpenGL SC 也会继续服务于军工、航天、车机等安全关键行业。就好像虽然 WebGPU 会代替 WebGL 成为网页图形新标准，但是 WebGL 依然会继续存在一样，在一些特殊领域发光发热。

## 图形行业格局：从龙虎斗到三足鼎立

那么现在的图形行业是一个什么样的情况呢？

最早的时候，图形行业是 OpenGL 和 Direct3D 两者龙虎斗，现在，开发者有了更多的选择——DirectX 12、Vulkan、Metal 并列为三大现代图形框架，全面释放了 GPU 的可编程能力，让开发者可以最大限度地自由操控 GPU。

这里还有一个对比，做过 WebGL 的可能都知道 Blinn Phong 这些早期的传统材质，而当时基于物理渲染的 PBR 材质还被视为次世代高端技术，只有在 Xbox、PlayStation 上才可以用，但它现在已经是遍地开花，所有的 Three.js、Babylon.js 等等都是以 PBR 为主要标准材质的。

还有就是光线追踪技术，你所看到的那些优秀的电影的表现、电视特效都是由光线追踪技术来渲染生成的，这个技术对算力有极大的要求。

我可以举一个例子，《星际穿越》这个电影是由新西兰的维塔工作室负责特效制作的，其中的黑洞镜头每一帧需要渲染 100 小时，也就是说，你看到每秒钟的黑洞镜头，需要超过 100 天的渲染时间。而现在我们藉由 NVIDIA RTX 显卡的专门硬件处理单元甚至可以做到实时光线追踪。

再说一个变化，当年的 GPU 实时渲染还只能作为产品草稿图和预览图，因为它噪点非常多，但是随着基于深度学习的人工智能降噪技术的提出，GPU 渲染一夜翻身，直接迈步成为生产环境可用的可靠渲染方式之一。

![《古墓丽影 8》](https://assets.ng-tech.icu/item/20230407204704.png)

![《古墓丽影 9》](https://assets.ng-tech.icu/item/20230407204843.png)

所以说，图形行业在这几年的发展和我们前端一样都是非常迅猛的。我们举一个简单的例子，就是古墓丽影这款游戏。《古墓丽影 8》和《古墓丽影 9》只差一个版本，但是一个是 2008 年，一个是 2013 年，从它们身上完全可以看出图形发展的两个不同的阶段。从图上你可以看出，2008 年的《古墓丽影 8》的场景非常简单，也不够细致，光影效果也比较一般，尤其是劳拉，她身上的建模是非常生硬的，但是到了 2013 年，《古墓丽影 9》里的背景已经非常细致了，它的右上角还用了体积云的绘制技术，虽然从这张图中可能看不清劳拉的背影，但是她皮肤的质感、人物的动作已经和真人非常相近了，尤其是她的头发，玩游戏的可能都知道，被玩家称为“海飞丝”技术，它可以让每一根发丝随着物理的引擎的驱动来进行真实的摆动。

图形工业发展如此之快，WebGL 显然已经不再适合我们在未来的网页图形开发，所以一个新的标准 WebGPU 诞生了。

# WebGPU，网页图形的未来

WebGPU 的目的在于提供现代 3D 图形和计算能力，和 WebGL 不同首先在于它不再由 Khronos 这个图形界的标准组织拥有，而是回归到了我们前端程序员的快乐老家 W3C，由 GPU for the Web 社区工作组开发。第二个不同是，它不再继承或者完全仿制某一个已经实现的本地图形标准，而是参考了 Vulkan、Metal 和 D3D12 的 API 设计理念，对标这些图形框架研发了一个全新的跨平台的高性能图形接口。

## WebGPU 的诞生：大厂角力的结果

WebGPU 的诞生过程实际上就是大厂角力的一个过程。

2016 年，Google 发现 WebGL 存在一些问题，于是就提出了一个新的提案叫 WebGL Next，说我们要再做一个精确的图形 API。然后，其他的厂商也纷纷跟进，Mozilla、Apple、Opera 都提出了自己的概念。

这个时候，Apple 起名部的工作人员立了大功，他们向 W3C 提交了一个叫做 WebGPU 的提案，这个提案好不好咱们另说，但是 WebGPU 这个名字是非常好的，让人耳目一新，于是 W3C 决定采纳这个名字作为未来新标准的命名，并且成立工作组来做 WebGPU 的工作。

因为这个名字是 Apple 起的，所以最后只有 Apple 的提案进入了他们“gpuweb-proposals”的代码仓库，不过为了避免重名造成的误解和冲突，Apple 最初的那个提案的名字被改为了 WebMetal。

看到 W3C 接纳了 Apple 的提案，Mozilla 不甘心，转而又向 Khornos Group 提交了一个基于 Vulkan 的命名为 WebGL Next 的提案，但这已经是 WebGL 的最后一搏了。

这个时候，大家都很迷茫——我们是跟着 W3C 走还是跟着 Khornos 走呢？最后，浏览器厂商用脚投票，站到了 WebGPU 这边。2018 年的时候，Google Chrome 团队宣布开始着手 WebGPU 标准的实现工作，这也在事实上宣布了 WebGPU 的胜出和 WebGL 的终结——不会再有 WebGL 3.0 和 WebGL Next 了。

随后，WebGPU 标准进入了一个茁壮成长的阶段，因为 WebGL 让人们知道在网页上开发图形是可行的，可以说，WebGPU 标准是站在 WebGL 的肩膀上发展的，WebGL 给它的成长打好了基础。于是，工作组的人员在那几年中密切开会，制定了新的标准。到了今年的 9 月份，我们已经可以在 Chrome 和 Safari 上对 WebGPU 进行大规模测试了，你只需要填写申请表获取一个 Token，然后在 HTML 文件的标签中填入此 Token，Chrome 浏览器就会为此网页开启 WebGPU 支持。

根据 WebGPU 工作组的计划，他们准备在今年年底发布 WebGPU 1.0 标准，但是现在已经是 12 月了，显然留给工作组的时间不多了。

## WebGPU 到底是什么

那么 WebGPU 到底是一个什么东西？

首先，WebGPU 和 WebGL 不一样的是，WebGPU 是一个精确的图形 API。什么叫做精确？举一个简单例子，当你在 WebGL 里绘制一些东西的时候，你说 gl = canvas.getContext('webgl')，你获得了一个上下文，你可以在里面画东西，但这个上下文或者背后发生了什么？显卡是如何反应的？浏览器跟显卡是如何协同工作的？这些东西你都不知道。但是 WebGPU 不一样，它完全开放了整个显卡能力，你要向显卡发送命令去控制显卡，它不再是画东西的一个库，而是一个利用 GPU 的库。

第二，WebGPU 的设计标准的起点非常高，它的野心绝对不只是在网页上做图形。WebGPU 一开始就是和 Vulkan、Metal、Direct3D 12 等更高性能的本地图形标准对标的，意思是说我的 WebGPU 就像一个 HAL 硬件抽象层一样，我只要对应这套标准，未来不仅可以在网页运行，甚至也可以在嵌入式、在服务器运行，就像 WebAssembly 一样。WebAssembly 本意是在网页运行，但是现在在服务器上运行也有非常好的发展前途。WebGPU 也有这样的野心，它想把自己这个东西去做大，所以它的核心的关键词是 「跨平台的高性能图形标准」。

第三，WebCPU 终于开始支持 GPU Compute Shader，并且是把 GPU 通用计算作为首要支持。

第四，WebGPU 包含一个全新的专为 Web 设计的、人类可编写的着色器语言——WGSL（WebGPU Shading Language），这里我会稍微展开解释下为什么它要包含这个东西。我们传统的基于字符串形式的着色器代码，对于浏览器厂商来说是非常头疼的，如果你写过 GLSL，可能就知道它是一个类 C 的语言，它的编译器也像 C 一样，而每一个厂商的驱动都不一样，最终很难保持跨端的一致性。同时，人们发现，Vulkan 标准提出的 SPIR-V 的着色器标准，是一个非常好的基于汇编的一个二进制的着色器程序，所以 WebGPU 也是对标它的。

WebGPU 的标准里面就写的很明白，就是说我这里面着色器所有的东西都要一一对应于 SPIR-V 里的东西，每一个东西都要在 SPIR-V 里头找到一个相应的映射。那么有一个问题，既然我们完全对标 SPIR-V，那我们为什么不直接用 SPIR-V 呢？这是因为 Apple 跟前面提到的 Khronos，他们之间有一个关于知识产权上的官司，所以大家可以发现 Apple 一直在消极对待 Khronos 的各种各样的产品，所以在 WebGPU 工作组中，Apple 就明确发言我绝对不会在自己的标准中使用任何 Khronos 的技术，于是没有办法，工作组就只能重新设计了这样一个着色器语言。

最后，WebCPU 没有状态机的机制了，它是面向对象的编程，新增了很多的对象，增加了异步支持，并且改善了验证机制。

## WebGPU 与 WebGL 性能对比

![WebGL](https://assets.ng-tech.icu/item/20230407205317.png)

![WebGPU](https://assets.ng-tech.icu/item/20230407205332.png)

让我们看一下复杂场景的渲染性能，这个场景中有 1000 棵树，它们不是使用实例化绘制的，而是每一棵树都有一个 draw call，所以一个场景我要有 1000 多个 draw call。如果使用 WebGL 进行绘制的话，你可以看到在我的电脑上使用 2070 显卡只能跑到 21FPS，而且每一帧的 CPU 时间需要 44 毫秒，但是同样用 WebGPU 来处理，在我的电脑上可以跑到 123 帧，每一帧的 CPU 时间只有 0.1 毫秒，这个是 WebGPU 和 WebGL 最大最显著的性能上的差距。

```js
let gl = canvas.getContext("webgl");

gl.createShader(type);
gl.shaderSource(shader, sourceCode);
gl.compileShader(shader);
gl.createProgram();
gl.attachShader(program, shader);
gl.linkProgram(program);
gl.useProgram(program);
gl.createBuffer();
gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
gl.bufferData(gl.ARRAY_BUFFER, dataView, gl.STATIC_DRAW);
gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
gl.drawArrays(mode, 0, size);
```

另外就是一个代码上的差距，观察我们用 WebGL 原生 API 绘制的过程，你可以发现所有的东西的起点都在于 Canvas；然而这是一件很不可思议的事情，就是我即使不需要画什么东西，我也需要创建一个 Canvas 元素，这个操作对于我们这个前端可能是无感知的，但是对于浏览器开发者来说我要新建一个 DOM 元素，就要给它增加所有它需要有的东西，一旦 DOM 元素崩溃了，浏览器要处理所有这些事情，对于开发者而言后面的事情就会变得非常复杂。

```js
let adapter = await navigator.gpu.requestAdapter();
let device = await adapter.requestDevice();
let context = canvas.getContext('webgpu');
let context.configure({ ... });
let commandEncoder = device.createCommandEncoder();
let renderPassEncoder = commandEncoder.beginRenderPass(renderPassDescriptor);
let renderPipeline = await device.createRenderPipelineAsync(pipelineDescriptor);
renderPassEncoder.setPipeline(renderPipeline);
renderPassEncoder.drawIndexed(indexCount, 1, 0, 0, 0);
renderPassEncoder.endPass();
device.queue.submit([ commandEncoder.finish() ]);
```

但是 WebGPU 不是这样，WebGPU 的入口是 navigator.gpu，你可以从这里获取到一个显卡，再从显卡获取到一个设备，而中间的 Canvas 有没有是可选的。

如果你单纯只是想用显卡做一些事情，不想把它绘制在屏幕上，你完全可以不用新建 Canvas 元素，整个代码实例我们后面还会详细讲一下，所以我们这里就略过。

## 多进程的浏览器架构

![多进程浏览器](https://assets.ng-tech.icu/item/20230407205617.png)

WebGPU 除了对前端开发好之外，还对谁好呢？当然是浏览器的开发厂商，他们终于可以痛快地去写他们的代码了，这是因为现在的浏览器基本都是一个多线程的架构。大家开发的时候可能经常会打开任务管理器看资源消耗，你可以看到浏览器经常不是只有一个进程，而是有非常多的进程在跑着。但是现在的 Chrome 浏览器有一个缺点，它把所有的进程名都设定为同一个名字，所以你也不知道这些进程到底是干啥的。而新版在 Windows11 的 Edge 浏览器做了一个改变，它会标明每个进程的名字，告诉你每个进程是干啥的，你可以在这张图里看到有浏览器进程，有 GPU 进程，有处理崩溃的 Crashpad 进程等等。我相信 Chrome 可能也会改一下。

![多进程浏览器](https://assets.ng-tech.icu/item/20230407205646.png)

这是整个浏览器的一个大概框架图，比如我开了 4 个标签页，整个浏览器是跑在 browser 进程里的，每个标签页都有自己的渲染进程。如果你想要安装一些扩展，比如说去广告的扩展，这些扩展会跑在扩展进程里。同时你看到这有一个广告，这个广告实际上是跑在一个独立的渲染进程里的，这主要是基于安全问题而考虑的。然后，中间视频需要编辑，可能要跑一个插件，那插件又有自己的进程，最左边就是我们关心的地方，这里有很多的视频，这些视频可能是 MP4 格式 x264 编码的，浏览器可能要借助显卡驱动来进行硬件解码，这些东西都会跑到 GPU 的进程里面去。

所以说当你在 WebGPU 中，在 JavaScript 里新建了一个 ArrayBuffer，你想把它最后传到 GPU 里是要过好几层关卡的。首先在内容进程中的 CPU 读到了 ArrayBuffer，要把它放到共享内存里，通过共享内存让 GPU 进程的 CPU 可以看到它，GPU 进程中的 CPU 再把它放到可以映射到 GPU 的缓存中，最后 GPU 再去从映射缓存里拷贝到自己的显存中，然后再去进行后续的操作。

因此，实际上在 WebGPU 的编程模型中，有两条时间线，就像平行宇宙、平行时空一样，一条时间线是内容时间线，一条时间线是 GPU 设备的时间线。比如说当你在内容进程，也就是你的 JavaScript 代码里写 create buffer 的时候，实际上这个 buffer 还没有被 GPU 建立，它只是通知了 GPU 说我要创建一个 buffer，顺利的情况下你可以这样去往下做，但是如果错误的情况下就比较麻烦了。因为 GPU 报错的时候，你的 CPU 是不知道的，你并不知道 buffer 创建失败了，但是好在 WebGPU 给我们提供了非常好的错误处理机制，让你在开发、调试，包括产品上线之后的埋点遥测阶段都可以非常清楚地知道客户端发生了什么事情。

## 万物皆 Promise

其实，你可以把 WebGPU 开发理解为“万物皆 Promise”，理解成面向未来的编程，就是所有都是 Future，每一个 WebGPU 对象都是一个 Promise，都是异步过程，相应操作都被外包到刚才所说的 GPU 进程中，然后在那实际上才是同步的。还有就是编程的时候一定要清楚地意识到每一个对象代表的含义，当你在 GPU 中创建了一个 buffer，它可能只占你的 CPU 内存中的 150 字节，但实际上它可能在 GPU 中占了一个 GB 的显存，这种事情也是有可能发生的。

还有一个问题就是通过这样的一个映射，我们不再在 CPU 端做验证，取而代之的是，所有的验证都会放到 GPU 端去做，这样做的好处就是提升了运行效率。WebGL 之所以那么慢，就是因为 WebGL 的验证机制非常差劲，当然，这也是因为历史原因造成的。

所以说在用 WebGPU 编程的时候，你的脑子可能会自我精神分裂成两个时间线，去注意两个时间线里不同的进程，同时结合你自己的前端的任务控制机制，包括异步、宏任务、微任务等等，包括你使用的前端框架的生命周期来做编程开发。

## WebGPU 开发体验，好

下面我们来讲一下 WebGPU 的开发体验。

WebGPU 的开发体验还是非常不错的，我在这次演讲中用到的 PPT 的背景就是用 WebGPU 写的着色器效果，这个效果其实是非常复杂的，而且现在 WebGPU 没有多线程，我只是把它跑在主线程上，但是看起来渲染性能也还挺好。

简单来说首先就是大量的步方法，就像刚才说的你需要掌握 Promise；第二它有很好的 TypeScript 支持，官方提供类型定义文件；另外它有一个全新 WGSL 语言，你需要去学习，这个语言的语法非常怪异，而且现在显然还是有缺陷的，社区和工作组每天都在提新的设计修改意见，它是一个有点类似于 Rust 和 TypeScript 的缝合怪，如果你的项目有大量的以前的着色器代码，不想把它翻译成 WGSL，你也可以回滚到 GLSL，比如，你可以预先把它编译成刚才所说的符合 SPIRV 的二进制代码；最后就是你可以尽情使用所有新的浏览器特性，因为它会跑在未来的浏览器里面。

```rs
[[block]]
struct Uniforms {
    [[size(64)]]uPMatrix: mat4x4<f32>;
    [[size(64)]]uMVMatrix: mat4x4<f32>;
};
[[group(0), binding(0)]]
var<uniform> uniforms: Uniforms;
[[stage(vertex)]]
fn main (
    [[location(0)]] aVertexPosition : vec3<f32>
) -> [[builtin(position)]] vec4<f32> {
    return uniforms.uPMatrix * uniforms.uMVMatrix * vec4<f32>(aVertexPosition, 1.0);
}
```

上面这个就是 WGSL 语言写的一个很简单的着色器，你可以看到它的变量名称后面跟了冒号，然后再是类型，这点很像 TypeScript，并且出现了泛型，而它下面的这个函数 fn，一个单箭头指向的语法也很像 Rust，所以说它就是这么一个缝合怪，它现在的语言的标准也在不断地修改。

```js
// 获取硬件设备
let adapter = await navigator.gpu.requestAdapter();
let device = await adapter.requestDevice();
// 可以用 Canvas，也可以不用 Canvas，还可以用很多 Canvas；用的话就把 Canvas 与设备相连
let context = canvas.getContext( 'webgpu' );
let context.configure( { ... });
// 创建命令编码器，所有 GPU 指令都是通过它发给 GPU 的
let commandEncoder = device.createCommandEncoder();

// 创建渲染通道、渲染管线、着色器……等等所有你想做的 GPU 指令
let renderPassEncoder = commandEncoder.beginRenderPass( renderPassDescriptor );
let renderPipeline = await device.createRenderPipelineAsync( renderPipelineDescriptor );
renderPassEncoder.setPipeline( renderPipeline );
renderPassEncoder.drawIndexed( indexCount, 1, 0, 0, 0 );
renderPassEncoder.endPass();
// 结束命令编码器并发送到 GPU 设备的指令队列中
device.queue.submit( [ commandEncoder.finish() ] );
```

下面，我们简单讲一下 WebGPU 的整个绘制过程。首先就是你要获取一个硬件设备，之前在 WebGL 中开发者对硬件设备的获取其实是模糊的，你也不太需要关心用户使用的什么显卡，但是现在你可以精确地知道用户安装的是什么显卡。

另外就是 Canvas，以前所有的 WebGL 接口都是绑定在上下文里，但是现在上下文只是负责一个类似于交换链的作用，告诉 GPU 最后画到哪儿。如果你的应用不需要绘制在屏幕上，你完全不需要新建 Canvas。最后一个很重要的概念是命令编码器，command encoder，它的意思是说你可以把你想让 GPU 执行所有的命令都压到命令编码器里面，让命令编码器把所有的这些命令编在一起，然后存成命令缓存，然后再发送到 GPU 里面。下面还有一些很重要的概念，就是跟绘制相关的，包括渲染通道，然后渲染管线等等这些。

## GPU 通用计算

接下来我们讲一下通用计算。这里有一个故事非常有意思，英特尔公司曾经想给 WebGL 增加通用计算能力，但是当这个被称之为 WebGL 2.0 Compute 的标准被提出之后，只有 Chrome 这一个浏览器团队实现了这个标准，而且他们实现起来也相当困难，其他团队根本就没有去实现这个标准。

所以此后，英特尔公司就决定停止开发 WebGL 2.0 Compute 标准，并把注意力转移到 WebGPU 上，Google 也从 Chrome 里移除了 WebGL 的 Compute 支持，所以说这个标准现在已经是名存实亡了。

另外说一句，英特尔公司负责 WebGL Compute，包括现在 WebGPU Compute 部分，很多都是我们中国的工程师。希望能有更多的中国公司参与到网页图形标准的制定中。

在这里，我们举一个简单例子，最简单的排序，我们跟 CPU 排序做一下对比。CPU 排序我们就用 JavaScript 自带的 Array.sort()，而右边的排序我们用的是双调排序，这是一种可以用 GPU 来做并行计算的排序方法。我们现在有一个数组，这个数组的长度是 2 的 23 次方，也就是数组里有 800 多万个浮点数。现在，我们要对这个数组进行排序。

![排序对比](https://assets.ng-tech.icu/item/20230407210351.png)

当我点了排序按钮之后，整个主线程的渲染都已经被卡死了，阻塞了，都停在这儿了，最终我们把它排序完花了 10455 毫秒。现在，我们再来看一下 GPU 的排序，大家不要看绝对数值，要看相对数值，GPU 只用了 394 毫秒，它的排序要比整个的 CPU 排序快非常多。未来 GPU 通用计算会是一个非常关键的前端领域，像 TensorFlow.js 等基于做人工智能方向的一些东西，会用它去做非常多的事情，所以它是非常好的一个能力。

## 网页图形的未来

最后我们来说一下网页图形学的未来。

WebGPU 的未来会变成什么样呢？首先，在很快到来的未来，也就是明年，WebGPU 工作组的主要工作方向是多线程，他们要为 WebGPU 增加多线程能力。我们知道现在在 WebGL 中可以用 OffscreenCanvas 实现多线程，但是 Apple Safari 并不支持这个特性，所以实际使用起来会遇到巨大的兼容问题。

还有一个问题，即使使用 OffscreenCanvas，它的多线程操作也是比较局限的，因为你需要把整个 Canvas 的操作全部都转移到唯一的一个 Worker 里实现。但是 WebGPU 的多线程相对就非常灵活，你可以把一个 Buffer、一个 GPU 对象简单地通过 postMessage() 方法发送到任何一个 worker，这些 worker 只要在时间线上没有互斥的操作，它们都可以在不同时间不同的 worker 里面去对同一个或者多个 GPU 对象进行操作。所以它的多线程开发体验要比 WebGL 要好很多。

那在比较远的未来呢？比如说实时光线追踪，这个不是我说的，而是工作组说的，工作组希望在未来他们能够直接调用本地图形，例如 DirectX 12，我们能调用本地图形能力来进行一些网页上的绘制，比如说实时光线追踪，这两张图片是当时微软 DXR 发布的时候的图片，它们不是用 CPU 离线渲染的那种光线追踪渲染图片，而是一个实时渲染的场景的截图，其中使用了实时光线追踪能力。

![实时光线追踪](https://assets.ng-tech.icu/item/20230407210619.png)

大家可以设想一下，如果这种质量的实时渲染图形出现在了网页上，我们的网页的生态会变得更加丰富多彩。
