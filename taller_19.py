import operator
import statistics
import math
import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3,4,5,6,7]
y = [0.2,0.5,1.8,3.4,5.7,9.0,13.8]
xy = list(map(operator.mul, x, y))

x2 = [1,2,3,4,5,6,7]
for i in range(0,len(x)):
	x2[i]=x2[i]*x2[i]

promy = statistics.mean(y)
promx = statistics.mean(x)

a1 = ((len(x))*(sum(xy))-(sum(x))*(sum(y)))/((len(x))*(sum(x2))-(sum(x))**2)
a0 = promy - (a1)*promx
print("a1 = ", a1)
print("a0 = ", a0)

#desviación estandar
ypy = [0.2,0.5,1.8,3.4,5.7,9.0,13.8]
for i in range(0,len(x)):
	ypy[i]=(ypy[i]-promy)**2

yax = [0.2,0.5,1.8,3.4,5.7,9.0,13.8]
for i in range(0,len(x)):
	yax[i]=(yax[i]-a0-a1*x[i])**2

st = sum(ypy)
print("Desviación estandar: ", st)

#error estandar
sr = sum(yax)
syx = math.sqrt(sr/(len(yax)-2))
print("error estándar de la estimación: ", syx)

#coeficiente de correlación
r = (math.sqrt((st-sr)/st))*100
print("coeficiente de correlación: ",r,"%")
