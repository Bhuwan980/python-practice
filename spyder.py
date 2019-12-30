"""my_list = [1,2,3,4,54,6,7,8]
print(len(my_list))

for i in enumerate(my_list):
    print(i)"""
    
    
class employee():
    na = "name"
   
bhuwan = employee()
hulk = employee()
bhuwan.name = "bhuwna"
bhuwan.classs = "csit 5th sem"
bhuwan.rank  = "1st"
employee.na = "tell me somthing i don't know"
print(bhuwan.__dict__)

hulk.name = "monster"
hulk.rank = "100"
hulk.power = "smash"

