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
        
        
    
    # PRODUTOS
    #
    #
    # PRODUTOS 
    
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
        
    def TabelaVendas(self):
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
        
    
        