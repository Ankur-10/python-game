  
import random

def game(comp,user):

    if comp==user:
        return None
    elif comp==1:
        if user==2:
            return True
        elif user==3:
            return False
    elif comp==2:
        if user==1:
            return False
        elif user==3:
            return True
    elif comp==3:
        if user==1:
            return True
        elif user==2:
            return False


print(''' here 1 shows stone 
      2 shows paper
      3 shows scissors''')
user=int(input("user wish :"))
comp=random.randint(1,3)
print(comp)

a=game(comp,user)

print("computer chooses " + str(comp))
print("user chooses " + str(user))
if a==None:
    print("its a tie")
elif a==True:
    print("user win")
elif a==False:
    print("computer win")
