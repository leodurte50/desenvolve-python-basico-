import random
import math

# Peça ao usuário o valor de n
n = int(input("Insira o valor de n: "))

# Gere n valores inteiros aleatórios entre 0 e 100
valores = [random.randint(0, 100) for _ in range(n)]

# Calcula a soma dos valores
soma = sum(valores)

# Calcula a raíz quadrada da soma
raiz_quadrada = math.sqrt(soma)

# Exibe o resultado
print(f"A raíz quadrada da soma dos {n} valores é: {raiz_quadrada:.2f}")