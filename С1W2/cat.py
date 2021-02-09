import numpy as np
import re
from scipy.spatial import distance

# 1
f = open('sentences.txt')
list_words = re.split('[^a-z]', f.read().lower())
list_words = [x for x in list_words if x is not '']

f.seek(0)
list_sent = f.readlines()

for sent in range(len(list_sent)):
    list_sent[sent] = re.split('[^a-z]', list_sent[sent].lower())
    list_sent[sent] = [x for x in list_sent[sent] if x is not '']


# 4
dictionary = {}
count = 0
for word in list_words:
    if word not in dictionary.keys():
        dictionary[word] = count
        count += 1
    
#5
n = len(list_sent)
d = len(dictionary)
matrix = np.ones((n,d))

for i in range(n):
    for j in range(d):
        matrix[i][j] = list_sent[i].count(list(dictionary.keys())[j])

#6
dist_cos = []
for i in range(1, n):
    cos = distance.cosine(matrix[0], matrix[i])
    dist_cos.append((i,cos))
dist_cos.sort(key=lambda touple:touple[1])

print(dist_cos)

f = open('submission-1.txt', 'w')
f.write(str(dist_cos[0][0])+' '+str(dist_cos[1][0]).strip('\n'))
print()