import customtkinter as ctk

class App(ctk.CTk): #Define uma nova classe chamada App que herda de ctk.CTk. Isso significa que sua classe App terá todas as funcionalidades básicas de uma janela CustomTkinter.
    def __init__(self):
        super().__init__()
        self.configuracoes_de_janela_inicial()
    
    # Configurando a janela principal 
    def configuracoes_de_janela_inicial(self):
        self.geometry("700x400")
        self.title("Sistema de login")
        self.resizable(False, False)


if __name__ == "__main__":
    app = App()
    app.mainloop()
