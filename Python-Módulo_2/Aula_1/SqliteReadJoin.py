import sqlite3
# Criar uma conexão com o banco de dados
conn = sqlite3.connect('mydatabase.db')
# Buscar os dados na tabela
cursor = conn.execute("SELECT stocks.date, stocks.act, stocks.qty, \
                      stocks.price,stocks.symbol,companies.symbol, "
                      "companies.name \
                      FROM stocks \
                      INNER JOIN companies ON stocks.symbol=companies.symbol")
# Iterar sobre os dados e exibi-los
for row in cursor:
    print(row)
# Fechar a conexão com o banco de dados
conn.close()
