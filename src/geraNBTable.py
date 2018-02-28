import math

def geraTabela(argCalm, argHappy, argSuspense, argAgitated):


    PCalm = 0
    PHappy = 0
    PSuspense = 0
    PAgitated = 0


    PCalm = 1
    PHappy = 1
    PSuspense = 1
    PAgitated = 1

    TrainingCalm = []

    TrainingCalm = TrainingCalm + argCalm


    TrainingHappy = []

    TrainingHappy = TrainingHappy + argHappy


    TrainingSuspense = []

    TrainingSuspense = TrainingSuspense + argSuspense


    TrainingAgitated = []

    TrainingAgitated = TrainingAgitated + argAgitated


    totalCalm = 0
    for i in range(0, len(TrainingCalm)):
        totalCalm = totalCalm + 1

    print("Total Calm: ", totalCalm)

    totalHappy = 0
    for i in range(0, len(TrainingHappy)):
        totalHappy = totalHappy + 1

    print("Total Happy: ", totalHappy)

    totalSuspense = 0
    for i in range(0, len(TrainingSuspense)):
        totalSuspense = totalSuspense + 1

    print("Total Suspense: ", totalSuspense)

    totalAgitated = 0
    for i in range(0, len(TrainingAgitated)):
        totalAgitated = totalAgitated + 1

    print("Total Agitated: ", totalAgitated)


    totalGeral = totalCalm + totalHappy + totalSuspense + totalAgitated


    auxCalm = []

    auxHappy = []

    auxSuspense = []

    auxAgitated = []



    countCalm = []

    countHappy = []

    countSuspense = []

    countAgitated = []



    # ------------------------------------
    # -----Total sem repetições-----------
    # ------------------------------------
    TotalSemRep = []  #--Train sem repetições
    TotalTraining = []  #--Train total

    for i in range(0, len(TrainingCalm)):
        TotalTraining.append(TrainingCalm[i])


    for i in range(0, len(TrainingHappy)):
        TotalTraining.append(TrainingHappy[i])


    for i in range(0, len(TrainingSuspense)):
        TotalTraining.append(TrainingSuspense[i])


    for i in range(0, len(TrainingAgitated)):
        TotalTraining.append(TrainingAgitated[i])



    for i in range(0, len(TotalTraining)):
        if not TotalTraining[i] in TotalSemRep:
            TotalSemRep.append(TotalTraining[i])


    vocabulario = 0
    for i in range(0, len(TotalSemRep)):
        vocabulario = vocabulario + 1


    palavras = []

    #varrer Test sem repetições
    for i in range(0, len(TotalSemRep)):
        palavra = TotalSemRep[i]
        calculoCalm = 0
        calculoHappy = 0
        calculoSuspense = 0
        calculoAgitated = 0
        calculoNotCalm = 0
        calculoNotHappy = 0
        calculoNotSuspense = 0
        calculoNotAgitated = 0
        freq = 0
        #contagem da palavra em questão em Calm
        contCalm = 0
        for j in range(0, len(TrainingCalm)):
            if palavra == TrainingCalm[j]:
                contCalm = contCalm + 1

        calculoCalm = (contCalm+1)/(totalCalm+vocabulario)
        #contagem da palavra em questão em Happy
        contHappy = 0
        for j in range(0, len(TrainingHappy)):
            if palavra == TrainingHappy[j]:
                contHappy = contHappy + 1

        calculoHappy = (contHappy+1)/(totalHappy+vocabulario)
        #contagem da palavra em questão em Happy
        contSuspense = 0
        for j in range(0, len(TrainingSuspense)):
            if palavra == TrainingSuspense[j]:
                    contSuspense = contSuspense + 1

        calculoSuspense = (contSuspense+1)/(totalSuspense+vocabulario)
        #contagem da palavra em questão em Agitated
        contAgitated = 0
        for j in range(0, len(TrainingAgitated)):
            if palavra == TrainingAgitated[j]:
                contAgitated = contAgitated + 1

        calculoAgitated = (contAgitated+1)/(totalAgitated+vocabulario)

        #-----------------------

        #insert multiple
        palavras.append({'palavra' : palavra, 'calculoCalm' : calculoCalm, 'calculoHappy' : calculoHappy, 'calculoSuspense' : calculoSuspense, 'calculoAgitated' : calculoAgitated})


    return palavras
