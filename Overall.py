while True: 
    print("**MENU**")
    físico = int(input("Digite seu fisico: "))
    passe = int(input("Digite seu passe: "))
    chute = int(input("Digite seu chute: "))
    conducao = int(input("Digite sua condução: "))
    velelocidade = int(input("Digite sua velocidade: "))

    print("---------------------------")
    print("Escolha sua posição: ")

    print("1.ST")
    print("2.CM")
    print("3.CB")
    print("4.GK")
    print("5.Sair")

    p = int(input("Selecione uma opção: "))

    #variaveis e posições
    st = ( )
    cm = ( )
    cb = ( ) 
    gk = ( ) 
    # Preciso saber como posso passar de forma certa para media poderada
    # Mas até final do dia posso tentar aplicar no codigo 
    
     pod = passe + chute + conducao + velocidade + fisico / 5 
     div = pod / 99
     over = 99

    if p == 1:
        print("Você é um atacante com", div, "de pontuação geral")
    elif p == 2:
        print("Você é um meio-campista com", div, "de pontuação geral")
    elif p == 3:
        print("Você é um defensor com", div, "de pontuação geral")
    elif p == 4:
        print("Você é um goleiro com", div, "de pontuação geral")
    elif p == 5:
        print("Saindo")
        break
else:
    print("Posição inválida")

