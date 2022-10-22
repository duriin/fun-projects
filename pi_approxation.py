#sum of 1/n^2 = pi^2/6
import math 

n = 1
s = n

while True:
	n += 1
	s += 1/(n*n)
	if n == 5000: #the more numbers, the more accurate
		break

print(math.sqrt(6*s))