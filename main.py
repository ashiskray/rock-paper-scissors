'''
rock=1
paper=-1
scissor=0
'''
import random 
computer=random.choice([1,0,-1])
youstr=input("entr your choice: ")
youdict={"rock":1, "paper":-1, "scissor":0}
reversedict={1:"rock", -1:"paper", 0:"scissor"}
you=youdict[youstr]
print(f"you chose {youstr}\n computer choose {reversedict[computer]}")
if (computer==1 and you == 1):
    print ("its a draw try again !")
elif (computer==1 and you == -1):
    print (" congrats ! you win  !")
elif (computer==1 and you == 0):
    print (" you lose ! try again !")
elif (computer==0 and you == 0):
    print (" its a draw try again!")
elif (computer==0 and you == 1):
    print (" congrats ! you wwin !")
elif (computer==0 and you == -1):
    print (" you lose ! try again !")
elif (computer==-1 and you == -1):
    print ("its a draw try again !")
elif (computer==-1 and you == 0):
    print (" congrats ! you win  !")
elif (computer==-1 and you == 1):
    print (" you lose! try again !")

else:
    print("something went worng !")