"""fájlbeolvasáás"""
from Csomag import Csomag
def fajlbeolvasas():
    fajl=open("csomag.txt", "r", encoding="utf-8")
    #Megnyitom olvasásra a fájlomat
    fajl.readline() #Beolvas egyetlen sort, itt elöször a fejléct olvasuk be amire nincs szükségünk ezért nem mentjük el változoba
    fajbol_sorok_lista=fajl.readlines()#Beolvassa a többi sort amit egy listába tárolunk el
    fajl.close()

    '''
    1. megynitom a fájlt olvasásra.
    2. beolvasom a fejléc sort, ha van.
    3. beolbasom az összes sort egy listába- string lista
    4. bezárom a fájlt.
    5. sorokat átalakítom objektumokká, szétszedem a benne lévő adatokat.
    5.1 létrehozom az osztályt amibe majd beolvasom az adatokat ez a Csomag osztály
        5.2 végig megyek a listán és minden sorát feldolgozom egyenként
            5.2.1 eltüntetem a végéről az entereket
            5.2.2 szétvágom a szeparátorok mentén
    
    '''
    csomag_lista=[]#itt tárolom az elkészült csomag objektumaimat
    for i in range(0,len(fajbol_sorok_lista),1):
        aktelem=fajbol_sorok_lista[i] #beolvasom a lista i. elemét mindig
        sor_lista=aktelem.strip().split("#") #az aktuális elemnek eltávolitom az utolsó jelét az entert a strippel, majd szétdaraborm a splittel, és ezt az egészet egy uj listába olvasom be
        #új csomag leztehozása
        a=int(sor_lista[0])
        b=int(sor_lista[1])
        c=int(sor_lista[2])
        m=int(sor_lista[3])#itt megyadom hogy a feldarabolt elemek a lsitában hanyadik helyen állnak
        csomag=Csomag(a,b,c,m)
        #ezteket össze gyüjtük egy listába
        csomag_lista.append(csomag)
    return csomag_lista #vissza térek a csomag listával a ciklus után

def pogyasz_atlag_suly(lista):
    """ C.	Határozza meg és írassa ki a konzolra a minta szerint, hogy mennyi az 51 cm széles pogyászok
     átlag súlya gramban. (1kg = 1000g) (4p)"""
    osszeg=0
    db=0

    for i in range(0,len(lista),1):
        if (lista[i].a == 51):
            osszeg+= lista[i].m
            db+= 1

    return 1000*osszeg/db

def legmagasabb_pogyasz(csomag_lista):
    max:int=0
    max_index:int=0
    for i in range(0, len(csomag_lista),1):
        if  max> csomag_lista[i].b:
            max= csomag_lista[i].b
            max_index=i

    return max_index

