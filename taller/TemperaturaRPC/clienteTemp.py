import xmlrpc.client

cliente = xmlrpc.client.ServerProxy("http://localhost:8000")

while True:
    print("\n--- CONVERSOR DE TEMPERATURA ---")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Salir")
    
    opcion = input("Seleccione la opcion: ")
    if opcion == "3":
        break
    
    a = float(input("Ingrese la temperatura: "))
    
    if opcion == "1":
        r = cliente.CelsiusAFahrenheit(a)
        print(f"La temperatura {a} en Fahrenheit es {r}")
    elif opcion == "2":
        r = cliente.FahrenheitACelsius(a)
        print(f"La temperatura {a} en Celsius es {r}")
    else:
        print("Opcion invalida")
        continue