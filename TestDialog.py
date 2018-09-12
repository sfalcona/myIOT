#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import http.server
import socketserver
import simplejson
import json
import random
import myFSM
import jsonParser
import mqttDriver


mqttIp = 'ACA PONGO LA IP'

# Todavia no se bien como armar este callback

topic = ''
msg = ''

def messageCallback(client, userdata, message):
    topic = message.topic
    msg = message.payload






mqttClient = mqttDriver.mqttClient(mqttIp, messageCallback)



myLogic = jsonParser.myDiaLogic(checkCallback = callBack3,setCallback = callBack4)
FSM = myFSM.myFSM()

#Creo estados
FSM.addState('Idle')
FSM.addState('EsperoAccion')
FSM.addState('EsperoObjeto')

#Creo eventos para Idle
FSM.addPath('Idle', myFSM.myOptions('Pregunta', callBack1, 'EsperoAccion'))
FSM.addPath('Idle', myFSM.myOptions('Accion', callBack2, 'EsperoObjeto'))

#Creo eventos para EsperoAccion

FSM.addPath('EsperoAccion', myFSM.myOptions('Accion', callBack2, 'EsperoObjeto'))
FSM.addPath('EsperoAccion', myFSM.myOptions('Pregunta', callBack1, 'EsperoAccion'))

#Creo eventos para EsperoObjeto

FSM.addPath('EsperoObjeto', myFSM.myOptions('Accion', callBack2, 'EsperoObjeto'))
FSM.addPath('EsperoObjeto', myFSM.myOptions('Pregunta', callBack1, 'EsperoAccion'))


#Testeo commit desde PC
FSM.printFSM()



def jsonPPrint(filename):
    f = open(filename,'r')
    data = json.loads(f.read())
    print(json.dumps(data,indent=4,sort_keys = True))

class S(http.server.BaseHTTPRequestHandler):
    '''Servidor HTTP'''
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        f = open("GETResponse.html", "r")
        self.wfile.write(f.read().encode())
        # self.wfile.write("<!DOCTYPE html><html><head><title>Page Title</title></head><body><h1>My First Heading</h1><p>My first paragraph.</p></body><html>".encode())

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        print ("in post method")
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        #self.end_headers()
        data = simplejson.loads(self.data_string)
        with open("myFulfillment.json", "w") as outfile:
            simplejson.dump(data, outfile)

        jsonPPrint("myFulfillment.json")
        # print ("{}".format(data))
        f = open("response.json")
        self.wfile.write(f.read().encode())
        return


def run(server_class=http.server.HTTPServer, handler_class=S, port=80):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print ('Server starting at ' + str(server_address[0]) + ':' + str(port))
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv


if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()
