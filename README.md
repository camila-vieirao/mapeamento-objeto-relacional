# Sistema de Gerenciamento de Loja de Vinil com SQLAlchemy

Este projeto tem como objetivo desenvolver um mapeamento objeto-relacional utilizando a biblioteca **SQLAlchemy** em Python para interagir com bancos de dados relacionais. O modelo foi desenvolvido para gerenciar uma loja de discos de vinil, permitindo o cadastro de clientes, funcionários e vinis, além de operações CRUD no banco de dados.

## Sumário

1. [Introdução](#introdução)  
2. [Descrição Textual – Entidades e Atributos](#descrição-textual--entidades-e-atributos)  
3. [Relacionamentos](#relacionamentos)  
4. [Rodando o programa](#rodando-o-programa)  

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

---

## Rodando o programa

Foi utilizado um ambiente virtual Python para o isolamento das dependências do projeto:
```bash
python -m venv env
env\Scripts\activate
pip install -r .\requirements.txt
```

### Inserção e Verificação de Dados

Após a inserção dos dados no banco de dados através do menu, é possível verificar os dados executando comandos SQL diretamente no MySQL Workbench, como o exemplo abaixo:

```
SELECT * FROM clientes;
```
Dessa forma, podemos consultar os registros inseridos no banco de dados e verificar o funcionamento do sistema.

