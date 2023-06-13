import pandas as pd
from helpers.arbolesAnt import crearTabla
from helpers.crearBarra import graficarQuery

# Crear el dataFrame

tabla=pd.read_csv("./data/Siembras.csv",delimiter=";")

# Crear los query de los filtros

querysantaFeAntioquia=tabla.query('Ciudad == "Santa Fe de Antioquia" and Arboles > 250')
queryCaucasia=tabla.query('Ciudad == "Caucasia"')
queryBelmira=tabla.query('Vereda == "Rio Arriba" or Vereda == "La Salazar"')
queryBello=tabla.query('Ciudad == "Bello" and Vereda == "Quitasol"')
queryCaramanta=tabla.query('Ciudad == "Caramanta" and Arboles > 100')
queryYarumal=tabla.query('Vereda == "Mallarino"')

# Crear las tablas de los query

crearTabla(querysantaFeAntioquia,"arbolesSantaFeAnt")
crearTabla(queryCaucasia,"caucasia")
crearTabla(queryBelmira,"veredasBelmira")
crearTabla(queryBello,"veredaQuitasolBello")
crearTabla(queryCaramanta,"arbolesMayoresCaramanta")
crearTabla(queryYarumal,"veredaMallaridoYarumal")
crearTabla(queryBello.describe(),"veredaQuitasolBello")

# Crear los query de cada ciudad con Arboles sembrados mayores a 500

queryGraficaSantaFeAnt=tabla.query('Ciudad == "Santa Fe de Antioquia" and Arboles > 500')
queryGraficaCaucasia=tabla.query('Ciudad == "Caucasia" and Arboles > 500')
queryGraficaBelmira=tabla.query('Ciudad == "Belmira" and Arboles > 500')
queryGraficaBello=tabla.query('Ciudad == "Bello" and Arboles > 500')
queryGraficaCaramanta=tabla.query('Ciudad == "Caramanta" and Arboles > 500')
queryGraficaYarumal=tabla.query('Ciudad == "Yarumal" and Arboles > 500')

# Graficar los query realizados para cada municipio

graficarQuery(queryGraficaSantaFeAnt,'Vereda','Arboles','graficaSantafeAnt')
graficarQuery(queryGraficaCaucasia,'Vereda','Arboles','graficaCaucasia')
graficarQuery(queryGraficaBelmira,'Vereda','Arboles','graficaBelmira')
graficarQuery(queryGraficaBello,'Vereda','Arboles','graficaBello')
graficarQuery(queryGraficaCaramanta,'Vereda','Arboles','graficaCaramanta')
graficarQuery(queryGraficaYarumal,'Vereda','Arboles','graficaYarumal')

