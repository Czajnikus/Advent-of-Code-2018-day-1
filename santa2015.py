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
                print('ddd')
                break
        elif x == ")":
            pietro -= 1
            n += 1
            if pietro == -1:
                print('dd')
                break

print(pietro)
print(n)