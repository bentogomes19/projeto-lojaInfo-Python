import os
import random
from database import db

class Produtos(db): # CLASSE FILHA Produtos() -> CLASSE MÃE db()
    def __init__(self): # MÉTODO CONSTRUTOR ONDE OS ATRIBUTOS SÃO RECONHECIDOS SOMENTE PELA CLASSE
        super(Produtos, self).__init__()
        self.cod_produto = None
        self.nome = ''
        self.marca = ''
        self.quantidade = None
        self.valor = None
        
    # MÉTODO PARA CADASTRAR UM PRODUTO
    def CadastrarProdutos(self):
        self.ConnectDB() # CONEXÃO AO BANCO DE DADOS
        self.TabelaProdutos() # CRIAÇÃO DA TABELA PRODUTOS
        
        os.system("cls")
        print("BEM-VINDO AO CADASTRO DE PRODUTOS DA LOJA")
        
        # INSERINDO OS DADOS
        self.cod_produto = random.randint(1000, 9999) # GERANDO O CÓDIGO DO PRODUTO ALEATÓRIAMENTE NO SISTEMA
        self.marca = str(input("Digite o marca do produto: "))
        self.nome = str(input("Digite o nome do produto: "))
        self.quantidade = int(input("Informe a quantidade de itens armazenados: "))
        self.valor = float(input("Digite o valor unitário (R$): "))
        
        # CONFIRMANDO OS DADOS
        print("\n\n CONFIRME SEUS DADOS")
        
        print(f"MARCA: {self.marca}")
        print(f"NOME: {self.nome}")
        print(f"QUANTIDADE: {self.quantidade}")
        print(f"VALOR UNITÁRIO (R$): {self.valor}")
        
        confirmar = input("Deseja confirmar seus dados [S][N]: ").upper()
        if(confirmar == 'S'):
            self.InsertDataTabelaProdutos(self.cod_produto, self.marca, self.nome, self.quantidade, self.valor)
            input("Dados cadastrados com sucesso...")
        else:
            input("Seus dados serão descartados...Pressione Enter para continuar...")
            self.__init__()
            return
    
    # MÉTODO PARA MOSTRAR OS PRODUTOS CADASTRADOS
    def MostrarProdutosCadastrados(self):
        # BUSCAR OS DADOS NO BANCO
        self.QueryTabelaProdutos()
        if not self.linhas:
            input("Não há produtos cadastrados....")
            return
        else:
            # SOMAR DADOS DO ESTOUQE -> QUANTIDADE E VALOR
            soma_estoque = 0
            soma_valor = 0
            soma_produtos = 0
            os.system("cls") # os.system('clear')
            # MOSTAR OS PRODUTOS CADASTRADOS FORMATADOS NA TABELA NO TERMINAL
            print("\n\n\t\t\tLISTA DE PRODUTOS CADASTRADOS NO SISTEMA DA LOJA")
            print("-" * 110) 
            print(f"{'CODIGO':<19} {'MARCA':<25} {'NOME':<27} {'QUANTIDADE':<20} {'VALOR UNIT (R$)':<11}")
            print("-" * 110)
            for dado in self.linhas:
                cod_produto, marca, nome_produto, quantidade_estoque, valor_unit = dado
                print(f"{cod_produto:<14} {marca:<21} {nome_produto:<41} {quantidade_estoque:<18} {valor_unit:<16}")
                soma_estoque += quantidade_estoque
                soma_valor += valor_unit
                soma_produtos += 1
                
            print(f"\n\nESTOQUE TOTAL: {soma_estoque}")
            print(f'\nVALOR TOTAL DO ESTOQUE: R$ {soma_valor}')
            print(f'TOTAL DE PRODUTOS: {soma_produtos}')
            input("Pressione Enter para continuar...")
            
        
    # MÉTODO PARA EDITAR OS DADOS DO PRODUTO
    def EditarDadosProduto(self, codigo, produto):
        cod_produto, marca, nome, quantidade_estoque, valor_unit = produto
        if (codigo == 1):
            self.marca = str(input("Digite a marca: "))
            self.UpdateMarcaTabelaProdutos(self.marca, cod_produto)
        elif (codigo == 2):
            self.nome = str(input("Digite o nome: "))
            self.UpdateNomeTabelaProdutos(self.nome, cod_produto)
        elif (codigo == 3):
            self.quantidade = int(input("Digite a quantidade no estoque: "))
            self.UpdateQuantidadeTabelaProdutos(self.quantidade, cod_produto)
        elif (codigo == 4):
            self.valor_unit = float(input("Digite o valor unitário R$: "))
            self.UpdateValorUnitTabelaProdutos(self.valor_unit, cod_produto)
            
        input("Dados alterados com sucesso...")
            