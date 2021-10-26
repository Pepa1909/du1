from turtle import *
# základní informace pro hráče
print("""
Dobrý den, 
budete hrát piškvorky v poli 3x3. Musíte sledovat jak hrací tabulku, tak dodatečné informace v terminálu.
Během hry může kdykoliv napsat quit a tím hru ukončit.
Rozmístění políček je jako na numerické klávesnici, tedy takto:
7  8  9
4  5  6
1  2  3
""")
# jména hráčů pro oslovení během hry
hrac_1 = input("Jméno hráče 1: ")
print("Vy budete hrát s křížky.")
hrac_2 = input("Jméno hráče 2: ")
print("Váš tvar jsou kolečka.")
# posun doleva dolů, aby bylo dost místa + vykreslení tabulky 3x3
speed(0)
up()
setpos(-250,-150)
down()
hrana=100
for _ in range (3):
    for _ in range(3):
        for _ in range(4):
            forward(hrana)
            left(90)
        forward(hrana)
    left(180)
    forward(hrana*3)
    right(90)
    forward(hrana)
    right(90)
# hra samotná - celý for cyklus
speed(6)
for kolo in range(9):
    up()
# jak poznat sudé a liché kolo --> koho oslovit
    if kolo % 2 == 0:
        tah = (int(input(f"{hrac_1}, vyber políčko (čísla 1-9): ")))
    else:
        tah = (int(input(f"{hrac_2}, vyber políčko (čísla 1-9): ")))
# želva zajede do správného políčka
    while tah < 1 or tah > 9:
        tah = int(input("zkus to znovu: "))
    if tah == 1:
        setpos(-200, -140)
    elif tah == 2:
        setpos(-100,-140)
    elif tah == 3:
        setpos(0,-140)         
    elif tah == 4:
        setpos(-200, -40)
    elif tah == 5:
        setpos(-100,-40)
    elif tah == 6:
        setpos(0,-40)         
    elif tah == 7:
        setpos(-200, 60)
    elif tah == 8:
        setpos(-100, 60)     
    elif tah == 9:
        setpos(0,60)
# jak se pozná, jestli se kreslí křížek nebo kolečko (jako u oslovení) + vykreslení tvaru
    if kolo % 2 == 0:
        left(90)
        forward(40)
        left(45)
        down()
        for _ in range(4):
            forward(60)
            left(180)
            forward(60)
            left(90)
        right(135)
    else:
        down()
        circle(40)
print("A jsme u konce, klikněte do okna piškvorek pro ukončení.")
exitonclick()
    