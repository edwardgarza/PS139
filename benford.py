import numpy as np
import matplotlib.pyplot as plt

def simBenrand(iterrations):
    out = np.random.rand(10000)    
    for i in range(iterrations):
        out *= np.random.rand(10000) * 10
    
    digits = [int(str(x)[0]) for x in out]
    firstdig = np.array([digits.count(x) for x in range(1, 10)])
    plt.plot(range(1, 10), firstdig / float(sum(firstdig)))
    plt.plot(range(1, 10), np.array([np.log10(1 + 1 / float(x)) for x in range(1, 10)]) * len(digits) / (10000.))
    #plt.plot(firstdig - np.array([np.log10(1 + 1 / float(x)) for x in range(1, 10)]) * len(digits))
    plt.show()
    title = 'Multiplication of ' + str(iterrations) + ' random numbers vs log'
    plt.title(title)
    plt.xlabel('leading digit')
    plt.ylabel('normalized frequency')
    
def simBenexp():
    out = np.random.rand(10000)
    firstdig = [int(str(x)[0]) for x in 10 **  out]
    plt.plot([firstdig.count(x) for x in range(1, 10)])
    plt.plot(np.array([np.log10(1 + 1 / float(x)) for x in range(1, 10)]) * len(firstdig))    
    plt.show()
