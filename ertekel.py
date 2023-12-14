def adatbekeres():
    etel_neve:str=str(input("Étel neve: "))
    rendelo_neve:str=str(input("Étel rendelőjének neve: "))
    ertekeles:int=int(input("Értékelés (1-5): "))
    while not (ertekeles <= 1 and ertekeles >=5):
        