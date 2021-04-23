#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================
******FECHA CREACION******
Feb  5 09:58:19 2021

******PROGRAMA******: 
VIDA MEDIA MUÓN

******INSTITUCION******:
Universidad del Valle de Guatemala
Introduccion  a la Fisica de Particulas

*****AUTORES******:
-Christian Ramirez
-Pablo Marroquin
-Julio Monzon
-Paula Valdes

================================================================
"""
#LIBRERIA PARA GRAFICAR
import matplotlib.pyplot as plt
import os
import pathlib

#===============================================================
#DECLARACION DE VARIABLES
"""
temp_particulas=0
num_archivo=0
cant_particulas=[]
psn=[]                                                              # posicion nuevo archivo en lista archivo
"""
t_maxes=[]                                                          # estan guardados los valores de tiempo donde ocurre el pico
tiempos=[]                                                          # tiempos de decaimiento del muon
t12=[]                                                              # tiempos que aparecen abajo de cada 12 datos
archivo = []                                                        #lista de lineas del archivo dat
cargas = []                                                         #lista de cargas medidas
cargas_integradas=[]                                                #lista de cargas integradas calculadas
suma_parcial_cargas = []                                            #variable temporal para sumar cargas
#===============================================================
ruta = pathlib.Path(__file__).parent.absolute()                                #se guarda la ruta actual
for root, dirs, files in os.walk(ruta):                                        # se recorre todo el directorio
    for file in files:                                                         # se guardan archivos en lista
        filename, extension = os.path.splitext(file)
        if extension == '.dat':                                                #se verifica que sean .dat
            with open(file, "r") as file:       #se lee el archivo
                for linea in file:                                             #se recorre el archivo
                   if linea[0]=="#":                                           #se ignoran las línas que inician con numeral
                       if linea[2]=="t":
                           t12.append(float(linea[6:]))
                       else:
                           pass
                   else:
                       archivo.append(linea)                                   #se agrega cada lineal del archivo a la lista   
            """psn.append(len(archivo))"""
            #print("escribi en psn")
#===============================================================
                
for indice in archivo:                                              #se recorre la lista
    try:
        valor_carga = abs(int(indice[:3]) - 50)                         #se toma el valor de la carga en la linea
        cargas.append(valor_carga)                                      #se agrega el valor a la lista de cargas
    except:
        pass
#===============================================================

for indice in range(len(cargas)):                                   #se recorre la lista
    if indice%12 == 0 and indice!=0:                                #se revisa el indice para saber si termina la suma parcial
        try:
            suma_parcial_cargas.append(cargas[indice])                  #se agrega cada carga a la suma parcial
            carga_n = sum(suma_parcial_cargas)                          #se hace la suma parcial y se guarda en carga_n
            cargas_integradas.append(carga_n)                           #se agrega la carga_n a la lista de cargas integradas
            suma_parcial_cargas = []                                    #IMPORTANTE se vacia la lista de la suma parcial
           

        except:
            pass
            
    else:
        suma_parcial_cargas.append(cargas[indice])                  #se revisa el indice para saber si termina la suma parcial

#================================================================
# verificar si el evento es un muón
for i in range(0,len(cargas_integradas)-1,1):                       
    carga = cargas_integradas[i]
    t=t12[i]
    
    carga_sig=cargas_integradas[i+1]
    t_sig=t12[i+1]
    
    #Si la carga esta en el rango 354-642 y el siguiente es menor que 354, entonces se cataloga como muón
    if( (carga<= 642 and carga >= 354) and (carga_sig<354)):
        tiempos.append( t_sig-t + ((12/40)*10**(-6)) )              #se toma el tiempo entre eventos
    else:
        pass
""" #codigo alternativo para obtener alturas de los bines
# alturas de los bines
ax = plt.gca()
#p son todos los bins
p = ax.patches
dens=[]
for i in p:
    dens.append(i.get_height())
"""

n, bins, patches = plt.hist(tiempos, bins=1000, log=False)          #se realiza el histograma para luego utilizar las alturas para la vida media del muón
bins=bins[1:]
plt.plot(bins,n)
       
# se imprimen en archivos los datos para poder realizar la regresión exponencial en Excel
f1 = open("bins.txt", "w")
for i in range(0,len(bins),1) :
    f1.write(str(bins[i])+ os.linesep)
    
f2 = open("n.txt", "w")
for i in range(0,len(n),1) :
    f2.write(str(n[i])+ os.linesep)
#===============================================================

#GRAFICAR
        
#plt.hist(tiempos, bins=1000,log=False)                     #se grafica el histograma de cargas integradas
#print("Datos totales: ",len(archivo))                                                 #para verificar la cantidad de datos registrados
        
