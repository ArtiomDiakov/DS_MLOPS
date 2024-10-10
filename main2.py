from fastapi import FastAPI
import json
import pandas as pd

app = FastAPI()

data = []
# Leer y cargar los datos usando json.loads
with open('user_reviews_with_sentiment.json', 'r', encoding='utf-8') as f:
    for line_number, line in enumerate(f, start=1):
        line = line.strip()
        if not line:
            continue
        try:
            # Usar json.loads para analizar cada línea
            obj = json.loads(line)
            data.append(obj)
        except json.JSONDecodeError as e:
            print(f"Error al analizar la línea {line_number}: {e}")
        except Exception as e:
            print(f"Error inesperado en la línea {line_number}: {e}")

print(f"Se cargaron correctamente {len(data)} reseñas de usuarios.")

# Convertir los datos en un DataFrame para manejarlos
try:
    df = pd.DataFrame(data)
except Exception as e:
    print(f"Error al crear el DataFrame: {e}")

print(df.head)

# Endpoints de FastAPI
@app.get("/")
def read_root():
    return {"message": "API de recomendaciones está funcionando adecuadamente"}

@app.get("/reviews")
def get_reviews():
    return data