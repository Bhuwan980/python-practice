"""
my_list = [1,2,3,4,54,6,7,8]
print(len(my_list))

for i in enumerate(my_list):
    print(i)
    
    """
    ############################################
    ###########################################
    ############################################
    ###########################################
    
"""    

class employee():
    na = "name"
   
bhuwan = employee()
hulk = employee()
bhuwan.name = "bhuwna"
bhuwan.classs = "csit 5th sem"
bhuwan.rank  = "1st"
employee.na = "tell me somthing i don't know"
print(bhuwan.__dict__)#__dict__ display the parameter in object 

hulk.name = "monster"
hulk.rank = "100"
hulk.power = "smash"  


 """
##################################################
 #if function doesn't return anything the it gives none
 ##################################################
"""
class school:
        
    def __init__(self):
        pass
   
    def classes(self):
            return "this is class room"   
    def canteen(self):
            return("this is canteen")   
    def ground(self):
            return("this is ground")
        
    def reception(self):
            return("this is reception")
       
    def library(self):
            return("this is library")

print("1> classes 2> canteen 3>ground 4>reception 5>library ")
choice = int(input("enter your choice: "))
o = school()

if choice == 1:
    print(o.classes())
elif choice == 2:
    print(o.canteen())
elif choice == 3:
    print(o.ground())
elif choice == 4:
    print(o.reception())
elif choice == 5:
    print(o.library())
else:
    print("please enter the valid input.")"""
    
###########################################################
    ##########################################################
    ##########################################################
    ###################################################################
    ####################################################
    
"""
class sch:
    def __init__(self,name,age,roll):
        self.name = name
        self.age = age
        self.roll = roll
    def void(self):
        return "this is bhuwan"
        
s = sch('bu',10,11)

s.name = "victor"
print(s.name)\


"""


###############################\
# class inheritance in python
###

class person:
    def __init__(self, fname,lname):
        self.fname = fname
        self.lname = lname
    def display(self):
        print(self.fname,self.lname)
class inh(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname)
        
x = inh("bhuawn","neupane")
x.display()







class practice:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("hi ",self.name,"is your age is ",self.age)

class inherit(practice):
    def __init__(self,name,age):
        super().__init__(name,age)
obj = inherit("bhuwan",19)
obj.display()




#######################################
########################################
#####################################
# iterator in python
###################################
################################################
############################




mylist = ["bhwuan","hulk","thor"]
my= iter(mylist)

print(next(my))
print(next(my))
print(next(my))
        




##################
#################
# modules in python 
###################
#############

# import mymodule

# mymodule.greeting("Jonathan")


import datetime

x = datetime.date

print(x)



##################
############
#map filter zip reduce