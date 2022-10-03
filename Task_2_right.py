#Find E

res = 0
count = 0

while True:
	a = int(input())

	if (a == 0):
		break
	if res == 0:
		res += a
	elif count == 1:
		b = int(input())
		if (b == 0):
			res += a
			break

		res += a * b
		count = 0

	count += 1

print(res)