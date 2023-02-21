opcion = 0
sumaProd = 0
cantLeche = 0
cantAzucar = 0
cantChocolate = 0
cantHarina = 0
cantBebida = 0
x = 0
listaProducto = []
listaCantidad = []
listaPrecio = []
while opcion != 4:	  
    print()
    print("\tMenu de Compras")
    print("1) Agregar productos al carro")
    print("2) Ver canasta")
    print("3) Ver total")
    print("4) Salir")
    try:        
        opcion = int(input("Ingrese una opción: "))
    except:
        print()
        print("La opción debe ser numerica.")
        print()
    if opcion == 1:
        while True:
            print()
            print("\tCual producto quieres agregar?")
            print("1) Leche: \t$950")
            print("2) Azucar(kg): \t$900")
            print("3) Chocolate: \t$1500")
            print("4) Harina(kg): \t$900")
            print("5) Bebida(1L): \t$1200")
            print("6) Volver al menu principal")
            try:
                x = int(input())
            except:
                print()
                print("La opción debe ser numerica.")
                print()
            if x == 6:
                print()
                print("Volvendo al menu...")
                break
            if x >= 1 and x <= 5:
                if x == 1:
                    try:
                        cantLeche = int(input("Ingrese cantidad de leche a comprar: "))
                    except:
                        print()
                        print("Debe ingresar solo numeros")
                    if cantLeche > 0:
                        totalLeche = cantLeche * 950
                        listaCantidad.append(cantLeche)
                        listaProducto.append("Leche")
                        listaPrecio.append(totalLeche)
                        print()
                        print("Agregaste", cantLeche,"unidades de leche.")
                    else:
                        print("Cantidad erronea. Volvamos al menu...")
                if x == 2:
                    try:
                        cantAzucar = int(input("Ingrese cantidad de azucar a comprar: "))
                    except:
                        print()
                        print("Debe ingresar solo numeros")
                    if cantAzucar > 0:
                        totalAzucar = cantAzucar * 900
                        listaCantidad.append(cantAzucar)
                        listaProducto.append("Azucar")
                        listaPrecio.append(totalAzucar)
                        print()
                        print("Agregaste", cantAzucar,"kg de azucar.")
                    else:
                        print("Cantidad erronea. Volvamos al menu...")
                if x == 3:
                    try:
                        cantChocolate = int(input("Ingrese cantidad de chocolate a comprar: "))
                    except:
                        print()
                        print("Debe ingresar solo numeros")
                    if cantChocolate > 0:
                        totalChocolate = cantChocolate * 1500
                        listaCantidad.append(cantChocolate)
                        listaProducto.append("Chocolate")
                        listaPrecio.append(totalChocolate)
                        print()
                        print("Agregaste", cantChocolate,"unidades de chocolate.")
                    else:
                        print("Cantidad erronea. Volvamos al menu...")
                if x == 4:
                    try:
                        cantHarina = int(input("Ingrese cantidad harina a comprar: "))
                    except:
                        print()
                        print("Debe ingresar solo numeros")
                    if cantHarina > 0:
                        totalHarina = cantHarina * 900
                        listaCantidad.append(cantHarina)
                        listaProducto.append("Harina")
                        listaPrecio.append(totalHarina)
                        print()
                        print("Agregaste", cantHarina,"kg de harina.")
                    else:
                        print("Cantidad erronea. Volvamos al menu...")           
                if x == 5:
                    try:
                        cantBebida = int(input("Ingrese cantidad bebida a comprar: "))
                    except:
                        print()
                        print("Debe ingresar solo numeros")
                    if cantBebida > 0:
                        totalBebida = cantBebida * 1200
                        listaCantidad.append(cantBebida)
                        listaProducto.append("Bebida")
                        listaPrecio.append(totalBebida)
                        print()
                        print("Agregaste", cantBebida,"litros de bebida.")
                    else:
                        print("Cantidad erronea. Volvamos al menu...")
            else:
                print("Volvamos al menu...")
                print()
    if opcion == 2:
        largoLista = len(listaPrecio)
        if largoLista == 0:
            print()
            print("\tNo hay productos en la canasta.")
        else:
            for i in range(largoLista):
                print()
                print("Producto:", listaProducto[i], "\tCantidad:", listaCantidad[i], "\tPrecio:",listaPrecio[i])
    if opcion == 3:
        largoLista = len(listaPrecio)
        if largoLista == 0:
            print()
            print("\tNo hay productos en la lista.")
        else:
            for i in range(largoLista):
                sumaProd = sumaProd + int(listaPrecio[i])
            print()
            print("El total a pagar es:", sumaProd,"pesos.")
    if opcion == 4:
        print()
        print("Hasta luego :)")