import numpy as np

# Parámetros de la distribución exponencial
lambd = 1  # Parámetro de tasa lambda

# Tamaño de la muestra
n = 100

# Generar muestra de datos a partir de una distribución exponencial
data = np.random.exponential(scale=1/lambd, size=n)

# Imprimir la muestra generada
print(data)
