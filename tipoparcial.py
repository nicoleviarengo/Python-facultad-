"""2.- En una empresa de correos se deben cargar un camión con sacos de cartas destinados a la ciudad de Córdoba.  
Para tener un control de los sacos que se envía se pide cargar una estructura pila teniendo en cuenta 
el orden de carga de los sacos en el camión con el número de identificación de cada saco (4 dígitos – validar).
En el lugar de destino se debe procesar la carga y determinar:
•	Mostrar el número de identificación más grande que tiene los sacos del camión.
•	Generar y mostrar una cola con los sacos mayores a 3500 y menores a 5004.
•	Depurar la carga del camión para que queden aquellos sacos que no se cargaron en la cola."""

pila = []
cola = []

def carga():
    cant = input("Ingrese la cantidad de camiones: ")
    for i in range (cant):
        num = input("Ingrese el numero de identificacion: ")
    while num <= 999 and num > 9999: #validacion que sea de 4 digitos
        print("Debe ser de 4 digitos")
        num = input("Ingrese el numero de identificacion: ")
        while num != 0:
            pila.append(num)
carga()

def proceso():
    #Numero de identificacion mas grande
    max = 9999
    while len(pila)!=0:
        v = pila.pop
        if v > max:
            v = max
    print(f"Mayor numero de identificacion: {max}")
    #Cola
    if v > 3500 and v < 5004:
        cola.append(v)
    while len(cola)!=0:
        c = cola.pop
        print(f"Sacos mayores a 3500 y menores a 5004: {c}")
    else:
        pila.append(v)
    while len(pila)!=0:
        p = pila.pop
        print(f"Pila con el resto de los elementos: {p}")
proceso()