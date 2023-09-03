import extract as e 
import transform as t 
import load as l
import json
import pandas as pd
import openai
import os 

sdw2023_api_url = "https://sdw-2023-prd.up.railway.app";
openai.api_key = os.getenv("OPENAI_API_KEY")

print(openai.api_key)


df = pd.read_csv('SDW2023.csv');
user_ids = df['UserID'].tolist();

users = [user for id in user_ids if (user := e.get_user(sdw2023_api_url, id)) is not None];

print(json.dumps(users, indent=2));

for user in users:
    news = t.generate_ai_news(user);
    print(news);
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news 
    })

for user in users:
    success = l.update_user(sdw2023_api_url, user)
    print(f"User {user['name']} updated? {success}!")