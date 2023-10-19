from pars import get_enemy_info
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
    def __init__(self, nam:str) -> None:
        self.name = nam
    pass
class Player(Object):
    def __init__(self,nae) -> None:
        self.name = nae
    iniciat = 0
    vdohn = False
    
    def get_stat_player(self):
        return "{}\n\nЛовкость {}\nСила {}\nТелосложение {}\nИнтеллект {}\nХаризма {}\nМудрость {}\nСпособности {}".format(self.name, self.Dexterity, self.Strength,
                                                                                     self.Constitution,self.Intelligence, self.Charisma,self.Wisdom,self.abilityList)
    pass
class Enemy(Object):
    
    def __init__(self, url) -> None:
        self.info = get_enemy_info(url)
        self.stateField = "мёртв"
        self.lootList = []
        self.about = self.info[0][0]
        self.speed = self.info[0][3]
        self.hp = self.info[0][2]
        self.classArmor = self.info[0][1]

        self.Dexterity = self.info[0][4].split(')')[1]+')'
        self.Strength = self.info[0][4].split(')')[0]+')'
        self.Constitution = self.info[0][4].split(')')[2]+')'
        self.Intelligence = self.info[0][4].split(')')[3]+')'
        self.Charisma = self.info[0][4].split(')')[5]+')'
        self.Wisdom = self.info[0][4].split(')')[4]+')'

        j = 0
        for i in range(len(self.info[0])):
            if "опыта" in self.info[0][i]:
                j = i
        self.lvl = self.info[0][j]
    
   
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