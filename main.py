num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
N = len(num1) 
M = len(num2) 

if N<M:
	num3 = num1 + num2
else:
	num3 = num2 + num1
print (num3)

