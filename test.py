import sqlite3

conn = sqlite3.connect('baseDonnees.db')
cur = conn.cursor()

cur.execute("CREATE TABLE LIVRES(id INT, titre TEXT, auteur TXT, ann_publi INT, note INT)")

conn.commit()

cur.close()
conn.close()
