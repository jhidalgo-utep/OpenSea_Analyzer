# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 17:18:42 2023

@author: joaquin
"""

from Controller.Main_Window_Controller import Main_Window_Controller

class Main_Window(object):
    def __init__(self):
        self.custom = True


    def execute():
        program_runnning = True
        
        while program_runnning:
            print_user_menu()
            user_input = input('\n$').strip()
            Main_Window_Controller.execute(user_input)
            
            
    
def print_user_menu():
    print('\n\n\n\n\n---------------------------\n++ USER MENU ++\n')
    print("Enter: collection stats")
    print("Enter: top sell/most sell")
    print("Enter: get collection event types/get event collection")
    print("Enter: add collection/add a collection")
    print("Enter: END/STOP")
    



