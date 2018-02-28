from gerarTabelas import gerarTabelas
from calculaPrior import calculaPrior
from NS import NS
from NHS import NHS
from NM import NM
from NHM import NHM
import codecs
import rpg_ec
import operator
import collections
import sys
import random


episodioTeste = int(sys.argv[1])

numepisodios = 9

limiar = 0

episodios = []

resultEp = codecs.open('testesNSALL/resultEp'+str(episodioTeste)+'.txt', 'w', 'utf-8')
classificationEp = codecs.open('testesNSALL/classificationEp'+str(episodioTeste)+'.txt', 'w', 'utf-8')

for j in range(1, (numepisodios+1)):
    if j != episodioTeste:
        episodios.append(j)

print('Testar com episodio ', episodioTeste)
print('Validar com episodios ', episodios)

resultEp1Accura = []
limiarArray = []
janelaArray = []
contArray = 0
arrayFinal = []
precisaoArray = []

############# GET ATRIBUTES LISTS ##############
happyFile = codecs.open('happyFile.txt', 'r', 'utf-8')
happyAtrib = []
for line in happyFile:
    lista = line.split('\n')
    happyAtrib.append(lista[0])

calmFile = codecs.open('calmFile.txt', 'r', 'utf-8')
calmAtrib = []
for line in calmFile:
    lista = line.split('\n')
    calmAtrib.append(lista[0])

suspenseFile = codecs.open('suspenseFile.txt', 'r', 'utf-8')
suspenseAtrib = []
for line in suspenseFile:
    lista = line.split('\n')
    suspenseAtrib.append(lista[0])

agitatedFile = codecs.open('agitatedFile.txt', 'r', 'utf-8')
agitatedAtrib = []
for line in agitatedFile:
    lista = line.split('\n')
    agitatedAtrib.append(lista[0])

listaAtributes = []
listaAtributes.append(calmAtrib)
listaAtributes.append(happyAtrib)
listaAtributes.append(suspenseAtrib)
listaAtributes.append(agitatedAtrib)

################################################

################### MODELS #####################

NSarray = [{'janela':25}, {'janela':20}, {'janela':20},
           {'janela':20}, {'janela':35}, {'janela':20},
           {'janela':20}, {'janela':25}, {'janela':25}]

NHSarray = [{'janela':25, 'k':500}, {'janela':30, 'k':500}, {'janela':25, 'k':500},
       {'janela':25, 'k':500}, {'janela':30, 'k':500}, {'janela':40, 'k':500},
        {'janela':25, 'k':500}, {'janela':25, 'k':500}, {'janela':30, 'k':500}]

NMarray = [{'janela':30}, {'janela':25}, {'janela':35},
            {'janela':25}, {'janela':40}, {'janela':40},
            {'janela':25}, {'janela':30}, {'janela':25}]

NHMarray = [{'janela':25, 'k':1140}, {'janela':30, 'k':500}, {'janela':25, 'k':540},
         {'janela':25, 'k':510}, {'janela':40, 'k':520}, {'janela':25, 'k':530},
         {'janela':30, 'k':570}, {'janela':40, 'k':520}, {'janela':30, 'k':500}]

janelaNS = NSarray[episodioTeste-1]['janela']
janelaNHS = NHSarray[episodioTeste-1]['janela']
janelaNM = NMarray[episodioTeste-1]['janela']
janelaNHM = NHMarray[episodioTeste-1]['janela']
kvalueNHS = NHSarray[episodioTeste-1]['k']
kvalueNHM = NHMarray[episodioTeste-1]['k']

################################################

#TRANSITIONS EPISODES
TransEps = [7, 8, 5, 12, 8, 9, 4, 6, 4]


print('Testando episodio ', episodioTeste)
tabela = gerarTabelas(episodioTeste, episodios)

priori = calculaPrior(episodioTeste, episodios)


ep = codecs.open('data/test/limpos/ep'+str(episodioTeste)+'.txt', 'r', 'utf-8')

classification = {}
linhas = []
linha = 0
inicio = 0
identi = 0
arrayWindow = []

atualTrans = 1
cont = 0
transition = 0

arrayWindowNS = []
arrayWindowNHS = []
arrayWindowNM = []
arrayWindowNHM = []
mudou = False

for i, line in enumerate(ep):
    identi = identi+1
    array = []
    linha = linha + 1
    lista = line.split(' ')
    for word in lista:
        array.append(word)
    linhas.append({'identi' : identi, 'arranjo' : array})

    #arrayWindowNS
    if linha < janelaNS:
        for y in range(0, linha):
            for b in range(0, len(linhas[y]['arranjo'])):
                arrayWindowNS.append(linhas[y]['arranjo'][b])
    elif linha >= janelaNS:
        for y in range(linha-janelaNS, linha):
            for b in range(0, len(linhas[y]['arranjo'])):
                arrayWindowNS.append(linhas[y]['arranjo'][b])

    #arrayWindowNHS
    if linha < janelaNHS:
        for y in range(0, linha):
            for b in range(0, len(linhas[y]['arranjo'])):
                arrayWindowNHS.append(linhas[y]['arranjo'][b])
    elif linha >= janelaNHS:
        for y in range(linha-janelaNHS, linha):
            for b in range(0, len(linhas[y]['arranjo'])):
                arrayWindowNHS.append(linhas[y]['arranjo'][b])

    #arrayWindowNM
    if linha < janelaNM:
        for y in range(0, linha):
            for b in range(0, len(linhas[y]['arranjo'])):
                arrayWindowNM.append(linhas[y]['arranjo'][b])
    elif linha >= janelaNM:
        for y in range(linha-janelaNM, linha):
            for b in range(0, len(linhas[y]['arranjo'])):
                arrayWindowNM.append(linhas[y]['arranjo'][b])

    #arrayWindowNHM
    if linha < janelaNHM:
        for y in range(0, linha):
            for b in range(0, len(linhas[y]['arranjo'])):
                arrayWindowNHM.append(linhas[y]['arranjo'][b])
    elif linha >= janelaNHM:
        for y in range(linha-janelaNHM, linha):
            for b in range(0, len(linhas[y]['arranjo'])):
                arrayWindowNHM.append(linhas[y]['arranjo'][b])


    #NS
    situationNS = NS(arrayWindowNS, tabela, priori)
    arrayWindowNS = []
    #NHS
    situationNSK = NHS(arrayWindowNHS, tabela, priori, kvalueNHS, listaAtributes)
    arrayWindowNHS = []
    #NM
    situationNSMO = NM(arrayWindowNM, tabela, priori)
    arrayWindowNM = []
    #NHM
    situationNSKMO = NHM(arrayWindowNHM, tabela, priori, kvalueNHM, listaAtributes)
    arrayWindowNHM = []

    def checkTie(freq):
        a = 0
        b = 0
        tie = False
        for i in range(1, 5):
            for j in range(1, 5):
                if i != j:
                    if freq[i] == 2 and freq[j] == 2:
                        tie = True
                        a = i
                        b = j
        return tie, a, b

    def checkWinner(options):
        freq = {1:0, 2:0, 3:0, 4:0}
        semRep = []
        for i in range(0, 4):
            if options[i] not in semRep:
                semRep.append(options[i])
        for i in range(0, len(semRep)):
            for j in range(0, 4):
                if semRep[i] == options[j]:
                    freq[semRep[i]] = freq[semRep[i]] + 1
        tie = False
        a = 0
        b = 0
        tie, a, b = checkTie(freq)
        if tie == False:
            maior = 0
            choice = 0
            for i in range(1, 5):
                if freq[i] > maior:
                    maior = freq[i]
                    choice = i
        elif tie == True:
            choice = random.choice([a,b])
        return choice

    options = [situationNS, situationNSK, situationNSMO, situationNSKMO]

    situation = checkWinner(options)

    mudou = False
    if cont>0 and situationNS == situationNSK and situationNSK == situationNSMO and situationNSMO == situationNSKMO:
        if atualTrans != situation:
            transition = transition + 1
            mudou = True

    if mudou ==  False or cont == 0:
        if atualTrans == 1:
            linhas[linha-1]['emotion'] = 'calm'
            atualTrans = 1
            print('calm')
        elif atualTrans == 2:
            linhas[linha-1]['emotion'] = 'happy'
            atualTrans = 2
            print('happy')
        elif atualTrans == 3:
            linhas[linha-1]['emotion'] = 'suspense'
            atualTrans = 3
            print('suspense')
        elif atualTrans == 4:
            linhas[linha-1]['emotion'] = 'agitated'
            atualTrans = 4
            print('agitated')

        cont = cont + 1
    elif mudou == True:
        if situation == 1:
            linhas[linha-1]['emotion'] = 'calm'
            atualTrans = 1
            print('calm')
        elif situation == 2:
            linhas[linha-1]['emotion'] = 'happy'
            atualTrans = 2
            print('happy')
        elif situation == 3:
            linhas[linha-1]['emotion'] = 'suspense'
            atualTrans = 3
            print('suspense')
        elif situation == 4:
            linhas[linha-1]['emotion'] = 'agitated'
            atualTrans = 4
            print('agitated')

        cont = cont + 1
        mudou = False




for x in range(0, len(linhas)):
    str1 = ' '.join(linhas[x]['arranjo'])
    classification[x+1] = (str1, str(linhas[x]['emotion']))
    classificationEp.write(str(x+1)+':')
    for a in range(0, len(linhas[x]['arranjo'])):
        if a == len(linhas[x]['arranjo'])-1:
            string = str(linhas[x]['arranjo'][a])
            string = string.replace('\n','')
            classificationEp.write(string)
        else:
            classificationEp.write(str(linhas[x]['arranjo'][a]+' '))
    classificationEp.write(':'+str(linhas[x]['emotion']))
    classificationEp.write("\n")


narrative = rpg_ec.parse_narrative_data('datasets/ep'+str(episodioTeste)+'.txt')

confusion_matrix = rpg_ec.rpg_create_confusion_matrix(narrative, classification)

janela = 0
kvalue = 0

resultado = rpg_ec.calculate_accuracy(confusion_matrix)


DifTransicao = 0
def calculateDifference(transition, episodio, TransEps):
    DifTrans = 0
    if transition >= TransEps[episodio-1]:
        DifTrans = transition - TransEps[episodio-1]
    elif transition < TransEps[episodio-1]:
        DifTrans = TransEps[episodio-1] - transition
    return DifTrans

DifTransicao = calculateDifference(transition, episodioTeste, TransEps)

resultEp.write(str(resultado)+' ')
resultEp.write(str(DifTransicao))
resultEp.write("\n")
resultEp.write("\n")
print('Resultado Teste: %d: Precisao e Janela' %episodioTeste)
print(str(resultado), 'Transicoes: ', str(DifTransicao))
