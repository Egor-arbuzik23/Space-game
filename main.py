import random
import time
import pygame as pg
pg.init()
victory=pg.mixer.Sound("SOUNDS and MUSIC/Victory_sound.mp3")
small_defeat=pg.mixer.Sound("SOUNDS and MUSIC/Small_fail_sound.mp3")
new_day=pg.mixer.Sound("SOUNDS and MUSIC/Small_victory_sound.wav")
bg_music=pg.mixer.Sound("SOUNDS and MUSIC/Background_music.mp3")
defeat=pg.mixer.Sound("SOUNDS and MUSIC/Fail_sound.mp3")
torpedo=pg.mixer.Sound("SOUNDS and MUSIC/torpedoe.mp3")
research=pg.mixer.Sound("SOUNDS and MUSIC/research.mp3")
the_Gamer=pg.mixer.Sound("SOUNDS and MUSIC/scary.mp3")
inf_ships=pg.mixer.Sound("SOUNDS and MUSIC/inf_ships sound.mp3")
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
action=None
player_ship=""
player_ship_active=""
#bg_music.play(100)

enemy_arrogantness=0
enemy_is_partly_destroyed=0
losts=0
trader_event=60+random.randint(0, 10)
a_gamer_event=23+random.randint(0, 10)
player_inv=[scouts, destroyers, battleships, torpedoes, creds, credonium]
enemy_damage=0
enemy_defense=0
player_damage_b=0
player_defense_b=0
reward_b=0

is_armor_advanced=False
is_AA_built=False
is_AA_upgraded=False
is_credonium_buildings=False
is_income_in_credonium=False
is_building_advanced=False
is_building_titans=False
is_torpedoes_upgraded_once=False
battle=False
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
    scout_damage=2
    scout_defense=random.randint(1, 2)
    destroyer_damage=random.randint(3, 4)
    destroyer_defense=random.randint(2, 4)
    battleship_damage=random.randint(4, 5)
    battleship_defense=random.randint(3, 5)
    titan_damage=random.randint(3, 8)
    titan_defense=random.randint(4, 6)
    event=pg.event.get()
    enemy=random.choice(enemies)-random.randint(-1, 1)
    reward_b=enemy
    enemy_type=random.choice(enemies_types)
    if enemy_type=="scout(s)":
        enemy_damage=scout_damage
        enemy_defense=scout_defense
    if enemy_type=="destroyer(s)":
        enemy_damage=destroyer_damage
        enemy_defense=destroyer_defense
    if enemy_type=="battleship(s)":
        enemy_damage=battleship_damage
        enemy_defense=battleship_defense
    if enemy_type=="titan(s)":
        enemy_damage=titan_damage
        enemy_defense=titan_defense
    print("                    Day", days)
    if action!="inf_ships" or battle==False:
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
    if not battle:
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
    if enemy!=0 and action!="inf_ships":
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
                losts=enemy_arrogantness+days
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
    if action!="inf_ships":
        days+=1
    if days==trader_event:
        print(" You spotted a merchant ship.")
        print("He offers you 10 credonium for only 50 creds.")
        print("Type \"y\" to accept this offer.")
    if days==a_gamer_event:
        the_Gamer.play()
        print("A strange man just appeared in front of you.")
        print("- Call me the Gamer. I can give you some creds, or you can give them to me.")
        print("- Do you want to play a game?")
        print("Type \"y\" to accept this offer.")
        time.sleep(2)
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
            print("")
            print("")
            print("")
            print("        |EXIT|")
            print("   O")
            print("  /|\\_")
            print("  ||")
            print(" _/\\")
            print("    |")
    if days==90:
        print(" Our fleet is on its way, 10 days until rescue.")
    if enemy_is_partly_destroyed>0:
        enemy_is_partly_destroyed-=1
    if is_income_in_credonium==True:
        credonium+=1
    if action=="battle" and enemy!=0:
        battle=True
    if battle==True:
        print(" You've entered the battle mode.")
        if is_building_titans==False:
            print("At first, choose your ship. (scout - \"s\", destroyer - \"d\", battleship - \"b\")")
        else:
            print("At first, choose your ship. (scout - \"s\", destroyer - \"d\", battleship - \"b\", titan - \"t\")")
        print("Then, type \"a\" (attack) to attack enemies.")
        print("If you type \"e\" (exit) you'll lose 5 creds, but you'll also exit this fight if it's so annoying.")
    while battle:
        print("You fight against", enemy, "enemy", enemy_type)
        if not player_ship=="s" or not player_ship=="d" or not player_ship=="b" or not player_ship=="t":
            player_ship=str(input("Choose your ship: "))
# UPGRADE THIS NOW
            if player_ship=="s" and scouts>=1:
                player_ship_active="scout(s)"
            if player_ship=="d" and destroyers>=1:
                player_ship_active="destroyer(s)"
            if player_ship=="b" and battleships>=1:
                player_ship_active="battleship(s)"
            if player_ship=="t" and titans>=1:
                player_ship_active="titan(s)"
# UPGRADE THIS NOW
        if player_ship_active=="scout(s)":
            player_damage_b=scout_damage
            player_defense_b=scout_defense
        if player_ship_active=="destroyer(s)":
            player_damage_b=destroyer_damage
            player_defense_b=destroyer_defense
        if player_ship_active=="battleship(s)":
            player_damage_b=battleship_damage
            player_defense_b=battleship_defense
        if player_ship_active=="titan(s)":
            player_damage_b=titan_damage
            player_defense_b=titan_defense
        battle_action=str(input("Your battle action: "))
        if battle_action=="e":
            battle=False
        if battle_action=="a":
            if player_damage_b>=enemy_defense:
                enemy-=1
                if enemy==0:
                    battle=False
                    print("You won this battle, but not this war. You gained", reward_b, "creds.")
                    creds+=reward_b
                else:
                    print("I hit one!")
            if enemy_damage>=player_defense_b:
                print("Your ship has been shot down, choose another one.")
                creds-=1
                if player_ship_active=="scout(s)":
                    if scouts>=1:
                        scouts-=1
    
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
        torpedo.play()
        if is_torpedoes_upgraded_once==False:
            enemy_is_partly_destroyed=3
        else:
            enemy_is_partly_destroyed=4
    if action=="Btorp" and creds>=50:
        torpedoes+=1
        creds-=50

# RESEARCHES RESEARCHES RESEARCHES RESEARCHES RESEARCHES RESEARCHES RESEARCHES RESEARCHES RESEARCHES RESEARCHES

    if action=="R1" and creds>=10 and credonium>=2 and is_armor_advanced==False:
        research.play()
        credonium-=2
        creds-=10
        defense+=1
        is_armor_advanced=True
        print("Successfully researched advanced armor, defense increased by 1.")
    if action=="R2" and creds>=15 and credonium>=3:
        research.play()
        creds-=15
        credonium-=3
        is_AA_built=True
        print("Successfully researched AA, now you can defend against scouts.")
    if action=="R3" and creds>=30 and credonium>=5 and is_AA_built==True:
        research.play()
        creds-=30
        credonium-=5
        defense+=2
        is_AA_upgraded=True
        print("Successfully upgraded AA, its strength increased, damage increased by 2.")
    if action=="R4" and creds>=20 and credonium>=10:
        research.play()
        creds-=20
        credonium-=10
        is_credonium_buildings=True
        print("Congratulations, now we know how to produce credonium!")
    if action=="R5" and creds>=70 and credonium>=5 and is_credonium_buildings==True:
        research.play()
        creds-=70
        credonium-=5
        is_income_in_credonium=True
        print("Congratulations, now we can produce credonium!")
    if action=="R6" and creds>=30 and credonium>=3:
        research.play()
        creds-=30
        credonium-=3
        is_building_advanced=True
        print("Successfully upgraded docks, all ships' cost decreased by 5.")
    if action=="R7" and creds>=50 and credonium>=10 and is_building_advanced==True:
        research.play()
        creds-=50
        credonium-=10
        is_building_titans=True
        print("Now you can build titans!")
    if action=="R8" and creds>=15:
        research.play()
        creds-=15
        is_torpedoes_upgraded_once=True
        print("Successfully upgraded torpedoes.")

# SHIPS SHIPS SHIPS SHIPS SHIPS SHIPS SHIPS SHIPS SHIPS SHIPS

    if action=="inf_ships":
        inf_ships.play()
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