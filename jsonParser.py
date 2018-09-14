import json

# Cambiar room y obj [] por dir {}

class myDiaLogic:
    '''Generador de respuestas para Fulfillments de Dialogflow.'''
    def __init__(self, objs = {}):
        '''Inicializador de clase, recibe como parametros obligatorios las funciones
        para setear y checkear los estados de los objetos, y como parametros opcionales
        una lista de habitaciones y otra de objetos, siendo posible en todo momento
        agregar o quitar elementos de las mismas.
        '''
        self.objs = objs
        self.lastAction, self.lastRoom, self.lastState, self.lastObjetct = '','','',''
        self.action, self.room, self.dia, self.hour, self.object, self.state = '','','','','',''
        self.event = ''

    def addObj(self, room, obj):
        '''Agrego objeto con habitacion'''
        try:
            self.objs[room].append(obj)
        except KeyError:
            self.objs[room] = []
            self.objs[room].append(obj)

    def remObj(self, room, obj):
        '''Elimino objeto'''
        try:
            self.objs[room].remove(obj)
        except ValueError:
            print('No se encuentra el objeto en dicha habitacion')

    def queryParser(self, jsonObj):
        '''Levanto informacion util del json correspondiente al fulfillment.
	Para cada campo me fijo si el query esta vacio o no, y en el caso de estarlo
	le asigno el ultimo valor recibido, con el fin de poder generar dialogos un poco 
	mas dinamicos.
	'''
        try:
            self.action = jsonObj["queryResult"]["parameters"]['Acciones']
            self.event = 'Accion'
        except KeyError:
            self.action = self.lastAction
            self.event = 'Pregunta'
        try:
            self.room = jsonObj["queryResult"]["parameters"]['Rooms']
        except KeyError:
            self.room = self.lastRoom
        try:
            self.time = jsonObj["queryResult"]["parameters"]['time']
        except KeyError:
            self.time = 'Now'
        try:
            self.dia = jsonObj["queryResult"]["parameters"]['date']
        except KeyError:
            self.dia = 'Now'
        try:
            self.object = jsonObj["queryResult"]["parameters"]['Objetos']
        except KeyError:
            self.object = self.lastObject
        try:
            self.state = jsonObj["queryResult"]["parameters"]['Estados']
        except KeyError:
            self.state = self.lastState
        self.lastAction, self.lastRoom, self.lastState, self.lastObject = self.action, self.room, self.state,self.object
        
    def responseCreator(self):
        '''Diseno el contenido a enviar como respuesta en un request POST para continuar el dialogo con la aplicacion.'''
        response = {"fulfillmentText": "Esto es un mensaje nuevo"}
		


# Ejemplo de json recibido





#Esto de acá lo comenté ayer porque parecía que solo era un ejemplo de como está estructurado el json


'''
myData = {
  "responseId": "bef07f55-ef4a-49f1-a519-131a2c941be2",
  "queryResult": {
    "queryText": "El proximo jueves a la tarde apaga la luz de  el baño",
    "parameters": {
      "date": "2018-09-06T18:49:11-03:00",
      "Estados": "",
      "time-period": {
        "endTime": "2018-09-04T16:00:00-03:00",
        "startTime": "2018-09-04T12:00:00-03:00"
      },
      "Acciones": "Apagar",
      "room": "el baño"
    },
    "allRequiredParamsPresent": True,
    "fulfillmentText": "Respuesta casera by Nono de Lanus",
    "fulfillmentMessages": [
      {
        "text": {
          "text": [
            "Respuesta casera by Nono de Lanus"
          ]
        }
      }
    ],
    "intent": {
      "name": "projects/testiot-b5428/agent/intents/31d67a2e-247c-49d0-9d31-0d2913695077",
      "displayName": "Testeo Luces"
    },
    "intentDetectionConfidence": 1,
    "diagnosticInfo": {
      "webhook_latency_ms": 590
    },
    "languageCode": "es"
  },
  "webhookStatus": {
    "message": "Webhook execution successful"
  }
}'''


#print(myData[queryResult.parameters.Acciones])
