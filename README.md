# Random Greetings

## Descrição do projeto

A ideia deste projeto surgiu de uma ideia minha e do meu amigo [Filipe](https://github.com/oliveirafilipe) em um momento totalmente ~~im~~produtivo de uma aula da faculdade. 

Fortemente inspirados na ideia trazida pela conta de Twitter [Nomes de Garçom](https://twitter.com/NomesGarcom) e pelas brincadeiras internas com os amigos do curso de Informática Biomédica da UFCSPA (Universidade Federal de Ciências da Saúde de Porto Alegre), pensamos em criar uma aplicação que gerasse cumprimentos aleatórios utilizando a lista do CBO (Classificação Brasileira de Ocupações), que é a lista com todos os nomes oficiais de profissões no Brasil, desde os mais simples até os mais peculiares.

## Tecnologias utilizadas

- Python 3
- Docker

## Como Contribuir

- Para contribuir com o projeto basta fazer um fork, realizar as alterações e abrir um pull request (PR) para a branch ***main*** do repositório.
    - O ***pull request*** deve conter uma descrição simples do que está sendo alterado.
    - Todos os commits devem seguir o padrão de [commits semânticos](https://medium.com/@joao.dartora/tudo-o-que-voce-precisa-saber-sobre-commits-semanticos-1cd17d099fd0).
    - Todo o código novo deverá seguir boas práticas de desenvolvimento de código / clean code e ser coberto por testes unitários (e de contrato, quando for o caso)

## Acessando o server no Heroku

- O endereço da aplicação no servidor gratuito Heroku é: ```https://randomgreetings.herokuapp.com/random-greeting```
- Para acessar o conteúdo da API, basta fazer uma requisição GET para o endereço acima. Exemplo: ```curl --location --request GET 'https://randomgreetings.herokuapp.com/random-greeting'```
- Como o Heroku é um servidor gratuito, suas máquinas ficam down quando não estão sendo utilizadas, então numa primeira requisição pode haver um tempo de resposta maior (de 15 a 20 segundos) pois a máquina estará subindo.

## Como rodar local

- Você precisará ter a engine Docker instalada.
- Remova o comentário do EXPOSE no Dockerfile para pode expor a port do server.
- Na pasta do projeto, execute o comando ```docker build -t random-greetings .``` para buildar a imagem Docker.
- Para rodar o projeto dentro do container execute o comando ```docker run -d -p 5000:5000 --name random-greetings random-greetings```.
- Após isso, o endpoint ```http://localhost:5000/random-greeting``` estará disponível para receber uma requisição do tipo GET

## Melhorias

- Utilizar imagem nativa Python
- Instalar dependências com requirements
- Adicionar um página HTML de boas-vindas no endpoint root do serviço.
- Expandir a lista de saudações possíveis para conter adjetivos.
- Retornar JSON paginado com a lista da CBO.
- Retornar um base64 em WordArt.
