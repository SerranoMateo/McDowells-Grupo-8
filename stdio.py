from colorama import Fore, init


def output(string):
	print(string, end = "")


def def_input(string = ""):
	init(convert = True) # <--- Necesario para el colorama
	output(string)
	output("\033[91m")
	string = input()
	output(Fore.WHITE)
	return string


def verificar_opcion(mensaje):
	opcion = def_input(mensaje)
	while opcion != "1" and opcion != "2" and opcion != "3":
		opcion = def_input("\nError, opcion incorrecta.\nIngrese otra opcion:\n>>> ")

	return opcion


def verificar_str(mensaje):
	mensaje = def_input(mensaje) 
	while mensaje == "" or mensaje == " " or mensaje.isalpha() == False:
		if mensaje == "" or mensaje == " ":
			mensaje = def_input("\nError, valor vacio!\nIngrese nuevamente:\n>>> ")
		elif mensaje.isalpha() == False:
			mensaje = def_input("\nError, nombre invalido!\nIngrese nuevamente:\n>>> ")

	return mensaje


def verificar_int(mensaje):
	mensaje = def_input(mensaje)
	while mensaje.isdecimal() != True:
		mensaje = def_input("\nError, lo ingresado no es un numero!\nIngrese nuevamente:\n>>> ")

	return int(mensaje)
