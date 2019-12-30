# l1 = [1,2,3,4,5]
# class maths:
# 	def __init__(self,n1):
# 		self.n1 = n1
		
# 	def add(self):
# 		return self.n1 + 3
# 	def subtract(self):
# 		return self.n1 - 3
# 	def multiplication(self):
# 		return self.n1 * 3
# 	def divide(self):
# 		return self.n1 / 3
# 	def remainder(self):
# 		return self.n1 % 3 

# 	print("1> addition 2>subtract 3>multiplication 4> divide 5> remainder")
# 	choice = int(input("enter your choice: "))
# 	print("your choice is: ",choice)
# 	if choice==1:
# 		print(list(map(add, l1)))
# 	elif choice==2:
# 		print(list(map(subtract, l1)))
# 	elif choice==3:
# 		print(list(map(multiplication, l1)))
# 	elif choice==4:
# 		print(list(map(divide, l1)))
# 	elif choice==5:
# 		print(list(map(remainder, l1)))
# 	else:
# 		print("please enter valid input.")
		

# obj = maths()



lists = [1,2,3,4,5]

print(list(map(lambda x: x+1, lists)))