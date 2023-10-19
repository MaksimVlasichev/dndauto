from typing import Optional, Tuple, Union
import customtkinter as tk
import os
import random
from players import Player, Enemy
from GameProcess import CalcBonus
from PIL import Image
from enemyWindow import EnemyWindow
import pyautogui
import pydirectinput
import time
from pathlib import Path
# from players import Enemy,Player
class InicialCalc(tk.CTkToplevel):
    def __init__(self, players_list,enemy):
        super().__init__()
        self.players_list = players_list
        self.enemys = enemy

        self.name_list = []
        self.initList = []
        self.dict_init = {}
        for i in self.enemys:
            for j in range(int(i.split(' ')[1])):
                enem = i.split(' ')[0]
                en = Enemy(enem)
                self.dict_init[en.name+" №{}".format(j+1)] = random.randint(1,21)+int(CalcBonus(en.Dexterity))
        self.geometry("200x400")
        self.title("Инициатива")
        self.attributes("-topmost",True)
        ry=0.02
        for i in players_list:
            lab = tk.CTkEntry(self, placeholder_text = i.name)
            self.initList.append(lab)
            lab.place(relx = 0.2, rely = ry)
            self.name_list.append(i.name)
            ry+=0.07
        but = tk.CTkButton(self, text = "Ввести", command=self.getin)
        but.place(relx = 0.2,rely = 0.9)
    def getin(self):
        for i in range(len(self.initList)):
            self.initList[i] = int(self.initList[i].get())+int(str(CalcBonus(self.players_list[i].Dexterity)).replace('+',''))
        for i in range(len(self.name_list)):
            self.dict_init[self.name_list[i]] = self.initList[i]
        self.dict_init = dict(sorted(self.dict_init.items(), key=lambda item: item[1], reverse=True))
        BattleScen(self.dict_init, self.enemys)
        self.destroy()
class PreBattle(tk.CTkToplevel):
    def __init__(self,players_list):
        super().__init__()
        self.playerlst = players_list
        # self.dict_init = dict_init
        self.geometry("500x400")
        self.title("Список врагов")
        self.attributes("-topmost",True)
        self.EnemyList = {}
        for j in os.listdir("{}\\enemys".format(os.getcwd().replace("new",""))):
            self.EnemyList[tk.CTkCheckBox(self,text=j)] = tk.CTkEntry(self, placeholder_text="'Кол-во','Уровень'")
        ry = 0.02
        for k,v in self.EnemyList.items():
            k.place(relx = 0.1,rely = ry)
            v.place(relx = 0.35, rely = ry)
            ry+=0.07
        self.GoBut = tk.CTkButton(self, text="Начать", command=self.Start)
        self.GoBut.place(relx = 0.3,rely = 0.9)
    def Start(self):
        enLi = []
        for k,v in self.EnemyList.items():
            if k._check_state == True:
                f = v.get().split(",")
                enLi.append("{} {} {}".format(k.cget("text"),f[0],f[1]))
        InicialCalc(self.playerlst, enLi)
        # BattleScen(self.dict_init, enLi)
        self.destroy()

class BattleScen(tk.CTkToplevel):
    def __init__(self,dict_init:dict, enemys:list):
        print(enemys)
        print(dict_init)
        super().__init__()
        self.playerslist = []
        onlyenemy = []
        self.enemyTypeStr = {}
        for i in enemys:
            self.enemyTypeStr[i.split(' ')[0]] = int(i.split(' ')[1])
        # self.write = False
        self.folder = Path(os.getcwd()+"\\battleLogs")
        f = open(os.getcwd()+"\\battleLogs\\battle №{}.txt".format(len(list(self.folder.iterdir()))+1),'x')
        for i in enemys:
            onlyenemy.append(i.split(' ')[0])
        for v,k in dict_init.items():
            if v.split(' ')[0] in onlyenemy:
                continue
            else:
                self.playerslist.append(v)
        for i in range(len(self.playerslist)):
            self.playerslist[i] = Player(self.playerslist[i])
            self.playerslist[i].initialplayer()
        self.step = 0
        self.dict_init = dict_init
        self.state('zoomed')
        self.BattleWindowFall = tk.CTkToplevel()
        self.BattleWindowFall.title("Бой")
        self.BattleWindowFall.state('zoomed')
        self.default_color =  self.BattleWindowFall.cget('fg_color')
        # print(self.default_color)
        self.actualPerson = None
        # self.default_color =  self.BattleWindowFall.cget('fg_color')
        # print(self.default_color)
        self.move_right()
        self.enemyByInit = []
        # rx = 0.01
        
        self.cubChoice = tk.CTkOptionMenu(self,values=["d4","d6","d8","d10","d12","d20"])
        self.cubeCount = tk.CTkEntry(self,width=60,placeholder_text="кол-во")
        self.cubChoice.place(relx = 0.65, rely = 0.9)
        self.cubeCount.place(relx = 0.6, rely = 0.9)
        self.cubBut = tk.CTkButton(self,text="Бросить", command=self.DropCube)
        self.cubBut.place(relx = 0.65, rely = 0.95)

        self.nowStepPerson = tk.CTkLabel(self)
        self.nowStepPerson.place(relx = 0.2,rely = 0.65)

        self.addEnemy = tk.CTkButton(self,text="Добавить врагов",command=self.AddEnemys)
        self.addEnemy.place(relx = 0.4,rely = 0.95)

        colorBut = tk.CTkButton(self,text="прозрачнй", command= self.ChangeColor)
        colorBut.place(relx = 0.8,rely = 0.9)
            # lb = tk.CTkLabel(self.BattleWindowFall, text = v, bg_color='grey', width=70)
            # self.initLab.append(lb)
            # lb.place(relx = rx, rely = 0.01)
            # rx +=0.1
        # self.initLab[0].configure(bg_color='green')

        self.LogStr = tk.CTkEntry(self,width=200,placeholder_text="введите действие")
        self.LogStr.place(relx = 0.4,rely = 0.9)
        self.LogStr.bind("<Return>", command=(lambda event: self.FightLog()))

        self.nextStep = tk.CTkButton(self, text = "следующий", command=self.NextStep)
        self.nextStep.place(relx = 0.1,rely = 0.9)
        self.enemyList = {}
        self.mylabList = []
        self.newEnemys = []
        rx = 0.5
        for i in enemys:
            enemy = i.split(' ')
            ry = 0.1
            for j in range(int(enemy[1])):
                enemyf = Enemy(enemy[0])
                # self.enemyList.append(enemyf)
                img = tk.CTkImage(light_image=Image.open(enemyf.picture_url),size=(150,90))
                myenlb = tk.CTkLabel(self,text = "{} №{}\n[{}]".format(enemyf.name, int(j+1),enemyf.hp))
                self.mylabList.append(myenlb)
                myenlb.place(relx = rx, rely = ry)
                enlb = tk.CTkLabel(self.BattleWindowFall, text="{} №{}\n[{}]".format(enemyf.name, int(j+1),enemyf.stateField) ,image=img,compound="top")
                self.enemyList[enlb] = enemyf
                enlb.place(relx = rx,rely = ry)
                ry+=0.23
            rx+=0.15
        self.LabPlayers = []
        self.MyLabPlayers = []
        k = 0
        ry = 0.1
        rx = 0.05
        for i in self.playerslist:
            img = tk.CTkImage(light_image=i.picture_url,size=(170,120))
            plLb = tk.CTkLabel(self.BattleWindowFall,text = "{} \nЗдоровье: {}\nСостояние: {}".format(i.name,i.hp,i.stateField),image=img,compound="top" )
            mypllb = tk.CTkLabel(self,text = "{} \nЗдоровье: {}\nСостояние: {}".format(i.name,i.hp,i.stateField),compound="top" )
            self.MyLabPlayers.append(mypllb)
            self.LabPlayers.append(plLb)
            if k %2 ==0 and k !=0:
                ry +=0.25
                rx =0.05
            plLb.place(relx = rx, rely = ry)
            mypllb.place(relx = rx, rely = ry)
            rx+=0.15
            k+=1

        self.initLab = self.LabPlayers + [v for v,k in self.enemyList.items()]
        
        
        
        self.placeLab()   
            
        ry = 0.05
        self.dmgNum = tk.CTkEntry(self, width=60,placeholder_text="кол-во")
        self.enemOption = tk.CTkOptionMenu(self,values=[v for v,k in dict_init.items()])
        self.dmgBut = tk.CTkButton(self,text="Нанести",command=self.DoDamage)
        self.dmgBut.place(relx = 0.25,rely =0.95)
        self.dmgNum.place(relx = 0.2,rely = 0.9)
        self.enemOption.place(relx = 0.25,rely = 0.9)

        self.EndButt = tk.CTkButton(self,text="Завершить",fg_color='red', command= self.EndButton)
        self.EndButt.place(relx = 0.8,rely = 0.95)

        # self.enListFMe = self.enemyList
        # for v,k in self.enListFMe.items():
        #     pass
        self.initLabxz = []
        # print(self.initLab)
        
        self.xzZachemEto()
        
        # print(self.initLab)
        # print(self.initLabxz)
        f = open(os.getcwd()+"\\battleLogs\\battle №{}.txt".format(len(list(self.folder.iterdir()))),'a')
        f.write("ход №{}, Игрок: {}\n".format(self.step+1, self.initLabxz[self.step]))
        f.close()
    
    def AddEnemys(self):
        enwin = tk.CTkToplevel()
        enwin.geometry("500x400")
        enwin.title("Список врагов")
        enwin.attributes("-topmost",True)
        EnemyList = {}
        def Start():
            for k,v in EnemyList.items():
                if k._check_state == True:
                    f = v.get().split(",")
                    self.newEnemys.append("{} {} {}".format(k.cget("text"),f[0],f[1]))
            # print(self.newEnemys)
            # for i in self.newEnemys:
            #     self.dict_init[i.split(' ')[0]] = 
            enemyCount = {}
            # print(self.enemyTypeStr)
            for k,v in self.enemyTypeStr.items():
                enemyCount[k] = v
            # for i in self.newEnemys:
            #     for j in range(int(i.split(' ')[1])):
            #         enem = i.split(' ')[0]
            #         en = Enemy(enem)
            #         self.dict_init[en.name+" №{}".format(j+1)] = random.randint(1,21)+int(CalcBonus(en.Dexterity))
            print(self.newEnemys)
            
            print(enemyCount.keys())
            for i in self.newEnemys:
                f = open(os.getcwd()+"\\battleLogs\\battle №{}.txt".format(len(list(self.folder.iterdir()))),'a')
                f.write("Добавлено {} объекта {}\n".format(i.split(' ')[1], i.split(' ')[0]))
                f.close()
                if i.split(' ')[0] in enemyCount.keys():
                    print(i.split(' ')[0])
                    print(enemyCount[i.split(' ')[0]])
                    print(int(i.split(' ')[1]))
                    for j in range(int(enemyCount[i.split(' ')[0]]), int(i.split(' ')[1])+int(enemyCount[i.split(' ')[0]])):
                        self.enemyTypeStr[i.split(' ')[0]] +=1
                        enemyf = Enemy(i.split(' ')[0])
                        # self.enemyList.append(enemyf)
                        img = tk.CTkImage(light_image=Image.open(enemyf.picture_url),size=(150,90))
                        myenlb = tk.CTkLabel(self,text = "{} №{}\n[{}]".format(enemyf.name, int(j+1),enemyf.hp))
                        self.dict_init[enemyf.name+" №{}".format(j+1)] = random.randint(1,21)+int(CalcBonus(enemyf.Dexterity))
                        self.enemOption.configure(values=[v for v,k in self.dict_init.items()])
                        self.xzZachemEto()
                        self.mylabList.append(myenlb)
                        enlb = tk.CTkLabel(self.BattleWindowFall, text="{} №{}\n[{}]".format(enemyf.name, int(j+1),enemyf.stateField) ,image=img,compound="top")
                        self.enemyList[enlb] = enemyf
                else:
                    self.enemyTypeStr[i.split(' ')[0]] = int(i.split(' ')[1])
                    for j in range(int(i.split(' ')[1])):
                        
                        enemyf = Enemy(i.split(' ')[0])
                        # self.enemyList.append(enemyf)
                        img = tk.CTkImage(light_image=Image.open(enemyf.picture_url),size=(150,90))
                        myenlb = tk.CTkLabel(self,text = "{} №{}\n[{}]".format(enemyf.name, int(j+1),enemyf.hp))
                        self.dict_init[enemyf.name+" №{}".format(j+1)] = random.randint(1,21)+int(CalcBonus(enemyf.Dexterity))
                        self.enemOption.configure(values=[v for v,k in self.dict_init.items()])
                        self.xzZachemEto()
                        self.mylabList.append(myenlb)
                        enlb = tk.CTkLabel(self.BattleWindowFall, text="{} №{}\n[{}]".format(enemyf.name, int(j+1),enemyf.stateField) ,image=img,compound="top")
                        self.enemyList[enlb] = enemyf
            self.initLab = self.LabPlayers + [v for v,k in self.enemyList.items()]
            self.placeLab()
            print(self.dict_init)
            self.newEnemys = []
            enwin.destroy()
        for j in os.listdir("{}\\enemys".format(os.getcwd().replace("new",""))):
            EnemyList[tk.CTkCheckBox(enwin,text=j)] = tk.CTkEntry(enwin, placeholder_text="'Кол-во','Уровень'")
        ry = 0.02
        for k,v in EnemyList.items():
            k.place(relx = 0.1,rely = ry)
            v.place(relx = 0.35, rely = ry)
            ry+=0.07
        GoBut = tk.CTkButton(enwin, text="Добавить", command=Start)
        GoBut.place(relx = 0.3,rely = 0.9)
        
    def EndButton(self):
        f = open(os.getcwd()+"\\battleLogs\\battle №{}.txt".format(len(list(self.folder.iterdir()))),'a')
        f.write("Бой завершён")
        f.close()
        self.BattleWindowFall.destroy()
        self.destroy()
    def DropCube(self):
        cubType = self.cubChoice.get().split('d')[1]
        cubNum = self.cubeCount.get()
        dropcube = tk.CTkToplevel()
        dropcube.title("{} {}".format(cubNum, self.cubChoice.get()))
        dropcube.geometry("100x100")
        dropcube.attributes("-topmost",True)
        textt =""
        for i in range(int(cubNum)):
            textt+=f"{i}. {random.randint(1,int(cubType))}\n"
        lb = tk.CTkLabel(master=dropcube, text= textt)
        lb.place(relx = 0.4,rely = 0.1)
    def FightLog(self):
        f = open(os.getcwd()+"\\battleLogs\\battle №{}.txt".format(len(list(self.folder.iterdir()))),'a')
        f.write(self.LogStr.get()+'\n')
        f.close()
        self.LogStr.delete(0,len(self.LogStr.get()))
    def NextStep(self):
        self.swap()
        f = open(os.getcwd()+"\\battleLogs\\battle №{}.txt".format(len(list(self.folder.iterdir()))),'a')
        f.write("ход №{}, Игрок: {}\n".format(self.step+1, self.initLabxz[self.step]))
        f.close()
    def ChangeColor(self):
        if self.BattleWindowFall.cget('fg_color') == '#add123':
            self.BattleWindowFall.configure(fg_color = self.default_color)
            for i,k in self.dict_init.items():
                self.swap()
        else:
            self.BattleWindowFall.configure(fg_color = '#add123')
            self.BattleWindowFall.wm_attributes('-transparentcolor','#add123')
            for i,k in self.dict_init.items():
                self.swap()

    def placeLab(self):
            for i in self.initLab:
                if i.cget('bg_color') not in  ['red', 'green']:
                    i.configure(bg_color = '#734a12')
            if len(self.initLab) - len(self.playerslist) >16:
                for i in self.initLab:
                    img = i.cget('image')
                    img.configure(size=(80,70))
                rx = 0.35
                ry = 0.05
                for v,k in self.enemyList.items():
                    if rx >0.9:
                        rx=0.35
                        ry+=0.17
                    v.place(relx = rx, rely = ry)
                    rx +=0.15
                rx = 0.35
                ry = 0.05
                for i in self.mylabList:
                    if rx >0.9:
                        rx=0.35
                        ry+=0.17
                    i.place(relx = rx, rely = ry)
                    rx +=0.15
            else:
                rx = 0.4
                ry = 0.05
                for v,k in self.enemyList.items():
                    if rx >0.9:
                        rx=0.4
                        ry+=0.17
                    v.place(relx = rx, rely = ry)
                    rx +=0.15
                rx = 0.4
                ry = 0.05
                for i in self.mylabList:
                    if rx >0.9:
                        rx=0.35
                        ry+=0.17
                    i.place(relx = rx, rely = ry)
                    rx +=0.15
    def xzZachemEto(self):
        self.initLabxz = []
        for v,k in self.dict_init.items():
            self.initLabxz.append(v)
        for i in self.initLab:
            if self.initLabxz[self.step] in i.cget('text'):
                i.configure(bg_color = 'green')
                self.nowStepPerson.configure(text = i.cget('text'), image = i.cget('image'),compound="top")
                break
    def DoDamage(self):
        enem = self.enemOption.get()
        dmg = int(self.dmgNum.get())
        f = open(os.getcwd()+"\\battleLogs\\battle №{}.txt".format(len(list(self.folder.iterdir()))),'a')
        f.write("Существо: {} Получает {} урона\n".format(enem, dmg))
        f.close()
        if enem in [names.name for names in self.playerslist]:
            pths = os.getcwd().replace("new", "")+"\\players"
            f = open(pths+"\\{}.txt".format(enem), mode='r+',encoding = 'utf-8',errors='ignore')
            player = f.readlines()
            f.close()
            oldhp = player[2].split(' ')[1].strip()
            newhp = int(oldhp) - dmg
            player[2] = player[2].replace(oldhp, str(newhp))

            f = open(pths+"\\{}.txt".format(enem), mode='w',encoding = 'utf-8',errors='ignore')
            f.writelines(player)
            f.close()
            for i in range(len(self.LabPlayers)):
                if enem in self.LabPlayers[i].cget('text'):
                    self.LabPlayers[i].configure(text = self.LabPlayers[i].cget('text').replace(str(oldhp), str(newhp)))
                    if newhp<=0:
                        self.LabPlayers[i].configure(bg_color = 'red', text = self.LabPlayers[i].cget('text').replace(str(newhp),"нет").replace("Жив","Мёртв"))
                        self.MyLabPlayers[i].configure(bg_color = 'red', text = self.LabPlayers[i].cget('text').replace(str(newhp),"нет").replace("Жив","Мёртв"))
                        f = open(pths+"\\{}.txt".format(enem), mode='w',encoding = 'utf-8',errors='ignore')
                        player[10]= player[10].split(' ')[0]+" мёртв\n"
                        f.writelines(player)
                        f.close()
                    break
                    return
        for i in self.mylabList:
            if enem in i.cget('text'):
                hpnow = int(i.cget('text').split('[')[1].replace("]",""))
                hpnew = hpnow-dmg
                newtext = i.cget('text').replace(str(hpnow), str(hpnew))
                if hpnew <=0:
                    i.configure(bg_color = 'red')
                    for v,k in self.enemyList.items():
                        if enem in v.cget('text'):
                            v.configure(bg_color = 'red',text =v.cget('text').replace("[жив]", "мёртв"))
                            break
                i.configure(text = newtext)
                
                break
        
        
    def move_right(self):
        with pyautogui.hold('win'):
            pydirectinput.keyDown('shift')
            pydirectinput.press('right')
        pydirectinput.keyUp('shift')
    def swap(self):
        
        if self.step == len(self.dict_init)-1:
            self.step = 0
        else:
            self.step+=1
        for i in range(len(self.initLab)):
            if str(self.initLabxz[self.step]).strip() == str(self.initLab[i].cget('text').split('\n')[0]).strip():
                if self.initLab[i].cget('bg_color') !='red':
                    self.initLab[i].configure(bg_color = 'green')
                    self.nowStepPerson.configure(text = self.initLab[i].cget('text'), image = self.initLab[i].cget('image'),compound="top")

                    for j in range(len(self.initLab)):
                        if self.initLabxz[self.step-1].strip() == self.initLab[j].cget('text').split('\n')[0].strip():
                            if self.initLab[j].cget('bg_color') !='red':
                                self.initLab[j].configure(bg_color = '#734a12')
                                break
                            else:
                                break
                else:
                    for j in range(len(self.initLab)):
                        if self.initLabxz[self.step-1].strip() == self.initLab[j].cget('text').split('\n')[0].strip():
                            if self.initLab[j].cget('bg_color') !='red':
                                self.initLab[j].configure(bg_color = '#734a12')
                                break
                            else:
                                break
                    self.swap()
                    return

          

            