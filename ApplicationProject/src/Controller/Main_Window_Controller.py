# -*- coding: utf-8 -*-

import sys
import time
from Model.Add_New_Collection import AddNewCollection
from Model.Top_Selling_NFTs import Top_Selling_NFTs
from Model.Collection_Stats import Collection_Stats
from Model.Get_Collection_Event_Types import Get_Collection_Event_Types

# Objects
# UserSetting = UserSetting()
# AddNewCollection = AddNewCollection()

class Main_Window_Controller(object):
    def __init__(self):
        self.custom = True
        

    def execute(user_choice):
        if user_choice == "":
            print('Error: please enter valid command\n')


        else:
            if "END" in user_choice or "STOP" in user_choice:
                print('ending program....') 
                time.sleep(1.4)
                print('Good-Bye')
                sys.exit(0)
            
            
            elif "top sell" in user_choice or "most sell" in user_choice:
                Top_Selling_NFTs.execute()
            
            
            elif "collection stats" in user_choice:
                Collection_Stats.execute()
            
            
            elif "get collection event types" in user_choice or "get event collection" in user_choice:
                Get_Collection_Event_Types.execute()
            
            
            elif "add collection" in user_choice or "add a collection" in user_choice:
                print_loading_screen()
                collection_slug = input("define collection slug $").strip()
                AddNewCollection.execute(collection_slug)


def print_loading_screen():
    time.sleep(.2)
    print('...')
    time.sleep(.5)
    print('..')
    time.sleep(1.4)
    print('.')
    time.sleep(.4)
    print('...')
    time.sleep(.9)
    print('.....')
    time.sleep(.5)
    print()
    

