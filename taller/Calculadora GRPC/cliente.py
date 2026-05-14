import calculadora_pb2
import calculadora_pb2_grpc
import grpc

conexion = grpc.insecure_channel(
    'localhost:5000'
)

stub = calculadora_pb2_grpc.CalculadoraStub(
    conexion
)

while True:
        print("\n--- CALCULADORA GRPC ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        op = input("Seleccione opción: ")

        if op == "5":
            break

        a = int(input("Ingrese número A: "))
        b = int(input("Ingrese número B: "))

        request = calculadora_pb2.Operacion(a=a, b=b)

        if op == "1":
            res = stub.Sumar(request)
        elif op == "2":
            res = stub.Restar(request)
        elif op == "3":
            res = stub.Multiplicar(request)
        elif op == "4":
            res = stub.Dividir(request)
        else:
            print("Opción inválida")
            continue

        print("Resultado:", res.r)
