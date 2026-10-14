#Programa de cálculo de IMC
print("Programa para cálcular o 'IMC'")
print()
nome = input("Olá! Digite o seu nome: ")
idade = input("Agora digite a suas idade: ")
print()
peso =float(input("Digite o seu peso: "))
altura =float(input("Digite a sua altura: "))

imc = peso/(altura**2)
print("="*60)
print("'RESULTADO'")
print("Idade do paciente:",idade)
print("Peso do paciente:",peso)
print("altura do paciente:",altura)
print(f" IMC:{imc:.2f}")

if imc <= 18.9:
    print("Abaixo do peso")
elif imc <= 24.9:
    print("Peso Normal.")
elif imc <= 34.9:
    print("Obesidade Grau I.")
elif imc
<= 39.9:
    print("Obesidade Grau II.")
else:
    print("Obesidade Grau III(Mórbida.)")


