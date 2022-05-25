#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 18:21:21 2022

@author: andrew
"""

import numpy as np

    
def slicendice(tensor,L=3):
    '''slice-n-dice'''
    return tensor.reshape((*6*[L]))



    
