print("Bem vindo ao app de energia mecanica!")
#possiveis exercicios
print("1 - Massa")
print("2 - Altura")
print("3 - Velocidade")
opt = float(input("Digite qual tipo de conta deseja: "))
#descobrir a massa
if (opt == 1):
    J = float(input("Digite a quantidade de Jaws: "))
    G = float(input("Digite a gravidade: "))
    H = float(input("Digite a altura: "))
    M1 = G * H
    Mf = J/M1
    print("A massa é igual a ", Mf)
#descobrir a altura
elif (opt == 2):
    J = float(input("Digite a quantidade de Jaws: "))
    G = float(input("Digite a gravidade: "))
    M = float(input("Digite a massa: "))
    H1 = G*M
    Hf = J/H1
    print("A altura é igual a ", Hf)
#descobrir a velocidade
elif (opt == 3):
    J = float(input("Digite a quantidade de Jaws: "))
    M = float(input("Digite a massa: "))
    V1 = J*2
    V2 = J/M
    Vf = J^0.5
    print("A velocidade é igual a ", Vf)
    
