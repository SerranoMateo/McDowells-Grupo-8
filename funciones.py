total_en_caja = 2000

def verificar_vacio(dato):
	while dato == " " or dato == "":
		print("Error, valor vacio!")
		dato = input("Ingrese nuevamente: ")
	return dato

def verificar_nombre(dato):
    while dato.isalpha() == False:
        print("Error, Nombre invalido")
        dato = input("Ingrese su nombre nuevamente \n >>> ")
    return dato

def verificar_numero_str(dato):
    while dato.isdigit() == False:
        print("Error, opcion incorrecta")
        dato = input("Ingrese nuevamente la opcion  \n >>> ")
    return dato

def convertir(valor):
	while valor.isdecimal() == False:
		print("Error, solo numeros enteros")
		valor = input("Ingrese nuevamente: ")
	valor = int(valor)
	return valor
 