import math

def NHM( Test2, tabela, priori, k, listaAtributes):

    stopWords = ["The", "the", "the", "as", "one", "one", "some", "some", "in", "for", "of" , "i", "re", "nt", "s", "so",
    "with", "without", "is", "are", "up", "yet", "when", "how", "where", "but", "but", "yet", "yet", "and", "or", "it",
    "To", "to", "to", "to", "as", "some", "some", "some", "some", "your", "your", "No", "us","na", "uh", "oh", "m", "ll",
    "None", "none", "none", "there", "there", "there", "this", "these", "this", "these", "these ", "Those", "his", "her",
    "That", "those", "those", "those", "that", "those", "those", "why", "why", "what", "what", "why", "yes", "Nor",
    "Never", "always", "therefore", "thus", "then", "this", "this", "this", "this", "these", "these", "these", "ve",
    "By", "by", "by", "if", "each", "which", "which", "already", "where", "However", "On", "o", "a", "the", "as",
    "after", "until", "with", "against", "from", "from","Between", "for", "before", "By", "without", "under", "on",
    "behind", "an", "numas", "and", "One", "one", "I", "you", "he", "we", "you", "they", "my", "my", "mine", "mine",
    "yours", "yours","You", "you", "you", "You", "you", "have", "had", "will", "will", "me", "what", "t", "d", "at",
    "how many", "how much", "say", "said", "plus", "She", "they", "see", "see", "saw", "saw", "and", "where", "by",
    "Are", "were", "were", "If", "me", "me", "with me", "te", "you", "you", "if", "if", "with", "with", "with", "Them",
    "this", "These", "those", "those", "these", "these", "these", "these", "this", "that", "those", "also", "to", "was",
    "Will", "will", "will", "own", "own", "own", "own", "own", "already", "here", "there", "but", "however", "however",
    "however", "or", "be", "why", "for", "what", "alias", "before", "after", "then", "Only", "only", "up", "still", "beyond",
    "beyond", "this", "including", "example", "Even", "only", "here", "where", "right", "left", "behind",
    "Above", "way", "doubt", "maybe", "below", "above", "once", "when", "both", "In", "give", "give", "give", "now",
    "after", "wanted", "want", "wanted", "mostly", "opened", "created", "Arrived", "arrived", "owner", "outside", "corner",
    "side", "to", "singing", "sent", "want", "where", "come", "Many", "niece", "time", "leaves", "painting", "ask", "ask",
    "many", "Each", "pieces"]


    PCalm = 0
    PHappy = 0
    PSuspense = 0
    PAgitated = 0


    PCalm = 1
    PHappy = 1
    PSuspense = 1
    PAgitated = 1

    # --------------------------------
    # ------Test sem repetições-------
    # --------------------------------
    TestSemRep = []

    for i in range(0, len(Test2)):
        if not Test2[i] in stopWords:
            TestSemRep.append(Test2[i])


    #PREPARE LISTS BASED ON K
    def prepareLists(lista, listaAtrib, k):
        if len(listaAtrib) < k:
            lista = listaAtrib
            return lista
        else:
            for i in range(0, k):
                lista.append(listaAtrib[i])
            return lista
    calmA = []
    happyA = []
    suspenseA = []
    agitatedA = []
    calmA = prepareLists(calmA, listaAtributes[0], k)
    happyA = prepareLists(happyA, listaAtributes[1], k)
    suspenseA = prepareLists(suspenseA, listaAtributes[2], k)
    agitatedA = prepareLists(agitatedA, listaAtributes[3], k)
    listaTotal = calmA + happyA + suspenseA + agitatedA


    # --------------------------------
    # --------------------------------
    # --------------------------------

    freq = 0
    naiveCalm = []
    naiveHappy = []
    naiveSuspense = []
    naiveAgitated = []
    powCalm = 0
    powHappy = 0
    powSuspense = 0
    powAgitated = 0
    for i in range(0, len(TestSemRep)):
        freq = 0
        powCalm = 0
        powHappy = 0
        powSuspense = 0
        powAgitated = 0
        palavra = TestSemRep[i]
        #contagem de frequencia
        for y in range(0, len(Test2)):
            if palavra == Test2[y]:
                freq = freq + 1
        for j in range(0, len(tabela)):
            if palavra == tabela[j]['palavra']:
                if palavra in listaTotal:
                    naiveCalm.append(tabela[j]['calculoCalm'])
                if palavra in listaTotal:
                    naiveHappy.append(tabela[j]['calculoHappy'])
                if palavra in listaTotal:
                    naiveSuspense.append(tabela[j]['calculoSuspense'])
                if palavra in listaTotal:
                    naiveAgitated.append(tabela[j]['calculoAgitated'])
                break



    for i in range(0, len(naiveCalm)):
        PCalm = PCalm + math.log(naiveCalm[i])

    PCalm = PCalm + math.log(priori[0])


    for i in range(0, len(naiveHappy)):
        PHappy = PHappy + math.log(naiveHappy[i])

    PHappy = PHappy + math.log(priori[1])


    for i in range(0, len(naiveSuspense)):
        PSuspense = PSuspense + math.log(naiveSuspense[i])

    PSuspense = PSuspense + math.log( priori[2])


    for i in range(0, len(naiveAgitated)):
        PAgitated = PAgitated + math.log(naiveAgitated[i])

    PAgitated = PAgitated + math.log(priori[3])


    maior = 0
    selecionado = 0
    maior = max(PCalm, PHappy, PSuspense, PAgitated)

    if maior == PCalm:
        selecionado = 1
    elif maior == PHappy:
        selecionado = 2
    elif maior == PSuspense:
        selecionado = 3
    else:
        selecionado = 4


    return selecionado
