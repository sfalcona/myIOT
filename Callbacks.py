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
	cliente.pusblish(room + "/" + obj,"estado")
	#  Una vez que hago un publish del estado, tengo que recibir la respuesta del mismo.
	#esta respuesta la voy a escuchar con un suscribe.
	
	#Espero la respuesta, esto puede ser un futuro callback
	if cliente.suscribe(room + "/" + obj) == MQTT_ERR_SUCCESS:
		while not esperandoRespuesta: #esperandoRespuesta tiene que modificarse cuando la ESP32 genera la respuesta con el estado del tópico que se publicó
			if estado: #Tiene que guardar la respuesta en esta variable.
				data = {"fullfilmentText": "Sí"}
			else
				data = {"fullfilmentText": "No"}
    		#Para salir de este while, tengo que poner un timeout
	else #fullfilmentText de error. Se podría hacer que intente de nuevo como para que sea más robusto
		data = {"fullfilmentText" : "Ocurrió un error en la conección con Mi Casa De Lejos"}

	#Guardo la respuesta en un archivo
	with open("response.json", "w") as outfile:
    	simplejson.dump(data, outfile)

def esperandoObjeto2EsperandoAccion(room, obj):
