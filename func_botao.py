import sys
from Tela_Cadastra_Usuario import Tela_Cadastra
from Banco import Valida_Login


def bt_click_Entrar(login,senha):
	if(Valida_Login(login,senha)):
		Tela_Cadastra()
		

def bt_click_Criar_Usu():
	print("Criar")
	
def bt_click_Sair():
	sys.exit(0)
	
	