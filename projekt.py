from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from functools import partial
import requests
import json
from datetime import datetime
from datetime import timedelta
from datetime import date
import os

failiAsukoht = os.path.dirname(os.path.abspath("projekt.py"))

kuupäev = "-".join(str(datetime.utcnow().date()).split("-")[::-1]) ## (dd,mm,yyyy)
r = requests.get("http://ssbudgeting.herokuapp.com/api/v1.0/users/1/items", auth=("sten", "pass"))
data = r.json()

## requests.get("http://ssbudgeting.herokuapp.com/api/v1.0/users/1/items?date=09-12-2014", auth=("sten", "pass"))

items =  {"toiduained": 0, "riided": 0, "sport": 0, "transport": 0, "restoran": 0, "meelelahutus": 0, "alkohol": 0, "teenused": 0, "kodu": 0, "muu": 0}
for item in data["items"]:
    items[item["category"]] += item["amount"]

today = date.today()
def esmaspäev(täna):
    esmaspäev = täna - timedelta(today.weekday())
    return "-".join(str(esmaspäev).split("-")[::-1])

nädalaalgus = esmaspäev(today)
def seenädal():
    nädalaandmed = requests.get("http://ssbudgeting.herokuapp.com/api/v1.0/users/1/items?from="+ nädalaalgus +"&to="+ kuupäev, auth=("sten", "pass"))
    nädalaanmedDict = nädalaandmed.json()

    items =  {"toiduained": 0, "riided": 0, "sport": 0, "transport": 0, "restoran": 0, "meelelahutus": 0, "alkohol": 0, "teenused": 0, "kodu": 0, "muu": 0}
    for item in nädalaanmedDict["items"]:
        items[item["category"]] += item["amount"]

def seekuu():
    kuunumber = str(datetime.utcnow().date().month).rjust(2, "0")
    aastanumber = datetime.utcnow().date().year
    kuuandmed =requests.get("http://ssbudgeting.herokuapp.com/api/v1.0/users/1/items?from=01-"+str(kuunumber)+"-"+str(aastanumber)+"&to="+ str(kuupäev), auth=("sten", "pass"))
    kuuandmedDict = kuuandmed.json()

    items =  {"toiduained": 0, "riided": 0, "sport": 0, "transport": 0, "restoran": 0, "meelelahutus": 0, "alkohol": 0, "teenused": 0, "kodu": 0, "muu": 0}
    for item in kuuandmedDict["items"]:
        items[item["category"]] += item["amount"]

def kokku():
    kuupäev = "-".join(str(datetime.utcnow().date()).split("-")[::-1]) ## (dd,mm,yyyy)
    r = requests.get("http://ssbudgeting.herokuapp.com/api/v1.0/users/1/items", auth=("sten", "pass"))
    data = r.json()

    items =  {"toiduained": 0, "riided": 0, "sport": 0, "transport": 0, "restoran": 0, "meelelahutus": 0, "alkohol": 0, "teenused": 0, "kodu": 0, "muu": 0}
    for item in data["items"]:
        items[item["category"]] += item["amount"]
    

def total(items):
    total = 0
    for key in items:
        if key != "id" and key != "userid":
            total += items[key]
    protsent(total)

def summa(liidetav):
    global items
    rahakast = sisestatavraha.get()
    items[liidetav] += float(rahakast) * 100
    headers = {"content-type": "application/json"}
    payload = {"category": liidetav, "amount": int(rahakast) * 100}
    r = requests.post("http://ssbudgeting.herokuapp.com/api/v1.0/items", headers=headers, data=json.dumps(payload), auth=("sten", "pass"))
    print(items)                                       ##KONTROLL
    total(items)
    sildid[liidetav]["text"] = items[liidetav] /100
    
    
def protsent(total):
    #PROTSENTARVUTUS
    tahvel.create_oval(üleminenurk, üleminenurk, aluminenurk, aluminenurk, fill = "white")
    toiduaineprotsent = (items["toiduained"] / total) * 360
    riieteprotsent = (items["riided"] / total) * 360 
    spordiprotsent = (items["sport"] / total) * 360
    transpordiprotsent = (items["transport"]/ total) * 360
    restoraniprotsent = (items["restoran"] / total) * 360
    meelelahutusprotsent = (items["meelelahutus"] / total) * 360
    alkoholiprotsent = (items["alkohol"] / total) * 360
    teenusteprotsent = (items["teenused"] / total) * 360
    koduprotsent = (items["kodu"] / total) * 360
    muuprotsent = (items["muu"] / total) * 360
    #PIECHART

    kaarealumine = 20
    kaareülemine = kõrgus - kaarealumine
    algus = 0
    tahvel.create_arc(kaarealumine,kaarealumine,kaareülemine,kaareülemine, start = algus, extent =toiduaineprotsent , fill = "#F54900", outline = "#F54900")
    algus += toiduaineprotsent
    tahvel.create_arc( kaarealumine, kaarealumine,kaareülemine,kaareülemine, start = algus, extent = riieteprotsent, fill = "#C6FA0C", outline = "#C6FA0C")
    algus += riieteprotsent
    tahvel.create_arc( kaarealumine, kaarealumine,kaareülemine,kaareülemine, start = algus, extent = spordiprotsent, fill = "#0CFAD2", outline = "#0CFAD2")
    algus += spordiprotsent
    tahvel.create_arc( kaarealumine, kaarealumine,kaareülemine,kaareülemine, start = algus, extent = transpordiprotsent, fill = "#0D089E", outline = "#0D089E")
    algus += transpordiprotsent
    tahvel.create_arc( kaarealumine, kaarealumine,kaareülemine,kaareülemine, start = algus, extent = restoraniprotsent, fill = "#FCFC47", outline = "#FCFC47")
    algus += restoraniprotsent
    tahvel.create_arc( kaarealumine, kaarealumine,kaareülemine,kaareülemine, start = algus, extent = meelelahutusprotsent, fill = "#3A3940", outline = "#3A3940")
    algus += meelelahutusprotsent
    tahvel.create_arc( kaarealumine, kaarealumine,kaareülemine,kaareülemine, start = algus, extent = alkoholiprotsent, fill = "#C72626", outline = "#C72626")
    algus += alkoholiprotsent
    tahvel.create_arc( kaarealumine, kaarealumine,kaareülemine,kaareülemine, start = algus, extent = teenusteprotsent, fill = "#8A059C", outline = "#8A059C")
    algus += teenusteprotsent
    tahvel.create_arc( kaarealumine, kaarealumine,kaareülemine,kaareülemine, start = algus, extent = koduprotsent, fill = "#B57010", outline = "#B57010")
    algus += koduprotsent
    tahvel.create_arc( kaarealumine, kaarealumine,kaareülemine,kaareülemine, start = algus, extent = muuprotsent, fill = "#0095FF", outline = "#0095FF")

    #KESKOSA
    tahvel.create_oval(üleminenurk, üleminenurk, aluminenurk, aluminenurk, fill = "white", outline = "white")
    kulutused = tahvel.create_text(kõrgus//2,laius//2, font = suur_suur_font, text = round(total / 100, 2))

##########################################################################################################

toiduained = items["toiduained"]
riided = items["riided"]
sport = items["sport"]
transport = items ["transport"]
restoran = items["restoran"]
meelelahutus = items["meelelahutus"]
alkohol = items["alkohol"]
teenused = items["teenused"]
kodu = items["kodu"]
muu = items["muu"]
sildid = dict()

#SUUR RAAM
raam = Tk()
raam.title("Finants kalkulaator")
raam.configure(background = "white")

## RAAM
suur_font= font.Font(family = "Microsoft JhengHei Light", size = 32)
väike_font=font.Font(family="Microsoft JhengHei Light", size=24)
suur_suur_font= font.Font(family = "Microsoft JhengHei Light", size = 40)

#LABELID
taust = "white"
toiduainedkokku = ttk.Label(raam, text = round(toiduained / 100, 2), font =väike_font)
sildid["toiduained"] = toiduainedkokku
toiduainedkokku.grid(column= 1, row = 1)
toiduainedkokku.config(background = taust)

transportkokku = ttk.Label(raam, text = round(transport / 100, 2), font = väike_font)
sildid["transport"] = transportkokku
transportkokku.grid(column=1, row=2)
transportkokku.config(background = taust)

restoransööminekokku = ttk.Label(raam, text = round(restoran / 100, 2), font = väike_font)
sildid["restoran"] = restoransööminekokku
restoransööminekokku.grid(column=1, row=3)
restoransööminekokku.config(background = taust)

kodukokku = ttk.Label(raam, text = round(kodu / 100, 2), font = väike_font)
sildid["kodu"] = kodukokku
kodukokku.grid(column=1, row=4)
kodukokku.config(background = taust)

sportkokku = ttk.Label(raam, text = round(sport / 100, 2), font = väike_font)
sildid["sport"] = sportkokku
sportkokku.grid(column=1, row=5)
sportkokku.config(background = taust)

teenusedkokku = ttk.Label(raam, text = round(teenused / 100, 2), font = väike_font)
sildid["teenused"] = teenusedkokku
teenusedkokku.grid(column=1, row=6)
teenusedkokku.config(background = taust)

alkoholkokku = ttk.Label(raam, text = round(alkohol / 100, 2), font = väike_font)
sildid["alkohol"] = alkoholkokku
alkoholkokku.grid(column=1, row=7)
alkoholkokku.config(background = taust)

meelelahutuskokku = ttk.Label(raam, text = round(meelelahutus / 100, 2), font = väike_font)
sildid["meelelahutus"] = meelelahutuskokku
meelelahutuskokku.grid(column=1, row=8)
meelelahutuskokku.config(background = taust)

riidedkokku = ttk.Label(raam, text = round(riided / 100, 2), font = väike_font)
sildid["riided"] = riidedkokku
riidedkokku.grid(column=1, row=9)
riidedkokku.config(background = taust)

muukokku = ttk.Label(raam, text = round(muu / 100, 2), font = väike_font)
sildid["muu"] = muukokku
muukokku.grid(column=1, row=10)
muukokku.config(background = taust)

## RAHAKAST
sisestatavraha = ttk.Entry(raam)
sisestatavraha.grid(column=0, row=11, padx=5, pady=5, sticky=(W,S,E), columnspan = 5)
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(11, weight = 1)

## NUPUD
toidupilt = PhotoImage(file = failiAsukoht + "/ikoonid/Toit_80.gif")
toiduliitmine = partial(summa, "toiduained")
nupp1 = ttk.Button(raam, text="toiduained",command = toiduliitmine, image = toidupilt)
nupp1.grid(column = 0, row = 1, padx=5, pady=5)
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(1, weight = 1)

autopilt = PhotoImage(file = failiAsukoht + "/ikoonid/auto_80.gif")
transpordiliitmine = partial(summa, "transport")
nupp2 = ttk.Button(raam, text="transport", command = transpordiliitmine, image = autopilt)
nupp2.grid(column = 0, row = 2, padx=5, pady=5)
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(2, weight = 1)

restoranipilt = PhotoImage(file = failiAsukoht + "/ikoonid/Restoran_80.gif")
söögiliitmine = partial(summa, "restoran")
nupp3 = ttk.Button(raam, text="väljas söömine", command = söögiliitmine, image = restoranipilt)
nupp3.grid(column = 0, row = 3, padx=5, pady=5)
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(3, weight = 1)

kodupilt = PhotoImage(file = failiAsukoht + "/ikoonid/kodu_80.gif")
koduliitmine = partial(summa, "kodu")
nupp4 = ttk.Button(raam, command=koduliitmine, image = kodupilt)   
nupp4.grid(column = 0, row = 4, padx=5, pady=5)
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(4, weight = 1)

spordipilt = PhotoImage(file = failiAsukoht + "/ikoonid/sport_80.gif")
spordiliitmine = partial(summa, "sport")
nupp5 = ttk.Button(raam, text="sport", command = spordiliitmine, image = spordipilt)
nupp5.grid(column = 0, row = 5, padx=5, pady=5)
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(5, weight = 1)

teenustepilt = PhotoImage(file = failiAsukoht + "/ikoonid/teenused_80.gif")
teenusteliitmine = partial(summa, "teenused")
nupp6 = ttk.Button(raam, text="teenused", command = teenusteliitmine, image = teenustepilt)
nupp6.grid(column = 0, row = 6, padx=5, pady=5)
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(6, weight = 1)

alkoholipilt = PhotoImage(file = failiAsukoht + "/ikoonid/Alkohol_80.gif")
alkoholiliitmine = partial(summa, "alkohol")
nupp7 = ttk.Button(raam, text="alkohol", command = alkoholiliitmine, image = alkoholipilt)
nupp7.grid(column = 0, row = 7, padx=5, pady=5)
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(7, weight = 1)

meelelahutuspilt = PhotoImage(file = failiAsukoht + "/ikoonid/Meelelahutus_80.gif")
meelelahutuseliitmine = partial(summa, "meelelahutus")
nupp8 = ttk.Button(raam, text="meelelahutus", command = meelelahutuseliitmine, image = meelelahutuspilt)
nupp8.grid(column = 0, row = 8, padx=5, pady=5)
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(8, weight = 1)

riietepilt = PhotoImage(file = failiAsukoht + "/ikoonid/Riided_80.gif")
riieteliitmine = partial(summa, "riided")
nupp9 = ttk.Button(raam, text="riided", command = riieteliitmine, image = riietepilt)
nupp9.grid(column = 0, row = 9, padx=5, pady=5)
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(9, weight = 1)

muupilt = PhotoImage(file = failiAsukoht + "/ikoonid/muu_80.gif")
muuliitmine = partial(summa, "muu")
nupp10 = ttk.Button(raam, text="muu", command = muuliitmine, image = muupilt)
nupp10.grid(column = 0, row = 10, padx=5, pady=5)
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(10, weight = 1)

nädalanupp = ttk.Button(raam, text= "See nädal", command = seenädal)
nädalanupp.grid(column = 4, row = 11, padx = 5, pady = 5,sticky = (N,W,S,E))
raam.columnconfigure(4, weight = 1)
raam.rowconfigure(11, weight = 1)

kuunupp = ttk.Button(raam, text = "See kuu", command = seekuu)
kuunupp.grid(column = 5, row = 11, padx = 5, pady = 5, sticky = (N,W,S,E))
raam.columnconfigure(5, weight = 1)
raam.rowconfigure(11, weight = 1)

kokkunupp = ttk.Button(raam, text = "Kokku", command = kokku)
kokkunupp.grid(column = 6, row = 11, padx = 5, pady = 5, sticky = (N,W,S,E))
raam.columnconfigure(6, weight = 1)
raam.rowconfigure(11, weight = 1)


##TAHVEL
kõrgus = 800
laius = 800
tahvel = Canvas(raam, background = "white", height = kõrgus, width= laius)
tahvel.grid(column = 2, row = 1, padx= 5, pady=5, columnspan = 5, rowspan = 10, sticky = (N, S , W ,E))

#KESKOSA
diameeter = kõrgus - 200
üleminenurk = int(tahvel["width"])/2 - diameeter/2
aluminenurk = int(tahvel["width"])/2 + diameeter/2

total(items)
raam.mainloop()

## PROOV

