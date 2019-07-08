# function：可以把文件夹中的所有图片每三个拼接在一起
# author： xingjianzhang
# time： 2019/7/8

import os
from PIL import Image
from os import listdir

num = 0

# 获取当前文件夹中所有JPG图像
os.chdir("D:/python/BCI/Data")
im_list = [Image.open(fn) for fn in listdir() if fn.endswith('.jpg')]

for i in range(1236):     # len（im_list）==1236
    # 图片转化为相同的尺寸
    ims = []
    for a in im_list[num:num+3]:
        new_img = a.resize((1280, 1280), Image.BILINEAR)  # bilinear函数使用双线性插值调整images的size
        ims.append(new_img)

    # 单幅图像尺寸
    width, height = ims[0].size

    # 创建空白长图
    result = Image.new(ims[0].mode, (width, height * 3))

    # 拼接图片
    for x, im in enumerate(ims):
        result.paste(im, box=(0, x * height))

    # 保存图片
    result.save('D:/python/BCI/jpg-data/jpg%d.label.jpg' %(i+1))
    num = num + 3

    
