from turtle import *
# základní informace pro hráče
print("""
Dobrý den, 
budete hrát piškvorky v šestiúhelníkovém poli 3x3. Musíte sledovat jak hrací tabulku, tak dodatečné informace v terminálu.
Během hry může kdykoliv napsat quit a tím hru ukončit.
Rozmístění políček je následující:
         3 
     2       6
 1       5       9
     4       8
         7
""")
# jména hráčů pro oslovení během hry
hrac_1 = input("Jméno hráče 1: ")
print("Vy budete hrát s křížky.")
hrac_2 = input("Jméno hráče 2: ")
print("Váš tvar jsou kolečka.")
# posun doleva dolů, aby bylo dost místa + vykreslení tabulky 3x3
speed(0)
up()
left(180)
forward(300)
left(180)
down()
for _ in range(3):
    for _ in range(3):
        for _ in range(6):
            forward(50)
            left(60)
        forward(50)
        left(60)
        forward(50)
        right(60)
    right(120)
    for _ in range(3):
            forward(50)
            right(60)
            forward(50)
            left(60)
    left(120)
    forward(50)
    right(60)
    up()
    forward(50)
    left(60)
    down()
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
        setpos(-275, 8)
    elif tah == 2:
        setpos(-200,51)
    elif tah == 3:
        setpos(-125,94)         
    elif tah == 4:
        setpos(-200,-35)
    elif tah == 5:
        setpos(-125,8)
    elif tah == 6:
        setpos(-50, 51)         
    elif tah == 7:
        setpos(-125, -78)
    elif tah == 8:
        setpos(-50, -35)     
    elif tah == 9:
        setpos(25,8)
# jak se pozná, jestli se kreslí křížek nebo kolečko (jako u oslovení) + vykreslení tvaru
    if kolo % 2 == 0:
        left(90)
        forward(35)
        left(45)
        down()
        for _ in range(4):
            forward(40)
            left(180)
            forward(40)
            left(90)
        right(135)
    else:
        down()
        circle(35)
print("A jsme u konce, klikněte do okna piškvorek pro ukončení.")
exitonclick()