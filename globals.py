#encoder data

base_f = 50
reso = 5
def ifreq(base_f, reso, i):#gives ith frequence
    return base_f + reso * i

T=1/8000
nc = int(((1/T)/2 - base_f)//reso)#number of coefficients to be encoded in one unit of sound
n=2*ifreq(base_f, reso, nc)#number of data points in one unit of sound [2 * maximum frequency]

k = n / (1/T)
base_f_m = base_f * k
reso_m = reso * k

LCHUNKS = nc

#filespecific
filename="input/test1.jpg"
vidfile="input/giphy1.gif"
