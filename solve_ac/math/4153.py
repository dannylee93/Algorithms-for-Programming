# 직각삼각형 : 피타고라스 정의

while True:
	a, b, c = map(int, input().split())
	if a == 0 and b == 0 and c == 0:
		break
	if (a ** 2) + (b ** 2) == (c ** 2):
		print("right")
	else:
		print("wrong")