import cv2
import os
num = 0
file_dir = 'D:/python/deep-learning/MRI-2D/data/NC'

for file in os.listdir(file_dir):  # file就是要读取的照片
    print(file)
    dir = 'D:/python/deep-learning/MRI-2D/data/NC/'+ file
    print(dir)
    src = cv2.imread(dir, 0)  # 通过实验发现直接用cv2.imread读取图片就会变成3通道
    print(src.shape)
    src_RGB = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
    print(src_RGB.shape)
    num += 1
    cv2.imwrite('D:/python/deep-learning/MRI-2D/data/NC-RGB/' + "NC." + str(num) + ".jpg", src_RGB)

print("over")
