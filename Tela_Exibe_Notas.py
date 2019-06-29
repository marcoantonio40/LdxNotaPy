from tkinter import *
from Banco import Notas_Usuario

def Tela_Exibe_Notas(codigo_Usu):
	janela = Tk()
	janela.geometry("675x400+400+400")
	
	
	lbl1= Label(janela, text=" Código Nota ", bg="blue", fg="white")
	lbl2= Label(janela, text="   Usuário   ", bg="blue", fg="white")
	lbl3= Label(janela, text="   Título    ", bg="blue", fg="white")
	lbl4= Label(janela, text="  Descrição  ", bg="blue", fg="white")
	lbl5= Label(janela, text="     Data    ", bg="blue", fg="white")

	lbl1.grid(row=0,column=0,padx= 10, pady=10)
	lbl2.grid(row=0,column=1,padx= 10, pady=10)
	lbl3.grid(row=0,column=2,padx= 10, pady=10)
	lbl4.grid(row=0,column=3,padx= 10, pady=10)
	lbl5.grid(row=0,column=4,padx= 10, pady=10)
	
	#seperator = Label(janela, text ="Marco \n\nAntonio da Silva Rodrigues",background='#2b5bce',width=5, height = 5)
	#seperator.grid(row=1, column=0,rowspan=1, columnspan=4, ipadx = 10)
	teste=Notas_Usuario(codigo_Usu)
	print(teste[0])
	print(teste[1])
	print(teste[2])
	print(teste[3])
	print(teste[4])
	
	
	botao_Cadastrar_Nota = Button(janela, width=20,text="Cadastrar Nota", command = print("Cadastrar nota"))
	botao_Cadastrar_Nota.place(x=20, y=370)
		
	botao_Editar_Nota = Button(janela, width=20, text="Editar", command = print("Editar Nota"))
	botao_Editar_Nota.place(x=180, y=370)
	
	botao_Deletar_Nota = Button(janela, width=20, text="Deletar", command = print("Deletar Nota"))
	botao_Deletar_Nota.place(x=340, y=370)
	
	botao_Sair = Button(janela, width=20,text="SAIR", command = print("Sair"))
	botao_Sair.place(x=500, y=370)
	
