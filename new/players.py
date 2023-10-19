from pars import get_enemy_info
import os
from PIL import Image
class Object:
    picture_url = ""
    speed = 0
    lvl = 0
    hp = 0
    classArmor = 0
    name:str = ""
    Dexterity = 0 #ловкость
    Strength = 0 #сила
    Constitution = 0 #телосложение
    Intelligence = 0 #интеллект
    Charisma = 0 #харизма
    Wisdom = 0 #мудрость
    abilityList = []
    stateField = ""
    masterBonus = 2
    maxHp = 0
    money = 0
    
    def __init__(self, nam:str) -> None:
        self.name = nam
    pass
class Player(Object):
    def __init__(self,nae) -> None:
        self.name = nae
    iniciat = 0
    vdohn = False
    def getUrlPic(self):
        self.picture_url = Image.open(os.getcwd()+"\\players\\pictures\\{}.png".format(self.name))
        print(self.picture_url)
    def initialplayer(self):
        path = os.getcwd()+"\\players\\{}.txt".format(self.name)
        print(path)
        # pathing = os.getcwd().replace("new","")+"\\players\\{}\\{}.jpg".format(self.name,self.name)
        f = open(path,'r', encoding='utf-8', errors = 'ignore')
        info = f.readlines()
        f.close()
        self.getUrlPic()
        self.lvl = int(info[1].split(" ")[1].replace("\n",""))
        self.hp = int(info[2].split(" ")[1].replace("\n",""))
        self.classArmor = int(info[3].split(" ")[1].replace("\n",""))
        self.Dexterity = int(info[4].split(" ")[1].replace("\n",""))
        self.Strength = int(info[5].split(" ")[1].replace("\n",""))
        self.Constitution = int(info[6].split(" ")[1].replace("\n",""))
        self.Intelligence = int(info[7].split(" ")[1].replace("\n",""))
        self.Charisma = int(info[8].split(" ")[1].replace("\n",""))
        self.Wisdom = int(info[9].split(" ")[1].replace("\n",""))
        self.abilityList = info[11].split(",")
        self.stateField = str(info[10].split(" ")[1].replace("\n",""))
        self.maxHp = str(info[13].split(" ")[1].replace("\n",""))
        self.money = str(info[14].split(" ")[1].replace("\n",""))


    def get_stat_player(self):
        return "{}\n\nЛовкость {}\nСила {}\nТелосложение {}\nИнтеллект {}\nХаризма {}\nМудрость {}\nСпособности {}".format(self.name, self.Dexterity, self.Strength,
                                                                                     self.Constitution,self.Intelligence, self.Charisma,self.Wisdom,self.abilityList)

class Enemy(Object):
    
    def __init__(self,name):
        path = os.getcwd()+"\\enemys\\{}\\{}.txt".format(name,name)
        pathing = os.getcwd().replace("new","")+"\\enemys\\{}\\{}.jpg".format(name,name)
        f = open(path,'r', encoding='utf-8', errors = 'ignore')
        info = f.readlines()
        f.close()
        self.name = name
        self.stateField = "жив"
        self.lootList = []
        self.about = ""
        self.speed = 5
        self.hp = int(info[2].split(" ")[1].replace("\n",""))
        self.classArmor = int(info[3].split(" ")[1].replace("\n",""))
        self.url = info[12].split(" ")[1]
        self.Dexterity = int(info[4].split(" ")[1].replace("\n",""))
        self.Strength = int(info[5].split(" ")[1].replace("\n",""))
        self.Constitution = int(info[6].split(" ")[1].replace("\n",""))
        self.Intelligence = int(info[7].split(" ")[1].replace("\n",""))
        self.Charisma = int(info[8].split(" ")[1].replace("\n",""))
        self.Wisdom = int(info[9].split(" ")[1].replace("\n",""))
        self.picture_url = str(pathing)

   
    def get_stat_enemy(self):
        return "{}\nЛовкость {}\n\nСила {}\n\nТелосложение {}\n\nИнтеллект {}\n\nХаризма {}\n\nМудрость {}\n".format(self.name, self.Dexterity, self.Strength,
                                                                                     self.Constitution,self.Intelligence, self.Charisma,self.Wisdom)
    def get_picture(self):
        return self.picture_url
    def get_about(self):
        return self.about
    def get_loot(self):
        return self.lootList
    def set_loot(self, loot:list):
        self.lootList = loot
        return 0
    def get_ability(self):
        return self.abilityList
    pass