# def student(*args):
# 	print("your details is: ")
# 	if len(args) == 3:
# 		print("name: ",name ,"id:",ids,"roll: ",roll)
#     else:
#     	print("name: ",name ,"id:",ids)

# name = input("enter your name: ")
# ids = input("enter your id: ")
# roll = input("enter your roll: ")
# list1 = [name,ids,roll]

# student(*list1)

dicto = {"bhuwan":100,"hulk":101,"thor":105,"iron man":80,"scarllet witch":175}
def marvel(**kwarg):
	print("name","     ","rank")
	print("---------------------")
	for key,value in kwarg.items():

		print(key,":",value)

marvel(**dicto)