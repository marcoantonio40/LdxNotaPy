##landix
##marco
import sqlite3  # para o SQLite
con = sqlite3.connect('dadosPy.sqlite')

cursor = con.cursor()

cursor.execute("CREATE TABLE X (nome int)")
