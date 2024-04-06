from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler
#funcion sumar
def suma(n,m):
    return n+m
#funcion resta
def resta(n,m):
    return n-m
#funcion de multiplicacion 
def multiplicacion(n,m):
    return n*m
#funcion de Division 
def division(n,m):
    try: 
        return n/m
    except ZeroDivisionError:
        print("Error: Division con Cero")
        return None  
    

# creacion de la ruta del servidor
dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)
# Registrar el Servicio
dispatcher.register_function(
    "Suma",
    suma,
    returns={"suma": int},
    args={"n": int , "m": int},
)
dispatcher.register_function(
    "Resta",
    resta,
    returns={"resta": int},
    args={"n": int , "m": int},
)
dispatcher.register_function(
    "Multiplicacion",
    multiplicacion,
    returns={"multiplicacion": int},
    args={"n": int , "m": int},
)
dispatcher.register_function(
    "Division",
    division,
    returns={"division": float},
    args={"n": float , "m": float},
)

# Iniciamos el servidor HTTP
server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()