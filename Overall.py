while True:
    print("\n**MENU**")
    print("Escolha sua posição: ")
    print("1.Ataque")
    print("2.Meio-campo")
    print("3.Defensor")
    print("4.Goleiro")
    print("5.Sair")

    #Meio-campista
    p_passe_curto_cm = 0.15
    p_passe_longo_cm = 0.13
    p_visao = 0.12
    p_controle_bola_cm = 0.1
    p_drible_cm = 0.9
    p_reacao_cm = 0.8
    p_interceptacoes_cm = 0.8
    p_posicionamento_ataque_cm = 0.8
    p_tackle_cm = 0.6
    p_resistencia = 0.6
    p_finalizacao_longa_cm = 0.5

    #Zagueiro
    p_tackle = 0.17
    p_consciencia_defensiva = 0.14
    p_interceptacoes = 0.13
    p_tackle_deslizante = 0.1
    p_cabeca_zag = 0.1
    p_forca_zag = 0.1
    p_agressividade = 0.7
    p_passe_curto_zag = 0.5
    p_reacao_zag = 0.5
    p_controle_bola_zag = 0.4
    p_pulo = 0.4

    #Atacante
    p_finalizacao = 0.20
    p_posicionamento = 0.12
    p_cabeca = 0.1
    p_poder_tiro = 0.1
    p_reacao = 0.1
    p_drible = 0.8
    p_controle_bola = 0.8
    p_bicicleta = 0.5
    p_finalizacao_longa = 0.5
    p_aceleracao = 0.5
    p_velocidade = 0.4
    p_forca = 0.3

    # Goleiro
    p_reflexos = 0.21
    p_dominio = 0.21
    p_posicionamento = 0.21
    p_reflexos = 0.21
    p_reacoes = 0.11
    p_chute = 0.5

    p = int(input("Selecione uma opção: "))

    if p == 1:
        #Atacante
        finalizacao = float(input("Adicione o finalização: "))
        posicionamento = float(input("Adicione o posicionamento: "))
        cabeca = float(input("Adicione o cabeça: "))
        poder_tiro = float(input("Adicione o poder tiro: "))
        reacao = float(input("Adicione o reação: "))
        drible = float(input("Adicione o drible: "))
        controle_bola = float(input("Adicione o controle bola: "))
        bicicleta = float(input("Adicione o bicicleta: "))
        finalizacao_longa = float(input("Adicione o finalização longa: "))
        aceleracao = float(input("Adicione o aceleracao: "))
        velocidade = float(input("Adicione o velocidade: "))
        forca = float(input("Adicione o forca: "))
        overall_atacante = p_finalizacao*finalizacao + p_posicionamento*posicionamento + p_cabeca*cabeca + p_poder_tiro * poder_tiro + p_reacao * reacao + p_drible * drible + p_controle_bola * controle_bola + p_bicicleta * bicicleta + p_finalizacao_longa * finalizacao_longa + p_aceleracao * aceleracao + p_velocidade * velocidade + p_forca * forca
        print(overall_atacante)

    elif p == 2:
        # Meio-campista
        passe_curto_cm = float(input("Adicione o passe curto: "))
        passe_longo_cm = float(input("Adicione o passe longo: "))
        visao = float(input("Adicione o visao"))
        controle_bola_cm = float(input("Adicione o controle bola: "))
        drible_cm = float(input("Adicione o drible: "))
        reacao_cm = float(input("Adicione o reacao: "))
        interceptacoes_cm = float(input("Adicione o interceptacoes: "))
        posicionamento_ataque_cm = float(input("Adicione o posicionamento ataque: "))
        tackle_cm = float(input("Adicione o tackle: "))
        resistencia = float(input("Adicione o resistencia: "))
        finalizacao_longa_cm = float(input("Adicione o finalizacao longa: "))
        overall_meio_campista = p_passe_curto_cm*passe_curto_cm+p_passe_longo_cm*passe_longo_cm+p_visao*visao+p_controle_bola_cm*controle_bola_cm+p_drible_cm*drible_cm+p_reacao_cm*reacao_cm+p_reacao_cm*reacao_cm+p_interceptacoes*interceptacoes_cm+p_posicionamento_ataque_cm*posicionamento_ataque_cm+p_tackle_cm*tackle_cm+p_resistencia*resistencia+p_finalizacao_longa_cm*finalizacao_longa_cm
        print(overall_meio_campista)

    elif p == 3:
        #Zagueiro
        tackle = float(input("Adicione o tackle: "))
        consciencia_defensiva = float(input("Adicione o consciencia defensiva: "))
        interceptacoes = float(input("Adicione o interceptacoes: "))
        tackle_deslizante = float(input("Adicione o tackle deslizante: "))
        cabeca_zag = float(input("Adicione o cabeça: "))
        forca_zag = float(input("Adicione o forca: "))
        agressividade = float(input("Adicione o agressividade: "))
        passe_curto = float(input("Adicione o passe curto: "))
        reacao_zag = float(input("Adicione o reacao: "))
        controle_bola_zag = float(input("Adicione o controle bola: "))
        pulo = float(input("Adicione o pulo: "))
        overall_zagueiro = p_tackle * tackle + p_consciencia_defensiva*consciencia_defensiva+p_interceptacoes*interceptacoes+p_tackle_deslizante*tackle_deslizante+p_cabeca_zag*cabeca_zag+p_forca_zag*forca_zag+p_agressividade*agressividade+p_passe_curto_zag*passe_curto+p_reacao_zag*reacao_zag+p_controle_bola_zag*controle_bola_zag+p_pulo*pulo
        print(overall_zagueiro)

    elif p == 4:
        # Goleiro
        reflexos = float(input("Adicione o reflexos: "))
        dominio = float(input("Adicione o dominio: "))
        posicionamento = float(input("Adicione o posicionamento: "))
        reflexos = float(input("Adicione o reflexos: "))
        reacoes = float(input("Adicione o reacoes: "))
        chute = float(input("Adicione o chute: "))
        overall_goleiro = p_reflexos*reflexos + p_dominio*dominio + p_posicionamento*posicionamento + p_reflexos*reflexos+p_reacoes*reacoes+p_chute*chute
        print(overall_goleiro)

    elif p == 5:
        print("Saindo")
        break
    else:
        print("Posição inválida")
