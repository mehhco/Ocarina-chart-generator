#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/7 23:50
# @Author  : Haicheng
# @Contact : mehhco@163.com
# @File    : unit_test.py

"""
unit test
"""

from PIL import Image

def create_canvas():
    """
    :return: a A4 format canvas
    """
    # A4纸的尺寸
    a4_size = (210, 297)  # 单位：毫米

    # 将毫米转换为像素，设置像素大小
    pixel_size = tuple(int(2.83465 * size) for size in a4_size)

    # 创建画布
    canvas = Image.new('RGB', pixel_size, (255, 255, 255))

    # 在画布上绘制图像或文本等

    # 保存画布
    canvas.save('img_cache/a4_canvas.jpg')



if __name__ == '__main__':
    create_canvas()
