import lib as scout
import numpy as np


def tensorloopA(tensor=np.ones((2,2))):
    
    for i in range(2000):
        tensor += np.random.randint(0,9,(tensor.shape))

    return tensor 

def tensorloopB(tensor=np.ones((2,2))):

    for i in range(2000):
        tensor += np.random.randint(0,9,(tensor.shape))

    return tensor, np.sum(tensor), 'hello'


def tensorloopC(tensor=np.ones((2,2))):
    return 1,2,3,4

def tensorloopD(tensor=np.ones((2,2))):
    return 'hello'

def tensorloopE(tensor=np.ones((2,2))):
    return 1


    
def test_oneproc():

    A = np.random.randint(0,2,(100,100))
    # A = A.reshape((2,500,1000))
    res = tensorloopA(A)

    return res


def test_multiprocA():

    A = np.random.randint(0,2,(100,100))
    res = scout.multi_core(A, tensorloopA, cores = 2)
    
    return res

def test_multiprocB():

    A = np.random.randint(0,2,(100,100))
    res = scout.multi_core(A, tensorloopB, cores = 2)
    
    return res

def test_multiprocC():

    A = np.random.randint(0,2,(100,100))
    res = scout.multi_core(A, tensorloopC, cores = 2)
    
    return res

def test_multiprocD():

    A = np.random.randint(0,2,(100,100))
    res = scout.multi_core(A, tensorloopD, cores = 2)
    
    return res

def test_multiprocE():

    A = np.random.randint(0,2,(100,100))
    res = scout.multi_core(A, tensorloopE, cores = 2)
    
    return res

def test_rebuild():

    tensor = test_multiprocA()
    res1 = scout.rebuild(tensor)
    
    tensor = test_multiprocB()[0]
    res2 = scout.rebuild(tensor)
    
    return res1, res2

test_oneproc()
test_multiprocA()
test_multiprocB()
test_multiprocC()
test_multiprocD()
test_multiprocE()
test_rebuild()
