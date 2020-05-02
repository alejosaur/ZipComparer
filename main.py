import algorythms
import differences_printer as pr
import sys

WAR_ANTERIOR = sys.argv[1]
WAR_NUEVO = sys.argv[2]

try:
	TRESSHOLD = int(sys.argv[3])
except (ValueError, IndexError):
	pr.cls()
	input("No se ingresó un parámetro correcto para el tresshold, se usará 3 por defecto. \nPresione enter para continuar...")
	TRESSHOLD = 3

pr.cls()

print(pr.print_different_files.__doc__)

while(True):
	print(r"""
╔════════════════════════════════════════════════════════════════════════════════════════════╗
║                             COMPARADOR DE ARCHIVOS COMPRIMIDOS                             ║
╠════════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                            ║
║                           1. Comparación por tamaño de archivos                             ║
║                           2. Comparación por contenido de archivos                          ║
║                           3. Salir                                                         ║
║                                                                                            ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝

Seleccione una opción (1,2,3): """, end='')
	try:
		option = int(input())
	except ValueError:
		option = 0
	pr.cls()
	if(option == 1):
		algorythms.size_compare(WAR_ANTERIOR, WAR_NUEVO, TRESSHOLD)	
	elif(option == 2):
		algorythms.data_compare(WAR_ANTERIOR, WAR_NUEVO, TRESSHOLD)
	elif(option == 3):
		exit()
	else:
		print("Opción inválida, intente nuevamente")
	input("\n\033[1mPresione enter para continuar...\033[0m ")
	pr.cls()
