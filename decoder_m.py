import scipy
import numpy as np
from globals import *
from matplotlib import pyplot as plt
from math import ceil
from scipy.signal import find_peaks

wavfilename = "test.wav"
a = scipy.io.wavfile.read(wavfilename, 1/T)[1]

l = a[0]
a = np.array(a[1:])
nunits = ceil(len(a)/(n+1))
coeffs = []
raw = bytearray(b'')


for i in range(nunits):
    _tmp = a[i*(n+1):(i+1)*(n+1)]
    xmax = _tmp[0]
    _tmp = _tmp[1:]
    
    tmp = (_tmp / 2147483647) * xmax
    w = scipy.signal.blackman(n)
    yf = (2.0 / n * np.abs(scipy.fft.fft(tmp)[:n//2]))
    peaks = scipy.signal.find_peaks(yf)
    ctr = 0
    for p in peaks[0]:
        if not (i == nunits-1 and ctr>l):
            if p>=50 and p%5 == 0:
                coeff = (int(round(yf[p])))
                #print(i, p, coeff)
                raw.append(coeff)
                ctr += 1

file = open("output/"+filename, "wb")
file.write(raw)
file.flush()

