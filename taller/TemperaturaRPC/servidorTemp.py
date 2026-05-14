from xmlrpc.server import SimpleXMLRPCServer

def CelsiusAFahrenheit(a):
    return (a * 9/5) + 32
def FahrenheitACelsius(a):
    return (a - 32) * 5/9

servidor = SimpleXMLRPCServer(("localhost",8000))
servidor.register_function(CelsiusAFahrenheit,"CelsiusAFahrenheit")
servidor.register_function(FahrenheitACelsius,"FahrenheitACelsius")
print("Servidor iniciado...")

servidor.serve_forever()