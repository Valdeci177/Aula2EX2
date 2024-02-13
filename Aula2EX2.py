velocidade = int(input("Insira a velocidade do carro:"))
excesso = velocidade - 80
multa = 20.0 * excesso

if velocidade > 80:
    print(f"Você ultrapassou a velocidade permitida. Você receberá uma multa de R${multa:.2f}")

else:
    print("Você não ultrapassou o limite de velocidade")
