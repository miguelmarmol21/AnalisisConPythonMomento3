import matplotlib.pyplot as plt

def graficarQuery(dataFrame,campoX,campoY,nombreGrafica):
    colores=['#2A5C30', '#185286', '#9E6114', '#49BB0D', '#BB0D15']
    promedio=dataFrame.groupby(campoX)[campoY].mean()
    
    #Generar la grafica

    plt.bar(promedio.index,promedio,color=colores)
    plt.title('Promedio de Siembra')
    plt.xlabel('Veredas')
    plt.ylabel('Arboles Sembrados')
    
    plt.savefig(f"./assets/img/{nombreGrafica}.png")