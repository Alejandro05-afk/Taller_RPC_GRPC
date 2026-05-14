import grpc
import temperatura_pb2
import temperatura_pb2_grpc

def run():

    # Conexión al servidor
    channel = grpc.insecure_channel('localhost:50051')

    stub = temperatura_pb2_grpc.ConversorTemperaturaStub(channel)

    print("=== CONVERSOR DE TEMPERATURA ===")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")

    opcion = input("Seleccione una opción: ")

    temperatura = float(input("Ingrese la temperatura: "))

    if opcion == "1":

        respuesta = stub.CelsiusAFahrenheit(
            temperatura_pb2.Temperatura(valor=temperatura)
        )

        print(f"\nResultado: {respuesta.valor:.2f} °F")

    elif opcion == "2":

        respuesta = stub.FahrenheitACelsius(
            temperatura_pb2.Temperatura(valor=temperatura)
        )

        print(f"\nResultado: {respuesta.valor:.2f} °C")

    else:
        print("Opción inválida")


if __name__ == '__main__':
    run()