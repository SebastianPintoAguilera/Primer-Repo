print("===================")
print("      Factura      ")
print("===================\n")


Nombre = input("nombre: ")
Rut = str(input(("Rut: ")))
Direccion = print("Direccion: Puente Alto ")
print("Giro: Basar")
print("  ")


cod_1 = ("====Pasta de dientes====")
cod_2 = ("====Maquillaje====")
cod_3 = ("====Apoya fregadero====")
cod_4 = ("====Cuaderno====")
cod_5 = ("====Lapices====")
cod_6 = ("====Jabón====")
cod_7 = ("====Zapatos====")
cod_8 = ("====Papas====")
cod_9 = ("====Botella====")
cod_10 = ("====Pelota====")
cod_11 = ("====Mochilas====")
cod_12 = ("====Plumones====")
cod_13 = ("====Polera====")
cod_14 = ("====Poleron====")
cod_15 = ("====Libros====")
cod_16 = ("====Ropa interior====")
cod_17 = ("====Shampoo====")
cod_18 = ("====Calcetines====")
cod_19 = ("====Colonia====")
cod_20 = ("Doritos")



import random
numero_aleatorio = random.randint(300,750)
Numero_aleatorio = random.randint(300,750)
num_aleatorio = random.randint(300,750)
numero_al = random.randint(300,750)
numero_aleatori = random.randint(300,750)


print("==============")
objeto = input("Primer producto deseado: " )
cantidad = int(input("Cuanta cantidad: "))
precio = print("Que precio es: ", numero_aleatorio)
continuar = input("Precionar X para calcular: ")


if continuar == "X":
    total_1 = cantidad * numero_aleatorio
    print("Precio Total del primer producto es : ",total_1)
    print("==============")
    print(" ")
    print(" ")


print("==============")
objeto = input("Segundo producto deseado: ")
cantidad = int(input("Cuanta cantidad: "))
precio = print("Que precio es: ", Numero_aleatorio)
continuar = input("Precionar X para calcular: ")


if continuar == "X":
    total_2 = cantidad * Numero_aleatorio
    print("Precio Total del segundo producto es : ",total_2)
    print("==============")
    print(" ")
    print(" ")


print("==============")
objeto = input("Tercer producto deseado: ")
cantidad = int(input("Cuanta cantidad: "))
precio = print("Que precio es: ", num_aleatorio )
continuar = input("Precionar X para calcular: ")


if continuar == "X":
    total_3 = cantidad * num_aleatorio
    print("productos: ", objeto)
    print("Precio Total del tercer producto es : ",total_3)
    print("==============")
    print(" ")
    print(" ")

    
print("==============")   
objeto = input("Cuarto producto deseado: ")
cantidad = int(input("Cuanta cantidad: "))
precio = print("Que precio es: ", numero_al)
continuar = input("Precionar X para calcular: ")


if continuar == "X":
    total_4 = cantidad * numero_al
    print("productos: ", objeto)
    print("Precio Total del cuarto producto es : ",total_4)
    print("==============")
    print(" ")
    print(" ")


print("==============")    
objeto = input("Quinto producto deseado: ")
cantidad = int(input("Cuanta cantidad: "))
precio = print("Que precio es: ", numero_aleatori)
continuar = input("Precionar X para calcular: ")


if continuar == "X":
    total_5 = cantidad * numero_aleatori
    print("productos: ", objeto)
    print("Precio Total del quinto producto es : ",total_5)
    print("==============")
    print(" ")
    print(" ")


Valor_Neto = total_1 + total_2 + total_3 + total_4 + total_5
print("==============")
print("Valor Neto", Valor_Neto)
print("==============")
print(" ")
print(" ")


iva = Valor_Neto * .19
print("========")
print("Ivá", iva)
print("=========\n")
print(" ")

valor_bruto = iva + Valor_Neto
print("=========")
print("Valor Bruto", valor_bruto)
print("==========\n")


 


 
