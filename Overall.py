print("1.Ataque")
print("2.Meio-campo")
print("3.Defensor")
print("4.Goleiro")
p = int(input("Escolha uma posicao: "))
fis = int(input("Digite seu fisico: "))
pas = int(input("Digite seu passe: "))
chu = int(input("Digite seu chute: "))
con = int(input("Digite sua conducao: "))
vel = int(input("Digite sua velocidade: "))
over = (fis + pas + chu + con + vel / 5)  
if p == 1:
    print("Você é um atacante com",over,"de pontuacao geral")
elif p == 2:
    print("Você é um meio-campista com",over,"de pontuacao geral")
elif p == 3:
    print("Você é um defensor com",over,"de pontuacao geral")
elif p == 4:
    print("Você é um goleiro com",over,"de pontuacao geral")
else:
    print("Pontuacao geral nao identifacada")  