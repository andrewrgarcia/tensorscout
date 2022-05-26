from lib import module as scout
import numpy as np


# def test_slice():
#     #A = np.arange(1,28).reshape((3,3,3))
#     A = np.arange(9**3).reshape((*3*[9]))
#     AS = scout.slicendice(A,3)
    
#     print(AS[(0,0,0)]) #sector 1
#     print(AS[(0,0,1)]) #sector 2
#     # ... etc

def test_multiproc():

    A = np.random.randint(0,2,(1000,1000))
    res = scout.multi_core(A, np.count_nonzero, cores = 2)
    
    return res

# test_slice()
res = test_multiproc()
print(res)