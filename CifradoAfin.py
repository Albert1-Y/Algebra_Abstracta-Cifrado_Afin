from inverso import inverso

ABC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


#--------------------------------------------
def cifrarAfin(m, clave):

    if not inverso(clave[0], 27):
        return None

    mesCifr = ""

    for c in m:
        cif = (clave[0] * ABC.find(c) + clave[1]) % 27
        mesCifr += ABC[cif]

    return mesCifr


#--------------------------------------------

def descifrarAfin(m, clave):

    inv = inverso(clave[0], 27)

    if not inv:
        return None
    mensDes = ""

    
    for c in m:
        des = (inv * (ABC.find(c) - clave[1])) % 27
        mensDes += ABC[des]
    return mensDes

#--------------------------------------------

if __name__ == "__main__":

    a=(int(input("ingrese a: ")))
    n=(int(input("ingrese n: ")))
    print(inverso(a,n))

    print()

    clave =[4,7]

    m1 = "ELEMENTALMIQUERIDOWATSON"
    m2 = "WXWBWFGHXBMUKWYMSNRHGCNF"
    print(cifrarAfin(m1,clave))
    print(descifrarAfin(m2,clave))

    print()