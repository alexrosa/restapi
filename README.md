# Agriness - Desafio 1
Obrigado pela oportunidade

# Sobre a solução:
A solução foi desenvolvida utlizando Python 3, Flask, Flask RESTPlus e SQLAlchemy. 
Busquei seguir os padrões de desenvolvimento e boas práticas do mercado. O motivo de ter utilizado essa stack é porque acho leve e prática.

A aplicação está dividida na seguinte estrutura:
* app/ -> diretório ráiz 
* /app/endpoints: serviços da api
* /app/persistência: camada de persistência com o banco de dados
* /app/business.py: módulo responsável por concentrar a camada de negócio com repositórios das entidades da aplicação.
* /app/serializers: módulo contendo os serializers JSON
* /app/settings: configurações básicas da api

# Instalando o Python no OSX:
Por favor, verifique antes de comeeçar se você já não possui a versão instalada em seu sistema operacional.
Utilize o comando abaixo para saber qual versão você tem instalada.

$ which python

ou

$ which python3

Se esse comando retornar /usr/bin/python significa que o python já está instalado em seu sistema operacional.

# Instalando Python
Por favor, instale o python seguindo este link: http://programwithus.com/learn-to-code/install-python3-mac/

# Instalando o pip
$ sudo easy_install pip

Agora por favor, instale as bibliotecas utilizadas, executando o comando abaixo dentro da pasta do projeto

$ pip install -r requirements.txt

# Executando a aplicação
Open your command line

$ cd ../agriness

$ python app.py

# TODO LIST:

1 - Desenvolver os seguintes relatórios:

    * Lista de produtos finais;

2 - Desenvolver a interface gráfica (front-end);

    * Desenvolver interface gráfica para o usuário utilizando ReactJS

