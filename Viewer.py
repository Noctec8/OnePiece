from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

class Viewer:
    def __init__(self, controlador):
        self.controller = controlador

        self.root = tk.Tk()
        self.root.title("TELA DE LOGIN")
        self.root.geometry("1200x600")
        self.root.configure(bg="#3698F3")
        self.root.resizable(False, False)
        self.container = tk.Frame(self.root, bg="#3698F3")
        self.container.place(relx=0, rely=0.1, relwidth=0.9, relheight=0.5)

        self.areaLogin = tk.Label(self.root, text="Área de Login", fg="white", bg="#3698F3", font=("Italic", 15))
        self.areaLogin.place(x=620, y=20)

        self.id_label = tk.Label(self.root, text="ID", padx=20, fg="white", bg="#3698F3", font=("Italic", 15))
        self.id_label.place(x=550, y=65)
        self.id_entry = tk.Entry(self.root)
        self.id_entry.place(x=620, y=70)

        self.senha_label = tk.Label(self.root, text="SENHA", fg="white", bg="#3698F3", font=("Italic", 15))
        self.senha_label.place(x=550, y=110)
        self.senha_entry = tk.Entry(self.root, show="*")
        self.senha_entry.place(x=620, y=115)

        self.Bt_login = tk.Button(self.root, text="LOGIN",command=self.controller.verificar_login)
        self.Bt_login.place(x=700, y=180)

        self.linha = tk.Canvas(self.root, width=1800, height=2, bg="black")
        self.linha.place(x=0, y=240)

        self.LG_Cadastro = tk.Label(self.root, text="Área de Cadastro", fg="white", bg="#3698F3", font=("Italic", 15))
        self.LG_Cadastro.place(x=600, y=280)

        self.LG_Cadastro = tk.Label(text="ID", padx=20, fg="white", bg="#3698F3", font=("Italic", 15))
        self.LG_Cadastro.place(x=550, y=350)
        self.LG_Cadastro_entry = tk.Entry(self.root)
        self.LG_Cadastro_entry.place(x=620, y=355)

        self.SN_Cadastro = tk.Label(self.root, text="SENHA", fg="white", bg="#3698F3", font=("Italic", 15))
        self.SN_Cadastro.place(x=550, y=395)
        self.SN_Cadastro_entry = tk.Entry(self.root, show="*")
        self.SN_Cadastro_entry.place(x=620, y=400)
        self.SN_CadastroBT = tk.Button(self.root, text="CADASTRO",command=self.controller.cadastrar_usuario)
        self.SN_CadastroBT.place(x=675, y=475)
        self.x = tk.Button(self.root, text="X", padx=12, pady=5,command=self.fechartela)
        self.x.place(x=1162, y=1)
        
    def tela_comum (self):
        self.root = tk.Tk()
        self.root.title("CAPTURAR")
        self.root.geometry("1200x960")
        self.root.configure(bg="#3698F3")
        self.container3 = tk.Frame(self.root, bg="#3698F3")
        self.frase = tk.Label(self.container3, text="PIRATAS A SEREM CAPTURADOS PELO GOVERNO MUNDIAL", fg="black", bg="#3698F3", font=("Arial", 12))
        self.frase.place(x=350, y=10,relheight=0.3) 

        self.container3.place(relx=0, rely=0.25, relwidth=1, relheight=0.6)
        self.style = ttk.Style()
        self.style.theme_use("default")

        self.style.configure("Treeview.Heading", background="#3698F3", fieldbackground="#3698F3", foreground="black")
        self.style.configure("Treeview", background="#3698F3", fieldbackground="#3698F3", foreground="black")

        self.treeview = ttk.Treeview(self.container3, columns=("ID", "Nome do Pirata", "Akuma no mi", "Haki", "Nome da tripulação", "Possui Arma", "Recompensa"), show="headings")
        self.treeview.heading("#1", text="ID")
        self.treeview.heading("#2", text="Nome do Pirata")
        self.treeview.heading("#3", text="Akuma no mi")
        self.treeview.heading("#4", text="Haki")
        self.treeview.heading("#5", text="Nome da tripulação")
        self.treeview.heading("#6", text="Possui Arma")
        self.treeview.heading("#7", text="Recompensa")

        self.treeview.place(relx=0, rely=0.3, relwidth=1, relheight=1)
        x_scrollbar = ttk.Scrollbar(self.root, orient="horizontal", command=self.treeview.xview)
        x_scrollbar.place(x=0, y=800, relwidth=1)
        self.treeview.configure(xscrollcommand=x_scrollbar.set, xscroll="baixo")

        self.procurar_telaComum = tk.Label(self.container3 ,text="PROCURAR", fg="black", bg="#3698F3", font=("Italic", 13))
        self.procurar_telaComum.place(x=0 , y=0)
        self.procurar_entry = tk.Entry(self.container3)
        self.procurar_entry.place(x=100,y=3)

        self.Fechar_Tcomum = tk.Button(self.container3, text="FECHAR", fg="black",  font=("Italic", 13), command=self.fechartela)
        self.Fechar_Tcomum.place(x=960,y=0)
        
        self.procurar_entry.bind("<Return>", self.procurar_pirata)

        self.escrever_tabela()
        
    def Tela_adm(self):
        self.root = tk.Tk()
        self.root.title("TELA ADM")
        self.root.geometry("1200x960")
        self.root.configure(bg="#3698F3")
        self.root.resizable(False, False)

        self.container1 = tk.Frame(self.root, bg="#3698F3")
        self.container1.place(relx=0, rely=0, relwidth=1, relheight=0.8)  

        self.frase = tk.Label(self.container1, text="PIRATAS A SEREM CAPTURADOS PELO GOVERNO MUNDIAL", fg="black", bg="#3698F3", font=("Italic", 12))
        self.frase.place(x=360, y=70) 

        self.procurar_label = tk.Label(self.container1, text="PROCURAR", fg="black", bg="#3698F3", font=("Italic", 12))
        self.procurar_label.place(relx=0.0, y=0)
        self.procurar_entry = tk.Entry(self.container1,)
        self.procurar_entry.place(x=97, rely=0)

        self.fechar_label = tk.Button(self.container1, text="FECHAR", command=self.fechartela)
        self.fechar_label.place(x=1150, y=0)

        self.nomePirata_label = tk.Label(self.container1, text="Nome do Pirata", fg="black", bg="#3698F3", font=("Italic", 14))
        self.nomePirata_label.place(x=25, y=180)
        self.nomePirata_entry = tk.Entry(self.container1)
        self.nomePirata_entry.place(x=200, y=183)

        self.Akumanomi_label = tk.Label(self.container1, text="Akuma no Mi", fg="black", bg="#3698F3", font=("Italic", 14))
        self.Akumanomi_label.place(x=25, y=210)
        self.Akumanomi_entry = tk.Entry(self.container1)
        self.Akumanomi_entry.place(x=200, y=210)

        self.haki_label = tk.Label(self.container1, text="Haki", fg="black", bg="#3698F3", font=("Italic", 14))
        self.haki_label.place(x=65, y=235)
        self.haki_entry = tk.Entry(self.container1)
        self.haki_entry.place(x=200, y=240)

        self.tripulacao_label = tk.Label(self.container1, text="Nome da Tripulação", fg="black", bg="#3698F3", font=("Italic", 14))
        self.tripulacao_label.place(x=5, y=265)
        self.tripulacao_entry = tk.Entry(self.container1)
        self.tripulacao_entry.place(x=200, y=270)

        self.arma_label = tk.Label(self.container1, text="Possui Arma", fg="black", bg="#3698F3", font=("Italic", 14))
        self.arma_label.place(x=25,y=295)
        self.arma_entry = tk.Entry(self.root)
        self.arma_entry.place(x=200,y=300)

        self.recompensa_label = tk.Label(self.container1, text="Recompensa", fg="black", bg="#3698F3", font=("Italic", 14))
        self.recompensa_label.place(x=25,y=325)
        self.recompensa_entry = tk.Entry(self.root)
        self.recompensa_entry.place(x=200,y=330)

        self.capturar_bt = tk.Button(self.container1, text="CAPTURAR",fg="black",  font=("Italic", 12), command=self.inserir_pirata)
        self.capturar_bt.place(x=1153,y=310,anchor="center",relwidth=0.1)
        self.remover_bt = tk.Button(self.container1,text="REMOVER",fg="black",  font=("Italic", 12), command=self.deletar_pirata)
        self.remover_bt.place(x=1153,y=360,anchor="center",relwidth=0.1)

        self.editar_bt = tk.Button(self.container1,text="EDITAR",fg="black",  font=("Italic", 13), command=self.editar_pirata)
        self.editar_bt.place(x=1153,y=415,relwidth=0.1,anchor="center")

        self.container2 = tk.Frame(self.root, bg="#3698F3")
        self.container2.place(relx=0, rely=0.5, relwidth=1, relheight=0.6)
        self.style = ttk.Style()
        self.style.theme_use("default")

        self.style.configure("Treeview.Heading", background="#3698F3", fieldbackground="#3698F3", foreground="black")
        self.style.configure("Treeview", background="#3698F3", fieldbackground="#3698F3", foreground="black")
        self.style.configure("Treeview", background="#3698F3", fieldbackground="#3698F3")

        self.treeview = ttk.Treeview(self.container2, columns=("ID", "Nome do Pirata", "Akuma no mi", "Haki", "Nome da tripulação", "Possui Arma", "Recompensa"), show="headings")
        self.treeview.heading("#1", text="ID")
        self.treeview.heading("#2", text="Nome do Pirata")
        self.treeview.heading("#3", text="Akuma no mi")
        self.treeview.heading("#4", text="Haki")
        self.treeview.heading("#5", text="Nome da tripulação")
        self.treeview.heading("#6", text="Possui Arma")
        self.treeview.heading("#7", text="Recompensa")
        
        self.treeview.bind('<ButtonRelease-1>', self.selecionar_pirata)
        self.procurar_entry.bind('<Return>', self.procurar_pirata)
        
        self.treeview.place(relx=0, rely=0, relwidth=1, relheight=1)
        x_scrollbar = ttk.Scrollbar(self.root, orient="horizontal", command=self.treeview.xview)
        x_scrollbar.place(x=0, y=800, relwidth=1)
        self.treeview.configure(xscrollcommand=x_scrollbar.set, xscroll="auto")
        
        self.escrever_tabela()

    def obter_nome_cadastro(self):
        return self.LG_Cadastro_entry.get()

    def obter_senha_cadastro(self):
        return self.SN_Cadastro_entry.get()

    def obter_nome_login(self):
        return self.id_entry.get()
    
    def obter_senha_login(self):
        return self.senha_entry.get()

    def limpar_campos_cadastro(self):
        self.LG_Cadastro_entry.delete(0, tk.END)
        self.SN_Cadastro_entry.delete(0, tk.END)

    def fechartela(self):
        self.root.destroy()
    
    def exibir_tela(self):
        self.root.mainloop()

    def abrir_tela_comum(self):
        self.tela_comum()

    def abrir_tela_adm(self):
        self.Tela_adm()
        
    def escrever_tabela(self, busca_pirata = ""):
        piratas = self.controller.buscar_piratas(busca_pirata)
        self.treeview.delete(*self.treeview.get_children())

        if piratas == None:
            return

        # Inserir todos os piratas no TreeView
        if type(piratas) == dict:
            self.treeview.insert("", "end", values=list(piratas.values()))            
        else :
            for pirata in piratas :
                self.treeview.insert("", "end", values=list(pirata.values()))

    def deletar_pirata(self):
        pirata = self.treeview.item(self.treeview.focus())
        self.controller.deletar_pirata(pirata["values"][1])

    def inserir_pirata(self):
        self.controller.inserir_pirata(self.nomePirata_entry.get(), self.Akumanomi_entry.get(), self.haki_entry.get(), self.tripulacao_entry.get(), self.arma_entry.get(), self.recompensa_entry.get())
       
    def selecionar_pirata(self, p):
        pirata_selecionado = self.treeview.item(self.treeview.focus())["values"]
        
        if pirata_selecionado:
            self.nomePirata_entry.delete(0, tk.END)
            self.nomePirata_entry.insert(0, pirata_selecionado[1])
            
            self.Akumanomi_entry.delete(0, tk.END)
            self.Akumanomi_entry.insert(0, pirata_selecionado[2])
            
            self.haki_entry.delete(0, tk.END)
            self.haki_entry.insert(0, pirata_selecionado[3])
            
            self.tripulacao_entry.delete(0, tk.END)
            self.tripulacao_entry.insert(0, pirata_selecionado[4])
            
            self.arma_entry.delete(0, tk.END)
            self.arma_entry.insert(0, pirata_selecionado[5])
            
            self.recompensa_entry.delete(0, tk.END)
            self.recompensa_entry.insert(0, pirata_selecionado[6])
        
    def editar_pirata(self):
        self.controller.editar_pirata(self.treeview.item(self.treeview.focus())["values"][0], self.nomePirata_entry.get(), self.Akumanomi_entry.get(), self.haki_entry.get(), self.tripulacao_entry.get(), self.arma_entry.get(), self.recompensa_entry.get())
    
    def procurar_pirata(self, p):
        self.escrever_tabela(self.procurar_entry.get())