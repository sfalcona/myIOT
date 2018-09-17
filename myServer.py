#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import http.server
import socketserver
import simplejson
import json
import random
import myFSM
import diaLogic
import mqttDriver
import os


# mqttIp = 'ACA PONGO LA IP'

# # Callback para mensajes de mqtt, todavia no se bien como armar este callback jaja xd
# topic = ''
# msg = ''


# def messageCallback(client, userdata, message):
#     userdata.topic = message.topic
#     userdata.msg = message.payload
#     return userdata

# Callbacks para la FSM


# def idle2EspObj():


# def idle2EspAcc():


# def espAcc2EspAcc():


# def espAcc2EspObj():


# def espObj2EspObj():


# def espObj2EspAcc():



#     # Una vez definidos los callbacks y el IP creo el cliente
# mqttClient = mqttDriver.mqttClient(mqttIp, messageCallback)

# # Una vez definidos los callbacks genero la FSM
# myLogic = jsonParser.myDiaLogic(
#     checkCallback=checkCallback, setCallback=setCallback)
# FSM = myFSM.myFSM()

# # Creo estados
# FSM.addState('Idle')
# FSM.addState('EsperoAccion')
# FSM.addState('EsperoObjeto')

# # Creo eventos para Idle
# FSM.addPath('Idle', myFSM.myOptions('Pregunta', callBack1, 'EsperoAccion'))
# FSM.addPath('Idle', myFSM.myOptions('Accion', callBack2, 'EsperoObjeto'))

# # Creo eventos para EsperoAccion

# FSM.addPath('EsperoAccion', myFSM.myOptions(
#     'Accion', callBack2, 'EsperoObjeto'))
# FSM.addPath('EsperoAccion', myFSM.myOptions(
#     'Pregunta', callBack1, 'EsperoAccion'))

# # Creo eventos para EsperoObjeto

# FSM.addPath('EsperoObjeto', myFSM.myOptions(
#     'Accion', callBack2, 'EsperoObjeto'))
# FSM.addPath('EsperoObjeto', myFSM.myOptions(
#     'Pregunta', callBack1, 'EsperoAccion'))


# # Testeo commit desde PC
# FSM.printFSM()


def jsonPPrint(filename):
    f = open(filename, 'r')
    data = json.loads(f.read())
    print(json.dumps(data, indent=4, sort_keys=True))


class S(http.server.BaseHTTPRequestHandler):
    '''Servidor HTTP'''

    def do_GET(self):
        print(self.path)
        if(self.path.endswith('/')):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            print('Me llego vacio, imprimo la pagina')
            f = open("myPag.htm", "r", encoding="utf8")
            self.wfile.write(f.read().encode())
            f.close()
        if(self.path.endswith('.png')):
            f=open(os.path.dirname(os.path.abspath(__file__)) + self.path , 'rb')
            self.send_response(200)
            self.send_header('Content-type', 'image/png')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        if(self.path.endswith('.jpg')):
            f=open(os.path.dirname(os.path.abspath(__file__)) + self.path , 'rb')
            self.send_response(200)
            self.send_header('Content-type', 'image/jpg')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        if(self.path.endswith('.js')):
            f=open(os.path.dirname(os.path.abspath(__file__)) + self.path , 'rb')
            self.send_response(200)
            self.send_header('Content-type', 'text/javascript')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        if(self.path.endswith('.css')):
            f=open(os.path.dirname(os.path.abspath(__file__)) + self.path , 'rb')
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        if(self.path.endswith('.woff')):
            f=open(os.path.dirname(os.path.abspath(__file__)) + self.path , 'rb')
            self.send_response(200)
            self.send_header('Content-type', 'application/x-font-woff')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        if(self.path.endswith('.ico')):
            f=open(os.path.dirname(os.path.abspath(__file__)) + self.path , 'rb')
            self.send_response(200)
            self.send_header('Content-type', 'image/ico')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        # self.send_response(200)
        data = simplejson.loads(self.data_string)
        with open("myFulfillment.json", "w") as outfile:
            simplejson.dump(data, outfile)
        # jsonPPrint("myFulfillment.json")
        f = open("response.json")
        self.wfile.write(f.read().encode())
        return


def run(server_class=http.server.HTTPServer, handler_class=S, server='localhost', port=80):
    server_address = (server, port)
    httpd = server_class(server_address, handler_class)
    print('Server starting at ' + str(server_address[0]) + ':' + str(port))
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

if len(argv) == 3:
    run(server=argv[1], port=int(argv[2]))
    print(argv[1])
else:
    run()
    

