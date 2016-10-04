#! /usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFont


def stamp_num(img, num):
    drawSurface = ImageDraw.Draw(img)	#创建一个绘画图形
    print (img.size) #打印图片尺寸
    numFont = ImageFont.truetype("simsun.ttc", 300)#设置字体
    drawSurface.text((500, 0), num, font=numFont, fill=(255, 0, 0))#写字)
    img.save("C:\\Users\\ZhanGe\\Downloads\\1234.png", "png")
    img.show()	#显示图片


if __name__ == '__main__':
    img = Image.open("C:\\Users\\ZhanGe\\Downloads\\123.png")
    number = input("请输入您要写的数值:")
    stamp_num(img, number)