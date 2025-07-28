import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

# Cores
co0 = "#FFFFFF"
co1 = "#333333"
co2 = "#fcc058"
co3 = "#38576b"
co4 = "#3297ab"
co5 = "#fff873"
co6 = "#fcc058"
co7 = "#e85151"
co8 = "#34eb3d"
fundo = "#3b3b3b"

# Janela
janela = tk.Tk()
janela.title('Pedra, Papel e Tesoura')
janela.geometry('360x380')
janela.configure(bg=co0)

# Frames
frame_cima = tk.Frame(janela, width=360, height=100, bg=co1)
frame_cima.grid(row=0, column=0, sticky="nw")

frame_baixo = tk.Frame(janela, width=360, height=280, bg=co0)
frame_baixo.grid(row=1, column=0, sticky="nw")

# Estilo
estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Labels de pontuação
app_1 = tk.Label(frame_cima, text="Você", font=('Ivy 15 bold'), bg=co1, fg=co0)
app_1.place(x=25, y=70)
app_1_pontos = tk.Label(frame_cima, text="0", font=('Ivy 30 bold'), bg=co1, fg=co0)
app_1_pontos.place(x=35, y=20)

app_2 = tk.Label(frame_cima, text="PC", font=('Ivy 15 bold'), bg=co1, fg=co0)
app_2.place(x=300, y=70)
app_2_pontos = tk.Label(frame_cima, text="0", font=('Ivy 30 bold'), bg=co1, fg=co0)
app_2_pontos.place(x=300, y=20)

app_1_divisor = tk.Label(frame_cima, text=":", font=('Ivy 30 bold'), bg=co1, fg=co0)
app_1_divisor.place(x=180, y=20)

app_1_linha = tk.Label(frame_cima, width=1, height=10, bg=co0)
app_1_linha.place(x=0, y=0)
app_2_linha = tk.Label(frame_cima, width=1, height=10, bg=co0)
app_2_linha.place(x=355, y=0)
app_linha = tk.Label(frame_cima, width=360, height=1, bg=co6)
app_linha.place(x=0, y=95)

# Label para mostrar rodadas restantes
rodadas_label = tk.Label(frame_baixo, text="Rodadas restantes: 5", font=('Ivy 12 bold'), bg=co0, fg=co1)
rodadas_label.place(x=110, y=30)

# Variáveis globais
pontos_voce = 0
pontos_pc = 0
rondas = 5
jogo_iniciado = False
botoes_jogo = []

def mostrar_resultado_rodada(voce, pc, resultado):
    # Criar label temporário para mostrar resultado da rodada
    resultado_temp = tk.Label(frame_baixo, text=f"Você: {voce} | PC: {pc} | {resultado}", 
                             font=('Ivy 12 bold'), bg=co0, fg=co1)
    resultado_temp.place(x=60, y=180)
    
    # Remover após 2 segundos
    janela.after(2000, resultado_temp.destroy)

def mostrar_proxima_rodada():
    # Mostrar mensagem "Próxima rodada em..."
    proxima_msg = tk.Label(frame_baixo, text="Próxima rodada começando...", 
                          font=('Ivy 14 bold'), bg=co0, fg=co4)
    proxima_msg.place(x=90, y=210)
    
    # Remover mensagem e reabilitar botões
    janela.after(1000, lambda: [proxima_msg.destroy(), habilitar_botoes()])

def jogar(escolha):
    global pontos_voce, pontos_pc, rondas, jogo_iniciado
    
    if not jogo_iniciado:
        messagebox.showwarning("Aviso", "Clique em 'Iniciar o Jogo' primeiro!")
        return
        
    if rondas <= 0:
        return

    opcoes = ['Pedra', 'Papel', 'Tesoura']
    pc = random.choice(opcoes)
    voce = escolha

    # Empate
    if voce == pc:
        app_linha['bg'] = co6
        app_1_linha['bg'] = co0
        app_2_linha['bg'] = co0
    # Vitória do jogador
    elif (voce == 'Pedra' and pc == 'Tesoura') or \
         (voce == 'Papel' and pc == 'Pedra') or \
         (voce == 'Tesoura' and pc == 'Papel'):
        pontos_voce += 1
        app_1_linha['bg'] = co8
        app_2_linha['bg'] = co0
        app_linha['bg'] = co8
    else:
        pontos_pc += 1
        app_1_linha['bg'] = co0
        app_2_linha['bg'] = co8
        app_linha['bg'] = co8

    app_1_pontos['text'] = str(pontos_voce)
    app_2_pontos['text'] = str(pontos_pc)

    rondas -= 1
    rodadas_label['text'] = f"Rodadas restantes: {rondas}"
    
    if rondas == 0:
        fim_do_jogo()

def iniciar_jogo():
    global icon_1, icon_2, icon_3, pontos_voce, pontos_pc, rondas, jogo_iniciado
    
    # Reset das variáveis
    pontos_voce = 0
    pontos_pc = 0
    rondas = 5
    jogo_iniciado = True
    
    # Reset da interface
    app_1_pontos['text'] = "0"
    app_2_pontos['text'] = "0"
    app_linha['bg'] = co6
    app_1_linha['bg'] = co0
    app_2_linha['bg'] = co0
    
    # Limpar todos os widgets do frame_baixo exceto o botão
    for widget in frame_baixo.winfo_children():
        if widget != botao_iniciar:
            widget.destroy()
    
    # Recriar label de rodadas
    global rodadas_label
    rodadas_label = tk.Label(frame_baixo, text="Rodadas restantes: 5", font=('Ivy 12 bold'), bg=co0, fg=co1)
    rodadas_label.place(x=110, y=30)

    # Botões com imagens
    icon_1 = Image.open('hand_closed.png').resize((80, 80))
    icon_1 = ImageTk.PhotoImage(icon_1)
    icon_2 = Image.open('hand.png').resize((80, 80))
    icon_2 = ImageTk.PhotoImage(icon_2)
    icon_3 = Image.open('hand_scissors.png').resize((80, 80))
    icon_3 = ImageTk.PhotoImage(icon_3)

    b1 = tk.Button(frame_baixo, image=icon_1, command=lambda: jogar('Pedra'), bg=co0, relief='flat')
    b1.place(x=15, y=70)
    b2 = tk.Button(frame_baixo, image=icon_2, command=lambda: jogar('Papel'), bg=co0, relief='flat')
    b2.place(x=140, y=70)
    b3 = tk.Button(frame_baixo, image=icon_3, command=lambda: jogar('Tesoura'), bg=co0, relief='flat')
    b3.place(x=265, y=70)
    
    # Armazenar referências dos botões
    global botoes_jogo
    botoes_jogo = [b1, b2, b3]
    
    # Restaurar o texto original do botão
    botao_iniciar['text'] = "Iniciar o Jogo"
    
    print(f"Jogo iniciado - Rodadas: {rondas}, Jogo iniciado: {jogo_iniciado}")  # Debug

def fim_do_jogo():
    global jogo_iniciado
    jogo_iniciado = False
    
    # Limpar todos os widgets do frame_baixo exceto o botão
    for widget in frame_baixo.winfo_children():
        if widget != botao_iniciar:
            widget.destroy()
    
    # Determinar o resultado e criar mensagem na janela
    if pontos_voce > pontos_pc:
        titulo = "🎉 PARABÉNS! 🎉"
        mensagem = f"Você venceu o confronto!"
        cor_resultado = co8  # Verde para vitória
    elif pontos_pc > pontos_voce:
        titulo = "😔 Que pena!"
        mensagem = f"O PC venceu o confronto!"
        cor_resultado = co7  # Vermelho para derrota
    else:
        titulo = "🤝 Empate!"
        mensagem = f"Ninguém Venceu!"
        cor_resultado = co1  # Preto para empate
    
    # Criar labels com o resultado na janela
    resultado_titulo = tk.Label(frame_baixo, text=titulo, font=('Ivy 20 bold'), bg=co0, fg=cor_resultado)
    resultado_titulo.place(x=90, y=50)
    
    resultado_mensagem = tk.Label(frame_baixo, text=mensagem, font=('Ivy 14 bold'), bg=co0, fg=co1)
    resultado_mensagem.place(x=90, y=90)
    
    placar_final = tk.Label(frame_baixo, text=f"Placar final: {pontos_voce} x {pontos_pc}", font=('Ivy 16 bold'), bg=co0, fg=co1)
    placar_final.place(x=90, y=120)
    
    # Alterar o texto do botão para "Jogar Novamente"
    botao_iniciar['text'] = "Jogar Novamente"
    
    print(f"Fim do jogo - Você: {pontos_voce}, PC: {pontos_pc}")  # Debug

# Botão iniciar
botao_iniciar = tk.Button(frame_baixo, text="Iniciar o Jogo", command=iniciar_jogo, bg=fundo, fg=co0, font=('Ivy 15 bold'), relief='raised', overrelief='ridge')
botao_iniciar.place(x=100, y=200)

janela.mainloop()