total_en_caja = 2000
import os
import time as t

def verificar_vacio(dato):
	while dato == " " or dato == "":
		print("Error, valor vacio!")
		dato = input("Ingrese nuevamente: \n>>> ")
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
		valor = input("Ingrese nuevamente: \n>>> ")
	valor = int(valor)
	return valor

def verif_vuelto(Total, Abono):
	while Total > Abono:
		print("Error el abono debe ser mayor al total.")
		Abono = input("Ingrese nuevamente el abono: \n>>> ")
		Abono = verificar_vacio(Abono)
		Abono = convertir(Abono)
	return Abono
 
def carga():
	os.system("cls")
	print("Cargando.")
	t.sleep(1)
	os.system("cls")
	print("Cargando..")
	t.sleep(1)
	os.system("cls")
	print("Cargando...")
	t.sleep(1)