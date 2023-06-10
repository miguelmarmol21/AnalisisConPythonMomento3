import pandas as pd
from helpers.arbolesAnt import crearTabla
from helpers.crearBarra import graficarQuery

tabla=pd.read_csv("./data/Siembras.csv",delimiter=";")

# arboleSembrados=tabla.query('Ciudad == "Santa Fe de Antioquia" and Arboles > 250')
# queryCaucasia=tabla.query('Ciudad == "Caucasia"')
# queryBelmira=tabla.query('Vereda == "Rio Arriba" or Vereda == "La Salazar"')
queryBello=tabla.query('Ciudad == "Bello" and Vereda == "Quitasol"')
# queryCaramanta=tabla.query('Ciudad == "Caramanta" and Arboles > 100')
# queryYarumal=tabla.query('Vereda == "Mallarino"')

# crearTabla(arboleSembrados,"arbolesAnt")
# crearTabla(queryCaucasia,"caucasia")
# crearTabla(queryBelmira,"veredasBelmira")
# crearTabla(queryBello,"veredaQuitasolBello")
# crearTabla(queryCaramanta,"arbolesMayoresCaramanta")
# crearTabla(queryYarumal,"veredaMallaridoYarumal")
crearTabla(queryBello.describe(),"veredaQuitasolBello")
# estadisticaBello = queryBello.describe()

# print(estadisticaBello)