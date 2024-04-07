# Use uma imagem base do Node.js
FROM node:alpine

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie os arquivos do projeto para o diretório de trabalho
COPY . .

# Instale as dependências
RUN npm install

# Exponha a porta que a aplicação usará
EXPOSE 3000

# Defina o comando padrão para executar a aplicação
CMD ["npm", "run", "dev"]