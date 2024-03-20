#!/bin/bash

#Navegar até o diretório do backend
cd ../CB_BACK

# Dependências Back-End do Projeto
pip install -r requirements.txt
#Executar o servidor Flask do Python
python app.py &

#Navegar de volta para o frontend
cd ../CB_FRONT/cbtrips

# Dependências Front-End do Projeto

npm install
# Executar o servidore Front-End
npm run serve



