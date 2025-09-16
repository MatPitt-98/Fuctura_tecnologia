import sqlite3
# Criar uma conexão com o banco de dados
conn = sqlite3.connect('mydatabase.db')
# Criar uma tabela
conn.execute('''CREATE TABLE companies (symbol text, name text, sector text)''')
# Inserir dados na tabela
conn.execute(
    "INSERT INTO companies VALUES ('RHAT', 'Red Hat Inc.', 'Software')")
conn.execute("INSERT INTO companies VALUES ('IBM', 'Int. Bus. Mach. Corp.', "
             "'Technology')")
conn.execute("INSERT INTO companies VALUES ('AAPL', 'Aple Inc.', 'Technology')")
# Salvar as alterações
conn.commit()
# Fechar a conexão com o banco de dados
conn.close()
