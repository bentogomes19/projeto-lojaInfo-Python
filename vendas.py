import os
import time
import random
from database import db
from clientes import Clientes
from produtos import Produtos

class Vendas(db):
    def __init__(self):
        self.cliente = Clientes()
        self.produto = Produtos()
        self.TabelaVendas()
        
    
    def CadastrarVendas(self):
        os.system("cls")
        print("CADASTRAR UMA VENDA")
        
        # GERANDO CODIGO DA VENDA
        cod_venda = random.randint(1000, 9999)
        
        # MOSTRANDO A LISTA DE PRODUTOS E CLIENTES CADASTRADOS
        x = False
        while not x: # CLIENTE
            cod_cliente = int(input("Digite o codigo do cliente (Digite 3 para mostrar os Clientes cadastrados): "))
            if(cod_cliente == 3):
                
                self.cliente.MostrarClientesCadastrados()
                continue
            
            busca_cod_cli = self.cliente.BuscarCliente(cod_cliente)
                
            if busca_cod_cli is None:
                input("Codigo inválido tente...Novamente")
            else:
                x = True

        x = False
        while not x: # PRODUTO
            cod_produto = int(input("Digite o codigo do produto (Digite 4 para mostrar os Produtos cadastrados): "))
            if(cod_produto == 4):
                
                self.produto.MostrarProdutosCadastrados()
                continue
            
            busca_cod_produto = self.produto.BuscarProduto(cod_produto)
                
            if busca_cod_produto is None:
                input("Codigo inválido tente...Novamente") 
            else:
                x = True
                
        # INSERINDO OS DADOS
        cod_cliente, nome, email, telefone, cpf, situacao = busca_cod_cli
        cod_produto, marca, nome_produto, quantidade_estoque, valor_unit = busca_cod_produto # Dados da tupla
        qtd_estoque = quantidade_estoque
        x = False
        while not x:
            quantidade_usr = int(input("Informe a quantidade: "))
            if quantidade_usr > qtd_estoque:
                print('A quantidade informada é maior do que esta armazenado...')
                time.sleep(2)
            elif quantidade_estoque < 10:
                print('Estoque em baixa!!')
                time.sleep(1)
            elif quantidade_usr < 0:
                print("Entrada Inválida...Tente novamente")
                time.sleep(1)
            else:
                x = True
        
        valor_total = quantidade_usr * valor_unit
        atualiza_estoque = qtd_estoque - quantidade_usr
        print("\n\n**** NOTA FISCAL ****")
        print(f"Cliente: {nome:<10} ##### COD: {cod_cliente} ")
        print(f"-" * 50)
        print(f"Produto: {marca:<5} {nome_produto:<1}")
        print(f"-" * 50)
        print(f"Quantidade: {quantidade_usr}")
        print(f"-" * 50)
        print(f"Valor Unitário: R$ {valor_unit}")
        print(f"-" * 50)
        print(f"Valor Total a pagar: {valor_total}")
        print(f"-" * 50)
        input("Pressione Enter para continuar...")
        resposta_usr = str(input("Deseja confirmar os dados [S][N]?: ")).upper()
        
        if resposta_usr == 'S':
            
            # ARMAZENANDO NO BANCO DE DADOS 
            self.InsertVendas(cod_venda, cod_cliente, cod_produto, quantidade_usr, valor_total)
            self.UpdateQuantidadeTabelaProdutos(atualiza_estoque, cod_produto)
            print("Venda Feita com sucesso...")
            time.sleep(2)
        else:
            print("Excuindo seus dados...Aguarde")
            for x in range(3):
                print(f"{x+1}..")
                time.sleep(0.8)        
            return
        
    def MostrarVendas(self):
        # BUSCAR OS DADOS NO BANCO
        self.QueryTabelaVendas()
        if not self.linhas:
            input("Não há VENDAS cadastrados....")
            return
        else:
            # SOMAR AS VENDAS
            soma_vendas = 0
            os.system("cls") # os.system('clear')
            # MOSTAR OS PRODUTOS CADASTRADOS FORMATADOS NA TABELA NO TERMINAL
            print("\n\n\t\t\tHISTÓRICO DE VENDAS FEITAS NO SISTEMA DA LOJA")
            print("-" * 100) 
            print(f"{'CODIGO':<14} {'CLIENTE':<20} {'PRODUTO':<17} {'QUANTIDADE':<20} {'VALOR TOTAL (R$)':<11}")
            print("-" * 100)
            for dado in self.linhas:
                cod_venda, cod_cliente, cod_produto, quantidade, valor_total = dado
                print(f"{cod_venda:<14} {cod_cliente:<21} {cod_produto:<19} {quantidade:<18} {valor_total:<10}")
                soma_vendas += valor_total
                
            print(f'\nVALOR TOTAL EM VENDAS: R$ {soma_vendas}')
            input("Pressione Enter para continuar...")