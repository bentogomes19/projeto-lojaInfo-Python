# Sistema para gerenciamento de Estoque/Vendas de uma loja de informática.

### Requsitos do Sistema
 - Sistema Operacional: Windows
 - Linguagem de Programação: Python 🐍
 - Banco de Dados: SQLite3
 
### Instalação

- Baixar o repositório
       $ git clone "https://github.com/bentogomes19/projeto-lojaInfo-Python.git"
- Comando para Compilar e executar o programa pelo terminal WINDOWS
       $ python main.py

### Menu de Opção
##### 1. Cadastrar Clientes 
##### 2. Cadastrar Produtos 
##### 3. Mostrar Clientes Cadastrados
##### 4. Mostrar Produtos Cadastrados
##### 5. Cadastrar Vendas 
##### 6. Mostrar todas as vendas realizadas
##### 7. Consultas (CLIENTES, PRODUTOS E VENDAS).

### Criar um Banco de Dados com as tabelas

 ## Tabela CLIENTES

| Coluna          | Tipo de Dado | Descrição                          |
|-----------------|--------------|------------------------------------|
| `cod_cliente`   | INTEGER      | Identificador único do cliente      |
| `nome`          | TEXT         | Nome do cliente                     |
| `email`         | TEXT         | Email do cliente                    |
| `telefone`      | TEXT         | Número de telefone do cliente       |
| `cpf`           | TEXT         | CPF do cliente                      |
| `data_registro` | DATE         | Data de registro do cliente         |
| `situacao`      | TEXT         | Situação do cliente (ativo/inativo) |


## Tabela PRODUTOS

| Coluna              | Tipo de Dado | Descrição                         |
|---------------------|--------------|-----------------------------------|
| `cod_produto`       | INTEGER      | Identificador único do produto     |
| `marca`             | TEXT         | Marca do produto                  |
| `nome`              | TEXT         | Nome do produto                   |
| `quantidade_estoque`| INTEGER      | Quantidade disponível em estoque  |
| `valor_unitario`    | REAL         | Valor unitário do produto         |
| `data_registro`     | DATE         | Data de registro do produto       |

## Tabela VENDAS

| Coluna         | Tipo de Dado | Descrição                        |
|----------------|--------------|----------------------------------|
| `cod_venda`    | INTEGER      | Identificador único da venda      |
| `cod_cliente`  | INTEGER      | Identificador do cliente (FK)     |
| `cod_produto`  | INTEGER      | Identificador do produto (FK)     |
| `quantidade`   | INTEGER      | Quantidade vendida                |
| `valor_total`  | REAL         | Valor total da venda              |
| `data_venda`   | DATE         | Data da venda                     |

#### Opção 01: Deve permitir que o usuário insira os seguintes dados (NOME, EMAIL, TELEFONE, CPF).
       cod_cliente -> gerado automaticamente pelo banco de dados.
       data_registro -> gerado automaticamente pelo banco de dados.
       situacao -> ATIVO OU INATIVO -> assim que o usuário confirmar seus dados o sistema automaticamente torna-se esse cliente ATIVO
       Permitir que o usuário possa ver e confirmar seus dados.
    
#### Opção 02: Deve permitir que o usuário insira os seguintes dados (MARCA, NOME, QUANTIDADE EM ESTOQUE, PREÇO (R$))
        cod_produto -> gerado automaticamente pelo banco de dados.
        data_registro -> gerado automaticamente pelo banco de dados.
        Se a quantidade de um produto estiver abaixo de 10 mostrar mensagem "ESTOQUE EM BAIXA!!"

#### Opção 03: Mostrar todos os clientes cadastrados no sistema.
       Fazer uma lista de todos os clientes cadastrados com os dados (COD_CLIENTE, NOME, EMAIL, TELEFONE, DATA_REGISTRO, SITUAÇÃO)

#### Opção 04: Mostrar todos os produtos cadastrados no sistema.
     # Mostrar ao usuário uma lista com todos os produtos cadastrados no sistema com os seguintes dados (COD_PRODUTO, NOME, MARCA, QUANTIDADE_ESTOQUE, VALOR_UNITARIO, DATA_REGISTRO)

     #  Ao final da listagem mostrar um relatório com um somatório de produtos cadastrados, ou seja, mostrar a quantidade de produtos cadastrados.
     # Mostrar ao final da listagem o valor total que há no estoque.

#### Opção 05: Efetuar o cadastro de uma venda no sistema com os seguintes dados a serem iseridos (COD_CLIENTE, COD_PRODUTO, QUANTIDADE)
        # Caso o usuário não saiba o codigo do cliente, poderá digitar 3 para mostrar todos os clientes cadastrados
        # Caso o usuário não saiba o codigo do produto, poderá digitar 4 para mostrar todos os produtos cadastrados
        # O sistema so pode efetuar uma venda se tiver uma quantidade maior do que zero no estoque, caso contrário, mostrar mensagem
        # Se a quantidade inserida pelo usuário for maior do que armazenada no estoque, mostrar mensagem
        # Após efetuar uma venda e respeitar todas as validações, mostrar mensagem.
        # Efetivar baixa no sistema após o usuário confirmar a venda.

#### Opção 06: Mostrar todas as vendas que foram efetuadas no sistema.
       # Fazer uma listagem com todas as vendas feitas com os seguinte dados 
       # (COD_VENDA, COD_CLIENTE, NOME DO CLIENTE, VALOR_PAGO)

#### Opção 07: Consultas
       - Criar um outro menu para consultas
       - MENU DE OPÇÕES
            - 01. CLIENTES
            - 02. PRODUTOS
            - 03. VENDAS
       
            # - 01. CLIENTES
                # Solicitar ao usuário o nome ou o codigo do cliente, caso ele não saiba o nome, deverá digitar 3 para listar todos os clientes cadastrados
                # Caso o cliente esteja cadastrado mostrar menu
           -        -> 1. EDITAR DADOS 2. EXCLUIR CLIENTE
                        1. O usuário deverá selecionar quais dados ele quer editar (NOME, EMAIL, TELEFONE, CPF, SITUAÇÃO)
                        1.1 Ao final da alteração mostrar mensagem
                        1.2 O sistema deve mostrar todos o clientes cadastrados
                        # Caso o cliente não esteja no banco de dados mostrar mensagem.

            # - 02. PRODUTOS
                # Solicitar ao usuário o codigo do produto, caso ele não saiba o codigo, deverá digitar 4 para listar todos os produtos cadastrados
                # Caso o produto esteja cadastrado mostrar menu
                    -> 1. EDITAR DADOS 2. EXCLUIR PRODUTO
                        1. O usuário deverá selecionar quais dados ele quer editar (QUANTIDADE EM ESTOQUE, VALOR UNITÁRIO)
                        1.1 Ao final da alteração mostrar mensagem
                    # Caso o produto não esteja no banco de dados mostrar mensagem.

            # - 03. VENDAS
                # Solicitar ao usuário O codigo da venda, caso ele não saiba o codigo, deverá digitar 6 para listar todas as vendas cadastradas
                - Caso uma venda esteja cadastrada mostrar menu
                        -> 1. EDITAR DADOS 2. EXCLUIR VENDA
                            1. O usuário deverá selecionar quais dados ele quer editar (CODIGO DO CLIENTE, CODIGO DO PRODUTO, QUANTIDADE, VALOR FINAL)
                            1.1 Ao final da alteração mostrar mensagem
                        - Caso a venda não esteja cadastrada mostrar mensagem.

### ** REGRAS GERAIS ***
### - Realizar todas as validações de codigo para clientes, produtos e vendas
### - os codigos são valores de 4 dígitos gerados aleatoriamente pelo sistema e não pode ser alterado
### - Ao excluir um cliente, produto ou uma venda dar baixa no banco de dados


# Árvore do Repositório
projeto_loja/
        ├── __pycache__/
        │   ├── clientes.cpython-3x.pyc
        │   ├── consultas.cpython-3x.pyc
        │   ├── database.cpython-3x.pyc
        │   └── ...
        ├── clientes.py
        ├── consultas.py
        ├── database.py
        ├── DataBaseLoja.db
        ├── produtos.py
        ├── pain.y
        ├── README.md
        └── vendas.py



