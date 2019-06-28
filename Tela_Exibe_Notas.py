from tkinter import *

def Tela_Exibe_Notas():
	janela = Tk()
	janela.geometry("675x400+400+400")
	
	botao_Cadastrar_Nota = Button(janela, width=20,text="Cadastrar Nota", command = print("Cadastrar nota"))
	botao_Cadastrar_Nota.place(x=20, y=370)
		
	botao_Editar_Nota = Button(janela, width=20, text="Editar", command = print("Editar Nota"))
	botao_Editar_Nota.place(x=180, y=370)
	
	botao_Deletar_Nota = Button(janela, width=20, text="Deletar", command = print("Deletar Nota"))
	botao_Deletar_Nota.place(x=340, y=370)
	
	botao_Sair = Button(janela, width=20,text="SAIR", command = print("Sair"))
	botao_Sair.place(x=500, y=370)