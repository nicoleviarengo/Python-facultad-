pila = []
primos = []

def carga(c):
    for i in range (c):
        num = input("Ingrese el numero de identificacion: ")
        while num <= 999 and num > 9999: #validar que sea de 4 digitos
            print("Debe ser de 4 digitos")
            num = input(f"Ingrese el numero de identificacion: ")
            pila.append(num)

#Menor numero de la pila
def menor(): 
    menor=0
    c=0
    while len(pila)!=0:
        c += 1
        v = pila.pop
        if v < menor:
            menor = v
    print(f"Menor numero de identificacio: {menor}")

#Armamos la pila con los numeros primos
def primo():
    while len(pila)!=0:
        v = pila.pop
        cont = 0
        for i in range(2, v): # empieza a contar desde el 2 hasta v
            if(v%2!=0):
                cont += 1 # para contar la cantidad de primos
                primos.append(v)
    print(f"Cantidad de primos{cont}")
    while len(primos!=0):
        p = primos.pop
        print(f"Numeros de identificacion primos: {p}")

c=int(input(f"Ingrese la antidad de paquetes: "))
carga(c)
menor()
primo()
