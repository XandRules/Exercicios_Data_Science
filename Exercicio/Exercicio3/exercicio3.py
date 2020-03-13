
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neural_network import MLPClassifier
import math
import matplotlib.pyplot as plt


class NeuralNetwork():

    df = None
    rede = None

    def __init__(self, file=None):
        self.df = pd.read_csv(file)

        print(self.df.shape)

        self.menu()

    def exibirDadosOriginais(self):
        print(self.df.head())
        print(self.df.shape)
        print(self.df.describe())

    def exibirGrafico(self):
        print('Gráfico')

    def menu(self):

        inputMenu = None

        while inputMenu != 9:
            os.system("cls")

            print("#### Rede Neural Para Previsão de Produtores de Vinho ####")
            print("#### 1 - Exibir dados originais e estatísticas ####")
            print(
                "#### 2 - Imprimir gráfico de Teor Alcóolico / Magnésio / Fenóis por Produtor ####")
            print("#### 3 - Exibir Previsão da Rede Neural ####")
            inputMenu = int(input())

            if inputMenu == 1:
                print("dados Originais")
                self.exibirDadosOriginais()

            if inputMenu == 2:
                self.exibirGrafico()

            if inputMenu == 3:
                print("Previsão")

            print("Pressione qualquer tecla...")
            input()


rede = NeuralNetwork("wine.csv")
