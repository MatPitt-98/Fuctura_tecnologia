import sqlite3
# Criar uma conexão com o banco de dados
conn = sqlite3.connect('mydatabase.db')
# Inserir dados na tabela
conn.execute("INSERT INTO stocks VALUES ('2024-09-29', 'BUY', 'RHAT', "
             "100, 35.14)")
conn.execute("INSERT INTO stocks VALUES ('2024-03-28', 'BUY', 'IBM', 1000, "
             "45.00)")
conn.execute("INSERT INTO stocks VALUES ('2024-04-06', 'SELL', 'IBM', 500, "
             "53.00)")
# Salvar as alterações
conn.commit()
# Fechar a conexão com o banco de dados
conn.close()
