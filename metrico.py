def menu():
    print("Escolha a categoria para conversão de unidades:")
    print("1 - Comprimento")
    print("2 - Superfície")
    print("3 - Volume")
    print("4 - Capacidade")
    print("5 - Massa")
    print("0 - Sair")

def comprimento():
    print("\nOpções de conversão de comprimento:")
    print("1 - Metro (m) para Centímetro (cm)")
    print("2 - Centímetro (cm) para Metro (m)")
    print("3 - Quilômetro (km) para Metro (m)")
    print("4 - Metro (m) para Quilômetro (km)")

    escolha = input("Escolha a opção desejada: ")
    valor = float(input("Digite o valor a ser convertido: "))

    if escolha == '1':
        resultado = valor * 100
        print(f"{valor} metros equivalem a {resultado} centímetros.")
    elif escolha == '2':
        resultado = valor / 100
        print(f"{valor} centímetros equivalem a {resultado} metros.")
    elif escolha == '3':
        resultado = valor * 1000
        print(f"{valor} quilômetros equivalem a {resultado} metros.")
    elif escolha == '4':
        resultado = valor / 1000
        print(f"{valor} metros equivalem a {resultado} quilômetros.")
    else:
        print("Opção inválida.")

def superficie():
    print("\nOpções de conversão de superfície:")
    print("1 - Metro quadrado (m²) para Centímetro quadrado (cm²)")
    print("2 - Centímetro quadrado (cm²) para Metro quadrado (m²)")
    print("3 - Hectare (ha) para Metro quadrado (m²)")
    print("4 - Metro quadrado (m²) para Hectare (ha)")

    escolha = input("Escolha a opção desejada: ")
    valor = float(input("Digite o valor a ser convertido: "))

    if escolha == '1':
        resultado = valor * 10000
        print(f"{valor} metros quadrados equivalem a {resultado} centímetros quadrados.")
    elif escolha == '2':
        resultado = valor / 10000
        print(f"{valor} centímetros quadrados equivalem a {resultado} metros quadrados.")
    elif escolha == '3':
        resultado = valor * 10000
        print(f"{valor} hectares equivalem a {resultado} metros quadrados.")
    elif escolha == '4':
        resultado = valor / 10000
        print(f"{valor} metros quadrados equivalem a {resultado} hectares.")
    else:
        print("Opção inválida.")

def volume():
    print("\nOpções de conversão de volume:")
    print("1 - Metro cúbico (m³) para Litro (L)")
    print("2 - Litro (L) para Metro cúbico (m³)")
    print("3 - Hectolitro (hL) para Litro (L)")
    print("4 - Litro (L) para Hectolitro (hL)")

    escolha = input("Escolha a opção desejada: ")
    valor = float(input("Digite o valor a ser convertido: "))

    if escolha == '1':
        resultado = valor * 1000
        print(f"{valor} metros cúbicos equivalem a {resultado} litros.")
    elif escolha == '2':
        resultado = valor / 1000
        print(f"{valor} litros equivalem a {resultado} metros cúbicos.")
    elif escolha == '3':
        resultado = valor * 100
        print(f"{valor} hectolitros equivalem a {resultado} litros.")
    elif escolha == '4':
        resultado = valor / 100
        print(f"{valor} litros equivalem a {resultado} hectolitros.")
    else:
        print("Opção inválida.")

def capacidade():
    print("\nOpções de conversão de capacidade:")
    print("1 - Litro (L) para Mililitro (mL)")
    print("2 - Mililitro (mL) para Litro (L)")
    print("3 - Kilolitro (kL) para Litro (L)")
    print("4 - Litro (L) para Kilolitro (kL)")

    escolha = input("Escolha a opção desejada: ")
    valor = float(input("Digite o valor a ser convertido: "))

    if escolha == '1':
        resultado = valor * 1000
        print(f"{valor} litros equivalem a {resultado} mililitros.")
    elif escolha == '2':
        resultado = valor / 1000
        print(f"{valor} mililitros equivalem a {resultado} litros.")
    elif escolha == '3':
        resultado = valor * 1000
        print(f"{valor} kilolitros equivalem a {resultado} litros.")
    elif escolha == '4':
        resultado = valor / 1000
        print(f"{valor} litros equivalem a {resultado} kilolitros.")
    else:
        print("Opção inválida.")

def massa():
    print("\nOpções de conversão de massa:")
    print("1 - Quilograma (kg) para Grama (g)")
    print("2 - Grama (g) para Quilograma (kg)")
    print("3 - Tonelada (t) para Quilograma (kg)")
    print("4 - Quilograma (kg) para Tonelada (t)")

    escolha = input("Escolha a opção desejada: ")
    valor = float(input("Digite o valor a ser convertido: "))

    if escolha == '1':
        resultado = valor * 1000
        print(f"{valor} quilogramas equivalem a {resultado} gramas.")
    elif escolha == '2':
        resultado = valor / 1000
        print(f"{valor} gramas equivalem a {resultado} quilogramas.")
    elif escolha == '3':
        resultado = valor * 1000
        print(f"{valor} toneladas equivalem a {resultado} quilogramas.")
    elif escolha == '4':
        resultado = valor / 1000
        print(f"{valor} quilogramas equivalem a {resultado} toneladas.")
    else:
        print("Opção inválida.")

while True:
    menu()
    escolha = input("\nEscolha a categoria (ou digite 0 para sair): ")

    if escolha == '0':
        print("Saindo do programa...")
        break
    elif escolha == '1':
        comprimento()
    elif escolha == '2':
        superficie()
    elif escolha == '3':
        volume()
    elif escolha == '4':
        capacidade()
    elif escolha == '5':
        massa()
    else:
        print("Escolha inválida. Por favor, selecione uma opção válida.")

