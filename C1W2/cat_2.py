import re
import numpy as np
from scipy.spatial import distance

with open('sentences.txt', 'r') as file_obj:
    sentences = file_obj.readlines()

for i in range(len(sentences)):
    sentences[i] = sentences[i].lower().strip('\n')
    sentences[i] = re.split('[^a-z]', sentences[i])
    for j in range(len(sentences[i])-1, -1, -1):
        if sentences[i][j] == '':
            del sentences[i][j]
words = dict()
index = 0
for sentence in sentences:
    for word in sentence:
        if words.get(word, -1) == -1:
            words[word] = index
            index += 1


m = 22
n = 254
matrix = np.zeros((22, 254))

for i, sentence in enumerate(sentences):
    for word in sentence:
        j = words[word]
        matrix[i][j] += 1
print(matrix)
