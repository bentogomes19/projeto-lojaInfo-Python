import sqlite3

class db():
    def __init__(self):
        self.db = None # conecta ao banco
        self.cursor = None # realiza COMANDOS SQL
        self.linhas = None
        self.linha = None
        
    def ConnectDB(self): # MÉTODO PARA CONECTAR AO BANCO DE DADOS
        self.db = sqlite3.connect("DataBaseLoja.db")
        # Criar cursor
        self.cursor = self.db.cursor()
    
    def DisconnectDB(self): # MÉTODO PARA DISCONECTAR AO BANCO DE DADOS
        if self.db:
            self.db.close()
            
    # CLIENTES
    #
    #
    # CLIENTES

    def TabelaCLientes(self): # CRIAR A TABELA CLIENTES NO BANCO DE DADOS
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes (
            cod_cliente INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL,
            cpf TEXT NOT NULL,
            situacao TEXT NOT NULL,
            data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP   
            )
            ''')
        self.db.commit()
    
    # METÓDO InsertDataTabelaClientes -> Insere os dados no banco 
    def InsertDataTabelaClientes(self, cod_cliente, nome, email, telefone, cpf, situacao):
        self.cursor.execute('''INSERT INTO Clientes (cod_cliente, nome, email, telefone, cpf, situacao) VALUES (
            ?, ?, ?, ?, ?, ?)''', (cod_cliente, nome, email, telefone, cpf, situacao))
        self.db.commit()
        
    # MÉTODO ALTERAR DADO SOMENTE DO NOME 
    def UpdateNomeTabelaClientes(self, novo_nome, cod_cliente):
        self.ConnectDB()
        self.cursor.execute('''UPDATE Clientes SET nome = ? WHERE cod_cliente = ?''',   (novo_nome, cod_cliente))
        self.db.commit()
        
    # MÉTODO ALTERAR DADO SOMENTE DO EMAIL
    def UpdateEmailTabelaClientes(self, novo_email, cod_cliente):
        self.ConnectDB()
        self.cursor.execute('''UPDATE Clientes SET email = ? WHERE cod_cliente = ?''', (novo_email, cod_cliente))
        self.db.commit()
        
    # MÉTODO ALTERAR DADO SOMENTE DO TELEFONE
    def UpdateTelTabelaClientes(self, novo_tel, cod_cliente):
        self.ConnectDB()
        self.cursor.execute('''UPDATE Clientes SET telefone = ? WHERE cod_cliente = ?''', (novo_tel, cod_cliente))
        self.db.commit()
    
    # MÉTODO ALTERAR DADO SOMENTE DO CPF
    def UpdateCPF_TabelaClientes(self, novo_cpf, cod_cliente):
        self.ConnectDB()
        self.cursor.execute('''UPDATE Clientes SET cpf = ? WHERE cod_cliente = ?''', (novo_cpf, cod_cliente))
        self.db.commit()

    # MÉTODO ALTERAR DADO SOMENTE DA SITUAÇÃO
    def UpdateSituacaoTabelaClientes(self, nova_situacao, cod_cliente):
        self.ConnectDB()
        self.cursor.execute('''UPDATE Clientes SET situacao = ? WHERE cod_cliente = ?''', (nova_situacao, cod_cliente))
        self.db.commit() 

    # MÉTODO QueryDataTabelaClientes -> Faz uma query no banco de dados 
    def QueryDataTabelaClientes(self):
        self.ConnectDB()
        self.cursor.execute("SELECT cod_cliente, nome, email, telefone, cpf, situacao FROM Clientes")       
        self.linhas = self.cursor.fetchall()

    # MÉTODO BuscarCLiente() -> Faz uma busca em um cliente específico
    def BuscarCliente(self, cliente_codigo):    
        self.ConnectDB() # Conecta ao banco
        self.cursor.execute("SELECT cod_cliente, nome, email, telefone, cpf, situacao FROM Clientes WHERE cod_cliente = ?", (cliente_codigo,))
        self.linha = self.cursor.fetchone() # BUSCA UMA INSTÂNCIA EM ESPECÍFICO    
        # Fazer a busca do cliente
        if self.linha:
            return self.linha   
        else:
            return None
        
    def BuscarCliente2(self, cliente_codigo):    
        self.ConnectDB() # Conecta ao banco
        self.cursor.execute("SELECT cod_cliente FROM Clientes WHERE cod_cliente = ?", (cliente_codigo,))
        self.linha = self.cursor.fetchone() # BUSCA UMA INSTÂNCIA EM ESPECÍFICO    
        # Fazer a busca do cliente
        if self.linha:
            return self.linha[0] # É UMA TUPLA E O CODIGO ESTA NO PRIMEIRO INDICE 
        else:
            return None
    
    def ExcluirCliente(self, cliente_codigo):
        self.ConnectDB()
        self.cursor.execute("DELETE FROM Clientes WHERE cod_cliente = ?", (cliente_codigo,))
        self.db.commit()
            
    # PRODUTOS
    #
    #
    # PRODUTOS 
    
    # MÉTODO PARA GERAR A TABELA DOS PRODUTOS
    def TabelaProdutos(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Produtos (
            cod_produto INTEGER PRIMARY KEY,
            marca TEXT NOT NULL,
            nome_produto TEXT NOT NULL,
            quantidade_estoque INTEGER NOT NULL,
            valor_unit REAL NOT NULL,
            data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            ''')
        
    # MÉTODO PARA INSERIR OS DADOS NA TABELA PRODUTOS
    def InsertDataTabelaProdutos(self, cod_produto, marca, nome_produto, quantidade_estoque, valor_unit):
        self.ConnectDB()
        self.cursor.execute('''INSERT INTO Produtos (cod_produto, marca, nome_produto, quantidade_estoque, valor_unit) 
                            VALUES (?,?,?,?,?)''', (cod_produto, marca, nome_produto, quantidade_estoque, valor_unit))
        self.db.commit()
        
    # MÉTODO PARA BUSCAR TODOS OS DADOS CADASTRADOS NA TABELA PRODUTOS
    def QueryTabelaProdutos(self):
        self.ConnectDB()
        self.cursor.execute('''SELECT cod_produto, marca, nome_produto, quantidade_estoque, valor_unit FROM Produtos''')
        self.linhas = self.cursor.fetchall()
    
    # MÉTODO PARA BUSCAR UM PRODUTO ESPECÍFICO NA TABLEA PRODUTOS
    def BuscarProduto(self, cod_produto):
        self.ConnectDB()
        self.cursor.execute("SELECT cod_produto, marca, nome_produto, quantidade_estoque, valor_unit FROM Produtos WHERE cod_produto = ?", (cod_produto,))
        self.linha = self.cursor.fetchone()
        if self.linha:
            return self.linha
        else:
            return None
        
    
    # MÉTODO PARA MODIFICAR OS DADOS DA MARCA DO PRODUTO NA TABELA PRODUTOS
    def UpdateMarcaTabelaProdutos(self, marca, cod_produto):
        self.ConnectDB()
        self.cursor.execute('''UPDATE Produtos SET marca = ? WHERE cod_produto = ?''', (marca, cod_produto))
        self.db.commit()
        
    # MÉTODO PARA MODIFICAR OS DADOS DO NOME DO PRODUTO NA TABELA PRODUTOS
    def UpdateNomeTabelaProdutos(self, nome, cod_produto):
        self.ConnectDB()
        self.cursor.execute('''UPDATE Produtos SET nome_produto = ? WHERE cod_produto = ?''', (nome, cod_produto))
        self.db.commit()
        
    # MÉTODO PARA ALTERAR A QUANTIDADE DE ITENS DE UM PRODUTO NA TABELA PRODUTOS
    def UpdateQuantidadeTabelaProdutos(self, quantidade, cod_produto):
        self.ConnectDB()
        self.cursor.execute('''UPDATE Produtos SET quantidade_estoque = ? WHERE cod_produto = ?''', (quantidade, cod_produto))
        self.db.commit()
        
    # MÉTODO PARA ALTERAR O VALOR UNITÁRIO DE UM PRODUTO NA TABELA PRODUTOS
    def UpdateValorUnitTabelaProdutos(self, valor_unitario, cod_produto):
        self.ConnectDB()
        self.cursor.execute('''UPDATE Produtos SET valor_unit = ? WHERE cod_produto = ?''', (valor_unitario, cod_produto))
        self.db.commit()
        
    # MÉTODO PARA EXCLUIR UM PRODUTO DA TABELA PRODUTOS
    def ExcluirProduto(self, cod_produto):
        self.ConnectDB()
        self.cursor.execute("DELETE FROM Produtos WHERE cod_produto = ?", (cod_produto,))
        self.db.commit()
        
    # VENDAS
    #
    #
    # VENDAS
        
    def TabelaVendas(self):
        self.ConnectDB()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Vendas (
            cod_venda INTEGER PRIMARY KEY,
            cod_cliente INTEGER,
            cod_produto INTEGER,
            quantidade INTEGER NOT NULL,
            valor_total REAL NOT NULL,
            data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (cod_cliente) REFERENCES Clientes(cod_cliente),
            FOREIGN KEY (cod_produto) REFERENCES Produtos(cod_produto)
            )
            ''')
        
    def InsertVendas(self, cod_venda, cod_cliente, cod_produto, quantidade, valor_total):
        self.ConnectDB()
        self.cursor.execute('''INSERT INTO Vendas (cod_venda, cod_cliente, cod_produto, quantidade, valor_total) VALUES (
                                ?,?,?,?,?)''', (cod_venda, cod_cliente, cod_produto, quantidade, valor_total))
        self.db.commit()
        
    # MÉTODO PARA BUSCAR TODOS AS VENDAS REALIZADAS NA TABELA VENDAS
    def QueryTabelaVendas(self):
        self.ConnectDB()
        self.cursor.execute('''SELECT cod_venda, cod_cliente, cod_produto, quantidade, valor_total FROM Vendas''')
        self.linhas = self.cursor.fetchall()
    
        