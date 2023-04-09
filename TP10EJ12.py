"""12- Dada una cola de enteros no ordenada, escribir una función que:
(a) Devuelva el máximo elemento.
(b) Devuelva el promedio de los elementos.
(c) Inserte un elemento.
(d) Elimine los elementos iguales a k, siendo k un valor ingresado."""

cola = []
def carga():
    cant = input("Ingrese la cantidad de enteros: ")
    for i in range (n):
        n = input("Ingrese un numero: ")
        cola.append(n)

def proceso():
    max = 100
    c = 0
    s = 0
    prom = 0
    while len(cola)!=0:
        v = cola.pop
        s = s + v
        c+= 1
        if v > max:
            v = max
    print(f"Maximo elemento: {max}")
    prom = s / c
    print(f"Promedio de los elementos: {prom}")
    elem = input("Ingrese el elementoa insertar: ")
    while len(cola)!=0:
        #e = cola.pop
        cola.append(v, elem)
    while len(cola)!=0:
        e = cola.pop
        print(f"Cola con elemento nuevo: {e}")
    k = input("Ingrese el elemento k: ")
    while e == k:
        print(f"Cola sin elementos iguales a k: {e}")
