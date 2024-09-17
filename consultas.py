import os
from database import db
from clientes import Clientes
from produtos import Produtos


class Consultas(db):
    def __init__(self):
        super().__init__()
        self.op = None
        self.cod_cli = ''
        self.cod = None
    
    def MenuConsultas(self):
        x = False
        while not x:
            os.system("cls")
            print("******** SISTEMA DE GERENCIAMENTO DE ESTOQUE ********")
            print("MENU DE OPÇÕES")
            print("[07] - CONSULTAS")
            print("01. CLIENTES")
            print("02. PRODUTOS")
            print("03. VENDAS")
            print("04. VOLTAR")
            self.op = int(input("Digite uma opção: "))
            
            if self.op == 1:
                self.ClientesConsulta()
            elif self.op == 2:
                self.ProdutosConsulta()
            elif self.op == 3:
                input("A se desenvolver")
            elif self.op == 4:
                x = True
                return
            else:
                input("Código inválido...Tente novamente")
    
    
    def ClientesConsulta(self): # PARA REALIZAR UMA CONSULTA A PARTIR DE UM CLIENTE 
        cliente = Clientes() # CRIAÇÃO DO OBJETO
        os.system("cls")
        print("[07] - CONSULTAS -> [01] CLIENTES")
        y = False # EXECEÇÕES
        while not y:
            cod_cli = int(input("Digite o codigo do cliente (OBS: Digite 3 para ver os clientes cadastrados): "))
            if cod_cli == 3:
                cliente.MostrarClientesCadastrados()
            else:
                y = True
        # FAZER A BUSCA NO BANCO DE DADOS   
        cliente_dados = self.BuscarCliente(cod_cli)
        
        # MOSTAR OS DADOS NA TELA PARA O USUÁRIO
        if cliente_dados:
            print("VERIFICAR DADOS")
            cod_cliente, nome, email, telefone, cpf, situacao = cliente_dados # Criação de uma tupla para armazenar os dados 
            print(f"Codigo do cliente: {cod_cliente}")
            print(f"Nome: {nome}")
            print(f"Email: {email}")
            print(f"Telefone: {telefone}")
            print(f"CPF: {cpf}")
            print(f"Situação: {situacao}")
            
            # EDITAR OS DADOS
            print("\nEDITAR DADOS -> [01] - NOME # [02] - EMAIL # [03] - TELEFONE # [04] - CPF # [05] - SITUAÇÃO")
            self.cod = int(input("DIgite uma opção para editar um dado: "))
            cliente.EditarDadosCliente(self.cod, cliente_dados) # chama o método que irá editar os dados
            
        else:
            input("cliente não encontrado..")
            return
        
            
    def ProdutosConsulta(self): # MODIFICAR DADOS DE UM PRODUTO OU BUSCA
        produto = Produtos() # OBJETO CRIADO
        os.system("cls")
        print("[07] - CONSULTAS -> [02] PRODUTOS")
        z = False
        while not z:
            cod_produto = int(input("Digite o código do produto (Digite 4 para ver os produtos cadastrados): "))
            if(cod_produto == 4):
                produto.MostrarProdutosCadastrados()
            else:
                z = True
        
        # FAZER A BUSCA NO BANCO
        produto_encontrado = self.BuscarProduto(cod_produto)
        if produto_encontrado:
            print("VERIFICAR DADOS")
            cod_produto, marca, nome_produto, quantidade_estoque, valor_unit = produto_encontrado
            print(f"CÓDIGO: {cod_produto}")
            print(f"MARCA: {marca}")
            print(f"NOME: {nome_produto}")
            print(f"QUANTIDADE: {quantidade_estoque}")
            print(f"VALOR UNITÁRIO : R$ {valor_unit}")

        # EDITAR OS DADOS
            print("\nEDITAR DADOS -> [01] - MARCA # [02] - NOME # [03] - QUANTIDADE # [04] - VALOR UNITÁRIO")
            self.cod = int(input("Digite uma opção para editar um dado: "))
            produto.EditarDadosProduto(self.cod, produto_encontrado) # chama o método que irá editar os dados
            
        else:
            input("cliente não encontrado..")
            return
                
            