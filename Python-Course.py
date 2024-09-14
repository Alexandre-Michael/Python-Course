#Python Curse


print("AVISO PRÉVIO!!!")
print("PARA ENTENDER O CONTEÚDO VC DEVE ABRIR O CODIGO NUMA IDE PARA VER OS COMENTARIOS\n")

    #Dicas

    # %s"% e +

#%s"% é o mesmo de + porém em alguns casos melhor usar o %s"%
#Como este caso por exemplo:

#nome_pessoa = "Jorge"
#status_assinatura = True
#print("Olá %s a sua assinatura está %s"% (nome_pessoa, status_assinatura))


    #Usando o print

print("-----------------------------------------\n")

print("Hello World\n")

#Um triangulo


print("   /|")
print("  / |")
print(" /  |")
print("/___|\n")

    #Aprendendo a usar variaveis 

print("-----------------------------------------\n")

nome_pessoa = "Jorge"
idade_pessoa = "70"

#Comandos Com variaveis

print("Havia uma pessoa chamada " + nome_pessoa)
print(nome_pessoa +" tinha " + idade_pessoa + " anos")
print("Ele gostava do nome " + nome_pessoa)
print("Mas não gostava de ter " + idade_pessoa + " anos\n")

print("Havia uma pessoa chamada ", nome_pessoa)
print(nome_pessoa," tinha ", idade_pessoa, " anos")
print("Ele gostava do nome ", nome_pessoa)
print("Mas não gostava de ter ", idade_pessoa, " anos\n")

    #True false and not

print("-----------------------------------------\n")

status_assinatura = True
print("Assinatura Netflix: %s"% status_assinatura)

status_assinatura = not True
print("Assinatura Netflix: %s"% status_assinatura)

status_assinatura = False
print("Assinatura Netflix: %s"% status_assinatura)

status_assinatura = not False
print("Assinatura Netflix: %s"% status_assinatura, "\n")

    #Inputs

#número ao contrario

print("-----------------------------------------\n")

print("Invertendo números")

num = int(input("Informe um número de 2 digitos: "))
dezena = num // 10
unidade = num % 10
print(f"Número Invertido: {unidade} {dezena}")

#Média Notas

print("-----Média Notas-----\n")
N1 = int(input("Informe A Primeira Nota: "))
N2 = int(input("Informe A Segunda Nota: "))
N3 = int(input("Informe A terceira Nota: "))
N4 = int(input("Informe A terceira Nota: "))
media = (N1 + N2 + N4)/4
print("A média das notas é: ", media,"\n")



    #IF ELSE E ELIF (SE, SENÃO, SENÃO SE)

#Impar ou Par

print("-----------------------------------------\n")

print("Descubra se o número é Impar ou par")

num = int(input("Informe um número: "))

if (num % 2 == 0):
    print(num, " é PAR")
else:
    print(num, " é IMPAR\n")

#Salário

print("-----------------------------------------\n")

salario = float(input("Digite o salário base do funcionário: "))
tempo = int(input("Digite o tempo de empresa do funcionário (em anos): "))

if tempo > 10:
    aumento = 0.30
else:
    if tempo >= 5:
        aumento = 0.20
    else:
        aumento = 0.10

novo_salario = salario * (1 + aumento)

print("O novo salário do funcionário será: R$%.2f" % novo_salario, "\n")

#represente um dos 7 dias da semana e imprima se esse dia é útil, fim de semana ou inválido.

print("-----------------------------------------\n")

dia = int(input("Digite um número inteiro representando um dia da semana (1 a 7): "))

# Verificação do dia
if dia == 1:  # Domingo
    print("Fim de semana\n")
else:
    if dia == 7:  # Sábado
        print("Fim de semana\n")
    else:
        if 2 <= dia <= 6:  # Segunda a Sexta
            print("Dia útil\n")
        else:
            print("Dia inválido\n")

print("-----------------------------------------\n")

#Faça um codigo que gere 10 números (até 20) e informe o percentual de numeros multiplos de 5 
# e percental de numeros impares e os divisores do maior numero

