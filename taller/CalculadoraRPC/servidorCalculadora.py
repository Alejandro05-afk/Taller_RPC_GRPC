from xmlrpc.server import SimpleXMLRPCServer

def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    return a/b

servidor = SimpleXMLRPCServer(("localhost",8000))

servidor.register_function(sumar, "sumar")
servidor.register_function(restar, "restar")
servidor.register_function(multiplicar, "multiplicar")
servidor.register_function(dividir, "dividir")

servidor.serve_forever()