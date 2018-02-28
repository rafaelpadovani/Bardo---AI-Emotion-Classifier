#-----------------------------------------------------------
# Name: rpg_density.py
# Calculate Emotion Word Density using NRC Emotion Lexicon
# Author: Lucas N. Ferreira
# E-mail: lferreira@ucsc.edu
#-----------------------------------------------------------

import sys
import operator
import collections
import rpg_ec

# General classes of emotions
NRC_EMOTIONS = ["anger", "anticipation", "disgust", "fear", "joy", "sadness", "surprise", "trust"]

# Mapping NRC emotions to RPG emotions
EMOTION_MAP = {
    "anger"       : "agitated",
    "fear"        : "suspense",
    "sadness"     : "agitated",
    # "disgust"     : "agitated",
    "joy"         : "happy",
    "trust"       : "calm",
    "surprise"    : "suspense",
    "anticipation": "suspense",
}

def parse_nrc_lexicon(lexicon_filepath):
    lexicon = {}

    lexicon_data = open(lexicon_filepath, 'r')
    for line in lexicon_data:
        line = line.split('\n')[0].split('\t')
        if len(line) < 3:
            continue

        word = line[0]
        emotion = line[1]
        association = int(line[2])

        if word not in lexicon:
            lexicon[word] = []

        lexicon[word].append((emotion, association))

    return lexicon

def calculate_emotion_density(sentence, emotions, lexicon):
    density = {}
    for emotion in emotions:
        density[emotion] = 0

    for word in sentence.split(' '):
        if word in lexicon:
            for associated_emotion in lexicon[word]:
                emotion_name = associated_emotion[0]
                if emotion_name in emotions:
                    association = associated_emotion[1]
                    density[emotion_name] += association

    return density

def density_to_rpg_emotions(density):
    emotions = {}
    for emotion in rpg_ec.RPG_EMOTIONS:
        emotions[emotion] = 0

    total_density = 0
    for emotion in density:
        if emotion in EMOTION_MAP:
            mapped_emotion = EMOTION_MAP[emotion]
            emotions[mapped_emotion] += density[emotion]

        total_density += density[emotion]

    if total_density == 0:
        emotions["calm"] = 1

    return emotions

def classify_narrative(narrative, lexicon, context_length = 0):
    classification = {}

    for s_id in narrative:
        sentence = narrative[s_id][0]
        density = calculate_emotion_density(sentence, NRC_EMOTIONS, lexicon)

        # Consider the last context_length lines in the density calculation
        for i in range(context_length):
            i += 1
            if s_id - i in narrative:

                # Caluclate previous sentence density
                prev_sentence = narrative[s_id - i][0]
                context_density = calculate_emotion_density(prev_sentence, NRC_EMOTIONS, lexicon)

                # Multiply it by a weight dependent of its distance from the current sentence
                # context_density.update((x, y * (1/(i+1))) for x, y in context_density.items())

                # Accumulate the previous density to the current one
                density = dict(collections.Counter(density) + collections.Counter(context_density))

        rpgEmotions = density_to_rpg_emotions(density)

        # Get the emotion with higher density
        max_emotion = max(sorted(rpgEmotions.items()), key=operator.itemgetter(1))[0]
        classification[s_id] = (sentence , max_emotion)

    return classification

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(sys.argv[0] + " <lexicon_filepath> " + "<narrative_filepath>")
        quit()

    lexicon_filepath = sys.argv[1]
    narrative_filepath = sys.argv[2]

    # Lexicon is a dict indexed by words of the english dictionary.
    # Each value is a list of tuples [(nrc_emotion, association)]
    lexicon = parse_nrc_lexicon(lexicon_filepath)

    # Narrative is a dict indexed by sentence id.
    # Each value is a tuple (sentence, rpg_emotion)
    narrative = rpg_ec.parse_narrative_data(narrative_filepath)

    # Classify a narrative according to rpg_emotions:
    classification = classify_narrative(narrative, lexicon, 20)

    # Calculate confusion matrix
    confusion_matrix = rpg_ec.rpg_create_confusion_matrix(narrative, classification)

    rpg_ec.rpg_print_confusion_matrix(confusion_matrix)
    print(rpg_ec.calculate_accuracy(confusion_matrix))

    rpg_ec.rpg_print_classification(classification, "classification.txt")
