import math
x = str(math.factorial(100))
sum_digit = 0

for i in range(len(x)):
	sum_digit += int(x[i])
print(sum_digit)
