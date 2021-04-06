# Fruit_and_vegetable_marking_machine
项目介绍：
：在国内的超市中，进行果蔬的价格计算主要是通过人工进行，这不仅效率低，而且超市用 人成本高。该项目采用图像识别方式。能够准确的识别果蔬类别，同类不同种的水果也能够准确识别。 该系统能够很好的适应超市市场变化做出调整，能够帮助企业节约大量的人力物力，实现超市智能化

运行环境：
python 3.6.8  + tensorflow-gpu 1.9.0 + opencv-python 4.1.0.25 + numpy 1.16.3 + serial 0.0.97

单片机型号 + AD转换模块（51 单片机  + hx711模块）

文件介绍：
detection_model 模型文件

utils 图片标记类包

data  label标签（分类的类别）

Get_Weight.py 串口通信（获取重量）

tf_test.py   主文件（图像识别）

5Kg电子秤程序 （hx 711x芯片进行电压信号的转换）

启动方式：
运行tf_test.py 文件（运行main方法）   需要提前接入单片机，设置波特率即可

