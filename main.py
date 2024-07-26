# main.py
import pandas as pd
from tratamientoDx import eliminar_columnas_nulas
from exploracionDx import calcular_correlacion_pearson
from exploracionDx import graficar_pairplot

df = pd.read_csv('diabetes.csv')
df = eliminar_columnas_nulas(df)
calcular_correlacion_pearson(df)
graficar_pairplot(df)
