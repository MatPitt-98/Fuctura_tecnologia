import sqlite3

# Criar uma conexão com o banco de dados
conn = sqlite3.connect('mydatabase.db')

# Inserir dados na tabela
conn.execute("UPDATE stocks SET price = 53.00 WHERE symbol = 'RHAT'")

# Salvar as alterações
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()
