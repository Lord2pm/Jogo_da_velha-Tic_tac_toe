from tkinter import *
from tkinter import messagebox

clicked = [False] * 9

jogador_O = 1
jogador_X = 0

pontos1 = 0
pontos2 = 0

def tic_tac_toe():
	def clenner():
		bt1["text"] = ""
		bt2["text"] = ""
		bt3["text"] = ""
		bt4["text"] = ""
		bt5["text"] = ""
		bt6["text"] = ""
		bt7["text"] = ""
		bt8["text"] = ""
		bt9["text"] = ""

		bt1["fg"] = "#000000"
		bt2["fg"] = "#000000"
		bt3["fg"] = "#000000"
		bt4["fg"] = "#000000"
		bt5["fg"] = "#000000"
		bt6["fg"] = "#000000"
		bt7["fg"] = "#000000"
		bt8["fg"] = "#000000"
		bt9["fg"] = "#000000"

	def end_game0():
		global clicked
		if bt1["text"] != "" and bt2["text"] != "" and bt3["text"] != "" and bt4["text"] != "" and bt5["text"] != "" and bt6["text"] != "" and bt7["text"] != "" and bt8["text"] != "" and bt9["text"] != "":
			messagebox.showinfo("Fim de jogo", "Empate")
			clenner()
			clicked = [False] * 9

	def end_game1():
		global clicked
		global pontos2
		cont = pontos2
		if bt1["text"] == bt2["text"] == bt3["text"] == "O":
			bt1["fg"] = "green"
			bt2["fg"] = "green"
			bt3["fg"] = "green"
			messagebox.showinfo("Fim de jogo", "O jogador O venceu!")
			pontos2 += 1
			lb1["text"] = f"Jogador X    {pontos1}    :    {pontos2}    Jogador O"
		if bt4["text"] == bt5["text"] == bt6["text"] == "O":
			bt4["fg"] = "green"
			bt5["fg"] = "green"
			bt6["fg"] = "green"
			messagebox.showinfo("Fim de jogo", "O jogador O venceu!")
			pontos2 += 1
			lb1["text"] = f"Jogador X    {pontos1}    :    {pontos2}    Jogador O"
		if bt7["text"] == bt8["text"] == bt9["text"] == "O":
			bt7["fg"] = "green"
			bt8["fg"] = "green"
			bt9["fg"] = "green"
			messagebox.showinfo("Fim de jogo", "O jogador O venceu!")
			pontos2 += 1
			lb1["text"] = f"Jogador X    {pontos1}    :    {pontos2}    Jogador O"
		if bt1["text"] == bt5["text"] == bt9["text"] == "O":
			bt1["fg"] = "green"
			bt5["fg"] = "green"
			bt9["fg"] = "green"
			messagebox.showinfo("Fim de jogo", "O jogador O venceu!")
			pontos2 += 1
			lb1["text"] = f"Jogador X    {pontos1}    :    {pontos2}    Jogador O"
		if bt3["text"] == bt5["text"] == bt7["text"] == "O":
			bt3["fg"] = "green"
			bt5["fg"] = "green"
			bt7["fg"] = "green"
			messagebox.showinfo("Fim de jogo", "O jogador O venceu!")
			pontos2 += 1
			lb1["text"] = f"Jogador X    {pontos1}    :    {pontos2}    Jogador O"
		if bt1["text"] == bt4["text"] == bt7["text"] == "O":
			bt1["fg"] = "green"
			bt4["fg"] = "green"
			bt7["fg"] = "green"
			messagebox.showinfo("Fim de jogo", "O jogador O venceu!")
			pontos2 += 1
			lb1["text"] = f"Jogador X    {pontos1}    :    {pontos2}    Jogador O"
		if bt2["text"] == bt5["text"] == bt8["text"] == "O":
			bt2["fg"] = "green"
			bt5["fg"] = "green"
			bt8["fg"] = "green"
			messagebox.showinfo("Fim de jogo", "O jogador O venceu!")
			pontos2 += 1
			lb1["text"] = f"Jogador X    {pontos1}    :    {pontos2}    Jogador O"
		if bt3["text"] == bt6["text"] == bt9["text"] == "O":
			bt3["fg"] = "green"
			bt6["fg"] = "green"
			bt9["fg"] = "green"
			messagebox.showinfo("Fim de jogo", "O jogador O venceu!")
			pontos2 += 1
			lb1["text"] = f"Jogador X    {pontos1}    :    {pontos2}    Jogador O"
		if cont < pontos2:
			clenner()
			clicked = [False] * 9

	def end_game2():
		global clicked
		global pontos1
		cont = pontos1
		if bt1["text"] == bt2["text"] == bt3["text"] == "X":
			bt1["fg"] = "green"
			bt2["fg"] = "green"
			bt3["fg"] = "green"
			messagebox.showinfo("Fim de jogo", "O jogador X venceu!")
			pontos1 += 1
			lb1["text"] = f"Jogador X    {pontos1}    :    {pontos2}    Jogador O"
		if bt4["text"] == bt5["text"] == bt6["text"] == "X":
			bt4["fg"] = "green"
			bt5["fg"] = "green"
			bt6["fg"] = "green"
			messagebox.showinfo("Fim de jogo", "O jogador X venceu!")
			pontos1 += 1
			lb1["text"] = f"Jogador X    {pontos1}    :    {pontos2}    Jogador O"
		if bt7["text"] == bt8["text"] == bt9["text"] == "X":
			bt7["fg"] = "green"
			bt8["fg"] = "green"
			bt9["fg"] = "green"
			messagebox.showinfo("Fim de jogo", "O jogador X venceu!")
			pontos1 += 1
			lb1["text"] = f"Jogador X    {pontos1}    :    {pontos2}    Jogador O"
		if bt1["text"] == bt5["text"] == bt9["text"] == "X":
			bt1["fg"] = "green"
			bt5["fg"] = "green"
			bt9["fg"] = "green"
			messagebox.showinfo("Fim de jogo", "O jogador X venceu!")
			pontos1 += 1
			lb1["text"] = f"Jogador X    {pontos1}    :    {pontos2}    Jogador O"
		if bt3["text"] == bt5["text"] == bt7["text"] == "X":
			bt3["fg"] = "green"
			bt5["fg"] = "green"
			bt7["fg"] = "green"
			messagebox.showinfo("Fim de jogo", "O jogador X venceu!")
			pontos1 += 1
			lb1["text"] = f"Jogador X    {pontos1}    :    {pontos2}    Jogador O"
		if bt1["text"] == bt4["text"] == bt7["text"] == "X":
			bt1["fg"] = "green"
			bt4["fg"] = "green"
			bt7["fg"] = "green"
			messagebox.showinfo("Fim de jogo", "O jogador X venceu!")
			pontos1 += 1
			lb1["text"] = f"Jogador X    {pontos1}    :    {pontos2}    Jogador O"
		if bt2["text"] == bt5["text"] == bt8["text"] == "X":
			bt2["fg"] = "green"
			bt5["fg"] = "green"
			bt8["fg"] = "green"
			messagebox.showinfo("Fim de jogo", "O jogador X venceu!")
			pontos1 += 1
			lb1["text"] = f"Jogador X    {pontos1}    :    {pontos2}    Jogador O"
		if bt3["text"] == bt6["text"] == bt9["text"] == "X":
			bt3["fg"] = "green"
			bt6["fg"] = "green"
			bt9["fg"] = "green"
			messagebox.showinfo("Fim de jogo", "O jogador X venceu!")
			pontos1 += 1
			lb1["text"] = f"Jogador X    {pontos1}    :    {pontos2}    Jogador O"
		if cont < pontos1:
			clenner()
			clicked = [False] * 9

	def bt1_click():
		global clicked
		global jogador_X
		global jogador_O
		if clicked[0] == False:
			if jogador_O == 1:
				bt1["text"] = "O"
				jogador_O = 0
				jogador_X = 1
			else:
				bt1["text"] = "X" 
				jogador_O = 1
				jogador_X = 0
			clicked[0] = True
		end_game1()
		end_game2()
		end_game0()

	def bt2_click():
		global clicked
		global jogador_X
		global jogador_O
		if clicked[1] == False:
			if jogador_O == 1:
				bt2["text"] = "O"
				jogador_O = 0
				jogador_X = 1
			else:
				bt2["text"] = "X" 
				jogador_O = 1
				jogador_X = 0
			clicked[1] = True
		end_game1()
		end_game2()
		end_game0()

	def bt3_click():
		global clicked
		global jogador_X
		global jogador_O
		if clicked[2] == False:
			if jogador_O == 1:
				bt3["text"] = "O"
				jogador_O = 0
				jogador_X = 1
			else:
				bt3["text"] = "X" 
				jogador_O = 1
				jogador_X = 0
			clicked[2] = True
		end_game1()
		end_game2()
		end_game0()

	def bt4_click():
		global clicked
		global jogador_X
		global jogador_O
		if clicked[3] == False:
			if jogador_O == 1:
				bt4["text"] = "O"
				jogador_O = 0
				jogador_X = 1
			else:
				bt4["text"] = "X" 
				jogador_O = 1
				jogador_X = 0
			clicked[3] = True
		end_game1()
		end_game2()
		end_game0()

	def bt5_click():
		global clicked
		global jogador_X
		global jogador_O
		if clicked[4] == False:
			if jogador_O == 1:
				bt5["text"] = "O"
				jogador_O = 0
				jogador_X = 1
			else:
				bt5["text"] = "X" 
				jogador_O = 1
				jogador_X = 0
			clicked[4] = True
		end_game1()
		end_game2()
		end_game0()

	def bt6_click():
		global clicked
		global jogador_X
		global jogador_O
		if clicked[5] == False:
			if jogador_O == 1:
				bt6["text"] = "O"
				jogador_O = 0
				jogador_X = 1
			else:
				bt6["text"] = "X" 
				jogador_O = 1
				jogador_X = 0
			clicked[5] = True
		end_game1()
		end_game2()
		end_game0()

	def bt7_click():
		global clicked
		global jogador_X
		global jogador_O
		if clicked[6] == False:
			if jogador_O == 1:
				bt7["text"] = "O"
				jogador_O = 0
				jogador_X = 1
			else:
				bt7["text"] = "X" 
				jogador_O = 1
				jogador_X = 0
			clicked[6] = True
		end_game1()
		end_game2()
		end_game0()

	def bt8_click():
		global clicked
		global jogador_X
		global jogador_O
		if clicked[7] == False:
			if jogador_O == 1:
				bt8["text"] = "O"
				jogador_O = 0
				jogador_X = 1
			else:
				bt8["text"] = "X" 
				jogador_O = 1
				jogador_X = 0
			clicked[7] = True
		end_game1()
		end_game2()
		end_game0()

	def bt9_click():
		global clicked
		global jogador_X
		global jogador_O
		if clicked[8] == False:
			if jogador_O == 1:
				bt9["text"] = "O"
				jogador_O = 0
				jogador_X = 1
			else:
				bt9["text"] = "X" 
				jogador_O = 1
				jogador_X = 0
			clicked[8] = True
		end_game1()
		end_game2()
		end_game0()

	def sobre():
		messagebox.showinfo("Sobre o Tic Tac Toe", "O Tic Tac Toe é um jogo clássico, cujo a finalidade consiste em articular estratégias para que as peças de um mesmo jogador estejam alinhadas e, preencham todos as posições numa linha, coluna ou diagonal do tabuleiro que, tem uma estrutura matricial de ordem 3.\n\nEle foi concebido pelo estudante de Eng. Informática Luís Manuel Muhele, entre os dias 15 e 16 de Maio de 2022.")
	
	def sair():
		janela.destroy()

	def novo_jogo():
		global clicked
		clicked = [False] * 9

		global pontos1
		global pontos2

		pontos1 = 0
		pontos2 = 0

		lb1["text"] = f"Jogador X    {pontos1}    :    {pontos2}    Jogador O"

		clenner()

	janela = Tk()
	janela.resizable(False, False)
	janela.geometry("700x540+150+0")
	janela.title("Tic Tac Toe")
	janela["bg"] = "#6f0039"

	barra_menu = Menu(janela)
	
	menu_ver = Menu(barra_menu, tearoff=0)
	menu_ver.add_command(label="Novo jogo", command=novo_jogo)
	menu_ver.add_separator()
	menu_ver.add_command(label="Sair", command=sair)

	menu_sobre = Menu(barra_menu, tearoff=0)
	menu_sobre.add_command(label="Sobre", command=sobre)

	barra_menu.add_cascade(label="Opções", menu=menu_ver)
	barra_menu.add_cascade(label="Sobre", menu=menu_sobre)

	janela.config(menu=barra_menu)

	lb1 = Label(janela, text=f"Jogador X    {pontos1}    :    {pontos2}    Jogador O", bg="#6f0039", fg="#c1c1c1", font=("Aachen-Bold", 20))
	lb1.place(x=105, y=20)

	#Frames verticais

	frame_v1 = Frame(janela, width=5, height=440, bg="#000000")
	frame_v1.place(x=250, y=90)

	frame_v2 = Frame(janela, width=5, height=440, bg="#000000")
	frame_v2.place(x=420, y=90)

	#Frames horizontais

	frame_h1 = Frame(janela, width=480, height=5, bg="#000000")
	frame_h1.place(x=100, y=230)

	frame_h2 = Frame(janela, width=480, height=5, bg="#000000")
	frame_h2.place(x=100, y=380)

	#Criando os botões

	#Primeira linha

	bt1 = Button(janela, width=4, border=0, bg="#6f0039", activebackground="#6f0039", font=("Aachen-Bold", 35), command=bt1_click)
	bt1.place(x=115, y=110)

	bt2 = Button(janela, width=4, border=0, bg="#6f0039", activebackground="#6f0039", font=("Aachen-Bold", 35), command=bt2_click)
	bt2.place(x=275, y=110)

	bt3 = Button(janela, width=4, border=0, bg="#6f0039", activebackground="#6f0039", font=("Aachen-Bold", 35), command=bt3_click)
	bt3.place(x=435, y=110)

	#Segunda linha

	bt4 = Button(janela, width=4, border=0, bg="#6f0039", activebackground="#6f0039", font=("Aachen-Bold", 35), command=bt4_click)
	bt4.place(x=115, y=250)

	bt5 = Button(janela, width=4, border=0, bg="#6f0039", activebackground="#6f0039",  font=("Aachen-Bold", 35), command=bt5_click)
	bt5.place(x=275, y=250)

	bt6 = Button(janela, width=4, border=0, bg="#6f0039", activebackground="#6f0039",  font=("Aachen-Bold", 35), command=bt6_click)
	bt6.place(x=435, y=250)

	#Terceira linha

	bt7 = Button(janela, width=4, border=0, bg="#6f0039", activebackground="#6f0039",  font=("Aachen-Bold", 35), command=bt7_click)
	bt7.place(x=115, y=390)

	bt8 = Button(janela, width=4, border=0, bg="#6f0039", activebackground="#6f0039",  font=("Aachen-Bold", 35), command=bt8_click)
	bt8.place(x=275, y=390)

	bt9 = Button(janela, width=4, border=0, bg="#6f0039", activebackground="#6f0039",  font=("Aachen-Bold", 35), command=bt9_click)
	bt9.place(x=435, y=390)

	janela.mainloop()

tic_tac_toe()