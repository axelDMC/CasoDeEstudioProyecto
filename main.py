# main.py
import pandas as pd
from exploracionDx import calcular_correlacion_pearson

df = pd.read_csv('D:\\PUCP\\Proyecto\\tareaLocal\\CasoDeEstudioProyecto\\diabetes.csv')
calcular_correlacion_pearson(df)
