# Pedir ao utilizador quanto dinheiro tem na carteira
dinheiro = float(input('Quantos euros você tem na carteira? '))

# Definir a cotação do dólar
dolar = 1.17

# Calcular quantos dólares o utilizador pode comprar e mostrar o resultado
print('você pode comprar {} dólares.'.format(dinheiro * dolar))
