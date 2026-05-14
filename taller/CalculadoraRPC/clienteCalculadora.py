import xmlrpc.client

cliente = xmlrpc.client.ServerProxy("http://localhost:8000")

while True:
    print("\n--- CALCULADORA RPC ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Seleccione la opcion: ")
    if opcion == "5":
        break
    
    a = int(input("Ingrese número A: "))
    b = int(input("Ingrese número B: "))
    
    if opcion == "1":
        r = cliente.sumar(a,b)
        print("Resultado = ",r)
    elif opcion == "2":
        r = cliente.restar(a,b)
        print("Resultado = ",r)
    elif opcion == "3":
        r = cliente.multiplicar(a,b)
        print("Resultado = ",r)
    elif opcion == "4":
        r = cliente.dividir(a,b)
        print("Resultado = ",r)
    else:
        print("Opcion invalida")
        continue




