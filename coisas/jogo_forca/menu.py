import forca

print("Menu de Jogos")
print("1 = Forca")

escolha = int(input("Qual jogo você quer jogar? Digite o número correspondente: "))

if escolha == 1:
    forca.jogar()  
else:
    print("Escolha inválida. Por favor, digite 1 para jogar Forca.")
