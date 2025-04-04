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

#Meio-campista
p_short_passing_cm = 0.15
p_long_passing_cm = 0.13
p_vision = 0.12
p_ball_control_cm = 0.10
p_drbbling_cm = 0.9
p_reaction_cm = 0.8
p_interceptions_cm = 0.8
p_attack_positiong_cm = 0.8
p_standing_tackle_cm = 0.6
p_stamina = 0.6
p_long_shots_cm = 0.5
#Zagueiro
p_standing_tackle = 0.17
p_denfesive_awareness = 0.14
p_interceptions = 0.13
p_sliding_tackle = 0.1
p_heading_zag = 0.1
p_streagth_zag = 0.1
p_aggression = 0.07
p_short_passing_zag = 0.05
p_reaction_zag = 0.05
p_ball_control_zag = 0.04
p_jumping = 0.04
#Atacante
p_finishing = 0.2
p_attack_positiong = 0.12
p_hending = 0.1
p_shot_power = 0.1
p_reaction = 0.1
p_dribbling = 0.08
p_ball_control = 0.08
p_volley = 0.05
p_long_shots = 0.05
p_acceleration = 0.05
p_sprint_speed = 0.04
p_streagth = 0.03
#Goleiro
p_diving = 0.21
p_handling = 0.21
p_positioning = 0.21
p_reflexes = 0.21
p_reactions = 0.11
p_kicking = 0.5


overall_meio_campista = p_short_passing_cm*short_passing_cm+p_long_passing_cm*long_passing_cm+p_vision*vision+p_ball_control_cm*ball_control_cm+p_drbbling_cm*drbbling_cm+p_reaction_cm*reaction_cm+p_reaction_cm*reaction_cm+p_interceptions*interceptions+p_attack_positiong_cm*attack_positiong_cm+p_standing_tackle_cm*standing_tackle_cm+p_stamina*stamina+p_long_shots_cm*long_shots_cm
overall_zagueiro = p_standing_tackle * standing_tackle + p_denfesive_awareness*denfesive_awareness+p_interceptions*interceptions+p_sliding_tackle*sliding_tackle+p_heading_zag*heading_zag+p_streagth_zag*streagth_zag+p_aggression*aggression+p_short_passing_zag*short_passing+p_reaction_zag*reaction_zag+p_ball_control_zag*ball_control_zag+p_jumping*jumping
overall_atacante = p_finishing*finishing + p_attack_positiong*attack_positioning + p_hending*heading + p_shot_power * shot_power + p_reaction * reaction + p_dribbling * dribbling + p_ball_control * ball_control + p_volley * volley + p_long_shots * long_shots + p_acceleration * acceleration + p_sprint_speed * sprint_speed + p_streagth * streaght
overall_goleiro = p_diving*diving + p_handling*handling + p_positioning*positioning + p_reflexes*reflexes+p_reactions*reactions+p_kicking*kicking

    p = int(input("Selecione uma opção: "))

    over = 99

    if p == 1:
        finishing = float(input("Adicione o finishing: "))
        attack_positioning = float(input("Adicione o attack position: "))
        heading = float(input("Adicione o heading: "))
        shot_power = float(input("Adicione o shot power: "))
        reaction = float(input("Adicione o reaction: "))
        dribbling = float(input("Adicione o dribbling: "))
        ball_control = float(input("Adicone o ball control: "))
        volley = float(input("Adicone o volley: "))
        long_shots = float(input("Adicone o long shot: "))
        acceleration = float(input("Adicone o acceleration: "))
        sprint_speed = float(input("Adicone o sprint speed: "))
        streaght = float(input("Adicone o streaght: "))
            print(overall_atacante)
    elif p == 2:
        short_passing_cm = float(input("Adicione o short passing: "))
        long_passing_cm = float("Adicione o long passing: ")
        vision = float(input("Adicione o vision"))
        ball_control_cm = float(input("Adicione o ball control: "))
        drbbling_cm = float(input("Adicione o dribbling: "))
        reaction_cm = float(input("Adicione o reaction: "))
        interceptions_cm = float(input("Adicione o interceptions: "))
        attack_positiong_cm = float(input("Adicione o attack possitiong: "))
        standing_tackle_cm = float(input("Adicione o standing tackle: "))
        stamina = float(input("Adicione o stamina: "))
        long_shots_cm = float(input("Adicione o long shots: "))
            print(overall_meio_campista)
    elif p == 3:
        standing_tackle = float(input("Adicione o standing tackle: "))
        denfesive_awareness = float(input("Adicione o defensive awareness: "))
        interceptions = float(input("Adicione o interceptions: "))
        sliding_tackle = float(input("Adicione o sliding tackle: "))
        heading_zag = float(input("Adicione o heading: "))
        streagth_zag = float(input("Adicione o streagth: "))
        aggression = float(input("Adicione o aggression: "))
        short_passing = float(input("Adicione o short passing: "))
        reaction_zag = float(input("Adicione o reaction: "))
        ball_control_zag = float(input("Adicione o ball control: "))
        jumping = float(input("Adicione o jumping: "))
            print(overall_zagueiro)    
    elif p == 4:
        diving = float(input("Adicione o diving: "))
        handling = float(input("Adicione o handling: "))
        positioning = float(input("Adicione o positioning: "))
        reflexes = float(input("Adicione o reflexes: "))
        reactions = float(input("Adicione o reactions: "))
        kicking = float(input("Adicione o kicking: "))
            print(overall_goleiro)
    elif p == 5:
        print("Saindo")
        break
else:
    print("Posição inválida")

"""
1. Só ficou faltando colocar a soma de over: https://pt.fifauteam.com/rating-do-jogador-fifa-20-ultimate-team/
"""
