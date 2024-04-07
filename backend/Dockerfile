# Use uma imagem base do Python
FROM python:3

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie os arquivos do projeto para o diretório de trabalho
COPY . .

# Instale as dependências do backend
RUN pip install -r requirements.txt

# Exponha a porta que a aplicação usará
EXPOSE 5000

# Defina o comando padrão para executar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
