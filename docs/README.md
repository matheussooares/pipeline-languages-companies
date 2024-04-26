
Somos contratados como pessoas engenheiras de dados em uma startup. Como nosso primeiro trabalho, nós precisamos desenvolver um projeto onde obtemos dados das linguagens de programação utilizadas por algumas grandes empresas, como Amazon, Spotify, Netflix e Apple.

Para realizar esse projeto, é necessário criarmos um pipeline ETL, que consiste nas etapas de extração, transformação e carga (em inglês, Extract, Transform e Load). Em outras palavras, iremos desenvolver um projeto no qual vamos extrair, transformar e armazenar dados específicos relacionados ao nosso objetivo.

## Tecnologias Utilizadas

Para implementar esse ETL, faremos uso da biblioteca Requests do Python e também da API do GitHub. Através da API, teremos acesso aos dados sobre as linguagens de programação utilizadas pelas empresas mencionadas em seus projetos.
````
import requests
````

[Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)

A biblioteca Requests facilita o envio e recebimento de informações pela internet.