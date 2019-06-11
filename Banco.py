##landix
##marco
import sqlite3 
import os.path

def Cria_Banco():
	if(os.path.exists('C:\csharp\Python\dadosPy.sqlite')):
		conn = sqlite3.connect('dadosPy.sqlite')
		return conn
	else:
		print("Banco de dados não existe!")

def Valida_Login(login, senha):
	con = Cria_Banco()
	cursor = con.cursor()
	cursor.execute("SELECT COUNT(*) FROM TUSUARIOS WHERE DSLOGIN = ? AND DSSENH = ?;",(login,senha))
	resultado = cursor.fetchmany(0)
	print(resultado)

Valida_Login("marco","12345")
