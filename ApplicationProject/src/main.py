# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 17:18:02 2023

@author: joaquin
"""
import time

#         self.my_api = "7b712a06a86444feb98e5fd4269eb83c"
from Main_Window import Main_Window      

if __name__ == "__main__":
    print('START')
    
    start_time = time.time()
    
    Main_Window.execute()
    
    print('END')
    
    end_time = time.time()
    print('time elapsed: ', int(end_time - start_time), 'secs')
    
    
    