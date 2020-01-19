# imagem base
FROM python:latest

MAINTAINER Gui Castro

# Copia o código fonte pro container (no caso o conteúdo da pasta atual)
COPY  . /api_relay_control

# Diretório aonde o container vai rodar comandos
WORKDIR /api_relay_control

# Instala as dependências - roda no build da imagem
RUN pip3 install Flask
RUN pip3 install adafruit-io

# Roda qnd o container é iniciado
ENTRYPOINT python3 app.py
