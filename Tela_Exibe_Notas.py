from tkinter import *
from Banco import *
from Tela_Cadastrar_Nota import *
from Tela_Relatorio import *
import ctypes

def Tela_Exibe_Notas(codigo_Usu):
	def Limpa_Entry():
		Entry_Codigo.delete(first=0,last=5)
		Entry_Titulo.delete(first=0,last=50)
		Entry_Descricao.delete(first=0,last=50)
	
	def fechar_Janela():	
		janela.destroy()
	
	def Tela_Cadastrar():
		Tela_Cadastrar_Nota(codigo_Usu)
	
	
		
	def Editar_Nota():	
		codigo = Entry_Codigo.get()
		if(codigo== ""):
			ctypes.windll.user32.MessageBoxW(0, "Digite um código", "Alerta", 0)
		else:
			Edita(codigo)
            
	
	def Apagar_Nota():
		codigo = Entry_Codigo.get()
		if(codigo== ""):
			ctypes.windll.user32.MessageBoxW(0, "Digite um código", "Alerta", 0)
		else:
			Apaga(codigo)
		
		
	def Edita(codigo):
		if(Verifica_Nota_Existe(codigo)==1):						
			nota = Nota_Usuario(codigo)
			
			Entry_Titulo.insert(0,nota[0])
			Entry_Descricao.insert(0,nota[1])
			
			def Nota_Editada_Teste():
				titulo = Entry_Titulo.get()
				descricao = Entry_Descricao.get()
				Nota_Editada(codigo, titulo, descricao)
				
			
			
			botao_Confirmar_Edicao = Button(janela, width=15, text="Confirmar", background='red', command = Nota_Editada_Teste)
			botao_Confirmar_Edicao.place(x=280, y=330)
			botao_Desistir_Edicao = Button(janela, width=15, text="Cancelar", background='blue', command = Limpa_Entry)
			botao_Desistir_Edicao.place(x=5, y=330)
			
			
			
		else:
			ctypes.windll.user32.MessageBoxW(0, "Código não correspondente", "Erro", 0)
			
	
	def Apaga(codigo):
		if(Verifica_Nota_Existe(codigo)==1):
			def Nota_Apagada_Teste():
				Deleta_Nota(codigo)
			
			botao_Confirmar_Apagar = Button(janela, width=15, text="Confirmar", background='red', command = Nota_Apagada_Teste)
			botao_Confirmar_Apagar.place(x=280, y=290)
			botao_Desistir_Apagar = Button(janela, width=15, text="Cancelar", background='blue', command = Limpa_Entry)
			botao_Desistir_Apagar.place(x=5, y=290)
		
	
	
	
			
	def Nota_Editada(codigo, titulo, descricao):
		Insere_Nota_Editada(codigo, titulo, descricao)
		Entry_Titulo.insert(0,"")
		Entry_Descricao.insert(0,"")
	
	janela = Tk()
	janela.geometry("400x400+500+150")
	
	Label_Codigo = Label(janela, text = "Código")
	Label_Codigo.place(x = 10, y = 35)
	
	Entry_Codigo = Entry(janela)
	Entry_Codigo.place(x = 70, y = 35)
			
	Label_Titulo = Label(janela, text="Título: ")
	Label_Titulo.place(x=10, y=65)
	
	Label_Descricao = Label(janela, text="Descrição: ")
	Label_Descricao.place(x=10, y=90)
	
	Entry_Titulo = Entry(janela)
	Entry_Titulo.place(x=70, y=65)
	
	Entry_Descricao = Entry(janela,width=50)
	Entry_Descricao.place(x=70, y=90)
	
	botao_Cadastrar_Nota = Button(janela, width=20,text="Cadastrar Nota", command = Tela_Cadastrar)
	botao_Cadastrar_Nota.place(x=120, y=210)

	botao_Ver_Nota = Button(janela, width=20,text="Relatório de notas", command = Exibe_Notas)
	botao_Ver_Nota.place(x=120, y=370)
		
	botao_Editar_Nota = Button(janela, width=20, text="Editar", command = Editar_Nota)
	botao_Editar_Nota.place(x=125, y=330)
	
	botao_Deletar_Nota = Button(janela, width=20, text="Deletar", command = Apagar_Nota)
	botao_Deletar_Nota.place(x=125, y=290)
	
	botao_Sair = Button(janela, width=20,text="SAIR", command = fechar_Janela)
	botao_Sair.place(x=120, y=250)
	
	
	