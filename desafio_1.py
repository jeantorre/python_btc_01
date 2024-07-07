nome = input('Digite seu nome: ')
salario = int(input('Digite seu salário: '))
bonus = 1.6
novo_salario = salario * bonus
acrescimo = novo_salario - salario
print(f'Neste ano tivemos um bônus de 60%!\nParabéns, {nome}! Você irá receber {novo_salario} neste mês.\nUm acréscimo de {acrescimo}!')