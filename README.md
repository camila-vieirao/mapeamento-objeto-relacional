# Sistema de Gerenciamento de Loja de Vinil com SQLAlchemy

Este projeto tem como objetivo desenvolver um mapeamento objeto-relacional utilizando a biblioteca **SQLAlchemy** em Python para interagir com bancos de dados relacionais. O modelo foi desenvolvido para gerenciar uma loja de discos de vinil, permitindo o cadastro de clientes, funcionários e vinis, além de operações CRUD no banco de dados.

## Sumário

1. [Introdução](#introdução)  
2. [Descrição Textual – Entidades e Atributos](#descrição-textual--entidades-e-atributos)  
3. [Relacionamentos](#relacionamentos)  
4. [Desenvolvimento do Projeto](#desenvolvimento-do-projeto)  

## Introdução

O sistema desenvolvido neste trabalho é voltado para o gerenciamento de uma loja de vinil. Através deste sistema, o usuário poderá realizar operações como o cadastro de clientes, funcionários e discos de vinil, além de consultas e manipulações de dados.

## Descrição Textual – Entidades e Atributos

### 2.1 Pessoa
- `cpf`: VARCHAR(11), UNIQUE, NOT NULL
- `nome`: VARCHAR(255), NOT NULL
- `rg`: VARCHAR(12), UNIQUE, NOT NULL
- `data_nasc`: DATE, NOT NULL

### 2.2 Cliente (Herda de Pessoa)
- `endereço`: VARCHAR(255), NOT NULL

### 2.3 Funcionário (Herda de Pessoa)
- `salario`: DECIMAL(8,2) NOT NULL

### 2.4 Vinil
- `id`: INT, PK, UNIQUE, NOT NULL, AU
- `genero`: VARCHAR(255), NOT NULL
- `artista`: VARCHAR(255), NOT NULL

## Relacionamentos

- Um Cliente pode comprar no mínimo 0 discos e no máximo N discos.
- Um disco de vinil é comprado por 1 cliente.

## Desenvolvimento do Projeto

### 4.1 Configuração do Ambiente

Foi utilizado um ambiente virtual Python para o isolamento das dependências do projeto:
```bash
python -m venv .venv
.venv\Scripts\activate
```
As bibliotecas MySQL e SQLAlchemy foram instaladas para gerenciar o banco de dados.

### 4.2 Configuração do Banco de Dados

A conexão com o banco de dados MySQL foi configurada no arquivo `database.py`, onde são definidos os parâmetros da conexão e o **engine** do **SQLAlchemy**. Abaixo, está o exemplo do código no arquivo `database.py`:

```python
from sqlalchemy import create_engine

DATABASE_URL = "mysql+mysqlconnector://user:password@localhost:3306/vinil_store"
engine = create_engine(DATABASE_URL)
```
Para criar e conectar o banco de dados no MySQL Workbench, utilizamos o seguinte comando SQL:
```
CREATE DATABASE vinil_store;
```

### 4.3 Definição dos Modelos

No diretório `models`, foram criados os seguintes arquivos, cada um representando uma entidade no sistema:

- `pessoa.py`
- `cliente.py`
- `funcionario.py`
- `vinil.py`

Cada arquivo define uma classe com os atributos e relacionamentos das entidades.

### 4.4 Criação das Tabelas

Para criar as tabelas no banco de dados a partir dos modelos, foi desenvolvido o script `create_once.py`. Este script executa a criação de todas as tabelas baseadas nas definições dos modelos.

### 4.5 Execução do Programa

Após a configuração do ambiente e a criação das tabelas, iniciamos o programa executando o arquivo `main.py`. O arquivo `menu.py` é responsável por apresentar o menu inicial para o usuário, permitindo interagir com o sistema.

O menu inclui opções para gerenciar clientes, funcionários e vinis, além de realizar operações CRUD (Create, Read, Update, Delete) em cada uma dessas entidades.

### 4.6 Inserção e Verificação de Dados

Após a inserção dos dados no banco de dados através do menu, é possível verificar os dados executando comandos SQL diretamente no MySQL Workbench, como o exemplo abaixo:

```
SELECT * FROM clientes;
```
Dessa forma, podemos consultar os registros inseridos no banco de dados e verificar o funcionamento do sistema.

