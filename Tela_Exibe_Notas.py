from tkinter import *
from Banco import *

def Tela_Exibe_Notas(codigo_Usu):
	janela = Tk()
	janela.geometry("675x400+400+400")
	
	
	Label_Codigo = Label(janela, text=" Código Nota ", bg="blue", fg="white")
	Label_Usuario = Label(janela, text="   Usuário   ", bg="blue", fg="white")
	Label_Titulo = Label(janela, text="   Título    ", bg="blue", fg="white")
	Label_Descricao = Label(janela, text="  Descrição  ", bg="blue", fg="white")
	Label_Data = Label(janela, text="     Data    ", bg="blue", fg="white")

	Label_Codigo.grid(row=0,column=0,padx= 10, pady=10)
	Label_Usuario.grid(row=0,column=1,padx= 10, pady=10)
	Label_Titulo.grid(row=0,column=2,padx= 10, pady=10)
	Label_Descricao.grid(row=0,column=3,padx= 10, pady=10)
	Label_Data.grid(row=0,column=4,padx= 10, pady=10)
	
	#seperator = Label(janela, text ="Marco \n\nAntonio da Silva Rodrigues",background='#2b5bce',width=5, height = 5)
	#seperator.grid(row=1, column=0,rowspan=1, columnspan=4, ipadx = 10)
	tamanho = Quantas_Notas_Usuario(codigo_Usu)
	notas = Notas_Usuario(codigo_Usu)
	
	for item in range(tamanho):
		linha=notas[item]
		if item % 2 ==0:
			Label1 = Label(janela, text=linha[0], bg="#87CEEB", fg="black")
			Label1.grid(row=item+1,column=0)
			Label2 = Label(janela, text=linha[1], bg="#87CEEB", fg="black")
			Label2.grid(row=item+1,column=1)
			Label3 = Label(janela, text=linha[2], bg="#87CEEB", fg="black")
			Label3.grid(row=item+1,column=2)
			Label4 = Label(janela, text=linha[3], bg="#87CEEB", fg="black")
			Label4.grid(row=item+1,column=3)
			Label5 = Label(janela, text=linha[4], bg="#87CEEB", fg="black")
			Label5.grid(row=item+1,column=4)
		else:
			Label1 = Label(janela, text=linha[0], bg="#B0C4DE", fg="black")
			Label1.grid(row=item+1,column=0)
			Label2 = Label(janela, text=linha[1], bg="#B0C4DE", fg="black")
			Label2.grid(row=item+1,column=1)
			Label3 = Label(janela, text=linha[2], bg="#B0C4DE", fg="black")
			Label3.grid(row=item+1,column=2)
			Label4 = Label(janela, text=linha[3], bg="#B0C4DE", fg="black")
			Label4.grid(row=item+1,column=3)
			Label5 = Label(janela, text=linha[4], bg="#B0C4DE", fg="black")
			Label5.grid(row=item+1,column=4)
		
	
	botao_Cadastrar_Nota = Button(janela, width=20,text="Cadastrar Nota", command = print("Cadastrar nota"))
	botao_Cadastrar_Nota.place(x=20, y=370)
		
	botao_Editar_Nota = Button(janela, width=20, text="Editar", command = print("Editar Nota"))
	botao_Editar_Nota.place(x=180, y=370)
	
	botao_Deletar_Nota = Button(janela, width=20, text="Deletar", command = print("Deletar Nota"))
	botao_Deletar_Nota.place(x=340, y=370)
	
	botao_Sair = Button(janela, width=20,text="SAIR", command = print("Sair"))
	botao_Sair.place(x=500, y=370)
	
