import asyncio
from typing import Optional, Tuple, Union
import customtkinter as tk
from CreatePlayers import Createplayers
from GameProcess import GameLaunch
tk.set_appearance_mode("dark")
class MainWindow(tk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Игра")
        self.geometry("500x500")
        self.lab = tk.CTkLabel(master=self, text = "Кол-во игроков").place(relx=0.4,rely = 0.35)
        self.players_count = tk.CTkEntry(master=self)
        self.players_count.grid()
        self.players_count.place(relx=0.4,rely = 0.4)
        self.button = tk.CTkButton(master=self,width=10,height=10, text= "Начать", command= lambda: asyncio.run(self.create_party()))
        self.buttonEn = tk.CTkButton(master=self,width=10,height=10, text= "Враг", command=self.create_enemy_stat)
        self.continueBut = tk.CTkButton(master=self,width=10,height=10, text= "Продолжить", command=lambda: asyncio.run(self.gameProcess()))
        self.button.place(relx=0.4,rely = 0.46)
        self.continueBut.place(relx=0.4,rely = 0.51)
        self.buttonEn.place(relx=0.4,rely = 0.6)
    async def create_party(self):
        cp = Createplayers(playersCount=int(self.players_count.get()))
        MainWindow.destroy(self)
        await cp.mainloop()
    def create_enemy_stat(self):
        print("enemy")
        pass
    async def gameProcess(self):
        MainWindow.destroy(self)
        gp = GameLaunch()
        await gp.mainloop()








if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()