## 17.Materials and Appearances

### 17.1 Appearances

![img](https://assets.ng-tech.icu/item/202304172223541.jpg)

现实世界中的光影材质非常多样和复杂。

比如光可能会在光路上和微粒碰撞漫反射出一条光路。

比如头发的丝质感，和微透明的感觉。

比如布料的纹理通常甚至需要考虑到其针织的方式。

日出的双彩虹现象。

还比如三文鱼肉的次表面反射。

等等

### 17.2 Material

![img](https://assets.ng-tech.icu/item/202304172223565.jpg)

我们可以为一个模型指定不同的材质。

在渲染方程中，决定材质的正是 BRDF

![img](https://assets.ng-tech.icu/item/202304172223583.jpg)

一个应用不同的 BRDF 的例子

![img](https://assets.ng-tech.icu/item/202304172223602.jpg)

一个各向同性的点，接受的光和漫反射的光能量一致，可以根据能量守恒计算出其 BRDF 系数为 1/𝜋

所以要自然地定义一个漫反射点的反射系数，其值应该位于 [0,1/𝜋]

通常把这个值称为 albedo

![img](https://assets.ng-tech.icu/item/202304172223617.jpg)

而这种靠近镜面反射，但又综合了漫反射性质的毛金属材质

![img](https://assets.ng-tech.icu/item/202304172223638.jpg)

还有的材质可以折射透过表面，达到玻璃效果。

### 17.3 Reflection

![img](https://assets.ng-tech.icu/item/202304172223652.jpg)

由入射光方向，计算镜面反射的出射的方法

![img](https://assets.ng-tech.icu/item/202304172223666.jpg)

一个镜面反射的例子

### 17.4 Refraction

![img](https://assets.ng-tech.icu/item/202304172223681.jpg)

折射的一些例子，偶尔需要对不同波长的光采用不同的折射率以模拟散射

![img](https://assets.ng-tech.icu/item/202304172223695.jpg)

高中物理中的折射定律

![img](https://assets.ng-tech.icu/item/202304172223714.jpg)

折射定律，且当入射角过大则不再有折射而发生全反射

![img](https://assets.ng-tech.icu/item/202304172223731.jpg)

一个全反射的例子：在泳池中往上看，只有正中一块区域能看到外部。周围都只会反射而不再能看到水面以上。

![img](https://assets.ng-tech.icu/item/202304172223746.jpg)

菲涅尔反射现象：入射光与法线角度越大越容易反射

![img](https://assets.ng-tech.icu/item/202304172223762.jpg)

绝缘体的菲涅尔项的大致走势

![img](https://assets.ng-tech.icu/item/202304172223777.jpg)

导体的菲涅尔项的大致走势

![img](https://assets.ng-tech.icu/item/202304172223795.jpg)

菲涅尔项的一个常用近似函数

### 17.5 Microfacet Material

![img](https://assets.ng-tech.icu/item/202304172223810.jpg)

同样的物体在不同的 Scale 下表现差异可能很大。比如海面波涛汹涌，但远看几乎光滑。

![img](https://assets.ng-tech.icu/item/202304172223831.jpg)

因此光滑或者粗糙等性质其实是相对的，需要基于尺度。即使是人们用的镜子，放大看依旧是粗糙不堪的。

![img](https://assets.ng-tech.icu/item/202304172223852.jpg)

或者体现在反射方向的分布方差越小，视觉上越光滑

![img](https://assets.ng-tech.icu/item/202304172223868.jpg)

也是因此有菲涅尔项，因为通常越是斜着看，表面的凹凸越容易被相互遮挡而隐藏，留下相对光滑的表现。

![img](https://assets.ng-tech.icu/item/202304172223884.jpg)

一些精细建模并渲染的例子

### 17.5 Isotropic

![img](https://assets.ng-tech.icu/item/202304172223897.jpg)

各向异性的例子。

![img](https://assets.ng-tech.icu/item/202304172223913.jpg)

源自于其材料在微观上表现有方向上的明显差异

![img](https://assets.ng-tech.icu/item/202304172223929.jpg)

各项异性的 BRDF

由于对于这种材质需要考虑入射光和出射光关于材质本身的旋转角度，所以需要额外增加一维进行描述其 BRDF

![img](https://assets.ng-tech.icu/item/202304172223942.jpg)

设置这类材质时需要考虑其生产或打磨的方式。比如锅是旋转拉丝制作的，所以其纹路呈环状

![img](https://assets.ng-tech.icu/item/202304172223956.jpg)

尼龙由于其制作方式是织，导致 90 度和 45 度视角下表现有差异，虽然整体已经稍接近各向同性

![img](https://assets.ng-tech.icu/item/202304172223969.jpg)

但天鹅绒，由于其局部的毛可能一起朝向一个方向，使其各向异性非常明显。

![img](https://assets.ng-tech.icu/item/202304172223984.jpg)

天鹅绒沙发的各向异性非常明显

### 17.6 Properties of BRDFs

![img](https://assets.ng-tech.icu/item/202304172223999.jpg)

非负性和可加性

![img](https://assets.ng-tech.icu/item/202304172223015.jpg)

可逆性和能量守恒性

![img](https://assets.ng-tech.icu/item/202304172223033.jpg)

前文的各向同性或各向异性

### 17.7 Measuring BRDFs

![img](https://assets.ng-tech.icu/item/202304172223052.jpg)

物理上的一些材质性质和人工模拟的差别有可能很大。

所以用测量的方式可以更好地确定目标物体的性质，以达到更好的渲染结果。

![img](https://assets.ng-tech.icu/item/202304172223068.jpg)

测量方式即遍历入射角和出射角

![img](https://assets.ng-tech.icu/item/202304172223084.jpg)

一个实际的测量机器

![img](https://assets.ng-tech.icu/item/202304172223102.jpg)

由于枚举入射和出射方向，数据量是四维的，量很恐怖，有一些方式可以略减少测量数据量

比如如果材质是各项同性的，则可以利用对称性，少测量一个维度。

![img](https://assets.ng-tech.icu/item/202304172223120.jpg)

测量 BRDF 的一些挑战

![img](https://assets.ng-tech.icu/item/202304172223137.jpg)

保存或表示 BRDF 的方法

![img](https://assets.ng-tech.icu/item/202304172223155.jpg)

一个 BRDF 的数据库:MERL BRDF Database
