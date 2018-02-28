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

resultEp = codecs.open('testesNBJD/resultEp'+str(episodioTeste)+'.txt', 'w', 'utf-8')
classificationEp = codecs.open('testesNBJD/classificationEp'+str(episodioTeste)+'.txt', 'w', 'utf-8')

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
                    if situation == 1:
                        linhas[linha-1]['emotion'] = 'calm'
                    elif situation == 2:
                        linhas[linha-1]['emotion'] = 'happy'
                    elif situation == 3:
                        linhas[linha-1]['emotion'] = 'suspense'
                    else:
                        linhas[linha-1]['emotion'] = 'agitated'

                if linha >= janela:
                    for y in range(inicio, linha):
                        for b in range(0, len(linhas[y]['arranjo'])): 
                            arrayWindow.append(linhas[y]['arranjo'][b])
                    #print()
                    situation, prob = classificadorNaive2(arrayWindow, tabela, priori)
                    arrayWindow = []
                    if situation == 1:
                        linhas[linha-1]['emotion'] = 'calm'
                        linhas[linha-1]['prob'] = prob
                        atual = 'calm'
                    elif situation == 2:
                        linhas[linha-1]['emotion'] = 'happy'
                        linhas[linha-1]['prob'] = prob
                        atual = 'happy'
                    elif situation == 3:
                        linhas[linha-1]['emotion'] = 'suspense'
                        linhas[linha-1]['prob'] = prob
                        atual = 'suspense'
                    else:
                        linhas[linha-1]['emotion'] = 'agitated'
                        linhas[linha-1]['prob'] = prob
                        atual = 'agitated'
                        

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
            if contArray <= 5:
                precisaoArray.append(resultado)
                arrayFinal.append({'janela' : janela, 'limiar' : limiar, 'precisao' : precisaoArray})
                contArray = contArray + 1
                precisaoArray = []
            else:
                arrayFinal[cont]['precisao'].append(resultado)
                cont = cont + 1
            

            print(str(rpg_ec.calculate_accuracy(confusion_matrix)), 'Limiar:',' ', str(limiar), 'Janela:',' ', str(janela))

maiorPrecisao = 0
limiarFinal = 0
janelaFinal = 0
for indice in range(0, len(arrayFinal)):
    media = sum(arrayFinal[indice]['precisao'])/7
    if media > maiorPrecisao:
        maiorPrecisao = media
        limiarFinal = arrayFinal[indice]['limiar']
        janelaFinal = arrayFinal[indice]['janela']

janela = janelaFinal
limiar = limiarFinal



#for episodio in range(1, (numepisodios+1)):
print('Testando episodio ', episodioTeste)
tabela = gerarTabelas(episodioTeste, episodios)

priori = calculaPrior(episodioTeste, episodios)


ep = codecs.open('data/test/limpos/ep'+str(episodioTeste)+'.txt', 'r', 'utf-8')

classification = {}
linhas = []
linha = 0
inicio = 0

for i, line in enumerate(ep):
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
        if situation == 1:
            linhas[linha-1]['emotion'] = 'calm'
        elif situation == 2:
            linhas[linha-1]['emotion'] = 'happy'
        elif situation == 3:
            linhas[linha-1]['emotion'] = 'suspense'
        else:
            linhas[linha-1]['emotion'] = 'agitated'
    if linha >= janela:
        for y in range(inicio, linha):
            for b in range(0, len(linhas[y]['arranjo'])): 
                arrayWindow.append(linhas[y]['arranjo'][b])
        #print()
        situation, prob = classificadorNaive2(arrayWindow, tabela, priori)
        arrayWindow = []
        if situation == 1:
            linhas[linha-1]['emotion'] = 'calm'
            linhas[linha-1]['prob'] = prob
            atual = 'calm'
        elif situation == 2:
            linhas[linha-1]['emotion'] = 'happy'
            linhas[linha-1]['prob'] = prob
            atual = 'happy'
        elif situation == 3:
            linhas[linha-1]['emotion'] = 'suspense'
            linhas[linha-1]['prob'] = prob
            atual = 'suspense'
        else:
            linhas[linha-1]['emotion'] = 'agitated'
            linhas[linha-1]['prob'] = prob
            atual = 'agitated'
            

        inicio = inicio + 1

for x in range(0, len(linhas)):
    str1 = ' '.join(linhas[x]['arranjo'])
    classification[x+1] = (str1, str(linhas[x]['emotion']))
    
    #classificationEp.write(str(linhas[x]['identi'])+':')
    classificationEp.write(str(x+1)+':')
    for a in range(0, len(linhas[x]['arranjo'])):
        if a == len(linhas[x]['arranjo'])-1:
            string = str(linhas[x]['arranjo'][a])
            string = string.replace('\n','')
            classificationEp.write(string)
            #classificationEp.write(str(linhas[x]['arranjo'][a]))
        else:
            classificationEp.write(str(linhas[x]['arranjo'][a]+' '))
    classificationEp.write(':'+str(linhas[x]['emotion']))
    classificationEp.write("\n")

                
narrative = rpg_ec.parse_narrative_data('datasets/ep'+str(episodioTeste)+'.txt')

confusion_matrix = rpg_ec.rpg_create_confusion_matrix(narrative, classification)

resultado = rpg_ec.calculate_accuracy(confusion_matrix)
resultEp.write(str(resultado)+' ')
resultEp.write('Limiar:'+' '+ str(limiar)+' ')
resultEp.write('Janela:'+' '+ str(janela))
resultEp.write("\n")
resultEp.write("\n")
print('Resultado Teste: %d: Precisao e Janela' %episodioTeste)
print(str(resultado), 'Janela:',' ', str(janela))


