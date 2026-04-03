import tkinter as tk
import random
import time
import pygame as pg

root=tk.Tk()
root.iconbitmap("satellite_dish_icon-icons.com_60267.ico")
root.title("Space Game")
root.geometry("800x800")
root.resizable(False, False)

pg.init()
victory=pg.mixer.Sound("Lunar Pool (Lunar Ball) – Victory_ Музыка из игры Dendy.mp3")
small_defeat=pg.mixer.Sound("Звук выбивания двери.mp3")
new_day=pg.mixer.Sound("Оповещение о начале Start Tone № 11.wav")
bg_music=pg.mixer.Sound("doomsday-lament_88023.mp3")
bg_music_newtk=pg.mixer.Sound("doug-maxwell-heartbeat-of-the-hood.mp3")
bg_music_no=pg.mixer.Sound("kevin-macleod-antechamber.mp3")
defeat=pg.mixer.Sound("a652fa61eca8500.mp3")

frame=tk.Frame(root)
frame.pack(expand=True, fill="both")

def start():
enemies=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 5, 5, 5, 10, 10]
creds=10
days=0
damage=1
income=5
dcost=15
icost=10
bg_music_no.play()
def i_upg():
    global dcost, damage, creds
    if creds>=dcost:
        creds-=dcost
        damage+=1
    dcost=15+days
label=tk.Label(frame, text=days, font="Algerian 23").grid(row=3, column=1)
def new_day_def():
    global creds, days, label
    enemy=random.choice(enemies)-random.randint(-1, 1)
    creds+=income    
    if enemy!=0:
        if damage>=enemy and enemies!=0:
            new_day.play()
        else:
            creds-=days
            small_defeat.play()
    if enemy==0:
        new_day.play()
    if days==50:
        creds+=250
    days+=1
    if days==100:
        enemy=23-damage
        if creds>=0:
            time.sleep(3)
            victory.play(2)
        if creds<0:
            time.sleep(1)
            defeat.play()
    label["text"]=str(days)


tk.Button(frame, text="Next Day...", font="None 23", command=new_day_def).grid(column=3, row=0, sticky="nsew")
tk.Button(frame, text="Income", font="None 23", command=i_upg).grid(column=2, row=1)
tk.Button(frame, text="Damage", font="None 23").grid(column=2, row=2)
tk.Label(frame, text="Credits:", font="Algerian 50").grid(row=0, column=0)
tk.Label(frame, text=creds, font="Algerian 50").grid(row=0, column=1)
tk.Label(frame, text=icost, font="Algerian 23").grid(row=1, column=1)
tk.Label(frame, text="Upgrade cost:", font="Algerian 23").grid(row=1, column=0)
tk.Label(frame, text=income, font="Algerian 23").grid(row=1, column=3)
tk.Label(frame, text=dcost, font="Algerian 23").grid(row=2, column=1)
tk.Label(frame, text="Upgrade cost:", font="Algerian 23").grid(row=2, column=0)
tk.Label(frame, text=damage, font="Algerian 23").grid(row=2, column=3)
tk.Label(frame, text="Current day:", font="Algerian 23").grid(row=3, column=0)

for i in range(5):
    frame.columnconfigure(i, weight=1)
    frame.rowconfigure(i, weight=1)


root.mainloop()
    