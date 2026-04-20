# Shading: Shading,Pipeline and Texture Mapping

# 7.1 目前的进度和局限

![Rotating Cubes](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218826.jpg)

能够用上面的方法绘制场景，即可做出如图的效果。但这样是不够的。我们想得到下面的效果

![Rotating Cubes Expected](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218849.jpg)

为什么会这样呢？为什么“相同”颜色的方块的每一面颜色不一致呢？容易发现，是环境光的影响。我们看到的物体画面是由物体本身和环境光共同作用得到的结果。所以需要考虑环境光。这个共同作用的方式，则体现出了物体的材质。

# 7.2 Shading 是什么

![Shading: Definition](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218866.jpg)

而 Shading 在本课中则对应着将材质应用于物体本身的过程。

# 7.3 Blinn-Phong 模型介绍

![A Simple Shading Model](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218887.jpg)

Blinn-Phong 是经验总结下的容易实现的材质模型。其原理来自于观察：当光源和观察者的方向接近时，物体的颜色会变得更亮。而当光源和观察者的方向相反时，物体的颜色会变得更暗。

![Perceptual Observations](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218909.jpg)

类似于绘画中的三大面。可以把物体表面分为高光区域、漫反射区域、环境光区域。

![Shading is Local](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218927.jpg)

需要注意的是，Shading 有局部性，只关心每个三角形本身，不关心三角形相互的作用，

# 7.4 Blinn-Phong 漫反射

![Lambertian (Diffuse) Shading](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218941.jpg)

Blinn-Phong 模型中，漫反射的颜色受到三个部分影响

- 材料的固有色，对应一个系数（可为颜色向量）$k_d$
- 反光点和光源的距离光源，距离越远亮度越底，对应于 $𝐼/𝑟^2$
- 表面法线与光线的夹角，夹角越大则单位面积能反射的光子理应越少，一旦大过 $𝜋/2$ 则意味着背光，不再漫反射。于是对应于 $𝑚𝑎𝑥(0,𝑛∗𝑙)$

![Lambertian (Diffuse) Shading](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218956.jpg)

仅利用漫反射模型，且单一灰阶的固有色即可渲染出上面的效果。

# 8.1 Blinn-Phong 高光

![Specular Term](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218968.jpg)

再考虑高光项。高光对应于镜面反射，摄像机越接近光源的镜面反射的出方向，则应接受到越强的镜面反射光。度量这个“接近度”有一个聪明的比较容易的计算的方法，是比较光源方向和摄像机方向的中间方向（很容易计算）和法线方向的夹角，夹角越大则越不接近。

且对于这个接近度可以取一个次数 $p$，使整体更容易调整，且接近想要的效果。

![Cosine Power Plots](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218981.jpg)

$p$ 越高，高亮区域越小。通常而言会用到 100 ～ 200。

![Blinn-Phong](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218993.jpg)

加入了高光项后，可以得到上图效果，且可以看出两个参数在调整时对结果的影响。

# 8.2 Blinn-Phong 环境光

![Ambient Term](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218008.jpg)

最后，对于暗部，并不希望全黑，所以可以加入环境光项，当然，并没有办法保证有光，也不可能环境光处处相同，所以这只是个不符合物理的趋近方法

![Blinn-Phong Reflection Model](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218020.jpg)

最后综合 漫反射、高光、环境光 三项后可以得到上图效果。

# 8.3 Shading 频率

![Shading Frequencies](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218034.jpg)

同样是应用 Blinn-Phong，也可以由于面向对象不同得到不同结果，上方三张图依次对应于

- 低频：面向三角形
- 中频：面向顶点，三角形内部应用重心坐标差值
- 高频：面向像素

![Shade each triangle](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218048.jpg)

面向三角形的 Shading 计算量最小。但对于不够高面又光滑曲面的物体而言会不再光滑。

![Shade each vertex](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218063.jpg)

对顶点着色，并应用差值：

![Shade each pixel](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218076.jpg)

对每个像素着色。这里的 Phong Shading 对应于着色频率，而非 Blinn-Phong 着色模型。

![Shading Frequency: Face, Vertex or Pixel](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218088.jpg)

这几种着色频率对应足够高面的模型而言表现是近似的。所以如果足够多面，应优先选择更低频的着色方式，减少计算量。

![Defining Per-Vertex Normal Vectors](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218101.jpg)

对逐顶点着色而言，是需要获得顶点的法线的。可以采用相邻三角形法线的简单平均，或者根据三角形面积加权平均。

![Defining Per-Pixel Normal Vectors](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218115.jpg)

对逐像素着色而言，则需要获得每个像素的法线方向，通常使用自己和附近面的法线用一些方式加权平均。

# 8.4 渲染管线

![Graphics Pipeline](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218127.jpg)

将一次渲染分成几步，大部分集成在 GPU 内部，成为硬件逻辑。部分可以编程。

![Graphics Pipeline](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218141.jpg)

比如一开始先处理顶点（等效于处理三角形，因为三角形被顶点决定）

![Graphics Pipeline](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218155.jpg)

![Rasterization Pipeline](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218170.jpg)

对片面的测试和处理（也可以算作光栅化的一部分）

![Graphics Pipeline](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218182.jpg)

Shading 根据不同着色频率可以对应至这两个步骤。

![Graphics Pipeline Texture mapping](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218196.jpg)

纹理映射也属于 Shading 一部分：

![Snail Shader Program](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218210.jpg)

纯靠 Shader 代码 800 行绘制出蜗牛。

# 8.5 纹理映射

![Visualization of Texture Coordinates](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218226.jpg)

将二维的表面和一张二维的图逐点一一对应：

![Texture can be used multiple times!](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218243.jpg)

一些纹理是可以上下左右拼接的，做到重复利用。

# 9.1 三角形重心坐标

![Interpolation Across Triangles](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218256.jpg)

![Barycentric Coordinates](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218272.jpg)

用对面三角形面积占比计算：

![Barycentric Coordinates: Formulas](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218290.jpg)

# 9.2 应用纹理

![Texture Magnification - Easy Case](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218306.jpg)

直接采样，又会有锯齿问题。可以通过双线性插值(Bilinear)一定程度解决。当然还可以用 Bicubic 三阶差值（取周围 16 个点），得到更好的效果：

![Bilinear Interpolation](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218322.jpg)

双线性插值的方法：

![Point Sampling Textures](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218336.jpg)

当纹理过大也会有问题，问题源自一个像素对应了纹理上太多像素：

![Screen Pixel "Footprint" in Texture](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218351.jpg)

![Will Supersampling Do Antialiasing?](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218367.jpg)

超采样可以解决，但计算量过大：

![Mipmap](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218380.jpg)

Mipmap 是一种对贴图进行预处理后很好的一种方式：

![Visualization of Mipmap Level](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218393.jpg)

使用 Mipmap 的情况下，如果直接为每个像素点指定一个层级，会让过渡比较硬。

![Trilinear Interpolation](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218408.jpg)

可以用相邻两个层级进行线性插值：

![Visualization of Mipmap Level](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218421.jpg)

得到更好的结果：

![Mipmap Limitations](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218434.jpg)

不过 Mipmap 依旧不能解决这个问题：

![Irregular Pixel Footprint in Texture](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218448.jpg)

这是由于 Mipmap 擅长解决正方形的采样，但不擅长非正方形的采样：

![Anisotropic Filtering](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218461.jpg)

所以后来还有 Ripmaps 可以支持任意正放的长方形采样，还有 EWA 更加复杂，但可以支持把任意形状分成多个圆形。但也意味着多次查询需要的更多开销。

# 10.1 贴图的其他应用

![img](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218476.jpg)

记录环境光

![img](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218490.jpg)

环境光可以记录在球上，但球的两极会有扭曲，所以一般记录在正方体的表面

![img](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218503.jpg)

还可以记录表面相对高度，即凹凸贴图（与法线贴图目标近似，但计算和优势不同）

![img](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218517.jpg)

二维上计算法线的方式是查分求导再旋转。

![img](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218530.jpg)

三维也类似

![img](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218545.jpg)

还可以在处理顶点时事实地改变顶点位置。

不过这要求模型的精细度足够高，以保证有足够多的顶点可以随贴图改变。目前 Direct X 支持这种情况下动态改变模型的精细度。

![img](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218559.jpg)

纹理也可以是 3D 的，甚至是函数化的

![img](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218573.jpg)

还可以用于预烘培，提前计算一些阴影啥的

![img](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172218586.jpg)

或者记录三维信息
