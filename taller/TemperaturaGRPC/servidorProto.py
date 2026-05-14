from concurrent import futures
import grpc
import temperatura_pb2
import temperatura_pb2_grpc

# Clase que implementa los métodos del servicio
class ConversorService(temperatura_pb2_grpc.ConversorTemperaturaServicer):

    # Conversión de Celsius a Fahrenheit
    def CelsiusAFahrenheit(self, request, context):
        celsius = request.valor
        fahrenheit = (celsius * 9/5) + 32

        return temperatura_pb2.Resultado(valor=fahrenheit)

    # Conversión de Fahrenheit a Celsius
    def FahrenheitACelsius(self, request, context):
        fahrenheit = request.valor
        celsius = (fahrenheit - 32) * 5/9

        return temperatura_pb2.Resultado(valor=celsius)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    temperatura_pb2_grpc.add_ConversorTemperaturaServicer_to_server(
        ConversorService(), server
    )

    server.add_insecure_port('[::]:50051')
    server.start()

    print("Servidor GRPC iniciado en el puerto 50051")

    server.wait_for_termination()


if __name__ == '__main__':
    serve()