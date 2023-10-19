from typing import Optional, Tuple, Union
import customtkinter as tk
import asyncio
import os
import math
from players import Player
from spinbox import FloatSpinbox
class WindowPlayer(tk.CTkToplevel):
    def __init__(self, player:Player):
        super().__init__()
        if player.name not in os.listdir(os.getcwd()+"\\enemys"):
            player.initialplayer()
        self.title(player.name)
        self.player = player
        self.LvlList = [0,300,900,2700,6500,14000,23000,34000,48000,64000,85000,100000,120000,140000,165000]
        self.geometry("1000x600")
        self.attributes("-topmost",True)
        self.abillityList = {"Атлетика":[tk.CTkCheckBox(self, text=""),tk.CTkLabel(self,text=(""))],
                 "Акробатика":[tk.CTkCheckBox(self, text=""),tk.CTkLabel(self,text="")],
                 "Ловкость рук":[tk.CTkCheckBox(self, text=""),tk.CTkLabel(self,text="")],
                 "Скрытность":[tk.CTkCheckBox(self, text=""),tk.CTkLabel(self,text="")],
                 "Магия":[tk.CTkCheckBox(self, text=""),tk.CTkLabel(self,text="")],
                 "История":[tk.CTkCheckBox(self, text=""),tk.CTkLabel(self,text="")],
                 "Расследование":[tk.CTkCheckBox(self, text=""),tk.CTkLabel(self,text="")],
                 "Природа":[tk.CTkCheckBox(self, text=""),tk.CTkLabel(self,text="")],
                 "Религия":[tk.CTkCheckBox(self, text=""),tk.CTkLabel(self,text="")],
                 "Обращение с животными":[tk.CTkCheckBox(self, text=""),tk.CTkLabel(self,text="")],
                 "Проницательность":[tk.CTkCheckBox(self, text=""),tk.CTkLabel(self,text="")],
                 "Медицина":[tk.CTkCheckBox(self, text=""),tk.CTkLabel(self,text="")],
                 "Восприятие":[tk.CTkCheckBox(self, text=""),tk.CTkLabel(self,text="")],
                 "Выживание":[tk.CTkCheckBox(self, text=""),tk.CTkLabel(self,text="")],
                 "Обман":[tk.CTkCheckBox(self, text=""),tk.CTkLabel(self,text="")],
                 "Запугивание":[tk.CTkCheckBox(self, text=""),tk.CTkLabel(self,text="")],
                 "Выступление":[tk.CTkCheckBox(self, text=""),tk.CTkLabel(self,text="")],
                 "Убеждение":[tk.CTkCheckBox(self, text=""),tk.CTkLabel(self,text="")]}
        for i in self.abillityList.keys():
            if i in self.player.abilityList:
                self.abillityList[i][0].select()

        self.statList:dict = {"Имя":tk.CTkLabel(self, text = player.name),
                "Опыт":[FloatSpinbox(self,width=150,startvalue=player.lvl ,step_size=5),tk.CTkLabel(self,text = str(self.LvlCalc()))],#дописать калькулятор опыта
                "Здоровье":tk.CTkLabel(self, text = player.hp),#дописать калькулятор здоровья
                "Броня":tk.CTkLabel(self, text = player.classArmor),
                "Ловкость":[FloatSpinbox(self,width=150,startvalue=player.Dexterity ,step_size=1),tk.CTkLabel(self, text = self.CalcBonus(player.Dexterity))],
                "Сила":[FloatSpinbox(self,width=150,startvalue=player.Strength ,step_size=1),tk.CTkLabel(self, text = self.CalcBonus(player.Strength))],
                "Телосложение":[FloatSpinbox(self,width=150,startvalue=player.Constitution ,step_size=1),tk.CTkLabel(self, text = self.CalcBonus(player.Constitution))],
                "Интеллект":[FloatSpinbox(self,width=150,startvalue=player.Intelligence ,step_size=1),tk.CTkLabel(self, text = self.CalcBonus(player.Intelligence))],
                "Харизма":[FloatSpinbox(self,width=150,startvalue=player.Charisma ,step_size=1),tk.CTkLabel(self, text = self.CalcBonus(player.Charisma))],
                "Мудрость":[FloatSpinbox(self,width=150,startvalue=player.Wisdom ,step_size=1),tk.CTkLabel(self, text = self.CalcBonus(player.Wisdom))],
                "Состояние:":tk.CTkLabel(self, text = player.stateField),
                "Бонус мастерства:":tk.CTkLabel(self, text = self.BMCalc()),
                "Макс_здоровье:":FloatSpinbox(self,width=150,startvalue=player.maxHp ,step_size=1),
                "Деньги:":FloatSpinbox(self,width=150,startvalue=player.money ,step_size=10)}
        self.loadBut = tk.CTkButton(self, text= "Обновить", command=self.Update)
        self.loadBut.place(relx = 0.7,rely = 0.75)
        self.file = tk.CTkButton(self, text= "Записать", command=self.to_file)
        self.file.place(relx = 0.7,rely = 0.9)

        self.ry = 0.02
        self.keyList = list(self.abillityList.keys())
        for v,k in self.statList.items():
            lb = tk.CTkLabel(self, text= v)
            lb.place(relx =0.02, rely=self.ry)
            if type(k) == list:
                k[0].place(relx =0.15, rely=self.ry)
                k[1].place(relx =0.33, rely=self.ry)
            else:
                k.place(relx =0.15, rely=self.ry)
            self.ry+=0.06
        relyy= 0.02
        for i in range(len(self.keyList)):
            lab = tk.CTkLabel(self, text=self.keyList[i])
            lab.place(relx = 0.4, rely = relyy)
            self.abillityList[self.keyList[i]][0].place(relx = 0.6,rely = relyy)
            self.abillityList[self.keyList[i]][1].place(relx = 0.65,rely = relyy)
            relyy+=0.05
    def BMCalc(self):
        lvl = self.LvlCalc()
        k = lvl/4
        if k<=1:
            return 2
        if k<=2:
            return 3
        if k<=3:
            return 4
        if k<=4:
            return 5
        if k<=5:
            return 6
        
    def LvlCalc(self):
        exp = self.player.lvl
        for i in range(len(self.LvlList)):
            if int(exp)>self.LvlList[i]:
                continue
            elif int(exp) == self.LvlList[i]:
                return i+1
            elif int(exp) < self.LvlList[i]:
                return i
    def Update(self):

        kwy,value = list(self.statList.items())[1]
        self.player.lvl = value[0].get()
        value[1].configure(text = self.LvlCalc())
        kwy,value = list(self.statList.items())[11]
        value.configure(text = self.BMCalc())


        for v in range(4,10,1):
            kwy,value = list(self.statList.items())[v]
            value[1].configure(text = self.CalcBonus(value[0].get())) 
        
        for i in range(len(self.keyList)):
            textt = ""
            if i == 0:
                kwy,value = list(self.statList.items())[5]
                textt = self.CalcBonus(value[0].get())
            if i in [1,2,3]:
                kwy,value = list(self.statList.items())[4]
                textt = self.CalcBonus(value[0].get())
            if i in [4,5,6,7,8]:
                kwy,value = list(self.statList.items())[7]
                textt = self.CalcBonus(value[0].get())
            if i in [9,10,11,12,13]:
                kwy,value = list(self.statList.items())[9]
                textt = self.CalcBonus(value[0].get())
            if i in [14,15,16,17]:
                kwy,value = list(self.statList.items())[8]
                textt = self.CalcBonus(value[0].get())
            if self.abillityList[self.keyList[i]][0].get() == 1:
                if type(textt) == str:
                    textt = "+"+str(int(textt.replace("+",""))+self.player.masterBonus)
                else:
                    textt +=self.player.masterBonus
            self.abillityList[self.keyList[i]][1].configure(text = str(textt))
    def updateClass(self):
        f = open(os.getcwd().replace("new","")+"\\players\\{}.txt".format(self.player.name),'r', encoding='utf-8', errors = 'ignore')
        info = f.readlines()
        f.close()
        # print(info)
        self.player.lvl = int(info[1].split(" ")[1].replace("\n",""))
        self.player.hp = int(info[2].split(" ")[1].replace("\n",""))
        self.player.classArmor = int(info[3].split(" ")[1].replace("\n",""))
        self.player.Dexterity = int(info[4].split(" ")[1].replace("\n",""))
        self.player.Strength = int(info[5].split(" ")[1].replace("\n",""))
        self.player.Constitution = int(info[6].split(" ")[1].replace("\n",""))
        self.player.Intelligence = int(info[7].split(" ")[1].replace("\n",""))
        self.player.Charisma = int(info[8].split(" ")[1].replace("\n",""))
        self.player.Wisdom = int(info[9].split(" ")[1].replace("\n",""))
        self.player.abilityList = info[11].split(",")
        self.player.stateField = str(info[10].split(" ")[1].replace("\n",""))
        self.player.maxHp = str(info[13].split(" ")[1].replace("\n",""))
        self.player.money = str(info[14].split(" ")[1].replace("\n",""))
    def CalcBonus(self, a:int):
        if a == '':
            return "none"
        a = int(a)
        if a>11:
            return "+"+str(math.floor((a-10)/2))
        elif a<=11:
            return (math.ceil((a-10)*(-1)/2))*(-1)
    def to_file(self):
        statlis = list(self.statList.items())
        print(statlis[1][1][0])
        infoList = []

        infoList.append(self.player.name)
        infoList.append("\nОпыт: "+str(statlis[1][1][0].get())+"\n")
        infoList.append("Здоровье: "+str(statlis[2][1].cget("text"))+"\n")
        infoList.append("Класс_брони: "+str(statlis[3][1].cget("text"))+"\n")
        infoList.append("Ловкость: "+str(statlis[4][1][0].get())+"\n")
        infoList.append("Сила: "+str(statlis[5][1][0].get())+"\n")
        infoList.append("Телосложение: "+str(statlis[6][1][0].get())+"\n")
        infoList.append("Интеллект: "+str(statlis[7][1][0].get())+"\n")
        infoList.append("Харизма: "+str(statlis[8][1][0].get())+"\n")
        infoList.append("Мудрость: "+str(statlis[9][1][0].get())+"\n")
        infoList.append("Состояние: "+str(statlis[10][1].cget("text"))+"\n")
        
        for v,k in self.abillityList.items():
            if k[0].get() == 1:
                infoList.append(v+",")
        infoList.append("\nБМ: "+str(statlis[11][1].cget("text"))+"\n")
        infoList.append("Макс_здоровье: "+str(str(statlis[12][1].get())+"\n"))
        infoList.append("Деньги: "+str(str(statlis[13][1].get())+"\n"))
        file = os.getcwd().replace("new", "")+"\\players"
        f = open(file+"\\{}.txt".format(self.player.name), 'w', encoding='utf-8')
        f.writelines(infoList)
        f.close()
        self.updateClass()
        self.destroy()