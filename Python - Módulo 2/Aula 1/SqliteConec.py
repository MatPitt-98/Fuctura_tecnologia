import sqlite3
# Criar uma conexão com o banco de dados
conn = sqlite3.connect('mydatabase.db')

# Criar uma tabela
conn.execute('''CREATE TABLE stocks (date text, act text , 
             symbol text, qty real, price real)''')

# Salvar as alterações
conn.commit()
# Fechar a conexão com o banco de dados
conn.close()
