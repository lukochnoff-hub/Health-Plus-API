# Health Plus API

API desenvolvida em **Python** para dar suporte à aplicação web **Health Plus**, responsável pelo gerenciamento de usuários, autenticação e comunicação entre o front-end e os dados da aplicação.

---

## Sobre o Projeto

A Health Plus API foi criada para fornecer os serviços necessários para o funcionamento da plataforma Health Plus, uma solução voltada para saúde, autocuidado e gamificação de hábitos saudáveis.

A API atua como camada de comunicação entre a interface web e os dados do sistema, permitindo que as informações dos usuários sejam armazenadas, consultadas e atualizadas de forma organizada.

---

## Funcionalidades

A API disponibiliza recursos para:

* cadastro de usuários
* autenticação de acesso
* consulta de informações do usuário
* atualização de dados cadastrais
* exclusão de contas
* integração com o front-end desenvolvido em React

---

## Equipe de Desenvolvimento

| RM | Nome |
|----|------|
| RM 567947 | Lara Mofid Essa Alssabak |
| RM 567355 | Maria Luisa Boucinhas Franco |
| RM 568459 | Maria Luiza Kochnoff da Matta |
| RM 567825 | Roberta Moreira dos Santos |


---

## Tecnologias Utilizadas

* Python
* Flask
* Flask-CORS
* Json
* REST API
* Render

---

## Estrutura do Projeto

```bash
Health-Plus-API/
├── app.py
├── models/
├── database/
├── routes/
├── requirements.txt
└── README.md
```

---

## Endpoints Principais

### Usuários

#### Cadastro

```http
POST /usuario
```

Cria um novo usuário.

#### Consulta

```http
GET /usuario/<cpf>
```

Retorna os dados de um usuário.

#### Atualização

```http
PUT /usuario/<cpf>
```

Atualiza as informações do usuário.

#### Exclusão

```http
DELETE /usuario/<cpf>
```

Remove o usuário do sistema.

---

## Integração com o Front-End

Esta API é consumida pela aplicação web Health Plus desenvolvida em React.

As operações de cadastro, login, consulta de perfil e gerenciamento de conta são realizadas através de requisições HTTP entre o front-end e a API.

Repositório Front-End:
```txt

https://github.com/1ESPA-PinkCode/Challenge-WebFront
```

---

## Deploy

API publicada utilizando Render.

Repositório:
```txt

https://challenge-web-front-self.vercel.app/
```

---

## Como Executar Localmente

### 1. Clone o repositório

```bash
https://github.com/lukochnoff-hub/Health-Plus-API
```

### 2. Entre na pasta do projeto

```bash
cd Health-Plus-API
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
python app.py
```

### 5. Acesse localmente

```bash
http://127.0.0.1:5000
```

---

## Objetivo Acadêmico

Este projeto foi desenvolvido para a disciplina de Web Development e Front-End Design com o objetivo de aplicar conceitos de:

* desenvolvimento de APIs REST
* integração entre front-end e back-end
* persistência de dados
* arquitetura cliente-servidor
* desenvolvimento com Python
* consumo de APIs
* experiência do usuário
* aplicações web completas

