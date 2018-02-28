from collectPriors import collectPriors

def calculaPrior(episodio, episodios):
    priors = []
    #priorCalm
    calm1 = 0
    happy1 = 0
    suspense1 = 0
    agitated1 = 0
    priorCalm = 0
    calm = 0
    happy = 0
    suspense = 0
    agitated = 0
    total = 0
    for i in range (0, len(episodios)):
        if i != episodio:
            calm1 = collectPriors('calm', episodios[i])
            happy1 = collectPriors('happy', episodios[i])
            suspense1 = collectPriors('suspense', episodios[i])
            agitated1 = collectPriors('agitated', episodios[i])

            calm = calm + calm1
            if calm == 0:
                calm = 1
            happy = happy + happy1
            if happy == 0:
                happy = 1
            suspense = suspense + suspense1
            if suspense == 0:
                suspense = 1
            agitated = agitated + agitated1
            if agitated == 0:
                agitated = 1

    total = calm + happy + suspense + agitated

    priors.append(calm/total)
    priors.append(happy/total)
    priors.append(suspense/total)
    priors.append(agitated/total)

    return priors
            

    
