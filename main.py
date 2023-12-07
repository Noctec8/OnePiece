# Arquivo: main.py
from Model import Model
from Controller import Controller
from Viewer import Viewer

controlador = Controller()
modelo = Model()
visualizador = Viewer(controlador)
controlador.referenciar_view_model(modelo, visualizador)

visualizador.exibir_tela()