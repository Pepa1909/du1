from turtle import speed, up, down, setpos, forward, left, right, exitonclick, circle
# základní informace pro hráče
print("""
Dobrý den, 
budete hrát piškvorky, velikost herního pole i velikost čtverečků si můžete sami zvolit. Musíte sledovat jak hrací tabulku,
tak dodatečné informace v terminálu.
Souřadnice políček se vybírají pomocí souřadnice x a poté y jako na osách. Políčko nejvíce vlevo dole má souřadnice (1,1).
""") 
# jména hráčů pro oslovení během hry
hrac_1 = input("Jméno hráče 1: ")
print("Ty budeš hrát s křížky.")
hrac_2 = input("Jméno hráče 2: ")
print("Tvůj tvar jsou kolečka.")
# posun doleva dolů, aby bylo dost místa + vykreslení tabulky
speed(0)
up()
hrana = int(input("Jak velká má být hrana políčka?  (Ideální velikost cca 50-100):  "))
while hrana < 1:
    hrana = int(input("Nemůžeš mít zápornou ani nulovou délku hrany! Zadej znovu: "))
velikost_x = int(input("Kolik má mít hrací plocha sloupců? "))
while velikost_x < 1:
    velikost_x = int(input("Nemůžeš mít záporný nebo nulový počet sloupců! Zadej znovu: "))
velikost_y = int(input("Kolik má mít hrací plocha řádků? "))
while velikost_y < 1:
    velikost_y = int(input("Nemůžeš mít záporný nebo nulový počet řádků! Zadej znovu: "))
setpos(-350,-300)
down()
for _ in range (velikost_y):
    for _ in range(velikost_x):
        for _ in range(4):
            forward(hrana)
            left(90)
        forward(hrana)
    left(180)
    forward(hrana*velikost_x)
    right(90)
    forward(hrana)
    right(90)
# hra samotná - celý for cyklus - počet kol se odvíjí od velikosti hrací plochy
speed(6)
for kolo in range(velikost_x*velikost_y):
    up()
    # jak poznat sudé a liché kolo --> koho oslovit
    if kolo % 2 == 0:
        tah_x = (int(input(f"{hrac_1}, vyber x souřadnici, kde budeš chtít hrát: ")))
        while tah_x > velikost_x or tah_x <= 0:
            tah_x = int(input("Zkus to znovu, zadej souřadnici x: "))
        tah_y = (int(input(f"{hrac_1}, vyber y souřadnici, kde budeš chtít hrát: ")))
        while tah_y > velikost_y or tah_y <= 0:
            tah_y = int(input("Zkus to znovu, zadej souřadnici y: "))
    else:
        tah_x = (int(input(f"{hrac_2}, vyber x souřadnici, kde budeš chtít hrát: ")))
        while tah_x > velikost_x or tah_x <= 0:
            tah_x = int(input("zkus to znovu, zadej souřadnici x: "))
        tah_y = (int(input(f"{hrac_2}, vyber y souřadnici, kde budeš chtít hrát: ")))
        while tah_y > velikost_y or tah_y <= 0:
            tah_y = int(input("zkus to znovu, zadej souřadnici y: "))
    # želva zajede do správného políčka
    setpos(-350+(hrana/2)+hrana*(tah_x-1),-300+(hrana/2)+hrana*(tah_y-1))
    # jak se pozná, jestli se kreslí křížek nebo kolečko (jako u oslovení) + vykreslení tvaru
    if kolo % 2 == 0:
        down()
        left(45)
        for _ in range(4):
            forward(hrana/2)
            left(180)
            forward(hrana/2)
            left(90)
        right(45)
    else:
        right(90)
        forward(hrana*0.4)
        left(90)
        down()
        circle(hrana*0.4)
print("A jsme u konce, klikněte do okna piškvorek pro ukončení \U0001F642.")
exitonclick()