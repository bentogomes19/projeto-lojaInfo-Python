import os
from database import db
from clientes import Clientes


class Consultas(db):
    def __init__(self):
        super().__init__()
        self.op = None
        self.cod_cli = ''
        self.cod = None
    
    def MenuConsultas(self):
        x = False
        while not x:
            os.system("clear")
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
                input("A se desenvolver")
            elif self.op == 3:
                input("A se desenvolver")
            elif self.op == 4:
                x = True
                return
            else:
                input("Código inválido...Tente novamente")
    
    
    def ClientesConsulta(self):
        cliente = Clientes()
        os.system("clear")
        print("[07] - CONSULTAS -> [01] CLIENTES")
        y = False
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
            cod_cliente, nome, email, telefone, cpf, situacao = cliente_dados
            print(f"Codigo do cliente: {cod_cliente}")
            print(f"Nome: {nome}")
            print(f"Email: {email}")
            print(f"Telefone: {telefone}")
            print(f"CPF: {cpf}")
            print(f"Situação: {situacao}")
            
            # EDITAR OS DADOS
            
            print("\nEDITAR DADOS -> [01] - NOME # [02] - EMAIL # [03] - TELEFONE # [04] - CPF # [05] - SITUAÇÃO")
            self.cod = int(input("DIgite uma opção para editar um dado: "))
            cliente.EditarDadosCliente(self.cod, cliente_dados)
            
        else:
            input("cliente não encontrado..")
            return
        
            
            
                
            