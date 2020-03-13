
import os


class NeuralNetwork():

    df = None
    rede = None

    def __init__(self, file=None):
        self.menu()

        # PORTA OU
        # [0,0] | resposta = 0
        # [0,1] | resposta = 1
        # [1,0] | resposta = 1
        # [1,1] | resposta = 1

        # PORTA AND
        # [0,0] | resposta = 0
        # [0,1] | resposta = 1
        # [1,0] | resposta = 1
        # [1,1] | resposta = 1

        x = [[0, 0], [0, 1], [1, 0], [1, 1]]

        respostaOU = [0, 1, 1, 1]
        respostaAND = [0, 1, 1, 1]

    def portaOU(self):

        print("#### Primeiro Valor( 0 - 1 ) ####")
        x1 = int(input())
        print("#### Segundo Valor( 0 - 1 ) ####")
        x2 = int(input())

        resposta = (x1 + x2) > 1

        if resposta == True:
            print("Saída é  1")

        elif resposta == False:
            print("Saída é  0")

    def portaAND(self):

        print("#### Primeiro Valor( 0 - 1 ) ####")
        x1 = int(input())
        print("#### Segundo Valor( 0 - 1 ) ####")
        x2 = int(input())

        resposta = (x1 * x2) > 1

        if resposta == True:
            print("Saída é  1")

        elif resposta == False:
            print("Saída é  0")

    def menu(self):

        inputMenu = None

        while inputMenu != 9:
            os.system("cls")

            print("#### 1 - Rede Neural Para Porta OU ####")
            print("#### 2 - Rede Neural Para Porta AND ####")

            inputMenu = int(input())

            if inputMenu == 1:
                self.portaOU()

            if inputMenu == 2:
                self.portaAND()

            print("Pressione qualquer tecla...")
            input()


rede = NeuralNetwork()


# RNA fazer pesquisa de Retro Propagação, Back Propagation para o dia 16/03

# Prova 26/03 prova e 30/03
