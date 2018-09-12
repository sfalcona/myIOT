class myOptions:
    ''' Clase para representar estados, con campos de 
    EVENTO, ACCION y ESTADO SIGUIENTE '''
    def __init__(self, event, callback, nextState):
        self.event = event
        self.callback = callback
        self.nextState = nextState	

    def __call__(self, event, callback, nextState):
        self.__init__(event, callback, nextState)


class myFSM:
    '''Maquina de estados finitos simple.'''
    def __init__(self):
        '''Inicializo el objeto creando variables a utilizar'''
        self.currState = None
        self.states = {}
    
    def __call__(self):
        '''Asigno constructor a los calls.'''
        self.__init__()
    
    def addState(self,name):
        '''Funcion para agregar estados a la fsm'''
        self.states[name] = []
    
    def addPath(self,name,path):
        '''Funcion para agregar ramales a cada estado, con formato myOptions'''
        self.states[name].append(path)
        
    def setStart(self, state):
        '''Funcion para settear el estado inicial de la FSM'''
        try:
            self.currState = state
        except KeyError:
            raise KeyError ("No hay ningun estado con ese nombre en la FSM.")
        
    def printFSM(self):
        '''Funcion para visualizar de manera mas practica la FSM'''
        for key, value in self.states.items():
            print('Estado: %s' % key)
            for path in value:
                print('\t Evento: %s, Accion: %s,Sig Estado: %s' % (path.event,path.callback.__name__,path.nextState))
    
    def whereAmI(self):
        '''Funcion para debuggear, indica el estado actual y las posibilidades.'''
        print("Estoy en el estado %s y mis posibles caminos son: " % self.currState)
        for i in self.states[self.currState]:
            print("\t %s si me llega %s" % (i.nextState, i.event))
    
    def run(self,event):
        '''Corro la FSM, partiendo de un estado actual y viendo el evento recibido.'''
        invalidEvent = True
        if self.currState == None:
            raise KeyError ("No hay estado inicial setteado.") # No es key error, pero no se que poner
        
        for i in self.states[self.currState]:
            if i.event == event:
                invalidEvent = False
                i.callback()
                self.currState = i.nextState
        if invalidEvent:
            raise KeyError ("Dicho evento no esta asociado al estado actual.") # Same
       


''' Ejemplo 

        
        
def printA():
    print(' ')

def printB():
    print(' ')
    
a = myFSM()

a.addState('Idle')
a.addPaths('Idle', myOptions('Buscar',printA, 'Idle'))
a.addPaths('Idle', myOptions('Activar',printB, 'FULL'))
a.addPaths('Idle', myOptions('Reset',printB, 'Idle'))
a.addState('FULL')
a.addPaths('FULL', myOptions('Reset',printB, 'Idle'))
a.addPaths('FULL', myOptions('Activar',printB, 'FULL'))

a.setStart('Idle')
a.run('Buscar')
a.whereAmI()
a.run('Activar')
a.whereAmI()
a.run('Activar')
a.whereAmI()



a.printFSM()

'''
