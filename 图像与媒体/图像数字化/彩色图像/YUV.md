# YUV

YUV 是一种颜色编码方方式，通常由彩色摄像机进行取像，然后把取得的彩色图像信号经过分色、分别放大校正后得到 RGB，再经过矩阵变换得到亮度信号 Y 和两个色差信号 B-Y（即 U）、R-Y（即 V），最后将亮度和色差三个信号分别编码，用同一信道发送出去。这种色彩的表示方法就是所谓的 YUV 色彩空间表示。采用 YUV 色彩空间的重要性就是它的亮度信号 Y 和色度信号 U、V 是分离的。

相对于 RGB 颜色空间，设计 YUV 的目的就是为了编码、传输的方便，减少带宽占用和信息出错。人眼的视觉特点是对亮度更铭感，对位置、色彩相对来说不铭感。在视频编码系统中为了降低带宽，可以保存更多的亮度信息(luma)，保存较少的色差信息(chroma)。Y’UV、YUV、YCbCr、YPbPr 几个概念其实是一回事儿。由于历史关系，Y’UV、YUV 主要是用在彩色电视中，用于模拟信号表示。YCbCr 是用在数字视频、图像的压缩和传输，如 MPEG、JPEG。今天大家所讲的 YUV 其实就是指 YCbCr。Y 表示亮度（luma），CbCr 表示色度（chroma）。

YUV 中“Y”表示明亮度（Luminance 或 Luma），也就是灰阶值；而“U”和“V” 表示的则是色度（Chrominance 或 Chroma），作用是描述影像色彩及饱和度，用于指定像素的颜色。“亮度”是透过 RGB 输入信号来建立的，方法是将 RGB 信号的特定部分叠加到一起。“色度”则定义了颜色的两个方面 ─ 色调与饱和度，分别用 Cr 和 Cb 来表示。其中，Cr 反映了 RGB 输入信号红色部分与 RGB 信号亮度值之间的差异。而 Cb 反映的是 RGB 输入信号蓝色部分与 RGB 信号亮度值之间的差异。

# YUV 采样

对于一个 w 宽、h 高的像素图，在水平方向，一行有 w 个像素；在垂直方向，一列有 h 个像素，整个图形有 `w * h` 个像素。我们把这个像素叫做图形像素。如果用 YCbCr 像素格式来表示像素图，那么要搞清楚亮度和图形像素的关系，色度和图形像素的关系。

![yuv 数字解释](https://s3.ax1x.com/2020/11/13/D9BMnS.png)

如上图中所示，左侧一列，每一个小矩形是图形像素表示，黑框矩形是色度像素表示，小黑点是表示色度像素值(Cb+Cr)，表示图形像素和色度像素在水平和垂直方向的比例关系。比如，

- 4:4:0 水平方向是 1/1，垂直方向是 1/2，表示一个色度像素对应了两个图形像素。
- 4:2:2 水平方向是 1/2，垂直方向是 1/1，表示一个色度像素对应了两个图形像素。
- 4:2:0 水平方向是 1/2，垂直方向是 1/2，表示一个色度像素对应了四个图形像素。

右侧一列是二次采样模式记号表示, 是 J：a：b 模式，实心黑色圆圈表示包含色度像素(Cb+Cr），空心圆圈表示不包含色度像素。对于 J:a:b 模式，主要是围绕参考块的概念定义的，这个参考块是一个 J x 2 的矩形，J 通常是 4。这样，此参考块就是宽度有 4 个像素、高度有 2 个像素的矩形。a 表示参考块的第一行包含的色度像素样本数，b 表示在参考块的第二行包含的色度像素样本数。

- 4：4：0 参考块第一行包含四个色度样本，第二行没有包含色度样本。
- 4：2：2 参考块第一行包含两个色度样本，第二行也包含两个色度样本，他们是交替出现。
- 4：2：0 参考块第一行包含两个色度样本，第二行没有包含色度样本。

现在我们发现 yuv444，yuv422，yuv420 yuv 等像素格式的本质是：每个图形像素都会包含亮度值，但是某几个图形像素会共用一个色度值，这个比例关系就是通过 4 x 2 的矩形参考块来定的。这样很容易理解类似 yuv440，yuv420 这样的格式了。

- 4：4：4 表示没有对色度通道进行缩减采样。
- 4：2：2 意味着 2：1 的水平缩减采样，没有垂直下采样。每扫描一行，每两个 U 或 V 采样包含四个 Y 采样。
- 4：2：0 表示 2：1 水平缩减采样，2：1 垂直缩减采样。
- 4：1：1 表示 4：1 水平缩减采样，没有垂直下采样。每个扫描线对于每个 U 或 V 采样包含四个 Y 采样。4：1：1 采样比其他格式少见。

换句话说来说，可以理解为：

- YUV 4:4:4 采样，每一个 Y 对应一组 UV 分量。
- YUV 4:2:2 采样，每两个 Y 共用一组 UV 分量。
- YUV 4:2:0 采样，每四个 Y 共用一组 UV 分量。

下面三个图分别是各自的采集方式：

![YUV 采集方式](https://s3.ax1x.com/2020/11/15/DFVtcq.png)

# YUV 存储

下面的图给出了常见的 YUV 码流的存储方式，并在存储方式后面附有取样每个像素点的 YUV 数据的方法，其中，Cb、Cr 的含义等同于 U、V。

## YUVY 格式 （属于 YUV422）

![img](https://images2017.cnblogs.com/blog/682616/201802/682616-20180209155346982-258986689.png)

YUYV 为 YUV422 采样的存储格式中的一种，相邻的两个 Y 共用其相邻的两个 Cb、Cr，分析，对于像素点 Y'00、Y'01 而言，其 Cb、Cr 的值均为 Cb00、Cr00，其他的像素点的 YUV 取值依次类推。

## UYVY 格式 （属于 YUV422）

![img](https://images2017.cnblogs.com/blog/682616/201802/682616-20180209155417170-837281930.png)

UYVY 格式也是 YUV422 采样的存储格式中的一种，只不过与 YUYV 不同的是 UV 的排列顺序不一样而已，还原其每个像素点的 YUV 值的方法与上面一样。

## YUV422P（属于 YUV422）

![img](https://images2017.cnblogs.com/blog/682616/201802/682616-20180209155457982-968223311.png)

YUV422P 也属于 YUV422 的一种，它是一种 Plane 模式，即打包模式，并不是将 YUV 数据交错存储，而是先存放所有的 Y 分量，然后存储所有的 U（Cb）分量，最后存储所有的 V（Cr）分量，如上图所示。其每一个像素点的 YUV 值提取方法也是遵循 YUV422 格式的最基本提取方法，即两个 Y 共用一个 UV。比如，对于像素点 Y'00、Y'01 而言，其 Cb、Cr 的值均为 Cb00、Cr00。

平面格式是指用三个不同的数组来表示 YCbCr 的三个 Component，每一个 Component 都是通过不同的平面表示。为此，每一个 Component 会对应一个 plane。yuv420p 也叫 i420 就是 yuv420 planar 表示。yuv420p 一共有三个平面分别是 Y，U，V，每一个平面都是用 8 bit 二进制数字表示，我们把 8 bit 称作位深度。

如果用 yuv420p 来表示分辨率为 `1280 * 720` 的图片，需要占用多少存储空间呢？

- 每一个像素都需要一个 luma 值，即 y。那么总共需要 `1280 * 720 = 921600 bytes`。
- 每四个像素需要一个 chroma u 值，那么总共需要 `1280 * 720 / 4 = 230400 bytes`。
- 每四个像素需要一个 chroma v 值，那么总共需要 `1280 * 720 / 4 = 230400 bytes`。

把 y、u、v 三个 plane 加起来就是：921600 + 230400 + 230400 = 1382400 bytes。

## YV12，YU12 格式（属于 YUV420）

![img](https://images2017.cnblogs.com/blog/682616/201802/682616-20180209155537466-578129036.png)

## NV12、NV21（属于 YUV420）

![img](https://images2017.cnblogs.com/blog/682616/201802/682616-20180209155555263-1405762791.png)

NV12 和 NV21 属于 YUV420 格式，是一种 two-plane 模式，即 Y 和 UV 分为两个 Plane，但是 UV（CbCr）为交错存储，而不是分为三个 plane。其提取方式与上一种类似，即 Y'00、Y'01、Y'10、Y'11 共用 Cr00、Cb00

## yuv420p 和 yuv420 的区别

二者在存储格式上有区别：

- yuv420p：yyyyyyyy uuuuuuuu vvvvv
- yuv420： yuv yuv yuv

yuv420P，Y，U，V 三个分量都是平面格式，分为 I420 和 YV12。I420 格式和 YV12 格式的不同处在 U 平面和 V 平面的位置不同。在 I420 格式中，U 平面紧跟在 Y 平面之后，然后才是 V 平面（即：YUV）；但 YV12 则是相反（即：YVU）。YUV420SP, Y 分量平面格式，UV 打包格式, 即 NV12。 NV12 与 NV21 类似，U 和 V 交错排列,不同在于 UV 顺序。

```s
I420: YYYYYYYY UU VV =>YUV420P
YV12: YYYYYYYY VV UU =>YUV420P
NV12: YYYYYYYY UVUV =>YUV420SP
NV21: YYYYYYYY VUVU =>YUV420SP
```

# YUV 格式与 RGB 格式的换算

- RGB 转换成 YUV

```
Y = (0.257 * R) + (0.504 * G) + (0.098 * B) + 16
Cr = V = (0.439 * R) - (0.368 * G) - (0.071 * B) + 128
Cb = U = -( 0.148 * R) - (0.291 * G) + (0.439 * B) + 128
```

- YUV 转换成 RGB

```
B = 1.164(Y - 16) + 2.018(U - 128)
G = 1.164(Y - 16) - 0.813(V - 128) - 0.391(U - 128)
R = 1.164(Y - 16) + 1.596(V - 128)
```

RGB 取值范围均为 0255,Y=0255,U=-122+122,V=-157+157，简化后的换算公式

- RGB 转 YUV

```
Y = 0.299R + 0.587G + 0.114B
U'= (BY)*0.565
V'= (RY)*0.713
```

- YUV 转 RGB

```
R = Y + 1.403V'
G = Y - 0.344U' - 0.714V'
B = Y + 1.770U'
```

# 压缩格式（Packed formats）

压缩格式是指用一个数组表示 YCbCr，每一个 component 是交替出现的。

## ffmpeg 中对 yuv420p 像素格式大小计算

yuv420p 的格式描述在 libavutil/pixdesc.c 的 173 行。

```text
173 static const AVPixFmtDescriptor av_pix_fmt_descriptors[AV_PIX_FMT_NB] = {
174     [AV_PIX_FMT_YUV420P] = {
175         .name = "yuv420p", // 像素格式名称
176         .nb_components = 3, // 表示有三个 component ，也是三个 plane
177         .log2_chroma_w = 1, // 表示色度(chroma) 像素和图形像素的水平比例关系
178         .log2_chroma_h = 1, // 表示色度(chroma) 像素和图形像素的垂直比例关系
179         .comp = {
180             { 0, 1, 0, 0, 8, 0, 7, 1 },        /* Y 平面，step 是 1，位深度是8 bit */
181             { 1, 1, 0, 0, 8, 0, 7, 1 },        /* U 平面，step 是 1，位深度是8 bit */
182             { 2, 1, 0, 0, 8, 0, 7, 1 },        /* V 平面，step 是 1，位深度是8 bit */
183         },
184         .flags = AV_PIX_FMT_FLAG_PLANAR,
185     },
```

所有的 YUV 像素格式表示都在 av_pix_fmt_descriptors 表中完成，我可以把这叫做像素格式描述表。

yuv420p 像素格式在水平方向(行)大小计算在 libavutil/imgutils.c 的 54 行。

```text
53 static inline
54 int image_get_linesize(int width, int plane,
55                        int max_step, int max_step_comp,
56                        const AVPixFmtDescriptor *desc)
57 {
58     int s, shifted_w, linesize;
59
60     if (!desc)
61         return AVERROR(EINVAL);
62
63     if (width < 0)
64         return AVERROR(EINVAL);
    // max_step_comp 的取值： 0：y，1：u，2：v。对于 y 平面，每一个图形像素需要一个亮度值，
    // 所以这里比例因子是 0；对于 u、v 平面来说，色度像素和图形像素在水平和垂直方向都是 2/1 的关系，
    // 所以计算行的时候，比例因子取像素格式描述表中的 log2_chroma_w。对于 yuv420p 来说，取值是 1 ，
    // 因为是通过移位运算完成的，右移 1 位，相当于是除以 2。
65     s = (max_step_comp == 1 || max_step_comp == 2) ? desc->log2_chroma_w : 0;
66     shifted_w = ((width + (1 << s) - 1)) >> s;
67     if (shifted_w && max_step > INT_MAX / shifted_w)
68         return AVERROR(EINVAL);
69     linesize = max_step * shifted_w;
70
    // 如果像素描述表中的单位是 bit，那么这里转换成 bytes，右移 3 位，就是除以 8。
71     if (desc->flags & AV_PIX_FMT_FLAG_BITSTREAM)
72         linesize = (linesize + 7) >> 3;
73     return linesize;
74 }
```

yuv420p 像素格式在垂直方向(列)大小计算在 libavutil/imgutils.c 的 111 行。

```text
111 int av_image_fill_pointers(uint8_t *data[4], enum AVPixelFormat pix_fmt, int height,
112                            uint8_t *ptr, const int linesizes[4])
113 {
114     int i, total_size, size[4] = { 0 }, has_plane[4] = { 0 };
115
116     const AVPixFmtDescriptor *desc = av_pix_fmt_desc_get(pix_fmt);
117     memset(data     , 0, sizeof(data[0])*4);
118
119     if (!desc || desc->flags & AV_PIX_FMT_FLAG_HWACCEL)
120         return AVERROR(EINVAL);
121
122     data[0] = ptr;
123     if (linesizes[0] > (INT_MAX - 1024) / height)
124         return AVERROR(EINVAL);
125     size[0] = linesizes[0] * height;
126
127     if (desc->flags & AV_PIX_FMT_FLAG_PAL ||
128         desc->flags & FF_PSEUDOPAL) {
129         data[1] = ptr + size[0]; /* palette is stored here as 256 32 bits words */
130         return size[0] + 256 * 4;
131     }
132
133     for (i = 0; i < 4; i++)
134         has_plane[desc->comp[i].plane] = 1;
135
136     total_size = size[0];
137     for (i = 1; i < 4 && has_plane[i]; i++) {
        // i 的取值： 0：y，1：u，2：v。对于 y 平面，每一个图形像素需要一个亮度值，
        // 所以这里比例因子是 0；对于 u、v 平面来说，色度像素和图形像素在水平和垂直方向都是 2/1 的关系，
        // 所以计算列的时候，比例因子取像素格式描述表中的 log2_chroma_h。对于 yuv420p 来说，取值是 1 ，
        // 因为是通过移位运算完成的，右移 1 位，相当于是除以 2。
138         int h, s = (i == 1 || i == 2) ? desc->log2_chroma_h : 0;
139         data[i] = data[i-1] + size[i-1];
140         h = (height + (1 << s) - 1) >> s;
141         if (linesizes[i] > INT_MAX / h)
142             return AVERROR(EINVAL);
        // 每一平面的行和列做乘法，就是像素总数。
143         size[i] = h * linesizes[i];
144         if (total_size > INT_MAX - size[i])
145             return AVERROR(EINVAL);
        // 每一个平面的像素数相加，就是图片占用的像素总数。
146         total_size += size[i];
147     }
148
149     return total_size;
150 }
```
