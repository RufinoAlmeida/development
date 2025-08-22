import tkinter as tk
from tkinter import messagebox
import json
import os

ARQUIVO_USUARIOS = "usuarios.json"

# Inicializa o arquivo se não existir
if not os.path.exists(ARQUIVO_USUARIOS):
    with open(ARQUIVO_USUARIOS, "w") as f:
        json.dump({}, f)

# Função para carregar usuários
def carregar_usuarios():
    with open(ARQUIVO_USUARIOS, "r") as f:
        return json.load(f)

# Função para salvar usuários
def salvar_usuarios(dados):
    with open(ARQUIVO_USUARIOS, "w") as f:
        json.dump(dados, f, indent=4)

# Função de login
def fazer_login():
    usuario = entry_usuario.get().strip()
    senha = entry_senha.get().strip()

    if not usuario or not senha:
        messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
        return

    usuarios = carregar_usuarios()
    if usuario in usuarios and usuarios[usuario] == senha:
        messagebox.showinfo("Login bem-sucedido", f"Bem-vindo, {usuario}!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos.")

# Função de registro
def registrar():
    usuario = entry_usuario.get().strip()
    senha = entry_senha.get().strip()

    if not usuario or not senha:
        messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
        return

    usuarios = carregar_usuarios()
    if usuario in usuarios:
        messagebox.showwarning("Usuário existente", "Este usuário já está cadastrado.")
    else:
        usuarios[usuario] = senha
        salvar_usuarios(usuarios)
        messagebox.showinfo("Registrado com sucesso", "Usuário registrado!")

# GUI principal
janela = tk.Tk()
janela.title("Sistema de Login")
janela.geometry("400x320")
janela.configure(bg="#1f1f2e")

# Título
titulo = tk.Label(janela, text="Login Inovador", font=("Segoe UI", 20, "bold"), bg="#1f1f2e", fg="white")
titulo.pack(pady=20)

# Campo Usuário
tk.Label(janela, text="Usuário:", font=("Segoe UI", 12), bg="#1f1f2e", fg="white").pack()
entry_usuario = tk.Entry(janela, font=("Segoe UI", 12), width=30)
entry_usuario.pack(pady=5)

# Campo Senha
tk.Label(janela, text="Senha:", font=("Segoe UI", 12), bg="#1f1f2e", fg="white").pack()
entry_senha = tk.Entry(janela, font=("Segoe UI", 12), width=30, show="*")
entry_senha.pack(pady=5)

# Botões
frame_botoes = tk.Frame(janela, bg="#1f1f2e")
frame_botoes.pack(pady=20)

btn_login = tk.Button(frame_botoes, text="Entrar", font=("Segoe UI", 12), width=10, command=fazer_login, bg="#3c9", fg="white")
btn_login.grid(row=0, column=0, padx=10)

btn_registrar = tk.Button(frame_botoes, text="Registrar", font=("Segoe UI", 12), width=10, command=registrar, bg="#69f", fg="white")
btn_registrar.grid(row=0, column=1, padx=10)

# Rodapé
footer = tk.Label(janela, text="© 2025 - Seu Sistema", font=("Segoe UI", 8), bg="#1f1f2e", fg="gray")
footer.pack(side="bottom", pady=10)

janela.mainloop()
