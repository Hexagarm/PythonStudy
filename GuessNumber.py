lucky_number = 20
guess = 5

print("您有", guess, "次机会")
print("*********************")

while guess > 0:
	guess_number = int(input("输入您的幸运数字:"))
	print("*********************")

	if guess_number < lucky_number:
		print("小啦！")
	elif guess_number > lucky_number:
		print("大啦！")
	else:
		print("Bingo")
		break

	print("还剩下", guess-1, "次")
	print("*********************")
	guess -= 1
	pass
