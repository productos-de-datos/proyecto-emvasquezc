FROM python:3.9.13-buster

WORKDIR /app_docker

# Instalar pip
RUN apt-get update && apt-get install -y \
    libmcrypt-dev \
    python-pip

# Set language spanish ColombiaS
RUN apt-get install -y locales locales-all
ENV LC_ALL es_CO.UTF-8
ENV LANG es_CO.UTF-8
ENV LANGUAGE es_CO.UTF-8

# Cambiar sh por bash (para habilitar el comando source)
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Crear ambiente de trabajo y activarlo
RUN python3 -m venv /opt/venv_impactos

# Actualizar pip
RUN . /opt/venv_impactos/bin/activate && pip install --upgrade pip

#  Instalar requerimientos
RUN mkdir /Requirements
COPY ./requirements_development.txt ./Requirements/requirements.txt
RUN . /opt/venv_impactos/bin/activate && pip install -r ./Requirements/requirements.txt

EXPOSE 5000

CMD . /opt/venv_impactos/bin/activate && bash


#################### START NEW IMAGE : DEBUGGER ##############################
# FROM base AS debug
# RUN pip install ptvsd

# WORKDIR /app_docker
# CMD python -m ptvsd --host 0.0.0.0 --port 5678 --wait main.py