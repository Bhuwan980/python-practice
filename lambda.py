# f = lambda a: a*a

# result = f(10)

# print(result)

a = lambda : print("the sum of three variable is:")
result = a()
print(result)


def square(a,b,c):
	return lambda x: a*x*x + b*x + c 
result = square(1,4,6)
s = result(1)
print(s)