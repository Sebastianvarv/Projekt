from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from functools import partial

items=  {"id":2, "userid": 1, "toiduained": 100, "riided": 110, "sport":120, "transport": 130, "restoran": 140, "meelelahutus": 150, "alkohol": 160, "teenused": 170, "kodu": 180, "muu": 190}

def total(items):
    total = 0 
    for key in items:
        if key != "id" and key != "userid":
            total += items[key]
    protsent(total)
    

def summa(liidetav):
    global items
    rahakast = sisestatavraha.get()
    items[liidetav] += float(rahakast)
    print(items)                                       ##KONRTOLL
    total(items)
    sildid[liidetav]["text"] = items[liidetav]
    
    
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
    algus = 0
    tahvel.create_arc(20,20,780,780, start = algus, extent =toiduaineprotsent , fill = "blue", outline = "blue")
    algus += toiduaineprotsent
    tahvel.create_arc(20,20,780,780, start = algus, extent = riieteprotsent, fill = "orange", outline = "orange")
    algus += riieteprotsent
    tahvel.create_arc(20,20,780,780, start = algus, extent = spordiprotsent, fill = "green", outline = "green")
    algus += spordiprotsent
    tahvel.create_arc(20,20,780,780, start = algus, extent = transpordiprotsent, fill = "yellow", outline = "yellow")
    algus += transpordiprotsent
    tahvel.create_arc(20,20,780,780, start = algus, extent = restoraniprotsent, fill = "red", outline = "red")
    algus += restoraniprotsent
    tahvel.create_arc(20,20,780,780, start = algus, extent = meelelahutusprotsent, fill = "cyan", outline = "cyan")
    algus += meelelahutusprotsent
    tahvel.create_arc(20,20,780,780, start = algus, extent = alkoholiprotsent, fill = "magenta", outline = "magenta")
    algus += alkoholiprotsent
    tahvel.create_arc(20,20,780,780, start = algus, extent = teenusteprotsent, fill = "purple", outline = "purple")
    algus += teenusteprotsent
    tahvel.create_arc(20,20,780,780, start = algus, extent = koduprotsent, fill = "brown", outline = "brown")
    algus += koduprotsent
    tahvel.create_arc(20,20,780,780, start = algus, extent = muuprotsent, fill = "grey", outline = "grey")
    #KESKOSA
    tahvel.create_oval(üleminenurk, üleminenurk, aluminenurk, aluminenurk, fill = "white", outline = "white")
    kulutused = tahvel.create_text(400,400, font = suur_suur_font, text = total)

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
toiduainedkokku = ttk.Label(raam, text = toiduained, font =väike_font)
sildid["toiduained"] = toiduainedkokku
toiduainedkokku.grid(column= 1, row = 1)
toiduainedkokku.config(background = taust)

transportkokku = ttk.Label(raam, text = transport, font = väike_font)
sildid["transport"] = transportkokku
transportkokku.grid(column=1, row=2)
transportkokku.config(background = taust)

restoransööminekokku = ttk.Label(raam, text = restoran, font = väike_font)
sildid["restoran"] = restoransööminekokku
restoransööminekokku.grid(column=1, row=3)
restoransööminekokku.config(background = taust)

kodukokku = ttk.Label(raam, text = kodu, font = väike_font)
sildid["kodu"] = kodukokku
kodukokku.grid(column=1, row=4)
kodukokku.config(background = taust)

sportkokku = ttk.Label(raam, text = sport, font = väike_font)
sildid["sport"] = sportkokku
sportkokku.grid(column=1, row=5)
sportkokku.config(background = taust)

teenusedkokku = ttk.Label(raam, text = teenused, font = väike_font)
sildid["teenused"] = teenusedkokku
teenusedkokku.grid(column=1, row=6)
teenusedkokku.config(background = taust)

alkoholkokku = ttk.Label(raam, text = alkohol, font = väike_font)
sildid["alkohol"] = alkoholkokku
alkoholkokku.grid(column=1, row=7)
alkoholkokku.config(background = taust)

meelelahutuskokku = ttk.Label(raam, text = meelelahutus, font = väike_font)
sildid["meelelahutus"] = meelelahutuskokku
meelelahutuskokku.grid(column=1, row=8)
meelelahutuskokku.config(background = taust)

riidedkokku = ttk.Label(raam, text = riided, font = väike_font)
sildid["riided"] = riidedkokku
riidedkokku.grid(column=1, row=9)
riidedkokku.config(background = taust)

muukokku = ttk.Label(raam, text = muu, font = väike_font)
sildid["muu"] = muukokku
muukokku.grid(column=1, row=10)
muukokku.config(background = taust)

## RAHAKAST
sisestatavraha = ttk.Entry(raam)
sisestatavraha.grid(column=0, row=11, padx=5, pady=5, sticky=(W,S,E), columnspan = 3)
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(11, weight = 1)

## NUPUD
toiduliitmine = partial(summa, "toiduained")
nupp1 = ttk.Button(raam, text="toiduained",command = toiduliitmine)
nupp1.grid(column = 0, row = 1, padx=5, pady=5, sticky=(N,S,W,E))
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(1, weight = 1)

transpordiliitmine = partial(summa, "transport")
nupp2 = ttk.Button(raam, text="transport", command = transpordiliitmine)
nupp2.grid(column = 0, row = 2, padx=5, pady=5, sticky=(N,S,W,E))
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(2, weight = 1)

söögiliitmine = partial(summa, "restoran")
nupp3 = ttk.Button(raam, text="väljas söömine", command = söögiliitmine)
nupp3.grid(column = 0, row = 3, padx=5, pady=5, sticky=(N,S,W,E))
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(3, weight = 1)

kodu = PhotoImage(file = "C:/Users/Sebastian/Documents/Kool/Programmeerimine/Projekt/kodu.gif")
koduliitmine = partial(summa, "kodu")
nupp4 = ttk.Button(raam, command=koduliitmine, image = kodu)    ##PROOVIPILT
nupp4.grid(column = 0, row = 4, padx=5, pady=5)
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(4, weight = 1)

spordiliitmine = partial(summa, "sport")
nupp5 = ttk.Button(raam, text="sport", command = spordiliitmine)
nupp5.grid(column = 0, row = 5, padx=5, pady=5, sticky=(N,S,W,E))
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(5, weight = 1)

teenusteliitmine = partial(summa, "teenused")
nupp6 = ttk.Button(raam, text="teenused", command = teenusteliitmine)
nupp6.grid(column = 0, row = 6, padx=5, pady=5, sticky=(N,S,W,E))
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(6, weight = 1)

alkoholiliitmine = partial(summa, "alkohol")
nupp7 = ttk.Button(raam, text="alkohol", command = alkoholiliitmine)
nupp7.grid(column = 0, row = 7, padx=5, pady=5, sticky=(N,S,W,E))
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(7, weight = 1)

meelelahutuseliitmine = partial(summa, "meelelahutus")
nupp8 = ttk.Button(raam, text="meelelahutus", command = meelelahutuseliitmine)
nupp8.grid(column = 0, row = 8, padx=5, pady=5, sticky=(N,S,W,E))
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(8, weight = 1)

riieteliitmine = partial(summa, "riided")
nupp9 = ttk.Button(raam, text="riided", command = riieteliitmine)
nupp9.grid(column = 0, row = 9, padx=5, pady=5, sticky=(N,S,W,E))
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(9, weight = 1)

muuliitmine = partial(summa, "muu")
nupp10 = ttk.Button(raam, text="muu", command = muuliitmine)
nupp10.grid(column = 0, row = 10, padx=5, pady=5, sticky=(N,S,W,E))
raam.columnconfigure(0, weight = 1)
raam.rowconfigure(10, weight = 1)

##TAHVEL
kõrgus = 800
laius = 800
tahvel = Canvas(raam, background = "white", height = kõrgus, width= laius)
tahvel.grid(column = 2, row = 1, padx= 5, pady=5, columnspan = 2, rowspan = 10, sticky = (N, S , W ,E))

#KESKOSA
diameeter = 600
üleminenurk = int(tahvel["width"])/2 - diameeter/2
aluminenurk = int(tahvel["width"])/2 + diameeter/2




##tahvel.create_oval(üleminenurk, üleminenurk, aluminenurk, aluminenurk, fill = "white")
##
##kulutused = tahvel.create_text(400,400, font = suur_font)


##toiduained_id = tahvel.create_text(text = str(toiduained))
##toiduained.id.grid(column = 1, row = 1)

##p1 = image.open("porgand.jpeg")
##foto1 = imageTk.PhotoImage(image1)
##
##button1 = tk.Button(raam, compound=tk.TOP, width=250, height=250, image=foto1, bg = "blue")
##button1.grid(column=1 , row = 1, padx = 5 , pady=5, sticky=(N, S , W, E))

##totalsilt = ttk.Label(raam, text = "Total: ", font = suur_font)
##totalsilt.grid( column=1, row=0, padx= 5, pady= 5, sticky= (N))
##totalsilt.config(background = taust)
##
##totalkokku = ttk.Label(raam, font=suur_font)
##totalkokku.grid(column = 2, row = 0, padx=5, pady=5, sticky= (N))
##totalkokku.config(background = taust)
total(items)
raam.mainloop()

