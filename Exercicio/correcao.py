
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neural_network import MLPClassifier


class NeuralNetwork():

    df = None
    rede = None

    def __init__(self, file=None):
        self.df = pd.read_csv(file)

        print(self.df.bought.value_counts())

        SEED = 20
        np.random.seed = SEED

        x = self.df.drop('bought', axis=1)

        y = self.df.bought

        treino_x, teste_x, treino_y, teste_y = train_test_split(
            x, y, test_size=0.25, stratify=y)

        self.rede = MLPClassifier()

        self.rede.fit(treino_x, treino_y)

        previsoes_y = self.rede.predict(teste_x)

        print(accuracy_score(teste_y, previsoes_y))
        print(confusion_matrix(teste_y, previsoes_y))

        self.menu()

    def menu(self):
        os.system("cls")

        print("#### Previsão de compras por usuario ####")

        print("#### Usuário acessou a página home(0-1)? ####")
        home = int(input())

        print("#### Usuário acessou a página como funciona? ####")
        how = int(input())

        print("#### Usuário acessou a página de contato? ####")
        contact = int(input())
        previsao = self.rede.predict([[home, how, contact]])

        print("ESSE USUARIO COMPRA OU NAO ? -> {}".format(previsao))


rede = NeuralNetwork("tracking.csv")
