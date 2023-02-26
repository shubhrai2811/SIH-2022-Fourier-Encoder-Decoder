import math
import numpy as np
import scipy
import matplotlib.pyplot as plt
from globals import *

file = open(filename, "rb")#file to sned

data = file.read()
chunks = []
sfile = np.array([])#for the sound array
test = []##IGNORE -- debug var --

l = len(data)
nchunks = math.ceil(l/LCHUNKS)
end = None

for i in range(nchunks):
    tmp = data[i*LCHUNKS:(i+1)*LCHUNKS]
    tmp1 = [0]*LCHUNKS
    for i in range(len(tmp)):
        tmp1[i] = int(tmp[i])
        end = i
    chunks.append(tmp1)

def encode(chunks):
    global sfile, nc, n, T

    base = np.linspace(0.0, n*T, n, endpoint=False)#base            
    x = np.zeros(n)
    data = chunks[0]
    for data in chunks:

        for i in range(len(data)):
            x = np.add(x, data[i]*np.sin(2 * np.pi * ifreq(base_f_m, reso_m, i) * base))
        print(x)
        x += np.random.normal(0, 0.1, n)
        print(x)
        input()
        xmax = max(x)
        x /= xmax

        scaled = x
        scaled = np.int32(x * 2147483647)
        scaled = np.concatenate(([xmax], scaled))#xmax should be within range of int32
        sfile = np.concatenate((sfile, scaled))

sfile = np.array([end])
encode(chunks)
scipy.io.wavfile.write('test.wav', int(1/T), sfile.astype(np.int32))
