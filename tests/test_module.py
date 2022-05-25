from lib import module as tes
import numpy as np


def test_slice():
    #A = np.arange(1,28).reshape((3,3,3))
    A = np.arange(9**3).reshape((*3*[9]))
    AS = tes.slicendice(A,3)
    
    print(AS[(0,0,0)]) #sector 1
    print(AS[(0,0,1)]) #sector 2
    # ... etc
    
test_slice()



