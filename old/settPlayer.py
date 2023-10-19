import customtkinter as ctk
import os
import math
from pathlib import Path
from players import Player
infoList=[]
valuee = ""
sb = ""
settingsWindow = ""
def CalcBonus(a):
    if a == '':
        return "none"
    a = int(a)
    if a>11:
        return "+"+str(math.floor((a-10)/2))
    elif a<=11:
        return (math.ceil((a-10)*(-1)/2))*(-1)
def get_window():
    return settingsWindow
def getList():
    global sb,valuee
    print(infoList)
    os.rename(os.getcwd()+"\\players\\{}.txt".format(value), os.getcwd()+"\\players\\{}.txt".format(infoList[0]))
    f = open(os.getcwd()+"\\players\\{}.txt".format(infoList[0]),'w')
    f.writelines(infoList)
    f.close()
    print(sb._value_list)
    print(value)
    sb._value_list.pop(sb._value_list.index(value))
    sbl = sb._value_list
    print(sbl)
    sbl.append(infoList[0])
    sb.configure(values = sbl)
    infoList.clear()
def changeSett(valuee, segmBut):
    global value, sb, settingsWindow
    sb = segmBut
    value= valuee
    global infoList
    settingsWindow = ctk.CTkToplevel()
    settingsWindow.geometry("1000x600")
    settingsWindow.title("Персонаж: {}".format(value))
    settingsWindow.attributes("-topmost",True)
    navikList = {"Атлетика":[ctk.CTkCheckBox(settingsWindow, text=""),ctk.CTkLabel(settingsWindow,text="")],
                 "Акробатика":[ctk.CTkCheckBox(settingsWindow, text=""),ctk.CTkLabel(settingsWindow,text="")],
                 "Ловкость рук":[ctk.CTkCheckBox(settingsWindow, text=""),ctk.CTkLabel(settingsWindow,text="")],
                 "Скрытность":[ctk.CTkCheckBox(settingsWindow, text=""),ctk.CTkLabel(settingsWindow,text="")],
                 "Магия":[ctk.CTkCheckBox(settingsWindow, text=""),ctk.CTkLabel(settingsWindow,text="")],
                 "История":[ctk.CTkCheckBox(settingsWindow, text=""),ctk.CTkLabel(settingsWindow,text="")],
                 "Расследование":[ctk.CTkCheckBox(settingsWindow, text=""),ctk.CTkLabel(settingsWindow,text="")],
                 "Природа":[ctk.CTkCheckBox(settingsWindow, text=""),ctk.CTkLabel(settingsWindow,text="")],
                 "Религия":[ctk.CTkCheckBox(settingsWindow, text=""),ctk.CTkLabel(settingsWindow,text="")],
                 "Обращение с животными":[ctk.CTkCheckBox(settingsWindow, text=""),ctk.CTkLabel(settingsWindow,text="")],
                 "Проницательность":[ctk.CTkCheckBox(settingsWindow, text=""),ctk.CTkLabel(settingsWindow,text="")],
                 "Медицина":[ctk.CTkCheckBox(settingsWindow, text=""),ctk.CTkLabel(settingsWindow,text="")],
                 "Восприятие":[ctk.CTkCheckBox(settingsWindow, text=""),ctk.CTkLabel(settingsWindow,text="")],
                 "Выживание":[ctk.CTkCheckBox(settingsWindow, text=""),ctk.CTkLabel(settingsWindow,text="")],
                 "Обман":[ctk.CTkCheckBox(settingsWindow, text=""),ctk.CTkLabel(settingsWindow,text="")],
                 "Запугивание":[ctk.CTkCheckBox(settingsWindow, text=""),ctk.CTkLabel(settingsWindow,text="")],
                 "Выступление":[ctk.CTkCheckBox(settingsWindow, text=""),ctk.CTkLabel(settingsWindow,text="")],
                 "Убеждение":[ctk.CTkCheckBox(settingsWindow, text=""),ctk.CTkLabel(settingsWindow,text="")]}
    keyList = list(navikList.keys())
    def Get_info():
        
        for i in range(len(keyList)):
            textt = ""
            if i == 0:
                textt = CalcBonus(Strenter.get())
            if i in [1,2,3]:
                textt = CalcBonus(DEXenter.get())
            if i in [4,5,6,7,8]:
                textt = CalcBonus(Intenter.get())
            if i in [9,10,11,12,13]:
                textt = CalcBonus(Wisenter.get())
            if i in [14,15,16,17]:
                textt = CalcBonus(Chaenter.get())
            if navikList[keyList[i]][0].get() == 1:
                if type(textt) == str:
                    textt = "+"+str(int(textt.replace("+",""))+int(BMenter.get()))
                else:
                    textt +=int(BMenter.get())
            navikList[keyList[i]][1].configure(text = str(textt))
                
            pass

        dexBonus.configure(text = str(CalcBonus(DEXenter.get())))
        strBonus.configure(text = str(CalcBonus(Strenter.get())))
        ConBonus.configure(text = str(CalcBonus(Conenter.get())))
        IntBonus.configure(text = str(CalcBonus(Intenter.get())))
        ChaBonus.configure(text = str(CalcBonus(Chaenter.get())))
        WisBonus.configure(text = str(CalcBonus(Wisenter.get())))


        infoList.append(nameEnter.get())
        infoList.append("\nОпыт: "+str(ExpEnter.get())+"\n")
        infoList.append("Здоровье: "+HpEnter.get()+"\n")
        infoList.append("Класс_брони: "+CBEnter.get()+"\n")
        infoList.append("Ловкость: "+DEXenter.get()+"\n")
        infoList.append("Сила: "+Strenter.get()+"\n")
        infoList.append("Телосложение: "+Conenter.get()+"\n")
        infoList.append("Интеллект: "+Intenter.get()+"\n")
        infoList.append("Харизма: "+Chaenter.get()+"\n")
        infoList.append("Мудрость: "+Wisenter.get()+"\n")
        infoList.append("Состояние: "+Statusenter.get()+"\n")
        for i in range(len(keyList)):
            if navikList[keyList[i]][0].get() == 1:
                infoList.append(keyList[i]+",")


        # infoList.append(Skillenter.get("1.0",'.'))
        print(infoList)
        # settingsWindow.destroy()
    rezBut = ctk.CTkButton(settingsWindow, text= "Ввести", command=Get_info)
    rezBut.place(relx = 0.7, rely = 0.9)
    rezBut = ctk.CTkButton(settingsWindow, text= "Записать", command=getList)
    rezBut.place(relx = 0.5, rely = 0.9)
    
    relyy = 0.02
    
    for i in range(len(keyList)):
        lab = ctk.CTkLabel(settingsWindow, text=keyList[i])
        lab.place(relx = 0.4, rely = relyy)
        navikList[keyList[i]][0].place(relx = 0.6,rely = relyy)
        navikList[keyList[i]][1].place(relx = 0.65,rely = relyy)
        relyy+=0.05

    labName = ctk.CTkLabel(settingsWindow, text = "Name:")
    labName.place(relx = 0.05, rely = 0.02)
    nameEnter = ctk.CTkEntry(settingsWindow, placeholder_text="name")
    nameEnter.place(relx = 0.25, rely = 0.02)
    labExp = ctk.CTkLabel(settingsWindow, text = "Exp:")
    labExp.place(relx = 0.05, rely = 0.07)
    ExpEnter = ctk.CTkEntry(settingsWindow, placeholder_text="exp(int)")
    ExpEnter.place(relx = 0.25, rely = 0.07)
    labHp = ctk.CTkLabel(settingsWindow, text = "Hits")
    labHp.place(relx = 0.05, rely = 0.12)
    HpEnter = ctk.CTkEntry(settingsWindow, placeholder_text="Hits")
    HpEnter.place(relx = 0.25, rely = 0.12)
    labCB = ctk.CTkLabel(settingsWindow, text = "Armor Class")
    labCB.place(relx = 0.05, rely = 0.17)
    CBEnter = ctk.CTkEntry(settingsWindow, placeholder_text="")
    CBEnter.place(relx = 0.25, rely = 0.17)
    labDex = ctk.CTkLabel(settingsWindow, text = "Ловкость")
    labDex.place(relx = 0.05, rely = 0.22)
    DEXenter = ctk.CTkEntry(settingsWindow, placeholder_text="Dexterity", width=30)
    dexBonus = ctk.CTkLabel(settingsWindow, text = "")
    dexBonus.place(relx = 0.295, rely = 0.22)
    labDex.place(relx = 0.05, rely = 0.22)
    DEXenter.place(relx = 0.25, rely = 0.22)
    labStr = ctk.CTkLabel(settingsWindow, text = "Сила")
    labStr.place(relx = 0.05, rely = 0.27)
    strBonus = ctk.CTkLabel(settingsWindow, text = "")
    strBonus.place(relx = 0.295, rely = 0.27)
    Strenter = ctk.CTkEntry(settingsWindow, placeholder_text="Strength", width=30)
    Strenter.place(relx = 0.25, rely = 0.27)
    labCon = ctk.CTkLabel(settingsWindow, text = "Телосложение")
    labCon.place(relx = 0.05, rely = 0.32)
    Conenter = ctk.CTkEntry(settingsWindow, placeholder_text="Constitution", width=30)
    Conenter.place(relx = 0.25, rely = 0.32)
    ConBonus = ctk.CTkLabel(settingsWindow, text = "")
    ConBonus.place(relx = 0.295, rely = 0.32)
    labInt = ctk.CTkLabel(settingsWindow, text = "Интеллект")
    labInt.place(relx = 0.05, rely = 0.37)
    Intenter = ctk.CTkEntry(settingsWindow, placeholder_text="Intelligence", width=30)
    Intenter.place(relx = 0.25, rely = 0.37)
    IntBonus = ctk.CTkLabel(settingsWindow, text = "")
    IntBonus.place(relx = 0.295, rely = 0.37)
    labCha = ctk.CTkLabel(settingsWindow, text = "Харизма", width=30)
    labCha.place(relx = 0.05, rely = 0.42)
    Chaenter = ctk.CTkEntry(settingsWindow, placeholder_text="Charisma", width=30)
    Chaenter.place(relx = 0.25, rely = 0.42)
    ChaBonus = ctk.CTkLabel(settingsWindow, text = "")
    ChaBonus.place(relx = 0.295, rely = 0.42)
    labWis = ctk.CTkLabel(settingsWindow, text = "Мудрость")
    labWis.place(relx = 0.05, rely = 0.47)
    Wisenter = ctk.CTkEntry(settingsWindow, placeholder_text="Wisdom", width=30)
    Wisenter.place(relx = 0.25, rely = 0.47)
    WisBonus = ctk.CTkLabel(settingsWindow, text = "")
    WisBonus.place(relx = 0.295, rely = 0.47)
    labStatus = ctk.CTkLabel(settingsWindow, text = "Состояние")
    labStatus.place(relx = 0.05, rely = 0.52)
    Statusenter = ctk.CTkEntry(settingsWindow, placeholder_text="Состояние персонажа")
    Statusenter.place(relx = 0.25, rely = 0.52)
    labBM = ctk.CTkLabel(settingsWindow, text = "Бонус мастерства")
    labBM.place(relx = 0.05, rely = 0.57)
    BMenter = ctk.CTkEntry(settingsWindow, placeholder_text="БМ", width=30)
    BMenter.place(relx = 0.25, rely = 0.57)
    # labSkills = ctk.CTkLabel(settingsWindow, text = "Действия")
    # labSkills.place(relx = 0.6, rely = 0.02)
    # Skillenter = ctk.CTkTextbox(settingsWindow)
    # Skillenter.place(relx = 0.6, rely = 0.07)
    # labAddSkills = ctk.CTkLabel(settingsWindow, text = "Добавить навык(и)")
    # labAddSkills.place(relx = 0.6, rely = 0.42)
    # SkillAddenter = ctk.CTkEntry(settingsWindow)
    # SkillAddenter.place(relx = 0.6, rely = 0.47)
    labItems = ctk.CTkLabel(settingsWindow, text = "Предметы")
    labItems.place(relx = 0.05, rely = 0.62)
    Skillenter = ctk.CTkTextbox(settingsWindow)
    Skillenter.place(relx = 0.05, rely = 0.67)
    # labAddSkills = ctk.CTkLabel(settingsWindow, text = "Добавить предмет(ы)")
    # labAddSkills.place(relx = 0.6, rely = 0.52)
    # SkillAddenter = ctk.CTkEntry(settingsWindow)
    # SkillAddenter.place(relx = 0.6, rely = 0.57)

    
        
    
    