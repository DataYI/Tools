# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 10:00:59 2018

@author: DataAnt
"""
from collections import defaultdict
import cv2
import numpy as np


def color_list(*args):
    return [np.array(args[:3]), np.array(args[3:])]
    

# 生成颜色字典
color_dict = defaultdict(list)
# 每种颜色的数值范围由两个ndarray表示，分别表示最小值和最大值
color_dict['black'] = color_list(0, 0, 0, 180, 255, 46)
color_dict['white'] = color_list(0, 0, 221, 180, 30, 255)
color_dict['red'] = color_list(156, 43, 46, 180, 255, 255)
color_dict['red2'] = color_list(0, 43, 46, 10, 255, 255)
color_dict['orange'] = color_list(11, 43, 46, 25, 255, 255)
color_dict['yellow'] = color_list(26, 43, 46, 34, 255, 255)
color_dict['green'] = color_list(35, 43, 46, 77, 255, 255)
color_dict['cyan'] = color_list(78, 43, 46, 99, 255, 255)
color_dict['blue'] = color_list(100, 43, 46, 124, 255, 255)
color_dict['purple'] = color_list(125, 43, 46, 155, 255, 255)

# 图片路径
filename = 'sample.png'
# 读入图片，生成一个用RGB数值表示的三维数组，size为(height, length, 3)
frame = cv2.imread(filename)
# 将RGB三维数组转为HSV三维数组
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

# 指定颜色
color = 'red2'
# 用颜色字典中的颜色对HSV三维数组过滤，在颜色范围内的数值变成255，范围外的变成0
mask = cv2.inRange(hsv,color_dict[color][0],color_dict[color][1])
# 生成颜色过滤后的图片，指定的颜色部分就白色，其它颜色部分变成黑色
cv2.imwrite(color + '.png', mask)
