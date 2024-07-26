import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def calcular_correlacion_pearson(df):
    """
    Calcula la correlación de Pearson entre pares de variables de un DataFrame y visualiza una matriz de calor.

    Parameters:
    df (DataFrame): El DataFrame con los datos.

    Returns:
    DataFrame: Matriz de correlación de Pearson.
    """
    correlacion_pearson = df.corr(method='pearson')
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlacion_pearson, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Matriz de Correlación de Pearson')
    plt.show()
    return correlacion_pearson


# exploracionDx.py
def graficar_pairplot(df):
    sns.pairplot(df)
    plt.show()