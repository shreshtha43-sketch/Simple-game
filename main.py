import random

print("Hii coder,It's time for some fun!😎")

def dice():
    print("Great!let's play (Roll the dice🎲) then..")
    player=input("Press enter to roll the dice:")
    if(player==""):
        dice=random.randint(1,6)
        print(f"You rolled:{dice}")
    return 

def SPS():
     print("Great!let's play (Stone-Paper-Scissors✂️) then..")
     d={1:"Stone",
        2:"Paper",
        3:"Scissors"}
     c=random.randint(1,3)
     print("Computer has played it's turn")
     p=int(input("Your turn..(1-Stone-2-Paper-3-Scissors):"))
     if(p-c==1 or p-c==-2):
        print(f"You won!🎉..Computer chose {d[c]},You chose {d[p]}")
     elif(p==c):
        print(f"Draw,you both chose {d[p]}")
     else:
        print(f"You lose!😢..Computer chose {d[c]},You chose {d[p]}")
    
     return



while True:
    print("1-Roll the dice "
        "2-Stone-Paper-Scissors ")
    c=int(input("which game do you wanna play❓\n"))
    if(c==1):
        dice()
    
    elif(c==2):
        SPS()
 
    else:
        print("No such command exist")
    coun=input("Want to continue?\n")
    if(coun.lower()!="yes"):
        break
        









