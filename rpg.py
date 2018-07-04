from gpiozero import LED, Button
button = Button(27)
led1 = LED(4)
playerhp = 100
slimehp = 100
while playerhp > 0 :
    name = input("what is your name")
    print(name + "you wake up to the sound of lightning, and a horn WAR you think")
    bob = input("do you A fight,or B cower")

    if bob == "A":
        print("you fight and are loyal to the king but you die. game over")
        playerhp = 0
        break
    
    if bob == "B":
        print("you are alive but the town is in ruins" + "/n")
     
    
    
    joe = input('do you A go out,or B stay')
    if joe == "A":
        print("you incounter slime!")
    else:
        print("an ork comes and kills you")

    playerhp = 0

    print(name+ str(playerhp) + "/n")
    print("slimehp:" + str("slimehp") + "/n")
        
    hitbutton = input('press button to hit the beast')
    button.wait_for_press()
    print("you hit the monster")
    slimehp = 0
        
        
    if slimehp == 0:
        if random.radiant(1,2) == 1:
                print("The slime hit you")
                playerhp -=20
        else:
                break


if playerhp > 0:
    print ("you defeated the monster")
else:
    print("you died")