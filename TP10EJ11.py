"""11- Simular el funcionamiento de una cola frente a la boletería de un teatro. Crear una
estructura Boletería, donde las personas llegan y compran una o más entradas. Diseñar
un programa que cargue la cola hasta que no haya más personas para ser atendidas y se
le pida a cada una la cantidad de entradas a comprar. Si se ingresa inicialmente la
cantidad de lugares disponibles de la sala y el precio de la entrada, se desea saber
después de la función la cantidad de personas que compraron entradas, el monto
obtenido por las ventas y la cantidad de entradas sobrantes."""

colaB = []

def ingreso():
    s = 0
    print("1)Agregar entradas\n")
    print("2)Salir\n")
    n = int(input())
    while n!=1 or n!=2:
        print("1)Agregar entradas\n")
        print("2)Salir\n")
        n = int(input())
    while n!=2 and s<entradas:
        if n == 1:
            print("Ingrese la cantidad de entradas: ")
            entradas = int(input())
            s = s+entradas
        if s < disp:
            colaB.append(entradas)
        if s>disp:
            s = s - entradas
            print(f"Quedan {disp - s} entradas")
            print("Ingrese la cantidad de entradas: ")
            entradas = int(input())
            s = s+ entradas
            if entradas!=0:
                colaB.append(entradas)
            elif s==disp:
                colaB.append(entradas)
                print("Entradas agotadas") # Aca pasar a la otra cola
        if s< disp:
            print("1)Agregar entradas\n")
            print("2)Salir\n")
            n = int(input())
        while n>2:
            print("1)Agregar entradas\n")
            print("2)Salir\n")
            n = int(input())

def totales(disp):
    personas = 0
    total = 0
    while len(colaB)!=0:
        v = colaB.pop
        personas +=1
        total = total + v
    monto = total*precio
    print(f"Cantidad de personas que compraron entradas: {personas}")
    print(f"Monto total: {monto}")
    sobrantes = disp - total
    if sobrantes == 0:
        print(f"No sobraron entradas")
    else: 
        print(f"Sobraron {sobrantes} entradas")

disp = input("Ingrese la cantidad de entradas disponibles a la venta: ")
precio = input("Ingrese el precio de las entradas: ")
ingreso(disp)
totales(precio, disp)