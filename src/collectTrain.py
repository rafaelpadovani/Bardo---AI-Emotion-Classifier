import codecs

def collectTrain(emotion, episodio):
    if emotion == 'calm':
        calmFile = codecs.open("data/train/calmep"+str(episodio)+".txt", 'r', 'utf-8')
        calm = []
        for line in calmFile:
            lista = line.split(' ')
            for word in lista:
                if word != '\n':
                    calm.append(word)

        return calm
    
    elif emotion == 'happy':
        happyFile = codecs.open("data/train/happyep"+str(episodio)+".txt", 'r', 'utf-8')
        happy = []
        for line in happyFile:
            lista = line.split(' ')
            for word in lista:
                if word != '\n':
                    happy.append(word)

        return happy

    elif emotion == 'suspense':
        suspenseFile = codecs.open("data/train/suspenseep"+str(episodio)+".txt", 'r', 'utf-8')
        suspense = []
        for line in suspenseFile:
            lista = line.split(' ')
            for word in lista:
                if word != '\n':
                    suspense.append(word)

        return suspense

    else:
        agitatedFile = codecs.open("data/train/agitatedep"+str(episodio)+".txt", 'r', 'utf-8')
        agitated = []
        for line in agitatedFile:
            lista = line.split(' ')
            for word in lista:
                if word != '\n':
                    agitated.append(word)

        return agitated



