from gerarTabelas import gerarTabelas
from calculaPrior import calculaPrior
from NaiveBayes2 import classificadorNaive2
import codecs
#import nltk
#from nltk.tokenize import sent_tokenize, word_tokenize
import rpg_ec
import operator
import collections
import sys

##episodioTeste = int(input('Testar qual episódio? '))
##
##numepisodios = int(input('Quantos episódios? '))
episodioTeste = int(sys.argv[1])

numepisodios = 9

limiar = 0

episodios = []

logs = codecs.open('testesNS/LogEp'+str(episodioTeste)+'.txt', 'w', 'utf-8')
logs.write('Precisao, Janela, K, Transicoes')
logs.write('\n')

for j in range(1, (numepisodios+1)):
    if j != episodioTeste:
        episodios.append(j)

#episodios.pop(episodioTeste-1)

print('Testar com episodio ', episodioTeste)
print('Validar com episodios ', episodios)

resultEp1Accura = []
limiarArray = []
janelaArray = []
contArray = 0
arrayFinal = []
precisaoArray = []
#Validacao Cruzada
#Gerar tabelas

################################################
#TRANSITIONS EPISODES
TransEps = [7, 8, 5, 12, 8, 9, 4, 6, 4]


for episodio in range(1, (numepisodios+1)):
    tabela = []
    priori = []
    if episodio != episodioTeste:
        print('Validando episodio ', episodio)
        tabela = gerarTabelas(episodio, episodios)

        priori = calculaPrior(episodio, episodios)

        resultEp1Accura = []
        limiarArray = []
        janelaArray = []

        array = []
        identi = 0
        linha = 0
        linhas = []
        inicio = 0
        arrayWindow = []
        atual = 'calm'
        limiar = 0
        classification = {}

        vari = 0
        cont = 0
        #for line in ep1:
        for m in range(20, 41, 5):
        #for m in range(25, 30, 5):
            janela = m
            ep1 = codecs.open('data/test/limpos/ep'+str(episodio)+'.txt', 'r', 'utf-8')
            classification = {}
            linhas = []
            linha = 0
            inicio = 0

            atualTrans = 1
            cont = 0
            transition = 0

            for i, line in enumerate(ep1):
                identi = identi+1
                array = []
                linha = linha + 1
                #lista = word_tokenize(line)
                lista = line.split(' ')
                for word in lista:
                    array.append(word)
                linhas.append({'identi' : identi, 'arranjo' : array})
                if linha < janela:
                    situation, prob = classificadorNaive2(array, tabela, priori)
                    if atualTrans != situation and cont>0:
                        transition = transition + 1
                    if situation == 1:
                        linhas[linha-1]['emotion'] = 'calm'
                        atualTrans = 1
                    elif situation == 2:
                        linhas[linha-1]['emotion'] = 'happy'
                        atualTrans = 2
                    elif situation == 3:
                        linhas[linha-1]['emotion'] = 'suspense'
                        atualTrans = 3
                    else:
                        linhas[linha-1]['emotion'] = 'agitated'
                        atualTrans = 4

                    cont = cont + 1

                if linha >= janela:
                    for y in range(inicio, linha):
                        for b in range(0, len(linhas[y]['arranjo'])):
                            arrayWindow.append(linhas[y]['arranjo'][b])
                    #print()
                    situation, prob = classificadorNaive2(arrayWindow, tabela, priori)
                    arrayWindow = []
                    if atualTrans != situation and cont>0:
                        transition = transition + 1
                    if situation == 1:
                        linhas[linha-1]['emotion'] = 'calm'
                        linhas[linha-1]['prob'] = prob
                        atual = 'calm'
                        atualTrans = 1
                    elif situation == 2:
                        linhas[linha-1]['emotion'] = 'happy'
                        linhas[linha-1]['prob'] = prob
                        atual = 'happy'
                        atualTrans = 2
                    elif situation == 3:
                        linhas[linha-1]['emotion'] = 'suspense'
                        linhas[linha-1]['prob'] = prob
                        atual = 'suspense'
                        atualTrans = 3
                    else:
                        linhas[linha-1]['emotion'] = 'agitated'
                        linhas[linha-1]['prob'] = prob
                        atual = 'agitated'
                        atualTrans = 4

                    cont = cont + 1

                    inicio = inicio + 1



            for x in range(0, len(linhas)):
                str1 = ' '.join(linhas[x]['arranjo'])
                classification[x+1] = (str1, str(linhas[x]['emotion']))


            narrative = rpg_ec.parse_narrative_data('datasets/ep'+str(episodio)+'.txt')

            confusion_matrix = rpg_ec.rpg_create_confusion_matrix(narrative, classification)

            resultado = rpg_ec.calculate_accuracy(confusion_matrix)
##                resultEp1Accura.append(resultado)
##                limiarArray.append(limiar)
##                janelaArray.append(janela)

            DifTransicao = 0
            def calculateDifference(transition, episodio, TransEps):
                DifTrans = 0
                if transition >= TransEps[episodio-1]:
                    DifTrans = transition - TransEps[episodio-1]
                elif transition < TransEps[episodio-1]:
                    DifTrans = TransEps[episodio-1] - transition
                return DifTrans

            DifTransicao = calculateDifference(transition, episodio, TransEps)

            print(str(rpg_ec.calculate_accuracy(confusion_matrix)), 'Janela: ', str(janela), 'DifTransicao: ', str(DifTransicao))


            logs.write(str(resultado)+':')
            logs.write(str(janela)+':')
            logs.write(str(DifTransicao))
            logs.write("\n")

            DifTransicao = 0
