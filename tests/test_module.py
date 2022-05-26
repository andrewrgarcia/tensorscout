from lib import module as scout
import numpy as np


    
def test_oneproc():
    
    def test_tensorloop(tensor):
    
        for i in range(2000):
            tensor += np.random.randint(0,9,(tensor.shape))
        

        # return 1,2,3,4
        # return 'hello'
        # return 1
        # return tensor, np.sum(tensor), 'hello'
        return tensor 


    A = np.random.randint(0,2,(1000,1000))
    # A = A.reshape((2,500,1000))
    res = test_tensorloop(A)

    return res


def test_multiproc():
    
    def test_tensorloop(tensor):
    
        for i in range(2000):
            tensor += np.random.randint(0,9,(tensor.shape))
        

        # return 1,2,3,4
        # return 'hello'
        # return 1
        # return tensor, np.sum(tensor), 'hello'
        return tensor 

    A = np.random.randint(0,2,(1000,1000))
    # A = A.reshape((2,500,1000))
    res = scout.multi_core(A, test_tensorloop, cores = 2)
    
    return res

# test_slice()
test_oneproc()
test_multiproc()
