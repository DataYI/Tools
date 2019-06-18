# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 11:53:22 2018

@author: DataAnt
"""
from pymouse import PyMouse
import time
import sys

m = PyMouse()

try:
    operation = sys.argv[1]
except IndexError:
    print('请输入参数')
    
if operation in dir():
    operation = operation.lower()


def action(delay, x_relative, y_relative):
    '''
    延迟delay秒后，点击指定位置
    :x_relative: 相对应用左上角的橫坐标
    :y_relative: 相对应用左上角的纵坐标
    '''
    time.sleep(delay)
    m.click(x_origin + x_relative, y_origin + y_relative, 1)


def _get_relative(x_absolute, y_absolute):
    '''
    绝对坐标转化为相对坐标
    '''
    x_relative = x_absolute - x_origin
    y_relative = y_absolute - y_origin
    return x_relative, y_relative


def get_relative():
    '''
    将当前鼠标所在位置绝对坐标转换成相对坐标
    '''
    pos = m.position()
    coor_relative = _get_relative(*pos)
    return coor_relative


if operation in ('r', 'relative'):
    # 2秒钟内将鼠标移动到应用界面的左上角
    time.sleep(2)
    x_origin = int(sys.argv[2])
    y_origin = int(sys.argv[3])
    # 输出相对坐标
    print(get_relative())
elif operation in ('a', 'absolute'):
    # 2秒钟内将鼠标移动到应用界面的左上角
    time.sleep(2)
    # 输出绝对坐标
    print(m.position())
else:
    print('参数错误')

