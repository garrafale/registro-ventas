from os import system
system("cls")
reg=open("lista.txt","a")

while input("Presione N si desea guardar un nuevo número de cliente. Para salir, presione otra letra    ").upper()=="N":
	from os import system
	system("cls")
	cliente=int(input("Guardar número de cliente (debe contener 2 cifras): "))
	pantallacliente=("NÚMERO DE CLIENTE: "+str(cliente)+"\n"+"\n")
	print()
	if 10<=cliente<=99:
		reg.write(pantallacliente)
	elif cliente>99 or cliente<10:
		print("\n"+"Usted no ha ingresado un número de cliente que contenga 2 cifras"+"\n")
		continue
	while input("Presione P si el cliente compró productos que aún no se cargaron al sistema. Para volver, presione otra letra    ").upper()=="P":
		print()
		producto=input("Ingrese el nombre del producto vendido a ese cliente: ")
		cantidad=int(input("Ingrese la cantidad vendida de ese producto (hasta 99 productos): "))
		if cantidad<=99:
			pantallacantidad=("Cantidades vendidas de "+producto+": "+str(cantidad)+"\n")
			reg.write(pantallacantidad)
			costo=int(input("Ingrese el valor por unidad de ese producto: "))
			print()
			costototal=costo*cantidad
			pantallacosto=("Costo total: "+str(costototal)+"\n"+"\n")
			reg.write(pantallacosto)
		elif cantidad>99:
			print("\n"+"Usted ha ingresado más de 99 productos"+"\n")
			continue
	from os import system
	system("cls")

from os import system
system("cls")
reg=open("lista.txt","r")
print(reg.read())
