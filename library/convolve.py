import numpy as np
from numpy.fft import rfft,irfft

def convolve(a1,a2):
    n = 2**(len(a1)+len(a2)+1).bit_length()
    b1,b2=np.zeros(n),np.zeros(n)
    b1[:len(a1)], b2[:len(a2)]= a1,a2
    return (irfft(rfft(b1)*rfft(b2))+0.5).astype(int)
