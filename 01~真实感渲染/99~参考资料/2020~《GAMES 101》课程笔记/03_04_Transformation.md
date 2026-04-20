# Transformation

# Basic of Transformation

![Why Transformation](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216606.jpg)

首先用几个例子（摄像机在空间中的运动、机器人运动、视角变换）介绍一下为什么要用 Transformation，之后介绍几种二维上的基本变换。

![Scale](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216620.jpg)

![Reflection Matrix](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216636.jpg)

![Shear Matrix](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216651.jpg)

![Rotation Martrix](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216665.jpg)

![Translation](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216679.jpg)

平移变换，但通常在齐次坐标下进行。合在一起成为仿射变换：

![Affine Transformations](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216692.jpg)

![Inverse Transform](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216706.jpg)

![Composing Transforms](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216720.jpg)

![3D Transformations](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216734.jpg)

![3D Transformations](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216749.jpg)

3D 的缩放、镜像、切变基本和 2D 可直接类比。但是旋转会有一些麻烦。这是一种解决方案，将任意旋转分解为绕坐标轴旋转。并且这里需要注意坐标系，课程中使用的是右手坐标系，部分 API 和软件会使用左手坐标系。

![Rodrigues' Rotation Formula](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216762.jpg)

# Camera Transformation

![View/Camera Transformation](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216778.jpg)

![View/Camera Transformation](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216792.jpg)

三维摄像机有 7 个维度

- 位置：3 维
- 朝向：3 维
- 画面旋转：1 维

通常用三个向量进行对应

- 位置向量
- 朝向向量
- 上方向量（由于一定和朝向正交，所以会冗余 2 维）

![View/Camera Transformation](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216807.jpg)

正向考虑摄像机变换的矩阵是比较麻烦的一件事情：

![View/Camera Transformation](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216821.jpg)

但反向考虑则比较容易，所以可以通过反向考虑，配合矩阵求逆得到结果。

# Projection Transformation

投影变换本身是一个降维变换，图形学中主要针对于将三维投影至二维：

![Projection Transformation](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216837.jpg)

3D 至 2D 的投影主要有两种：平行投影和透视投影：

![Orthographic Projection](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216853.jpg)

平行投影的操作比较简单，直接丢掉坐标中的 Z 分量即可。

![Orthographic Projection](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216868.jpg)

但通常需要 canonical，即首先将视图空间中心平移至原点，再缩放为标准正方体。

![Orthographic Projection](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216883.jpg)

整理一下可知这一系列操作对应的矩阵。

![Perspective Projection](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216898.jpg)

透视投影本质上是将空间投影至一个点，但在过程中用一个平面（如胶片）截下。而对于透视变换，可以考虑将其先变换为平行，再用平行投影。

![Perspective Projection](https://ngte-superbed.oss-cn-beijing.aliyuncs.com/item/202304172216912.jpg)

这个矩阵并不直观，但是可以通过设立条件对矩阵进行推导

- 胶片所在平面不发生变化
- 而远处的平面大小缩放至和胶片一样大，且中心对齐，但 Z 值不变
