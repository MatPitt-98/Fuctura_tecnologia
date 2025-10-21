import sqlite3

conn = sqlite3.connect('livro_x_escritor_x_editora.db')
conn.execute('PRAGMA foreign_keys = ON')

conn.execute('INSERT INTO escritor (nome_do_escritor) VALUES (?)',
             ('Charles Dickens',))
conn.execute('INSERT INTO editora (nome_da_editora) VALUES (?)',
             ('Bradbury & Evans',))

escritor_id = conn.execute(
    'SELECT id FROM escritor WHERE nome_do_escritor = ?', ('Charles Dickens',)).fetchone()[0]
editora_id = conn.execute(
    'SELECT id FROM editora WHERE nome_da_editora = ?', ('Bradbury & Evans',)).fetchone()[0]

conn.execute('INSERT INTO livro (titulo, escritor_id, editora_id) VALUES (?, ?, ?)',
             ('A Tale of Two Cities', escritor_id, editora_id))

conn.commit()
conn.close()
