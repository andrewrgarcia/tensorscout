import numpy as np
import pathos.multiprocessing as pathosmp
import timeit


class Chronos:
    '''CHRONOS -- A minimalist StopWatch class by Andrew Garcia  
    Usage:
        Chronos().start()  # starts timer
        Chronos().end()   # stops timer and returns the elapsed time in seconds
    '''
    starttime = 0
    def __init__(self):
        pass
    
    def start(self):
        Chronos.starttime = timeit.default_timer()
        print('-- Start time --')

    def end(self):
        elapsed = timeit.default_timer() - Chronos.starttime 
        print('--  End time  -- Elapsed time {} seconds'.format(elapsed))
        return elapsed



def experiments(tensor, func, core_idx=1):
    '''handles computation in a single core'''
    # print('computing on core #{}'.format(core_idx))
    num_expmts,Y,X = tensor.shape
    
    result = np.zeros((num_expmts,Y,X))
    for i in range(num_expmts):
        # result = func(tensor)
        result[i] = func(tensor[i])

    return result


def partitions(tensor, func, core_idx=1):
    '''handles computation in a 
    formerly known as single core'''
    # print('computing on core #{}'.format(core_idx))
    
    result = func(tensor)

    return result

def multi_core(tensor, func, cores = 2, core_func = partitions):
    '''split design into parts for each computing core to 
    handle multi-processing tasks'''
    parts = np.array_split(tensor, cores)
    
    'multiprocessing'
    var = pathosmp.ProcessingPool().map\
    (core_func, parts, [func]*cores, list(np.arange(cores)+1))
                    
    # 're-collect partitioned results from split function'
    # results = [ var[i] for i in range(cores)]
    
    # 'unpack (*)results if output is larger than a single value'
    # out = var[0]
    # if type(out) not in [float,int,str]:    
    #     results = np.stack([*results],axis=1) 

    return var


def rebuild(tensor):
    '''re-assemble tensor from parts (multi_core)'''
    
    tensor = np.array([*tensor])
    
    if len(tensor.shape) == 3:
        *zy,x = tensor.shape
        rebuilt = tensor.reshape((np.multiply(*zy),x))
    elif len(tensor.shape) == 4:
        q,z,y,x = tensor.shape
        rebuilt = tensor.reshape((int(q*z),y,x))
    else:
        rebuilt = None
        print('error')
        
    return rebuilt

# def rebuild2(tensor):
    
#     '''re-assemble tensor from parts (multi_core)'''
#     tensor = np.array([*tensor])
#     q,z,y,x = tensor.shape
    
#     return tensor.reshape((int(q*z),y,x))
    