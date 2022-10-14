#Practica 3 Exploracion de Datos con Python y R
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./data/avocado.csv')

#Realizar en Python o R lo siguiente.

#1. Obtener Cuantas filas y cuantas columnas tiene el conjunto de datos
table = data.shape
print("\nNumero de filas en el conjunto de datos es: " + str(table[0]))
print("Numero de columnas en el conjunto de datos es: " + str(table[1]))


#2. Mostrar los primeros 100 registros
print("\nMostrar los primeros 100 registros: ")
print(data.head(100))

#3. Mostrar los últimos 20 registros
print("\nMostrar los últimos 20 registros: ")
print(data.tail(20))

#4. Cual es el precio mínimo, máximo y promedio del aguacate en ese conjunto de datos
print("\nCual es el precio mínimo, máximo y promedio del aguacate en ese conjunto de datos:")
print("Precio mínimo: " + str(data['AveragePrice'].min()))
print("Precio máximo: " + str(data['AveragePrice'].max()))
print("Precio promedio: " + str(data['AveragePrice'].mean()))

'''
5.Generar un gráfico de tipo scatter usando  para la x la variable 'year'
y  para y la variable 'AveragePrice' para 3 regiones (las que usted elija),
los 3 sub-conjuntos deben mostrarse en el mismo gráfico.
'''
#Creando los subconjuntos por regiones

#region #1
r_atlanta = data[data['region'] == 'Atlanta']

#region #2
r_boston = data[data['region'] == 'Boston']

#region #3
r_california = data[data['region'] == 'California']

#Creando un subplot para agrupar los graficos
x1 = plt.subplot()

#Crear grafico de tipo dispersion con las variables x = year, y la y = averagePrice
g_Atlanta = r_atlanta.plot(x = 'year', y = 'AveragePrice', kind = 'scatter', color = 'blue', ax = x1)
g_boston = r_boston.plot(x = 'year', y = 'AveragePrice', kind = 'scatter', color = 'red', ax = x1)
g_california = r_california.plot(x = 'year', y = 'AveragePrice', kind = 'scatter', color = 'green', ax = x1)

#mostrando el grafico en la pantalla
plt.show()