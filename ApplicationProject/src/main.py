# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 17:18:02 2023

@author: joaquin
"""
from time import time
from StartUp.Main_Window import Main_Window      

if __name__ == "__main__":
    print('START\n\n')
    start_time = time()
    
    
    Main_Window.execute()
    
    
    
    print('END')
    end_time = time()
    print('time elapsed: ', int(end_time - start_time), 'secs')
    
    
    