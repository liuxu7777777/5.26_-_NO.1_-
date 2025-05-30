# 5.26_-_NO.1_OCR

网信安技术培训_5.26_第一天_第一个代码_正则表达式

查找匹配文档中的文本（通过ocr文本识别）

png文件夹内存放的是示例图片，需要把png文件夹和代码放在同一个文件夹内（一个文件夹下有png文件夹和代码，这两个东西平级）
注意路径必须是纯英文，有汉字文件夹路径会报错

代码需要用到GPU，如果没有独立显卡可能会警告：Neither CUDA nor MPS are available - defaulting to CPU. Note: This module is much faster with a GPU.
不过没关系，只是运行得慢点

如果缺少库，需要先win+R-cmd-pip相关的库

运行结果示例：
For image hHEm7ckm1vnLiuu2om.png: name:34, phone:0, address:0, ssn:34, bankcard:0
Processing image: IAz8DZlV43HKXVf5sG.png
