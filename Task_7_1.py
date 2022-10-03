# Solution for J

try:
	x = input()
	x = float(x)
	while x != 0:
		while x % 2 == 0:
			print("%.5f" %(1/x))
			break
		while x % 2 != 0:
			print("Not an even number!")
			break
		break
	while x == 0:
		print("Zero division error!")
except (TypeError, ValueError):
	print('String "%s" is not number.' % (x))