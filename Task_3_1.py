# Solution for F

import sys

max_count = 0
count = 0

k = 0

for line in sys.stdin:

	line = line.strip()

	if not line:
		break

	a = int(line)
	if k < 1:
		temp = a
		count += 1
		max_count = count
	k = 1

	if (a > temp):
		count += 1
		if max_count < count:
			max_count = count
	elif a < temp:
		count = 0
	
	temp = a

print(max_count)