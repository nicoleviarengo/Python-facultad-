"""En una oficina administrativa se atienden N personas con su número de trámite. 
Para su atención se debe cargar cada tramite en dos pilas de acuerdo con un número de tramite 
X siendo X un número leído con anterioridad. En una PILA1 se debe cargar los tramites 
menores o iguales a X y el la PILA2 los tramites mayores a X.
•	Se debe cargar en una cola los tramites cuyo numero sean múltiplos de 4.
•	Visualizar los números que sean capicúas y en que pila están ubicados."""

pila1 = []
pila2 = []
cola = []

def carga(n):
    for i in range (n):
        num = input("Ingrese el numero de tramite: ")
    x = input("Ingrese el numero X: ")
    if num >= x:
        pila1.append(num)
    if num > x:
        pila2.append(num)

def multiplos():
    while len(pila1) and len(pila2) !=0:
        v1 = pila1.pop
        v2 = pila2.pop
        if v1 % 4 !=0 and v2 %4 !=0:
            cola.append(v1, v2)
    while len(cola)!=0:
        c = cola.pop
        print(f"Multiplos de 4: {c}")

def invertir_numero():
    p1 = pila1.pop
    p2 = pila2.pop
    numero = 0
    while p1!= 0:
        numero = 10*numero+p1%10
        numero//=10
    while p2 !=0:
        numero = 10*numero+p2%10
        numero//=10

def capicua(numero, p1, p2):
    if numero == invertir_numero(p1):
        print(f"Numero capicua: {numero} en la pila1")
    elif numero == invertir_numero(p2):
        print(f"Numero capicua: {p2} en la pila2")

n = input("Ingrese la cantidad de personas: ")
carga(n)
capicua()
multiplos()

