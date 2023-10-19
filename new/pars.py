import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver 
import time
def get_enemy_info(url:str):
    sourse = url
    mainStat = []
    subStat = []
    r = requests.get(sourse)
    soup = bs(r.text, "html.parser")
    enemy =soup.find_all('div',class_='cards-wrapper')
    enemy_name = enemy[0].find('h2', class_='card-title').text.split(' ')[0]
    enemy_about = enemy[0].find('li', class_='size-type-alignment').text
    enemy_stat = enemy[0].find_all('li')
    # armor_class = enemy_stat[2].text
    # enemy_hit = enemy_stat[3].text
    # enemy_speed = enemy_stat[4].text
    # enemy_atrib = enemy_stat[5].text
    # enemy_passiv = enemy_stat[6].text.replace('?', "") +"\n" +enemy_stat[11].text
    # enemy_lvl_exp = enemy_stat[7].text
    # enemy_bm = enemy_stat[8].text
    # enemy_activ = enemy_stat[12].text.replace("Действия", "")
    # enemy_list = [enemy_name,enemy_about,armor_class,enemy_hit,enemy_speed,enemy_atrib,enemy_passiv,enemy_lvl_exp,enemy_bm,enemy_activ]
    t = soup.find_all('p')
    for i in range(1,len(t)):
        subStat.append(t[i].text)
    for i in range(1,len(enemy_stat)):
        if "Источник" in enemy_stat[i].text:
            break
        if "?" in enemy_stat[i].text:
            mainStat.append(enemy_stat[i].text.replace("?", ""))
            continue
        mainStat.append(enemy_stat[i].text)
    
    return(mainStat, subStat) 
# r = get_enemy_info("https://dnd.su/bestiary/307-vampire/")
# # print(r[1])
# for i in range(len(r[1])):
#     print(r[1][i].split('.')[0])

def open_enemy(url):
    sourse = url
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(sourse)
    input()
    driver.quit()