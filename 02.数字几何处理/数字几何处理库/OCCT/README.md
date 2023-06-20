# OCCT

![Cascade Technology](https://assets.ng-tech.icu/item/20230619220148.png)

CAD 技术从 60 年代诞生以来，经历了二维绘图、线框模型、自由曲面模型、实体造型、特征造型等重要发展阶段。随着 CAD 技术的发展也诞生了许多成熟和知名的 CAD 引擎和软件。目前，商用 CAD 引擎主要包括了 ACIS、HOOPS、ParaSolid 等。其中使用 ACIS 引擎的底层产品主要包括了 AutoCAD、Inventer、Catia、MicroSolid 等；使用 ParaSolid 引擎的主要包括了 UG、Solidworks、SolidEdge 等。但由于关注点的差别及商业保密的因素，不同的 CAD 软件都有自己的一套建模方式和存储体系，这导致了系统间数据无法进行直接的传递。目前采用的方式是通过中间标准格式文件为媒介进行传递，但是这种方式会丢失一些细节特征，这就还需要进行一些其它额外的修补工作，这也一定程度上影响了 CAD 技术的发展。

在商用 CAD 软件外，还有一些比较成熟的开源 CAD 引擎，其中使用的比较多的是 OpenCascade(简称 OCC)。OCC 平台是由法国 Matra Datavision 公司开发的 CAD/CAE/CAM 软件平台，可以说是世界上最重要的几何造型基础软件平台之一。它是一个开放源码 CAD 内核，可以定制和扩展（添加新的功能组件，类的进一步继承），面向 CAD/CAM，对主流 CAD 数据格式提供支持（STEP/STL/IGES 等，可自行开发转换程序提供特定数据格式的支持），提供高级建模函数（拟合，有理样条曲线，拉伸、旋转、扫出、层叠拉伸、圆角、倒角、薄壳、修剪、偏移等），参数化模型，提供几何模型的特征提取，对 Visual C++/MFC 有很好的支持。
