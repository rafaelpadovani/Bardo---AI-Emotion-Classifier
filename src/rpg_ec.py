#-----------------------------------------------------------
# Name: rpg_ec.py
# Functions to support emotion classification of RPG game sessions.
# Author: Lucas N. Ferreira
# E-mail: lferreira@ucsc.edu
#-----------------------------------------------------------

# Classes to define emotion in tabletop RPG games
RPG_EMOTIONS = ["agitated", "calm", "happy", "suspense"]

def parse_narrative_data(narrative_filepath):
    narrative = {}

    narrative_data = open(narrative_filepath, 'r')
    for line in narrative_data:
        line = line.split('\n')[0].split(':')

        sentence_id = int(line[0])
        senetence = line[1]
        senetence_emotion = line[2]

        narrative[sentence_id] = (senetence, senetence_emotion)

    return narrative

def create_confusion_matrix(expected, predicted, n_classes):
    conf_matrix = [[0] * n_classes for i in range(n_classes)]
    for exp, pred in zip(expected, predicted):
        conf_matrix[exp][pred] += 1

    return conf_matrix

def calculate_accuracy(conf_matrix):
    t = sum(sum(l) for l in conf_matrix)
    return sum(conf_matrix[i][i] for i in range(len(conf_matrix))) / t

def rpg_create_confusion_matrix(narrative, classification):
    expected = []
    for line in narrative.values():
        expected.append(RPG_EMOTIONS.index(line[1]));

    predicted = []
    for line in classification.values():
        predicted.append(RPG_EMOTIONS.index(line[1]));

    return create_confusion_matrix(expected, predicted, len(RPG_EMOTIONS))

def rpg_print_confusion_matrix(conf_matrix):
    line = ""
    longest_emotion_length = len(max(RPG_EMOTIONS))
    for i in range(longest_emotion_length + 1):
        line += " "
    for rpg_emo in RPG_EMOTIONS:
        line += rpg_emo + " "
    print(line)

    index_i = 0
    for row in conf_matrix:
        line = RPG_EMOTIONS[index_i]
        emot_lenght_i = len(RPG_EMOTIONS[index_i])
        diff_lenght = longest_emotion_length - emot_lenght_i

        for i in range(diff_lenght + 1):
            line += " "

        index_j = 0
        for column in row:
            line += str(column)

            emot_lenght_j = len(RPG_EMOTIONS[index_j])
            diff_lenght = emot_lenght_j - len(str(column)) + 1
            for i in range(diff_lenght):
                line += " "

            index_j += 1

        print(line)
        index_i += 1

def rpg_print_classification(classification):
    for s_id in classification.keys():
        print(str(s_id) + ":" + classification[s_id][0] + ":" + classification[s_id][1])

def rpg_print_classification(classification, output_filename):
    f = open(output_filename, 'w')
    for s_id in classification.keys():
        f.write(str(s_id) + ":" + classification[s_id][0] + ":" + classification[s_id][1] + "\n")
    f.close()
