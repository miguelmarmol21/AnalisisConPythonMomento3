import pandas as pd
import matplotlib.pyplot as plt

def calcularPromedioPorCiudad(dataFrame,rangos,columnaInteres,columnaPromediar,nombreGrafica):
    plt.figure()
    
    #Crear una columna nueva para rangos de veredas
    dataFrame['rangosArboles']=pd.cut(dataFrame[columnaInteres],bins=rangos)
    #Calcular la suma de los salarios por rango de edad
    salarioPorRango=dataFrame.groupby('rangosArboles')[columnaPromediar].sum()
    #Definimos los datos a 
    salario=salarioPorRango.values
    rangosEdad=salarioPorRango.index
    
    plt.pie(salario,labels=rangosEdad,autopct='%1.1f%%')
    plt.title('Salario el nombre por edad')
    
    plt.savefig(f"./assets/img/{nombreGrafica}.png")