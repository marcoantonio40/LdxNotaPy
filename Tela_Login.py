from tkinter import *
from func_botao import *
import sys

#Método utilizado para entrar na tela Tela_Exibe_Notas
#esse método é acionado quando o usuário clicar no botão botao_Entrar
def Click_Entrar():
    login = Entry_Login.get()
    senha = Entry_Senha.get()
    Entry_Login.insert(0,"")
    Entry_Senha.insert(0,"")
    bt_click_Entrar(login,senha)

def Click_Cadastra_Usuario():
	bt_click_Criar_Usu()
    
def fechar_Janela():	
	janela.destroy()

	
janela = Tk()

texto = Label(janela, text="LdxNota")
texto.place(x=100, y=10)

Label_Login = Label(janela, text="Login: ")
Label_Login.place(x=10, y=35)

Label_Senha = Label(janela, text="Senha: ")
Label_Senha.place(x=10, y=60)

Entry_Login = Entry(janela)
Entry_Login.place(x=55, y=35)

Entry_Senha = Entry(janela)
Entry_Senha.place(x=55, y=60)

login=Entry_Login.get()
senha=Entry_Senha.get()


botao_Entrar = Button(janela, width=20,text="Entrar", command = Click_Entrar)
botao_Entrar.place(x=50, y=100)

botao_Criar_Usu = Button(janela, width=20,text="Cadastrar Usuário", command = Click_Cadastra_Usuario)
botao_Criar_Usu.place(x=50, y=130)

botao_Sair = Button(janela, width=20, text="Sair", command = fechar_Janela)
botao_Sair.place(x=50, y=160)



janela.geometry("250x250+250+250")
janela.mainloop()
