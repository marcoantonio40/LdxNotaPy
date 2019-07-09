from tkinter import *
from Banco import *
from Tela_Cadastrar_Nota import *
from Tela_Relatorio import Exibe_Notas
import ctypes

def Tela_Exibe_Notas(codigo_Usu):
	
	def Tela_Cadastrar():
		Tela_Cadastrar_Nota(codigo_Usu)
	
	
		
	def Editar_Nota():	
		codigo = Entry_Codigo.get()
		if(codigo== ""):
			ctypes.windll.user32.MessageBoxW(0, "Digite um código", "Alerta", 0)
		else:
			Edita(codigo)
            
		
		
	def Edita(codigo):
		if(Verifica_Nota_Existe(codigo)==1):
			nota = Nota_Usuario(codigo)
			#nota = "marco"
			Entry_Titulo = nota[0]
			Entry_Descricao = nota[0]
			
			Label_Titulo = Label(janela, text="Título: ")
			Label_Titulo.place(x=10, y=65)
			
			Label_Descricao = Label(janela, text="Descrição: ")
			Label_Descricao.place(x=10, y=90)
			
			Entry_Titulo = Entry(janela)
			Entry_Titulo.place(x=70, y=65)
			
			Entry_Descricao = Entry(janela)
			Entry_Descricao.place(x=70, y=90)
		else:
			ctypes.windll.user32.MessageBoxW(0, "Código não correspondente", "Erro", 0)
			
	janela = Tk()
	janela.geometry("400x400+400+400")
	
	Label_Codigo = Label(janela, text = "Código")
	Label_Codigo.place(x = 10, y = 35)
	
	Entry_Codigo = Entry(janela)
	Entry_Codigo.place(x = 70, y = 35)
			
	
	
	botao_Cadastrar_Nota = Button(janela, width=20,text="Cadastrar Nota", command = Tela_Cadastrar)
	botao_Cadastrar_Nota.place(x=120, y=210)

	botao_Ver_Nota = Button(janela, width=20,text="Relatório de notas", command = Exibe_Notas)
	botao_Ver_Nota.place(x=120, y=370)
		
	botao_Editar_Nota = Button(janela, width=20, text="Editar", command = Editar_Nota)
	botao_Editar_Nota.place(x=120, y=330)
	
	botao_Deletar_Nota = Button(janela, width=20, text="Deletar", command = print("Deletar Nota"))
	botao_Deletar_Nota.place(x=120, y=290)
	
	botao_Sair = Button(janela, width=20,text="SAIR", command = print("Sair"))
	botao_Sair.place(x=120, y=250)
	
	
	