from tkinter import *

def Tela_Exibe_Notas():
	janela = Tk()
	janela.geometry("675x400+400+400")
	

	lbl1= Label(janela, text="Código Nota", bg="blue", fg="white")
	lbl2= Label(janela, text="Usuário", bg="blue", fg="white")
	lbl3= Label(janela, text="Título", bg="blue", fg="white")
	lbl4= Label(janela, text="Descrição", bg="blue", fg="white")
	lbl5= Label(janela, text="Data", bg="blue", fg="white")

	lbl1.grid(row=0,column=2,padx= 10, pady=10)
	lbl2.grid(row=0,column=3,padx= 10, pady=10)
	lbl3.grid(row=0,column=4,padx= 10, pady=10)
	lbl4.grid(row=0,column=5,padx= 10, pady=10)
	lbl5.grid(row=0,column=6,padx= 10, pady=10)

	
	botao_Cadastrar_Nota = Button(janela, width=20,text="Cadastrar Nota", command = print("Cadastrar nota"))
	botao_Cadastrar_Nota.place(x=20, y=370)
		
	botao_Editar_Nota = Button(janela, width=20, text="Editar", command = print("Editar Nota"))
	botao_Editar_Nota.place(x=180, y=370)
	
	botao_Deletar_Nota = Button(janela, width=20, text="Deletar", command = print("Deletar Nota"))
	botao_Deletar_Nota.place(x=340, y=370)
	
	botao_Sair = Button(janela, width=20,text="SAIR", command = print("Sair"))
	botao_Sair.place(x=500, y=370)