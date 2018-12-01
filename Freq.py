
wynik = 0


with open('tekst.txt', 'r+') as f:
    lista_linii = [line.rstrip() for line in f]
    print(lista_linii)

for wartosc in lista_linii:
    if wartosc[0] == "+":
        wynik=int(wynik) + int(wartosc[1:])
    elif wartosc[0] == "-":
        wynik=int(wynik) - int(wartosc[1:])
    print(wynik)


