<h1 align="center">Flix API</h1>

![Badge Concluído](https://img.shields.io/static/v1?label=Status&message=Concluído&color=green&style=for-the-badge)

![Badge Pytho](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

![Badge Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)

##📖 Resumo do projeto

Flix API é uma plataforma de compartilhamento de vídeos. Projeto proposto criado para colocar em prática conhecimentos de Django Rest e aprender API REST.

##💡 Funcionalidades

-`Autenticação</br> `

  Todos os recursos, exceto  **POST /authentication/token/** requerem clientes autenticados,

  o qual deve ser feita em todas as requisições via Json,

  enviando o body:

```
{
    "username": "user",
    "password": "password"
}
```

```````````````````</br>````````````````````

-`Generos</br>`

-`Listar todos os generos`: Lista todos os generos de filmes da API. Segue abaixo o corpo de requisicao:  `</br>`
