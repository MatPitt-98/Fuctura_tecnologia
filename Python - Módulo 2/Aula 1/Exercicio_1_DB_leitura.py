import sqlite3

conn = sqlite3.connect('livro_x_escritor_x_editora.db')

cursor = conn.execute('SELECT * from livro')

for row in cursor:
    print(row)

conn.close()
