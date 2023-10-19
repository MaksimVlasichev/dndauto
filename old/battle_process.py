import customtkinter as ctk
from gameProcess import get_plyers
from settPlayer import CalcBonus
players_list = get_plyers()
name_list = []
initList = []
dict_init = {}
def initial_calc():
    def getin():
        for i in range(len(initList)):
            initList[i] = int(initList[i].get())+int(CalcBonus(players_list[i].Dexterity).replace('+',''))
        for i in range(len(name_list)):
            dict_init[name_list[i]] = initList[i]
        dict_init = dict(sorted(dict_init.items(), key=lambda item: item[1], reverse=True))
        print(dict_init)
        name_list = []
        initList = []
        return 0

    win = ctk.CTkToplevel()
    win.geometry("200x400")
    win.title("Инициатива")
    win.attributes("-topmost",True)
    ry=0.02
    for i in players_list:
        lab = ctk.CTkEntry(win, placeholder_text = i.name)
        initList.append(lab)
        lab.place(relx = 0.2, rely = ry)
        name_list.append(i.name)
        ry+=0.07
    print(name_list, initList)
    but = ctk.CTkButton(win, text = "Ввести", command=getin)
    but.place(relx = 0.2,rely = 0.9)
    return 0 
# def fight():
#     win = ctk.CTkToplevel()
#     win.title("Бой")
#     win.geometry("1000x700")
#     init = ctk.CTkFrame(win,width=1000)
#     init.grid(row=0, column=2, rowspan=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
#     init.grid_rowconfigure(4, weight=1)
#     for i in range(len(r.keys())):
#         lab = ctk.CTkLabel(master=init,text=list(r.keys())[i])
#         lab.grid(row = 0, column = i)
