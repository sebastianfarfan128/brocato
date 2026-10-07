import pandas as pd
df = pd.read_csv("dataset_tito_v1.csv", encoding="utf-8")
categoria = input("Escribe una categoría: ").strip().lower()
resultado = df[df["categoria"] == categoria]
if len(resultado) == 0:
    print("No encontré esa categoría.")
else:
    print("\nPreguntas encontradas:")
    for texto in resultado["texto"]:
        print("-", texto)