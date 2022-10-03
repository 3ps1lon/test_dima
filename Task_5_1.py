# Solution for H

def dec_bin(x):
	counter = 0
	binary = 0
	while x > 0:
		binary = ((x % 2) * (10 ** counter)) + binary
		x = int(x / 2)
		counter += 1
	binary = str(binary)
	return binary

def more_null(x):
	while len(x) != 32:
		x = '0' + x
	return x

a = int(input())
b = int(input())

text = str(more_null(dec_bin(a)))[-b::]
print(int(text,2))