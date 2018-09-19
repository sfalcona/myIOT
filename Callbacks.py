import mqttDriver
import json

#hola

def idle2EsperandoOtroObjeto(room, obj, accion):
	'''Tengo que generar la acción en el room y obj que tienen como párametro
	publicar en un tópico mediante mqtt 
	Responder'''
	# NOSE COMO RECIBIR LA ACCION, CAPAZ HAY QUE AGREGAR UN PARÁMETRO MÁS
	cliente.pusblish([room, obj],"estado")

	# Tengo que publicar en el room.obj lo que quiero hacer
	# esperar la respuesta de esa publicación
	# ESPERO PARA VER QUE LA CONECCIÓN NO SE HAYA CORTADO, SIEMPRE CON TIMEOUT
	# una vez que recibo el ok
		#envio que ya se pudo concretar la acción
	# de lo contrario
		#Mando error


def idle2EsperandoAccion(room, obj):
	''' Tengo que obtener el estado en el que está el objeto en el room ingresado
	y enviar el estado obtenido'''
	cliente.pusblish([room, obj],"estado")
	#  Una vez que hago un publish del estado, tengo que recibir la respuesta del mismo.
	#esta respuesta la voy a escuchar con un suscribe.
	
	if ultimoMensaje == 'on':
		#Puedo hacer que espere a la respuesta, si no se conectó bien, tiro erro de una
	else
		#fullfilmentText de error. Se podría hacer que intente de nuevo como para que sea más robusto
	#publicar el tópico por mqtt
	#nose como hacer para preguntar el estado
	#ver la respuesta que recibo del mqtt driver
	#genero una respuesta para que se mande al servidor response.json
		# {
		#	"fullfilmentText" : "la" . "obj" . "de " . "room" . "se encuentra " . "estado obtenido"
		# }

def esperandoObjeto2EsperandoAccion(room, obj):
