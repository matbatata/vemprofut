while True: 
    print("**MENU**")
    fis = int(input("Digite seu fisico: "))
    pas = int(input("Digite seu passe: "))
    chu = int(input("Digite seu chute: "))
    con = int(input("Digite sua condução: "))
    vel = int(input("Digite sua velocidade: "))

    print("---------------------------")
    print("Escolha sua posição: ")

    print("1.Ataque")
    print("2.Meio-campo")
    print("3.Defensor")
    print("4.Goleiro")
    print("5.Sair")

    p = int(input("Selecione uma opção: "))

    #variaveis e posições
    st = ( )
    cm = ( )
    cb = ( ) 
    gk = ( ) 
    # Preciso saber como posso passar de forma certa para media poderada
    # Mas até final do dia posso tentar aplicar no codigo 
    
    over = 99

    if p == 1:
        print("Você é um atacante com", over, "de pontuação geral")
    elif p == 2:
        print("Você é um meio-campista com", over, "de pontuação geral")
    elif p == 3:
        print("Você é um defensor com", over, "de pontuação geral")
    elif p == 4:
        print("Você é um goleiro com", over, "de pontuação geral")
    elif p == 5:
        print("Saindo")
        break
else:
    print("Posição inválida")

