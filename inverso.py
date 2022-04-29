
def euclides(a, b):
    if b == 0:
        return a
    else:
        return euclides(b, a % b)

def euclidesExt(x, y):
    if y == 0:
        return (x, 1, 0)
    else:
        (d, dx, dy) = euclidesExt(y, x % y)
        (x, y) = (dy, dx - x//y * dy)
        return (d, x, y)


def inverso(a, n):
    (mcd, x, y) = euclidesExt(a, n)
    if mcd == 1:
        return x % n
    return None

if __name__ == "__main__":
    a = int(input("Ingrese un entero a: "))
    n = int(input("Ingrese un entero positivo n: "))

    inv = inverso(a, n)

    if inv:
        print("El inverso de a (mod n) es : ", inv)
    else:
        print("No se puede calcular el inverso")
