print("OPERACIONES CON CONJUNTOS")

# Leer conjuntos
A = input("Ingresa los elementos del conjunto A separados por espacio: ").split()
B = input("Ingesa los elementos del conjunto B separados por espacio: ").split()
U = input(
    "Ingresa los elementos del conjunto Universal separados por espacio: ").split()

while True:
    print("\nMENU")
    print("1. Union")
    print("2. Interseccion")
    print("3. Diferencia A - B")
    print("4. Complemento de A")
    print("5. Diferencia Simetrica")
    print("6. Salir")

    opcion = input("Elige una opcion: ")

    # UNION
    if opcion == "1":
        resultado = []

        for elemento in A:
            resultado.append(elemento)

        for elemento in B:
            if elemento not in resultado:
                resultado.append(elemento)

        print("Union:", resultado)

    # INTERSECCION
    elif opcion == "2":
        resultado = []

        for elemento in A:
            if elemento in B:
                resultado.append(elemento)

        print("Interseccion:", resultado)

    # DIFERENCIA A - B
    elif opcion == "3":
        resultado = []

        for elemento in A:
            if elemento not in B:
                resultado.append(elemento)

        print("Diferencia A - B:", resultado)

    # COMPLEMENTO DE A
    elif opcion == "4":
        resultado = []

        for elemento in U:
            if elemento not in A:
                resultado.append(elemento)

        print("Complemento de A:", resultado)

    # DIFERENCIA SIMETRICA
    elif opcion == "5":
        resultado = []

        for elemento in A:
            if elemento not in B:
                resultado.append(elemento)

        for elemento in B:
            if elemento not in A:
                resultado.append(elemento)

        print("Diferencia Simetrica:", resultado)

    # SALIR
    elif opcion == "6":
        print("Fin del programa")
        break

    else:
        print("Opcion no valida")
