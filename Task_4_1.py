#Solution for G

import sys

max_1 = None
max_2 = None
counter = 0

a = int(input())
max_1 = a
for line in sys.stdin:

	line = line.strip()

	if not line:
		break

	a = int(line)

	if a != max_1 and counter < 1:
		counter += 1
		max_2 = a
	if max_1 < max_2:
		max_1, max_2 = max_2, max_1
	if a > max_1:
		max_2 = max_1
		max_1 = a
	elif a > max_2 and max_1 != a:
		max_2 = a


	print(max_1, max_2)
print(max_2, max_1)