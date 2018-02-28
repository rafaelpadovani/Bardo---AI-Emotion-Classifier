#-----------------------------------------------------------
# Name: rpg_ec.py
# Create Datasets from Anotated RPG Sessions Transcripts
# Author: Lucas N. Ferreira
# E-mail: lferreira@ucsc.edu
#-----------------------------------------------------------

import sys
import re

def remove_html_tags(sentence):
    return re.sub("<.*?>", '', sentence)

def rpg_parse_transcripts(transcripts):
    files = {}
    dataset = {}

    line_counter = 0

    # Open the data files and get the classes
    for f in transcripts:
        data = open(f, 'r')
        emotion = f.split("/")[-1].split(".")[0]
        files[emotion] = data

    for f in files.keys():
        for line in files[f]:
            line = line.split('\n')[0]
            if line == '':
                continue

            if line_counter == 0:
                sentence_id = int(line)
                line_counter += 1

            elif line_counter == 1:
                line_counter += 1

            elif line_counter == 2:
                dataset[sentence_id] = (line, f)
                line_counter = 0

    return dataset

def rpg_print_dataset(dataset, output_filename):
    dataset_file = open(output_filename, 'w')

    for t in dataset.keys():
        sentence_id = str(t)
        sentence = remove_html_tags(str(dataset[t][0]))
        sentence_emotion = str(dataset[t][1])
        dataset_file.write(sentence_id + ":" + sentence + ":" + sentence_emotion.lower() + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(sys.argv[0] + " <narrative_filepath1> " + "<narrative_filepath2> " + "...")
        quit()

    transcripts = sys.argv
    transcripts.pop(0)

    dataset = rpg_parse_transcripts(transcripts)
    rpg_print_dataset(dataset, "dataset.txt")
