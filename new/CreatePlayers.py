from typing import Optional, Tuple, Union
import customtkinter as tk
import os 
class Createplayers(tk.CTk):
    def __init__(self, playersCount:int):
        super().__init__()
        self.title("Player list")
        self.geometry("500x500")
        self.lbCount = tk.CTkLabel(self, text= str(playersCount))
        self.lbCount.place(relx = 0.5, rely = 0.5)