from tkinter import messagebox
import tkinter as tk

class Controller:
    def __init__(self):
        self.model = None
        self.view = None

    def referenciar_view_model(self, model, view):
        self.model = model
        self.view = view
       
    def verificar_login(self):
        usuario = self.view.obter_nome_login()
        senha = self.view.obter_senha_login()
        login = self.model.verificar_usuario(usuario, senha)

        if login:
            if login["Nivel"] == 2:
                messagebox.showinfo("Sucesso", "Login bem-sucedido como administrador.")
                self.view.fechartela()
                self.view.abrir_tela_adm()
            elif login["Nivel"] == 1:
                messagebox.showinfo("Sucesso", "Login bem-sucedido como usuário comum.")
                self.view.fechartela()
                self.view.abrir_tela_comum()
        else:
            messagebox.showerror("Erro", "Credenciais inválidas. Por favor, tente novamente.")

    def cadastrar_usuario(self):
        nome_usuario = self.view.obter_nome_cadastro()
        senha = self.view.obter_senha_cadastro()

        if nome_usuario and senha:
            cadastrado = self.model.cadastrar_usuario(nome_usuario, senha)
            if cadastrado:
                messagebox.showinfo("Sucesso", "Cadastro bem-sucedido.")
                self.view.limpar_campos_cadastro()
            else:
                messagebox.showwarning("Atenção", "Usuário já existente. Por favor, escolha outro nome.")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos do cadastro.")

    def inserir_pirata(self, nomePirata, akuma, haki, nomeTripulacao, possuiArma, recompensa):
        if self.model.inserir_pirata(nomePirata, akuma, haki, nomeTripulacao, possuiArma, recompensa):
            messagebox.showinfo(message="Pirata cadastrado com sucesso!")
            self.view.escrever_tabela()
        else:
            messagebox.showerror(message="Pirata já foi cadastrado!")

    def buscar_piratas(self, pirata):
        piratas = self.model.buscar_piratas(pirata)

        if piratas:
            return piratas
        else :
            messagebox.showinfo(message="Não foi encontrado o pirata!")

    def deletar_pirata(self, pirata):
        if self.model.deletar_pirata(pirata):
            messagebox.showinfo(message="Pirata deletado com sucesso!")
            self.view.escrever_tabela()
        else:
            messagebox.showerror(message="Houve um erro ao deletar!")
    
    def editar_pirata(self, _id, nomePirata, akuma, haki, nomeTripulacao, possuiArma, recompensa):
        if self.model.editar_pirata(_id, nomePirata, akuma, haki, nomeTripulacao, possuiArma, recompensa):
            messagebox.showinfo(message="Pirata editado com sucesso!")
            self.view.escrever_tabela()
        else :
            messagebox.showerror(message="Houve um erro ao editar!")

    def limpar_campos_login(self):
        self.view.id_entry.delete(0, tk.END)
        self.view.senha_entry.delete(0, tk.END)

    def limpar_campos_cadastro(self):
        self.view.LG_Cadastro_entry.delete(0, tk.END)
        self.view.SN_Cadastro_entry.delete(0, tk.END)
