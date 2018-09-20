import mqttDriver
import time

def cocinaCallback(client, userdata, message):
	print("hola como andas, me llego esto del baño: ", str(message.payload.decode("utf-8")))

jorge = mqttDriver.mqttClient("localhost")
jorge.subscribe("casa")
jorge.subscribe("casa/cocina")

#jorge.publish("casa", "llegue a on_message")

jorge.addCallback("casa/cocina", cocinaCallback)

while True:
	pass
