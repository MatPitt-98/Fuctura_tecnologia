import sqlite3

# Criar uma conexão com o banco de dados
conn = sqlite3.connect('mydatabase.db')
# Busca os dados na tabela
cursor = conn.execute("SELECT * FROM stocks")
# cursor = conn.execute("SELECT stocks.act FROM stocks WHERE symbol = 'RHAT'")
# cursor = conn.execute("SELECT * FROM stocks WHERE symbol = 'RHAT'")
# Iterar sobre os dados e exibi-los
for row in cursor:
    print(row)
# Fechar a conexão com o banco de dados
conn.close()
