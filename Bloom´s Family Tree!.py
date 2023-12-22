#Bloom´s Family Tree!

listares = []
def famtree(a, b, c, d, e, f):
    ar=0
    br=0
    cr=0
    dr=0
    er=0
    fr=0
    if a == "Rose Schneider":
        ar += 1
    if b == "Michael Bloom":
        br += 1
    if c == "Constance Gardner":
        cr += 1
    if d == "Mickey Bloom":
        dr += 1
    if e == "Lucy Schneider":
        er += 1
    if f == "Timothy Schneider-Wilbour":
        fr += 1
    if ar == 1:
        listares.append(a)
    if br == 1:
        listares.append(b)
    if cr == 1:
        listares.append(c)
    if dr == 1:
        listares.append(d)
    if er == 1:
        listares.append(e)
    if fr == 1:
        listares.append(f)
    print("Você acertou os personagens: ",listares)

x = input("Mãe: \n")
y = input("Pai: \n")
z = input("Avó: \n")
w = input("Avô: \n")
q = input("Tia(o): \n")
p = input("Prima(o): \n")
famtree(x, y, z, w, q, p)