
#Importacion de la libreria necesaria para poder graficar
import matplotlib.pyplot as plt
#Le preguntamos al usuario cuantas veces se va a repetir el codigo
repeticion=int(input("Cuantas veces queres que se repita el codigo: "))
#Listas que llenaremos luego para hacer los graficos
graf1x=[]
graf1y=[]
graf2y=[]
graf2x=[]
for i in range(0,repeticion):
    def variables():
        #El usuario ingresa los valores con los que luego vamos a hacer las cuentas
        vel= float(input("ingrese la velocidad en m/s: "))
        #Bucle para no dejar que ingrese velocidad en negativo
        while vel<0:
          vel= float(input("Por favor, ingrese la velocidad en positivo:"))
          if vel>0:
            break
        cabal=float(input("ingrese la distancia del objeto 1 hasta el objeto 2(en metros): "))
        #Bucle para no dejar que el usuario ingrese la distancia en negativo
        while cabal<0:
          cabal=float(input("Por favor, ingresar de nuevo la distancia entre los dos puntos (en metros y positivo): "))
          if cabal>0:
            break
        fren= float(input("ingrese a que aceleracion el objeto 1 desacelera(expresalo en negativo): "))
        return calculos(vel, cabal, fren)
    def calculos(vel, cabal, fren):
        #Bucle para que el usuario no pueda poner la desaceleracion en positivo
        while fren>0:
            fren= float(input("NO se puede la desaceleracion numero positivo ponelo en negativo: "))
            if fren<0:
                break
        #Calculos con los numeros que haya puesto el usuario anteriormente
        calc= 0-vel
        tie= calc/fren
        dist= 0+vel*tie+0.5*fren*(tie*tie)
        #Resultados
        if dist>cabal:
            print("El objeto 1 choco al objeto 2")
            c = vel + (1/2)*(0-vel)
            c2 = cabal/c
            acel = (0-vel)/c2
            print("El objeto 1 necesitaba frenar a ", acel, "m/s2 para no chocar y lo choco en",tie, "segundos")
        elif dist<=cabal:
            dist2=cabal-dist
            print("Lo choco en",tie,"segundos y necesitaba frenar a",dist2,"m/s2 para no chocar")
        #Agregado de los resultados a las listas de los graficos para poder graficar mas abajo
        graf1y.append(tie)
        graf1x.append(dist)
        graf2x.append(vel)
        graf2y.append(tie)
    variables()
#Grafico 1 (Distancia en funcion del tiempo)
width=0.5
plt.figure(1)
plt.bar(graf1y,graf1x, width=width, color="grey")
plt.plot(graf1y, graf1x, color="black")
plt.ylabel("Distancia (m)")
plt.xlabel("Tiempo (s)")
plt.title("Distancia sobre tiempo")
#Grafico 2 (Velocidad en funcion del tiempo)
plt.figure(2)
width=2
plt.scatter(graf2y,graf2x,color="blue")
plt.plot(graf2y,graf2x, color="grey")
plt.ylabel("Velocidad (m/s)")
plt.xlabel("Tiempo (s)")
plt.title("Velocidad en funcion del Tiempo del objeto 1")
plt.show()
#Fin :)
