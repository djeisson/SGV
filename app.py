#Bibliotecas
import sys, os
from PySide6.QtWidgets import QApplication, QWidgetAction
from PySide6.QtWidgets import QMainWindow, QMessageBox, QDialog, QTableWidget,QTableWidgetItem,QPushButton
from PyQt5 import *
import sqlite3

#importando telas
from main_window import Ui_MainWindow
from cad_usuario_ui import Ui_cad_usuario
from login_ui import Ui_login
from cad_produtos_ui import Ui_cad_produtos
from about_ui import Ui_about
from cad_ticket_ui import Ui_cad_ticket
from about_ui import Ui_about
from venda_desktop_ui import Ui_venda_desktop
from cad_cliente_ui import Ui_cad_cliente
from usuarios_cadastrados_ui import Ui_usuarios_cadastrados
from produtos_cadastrados_ui import Ui_produtos_cadastrados
from clientes_cadastrados_ui import Ui_clientes_cadastrados
from gerar_ticket_ui import Ui_gerar_ticket

#tela de login
class login(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.verificacao_login)
        self.ui.pushButton_2.clicked.connect(self.fechar) 
        self.ui.pushButton.setDefault(True)

    def verificacao_login(self):
        login = self.ui.lineEdit_2.text()
        password = self.ui.lineEdit_3.text()

        # Conexão com o banco de dados
        conn = sqlite3.connect('SGV.DB')
        cursor = conn.cursor()

        # Consulta para verificar se o usuário existe
        cursor.execute("SELECT COUNT(*) FROM TBL_USUARIOS WHERE USUARIO = ? AND SENHA = ?", (login, password))
        result = cursor.fetchone()

        if result[0] > 0:
            self.window = MainWindow()
            self.window.show()
            self.close()
        else:
            QMessageBox.information(self, "Alerta de Login", "Usuário ou senha inválidos.")

        # Fechar a conexão com o banco de dados
        cursor.close()
        conn.close()
        
    def fechar(self):
        app.quit()
        print("tela de login fechada")
    
#tela principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Definir funções para os btn e line edit
        self.ui.actionCadastrar_Usuario.triggered.connect(self.abrir_cad_usuario)
        self.ui.actionCadastro_de_produtos.triggered.connect(self.abrir_cad_produtos)
        self.ui.actionSair.triggered.connect(self.fechar)
        self.ui.actionNovo_Ticket.triggered.connect(self.abrir_cad_ticket)
        self.ui.actionAbout.triggered.connect(self.abrir_about)
        self.ui.actionVenda_no_terminal.triggered.connect(self.nova_venda)
        self.ui.actionNovo_Cliente.triggered.connect(self.cad_cliente)
        self.ui.actionUsuarios_cadastrados.triggered.connect(self.usuarios_cadastrados)
        self.ui.actionEditar_produtos.triggered.connect(self.produtos_cadastrados)
        self.ui.actionEditar_Cliente.triggered.connect(self.cliente_cadastrados)
        self.ui.actionGerar_Qtd_Ticket.triggered.connect(self.gerar_ticket)
    

    #definindo funções para chamadas de tela a partir do Mainwindow
    def gerar_ticket(self):
        self.window = gerar_ticket()
        self.window.show()

    def cliente_cadastrados(self):
        self.window = clientes_cadastrados()
        self.window.show()

    def produtos_cadastrados(self):
        self.window = produtos_cadastrados()
        self.window.show()

    def usuarios_cadastrados(self):
        self.window = usuarios_cadastrados()
        self.window.show()

    def cad_cliente(self):
        self.window = cad_cliente()
        self.window.show()

    def nova_venda(self):
        self.window = venda_desktop()
        self.window.show()

    def abrir_about(self):
        self.window = about()
        self.window.show()

    def abrir_cad_ticket(self):
        self.window = cad_ticket()
        self.window.show()

    def abrir_cad_usuario(self):
        self.window = cad_usuario()
        self.window.show()

    def abrir_cad_produtos(self):
        self.window = cad_produtos()
        self.window.show()
        
    def fechar(self):
        app.quit()
        print("tela principal fechada")
    
class cad_usuario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_cad_usuario()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.fechar)
        self.ui.pushButton_3.clicked.connect(self.salvar_usuario)
        
        
    def salvar_usuario(self):
        nome_usuario = self.ui.lineEdit.text()
        usuario = self.ui.lineEdit_2.text()
        cpf = self.ui.lineEdit_4.text()
        senha = self.ui.lineEdit_3.text()
        tipo = self.ui.comboBox.currentText()
        """
        nome_usuario = nome_usuario.upper()
        usuario = usuario.upper()
        senha = senha.upper()
        tipo = tipo.upper()
        """  
        if nome_usuario.strip() == "":
            QMessageBox.information(self, "Alerta de Cadastro", "Nome invalido!\nVerifique.")
            print("Nome invalido, verifique")
        elif usuario is None or usuario.strip() == "":
            QMessageBox.information(self, "Alerta de Cadastro", "Usuario invalido!\nVerifique.")
            print("Usuario invalido, verifique")
        elif senha is None or senha.strip() == "":
            QMessageBox.information(self, "Alerta de Cadastro", "senha invalida!\nVerifique.")
            print( "senha invalida, verifique")
        elif cpf.isdigit() and len(cpf) == 11:#cpf.isnumeric
            print("CPF invalido, verifique")
            QMessageBox.information(self, "Alerta de Cadastro", "CPF invalido!\nVerifique.")
        else:
            conn = sqlite3.connect('SGV.DB')
            cursor = conn.cursor()
            #executar cursor
            cursor.execute("SELECT * FROM TBL_USUARIOS WHERE USUARIO = ?", (usuario,))
            result = cursor.fetchone()
            if result:
                print("Usuário já existe")
                QMessageBox.information(self, "Alerta de Cadastro", "Usuario ja cadastrado!\nVerifique.")
            else:
                cursor.execute("INSERT INTO TBL_USUARIOS (NOME_USUARIO, USUARIO, CPF, SENHA, TIPO) VALUES (?, ?, ?, ?, ?)", (nome_usuario, usuario, cpf, senha, tipo))
                # Salvar as alterações
                conn.commit()
                conn.close()
                print("usuario cadastrado com sucesso")
                QMessageBox.information(self, "Alerta de Cadastro", "Usuário cadastrado com sucesso!.")
                print("cadastro efetuado")
                self.fechar()
    
    def fechar(self):
        self.close()
    

class cad_produtos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_cad_produtos()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.salvar_produto)
        self.ui.pushButton_2.clicked.connect(self.fechar)

    def salvar_produto(self):
        descricao = self.ui.lineEdit.text()
        custo = self.ui.lineEdit_2.text()
        quantidade = self.ui.lineEdit_5.text()
        v_venda = self.ui.lineEdit_4.text()
        unidade = self.ui.comboBox.currentText()
        grupo = self.ui.comboBox_2.currentText()
        subgrupo = self.ui.comboBox_3.currentText()
        #conexão com banco
        conn = sqlite3.connect('SGV.DB')
        cursor = conn.cursor()
        #executar cursor
        cursor.execute("INSERT INTO TBL_CAD_PRODUTOS (DESCRIÇÃO, CUSTO_PRODUTO, VALOR_VENDA_PRODUTO, QUANTIDADE_ESTOQUE, UNIDADE_PRODUTO, GRUPO, SUBGRUPO) VALUES (?, ?, ?, ?, ?, ?, ?)", (descricao, custo, v_venda, quantidade, unidade, grupo, subgrupo))
        # Salvar as alterações
        conn.commit()
        conn.close()
        QMessageBox.information(self, "Alerta de Cadastro", "Produto cadastrado com sucesso!.")
        print("cadastro efetuado")
        self.fechar()

    def fechar(self):
        self.close()
        print("tela de cadastro de produtos fechada")

class about(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_about()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.fechar)

    def fechar(self):
        self.close()
        print("tela about fechada")

class usuarios_cadastrados(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_usuarios_cadastrados()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.listar_usuarios)
        self.ui.pushButton_3.clicked.connect(self.fechar)
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(['ID', 'Nome', 'Usuário', 'CPF', 'TIPO'])
    
    def listar_usuarios(self):
        conn = sqlite3.connect('SGV.DB')
        cursor = conn.cursor()

        # Executar consulta para obter os usuários
        cursor.execute('SELECT ID, NOME_USUARIO, USUARIO, CPF, TIPO FROM TBL_USUARIOS')
        users = cursor.fetchall()
        cursor.close()
        conn.close()

        # Limpar a tabela
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(len(users))
        
        for row, user in enumerate(users):
            # Adicionar os dados do usuário na QTableWidget
            for col, data in enumerate(user):
                item = QTableWidgetItem(str(data))
                self.ui.tableWidget.setItem(row, col, item)
        
        print("listagem bem sucedida")

    def fechar(self):
        self.close()
        print("tela about fechada")

class cad_ticket(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_cad_ticket()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.cadastrar_ticket)
        self.ui.pushButton_2.clicked.connect(self.fechar)

    def cadastrar_ticket(self):
        numero = self.ui.lineEdit.text()
        valor = self.ui.lineEdit_2.text()
        cliente = self.ui.comboBox.currentText()

        # Verificar se o ticket já existe
        conn = sqlite3.connect('SGV.DB')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM TBL_TICKET WHERE NUMERO_TICKET = ? AND CLIENTE_TICKET = ?", (numero, cliente))
        existing_ticket = cursor.fetchone()

        if existing_ticket:
            QMessageBox.warning(self, "Alerta de Cadastro", "O ticket já existe para esse cliente.")
        else:
            # Inserir o novo ticket no banco de dados
            cursor.execute("INSERT INTO TBL_TICKET (NUMERO_TICKET, VALOR_TICKET, CLIENTE_TICKET) VALUES (?, ?, ?)", (numero, valor, cliente))
            conn.commit()
            QMessageBox.information(self, "Alerta de Cadastro", "Ticket cadastrado com sucesso!")

        conn.close()
        self.fechar()

    def fechar(self):
        self.close()
        print("tela de cadastro de ticket fechada")

class venda_desktop(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_venda_desktop()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.salvar)
        self.ui.pushButton_2.clicked.connect(self.fechar)
        self.ui.pushButton_3.clicked.connect(self.buscar_produtos)
    
    def buscar_produtos(self):
        print("Buscando produtos")

    def salvar(self):
        print("salvar")

    def fechar(self):
        print("tela de vendas fechada")
        self.close()

class cad_cliente(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_cad_cliente()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.salvar)
        self.ui.pushButton_2.clicked.connect(self.fechar)

    def salvar(self):
        nome =self.ui.lineEdit.text()
        cpf =self.ui.lineEdit_2.text()
        email =self.ui.lineEdit_3.text()
        data_nasc = self.ui.dateEdit.text()
        uf = self.ui.comboBox.currentText()
        ticket = self.ui.lineEdit_4.text()

        conn = sqlite3.connect('SGV.DB')
        cursor = conn.cursor()
        #executar cursor
        cursor.execute("INSERT INTO TBL_CLIENTE (NOME, CPF, EMAIL, NASCIMENTO, UF,TICKET) VALUES (?, ?, ?, ?, ?, ?)", (nome, cpf, email, data_nasc, uf, ticket))
        # Salvar as alterações
        conn.commit()
        conn.close()
        QMessageBox.information(self, "Alerta de Cadastro", "Cliente cadastrado com sucesso!.")
        print("cadastro efetuado")
        self.fechar()
        print("salvar")

    def fechar(self):
        print("tela de cadastro de clientes fechada")
        self.close()

class produtos_cadastrados(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_produtos_cadastrados()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.listar_produtos)
        self.ui.pushButton_2.clicked.connect(self.fechar)
        self.ui.tableWidget.setColumnCount(8)
        self.ui.tableWidget.setHorizontalHeaderLabels(['ID_PRODUTO', 'DESCRIÇÃO', 'CUSTO_PRODUTO', 'VALOR_VENDA_PRODUTO', 'QUANTIDADE_ESTOQUE', 'UNIDADE_PRODUTO', 'GRUPO', 'SUBGRUPO'])

    def listar_produtos(self):
        conn = sqlite3.connect('SGV.DB')
        cursor = conn.cursor()

        # Executar consulta para obter os usuários
        cursor.execute('SELECT ID_PRODUTO, DESCRIÇÃO, CUSTO_PRODUTO, VALOR_VENDA_PRODUTO, QUANTIDADE_ESTOQUE, UNIDADE_PRODUTO, GRUPO, SUBGRUPO FROM TBL_CAD_PRODUTOS')
        users = cursor.fetchall()
        cursor.close()
        conn.close()

        # Limpar a tabela
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(len(users))
        
        for row, user in enumerate(users):
            # Adicionar os dados do usuário na QTableWidget
            for col, data in enumerate(user):
                item = QTableWidgetItem(str(data))
                self.ui.tableWidget.setItem(row, col, item)
        
        print("listagem bem sucedida")


    def fechar(self):
        print("tela de produtos cadastrados fechada")
        self.close()

class clientes_cadastrados(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_clientes_cadastrados()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.listar_produtos)
        self.ui.pushButton_3.clicked.connect(self.fechar)
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(['ID', 'NOME', 'CPF', 'EMAIL', 'NASCIMENTO', 'UF', 'TICKET'])

    def listar_produtos(self):
        conn = sqlite3.connect('SGV.DB')
        cursor = conn.cursor()

        # Executar consulta para obter os usuários
        cursor.execute('SELECT ID, NOME, CPF, EMAIL, NASCIMENTO, UF, TICKET FROM TBL_CLIENTE')
        users = cursor.fetchall()
        cursor.close()
        conn.close()

        # Limpar a tabela
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(len(users))
        
        for row, user in enumerate(users):
            # Adicionar os dados do usuário na QTableWidget
            for col, data in enumerate(user):
                item = QTableWidgetItem(str(data))
                self.ui.tableWidget.setItem(row, col, item)
        
        print("listagem bem sucedida")


    def fechar(self):
        print("tela de produtos cadastrados fechada")
        self.close()

class gerar_ticket(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_gerar_ticket()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.fechar)
        self.ui.pushButton.clicked.connect(self.abrir_confirmacao)
        
    def abrir_confirmacao(self):
        qtd = self.ui.lineEdit.text()
        qtd = int(qtd)
        reply = QMessageBox.question(self, "Alerta de Cadastro", "Deseja cadastrar os tickets?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            pass
        else:
            self.fechar()
        conn = sqlite3.connect('SGV.DB')
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(NUMERO_TICKET) FROM TBL_TICKET")
        result = cursor.fetchone()
        ultimo_numero = result[0]

        for i in range(qtd):
            ultimo_numero = result[0] if result[0] is not None else 0
            numero_ticket = ultimo_numero + i + 1
            cursor.execute("INSERT INTO TBL_TICKET (NUMERO_TICKET) VALUES (?)", (numero_ticket,))
        
        conn.commit()
        conn.close()
        QMessageBox.information(self, "Alerta de Cadastro", f"{qtd} Tickets cadastrados com sucesso!.")
        print("cadastro efetuado")
        self.close()
    def fechar(self):
        print("tela de ticket fechada")
        self.close()

app = QApplication(sys.argv)
window = login()
window.show()
sys.exit(app.exec())