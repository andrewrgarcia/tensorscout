#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 18:21:21 2022

@author: andrew
"""

import numpy as np
import pathos.multiprocessing as pathosmp
# from pathosMP import ProcessingPool as Pool
    

# def slicendice(tensor,L=3):
#     '''slice-n-dice
#     partition higher-order (>= 3D) tensors into dices 
#     currently beta)
#     '''
#     return tensor.reshape((*6*[L]))


def single_core(tensor, func, core_idx=1):

    # print('computing on core #{}'.format(core_idx))
    
    result = func(tensor)

    return result


def multi_core(tensor, func, cores = 2):
    '''split design into parts for each computing core to handle multi-processing tasks'''
    parts = np.array_split(tensor, cores)
       
    var = pathosmp.ProcessingPool().map\
    (single_core, parts, [func]*cores, list(np.arange(cores)+1))
                    
    # results = [ [ *var[i] ] for i in range(cores)]
    results = [ var[i] for i in range(cores)]

    return results

