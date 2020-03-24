import algorythms
import sys
from os import system, name

#clear screen
def cls():
	# windows
	if name == 'nt': 
		system('cls') 
    # mac and linux(here, os.name is 'posix') 
	else: 
		system('clear') 

WAR_ANTERIOR = sys.argv[1]
WAR_NUEVO = sys.argv[2]

try:
	TRESSHOLD = int(sys.argv[3])
except ValueError:
	input("No se ingresó un parámetro correcto para el tresshold, se usará 3 por defecto. \nPresione enter para continuar...")
	TRESSHOLD = 3

while(True):
	print(r"""
╔════════════════════════════════════════════════════════════════════════════════════════════╗
║  ¨S¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢í  [S¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢SÍï(,       =S¢¢¢¢¢¢¢¢¢¢¢¢1          ²¢¢¢¢¢¢¢¢¢¢¢¢¢) ║
║  ³MMMMMMMMMMMMMMMMÑ  óMMMMMMMMMMMMMMMMMMÆMÆæ2-    rMMMMMMMMMMMMM®,         ÃMMMMMMMMMMMMMô ║
║   '''''''''''''''''                                ''''''''''''''          ''''''''''''''  ║
║  ¨fçççççççççççççççY  {fççççççççççççççççççççççççr  ^fçççççççççççççç×      '9çççççççççççççç[ ║
║  ¯ÆMMMMMMMMMMMMMMMÑ  üÆMMMMMMMMMMMMMMMMMMMMMMMMÆ² rÆMMMMMMMMMMMMMMð      YÆMMMMMMMMMMMMMMV ║
║   '''''''''''''''''   ''''''''''''''''''''''''''   ''''''''''''''''       '''''''''''''''  ║
║       ,ççççççç'           jçççççç;      ¨ççççççç±      /çççççççççççs    Jçççççççççççr      ║
║       º®®®®®®®'           E®®®®®®S      ,®®®®®®®1      ìÆ®®®®®®®Æ®®®ª  _®®®®Æ®®®®®®®½      ║
║        '''''''            '''''''        '''''''        ''''''''''''    '''''''''''''      ║
║       ,öçöçççö'           jöççççççççççççççççççj        \öçööçöÝççöööç:=çöççççSççöççöc      ║
║       ºÆÆÆÆÆÆÆ'           DÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ©u'        IÆÆÆÆÆÆQEÆÆÆÆÆþÅÆÆÆÆÆØüÆÆÆÆÆÆÙ      ║
║        '                                                                                   ║
║       ³ôôôôôôô'           iôôôôôôôôôôôôôôôôôV~         ªôôôôôôv [ôôôôôôôôôô* 7ôôôôôôj      ║
║       º®®®®®®®'           ñ©©©©©©©©©©©©©©©©©ßÑr        ì®®®®®®À ,©®®®®®®®®®| ö®®®®®®ø      ║
║                                                                                            ║
║       ³ôôôôôôô'           iôôôôôô[      ­ôôôôôôô^      ªôôôôôôt   ÏôôôôôôV'  {ôôôôôôj      ║
║       °©®®®®®®'           Û®®®®®®Ì      ,®®®®®®®n      3®®®®®®È   ì®®®®®®Z   õ®®®®®®a      ║
║                                                                                            ║
║  ­ôôôôôôôôôôôôôôôôz  1ôôôôôôôôôôôôôôôôôôôôôôôôôô× °ôôôôôôôôôôôt    ~ôôôô|    ±ôôôôôôôôôôô} ║
║  ,®®®®®®®®®®®®®®®®W  ô®®®®®®®®®®®®®®®®®®®®®®®®®â' r®®®®®®®®®®®È    'å®®¾¨    ç®®®®®®®®®®®ö ║
║                                                                                            ║
║  ­ZZòòòòòòòòòòZòòòO  ròòZòòZòòZòZòòòòZòòòòòòV_    |òòòòòòòòòòZí      C9      1ZòòòòòòòòòZ1 ║
║  ·¾¾¾¾¾¾¾¾¾¾¾¾¾¾¾¾Ø  ö¾¾¾¾¾¾¾¾¾¾¾¾¾Ñ¾ÑÑ¾Ø§O±¨     >¾¾¾¾¾¾¾¾¾¾¾E      ¡l      S¾¾¾¾¾¾¾¾¾¾¾Ý ║
╠════════════════════════════════════════════════════════════════════════════════════════════╣
║                                    COMPARADOR DE WARS                                      ║
╠════════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                            ║
║                           1. Comparador por tamaño de archivos                             ║
║                           2. Comparador por contenido de archivos                          ║
║                           3. Salir                                                         ║
║                                                                                            ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝

Seleccione una opción (1,2,3): """, end='')
	option = int(input())
	cls()
	if(option == 1):
		algorythms.sizeCompare(WAR_ANTERIOR, WAR_NUEVO, TRESSHOLD)	
	elif(option == 2):
		algorythms.dataCompare(WAR_ANTERIOR, WAR_NUEVO, TRESSHOLD)
	elif(option == 3):
		exit()
	else:
		print("Opción inválida, intente nuevamente")
	input("\n\033[1mPresione enter para continuar...\033[0m ")
	cls()