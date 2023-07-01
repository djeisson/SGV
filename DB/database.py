import sqlite3

class sqlite_db:
    def  __init__(self, banco = None):
        self.conn = None
        self.cursor = None
        if banco:
            self.open(banco)

    def open(self, banco):
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
            print("conexão criada com sucesso!")
        except sqlite3.Error as e:
            print("Não foi possivel estabelecer conexão")

db = sqlite_db("SGV.DB")

"""
CREATE TABLE TBL_TICKET (
    ID_TICKET      INTEGER PRIMARY KEY AUTOINCREMENT,
    NUMERO_TICKET  NUMERIC NOT NULL,
    VALOR_TICKET   NUMERIC NOT NULL,
    CLIENTE_TICKET TEXT
);
CREATE TABLE TBL_USUARIOS (
    ID            INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME_USUARIO  TEXT    NOT NULL,
    USUARIO       TEXT    NOT NULL,
    CPF_USUARIO   NUMERIC NOT NULL,
    SENHA_USUARIO TEXT    NOT NULL
);
CREATE TABLE TBL_CAD_PRODUTOS (
    ID_PRODUTO          INTEGER PRIMARY KEY AUTOINCREMENT,
    DESCRIÇÃO           TEXT    NOT NULL,
    CUSTO_PRODUTO       NUMERIC NOT NULL,
    VALOR_VENDA_PRODUTO NUMERIC NOT NULL,
    QUANTIDADE_ESTOQUE  NUMERIC NOT NULL,
    UNIDADE_PRODUTO     TEXT    NOT NULL,
    GRUPO               TEXT    NOT NULL,
    SUBGRUPO            TEXT    NOT NULL
);

"""

