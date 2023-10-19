import customtkinter as ctk
from PIL import Image
from players import Player, Enemy
from players_window import show
from pars import open_enemy
from gameProcess import gameProcess
app = ctk.CTk()

def create_party():
    show(players_count)
        

        
def create_enemy_stat():
    enemy = Enemy("https://dnd.su/bestiary/307-vampire/")
    enemy_window = ctk.CTkToplevel()
    enemy_window.title("Враг")
    enemy_window.geometry("600x700")
    img = ctk.CTkImage(light_image=Image.open("C:\\Users\\kymsk\\Desktop\\dndauto\\pictures\\enemy\\307_1_1614262776.jpg"), size=(200,300))
    picEnemy = ctk.CTkLabel(enemy_window, image=img, text=enemy.stateField)
    picEnemy.place(relx = 0.01, rely = 0.01)
    about_loot = ctk.CTkLabel(enemy_window,bg_color="grey", text=enemy.about, width=100,height=100)
    about_loot.place(relx = 0.45, rely=0.01)
    mainStat = ctk.CTkLabel(enemy_window, text=enemy.get_stat_enemy()+"\n {}\n\n {}\n\n {}\n\n {}".format(enemy.speed, enemy.hp, enemy.classArmor, enemy.lvl),padx = 10 ,bg_color="grey", anchor=None, width=150,height=150)
    mainStat.place(relx = 0.01, rely = 0.45)
    urlButton = ctk.CTkButton(enemy_window, command=open_enemy, text="ссылка")
    urlButton.place(relx = 0.7, rely = 0.9)



app.title("game")
ctk.set_appearance_mode("dark")
app.geometry("500x500")
but = ctk.CTkButton(app, command=create_enemy_stat)
but.place(relx = 0.4, rely = 0.4)
app.mainloop()