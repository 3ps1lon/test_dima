#Taylor with loop

a = float(input())		# Angle (radians)
n = int(input())		# Number of summands

res = 0
temp = 1

for i in range(1, n + 1):
	fact = 1
	for j in range(1, temp + 1):
		fact *= j

	res += a ** temp / fact * (-1) ** (i + 1)
	temp += 2
print("%.6f" %res)
