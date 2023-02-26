from scipy.fft import fft, fftfreq
import numpy as np

# Number of sample points

N = 600

# sample spacing

T = 1.0 / 400.0

x = np.linspace(0.0, N*T, N, endpoint=False)

y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)

yf = fft(y)

xf = fftfreq(N, T)[:N//2]
for i in range(len(np.abs(yf)[:N//2])):
    print (i, np.abs(yf[i]))
print(xf)
import matplotlib.pyplot as plt

plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))

plt.grid()

plt.show()
