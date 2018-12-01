
wynik = 0
tablica = []
przerwij = 0

with open('tekst.txt', 'r+') as f:
    lista_linii = [linia.rstrip() for linia in f]

while True:
    for wartosc in lista_linii:
        if wartosc[0] == "+":
            wynik = int(wynik) + int(wartosc[1:])
            tablica.append(wynik)
            if tablica.count(wynik) > 1:
                print("Powtórzony: %d" % wynik)
                przerwij = 1
                break
        elif wartosc[0] == "-":
            wynik = int(wynik) - int(wartosc[1:])
            tablica.append(wynik)
            if tablica.count(wynik) > 1:
                print("Powtórzony: %d" % wynik)
                przerwij = 1
                break
    if przerwij == 1:
        break
    print(len(tablica))
