##landix
##marco
import sqlite3 
import os.path
import ctypes  

#Método para conectar no banco de dados e retornar o conector
def Cria_Banco():
	if(os.path.exists('C:\csharp\Python\dadosPy.sqlite')):
		conn = sqlite3.connect('dadosPy.sqlite')
		return conn
	else:
		print("Banco de dados não existe!")

#Método que utiliza o login e a senha inseridos na 	Tela_Login
#para conferir se o usuário existe no banco
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

#Método para buscar o último código do usuário e retornar
#o próxmo para ser utilizado no método Insere_Usuario
def Ultimo_Cod_Usu():
	con = Cria_Banco()
	cursor = con.cursor()
	cursor.execute("SELECT MAX(CDUSU)+1 FROM TUSUARIOS;")
	resultado = cursor.fetchmany(0)
	x = resultado[0]
	return x[0]

#Método para inserir usuários no banco de dados com
#as informações que vem da tela Tela_Cadastra_Usuario	
def Insere_Usuario(nome, login, senha):
	senha_Crip = criptografar(senha)
	con = Cria_Banco()
	cursor = con.cursor()
	if nome != "" and login != "" and senha != "":
		cursor.execute("INSERT INTO TUSUARIOS (CDUSU, DSNOME, DSLOGIN, DSSENH) VALUES (?, ?, ?, ?);",(Ultimo_Cod_Usu(), nome, login, senha_Crip))
		con.commit()
	else:
		ctypes.windll.user32.MessageBoxW(0, "Dados vazios", "Erro", 0)

#Método para criptografar as senhas que são inseridas na tela
#Tela_Cadastra_Usuario e armazenar no banco de dados
def criptografar(senha):
	import hashlib
	hash_obj = hashlib.md5(senha.encode())
	return hash_obj.hexdigest()	

#Método para retornar o código do usuário que será usado no método bt_click_Entrar
#do arquivo func_botao para enviar o código do usuário para tela Tela_Exibe_Notas	
def Retorna_Codigo_Usuario(login,senha):
	senha_Crip = criptografar(senha)
	con = Cria_Banco()
	cursor = con.cursor()
	cursor.execute("SELECT CDUSU FROM TUSUARIOS WHERE DSLOGIN = ? AND DSSENH = ?;",(login,senha_Crip))
	resultado = cursor.fetchmany(0)
	return resultado[0]
	 	
#Método para retornar as notas de um usuário para exibir na tela
#Tela_Exibe_Notas	
def Notas_Usuario():
	con = Cria_Banco()
	cursor = con.cursor()
	cursor.execute("SELECT CDNOTA, CDUSU, DSTITU, DSNOTA, DTNOTA FROM TNOTAS;")
	resultado = cursor.fetchmany(0)
	return resultado

#Método para contar quantas notas um usuário tem
# para ser utilizado na tela Tela_Exibe_Notas	
def Quantas_Notas_Usuario(usuario):
	con = Cria_Banco()
	cursor = con.cursor()
	cursor.execute("SELECT COUNT(*) FROM TNOTAS WHERE CDUSU = ?;", (usuario))
	resultado = cursor.fetchmany(0)
	x = resultado[0]
	return x[0]

#Método para pegar o último código da nota para inserir
#uma nova nota no banco
def Ultimo_Cod_Nota():
	con = Cria_Banco()
	cursor = con.cursor()
	cursor.execute("SELECT MAX(CDNOTA)+1 FROM TNOTAS;")
	resultado = cursor.fetchmany(0)
	x = resultado[0]
	return x[0]

#Método para pegar a data do banco para inserir
#uma nova nota no método Insere_Nota
def Data_Nota():
	con = Cria_Banco()
	cursor = con.cursor()
	cursor.execute("SELECT DATETIME();")
	resultado = cursor.fetchmany(0)
	x = resultado[0]
	return x[0]

#Método para inserir uma nova nota com os dados
#que são inseridos na tela Tela_Cadastra_Nota	
def Insere_Nota(usuario, titulo, descricao):
	con = Cria_Banco()
	cursor = con.cursor()
	if usuario != "" and titulo != "" and descricao != "":
		cursor.execute("INSERT INTO TNOTAS VALUES (?, ?, ?, ?, ?);",(Ultimo_Cod_Nota(), usuario[0],
		titulo, descricao, Data_Nota()))
		con.commit()
	else:
		ctypes.windll.user32.MessageBoxW(0, "Dados vazios", "Erro", 0)

#Método para consultar no banco de dados se uma nota
#existe e assim poder editar ou apagá-la na tela Tela_Exibe_Notas		
def Verifica_Nota_Existe(codigo):
	con = Cria_Banco()
	cursor = con.cursor()
	cursor.execute("SELECT COUNT(*) FROM TNOTAS WHERE CDNOTA = ?;",(codigo))
	resultado = cursor.fetchmany(0)
	x = resultado[0]
	return x[0]
	
	
def Nota_Usuario(codigo):
	con = Cria_Banco()
	cursor = con.cursor()
	cursor.execute("SELECT DSTITU, DSNOTA FROM TNOTAS WHERE CDNOTA = ?;",(codigo))
	resultado = cursor.fetchmany(0)
	x = resultado[0]
	return x
	
def Insere_Nota_Editada(codigo, titulo, descricao):
	con = Cria_Banco()
	cursor = con.cursor()
	if codigo != "" and titulo != "" and descricao != "":
		cursor.execute("UPDATE TNOTAS SET DSTITU = ?, DSNOTA = ?, DTNOTA = ? WHERE CDNOTA = ?;",(titulo, descricao, Data_Nota(), codigo))
		con.commit()
	else:
		ctypes.windll.user32.MessageBoxW(0, "Dados vazios", "Erro", 0)
	
	


	