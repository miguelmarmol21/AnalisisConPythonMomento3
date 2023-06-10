import matplotlib.pyplot as plt

def graficarQuery(dataFrame,campoX,campoY,nombreGrafica):
    colores=['green','red','blue']
    promedio=dataFrame.groupby(campoX)[campoY].mean()
    
    #Generar la grafica

    plt.bar(promedio.index,promedio,color=colores)
    plt.title('Promedio de Siembra')
    plt.xlabel('Veredas')
    plt.ylabel('Arboles')
    
    plt.savefig(f"./assets/img/{nombreGrafica}.png")