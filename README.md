# Bardo - AI Emotion Classifier
Emotion-Based Classifier for TableTop Games

Bardo is a real-time intelligent system to automatically select the background music for tabletop role-playing games. Bardo uses Naive Bayes classifier variants to select emotions based on text. The system was trained with a large dataset containing more than 4 hours of what is said by the players during a Dungeons and Dragons (D&D) campaign available on YouTube.

Inside the /src folder you can find the source code. This is the final approach called ENS, where 4 variants of Naive Bayes classifier are used to label the sentences of the entire campaign.

To run an example you go into /src folder and run this command on terminal:

`python3 main.py 1`

Where `1` is the episode you want to test. It is important to say that episode 1 is not used in training process in this case. The result will be store inside `testesNSALL` folder. There you can check the labeled text and accuracy.

The classifiers are NS, NHS, NM and NHM. They are variants of Naive Bayes classifier and you can find them separately inside the `classifiers` folder.

The official dataset is located inside the `datasets` and this the basis of ou supervised learning.

This work part of my master's degree and it was published ON AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment(AIIDE17). For more information see the paper: https://aaai.org/ocs/index.php/AIIDE/AIIDE17/paper/view/15909
