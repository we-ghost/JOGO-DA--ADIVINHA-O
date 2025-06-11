import tkinter as tk
import random as lol
from PIL import Image, ImageTk

#Funç new game
def new_game():
    global num_sec,tent
    num_sec = lol.randint(1,10)
    tent = 0
    resultado['text'] = ''
    botao['text'] = 'Verificar'
    botao['command'] = verif_resul
def verif_resul():
    global tent
    pal = palpite.get()

    if not pal.isdigit():
        resultado['text'] = 'Digite um número válido'
        return
    pal = int(pal)
    tent += 1

    if pal == num_sec:
        nomee = nome.get()
        imagen = 'final.jpg'
        resultado['text'] = f'Calmô, não espalha {nomee}\n Você descobriu em {tent}'

def inc_imag():
    pass

#interface

tela = tk.Tk()
tela.title(" Jogo de saber quantas eu já bati hj ")
tela.geometry("4000x1240")
tela.configure(background='lime')

palpite = tk.Label(tela, text='Informe um número: ', font=('Comic Sans MS', 15),bg= 'light blue' )
palpite.pack(pady=13.5)

entrada_palpite = tk.Entry(tela, justify='center', background='Blue', font=('Arial', 14))
entrada_palpite.pack(pady= 5)



imagem = Image.open('download (1).jfif')
imagem2 = imagem.resize((3000,800))
imagemTk = ImageTk.PhotoImage(imagem2)

instr = tk.Label (tela,text='Advinhe o número',font=('Comic Sans Ms',40),background='lime')
instr.pack(pady=10)

nome = tk.Label(tela,text='Quem quer saber?',font=('Comic Sans Ms',28))
nome.pack(pady=15)

entre = tk.Entry(tela,justify='center',bg='light blue', font=('arial',38))
entre.pack(pady=10)

botao = tk.Button(tela,text='Confirmar',font=('arial',14))
botao.pack(pady=10)

resultado = tk.Label(tela,text='',font=('Comic Sans Ms',28))
resultado.pack(pady=15)

imgemBai = tk.Label(tela,image = imagemTk)
imgemBai.pack(pady=10)

new_game()

tela.mainloop()
