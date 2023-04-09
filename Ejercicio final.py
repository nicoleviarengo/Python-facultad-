""""Un minisupermercado cuenta con dos cajeras, cada día se guarda el total recaudado
por la cajera en una estructura pila. Cada cajera tiene su estructura pila generada y al final de la semana,
se realiza la suma del total de ventas de cada cajera y a la que mayor recaudación tiene se le da un premio.
La suma del total de ventas por día se debe cargar en una Cola.
Escribir un programa que permita ingresar la recaudación diaria de cada cajera y conocer:
•	El día de menor venta de cada cajera
•	crear una función que permita determinar cuál es la cajera que recibirá el premio.
•	Mostrar el día de la semana con la suma total de lo recaudado en el mismo."""

cajera1=[]
cajera2=[]
def proceso ():
    suma=0
    suma2=0
    c=0
    c2=0
    min = 1000
    min2 = 1000
    lugar = 0 #inicializo posicion
    lugar2 = 0
    pos=0
    pos2=0
    print("Ingrese la recaudacion diaria de la Cajera 1: ")
    for i in range(7):
        recaudacion1=float(input())
        cajera1.append(recaudacion1)
        suma=suma+recaudacion1
    print("Ingrese la recaudacion diaria de la Cajera 2: ")
    for j in range(7):
        recaudacion2=float(input())
        cajera2.append(recaudacion2)
        suma2=suma2+recaudacion2
    if (suma>suma2):
        print(f"La cajera 1 es merecedora del premio con una recaudacion de -{suma}-")
    else:
        print(f"La cajera 2 es merecedora del premio con una recaudacion de -{suma2}-")
    while len(cajera1)!=0:
        v=cajera1.pop()
        print(f"-{c}- --> -{v}-")
        c+=1
        if(v<min):
            min=v
            pos=lugar
        lugar += 1
    print(f"La menor venta de la cajera 1 fue el dia -{pos}-")
    print() #salto de linea
    while len(cajera2)!=0:
        f=cajera2.pop()
        print(f"-{c2}- --> -{f}-") #muestro posicion y valor ingresado
        c2+=1 #incremento posicion
        if (f<min2):
            min2=f
            pos2=lugar2
        lugar2+=1
    print(f"La menor venta de la cajera 2 fue el dia -{pos2}-")

proceso()

