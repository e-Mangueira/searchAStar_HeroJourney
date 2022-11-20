import numpy as np

class Ilha:
     def __init__(self, no, poderDeLuta):
         self.no = no
         self.visitado = False
         self.poderDeLuta = poderDeLuta
         self.adjacentes = []

     def adiciona_adjacente(self, adjacente):
            self.adjacentes.append(adjacente)

     def visualiza_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.objetivo, i.distancia_lugar)

class Adjacente:

    def __init__(self, ilha, distancia_lugar):
        self.ilha = ilha
        self.distancia_lugar = distancia_lugar

        self.aestrela = ilha.poderDeLuta + self.distancia_lugar #heuristica

class Jornada:
    chefao1 = Ilha('Chefão1', 30) # A
    chefao2 = Ilha('Chefão2', 26) # B
    chefao3 = Ilha('Chefão3', 21) # C
    chefao4 = Ilha('Chefão4', 7) # D
    chefao5 = Ilha('Chefão5', 22) # E
    chefao6 = Ilha('Chefão6', 36) # F
    princesa = Ilha('Princesa', 0) # G

    chefao1.adiciona_adjacente(Adjacente(chefao2, 12)) # B
    chefao1.adiciona_adjacente(Adjacente(chefao3, 14)) # C

    chefao2.adiciona_adjacente(Adjacente(chefao3, 9)) # C
    chefao2.adiciona_adjacente(Adjacente(chefao4, 38))  # D

    chefao3.adiciona_adjacente(Adjacente(chefao4, 24))  # D
    chefao3.adiciona_adjacente(Adjacente(chefao5, 7))  # E

    chefao4.adiciona_adjacente(Adjacente(princesa, 9))  # G

    chefao5.adiciona_adjacente(Adjacente(chefao4, 13))  # D
    chefao5.adiciona_adjacente(Adjacente(chefao6, 9))  # F
    chefao5.adiciona_adjacente(Adjacente(princesa, 29))  # G

jornada = Jornada()


class VetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        #Mudança no tipo de dados
        self.valores = np.empty(self.capacidade, dtype=object)

    # Referência para o vértice e comparação com a distância para o objetivo
    def insere(self, adjacente):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].aestrela > adjacente.aestrela:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x+1] = self.valores[x]
            x -= 1
        self.valores[posicao] = adjacente
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print( '-', self.valores[i].ilha.no, '->',
                        self.valores[i].distancia_lugar, '+',
                        self.valores[i].ilha.poderDeLuta, '=',
                        self.valores[i].aestrela)

jornada.chefao1.adjacentes
jornada.chefao1.adjacentes[0].ilha.no, jornada.chefao1.adjacentes[0].ilha.poderDeLuta
jornada.chefao1.adjacentes[0].aestrela, jornada.chefao1.adjacentes[0].distancia_lugar

vetor = VetorOrdenado(20)
vetor.insere(jornada.chefao1.adjacentes[0])
vetor.insere(jornada.chefao1.adjacentes[1])


#vetor.imprime()

class AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('----------------')
        print('Posição Atual: {} \n' .format(atual.no))
        atual.visitado = True
        if atual == self.objetivo:
            self.encontrado = True

        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if adjacente.ilha.visitado == False:
                    adjacente.ilha.visitado = True
                    vetor_ordenado.insere(adjacente)
            vetor_ordenado.imprime()

            if vetor.valores[0] != None:
                self.buscar(vetor_ordenado.valores[0].ilha)

busca_aestrela = AEstrela(jornada.princesa)
busca_aestrela.buscar(jornada.chefao1)