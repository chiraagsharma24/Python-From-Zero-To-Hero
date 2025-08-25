# for virtual environment :
# python -m venv .venv
# .venv\Scripts\activate
# deactivate
# pip install -r requirements.txt
#-----------------------------------------------------
# any file with __init__.py is known as packages
# everything is object in python
#-----------------------------------------------------
name = "Chirag"
print(f"My name is {name}") #f-string
#-----------------------------------------------------
friends = set() # {} - use this
print(id(friends)) 
print(friends) 
friends.add("Chirag")
friends.add("Harshit")
print(id(friends)) #Mutable
print(friends)  # | - union , & - intersection , - , 
#-----------------------------------------------------
name = "Chirag Sharma" # String - immutable
print(name[:6])
print(name[7:])
#-----------------------------------------------------
friends = ('H','A','S','R') #tuples - immutable - () - use this
(f1,f2,f3,f4) = friends 
print(f"name is {f1}")
print(f"Is C in friends {'C' in friends}") #false
print(f"Is A in friends {'A' in friends}") #true
#-----------------------------------------------------
animals = ["Dog","cat","horse"] # lists - mutable
birds = ["Crow","Pigeon", "Parrot"]
animals.append("Lion") # adding
animals.remove("Dog") # removing
animals.extend(birds)  # merge 2 lists
#-----------------------------------------------------
students = {"C":24 , "A" :13 , "H" : 46}
del students["C"]
print(students["H"])
print(students.keys())
print(students.values())
print(students.items())
#-----------------------------------------------------
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
for idx,day in enumerate(days,start=1):
    print(f"{idx} : {day}")
#-----------------------------------------------------
names = ['Sam','Ram','Dam','Kaju']
marks = [45,25,27,73]
for idx, mark in zip(names,marks):
    print(f"{idx} : {mark}") 
#-----------------------------------------------------
# nonlocal - just above, global - everywhere