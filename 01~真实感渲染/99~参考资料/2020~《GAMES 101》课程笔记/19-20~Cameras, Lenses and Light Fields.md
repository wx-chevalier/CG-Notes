## 19.Cameras,Lenses and Light Fields

### 19.1 Camera

![img](https://assets.ng-tech.icu/item/202304172225547.jpg)

相机或眼睛用类似凸透镜的成像本质和小孔类似，但相比于小孔成像，透镜能聚焦更多光子

![img](https://assets.ng-tech.icu/item/202304172225575.jpg)

相机的感光元件记录的是 Irradiance，因此必须要有小孔或者透镜，否则会直接糊掉

![img](https://assets.ng-tech.icu/item/202304172225592.jpg)

小孔成像虽然光子少但是效果也不一定差

### 19.2 Field of View

![img](https://assets.ng-tech.icu/item/202304172225613.jpg)

同样大小的感光片情况下，焦距越小，视角越大

同样的焦距下，感光片越大视角越大

![img](https://assets.ng-tech.icu/item/202304172225629.jpg)

相机焦距和视角的关系（且统一使用 36\*24mm 的底片为计算标准，非标准底片需要相应折算）

![img](https://assets.ng-tech.icu/item/202304172225648.jpg)

这是调焦距可以调整画面“远近”的原因，但并非真实的“远近”，和把相机放近后拍照得到的透视关系有区别

![img](https://assets.ng-tech.icu/item/202304172225663.jpg)

感光器的大小区别

![img](https://assets.ng-tech.icu/item/202304172225676.jpg)

### 19.3 Exposure

![img](https://assets.ng-tech.icu/item/202304172225689.jpg)

显然，每个感光元件在一次曝光情况下接受的能量=时间\*irradiance

![img](https://assets.ng-tech.icu/item/202304172225702.jpg)

通常有三种方式可以调整曝光度：光圈大小、快门速度、ISO

![img](https://assets.ng-tech.icu/item/202304172225715.jpg)

用这三种方式调整会有各自的特征和利弊

![img](https://assets.ng-tech.icu/item/202304172225728.jpg)

ISO 由于是直接对数据进行放大，自然也会放大噪声。所以通常不倾向采用这种调整方式

![img](https://assets.ng-tech.icu/item/202304172225746.jpg)

调整光圈大小，且通常用 FN 来表示，其中 N 和光圈直径呈反比

调整光圈还会影响景深效果：光圈越小精深效果越弱。恰如近视眼虚眼看东西会清晰一些的原理

![img](https://assets.ng-tech.icu/item/202304172225759.jpg)

快门速度可能导致运动模糊

![img](https://assets.ng-tech.icu/item/202304172225773.jpg)

但运动模糊并不一定不好，很多时候反而是有更好，比如电影和游戏

![img](https://assets.ng-tech.icu/item/202304172225787.jpg)

快门由于是机械式，开关有一个过程，所以拍摄高速物体时可能产生畸变

![img](https://assets.ng-tech.icu/item/202304172225800.jpg)

为达到相同的曝光度，在不调整 ISO 的情况下需要相反地调整快门速度和光圈

所以可能要么牺牲一些景深，要么产生一些运动模糊，需要在这两者间根据照片目标效果进行平衡取舍

### 19.4 Fast and Slow Photography

![img](https://assets.ng-tech.icu/item/202304172225813.jpg)

极高的快门速度，于是一般需要配合极大的光圈或者高 ISO

![img](https://assets.ng-tech.icu/item/202304172225827.jpg)

长曝光效果

### 19.5 Thin Lens Approximation

![img](https://assets.ng-tech.icu/item/202304172225840.jpg)

在实际工业界，由于很多场景下空间不可能达到焦距要求的长度，通常使用多个镜片组合模拟出单凸透镜的效果。

![img](https://assets.ng-tech.icu/item/202304172225853.jpg)

事实上很多情况下镜片聚焦也不在一个点上

![img](https://assets.ng-tech.icu/item/202304172225865.jpg)

但我们通常只考虑最理想的透镜

### 19.6 Defocus Blur

![img](https://assets.ng-tech.icu/item/202304172225878.jpg)

失焦模糊的原理。并由此产生景深

![img](https://assets.ng-tech.icu/item/202304172225890.jpg)

![img](https://assets.ng-tech.icu/item/202304172225903.jpg)

光圈大小对于景深的影响

### 19.7 Ray Tracing Ideal Thin Lenses

![img](https://assets.ng-tech.icu/item/202304172225916.jpg)

由此在渲染中也可以根据这样的性质，主动建模出一个透镜和感光片（用以代替普通光线追踪的小孔成像模型）

![img](https://assets.ng-tech.icu/item/202304172225929.jpg)

并渲染出带景深效果的渲染图

![img](https://assets.ng-tech.icu/item/202304172225942.jpg)

由于实际的相机是有像素是离散的，可以如上考虑一个像素大小的景深模糊情况。

## 20.Color and Perception

### 20.1 Light Field

![img](https://assets.ng-tech.icu/item/202304172225956.jpg)

我们看到场景是因为场景有光发射向我们的眼睛

![img](https://assets.ng-tech.icu/item/202304172225969.jpg)

但如果一个屏幕能够模拟屏幕后方所有光矢，则理应让我们无法分辨真假，真裸眼 3D

![img](https://assets.ng-tech.icu/item/202304172225983.jpg)

记录一个点在一个时刻的广场，需要三个参数：

1. 两维记录视角
2. 一维记录波长

最后用函数记录这个视角下这个波长的光的能量

![img](https://assets.ng-tech.icu/item/202304172225000.jpg)

如果要记录全时全局的广场，则需要额外再增加一维时间，和三维坐标，一共七维进行记录

![img](https://assets.ng-tech.icu/item/202304172225013.jpg)

有了它我们可以重建任意画面

![img](https://assets.ng-tech.icu/item/202304172225030.jpg)

如果对于一个有限的区域，则只需要一个盒子，和盒子上每一点的光场信息即可复刻

![img](https://assets.ng-tech.icu/item/202304172225043.jpg)

为此一种痛常的做法是用两个平面，记录单平面光场，不考虑时间和光波长的话，刚好是 4 维

![img](https://assets.ng-tech.icu/item/202304172225058.jpg)

这是一个光场采样的实例

![img](https://assets.ng-tech.icu/item/202304172225072.jpg)

斯坦福的光场采集阵列

![img](https://assets.ng-tech.icu/item/202304172225086.jpg)

生物的复眼，本质也是一个光场相机

### 20.2 Light Field Camera

![img](https://assets.ng-tech.icu/item/202304172225100.jpg)

已经商业化量产的光场相机

![img](https://assets.ng-tech.icu/item/202304172225113.jpg)

光场相机的每个像素都是一个相机

![img](https://assets.ng-tech.icu/item/202304172225128.jpg)

如果我们只想用光场相机拍一张普通照片，则统一取一个方向的光即可

![img](https://assets.ng-tech.icu/item/202304172225146.jpg)

当然，光场相机如此牛逼的表现下，也是有极大的代价的

### 20.3 Physical Basis of Color

![img](https://assets.ng-tech.icu/item/202304172225160.jpg)

可见光的光谱

![img](https://assets.ng-tech.icu/item/202304172225174.jpg)

可以用谱功率密度记录一时刻一束光的性质

![img](https://assets.ng-tech.icu/item/202304172225188.jpg)

![img](https://assets.ng-tech.icu/item/202304172225203.jpg)

一些常见的光源的谱功率密度分布

![img](https://assets.ng-tech.icu/item/202304172225217.jpg)

且光是可以线性组合的

![img](https://assets.ng-tech.icu/item/202304172225232.jpg)

而颜色只是我们的感知，物理世界并不存在颜色的概念

### 20.4 Biological Basis of Color

![img](https://assets.ng-tech.icu/item/202304172225252.jpg)

人眼中的视杆细胞和视锥细胞

![img](https://assets.ng-tech.icu/item/202304172225269.jpg)

三种视锥细胞对光波频率的响应曲线

![img](https://assets.ng-tech.icu/item/202304172225284.jpg)

很神奇的一点是事实上每个人眼中的三种细胞的分布差异极大

每个人看到世界的感觉极大可能并不相同

![img](https://assets.ng-tech.icu/item/202304172225299.jpg)

视锥细胞响应光波的计算方式

![img](https://assets.ng-tech.icu/item/202304172225314.jpg)

大脑视觉感知的数据就仅仅来自于这些细胞的有限的处理后的信息

### 20.5 Metamerism

![img](https://assets.ng-tech.icu/item/202304172225328.jpg)

由于大脑接受到的是视细胞处理后的信号，相对于无穷维的光谱，大脑能接受的仅三维信号。所以是有信息缺失的。

比如大脑就无法分辨如图的几种广谱，看起来都是一种颜色

![img](https://assets.ng-tech.icu/item/202304172225345.jpg)

也是因为这样，显示器调色也只是调出感觉上较一致的光谱，而远非实际的光谱。

### 20.6 Color Reproduction or Matching

![img](https://assets.ng-tech.icu/item/202304172225364.jpg)

找实验人员来混合 RGB 使其和单光源的光看起来接近

![img](https://assets.ng-tech.icu/item/202304172225379.jpg)

但有的时候，靠 RGB 加和，是达不到目标光源的效果的，有可能需要对光源进行补光

这是则会导致 RGB 中产生负值分量

![img](https://assets.ng-tech.icu/item/202304172225394.jpg)

负值分量在单色光谱谱配中，红色是比较明显的

![img](https://assets.ng-tech.icu/item/202304172225410.jpg)

所以，在 CIE 颜色匹配系统中，采用的是这样的匹配方式

### 20.7 Color Spaces

![img](https://assets.ng-tech.icu/item/202304172225425.jpg)

我们通常常用的颜色空间 sRGB

![img](https://assets.ng-tech.icu/item/202304172225440.jpg)

科学界常用的人造颜色空间 CIE XYZ

![img](https://assets.ng-tech.icu/item/202304172225455.jpg)

将 XYZ 归一化后可以减少一维，展示出其实际颜色空间

单一波长光对应的坐标分布在边沿（但粉红边不对应自然中的单波光）

![img](https://assets.ng-tech.icu/item/202304172225470.jpg)

其他一些系统的色域则位于中间的一部分

![img](https://assets.ng-tech.icu/item/202304172225488.jpg)

HSV 颜色空间，由于比较直观，在美术工作中比较常用

![img](https://assets.ng-tech.icu/item/202304172225503.jpg)

CIELAB 颜色空间，用三组互补色确立三维颜色空间

![img](https://assets.ng-tech.icu/item/202304172225519.jpg)

颜色是相对的，是感知的实例（视觉白平衡，和蓝金衣服是一个原理）

![img](https://assets.ng-tech.icu/item/202304172225534.jpg)

打印用的减色颜色空间

理论上只用品红、蓝、黄即可，黑色可以由这三个颜色混合而成。但实际为了节省颜料费用，会单独使用黑色颜料（黑色颜料使用量大，且便宜）。
