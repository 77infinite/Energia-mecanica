print("Bem vindo ao app de energia mecanica!")
#possiveis exercicios
print("1 - Massa")
print("2 - Altura")
print("3 - Velocidade")
opt = int(input("Digite qual tipo de conta deseja: "))
#descobrir a massa
if (opt == 1):
    J = float("Digite a quantidade de Jaws: ")
    G = float("Digite a gravidade: ")
    H = float("Digite a altura: ")
    M1 = G * H
    Mf = J/M1
    print("A massa é igual a ", Mf)
#descobrir a altura
elif (opt == 2):
    J = float("Digite a quantidade de Jaws: ")
    G = float("Digite a gravidade: ")
    M = float("Digite a massa: ")
    H1 = G*M
    Hf = J/H1
    print("A altura é igual a ", Hf)
#descobrir a velocidade
elif (opt == 3):
    J = float("Digite a quantidade de Jaws: ")
    M = float("Digite a massa: ")
    V1 = J*2
    V2 = J/M
    Vf = J^0.5
    print("A velocidade é igual a ", Vf)
    