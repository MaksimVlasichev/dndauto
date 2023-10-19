import customtkinter as ctk
from players import Player, Enemy
from PIL import Image
from pathlib import Path
import os

from spinbox import FloatSpinbox
from settPlayer import changeSett,CalcBonus
from wathch_player import Show_player
from os import walk
folder = Path(os.getcwd()+"\\players")
segmBut = ""
list_players = []
def get_plyers():
    return list_players
def change_players(value):
    
    window = ctk.CTkToplevel()
    window.title(str(value))
    window.geometry("1000x700")
    window.attributes("-topmost",True)
    
    # spbox = FloatSpinbox(window, width=150,startvalue=24 ,step_size=1)
    # spbox.place(relx = 0.2, rely = 0.2)
    player:Player = None
    for i in list_players:
        if i.name == value:
            player = i
            break
    statList = {"Имя":ctk.CTkLabel(window, text = player.name),
                "Опыт":[FloatSpinbox(window,width=150,startvalue=player.lvl ,step_size=5),ctk.CTkLabel(window, text = "")],#дописать калькулятор опыта
                "Здоровье":ctk.CTkLabel(window, text = player.hp),#дописать калькулятор здоровья
                "Броня":ctk.CTkLabel(window, text = player.classArmor),
                "Ловкость":[FloatSpinbox(window,width=150,startvalue=player.Dexterity ,step_size=1),ctk.CTkLabel(window, text = CalcBonus(player.Dexterity))],
                "Сила":[FloatSpinbox(window,width=150,startvalue=player.Strength ,step_size=1),ctk.CTkLabel(window, text = CalcBonus(player.Strength))],
                "Телосложение":[FloatSpinbox(window,width=150,startvalue=player.Constitution ,step_size=1),ctk.CTkLabel(window, text = CalcBonus(player.Constitution))],
                "Интеллект":[FloatSpinbox(window,width=150,startvalue=player.Intelligence ,step_size=1),ctk.CTkLabel(window, text = CalcBonus(player.Intelligence))],
                "Харизма":[FloatSpinbox(window,width=150,startvalue=player.Charisma ,step_size=1),ctk.CTkLabel(window, text = CalcBonus(player.Charisma))],
                "Мудрость":[FloatSpinbox(window,width=150,startvalue=player.Wisdom ,step_size=1),ctk.CTkLabel(window, text = CalcBonus(player.Wisdom))],
                "Состояние":ctk.CTkLabel(window, text = player.stateField),
                "Бонус мастерства":ctk.CTkLabel(window, text = "+2")}
    ry = 0.02
    for v,k in statList.items():
        lb = ctk.CTkLabel(window, text= v)
        lb.place(relx =0.02, rely=ry)
        if type(k) == list:
            k[0].place(relx =0.15, rely=ry)
            k[1].place(relx =0.32, rely=ry)
        else:
            k.place(relx =0.15, rely=ry)
        ry+=0.05


from battle_process import initial_calc   
def gameProcess():
    global segmBut
    mainProcess = ctk.CTkToplevel()
    mainProcess.title("Game Process")
    # mainProcess.geometry("1920x1080")
    # width= mainProcess.winfo_screenwidth()               
    # height= mainProcess.winfo_screenheight()               
    # mainProcess.geometry("%dx%d" % (width, height))
    mainProcess.state('zoomed')

    img = ctk.CTkImage(light_image=Image.open("C:\\Users\\kymsk\\Desktop\\dndauto\\pictures\\accetes\\main.png"), size=(1000,600))
    picEnemy = ctk.CTkLabel(mainProcess, image=img, text= "")
    picEnemy.place(relx = 0.01, rely = 0.01)

    names = []
    for (dirpath, dirnames, filenames) in walk(folder):
        names.extend(filenames)
        break
    for i in range(len(names)):
        list_players.append(Player(names[i].replace(".txt", "")))
        f = open(os.getcwd()+"\\players\\{}".format(names[i]), 'r')
        info = f.readlines()
        f.close()
        print(info)
        list_players[i].lvl = int(info[1].split(" ")[1].replace("\n",""))
        list_players[i].hp = int(info[2].split(" ")[1].replace("\n",""))
        list_players[i].classArmor = int(info[3].split(" ")[1].replace("\n",""))
        list_players[i].Dexterity = int(info[4].split(" ")[1].replace("\n",""))
        list_players[i].Strength = int(info[5].split(" ")[1].replace("\n",""))
        list_players[i].Constitution = int(info[6].split(" ")[1].replace("\n",""))
        list_players[i].Intelligence = int(info[7].split(" ")[1].replace("\n",""))
        list_players[i].Charisma = int(info[8].split(" ")[1].replace("\n",""))
        list_players[i].Wisdom = int(info[9].split(" ")[1].replace("\n",""))
        list_players[i].abilityList = info[11].split(",")
        list_players[i].stateField = str(info[10].split(" ")[1].replace("\n",""))
        names[i] = names[i].replace(".txt", "")
    battle_start = ctk.CTkButton(mainProcess, text = "Бой", command=initial_calc)
    
    battle_start.place(relx = 0.5,rely = 0.8)
    segmBut = ctk.CTkSegmentedButton(mainProcess, values=[i for i in names], command=change_players)
    segmBut.place(relx = 0.01, rely = 0.9)
    # rf = battle_start._command.
    # print(rf)
    