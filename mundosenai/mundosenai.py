import tkinter as tk
import random
from PIL import Image, ImageTk

def iniciar_jogo():
    global numero_secreto, tentativas
    numero_secreto = random.randint(1, 10)
    tentativas = 0
    resultado["text"] = ''
    botao["text"] = 'VERIFICAR'
    botao["command"] = verificar_palpite

def verificar_palpite():
    global tentativas
    palpite = entrada_palpite.get()
    # o .grt pega o que a pessoa digitou la no palpite
    
    if not palpite.isdigit():
        resultado['text'] = 'Digite um número válido'
        return
    palpite = int(palpite)
    tentativas += 1
    
    if palpite == numero_secreto:
        nome = entrada_nome.get()
        #imagem = 'numeros.png'
        resultado['text'] = f'Legal{nome} \nVocê acertou em {tentativas}'
def incluir_imagem(imag):
    pass

#INTERFACE GRAFICA

tela_jogo = tk.Tk()
tela_jogo.title("Jogo de adivinhação do Jonas")
tela_jogo.geometry("400x500")
tela_jogo.configure(background='lightblue')

instrucao = tk.Label(tela_jogo, text='Adivinhe um número entre 1 a 10:',font=('Comic Sans MS', 15),bg= 'light blue')
instrucao.pack(pady=10)
#pady= da a distancia entre as extremidades. No caso acima, serão 10 pixels abaixo

nome_jogador = tk.Label(tela_jogo, text= 'Informe seu nome: ',
                        font=('Comic Sans MS', 15),bg= 'light blue' )
nome_jogador.pack(pady=15)

entrada_nome = tk.Entry(tela_jogo, justify= "center", 
                        background='Blue', font=('Arial', 14))
entrada_nome.pack(pady=5)
#tk.Entry para pedir valores
palpite = tk.Label(tela_jogo, text='Informe um número: ',
                   font=('Comic Sans MS', 15),bg= 'light blue' )
palpite.pack(pady=13.5)

entrada_palpite = tk.Entry(tela_jogo, justify='center',
                           background='Blue', font=('Arial', 14))
entrada_palpite.pack(pady= 5)

botao = tk.Button(tela_jogo, text= 'Verificar', command=verificar_palpite ,
                  font=('Arial', 14), bg= 'yellow')
botao.pack(pady=10)

resultado = tk.Label(tela_jogo, text='', 
                    font=('Comic Sans MS', 15),bg= 'light blue')
resultado.pack(pady=10)

figura = tk.Label(tela_jogo, image= '', background='light blue')
figura.pack(pady= 10)

#incluir imagem na tela
imagem = Image.open('dados.jpg')
imagem2 = imagem.resize((400,200))
imagem_tk = ImageTk.PhotoImage(imagem2)

imagem_rodape = tk.Label(tela_jogo, image=imagem_tk)
imagem_rodape.pack(pady=5)

tela_jogo.mainloop()