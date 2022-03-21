import numpy as np
from collections import defaultdict

songs = np.array([30, 20, 150, 100, 40])

database = defaultdict(int)
pair = 0

for song in songs:
    if(song%60 == 0):
        pair += database[song%60]
    else:
        pair += database[60 - song%60]
    database[song%60] += 1

print(pair)