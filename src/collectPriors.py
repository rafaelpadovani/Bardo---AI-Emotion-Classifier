import codecs

def collectPriors(emotion, episodio):
    if emotion == 'calm':
        calmFile = codecs.open("data/train/calmep"+str(episodio)+".txt", 'r', 'utf-8')
        contCalm = 0
        for line in calmFile:
            contCalm = contCalm + 1

        return contCalm
    
    elif emotion == 'happy':
        happyFile = codecs.open("data/train/happyep"+str(episodio)+".txt", 'r', 'utf-8')
        contHappy = 0
        for line in happyFile:
            contHappy = contHappy + 1

        return contHappy

    elif emotion == 'suspense':
        suspenseFile = codecs.open("data/train/suspenseep"+str(episodio)+".txt", 'r', 'utf-8')
        contSuspense = 0
        for line in suspenseFile:
            contSuspense = contSuspense + 1

        return contSuspense

    else:
        agitatedFile = codecs.open("data/train/agitatedep"+str(episodio)+".txt", 'r', 'utf-8')
        contAgitated = 0
        for line in agitatedFile:
            contAgitated = contAgitated + 1

        return contAgitated



