import numpy as np
from random import randint
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks, blackman
from scipy.io.wavfile import write

base_f = 50#base frequency
reso = 5#minimum difefrence between two frequencies

def ifreq(i):#gives ith frequence
    return base_f + reso * i

T=1/48000
nc = int(((1/T)/2 - base_f)//reso)#number of coefficients to be encoded in one unit of sound
n=2*ifreq(nc) + 100#number of data points in one unit of sound [2 * maximum frequency]
print(nc, n)
base = np.linspace(0.0, n*T, n, endpoint=False)#base
print("base - " + str(n))
x = np.zeros(n)
data = np.array([255] + [randint(0, 255) for i in range(nc-1)])#creating a random arrayo of 8-bit integers first bit is used for calibration and delimiting
data = data/255
print(data)
for i in range(len(data)):
    x = np.add(x, data[i]*np.sin(2 * np.pi * ifreq(i) * base))
    pass

print("done")
yf = fft(x)
xf = fftfreq(n, T)[:n//2]
print("len yf = " + str(xf))

plt.plot(xf, 2.0/n * np.abs(yf[0:n//2]))
plt.show()

cleaned = 2.0/n * np.abs(yf[0:n//2])
peaks = find_peaks(yf)[0]
print("peaks")
print(peaks[:50])
peaks = [(i, 2.0/n * np.abs(yf[i])) for i in peaks]
print(peaks[:50])

scaled = np.int16(x/np.max(np.abs(x)) * 32767)
print(len(scaled))
write('test.wav', 48000, scaled)
print(scaled)
