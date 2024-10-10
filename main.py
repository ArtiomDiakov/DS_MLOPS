from fastapi import FastAPI
import pandas as pd
import json

app = FastAPI()

# Cargar user_reviews_with_sentiment.json
with open('user_reviews_with_sentiment.json', 'r', encoding='utf-8') as f:
    user_reviews_data = [json.loads(line) for line in f if line.strip()]

df_user_reviews = pd.DataFrame(user_reviews_data)

# Cargar steam_games.json
with open('steam_games.json', 'r', encoding='utf-8') as f:
    steam_games_data = [json.loads(line) for line in f if line.strip()]

df_steam_games = pd.DataFrame(steam_games_data)

# Cargar users_items.json
with open('users_items.json', 'r', encoding='utf-8') as f:
    users_items_data = [json.loads(line) for line in f if line.strip()]

df_users_items = pd.DataFrame(users_items_data)

