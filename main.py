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
enemies_types=["scout(s)", "scout(s)", "scout(s)", "scout(s)", "scout(s)", "destroyer(s)", "destroyer(s)", "battleship(s)"]
creds=5
credonium=1
credonium_price=5
days=0
defense=1
scouts=5
destroyers=2
battleships=1
titans=0
torpedoes=3
income=5
dcost=15
icost=10
bg_music.play(100)

enemy_arrogantness=0
enemy_is_partly_destroyed=0
losts=0
trader_event=60+random.randint(0, 10)
a_gamer_event=23+random.randint(0, 10)
player_inv=[scouts, destroyers, battleships, torpedoes, creds, credonium]

is_armor_advanced=False
is_AA_built=False
is_AA_upgraded=False
is_credonium_buildings=False
is_income_in_credonium=False
is_building_advanced=False
is_building_titans=False
is_torpedoes_upgraded_once=False
print("________________________________________________________________________________________________________________________________________________")
print(" You are last space station in this sector.")
print("We have sent you some support, but it will arrive only after 100 days.")
print("We also spotted an enemy outpost nearby, so be careful")
print("________________________________________________________________________________________________________________________________________________")
print(" Controls:")
print("Type \"i\" if you need to upgrade your income per one day.")
print("Type \"d\" if you need to upgrade your defense.")
print("You can buy credonium (type \"b\") and sell it later (type \"s\") for a better price.")
print("Also you can build some ships - type \"inf_ships\" for more information!")
print("You can use a torpedo (type \"t\") to destroy all enemies that will arrive in next 3 days.")
print("Type \"Btorp\" to build 1 torpedo, it costs 50 creds.")
print("Your objective is to survive 100 days.")
print("Good luck!")
print("________________________________________________________________________________________________________________________________________________")
for i in range(100):
    event=pg.event.get()
    enemy=random.choice(enemies)-random.randint(-1, 1)
    enemy_type=random.choice(enemies_types)
    print("                    Day", days)
    creds+=income
    credonium_price+=random.randint(-2, 2)
    if credonium_price<=0:
        credonium_price=10
    if credonium_price>10:
        credonium_price=1
    if enemy_type=="scouts":
        enemy_arrogantness=0
    if enemy_type=="destroyers":
        enemy_arrogantness=5
    if enemy_type=="battleships":
        enemy_arrogantness=20
    print("__________________________________________________")
    print("Credits:", creds)
    print("Credonium:", credonium)
    print("Credonium costs", credonium_price, "at the moment.")
    print("Your defense is", defense)
    print("Your income per day is", income)
    if is_building_titans==False:
        print("You have", scouts, "scout(-s),", destroyers, "destroyer(-s) and", battleships, "battleship(-s).")
    if is_building_titans==True:
        print("You have", scouts, "scout(-s),", destroyers, "destroyer(-s),", battleships, "battleship(-s) and", titans, "titans.")
    print("You have", torpedoes, "torpedoes.")
    print("__________________________________________________")
    print("Available researches:")
    if is_armor_advanced==False:
        print("Advanced armor (+1 defense, type \"R1\") - 10 creds, 2 credonium")
    if is_AA_built==False:
        print("AA (defends against scouts, type \"R2\") - 15 creds, 3 credonium")
    if is_AA_built==True and is_AA_upgraded==False:
        print("AA upgrade (defends against scouts and + 2 defense, type \"R3\") - 30 creds, 5 credonium")
    if is_credonium_buildings==False:
        print("Explore credonium (unknown result, type \"R4\") - 25 creds, 10 credonium")
    if is_credonium_buildings==True and is_income_in_credonium==False:
        print("Credonium production (+1 credonium per 1 day, type \"R5\") - 70 creds, 5 credonium")
    if is_building_advanced==False:
        print("Advanced building (reduces ships' cost by 5 creds, type \"R6\") - 30 creds, 3 credonium")
    if is_building_titans==False and is_building_advanced==True:
        print("Building titans (allows you to build much larger ships, type \"R7\") - 50 creds, 10 credonium")
    if is_torpedoes_upgraded_once==False and is_building_advanced==True:
        print("Advanced torpedoes (+1 day without enemies, type \"R8\") - only 15 creds")
    print("__________________________________________________")
    print("Defense upgrade cost:", dcost)
    print("Income upgrade cost:", icost)
    print("__________________________________________________")
    if enemy_is_partly_destroyed!=0:
        enemy=0
    if enemy!=0:
        print("You have been attacked by", enemy, "enemy", enemy_type+".")
        if defense>=enemy and enemies!=0:
            print("You successfully destroyed them.")
            new_day.play()
        elif defense<enemy and enemies!=0:
            if enemy_type=="scouts" and is_AA_built==True and enemy>=3:
                print("You successfully destroyed them.")
                new_day.play()
            if enemy_type=="scouts" and is_AA_upgraded==True and enemy>=5:
                print("You successfully destroyed them.")
                new_day.play()
            else:
                losts=days+enemy_arrogantness
                print("You failed. Enemies have taken some of your credits.")
                print(losts, "credits lost")
                creds-=losts
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
    if days==a_gamer_event:
        print("A strange man just appeared in front of you.")
        print("- Call me the Gamer. I can give you some creds, or you can give them to me.")
        print("- Do you want to play a game?")
        print("Type \"y\" to accept this offer.")
    if days==100:
        enemy=23-defense
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
            print("__________________________________________________")
    if days==90:
        print(" Our fleet is on its way, 10 days until rescue.")
    if enemy_is_partly_destroyed>0:
        enemy_is_partly_destroyed-=1
    if is_income_in_credonium==True:
        credonium+=1
    
# ACTIONS ACTIONS ACTIONS ACTIONS ACTIONS ACTIONS ACTIONS ACTIONS ACTIONS ACTIONS

    action=str(input("Your action: "))
    if action=="d":
        if creds>=dcost:
            creds-=dcost
            defense+=1
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
    if action=="t" and torpedoes>0:
        torpedoes-=1
        if is_torpedoes_upgraded_once==False:
            enemy_is_partly_destroyed=3
        else:
            enemy_is_partly_destroyed=4
    if action=="Btorp" and creds>=50:
        torpedoes+=1
        creds-=50

# RESEARCHES RESEARCHES RESEARCHES RESEARCHES RESEARCHES RESEARCHES RESEARCHES RESEARCHES RESEARCHES RESEARCHES

    if action=="R1" and creds>=10 and credonium>=2 and is_armor_advanced==False:
        credonium-=2
        creds-=10
        defense+=1
        is_armor_advanced=True
        print("Successfully researched advanced armor, defense increased by 1.")
    if action=="R2" and creds>=15 and credonium>=3:
        creds-=15
        credonium-=3
        is_AA_built=True
        print("Successfully researched AA, now you can defend against scouts.")
    if action=="R3" and creds>=30 and credonium>=5 and is_AA_built==True:
        creds-=30
        credonium-=5
        defense+=2
        is_AA_upgraded=True
        print("Successfully upgraded AA, its strength increased, damage increased by 2.")
    if action=="R4" and creds>=20 and credonium>=10:
        creds-=20
        credonium-=10
        is_credonium_buildings=True
        print("Congratulations, now we know how to produce credonium!")
    if action=="R5" and creds>=70 and credonium>=5 and is_credonium_buildings==True:
        creds-=70
        credonium-=5
        is_income_in_credonium=True
        print("Congratulations, now we can produce credonium!")
    if action=="R6" and creds>=30 and credonium>=3:
        creds-=30
        credonium-=3
        is_building_advanced=True
        print("Successfully upgraded docks, all ships' cost decreased by 5.")
    if action=="R7" and creds>=50 and credonium>=10 and is_building_advanced==True:
        creds-=50
        credonium-=10
        is_building_titans=True
        print("Now you can build titans!")
    if action=="R8" and creds>=15:
        creds-=15
        is_torpedoes_upgraded_once=True

# SHIPS SHIPS SHIPS SHIPS SHIPS SHIPS SHIPS SHIPS SHIPS SHIPS

    if action=="inf_ships":
        print(" Building ships:")
        print("Scout - type \"Bs\", costs 5 creds and 1 credonium.")
        print("Destroyer - type \"Bd\", costs 15 creds and 3 credonium.")
        print("Battleship - type \"Bb\", costs 40 creds and 5 credonium.")
        print("Titan - type \"Bt\", costs 100 creds and 23 credonium.")
        print(" Ships' parameters:")
        print("Scout - damage 2, defense 1-2")
        print("Destroyer - damage 3-4, defense 2-4")
        print("Battleship - damage 4-5, defense 3-5")
        print("Titan - damage 3-8, defense 4-6")

    if action=="Bs" and creds>=5 and credonium>=1:
        scouts+=1
        if is_building_advanced==False:
            creds-=5
        credonium-=1
    if action=="Bd" and creds>=15 and credonium>=3:
        destroyers+=1
        if is_building_advanced==False:
            creds-=15
        else:
            creds-=10
        credonium-=3
    if action=="Bb" and creds>=40 and credonium>=5:
        battleships+=1
        if is_building_advanced==False:
            creds-=40
        else:
            creds-=35
        credonium-=5
    if action=="Bt" and creds>=100 and credonium>=23 and is_building_titans==True:
        titans+=1
        if is_building_advanced==False:
            creds-=100
        else:
            creds-=95
        credonium-=23

# DEBUGGER DEBUGGER DEBUGGER DEBUGGER DEBUGGER DEBUGGER DEBUGGER DEBUGGER DEBUGGER DEBUGGER
    if torpedoes<0:
        torpedoes=0
    if credonium<0:
        credonium=0
    if scouts<0:
        scouts=0
    if destroyers<0:
        destroyers=0
    if battleships<0:
        battleships=0

    #RANDOM EVS        
    if days==trader_event and action=="y" and creds>=50:
        creds-=50
        credonium+=10
    if days==trader_event and action=="y" and creds<50:
        print("You don't have enough money.")
    if days==a_gamer_event and action=="y":
        creds+=random.randint(-100, 100)