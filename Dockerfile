# Use a imagem oficial do Python como base
# FROM python:3
FROM python:3

# Define o diretório de trabalho dentro do contêiner
WORKDIR /usr/app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

RUN apt-get update 
# && apt-get install curl
RUN apt-get install apt-transport-https

# Instale o make
RUN apt-get install -y make

# Baixe e instale o OpenSSL a partir do arquivo tar.gz
RUN curl -LO https://www.openssl.org/source/openssl-1.1.1w.tar.gz && \
    tar xzf openssl-1.1.1w.tar.gz && \
    cd openssl-1.1.1w && \
    ./config && \
    make && \
    make install && \
    cd .. && \
    rm -rf openssl-1.1.1w openssl-1.1.1w.tar.gz

# # # Aceite o EULA automaticamente ao instalar os pacotes
ENV ACCEPT_EULA=Y

# Adicione a chave GPG da Microsoft
RUN curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc

# Adicione o repositório SQL Server à lista de fontes
RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | tee /etc/apt/sources.list.d/mssql-release.list

# Atualize a lista de pacotes e instale as dependências
RUN apt-get update && \
    apt-get install -y msodbcsql18 && \
    apt-get install -y mssql-tools18


# Adicione o diretório das ferramentas ao PATH do usuário
RUN echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc

RUN apt-get update && apt-get install -y unixodbc-dev && \
    apt-get install -y libgssapi-krb5-2

RUN rm /etc/odbcinst.ini
RUN echo "[ODBC Driver 18 for SQL Server]\n\
Description=Microsoft ODBC Driver 18 for SQL Server\n\
Driver=/opt/microsoft/msodbcsql18/lib64/libmsodbcsql-18.3.so.2.1\n\
UsageCount=1\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini

# Instale as dependências do projeto
RUN pip install -r requirements.txt


RUN chmod +rwx /etc/ssl/openssl.cnf
RUN sed -i 's/TLSv1.2/TLSv1/g' /etc/ssl/openssl.cnf
RUN sed -i 's/SECLEVEL=2/SECLEVEL=1/g' /etc/ssl/openssl.cnf

# Copie o restante dos arquivos do projeto para o contêiner
COPY . .

# Inicialize o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

