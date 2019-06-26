import sys
from Tela_Cadastra_Usuario import Tela_Cadastra
from Banco import Valida_Login
from Tela_Exibe_Notas import Tela_Exibe_Notas


def bt_click_Entrar(login,senha):
	if(Valida_Login(login,senha)):
		Tela_Exibe_Notas()		
	else:
		import ctypes  
		ctypes.windll.user32.MessageBoxW(0, "Dados incorretos", "Erro", 0)

def bt_click_Criar_Usu():
	Tela_Cadastra()
	
def bt_click_Sair():
	sys.exit(0)
	


	
	