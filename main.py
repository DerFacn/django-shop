import sqlite3 as sql

con = sql.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `test` (id INTEGER)")
    con.commit()
