from collectTrain import collectTrain
from geraNBTable import geraTabela


def gerarTabelas(episodio, episodios):
    calm = []
    happy = []
    suspense = []
    agitated = []
    calm1 = []
    happy = []
    suspense1 = []
    agitated1 = []

    for i in range (0, len(episodios)):
        if episodios[i] != episodio:
            calm1 = collectTrain('calm', episodios[i])
            happy1 = collectTrain('happy', episodios[i])
            suspense1 = collectTrain('suspense', episodios[i])
            agitated1 = collectTrain('agitated', episodios[i])


            calm = calm + calm1
            happy = happy + happy1
            suspense = suspense + suspense1
            agitated = agitated + agitated1
        

    tabela = geraTabela(calm, happy, suspense, agitated)

    return tabela


