# Pedir ao utilizador a largura da parede
largura = float(input('Qual é a largura da tua parede em metros?: '))

# Pedir ao utilizador a altura da parede
altura = float(input('Qual é a altura da tua parede em metros?: '))

# Calcular a área da parede e a quantidade de tinta necessária (1 litro para cada 2 m²)
print('A área da parede é {}m2 e são precisos {} litros de tinta para a pintar.'.format(largura * altura, (largura * altura) / 2))

