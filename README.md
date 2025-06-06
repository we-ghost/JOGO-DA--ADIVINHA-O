import tkinter as tk
import random as lol
from PIL import Image, ImageTk

#Funç new game
def new_game():
    global num_sec,ten
    num_sec = lol.randint(1,10)
    tent = 0
    #resul["text"] = ""

def verif_resul():
    pass

def inc_imag():
    pass

#interface

tela = tk.Tk()
tela.title(" Jogo de saber quantas eu já bati hj ")
tela.geometry("700x800")
tela.configure(background='lime')

palpite = tk.Label(tela, text='Informe um número: ', font=('Comic Sans MS', 15),bg= 'light blue' )
palpite.pack(pady=13.5)

entrada_palpite = tk.Entry(tela, justify='center', background='Blue', font=('Arial', 14))
entrada_palpite.pack(pady= 5)



imagem = Image.open('download (1).jfif')
imagem2 = imagem.resize((600,800))
imagemTk = ImageTk.PhotoImage(imagem2)

instr = tk.Label (tela,text='Advinhe quantas eu já bati hj',font=('Comic Sans Ms',15),background='lime')
instr.pack(pady=10)

nome = tk.Label(tela,text='Quem quer saber?',font=('Comic Sans Ms',8))
nome.pack(pady=15)

entre = tk.Entry(tela,justify='center',bg='light blue', font=('arial',14))
entre.pack(pady=5)

botao = tk.Button(tela,text='Confirmar',font=('arial',14))
botao.pack(pady=10)

imgemBai = tk.Label(tela,image = imagemTk)
imgemBai.pack(pady=10)

tela.mainloop()
