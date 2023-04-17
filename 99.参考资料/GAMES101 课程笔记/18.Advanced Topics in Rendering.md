## 18.Advanced Topics in Rendering

### 18.1 Advanced Light Transport

![img](https://assets.ng-tech.icu/item/202304172222201.jpg)

无偏光线传播方法：BDPT、MLT

有偏光线传播方法：光子映射、VCM

实时路径追踪方法

![img](https://assets.ng-tech.icu/item/202304172222231.jpg)

有偏性、一致性说明

### 18.2 Bidirectional Path Tracing

![img](https://assets.ng-tech.icu/item/202304172222249.jpg)

从光源和摄像机分别出一些光线并连接在一起

![img](https://assets.ng-tech.icu/item/202304172222268.jpg)

对于主要由间接光照照亮的场景而言，双向路径追踪的效率会高于单向路径追踪

### 18.3 Metropolis Light Transport

![img](https://assets.ng-tech.icu/item/202304172222283.jpg)

Metropolis 是人名而非大都市

基于马尔可夫链的采样方式，由上一个采样样本生成下一个新样本，进行估计函数值。

这种方式可以使采样的分布和实际 pdf 的分布一致，保证方差比较小，收敛效率比较高。

![img](https://assets.ng-tech.icu/item/202304172222297.jpg)

对于复杂的场景渲染效果很好。

![img](https://assets.ng-tech.icu/item/202304172222310.jpg)

但这个方法也有坏处，主要是不好估计什么时候会没有噪声。

并且，各个点的收敛率不同，导致图可能比较脏，以至于还不能应用于动画

### 18.4 Photon Mapping

![img](https://assets.ng-tech.icu/item/202304172222324.jpg)

光子映射方法，非常适合于渲染光线聚焦产生特殊图案（caustics 现象）的场景

![img](https://assets.ng-tech.icu/item/202304172222340.jpg)

一种实现方式是分成两步：

1. 先打出光子，并停在漫反射物体上
2. 第二步从视角出发打到表面上

![img](https://assets.ng-tech.icu/item/202304172222358.jpg)

对局部进行密度估计，值越高则越亮

![img](https://assets.ng-tech.icu/item/202304172222372.jpg)

但这种方法的关键是取光子数量，数量太少会噪声，数量太大会糊

仅当光子数量非常多之后才能接近正确结果。

所以是有偏但是一致的方法

![img](https://assets.ng-tech.icu/item/202304172222386.jpg)

渲染中直观地理解有偏和一致的方法是：

1. 如果糊则有偏
2. 如果无限时不糊则一致

### 18.5 Vertex Connection and Merging

![img](https://assets.ng-tech.icu/item/202304172222400.jpg)

结合了光子映射和双向路径追踪的思路，不让任何一个路径被浪费，最后表现也不错

### 18.6 Instant Radiosity

![img](https://assets.ng-tech.icu/item/202304172222414.jpg)

将被照亮的表面也当作光源，并取上面的一些点作为虚拟点光源

![img](https://assets.ng-tech.icu/item/202304172222429.jpg)

在有的场景中效果不错

但偶尔会有亮点，主要因为面积估计时偶尔会以一个极近的距离，导致最后除下来亮度非常高

### 18.7 Advanced Appearance Modeling:Intoduction

![img](https://assets.ng-tech.icu/item/202304172222442.jpg)

对一些材质用真实微观建模的方式表现和渲染

### 18.8 Participating Media

![img](https://assets.ng-tech.icu/item/202304172222456.jpg)

比如对于散射介质：雾

![img](https://assets.ng-tech.icu/item/202304172222477.jpg)

![img](https://assets.ng-tech.icu/item/202304172222492.jpg)

用一个相位函数来表达其散射方式

![img](https://assets.ng-tech.icu/item/202304172222506.jpg)

光线和体积进行作用最后到达眼睛

![img](https://assets.ng-tech.icu/item/202304172222521.jpg)

散射介质超能特工队中的应用

![img](https://assets.ng-tech.icu/item/202304172222536.jpg)

散射介质在刺客信条中的应用

![img](https://assets.ng-tech.icu/item/202304172222552.jpg)

即使是巧克力也会有一些光线会进入体积内再穿透出来

人的皮肤也是如此

### 18.9 Participating Media:Hair

![img](https://assets.ng-tech.icu/item/202304172222566.jpg)

头发也是这样的例子

![img](https://assets.ng-tech.icu/item/202304172222582.jpg)

可以仅仅把头发当成一个圆柱并只考虑一次反射

![img](https://assets.ng-tech.icu/item/202304172222596.jpg)

但这样得到的效果并不算非常好

![img](https://assets.ng-tech.icu/item/202304172222610.jpg)

而当进一步把头发当成一个可被穿透的圆柱

![img](https://assets.ng-tech.icu/item/202304172222626.jpg)

考虑直接反射(R)，折射再折射(TT)，折射反射再折射(TRT)三种光线

![img](https://assets.ng-tech.icu/item/202304172222640.jpg)

便能得到非常不错的结果

![img](https://assets.ng-tech.icu/item/202304172222654.jpg)

最终幻想里，头发建模的应用

![img](https://assets.ng-tech.icu/item/202304172222669.jpg)

疯狂动物城中头发建模的应用

![img](https://assets.ng-tech.icu/item/202304172222684.jpg)

事实上，人类的头发和动物的毛发也是不同的，直接套用也会使结果显得不那么自然

![img](https://assets.ng-tech.icu/item/202304172222698.jpg)

这是由于人类和动物毛发中 Medulla 占比不一致导致的

![img](https://assets.ng-tech.icu/item/202304172222719.jpg)

一个改变 Medulla 得到不同结果的例子。可见微观性质差异有时候对宏观的影响也是非常显著的

![img](https://assets.ng-tech.icu/item/202304172222734.jpg)

考虑 Medulla 后对头发渲染的影响

![img](https://assets.ng-tech.icu/item/202304172222748.jpg)

用双圆柱模拟含 Medulla 的头发模型

![img](https://assets.ng-tech.icu/item/202304172222762.jpg)

几种光线作用后的效果

![img](https://assets.ng-tech.icu/item/202304172222776.jpg)

巨量的建模细节和采样率

![img](https://assets.ng-tech.icu/item/202304172222791.jpg)

双层圆柱毛发模型在猩球崛起中的应用

![img](https://assets.ng-tech.icu/item/202304172222805.jpg)

双层圆柱毛发模型在狮子王中的应用

### 18.10 Granular Material

![img](https://assets.ng-tech.icu/item/202304172222821.jpg)

Granular Material 的一些例子

![img](https://assets.ng-tech.icu/item/202304172222836.jpg)

![img](https://assets.ng-tech.icu/item/202304172222850.jpg)

Pixar 应用 Granular Material 的动画短片

### 18.11 Translucent Material

![img](https://assets.ng-tech.icu/item/202304172222864.jpg)

玉

![img](https://assets.ng-tech.icu/item/202304172222880.jpg)

次表面反射

![img](https://assets.ng-tech.icu/item/202304172222895.jpg)

描述次表面反射需要对渲染方程增加额外一个维度

![img](https://assets.ng-tech.icu/item/202304172222910.jpg)

Dipole 有一种模拟的近似方案是在表面下方加入一个光源，模拟次表面反射的效果

![img](https://assets.ng-tech.icu/item/202304172222925.jpg)

仅用表面反射表现大理石

![img](https://assets.ng-tech.icu/item/202304172222939.jpg)

加入次表面反射后的大理石

![img](https://assets.ng-tech.icu/item/202304172222954.jpg)

是否有考虑次表面反射的皮肤效果对比

![img](https://assets.ng-tech.icu/item/202304172222970.jpg)

BSSRDF 渲染出的三个人物，非常接近真实照片

### 18.12 Cloth

![img](https://assets.ng-tech.icu/item/202304172222984.jpg)

理解布料需要从其层级结构说起

首先由纤维(Fibers) 相互缠绕，形成股(Ply)

再由股(Ply)相互缠绕，形成线(Yarn)

最后线再通过不同的纺织方式，最后得到布料

![img](https://assets.ng-tech.icu/item/202304172222999.jpg)

各种不同的编织方式会得到不同的布料效果

![img](https://assets.ng-tech.icu/item/202304172222014.jpg)

当然，也可以把布料当作一个表面取渲染。但效果经常是有限的。

![img](https://assets.ng-tech.icu/item/202304172222029.jpg)

所以一种更复杂但表现效果好的方式是真实地把布料建模成有体积有纺织方式的空间物体，再进行渲染，可以得到非常好的效果。

![img](https://assets.ng-tech.icu/item/202304172222044.jpg)

甚至把纤维细节都给建模出来进行渲染

![img](https://assets.ng-tech.icu/item/202304172222059.jpg)

布料在电影中的一些应用

### 18.13 Detailed Appearance

![img](https://assets.ng-tech.icu/item/202304172222080.jpg)

渲染出的车和鼠标都略有不真实的感觉

![img](https://assets.ng-tech.icu/item/202304172222098.jpg)

主要是由于现实中的这些物体都不会太完美，表面应有划痕等等

![img](https://assets.ng-tech.icu/item/202304172222114.jpg)

没有细节的水壶

![img](https://assets.ng-tech.icu/item/202304172222130.jpg)

对比有细节的水壶

![img](https://assets.ng-tech.icu/item/202304172222146.jpg)

统计学上的正态分布和实际的正态分布是有区别的

![img](https://assets.ng-tech.icu/item/202304172222162.jpg)

可以加入噪声函数去影响表面

![img](https://assets.ng-tech.icu/item/202304172222177.jpg)

当然，要达到那种细节刻画度，会非常难以渲染

![img](https://assets.ng-tech.icu/item/202304172222193.jpg)

并且也主要难在有效采样

![img](https://assets.ng-tech.icu/item/202304172222209.jpg)

一种优化方式是把对应反射区域的法线分布给算出来，作为近似

![img](https://assets.ng-tech.icu/item/202304172222225.jpg)

不同尺度下，这个近似的差异有可能比较大，尺度越大通常越平滑，尺度越小通常越有特征

![img](https://assets.ng-tech.icu/item/202304172222241.jpg)

一些特殊的发现贴图采样后分布也会呈现不同的性质

![img](https://assets.ng-tech.icu/item/202304172222257.jpg)

这种算法线分布方法进行渲染的一些应用

![img](https://assets.ng-tech.icu/item/202304172222274.jpg)

![img](https://assets.ng-tech.icu/item/202304172222293.jpg)

### 18.14 Wave Optics

![img](https://assets.ng-tech.icu/item/202304172222309.jpg)

当对于微观时，如果进一步考虑光波的性质则会出现一些新的问题，比如光波会衍射等等

![img](https://assets.ng-tech.icu/item/202304172222326.jpg)

比如照一个拉丝过的金属表面，会看见有很多颜色

![img](https://assets.ng-tech.icu/item/202304172222343.jpg)

如 Macbook 放大后也是非白色，会有很多彩色的点

![img](https://assets.ng-tech.icu/item/202304172222359.jpg)

要处理的话需要考虑光的波动方程，并在复数域上积分

![img](https://assets.ng-tech.icu/item/202304172222377.jpg)

非常复杂，但一旦做出来，能够得到很接近照片的效果

![img](https://assets.ng-tech.icu/item/202304172222393.jpg)

放大看

### 18.15 Procedural Appearance

![img](https://assets.ng-tech.icu/item/202304172222411.jpg)

用噪声函数去随用随取地表达空间中任一一点的纹理参数

![img](https://assets.ng-tech.icu/item/202304172222429.jpg)

噪声函数生成纹理的实例
