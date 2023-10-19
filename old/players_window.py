import customtkinter as ctk
import os
from pathlib import Path
from players import Player
from settPlayer import changeSett
play_window=None
segmBut = ""
def show(players_count):
    global play_window,segmBut
    play_window = ctk.CTkToplevel()
    play_window.title("Player list")
    play_window.geometry("500x500")
    play_window.attributes("-topmost",True)
    players_list = []
    folder = Path(os.getcwd()+"\\players")
    if len(list(folder.iterdir())) == 0:
        for i in range(int(players_count.get())):
            f= open(os.getcwd()+"\\players\\{}.txt".format(i),'x')
            f.close()
    for i in range(len(list(folder.iterdir()))):
        player = Player(i)
        
        # player = Enemy("https://dnd.su/bestiary/7758-alastrah/")
        label = ctk.CTkLabel(play_window, text=player.get_stat_player())
        players_list.append(player)
        label.grid(row=0, column=i, padx=(i+1)*10, pady=(10, 0), sticky="w")
        print(player.name)
    segmBut = ctk.CTkSegmentedButton(play_window, values=[i.name for i in players_list], command=change_player)
    segmBut.place(relx = 0.01, rely = 0.9)
def change_player(value):
    print("игрок № "+str(value))
    global play_window, segmBut
    # play_window.attributes("-topmost",False)
    # print(segmBut._value_list)
    changeSett(value, segmBut)
    

    
