import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('datos - Copy.csv') #Insertar csv para calcular

#Definir puntos
x= df.iloc[:,:-1].values
y= df.iloc[:,1].values

#Asignaciones y calculos básicos
n = len(x)

avgx = x.mean()
avgy = y.mean()

sumx = sum(x)
sumy = sum(y)

sxx = sum(x*x)
syy = sum(y*y)

#Calculcar sxy, xdiff, ydiff
mult = []
for i in range(1,n):
    temp = x[i]*y[i]
    mult.append(temp)
sxy = sum(mult)

for i in range(1,n):
    temp = x[i]-avgx
    mult.append(temp)
x_diff = sum(mult)

for i in range(1,n):
    temp = x[i]-avgx
    mult.append(temp)
y_diff = temp

#Calculas las true sxy, sxx, sxy
ssxy = sxy - 1/n * sumx * sumy
ssxx = sxx - ((sumx**2)/n)
ssyy = syy - ((sumy**2)/n)

#Calcular la recta y = b1x + b0
b1 = ssxy/ssxx
b0 = avgy - avgx * b1

#Recta eficiente, no hace falta calcular punto por punto
x_min = x.min()
x_max = x.max()

y1 = b0 + b1 * x_min
y2 = b0 + b1 * x_max



# r2 = 1 - sce/stc




#Grafico
plt.plot(x,y, 'o', label="Datos")
plt.xlabel('Minutos')
plt.ylabel('Unidades')
plt.plot([x_min, x_max],[y1,y2], label='Recta de Minimos Cuadrados Estimada')
plt.grid()
plt.legend()
plt.show()
