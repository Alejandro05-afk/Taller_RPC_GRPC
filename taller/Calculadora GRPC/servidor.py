import grpc
from concurrent import futures

import calculadora_pb2
import calculadora_pb2_grpc

class CalculadoraServidor(
    calculadora_pb2_grpc.CalculadoraServicer
):
    def Sumar(self,request,context):
        
        resultado = request.a + request.b
        
        return calculadora_pb2.Resultado(
            r=resultado
        )
        
    def Restar(self,request,context):
        
        resultado = request.a - request.b
        
        return calculadora_pb2.Resultado(
            r=resultado
        )
    
    def Multiplicar(self,request,context):
        
        resultado = request.a * request.b
        
        return calculadora_pb2.Resultado(
            r=resultado
        )
    
    def Dividir(self,request,context):
        
        resultado = request.a // request.b
        
        return calculadora_pb2.Resultado(
            r=resultado
        )
        
servidor = grpc.server(
    futures.ThreadPoolExecutor(max_workers=10)
)

calculadora_pb2_grpc.add_CalculadoraServicer_to_server(
    CalculadoraServidor(), servidor
)

servidor.add_insecure_port('[::]:5000')

servidor.start()
print("Servidor gRPC ejecutandoce..")
servidor.wait_for_termination()