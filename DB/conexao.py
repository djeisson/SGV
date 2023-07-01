import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('SGV.DB')

# Criar um cursor
cursor = conn.cursor()

# Executar comandos SQL

# Exemplo: inserir dados na tabela
cursor.execute("INSERT INTO TBL_USUARIOS (NOME_USUARIO, USUARIO,CPF_USUARIO,SENHA_USUARIO) VALUES (F"{},{},{},{}")", ('João', 'joao@example.com'))

# Salvar as alterações
conn.commit()

# Fechar a conexão
conn.close()