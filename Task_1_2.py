#Taylor with custom functions

def factorial(n):				# Factorial function
	fact = 1
	for i in range(1, n + 1):
		fact *= i	
	return fact

def Taylor(a, n):				# Taylor function
 	res = 0
 	temp = 1
 	for i in range(1, n + 1):
 		res += a ** temp / factorial(temp) * (-1) ** (i + 1)
 		temp += 2
 	return res

a = float(input())				# Angle (radians)
n = int(input())				# Number of summands


print("%.6f" %Taylor(a,n))