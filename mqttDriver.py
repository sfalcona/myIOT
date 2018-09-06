import paho.mqtt.client as mqtt




def setClient(self,serverIp,serverPort=1883,userName = 'RPi', messageCallback = None):
	'''Instancia de cliento Mosquitto'''
	myClient = mqtt.Client()
	myClient.username_pw_set('RPi')
	myClient.on_message = messageCallback
	myClient.connect(serverIp,serverPort,60)

	return myClient

