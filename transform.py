import openai

def generate_ai_news(user):

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                  "content": "Voce e um especialista em marketing bancario."
            },
            {
                "role": "user",
                 "content": f"Crie uma mensagem para {user['name']} sobre a importancia dos investimentos (maximo de 100 caracateres)"
            }
        ]
    )

    return completion.choices[0].message.content.strip('\"');