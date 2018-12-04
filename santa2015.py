pietro = 0
n = 0
with open('santa2015.txt', 'r') as f:
    tekst = f.read()

lista = [wyraz for wyraz in tekst]

while pietro != -1:
    for x in tekst:
        if x == "(":
            pietro += 1
            n += 1
            if pietro == -1:
                break
        elif x == ")":
            pietro -= 1
            n += 1
            if pietro == -1:
                break

print(pietro) # na którym aktualnie piętrze jest Mikołaj
print(n) # ile ruchów Mikołaj wykonał, aby po raz pierwszy wejść do piwnicy (-1)