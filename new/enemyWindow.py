import customtkinter as tk
import os
from players import Enemy
from plyerWindow import WindowPlayer
from pars import open_enemy
pths = os.getcwd().replace("new","")+"\\enemys\\"
def SetEnemy(name):
    en = Enemy(name)
    en.name = name
    pthsjpg = pths+"{}\\{}.jpg".format(name,name)
    f = open(pths+"{}\\{}.txt".format(name,name),'r', encoding='utf-8', errors = 'ignore')
    info = f.readlines()
    f.close()
    # print(info)
    en.picture_url = pthsjpg
    en.lvl = int(info[1].split(" ")[1].replace("\n",""))
    en.hp = int(info[2].split(" ")[1].replace("\n",""))
    en.classArmor = int(info[3].split(" ")[1].replace("\n",""))
    en.Dexterity = int(info[4].split(" ")[1].replace("\n",""))
    en.Strength = int(info[5].split(" ")[1].replace("\n",""))
    en.Constitution = int(info[6].split(" ")[1].replace("\n",""))
    en.Intelligence = int(info[7].split(" ")[1].replace("\n",""))
    en.Charisma = int(info[8].split(" ")[1].replace("\n",""))
    en.Wisdom = int(info[9].split(" ")[1].replace("\n",""))
    en.abilityList = info[13].split("::")[1].split("=")
    en.stateField = str(info[10].split(" ")[1].replace("\n",""))
    en.url = info[12].split(" ")[1]
    return en
class EnemyWindow(WindowPlayer):
    def __init__(self, name:str):
        super().__init__(SetEnemy(name))
        self.urlBut = None
        if "None" not in self.player.url:
            self.urlBut = tk.CTkButton(self,text = "Ссылка", command=lambda: open_enemy(self.player.url))
            self.urlBut.place(relx = 0.65, rely = 0.9 )
        self.abilText = tk.CTkTextbox(self,width=300,height=400)
        self.abilText.place(relx = 0.65, rely = 0.07)
        text = ""
        self.loadBut.destroy()
        self.file.destroy()
        for i in self.player.abilityList:
            text+=(i+"\n\n")
        self.abilText.insert("0.0",text = text)
        
