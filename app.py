from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Configura a chave da API usando uma variável de ambiente
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    if request.method == 'POST':
        text = request.form['text']
        summary = generate_summary(text)
    return render_template('index.html', summary=summary)

def generate_summary(text):
    try:
        response = openai.Completion.create(
            model='gpt-3.5-turbo',
            prompt=f"Resuma o seguinte texto: {text}",
            max_tokens=100  # Ajuste o número de tokens conforme necessário
        )
        return response['choices'][0]['text'].strip()
    except openai.OpenAIError as e:
        if 'insufficient_quota' in str(e):
            return "Erro na API: Limite de uso atingido. Verifique sua conta ou tente novamente mais tarde."
        return f"Erro na API: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
