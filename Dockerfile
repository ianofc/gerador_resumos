# Usar a imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar arquivos necessários
COPY requirements.txt requirements.txt

# Instalar as dependências
RUN pip install -r requirements.txt

# Copiar o restante do código
COPY . .

# Expor a porta que o Flask usará
EXPOSE 5000

# Comando para rodar o aplicativo
CMD ["python", "app.py"]
