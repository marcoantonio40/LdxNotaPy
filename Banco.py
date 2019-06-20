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
	x = resultado[0]
	if(x[0]==0):
		return False
	else:
		return True

def Ultimo_Cod_Usu():
	con = Cria_Banco()
	cursor = con.cursor()
	cursor.execute("SELECT MAX(CDUSU)+1 FROM TUSUARIOS;")
	resultado = cursor.fetchmany(0)
	x = resultado[0]
	return x[0]

		
def Insere_Usuario(codigo,nome, login, senha):
	con = Cria_Banco()
	cursor = con.cursor()
	#cursor.execute("INSERT INTO TUSUARIOS VALUES (?, ?, ?, ?);",(Ultimo_Cod_Usu(), nome, login, senha))
	
	query_Insert = '''INSERT INTO TUSUARIOS (CDUSU, DSNOME, DSLOGIN, DSSENH) VALUES (?, ?, ?, ?);'''
	query_Tuple = (codigo, nome, login, senha)
	cursor.execute(query_Insert, query_Tuple)
	cursor.lastrowid
	
	
	
	