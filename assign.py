n = int(input("enter the number of name do you want to put: "))
lis = []
for i in range(n):
	name = input("enter the name: ")
	lis.append(name)

c = 0

def count():
	for i in lis:
		if len(i)>=5:
			c = c + 1
			
		else:
			print("you donot have any name that have length 5.")
count()