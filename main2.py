import time as t
import os
import openpyxl as op
import funciones as fu

f = open("registro.txt","a")
f.close()
 
f = open("registro.txt","r")
data = f.readlines()
f.close()

os.system("cls")
x = True
while x == True:
	print("Bienvenido a McDowell´s 🍔")
	Encargado = input("Ingrese su nombre encargad@ : ")
	Encargado = fu.verificar_vacio(Encargado)
	Encargado = fu.verificar_nombre(Encargado.capitalize())
	f = open("registro.txt", "a")
	f.write("IN " + t.asctime() + " " + "Encargad@ " + str(Encargado.capitalize()) + "\n")
	f.close()

	
	while True:
		os.system("cls")
		print('McDowell´s \nRecuerda que siempre hay que recibir al cliente con una sonrisa 😊')
		print("""
		1 - Ingresar pedido
		2 - Cambio de turno
		3 - Apagar sistema
		""")
		opcion = input(">>> ")
		opcion = fu.verificar_vacio(opcion)
		opcion = fu.verificar_numero_str(opcion)
		if opcion == "1":
			os.system("cls")
			print("Cargando.")
			t.sleep(1)
			os.system("cls")
			print("Cargando..")
			t.sleep(1)
			os.system("cls")
			print("Cargando...")
			t.sleep(1)
			import Pedido
		elif opcion == "2":
			f = open("registro.txt", "a")
			f.write("OUT " + t.asctime() + " " + "Encargad@ " + str(Encargado.capitalize()) + " " + "$" + str(fu.total_en_caja) + "\n")
			f.write("###########################################\n")
			f.close()
			break
		elif opcion == "3":
			print("Gracias por usar el programa")
			f = open("registro.txt", "a")
			f.write("OUT " + t.asctime() + " " + "Encargad@ " + str(Encargado.capitalize()) + " " + "$" + str(fu.total_en_caja) + "\n")
			f.write("###########################################\n")
			f.close()
			t.sleep(1)
			x = False
			break
		else:
			print("Error, esa opcion no existe")
			t.sleep(2)
			os.system("cls")
			break
