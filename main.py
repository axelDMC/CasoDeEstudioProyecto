# main.py
import pandas as pd
from tratamientoDx import eliminar_columnas_nulas

df = pd.read_csv('diabetes.csv')
# df = pd.read_csv('D:\\PUCP\\Proyecto\\tareaLocal\\CasoDeEstudioProyecto\\diabetes.csv')
df = eliminar_columnas_nulas(df)
