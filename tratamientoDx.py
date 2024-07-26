import pandas as pd

def eliminar_columnas_nulas(df: pd.DataFrame) -> pd.DataFrame:
    # Elimina columnas con cualquier valor nulo
    df_limpio = df.dropna(axis=1, how='any')
     
    return df_limpio

def eliminar_filas_nulas(df: pd.DataFrame) -> pd.DataFrame:
    df_limpio = df.dropna(axis=0, how='any')
    return df_limpio