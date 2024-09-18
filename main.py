# Criar um programa para gerenciamento de vendas de uma loja de informática.
# Requsitos Obrigatório no Sistema
# Menu de Opção
# 1. Cadastrar Clientes 2. Cadastrar Produtos 3. Mostrar Clientes Cadastrados 4. Mostrar Produtos Cadastrados
# 5. Cadastrar Vendas 6. Mostrar todas as vendas realizadas 7. Consultas (CLIENTES, PRODUTOS E VENDAS).
# Criar um Banco de Dados com as tabelas
# CLIENTES                       PRODUTOS                    VENDAS
# cod_cliente                   cod_produto                 cod_venda
# nome                          marca                       cod_cliente
# email                         nome                        cod_produto
# telefone                      quantidade_estoque          quantidade
# cpf                           valor_unitario              valor_total
# data_registro                 data_registro               data_venda
# situacao

# Opção 01: Deve permitir que o usuário     insira os seguintes dados (NOME, EMAIL, TELEFONE, CPF).
#       - cod_cliente -> gerado automáticamente pelo banco de dados.
#       - data_registro -> gerado automáticamente pelo banco de dados.
#       - situacao -> ATIVO OU INATIVO -> assim que o usuário confirmar seus dados o sistema automaticamente torna-se esse cliente ATIVO
#       - Permitir que o usuário possa ver e confirmar seus dados.

# Opção 02: Deve permitir que o usuário insira os seguintes dados (MARCA, NOME, QUANTIDADE EM ESTOQUE, PREÇO (R$))
#       - cod_produto -> gerado automaticamente pelo banco de dados.
#       - data_registro -> gerado automaticamente pelo banco de dados.
#       - Se a quantidade de um produto estiver abaixo de 10 mostrar mensagem "ESTOQUE EM BAIXA!!"

# Opção 03: Mostrar todos os clientes cadastrados no sistema.
#       - Fazer uma lista de todos os clientes cadastrados com os dados (COD_CLIENTE, NOME, EMAIL, TELEFONE, DATA_REGISTRO, SITUAÇÃO)

# Opção 04: Mostrar todos os produtos cadastrados no sistema.
#       - Mostrar ao usuário uma lista com todos os produtos cadastrados no sistema com os seguintes dados (COD_PRODUTO, NOME, MARCA, QUANTIDADE_ESTOQUE, VALOR_UNITARIO, DATA_REGISTRO)
#       - Ao final da listagem mostrar um relatório com um somatório de produtos cadastrados, ou seja, mostrar a quantidade de produtos cadastrados.
#       - Mostrar ao final da listagem o valor total que há no estoque.

# Opção 05: Efetuar o cadastro de uma venda no sistema com os seguintes dados a serem iseridos (COD_CLIENTE, COD_PRODUTO, QUANTIDADE)
#       - Caso o usuário não saiba o codigo do cliente, poderá digitar 3 para mostrar todos os clientes cadastrados
#       - Caso o usuário não saiba o codigo do produto, poderá digitar 4 para mostrar todos os produtos cadastrados
#       - O sistema so pode efetuar uma venda se tiver uma quantidade maior do que zero no estoque, caso contrário, mostrar mensagem
#       - Se a quantidade inserida pelo usuário for maior do que armazenada no estoque, mostrar mensagem
#       - Após efetuar uma venda e respeitar todas as validações, mostrar mensagem.
#       - Efetivar baixa no sistema após o usuário confirmar a venda.

# Opção 06: Mostrar todas as vendas que foram efetuadas no sistema.
#       - Fazer uma listagem com todas as vendas feitas com os seguinte dados (COD_VENDA, COD_CLIENTE, NOME DO CLIENTE, VALOR_PAGO)

# Opção 07: Consultas
#       - Criar um outro menu para consultas
#       - MENU DE OPÇÕES
#       - 01. CLIENTES
#       - 02. PRODUTOS
#       
#       - 01. CLIENTES
#       - Solicitar ao usuário o nome ou o codigo do cliente, caso ele não saiba o nome, deverá digitar 3 para listar todos os clientes cadastrados
#       - Caso o cliente esteja cadastrado mostrar menu
#           - 1. EDITAR DADOS 2. EXCLUIR CLIENTE
#               1. O usuário deverá selecionar quais dados ele quer editar (NOME, EMAIL, TELEFONE, CPF, SITUAÇÃO)
#               1.1 Ao final da alteração mostrar mensagem
#               1.2 O sistema deve mostrar todos o clientes cadastrados
#       - Caso o cliente não esteja no banco de dados mostrar mensagem.

#       - 02. PRODUTOS
#       - Solicitar ao usuário o codigo do produto, caso ele não saiba o codigo, deverá digitar 4 para listar todos os produtos cadastrados
#       - Caso o produto esteja cadastrado mostrar menu
#           - 1. EDITAR DADOS 2. EXCLUIR PRODUTO
#               1. O usuário deverá selecionar quais dados ele quer editar (QUANTIDADE EM ESTOQUE, VALOR UNITÁRIO)
#               1.1 Ao final da alteração mostrar mensagem
#       - Caso o produto não esteja no banco de dados mostrar mensagem.

# ** REGRAS GERAIS ***
# - Realizar todas as validações de codigo para clientes, produtos e vendas
# - os codigos são valores de 4 dígitos gerados aleatoriamente pelo sistema e não pode ser alterado
# - Ao excluir um cliente ou produto dar baixa no banco de dados
    
import os
from clientes import Clientes
from produtos import Produtos
from consultas import Consultas
from vendas import Vendas
class Menu():
    def __init__(self):     
        self.op = None

    def MenuPrincipal(self):   
        produto = Produtos()     
        cliente = Clientes()
        venda = Vendas()
        consulta = Consultas()
        x = False
        while not x:
            os.system("cls") # os.system("clear") # LINUX
            print("******** SISTEMA DE GERENCIAMENTO DE ESTOQUE ********")
            print("                 MENU DE OPÇÕES")
            print("[01] - Cadastrar Clientes")
            print("[02] - Cadastrar Produtos")
            print("[03] - Mostrar Clientes Cadastrados")
            print("[04] - Mostrar Produtos Cadastrados")
            print("[05] - Cadastrar Venda")
            print("[06] - Mostrar todas as vendas Cadastradas")
            print("[07] - Consultas")
            print("[08] - SAIR")
            self.op = int(input("Digite uma opção: "))                  
            
            if self.op == 1:
                cliente.CadastrarClientes() # CADASTRO DE CLIENTES ok
            elif self.op == 2:
                produto.CadastrarProdutos() # CADASTRO DE PRODUTOS ok
            elif self.op == 3:
                cliente.MostrarClientesCadastrados() # LISTA OS CLIENTES CADASTRADOS ok
            elif self.op == 4:
                produto.MostrarProdutosCadastrados() # LISTA OS PRODUTOS CADASTRADOS NO SISTEMA ok
            elif self.op == 5:
                venda.CadastrarVendas() # OK CADASTRO DE VENDAS
            elif self.op == 6:
                venda.MostrarVendas() # OK LISTAR TODAS AS VENDAS FEITAS NA LOJA
            elif self.op == 7:
                consulta.MenuConsultas() 
            elif self.op == 8:
                x = True
            else:
                input("Codigo inválido...Tente novamente")
                
                
MenuOb = Menu()
MenuOb.MenuPrincipal()
