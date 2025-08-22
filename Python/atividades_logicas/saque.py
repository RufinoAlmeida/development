
'''Sistema de caixa eletronico para realizar um saque. Esse sistema vocÊ pode realizar o cadastro de usuario e o valor em conta'''

import tkinter as tk
from tkinter import messagebox

# Dicionário para armazenar usuários temporariamente (nome: [senha, saldo])
usuarios = {}
usuario_logado = None

# Função para mostrar a tela de login
def mostrar_tela_login():
    limpar_tela()
    root.geometry("400x400")

    tk.Label(root, text="Login", font=("Helvetica", 16)).pack(pady=10)

    tk.Label(root, text="Usuário:").pack()
    entry_usuario = tk.Entry(root)
    entry_usuario.pack()

    tk.Label(root, text="Senha:").pack()
    entry_senha = tk.Entry(root, show="*")
    entry_senha.pack()

    def fazer_login():
        nome = entry_usuario.get()
        senha = entry_senha.get()
        if nome in usuarios:
            if usuarios[nome][0] == senha:
                global usuario_logado
                usuario_logado = nome
                mostrar_tela_saldo()
            else:
                messagebox.showerror("Erro", "Senha incorreta")
        else:
            messagebox.showwarning("Aviso", "Usuário não cadastrado")

    tk.Button(root, text="Entrar", command=fazer_login).pack(pady=5)
    tk.Button(root, text="Cadastrar", command=mostrar_tela_cadastro).pack()

# Função para mostrar a tela de cadastro
def mostrar_tela_cadastro():
    limpar_tela()
    root.geometry("400x400")

    tk.Label(root, text="Cadastro de Usuário", font=("Helvetica", 16)).pack(pady=10)

    tk.Label(root, text="Usuário:").pack()
    entry_usuario = tk.Entry(root)
    entry_usuario.pack()

    tk.Label(root, text="Senha:").pack()
    entry_senha = tk.Entry(root, show="*")
    entry_senha.pack()

    tk.Label(root, text="Saldo Inicial (R$):").pack()
    entry_saldo = tk.Entry(root)
    entry_saldo.pack()

    def cadastrar():
        nome = entry_usuario.get()
        senha = entry_senha.get()
        try:
            saldo = float(entry_saldo.get())
        except ValueError:
            messagebox.showerror("Erro", "Saldo inválido")
            return

        if nome in usuarios:
            messagebox.showerror("Erro", "Usuário já cadastrado")
        else:
            usuarios[nome] = [senha, saldo]
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            mostrar_tela_login()

    tk.Button(root, text="Cadastrar", command=cadastrar).pack(pady=5)
    tk.Button(root, text="Voltar", command=mostrar_tela_login).pack()

# Função para mostrar a tela de saldo e saque
def mostrar_tela_saldo():
    limpar_tela()
    root.geometry("400x400")

    saldo = usuarios[usuario_logado][1]

    tk.Label(root, text=f"Bem-vindo, {usuario_logado}!", font=("Helvetica", 16)).pack(pady=10)
    tk.Label(root, text=f"Saldo atual: R$ {saldo:.2f}").pack(pady=5)

    tk.Label(root, text="Valor para saque (R$):").pack()
    entry_valor = tk.Entry(root)
    entry_valor.pack()

    def sacar():
        try:
            valor = int(entry_valor.get())
            if valor <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor inteiro positivo")
            return

        if valor > usuarios[usuario_logado][1]:
            messagebox.showwarning("Saldo insuficiente", "Você não tem saldo suficiente")
            return

        notas = [100, 50, 20, 10, 5, 2]
        resultado = {}
        restante = valor

        for nota in notas:
            qtd = restante // nota
            if qtd > 0:
                resultado[nota] = qtd
                restante -= nota * qtd

        if restante != 0:
            messagebox.showerror("Erro", "Valor inválido para saque. Não é possível fornecer troco com as notas disponíveis.")
            return

        usuarios[usuario_logado][1] -= valor
        mostrar_resultado_saque(valor, resultado)

    tk.Button(root, text="Sacar", command=sacar).pack(pady=10)
    tk.Button(root, text="Sair", command=mostrar_tela_login).pack()

# Tela de resultado do saque
def mostrar_resultado_saque(valor, notas):
    limpar_tela()
    root.geometry("400x400")

    tk.Label(root, text=f"Saque de R$ {valor:.2f} realizado com sucesso!", font=("Helvetica", 14)).pack(pady=10)

    for nota, qtd in notas.items():
        tk.Label(root, text=f"Notas de R$ {nota}: {qtd}").pack()

    novo_saldo = usuarios[usuario_logado][1]
    tk.Label(root, text=f"Novo saldo: R$ {novo_saldo:.2f}", font=("Helvetica", 12)).pack(pady=10)

    tk.Button(root, text="Voltar", command=mostrar_tela_saldo).pack()

# Função para limpar widgets da tela atual
def limpar_tela():
    for widget in root.winfo_children():
        widget.destroy()

# Inicialização do Tkinter
root = tk.Tk()
root.title("Caixa Eletrônico")
root.geometry("400x400")
mostrar_tela_login()
root.mainloop()
