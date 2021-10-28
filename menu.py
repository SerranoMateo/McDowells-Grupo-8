import time as t # sleep
from openpyxl import Workbook
import os

import stdio


def simular_carga(mensaje, comando_borrar):
	os.system(comando_borrar)
	print(mensaje + ".")
	t.sleep(1)
	os.system(comando_borrar)
	print(mensaje + "..")
	t.sleep(1)
	os.system(comando_borrar)
	print(mensaje + "...")
	t.sleep(1)
	os.system(comando_borrar)


def imprimir(comando_borrar):
	os.system(comando_borrar)

	print("""McDowell's\nRecuerda que siempre hay que recibir al cliente con una sonrisa :)\n
	1 - Ingreso de nuevo pedido
	2 - Cambio de turno
	3 - Apagar sistema\n\n""")


def ingresar_nuevo_pedido(ws, monto_turno, comando_borrar):
	os.system(comando_borrar)
	simular_carga("Cargando", comando_borrar)

	nombre_cliente = stdio.verificar_str("Ingrese el nombre del cliente: ")
	cant_s = stdio.verificar_int("Ingrese cantidad Combo S: ")
	cant_d = stdio.verificar_int("Ingrese cantidad Combo D: ")
	cant_t = stdio.verificar_int("Ingrese cantidad Combo T: ")
	cant_f = stdio.verificar_int("Ingrese cantidad Flurby: ")

	total = cant_s*650 + cant_d*700 + cant_t*800 + cant_f*250
	ws.append([nombre_cliente, t.asctime(), str(cant_s), str(cant_d), str(cant_t), str(cant_f), str(total)])

	print("\nTotal $" + str(total))
	abono = stdio.verificar_int("Abona con $ ")
	print("vuelto $ " + str(abono - total) + "\n\nVolviendo al menu principal...")

	t.sleep(3)

	return total


def realizar_cambio_de_turno(f_turnos, comando_borrar):
	os.system(comando_borrar)
	simular_carga("Cargando", comando_borrar)

	print("Bienvenido a McDowell's\n")
	nombre_encargadx = stdio.verificar_str("Ingrese su nombre encargad@: ")
	f_turnos.write("IN " + t.asctime() + " Encargad@ " + nombre_encargadx + '\n')
	return nombre_encargadx


def print_close_file_error():
	print("\n\nERROR: Asegurese de cerrar el archivo \"Compras confirmadas.xlsx\" antes de cerrar el programa, sino los datos no se podrán actualizar.\n")
	print("1) Cerrar el archivo y volver a intentar.")
	print("2) Salir sin guardar.\n")


def guardar_compras_confirmadas(wb):
	try:
		wb.save("Pedidos.xlsx")
	except PermissionError:
		opcion = "0"
		while opcion != "2":
			try:
				wb.save("Pedidos.xlsx")
				break;
			except PermissionError:
				print_close_file_error()
				opcion = stdio.verificar_str()


def final(comando_borrar):
	os.system(comando_borrar)
	print("Gracias por usar el programa! :D")
	t.sleep(1)
