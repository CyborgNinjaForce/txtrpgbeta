iplayerhp = 100
slimehp = 100
while playerhp > 0 :
    name = input("what is your name? ")
    print(name + "you wake up to the sound of lightning, and the horns of war!")
    bob = input("do you choose to fight,or cower?")

    if bob == "fight":
        print("you fight and are loyal to the king but you die." +"/n" + "GAME OVER")
        playerhp = 0
        break
    
    if bob == "cower":
        print("you are alive but the town is in ruins" + "/n")
     
    
    
    joe = input('do you GO out,or STAY')
    if joe == "go":

        print("you incounter slime!")

    print(name+ str(playerhp) + "/n")
    print("slimehp:" + str("slimehp") + "/n")
        
    hitbutton = input('press button to hit the beast')
    button.wait_for_press()
    print("you hit the monster")
    slimehp = 0
cd         
        
    if slimehp == 0:
        if random.radiant(1,2) == 1:
                print("The slime hit you")
                playerhp -=20
        else:
                break
            
                              
   

if playerhp > 0:
    print ("you defeated the monster")
else:
    print ("You have died. /n GAMEOVER")





