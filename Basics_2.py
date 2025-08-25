def learning(*args, **kwargs):
    print(args) 
    print(kwargs)

learning("hello" , "world" , name = "Chirag" , surname = "Sharma") 
# ('hello', 'world')
# {'name': 'Chirag', 'surname': 'Sharma'}

#------------------------------------------------------------------

num = [1,2,3,4,5,6,7,8,9] 
ans = list(filter(lambda n : (n%2==0),num))
print(ans)  #[2, 4, 6, 8]

#------------------------------------------------------------------

def solve(name):
    """Mein toh seekh rha hun"""
    print("Hula")

print(solve.__doc__) # Very first 3 cotted line
print(solve.__name__) # just its name
#------------------------------------------------------------------
states = ["Himachal Pradesh", "Goa" ," Uttar Pradesh" , "Assam" , "Madhya Pradesh"]
ans = [state for state in states if "Pradesh" in state]
print(ans) # List Comprehension
#------------------------------------------------------------------
