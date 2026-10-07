import pandas as pd
# Cargar dataset
df = pd.read_csv("dataset_tito_v1.csv", encoding="utf-8")
print("=== REPORTE DE CALIDAD ===")
print("Filas totales:", len(df))
print("\nValores faltantes por columna:")
print(df.isnull().sum())
print("\nFilas duplicadas:")
print(df.duplicated().sum())
print("\nCantidad por categoría:")
print(df["categoria"].value_counts())