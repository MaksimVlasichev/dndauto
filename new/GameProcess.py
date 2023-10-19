from typing import Optional, Tuple, Union
import tkinter
import customtkinter as tk
import os
from os import walk
import asyncio
from pathlib import Path
from PIL import Image
import math
from CTkMessagebox import CTkMessagebox
from players import Player
from enemyWindow import EnemyWindow
from plyerWindow import WindowPlayer
def CalcBonus(a:int):
        if a == '':
            return "none"
        a = int(a)
        if a>11:
            return "+"+str(math.floor((a-10)/2))
        elif a<=11:
            return (math.ceil((a-10)*(-1)/2))*(-1)
folder = Path(os.getcwd().replace("new", "")+"\\players")
pths = os.getcwd().replace("new", "")+"\\players"
from battleWindows import PreBattle
def SetPlayer(names:list):
    list_players = []
    for i in range(len(names)):
        list_players.append(Player(names[i].replace(".txt", "")))
        names[i] = names[i].replace(".txt", "")
        f = open(pths+"\\{}.txt".format(names[i]),'r', encoding='utf-8', errors = 'ignore')
        info = f.readlines()
        f.close()
        # print(info)
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
        list_players[i].maxHp = str(info[13].split(" ")[1].replace("\n",""))
        list_players[i].money = str(info[14].split(" ")[1].replace("\n",""))
        names[i] = names[i].replace(".txt", "")
    return list_players, names
class GameLaunch(tk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Игровой процесс")
        # self.lift()
        # # self.wm_attributes("-disabled", True)
        # self.wm_attributes("-transparentcolor", "white")
        
        self.img = tk.CTkImage(light_image=Image.open("C:\\Users\\kymsk\\Desktop\\dndauto\\pictures\\accetes\\main.png"), size=(1000,600))
        self.after(0, lambda: self.wm_state('zoomed'))
        self.picEnemy = tk.CTkLabel(master=self, image=self.img, text= "")
        self.picEnemy.place(relx = 0.01, rely = 0.01)
        self.names = []
        for (dirpath, dirnames, filenames) in walk(folder):
            self.names.extend(filenames)
            break
        self.list_players, self.names = SetPlayer(self.names)
        self.segmBut = tk.CTkSegmentedButton(self, values=[i for i in self.names], command=self.change_players)
        self.segmBut.place(relx = 0.01, rely = 0.9)
        self.Addexp = tk.CTkButton(self, text="добавить опыт",command= self.AddExpAll)
        self.Addexp.place(relx = 0.5,rely = 0.9)
        self.ExpNum = tk.CTkEntry(self)
        self.ExpNum.place(relx = 0.4, rely = 0.9) 

        self.Adddmg = tk.CTkButton(self, text="нанести урон",command= self.DamageAll)
        self.Adddmg.place(relx = 0.5,rely = 0.85)
        self.DmgNum = tk.CTkEntry(self)
        self.DmgNum.place(relx = 0.4, rely = 0.85)
        self.dificultClass = tk.CTkEntry(self, placeholder_text="Класс сложности",width=50)
        self.dificultClass.place(relx = 0.6, rely = 0.85)
        self.checkattrib = tk.CTkOptionMenu(self,values=["Ловкость", "Сила", "Телосложение", "Интеллект", "Харизма", "Мудрость"])
        self.checkattrib.place(relx = 0.65, rely = 0.85)
        self.BattleBut = tk.CTkButton(self, text="Бой", command=lambda: PreBattle(self.list_players))
        self.BattleBut.place(relx = 0.3,rely = 0.9)
        self.chillBut = tk.CTkButton(self, text = "Отдых", command=self.chill)
        self.chillBut.place(relx = 0.6,rely = 0.9)
        self.enemyList = []

        self.statusOption = tk.CTkOptionMenu(self,fg_color='green', button_color='green',values=["Жив","Мёртв","Бессознательный","Испуганный","Истощённый","Невидимый","Недееспособный","Оглохший","Окаменевший","Опутанный","Ослеплённый","Отравленный",
                                                          "Очарованный","Ошеломлённый","Парализованный","Сбитый_с_ног","Схваченный"])
        self.statperson = tk.CTkOptionMenu(self,fg_color='green',button_color='green',values=[i for i in self.names])
        self.statperson.configure(values = self.statperson.cget('values')+["Всем"])
        self.ChangeStat = tk.CTkButton(self,fg_color='green',text="Задать",command=self.ChangeStatus)

        self.statperson.place(relx = 0.75,rely = 0.85)
        self.statusOption.place(relx = 0.85,rely = 0.85)
        self.ChangeStat.place(relx = 0.85,rely = 0.9)

        self.LogStr = tk.CTkEntry(self,width=140,placeholder_text="введите действие")
        self.LogStr.place(relx = 0.3,rely = 0.85)
        self.LogStr.bind("<Return>", command=(lambda event: self.gameLog()))

        for j in os.listdir("{}\\enemys".format(os.getcwd().replace("new",""))):
            img = tk.CTkImage(light_image=Image.open("C:\\Users\\kymsk\\Desktop\\dndauto\\enemys\\{}\\{}.jpg".format(j,j)),size=(200,100))
            self.enemyList.append(tk.CTkButton(self,text=j, image=img,width=200,height=85))
        ry = 0.0
        for j in self.enemyList:
            j.configure(command = lambda j=j: self.VisualEnemy(j._text))
        for i in self.enemyList:
            i.place(relx = 0.7,rely = ry)
            ry+=0.14

    def ChangeStatus(self):
        player = self.statperson.get()
        status = self.statusOption.get()+"\n"
        if player!="Всем":
            f = open(os.getcwd()+"\\players\\{}.txt".format(player),'r',encoding='utf-8', errors = 'ignore')
            stat = f.readlines()
            f.close()
            oldstat = stat[10].split(' ')[1]
            stat[10] = stat[10].replace(oldstat,status)
            f = open(os.getcwd()+"\\players\\{}.txt".format(player),'w',encoding='utf-8', errors = 'ignore')
            f.writelines(stat)
            f.close()
        else:
            for i in self.names:
                f = open(os.getcwd()+"\\players\\{}.txt".format(i),'r',encoding='utf-8', errors = 'ignore')
                stat = f.readlines()
                f.close()
                oldstat = stat[10].split(' ')[1]
                stat[10] = stat[10].replace(oldstat,status)
                f = open(os.getcwd()+"\\players\\{}.txt".format(i),'w',encoding='utf-8', errors = 'ignore')
                f.writelines(stat)
                f.close()


    def gameLog(self):
        f= open(os.getcwd()+"\\game.txt", 'a')
        f.write(self.LogStr.get()+'\n')
        f.close()
        self.LogStr.delete(0,len(self.LogStr.get()))


    def chill(self):
        for i in self.list_players:
            # oldhp = i.hp
            i.hp = i.maxHp
            i.stateField = "Жив"
            f = open(pths+"\\{}.txt".format(i.name), mode='r+',encoding = 'utf-8',errors='ignore')
            alllist = f.readlines()
            f.close()
            alllist[2] = alllist[2].replace(alllist[2].split(' ')[1],str(i.hp)+"\n")
            alllist[10] = alllist[10].replace(alllist[10].split(' ')[1],i.stateField+"\n")
            f = open(pths+"\\{}.txt".format(i.name), mode='w',encoding = 'utf-8',errors='ignore')
            f.writelines(alllist)
            f.close()

    def VisualEnemy(self, name):
        EnemyWindow(name)
    def bonusList(self):
        ls = []
        
        for i in self.list_players:
            f = open(pths+"\\{}.txt".format(i.name), mode='r+',encoding = 'utf-8',errors='ignore')
            alllist = f.readlines()
            f.close()
            for j in range(len(alllist)):
                if self.checkattrib.get() in alllist[j]:
                    k = CalcBonus(int(alllist[j].split(" ")[1].strip()))
            ls.append((i.name, k))
        return ls
    def PregictDmg(self):
        arr = self.bonusList()
        mes = ""
        for i in arr:
            mes+="Игрок - {} Бонус {}\n".format(i[0],i[1])
        # mag = CTkMessagebox(master=self,title = "Проверка на - {}\nКласс сложности - {}".format(self.checkattrib.get(),self.dificultClass.get()), message = mes, options = self.names,width=900)
        messbox  = tk.CTkToplevel()
        messbox.geometry("600x200")
        messbox.attributes("-topmost",True)
        rx=0.01
        messbox.title("Проверка на - {}\n Класс сложности - {}".format(self.checkattrib.get(),self.dificultClass.get()))
        lab = tk.CTkLabel(messbox, text= mes)
        lab.place(relx = 0.3,rely = 0.01)
        for i in self.names:
            but = tk.CTkButton(messbox, text= i, command=lambda x = i:self.DamageOne(x),width=100)
            but.place(relx = rx,rely = 0.8)
            rx+=0.2
        # CTkMessagebox(title="Проверка на - {}\nКласс сложности - {}".format(self.checkattrib.get(),self.dificultClass.get()), message="This is a CTkMessagebox!")
        # self.DamageOne(mag.get())
    def DamageOne(self,name):
        print(name)
        f = open(pths+"\\{}.txt".format(name), mode='r+',encoding = 'utf-8',errors='ignore')
        alllist = f.readlines()
        print(alllist)
        f.close()
        oldhp = alllist[2].split(" ")[1]
        print(self.list_players)
        print(name)
        for i in self.list_players:
            if i.name == name:
                print(True)
                i.hp-=int(self.DmgNum.get())
                alllist[2] = alllist[2].replace(str(oldhp), str(i.hp)+'\n')
                f = open(pths+"\\{}.txt".format(i.name), mode='w',encoding = 'utf-8',errors='ignore')
                print(alllist)
                f.writelines(alllist)
                f.close()
                break
    def DamageAll(self):
        if self.dificultClass.get() != "":
            self.PregictDmg()
            return 0
        for i in self.list_players:
            f = open(pths+"\\{}.txt".format(i.name), mode='r+',encoding = 'utf-8',errors='ignore')
            alllist = f.readlines()
            f.close()
            if self.dificultClass.get() != "":
                for j in range(len(alllist)):
                    if self.checkattrib.get() in alllist[j]:
                        # i = alllist.index(self.checkattrib.get())
                        k = CalcBonus(int(alllist[j].split(" ")[1].strip()))
            oldhp = alllist[2].split(" ")[1]
            i.hp = int(i.hp) - int(self.DmgNum.get())
            alllist[2] = alllist[2].replace(str(oldhp), str(i.hp)+'\n')
            f = open(pths+"\\{}.txt".format(i.name), mode='w',encoding = 'utf-8',errors='ignore')
            f.writelines(alllist)
            f.close()
        
    def AddExpAll(self): 
        for i in self.list_players:
            f = open(pths+"\\{}.txt".format(i.name), mode='r+',encoding = 'utf-8',errors='ignore')
            alllist = f.readlines()
            f.close()
            oldex = alllist[1].split(" ")[1]
            i.lvl+=int(self.ExpNum.get())
            alllist[1] = alllist[1].replace(str(oldex), str(i.lvl)+'\n')
            f = open(pths+"\\{}.txt".format(i.name), mode='w',encoding = 'utf-8',errors='ignore')
            f.writelines(alllist)
            f.close()
            
    def change_players(self, value):
        
        
        for i in self.list_players:
            if i.name == value:
                pw = WindowPlayer(i)
                pw.protocol("WM_DELETE_WINDOW", SetPlayer(self.names))
        # self.segmBut.configure(state = "normal")
        self.segmBut._unselect_button_by_value(value=value)
        return 0 