##################################################################################
## Universidad de La Laguna                                                     ##
## Escuela Superior de Ingeniería y Tecnología                                  ##
## Grado en Ingeniería Informática                                              ##
## Seguridad en Sistemas Informáticos                                           ##
## Fecha: 21/02/2017                                                            ##
## Autor: Kevin Estévez Expósito (alu0100821390)                                ##
##                                                                              ##
## Práctica 2: Cifrado de Vigenere                                              ##
## Descripción: Cifrado y descifrado de mensajes mediante el cifrado Vigenere,  ##
##              empleando el abecedario español en mayúscula sin 'CH', 'LL',    ##
##              'Ñ', 'RR' ni espacios, pero con '*', '_', '?' y '¿'.            ##
##                                                                              ##
## Ejecución: py vigenere_mod.py                                                ##
## Ejemplo de mensaje: este mensaje se autodestruira                            ##
## Ejemplo de palabra clave: mision                                             ##
##################################################################################

import sys

abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ*_?¿'
mensaje = str(input("Introduzca el mensaje a cifrar: "))
mensaje = mensaje.replace(' ', '').upper()	# Se guarda el mensaje pasado por parámetros, en mayúsculas y sin espacios #
clave_original = str(input("Introduzca la palabra clave: "))
clave_original = clave_original.replace(' ', '').upper()	# Se guarda la clave pasada por parámetros, en mayúsculas y sin espacios #
clave = ''
cifrado = ''
descifrado = ''

if len(mensaje)>len(clave_original):	# Si la logitud del mensaje es mayor que la de la clave... #
	for i in range(int(len(mensaje)/len(clave_original))):		## Se alarga la clave, duplicándola y		 ##
		clave += clave_original									## concatenándosela a sí misma, hasta que su ##
	clave += clave_original[:len(mensaje)%len(clave_original)]	## longitud sea la misma que la del mensaje  ##

elif len(mensaje)<len(clave_original):	# Si la longitud del mensaje es menor que la de la clave...
	clave = clave_original[:len(mensaje)]	# Se trunca la clave para que tenga la misma longitud que el mensaje #

elif len(mensaje)==len(clave_original):	# Si la longitud del mensaje es igual que la de la clave... #
	clave = clave_original	# Se guarda la clave tal cual se encuentra en 'clave_original' #

else:
	print ('Ha ocurrido un error inesperado. Terminando ejecución...')
	sys.exit(1)


print ('Mensaje original: ' + mensaje)
print ('Palabra clave: ' + clave_original)
print ()


print ('Cifrando...')
for i in range(len(mensaje)):
	x = abecedario.find(mensaje[i])	# Se guarda la posición del caracter del mensaje en el abecedario
	y = abecedario.find(clave[i])	# Se guarda la posición del caracter de la clave en el abecedario
	suma = x+y	# Se calcula la suma de ambas posiciones
	modulo = suma%len(abecedario)	# Se calcula el módulo de la suma respecto a la longitud del abecedario
	cifrado += abecedario[modulo]	# Se concatena el caracter cifrado con 'cifrado'

print ('Mensaje cifrado: ' + cifrado)
print ()
	

print ('Descifrando...')
for i in range(len(cifrado)):
	x = abecedario.find(cifrado[i])	# Se guarda la posición del caracter del mensaje cifrado en el abecedario
	y = abecedario.find(clave[i])	# Se guarda la posición del caracter de la clave en el abecedario
	resta = x-y	# Se calcula la resta de ambas posiciones
	modulo = resta%len(abecedario)	# Se calcula el módulo de la resta respecto a la longitud del abecedario
	descifrado += abecedario[modulo]	# Se concatena el caracter descifrado con 'descifrado'

print ('Mensaje descifrado: ' + descifrado)

sys.exit(0)
