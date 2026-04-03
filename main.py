import random
import time
import pygame as pg
pg.init()
victory=pg.mixer.Sound("SOUNDS and MUSIC/Victory_sound.mp3")
small_defeat=pg.mixer.Sound("SOUNDS and MUSIC/Small_fail_sound.mp3")
new_day=pg.mixer.Sound("SOUNDS and MUSIC/Small_victory_sound.wav")
bg_music=pg.mixer.Sound("SOUNDS and MUSIC/Background_music.mp3")
defeat=pg.mixer.Sound("SOUNDS and MUSIC/Fail_sound.mp3")
enemies=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 5, 5, 5, 10, 10]
creds=5
credonium=1
credonium_price=5
days=0
damage=1
income=5
dcost=15
icost=10
bg_music.play(100)
trader_event=60+random.randint(0, 10)
is_armor_advanced=False
print("________________________________________________________________________________________________________________________________________________")
print(" You are last space station in this sector.")
print("We have sent you some support, but it will arrive only after 100 days.")
print("We also spotted an enemy outpost nearby, so be careful")
print("________________________________________________________________________________________________________________________________________________")
print(" Controls:")
print("Type \"i\" if you need to upgrade your income per one day.")
print("Type \"d\" if you need to upgrade your damage.")
print("You can buy credonium (type \"b\") and sell it later (type \"s\") for a better price.")
print("Your objective is to survive 100 days.")
print("Good luck!")
print("________________________________________________________________________________________________________________________________________________")
for i in range(100):
    enemy=random.choice(enemies)-random.randint(-1, 1)
    print("                    Day", days)
    creds+=income
    credonium_price+=random.randint(-2, 2)
    if credonium_price<=0:
        credonium_price=10
    if credonium_price>10:
        credonium_price=1
    print("__________________________________________________")
    print("Credits:", creds)
    print("Credonium:", credonium)
    print("Credonium costs", credonium_price, "at the moment.")
    print("Your damage is", damage)
    print("Your income per day is", income)
    print("__________________________________________________")
    print("Available researches:")
    if is_armor_advanced==False:
        print("Advanced armor (+1 damage, type \"R1\") - 10 creds, 2 credonium")
    print("__________________________________________________")
    print("Damage upgrade cost:", dcost)
    print("Income upgrade cost:", icost)
    print("__________________________________________________")
    if enemy!=0:
        print(enemy, "enemy ships attack you.")
        if damage>=enemy and enemies!=0:
            print("You successfully destroyed them.")
            new_day.play()
        else:
            print("You failed. Enemies have taken some of your credits.")
            print(days, "credits lost")
            creds-=days
            print("Now you have only", creds, "credits.")
            small_defeat.play()
    if enemy==0:
        print("You have not been attacked. Rest while you can.")
        new_day.play()
    if days==50:
        print(" One of our cargo ships reached the station.")
        print("You have earned 250 credits.")
        creds+=250
        print("Now you have", creds+125, "credits.")
    days+=1
    if days==trader_event:
        print(" You spotted a merchant ship.")
        print("He offers you 10 credonium for only 50 creds.")
        print("Type \"y\" to accept this offer.")
    if days==100:
        enemy=23-damage
        if creds>=0:
            time.sleep(3)
            victory.play(2)
            print("__________________________________________________")
            print("")
            print("Congrats, you won!!!")
            print("")
            print("__________________________________________________")
        if creds<0:
            time.sleep(1)
            defeat.play()
            print("__________________________________________________")
            print("")
            print("You died from debt collectors...")
            print("")
            print("__________________________________________________")
        if days==90:
            print(" Our fleet is on its way, 10 days until rescue.")
    


    action=str(input("Your action: "))
    if action=="d":
        if creds>=dcost:
            creds-=dcost
            damage+=1
        dcost=15+days
    if action=="i":
        if creds>=icost:
            creds-=icost
            income+=1
        icost=10+days
    if action=="b":
        if creds>=credonium_price:
            credonium+=1
            creds-=credonium_price
    if action=="CHEATER!!!":
        creds+=1000
        income=0
    if action=="s":
        if credonium>0:
            credonium-=1
            creds+=credonium_price
    if action=="R1" and creds>=10 and credonium>=2 and is_armor_advanced==False:
        credonium-=2
        creds-=10
        damage+=1
        is_armor_advanced=True
        print("Successfully researched advanced armor, damage increased by 1.")



    #RANDOM EVS        
    if days==trader_event and action=="y" and creds>=50:
        creds-=50
        credonium+=10
    if days==trader_event and action=="y" and creds<50:
        print("You don't have enough money.")