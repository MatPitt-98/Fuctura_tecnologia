import sqlite3

conn = sqlite3.connect('livro_x_escritor_x_editora.db')
conn.execute('PRAGMA foreign_keys = ON')

conn.execute(
    '''CREATE TABLE IF NOT EXISTS livro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    escritor_id INTEGER,
    editora_id INTEGER,
    FOREIGN KEY (escritor_id) REFERENCES escritor(id),
    FOREIGN KEY (editora_id) REFERENCES editora(id)
    )''')

conn.execute(
    '''CREATE TABLE IF NOT EXISTS escritor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_do_escritor TEXT NOT NULL
    )''')

conn.execute('''CREATE TABLE IF NOT EXISTS editora (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_da_editora TEXT NOT NULL
            )''')

conn.commit()
conn.close()
