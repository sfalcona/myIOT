import paho.mqtt.client as mqtt

# Ejemplo de callback

'''
def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))

mqttc.on_message = on_message

'''

class mqttClient(self):
	'''Servidor de mqtt utilizando la biblioteca paho. No gano mucho, es muy basado en la 
	biblioteca.
	'''
	def setClient(self,serverIp,serverPort=1883,userName = 'RPi', messageCallback = None):
		'''Instancia de cliente Mosquitto
		ServerPort por default es 1883 (standard de mqtt)
		userName y pwd por ahora no tienen importancia
		messageCallback define que accion realizar cuando se recibe un msj en un canal subscripto
		'''
		myClient = mqtt.Client()
		myClient.username_pw_set('RPi')
		myClient.on_message = messageCallback
		myClient.connect(serverIp,serverPort,60)
		return myClient

	def publish(self, topic, payload, qos = 0, retain = False):
		'''Publica un payload en un cierto topic, devuelve 
		MQTT_ERR_SUCCESS si mensaje ok
		MQTT_ERR_NO_CONN si no hay conexion 
		MQTT_ERR_QUEUE_SIZE si el mensaje no entro en queue ni se envio
		'''
		return = mqtt.publish(topic, payload, qos, retain)

	def subscribe(self, topic, qos =0):
		'''Me subscribo a un topico'''
		mqtt.subscribe(topic, qos)

	def unsubscribe(self, topic, qos = 0):
		'''Cancelo subscripcion a un topico'''
		mqtt.unsubscribe(topic, qos)


