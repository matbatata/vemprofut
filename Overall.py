print("1.Ataque")
print("2.Meio-campo")
print("3.Defensor")
print("4.Goleiro")
print("5.Sair")
p = int(input("Escolha uma opção: "))
if p == 5:
    print("Saindo... até logo!")
else:
    fis = int(input("Digite seu fisico: "))
    pas = int(input("Digite seu passe: "))
    chu = int(input("Digite seu chute: "))
    con = int(input("Digite sua condução: "))
    vel = int(input("Digite sua velocidade: "))
    over = (fis + pas + chu + con + vel) / 5  
    if p == 1:
        print("Você é um atacante com", over, "de pontuação geral")
    elif p == 2:
        print("Você é um meio-campista com", over, "de pontuação geral")
    elif p == 3:
        print("Você é um defensor com", over, "de pontuação geral")
    elif p == 4:
        print("Você é um goleiro com", over, "de pontuação geral")
    else:
        print("Posição inválida")
# Adicionei a saida no codigo ( pedi uma sugestão pro chat e falou para colocar um else
# nas variaveis) 
