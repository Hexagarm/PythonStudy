# -*- coding: utf-8 -*-

height = float(input("输入您的身高:"))
weight = float(input("输入您的体重:"))

BMI = weight / (height*height)

if BMI < 18.5:
	print("过轻")
elif (18.5 < BMI) and (BMI < 25):
	print("正常")
elif (25 < BMI) and (BMI < 28):
	print("过重")
elif (28 < BMI) and (BMI < 32):
	print("肥胖")
else:
	print("严重肥胖")
	pass