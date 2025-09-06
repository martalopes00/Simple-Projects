# Pedir ao utilizador para escrever algo
algo = input('Escreve algo: ')

# Mostrar o tipo primitivo do valor
print('O tipo primitivo deste valor é', type(algo))

# Verificar se contém apenas espaços
print('Só tem espaços?', algo.isspace())

# Verificar se é um número
print('É um número?', algo.isnumeric())

# Verificar se é alfabético
print('É alfabético?', algo.isalpha())

# Verificar se está em maiúsculas
print('Está em maiúsculas?', algo.isupper())

# Verificar se está em minúsculas
print('Está em minúsculas?', algo.islower())

# Verificar se está capitalizado 
print('Está capitalizado?', algo.istitle())
