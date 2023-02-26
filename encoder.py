import math
import numpy as np
import scipy
import matplotlib.pyplot as plt
from globals import *

file = open(filename, "rb")#binary data of file to transmit

data = file.read()
chunks = []#contains the divided and padded potions of the file
sfile = np.array([])#the final sound file
test = []#IGNORE - debug var

l = len(data)
nchunks = math.ceil(l/LCHUNKS)#calculating number of chunks
end = None

for i in range(nchunks):
    tmp = data[i*LCHUNKS:(i+1)*LCHUNKS]
    tmp1 = [0]*LCHUNKS
    for i in range(len(tmp)):
        tmp1[i] = int(tmp[i])
        end = i#used for decoding
    #print(tmp1)
    chunks.append(tmp1)
    
print("Converting")
def encode(chunks):
    global sfile, nc, n, T
    ct = 0

    base = np.linspace(0.0, n*T, n, endpoint=False)#discrete base
    x = np.zeros(n)
    for data in chunks:
        print("Chunk %d done."%(ct))
        for i in range(len(data)):
            x = np.add(x, data[i]*np.sin(2 * np.pi * ifreq(base_f_m, reso_m, i) * base))#main encoding
        xmax = max(x)
        x /= xmax#normalizing
        
        scaled = np.int32(x * 2147483647)
        scaled = np.concatenate(([xmax], scaled))#xmax should be within range of int32
        sfile = np.concatenate((sfile, scaled))
        ct+=1

sfile = np.array([end])
print("Number of Chunks = %d\nPadding=%d"%(nchunks, end))

def dialtone():
    base = np.linspace(0.0, n*T, n, endpoint=False)
    x = np.zeros(len(base))
    x = 2147483647*np.sin(2 * np.pi * 1000 * base)
    return x

tone = dialtone()
encode(chunks)
sfile = np.concatenate((tone, sfile))
scipy.io.wavfile.write('test.wav', int(1/T), sfile.astype(np.int32))
