# Pedir ao utilizador para inserir o salário
salario = float(input('Qual é o seu salário?'))

# Calcular o salário com aumento de 15%
novo_salario = salario + (salario * 0.15)

# Mostrar o resultado ao utilizador
print('Com um aumento de 15% o seu salário é {}'.format(novo_salario))
