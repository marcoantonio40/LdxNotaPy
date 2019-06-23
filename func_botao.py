import sys
from Tela_Cadastra_Usuario import Tela_Cadastra
from Banco import Valida_Login


def bt_click_Entrar(login,senha):
	if(Valida_Login(login,senha)):
		Tela_Cadastra()		
	else:
		import ctypes  
		ctypes.windll.user32.MessageBoxW(0, "Dados incorretos", "Erro", 0)

def bt_click_Criar_Usu():
	print("Criar")
	
def bt_click_Sair():
	sys.exit(0)
	


	
	