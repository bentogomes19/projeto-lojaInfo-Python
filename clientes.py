import os
import random
from database import db

class Clientes(db): # CLASSE MÃE (db) -> CLASSE FILHA Clientes
    def __init__(self):
        super().__init__() # Importando o construtor da classe db 
        self.nome = ''
        self.cod_cliente = None
        self.email = ''
        self.telefone = ''
        self.cpf = ''
        self.situacao = 'INATIVO'
    
    def CadastrarClientes(self): # MÉTODO PARA CADASTRAR UM CLIENTE
        self.ConnectDB() # Conecta ao banco de dados
        self.TabelaCLientes()
        
        os.system("clear") # LIMPA A TELA 
        print("BEM-VINDO AO CADASTRO DE CLIENTES DA LOJA")
        # INSERÇÃO DOS DADOS NOME, EMAIL, TELEFONE, CPF
        
        self.nome = str(input("Informe o nome: "))
        self.email = str(input("Informe o email: "))
        self.telefone = str(input("Digite o telefone: "))
        self.cpf = str(input("Digite o CPF: "))
        
        # GERANDO O CÓDIGO DO FUNCIONÁRIO
        self.cod_cliente = random.randint(1000,9999)
        # DEFININDO O PRIMEIRO CADASTRO COMO ATIVO
        self.situacao = 'ATIVO'
        # VERIFICAÇÃO DOS DADOS
        print("VERIFIQUE SEUS DADOS")
        print(f'Nome: {self.nome}')
        print(f'Email: {self.email}')
        print(f'Telefone: {self.telefone}')
        print(f'CPF: {self.cpf}')
        confirmar = input("Deseja confirmar estes dados [S][N]?: ").upper()
        
        if(confirmar == 'N'):
            input("Seus dados serão apagados...")
            self.__init__()
        else:
            # CHAMANDO O MÉTODO DA CLASSE db (InsertDataTabelaClientes) PARA A INSERÇÃO DOS DADOS NA TABELA CLIENTES
            self.InsertDataTabelaClientes(self.cod_cliente ,self.nome, self.email, self.telefone, self.cpf, self.situacao)
            input("Dados cadastrados com sucesso...Pressione enter para continar")
            
        self.DisconnectDB()
    
    def MostrarClientesCadastrados(self): # MOSTRAR TODOS OS CLIENTES CADASTRADOS
        self.QueryDataTabelaClientes() # CHAMA O MÉTODO PARA BUSCAR OS DADOS 
        if not self.linhas: # CASO NÃO TENHA CLIENTES CADASTRADOS
            input("Nenhum cliente cadastrado no sistema")
            return
        os.system("clear")
        # MOSTAR OS CLIENTES CADASTRADOS FORMATADOS NA TABELA NO TERMINAL
        print("\n\n\t\t\tLISTA DE CLIENTES CADASTRADOS NO SISTEMA DA LOJA")
        print("-" * 110) 
        print(f"{'CODIGO':<17} {'NOME':<22} {'EMAIL':<22} {'TELEFONE':<22} {'CPF':<11} {'SITUAÇÃO':<7}")
        print("-" * 110)
        for linha in self.linhas:
            cod_cliente, nome, email, telefone, cpf, situacao = linha
            print(f"{cod_cliente:<7} {nome:<28} {email:<25} {telefone:<18} {cpf:<20} {situacao:<10}")
        input()
        
    def EditarDadosCliente(self, opcao_consulta, dados_cliente):
        cod_cliente, nome, email, telefone, cpf, situacao = dados_cliente
        if opcao_consulta == 1:
            self.nome = str(input("Digite o nome: "))
            self.UpdateNomeTabelaClientes(self.nome, cod_cliente)
            input("Dados alterados com sucesso...")
    
        
            

        
        