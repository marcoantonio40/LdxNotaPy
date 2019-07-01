##landix
##marco
import sqlite3 
import os.path
import ctypes  

def Cria_Banco():
	if(os.path.exists('C:\csharp\Python\dadosPy.sqlite')):
		conn = sqlite3.connect('dadosPy.sqlite')
		return conn
	else:
		print("Banco de dados não existe!")

def Valida_Login(login, senha):
	senha_Crip = criptografar(senha)
	con = Cria_Banco()
	cursor = con.cursor()
	cursor.execute("SELECT COUNT(*) FROM TUSUARIOS WHERE DSLOGIN = ? AND DSSENH = ?;",(login,senha_Crip))
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

		
def Insere_Usuario(nome, login, senha):
	senha_Crip = criptografar(senha)
	con = Cria_Banco()
	cursor = con.cursor()
	if nome != "" and login != "" and senha != "":
		cursor.execute("INSERT INTO TUSUARIOS (CDUSU, DSNOME, DSLOGIN, DSSENH) VALUES (?, ?, ?, ?);",(Ultimo_Cod_Usu(), nome, login, senha_Crip))
		con.commit()
	else:
		ctypes.windll.user32.MessageBoxW(0, "Dados vazios", "Erro", 0)

		
def criptografar(senha):
	import hashlib
	hash_obj = hashlib.md5(senha.encode())
	return hash_obj.hexdigest()	

def Retorna_Codigo_Usuario(login,senha):
	senha_Crip = criptografar(senha)
	con = Cria_Banco()
	cursor = con.cursor()
	cursor.execute("SELECT CDUSU FROM TUSUARIOS WHERE DSLOGIN = ? AND DSSENH = ?;",(login,senha_Crip))
	resultado = cursor.fetchmany(0)
	return resultado[0]
	 	
	
def Notas_Usuario(usuario):
	con = Cria_Banco()
	cursor = con.cursor()
	cursor.execute("SELECT CDNOTA, CDUSU, DSTITU, DSNOTA, DTNOTA FROM TNOTAS WHERE CDUSU = ?;",(usuario))
	resultado = cursor.fetchmany(0)
	return resultado
	
def Quantas_Notas_Usuario(usuario):
	con = Cria_Banco()
	cursor = con.cursor()
	cursor.execute("SELECT COUNT(*) FROM TNOTAS WHERE CDUSU = ?;", (usuario))
	resultado = cursor.fetchmany(0)
	x = resultado[0]
	return x[0]

def Ultimo_Cod_Nota():
	con = Cria_Banco()
	cursor = con.cursor()
	cursor.execute("SELECT MAX(CDNOTA)+1 FROM TNOTAS;")
	resultado = cursor.fetchmany(0)
	x = resultado[0]
	return x[0]

def Data_Nota():
	con = Cria_Banco()
	cursor = con.cursor()
	cursor.execute("SELECT DATETIME();")
	resultado = cursor.fetchmany(0)
	x = resultado[0]
	return x[0]

	
def Insere_Nota(usuario, titulo, descricao):
	con = Cria_Banco()
	cursor = con.cursor()
	print(usuario[0])
	print(titulo)
	print(descricao)
	if usuario != "" and titulo != "" and descricao != "":
		cursor.execute("INSERT INTO TNOTAS VALUES (?, ?, ?, ?, ?);",(Ultimo_Cod_Nota(), usuario[0],
		titulo, descricao, Data_Nota()))
		con.commit()
	else:
		ctypes.windll.user32.MessageBoxW(0, "Dados vazios", "Erro", 0)
	
	
	
	
	


	