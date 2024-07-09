nome = input('Digite seu nome: ')
salario = int(input('Digite seu salário: '))
bonus_inicial = float(input('Digite o bônus: '))
bonus_inicial = bonus_inicial * 100
bonus_final = 1 + bonus_inicial
novo_salario = salario * bonus_final
acrescimo = novo_salario - salario
print(f'Neste ano tivemos um bônus de {bonus_inicial}%!\nParabéns, {nome}! Você irá receber {novo_salario} reais neste mês.\nUm acréscimo de {acrescimo} reais!')