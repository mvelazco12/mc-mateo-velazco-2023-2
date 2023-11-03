from IPython.utils import syspathcontext
import numpy as np
import matplotlib.pyplot as plt
import statistics

x = [0,1,2,3,4,5,6]
y = [3.2, 0.4, -1, -1.4, 1.1, 0.6, 3.1]

x2 = [0,1,2,3,4,5,6]
for i in range(0,len(x2)):
	x2[i]=x2[i]*x2[i]

x3 = [0,1,2,3,4,5,6]
for i in range(0,len(x3)):
	x3[i]=x3[i]*x3[i]*x3[i]

x4 = [0,1,2,3,4,5,6]
for i in range(0,len(x4)):
	x4[i]=x4[i]*x4[i]*x4[i]*x4[i]

xy= [0,1,2,3,4,5,6]
for i in range(0,len(xy)):
	xy[i]=x[i]*y[i]

x2y = [0,1,2,3,4,5,6]
for i in range(0,len(x2)):
	x2y[i]=(x2y[i]*x2y[i])*(y[i])

#obtener a0, a1, a0 GAUSS JORDAN
n = len(x)
xi = sum(x)
x2i = sum(x2)
x3i = sum(x3)
x4i = sum(x4)
xiyi = sum(xy)
yi = sum(y)
xi2yi = sum(x2y)
yprom = statistics.mean(y)
#matrices A y B
A = np.array([[n,xi,x2i],
              [xi,x2i,x3i],
              [x2i,x3i,x4i]])

B = np.array([[yi],
              [xiyi],
              [xi2yi]])

#PROCEDIMIENTO
#evitar truncamiento en operaciones
A = np.array(A,dtype=float) 

#hacer matriz aumentada
AB = np.concatenate((A,B),axis=1)
AB0 = np.copy(AB)

#pivoteo parcial por filas
tamaño = np.shape(AB)
n = tamaño[0]
m = tamaño[1]

# Para cada fila en AB
for i in range(0,n-1,1):
    # columna desde diagonal i en adelante
    columna = abs(AB[i:,i])
    max = np.argmax(columna)
    
    # dondemax no está en diagonal
    if (max !=0):
        # intercambia filas
        temporal = np.copy(AB[i,:])
        AB[i,:] = AB[max+i,:]
        AB[max+i,:] = temporal
        
AB1 = np.copy(AB)

#eliminacion hacia adelante
for i in range(0,n-1,1):
    pivote = AB[i,i]
    adelante = i + 1
    for k in range(adelante,n,1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
AB2 = np.copy(AB)

#elimina hacia atras
ultimafila = n-1
ultimacolumna = m-1
for i in range(ultimafila,0-1,-1):
    pivote = AB[i,i]
    atras = i-1 
    for k in range(atras,0-1,-1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
    # diagonal a unos
    AB[i,:] = AB[i,:]/AB[i,i]
X = np.copy(AB[:,ultimacolumna])
X = np.transpose([X])

# SALIDA
a0 = X[0]
a1 = X[1]
a2 = X[2]
print("a0 = ", a0)
print("a1 = ", a1)
print("a2 = ", a2)

yyprom2 = [4.2,1.4,0,-0.4,-0.1,1.6,4.1]
for i in range(0,len(yyprom2)):
	yyprom2[i]=(y[i]-yprom)**2

ya = [4.2,1.4,0,-0.4,-0.1,1.6,4.1]
for i in range(0,len(ya)):
	ya[i]=((y[i])-(a0)-(a1*x[i])-(a2*x2[i]))**2

sy = np.sqrt(sum(yyprom2)/(len(yyprom2)-1))
syx = np.sqrt(sum(ya)/((len(ya))-(2+1)))
r = (np.sqrt((sum(yyprom2)-sum(ya))/sum(yyprom2)))*100

print("Desviacion Estandar (Sy) = [",sy,"]")
print("Error Estandar (Sy/x) = ",syx)
print("Coeficiente de Correlación (r) = ",r, "%")
