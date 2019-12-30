# def fact():
# 	n = int(input("enter the number: "))
# 	f = 1
# 	for i in range(1, n+1):
# 		f = f*i
# 	print(f)

def fact(n):
	if (n==0):
		return 1
	else: 
		return n * fact(n-1)
n = int(input("enter the number do you want to get the factorial of number: "))
result = fact(n)
print(result)
