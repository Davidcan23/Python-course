# TODO proměnné
potraviny = { 
    'mleko': [30, 5], # index 0 -> cena; index 1 -> mnozstvi 
    'maso': [100, 1], 
    'banan': [30, 10], 
    'jogurt': [10, 5], 
    'chleb': [20, 5], 
    'jablko': [10, 10], 
    'pomeranc': [15, 10], 
}

nabidka = """
+-----------+----------+
| POTRAVINA |   CENA   |
+-----------+----------+
| mleko     |    30,-  |
| maso      |   100,-  |
| banan     |    30,-  |
| jogurt    |    10,-  |
| chleb     |    20,-  |
| jablko    |    10,-  |
| pomenrac  |    15,-  |
| jablko    |    20,-  |
| grep      |    45,-  |
+-----------+----------+
"""

kosik = {}

oddelovac = "=" * 35

# TODO Pozdrav a vypsání nabídky
print(
    'Vítejte u našeho nákupního košíku!', 
    oddelovac, 
    nabidka,
     'Zvol si zboží a pro zaplacení zaplať "q"',
     sep='\n')

# TODO celý cyklus
while (zbozi := input('Zadej název zboží:')) != 'q':

    # TODO pokud zboží nebude v nabídce
    if zbozi not in potraviny:
        print(zbozi, "bohužel není v nabídce")

    # TODO Pokud vybrané zboží není v nákupním košíku
    elif zbozi not in kosik and potraviny[zbozi][1] > 0:
        kosik[zbozi] = [potraviny[zbozi], 1]
        potraviny[zbozi][1] = potraviny[zbozi][1] - 1
        print(kosik)

    # TODO Pokud zboží ž je v košíku
    elif zbozi in kosik and potraviny[zbozi][1] > 0:
        kosik[zbozi][1] += 1
        potraviny[zbozi][1] -= 1
        print(kosik)
    # TODO Pokud zboží již není skladem
    elif potraviny[zbozi][1] == 0:
        print(f"{zbozi} již není na skladě")

# TODO vpiš obsah košíku
else:
    print(oddelovac, kosik, sep="\n")




