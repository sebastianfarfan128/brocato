import pandas as pd
# 1. Cargar el archivo CSV
df = pd.read_csv("dataset_tito.csv", encoding="utf-8")
# 2. Mostrar las primeras filas
print("PRIMERAS FILAS")
print(df.head())
# 3. Mostrar cuántas filas hay
print("\nCantidad de preguntas:", len(df))
# 4. Mostrar los nombres de las columnas
print("Columnas:", list(df.columns))
# 5. Mostrar las categorías existentes
print("Categorías:")
print(df["categoria"].unique())
# 6. Contar cuántas preguntas hay por categoría
print("\nPreguntas por categoría:")
print(df["categoria"].value_counts())