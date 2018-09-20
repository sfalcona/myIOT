import paho.mqtt.client as mqtt

# Ejemplo de callback

''' Callback por default a ejecutar cuando se reciba un mensaje de un topico al que se esta subscripto'''
def on_message(client, userdata, message):
	print("Received message: ", str(message.payload.decode("utf-8")))
	

class mqttClient():
	'''Servidor de mqtt utilizando la biblioteca paho. No gano mucho, es muy basado en la 
	biblioteca.
	'''

	def setClient(self, serverIp, serverPort = 1883, userName = 'RPi'):
		'''Instancia de cliente Mosquitto
		ServerPort por default es 1883 (standard de mqtt)
		userName y pwd por ahora no tienen importancia
		messageCallback define que accion realizar cuando se recibe un msj en un canal subscripto
		'''

		''' Genero mi cliente mqtt de la librería paho'''
		self.myClient = mqtt.Client()
		''' Defino el ID del cliente'''
		self.myClient.username_pw_set('RPi')
		''' Defino el callback por default para cuando me llega un mensaje de un tópico al que este subscripto el cliente'''
		self.myClient.on_message = on_message
		''' Conecto el clienete'''
		self.myClient.connect(serverIp, serverPort, 60)
		''' Incializo el thread que se encarga de los callbacks cuando me llega un mensaje de un tópico al que este subscripto el cliente'''
		self.myClient.loop_start()
		
		
		return self.myClient

	def publish(self, topic, payload, qos = 0, retain = False):
		'''Publica un payload en un cierto topic, devuelve 
		MQTT_ERR_SUCCESS si mensaje ok
		MQTT_ERR_NO_CONN si no hay conexion 
		MQTT_ERR_QUEUE_SIZE si el mensaje no entro en queue ni se envio
		'''
		return self.myClient.publish(topic, payload, qos, retain)

	def subscribe(self, topic, qos = 0):
		''' Subscribe el client a un topico'''
		self.myClient.subscribe(topic, qos)

	def unsubscribe(self, topic, qos = 0):
		''' Cancelo subscripcion a un topico'''
		self.myClient.unsubscribe(topic, qos)

	def addCallback(self, topic, callback):
		''' Agrego el callback a ejecutar cuando se recibe un mensaje de un topico al que se esta suscripto '''
		self.myClient.message_callback_add(topic, callback)

	def removeCallback(self, topic):
		''' Elimina el callback asociado a un determinado topico'''
		self.myClient.message_callback_remove(topic)

	def addDefaultCallback(self, callback):
		''' Agrega un nuevo callback por default'''
		self.myClient.on_message = callback


	def __init__(self, serverIp, serverPort = 1883, userName = 'RPi'):
		self.setClient(serverIp, serverPort, userName)

