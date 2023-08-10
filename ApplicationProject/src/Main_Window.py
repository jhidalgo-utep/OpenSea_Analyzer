# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 17:18:42 2023

@author: joaquin
"""
# from Execute_Command import Execute_Command
# from Update_Database import Update_Database
import requests
import json
import os
import time
from datetime import datetime
from Set import Set
from User_Setting import UserSetting
from Add_New_Collection import AddNewCollection

UserSetting = UserSetting()
AddNewCollection = AddNewCollection()

class Main_Window(object):
    def __init__(self):
        self.custom = True

    def execute():
        
        # print('executing Main Window...\n\n')
        program_runnning = True
        error_list = 0
        
        while program_runnning:
            user_choice = input('enter command here $')
            user_choice = user_choice.strip()
            
            if user_choice.isdigit():
                user_choice = int(user_choice)
                
                if user_choice == 0:
                    program_runnning = False # END

                elif user_choice == 1:
                    # show collection stats
                    pass
                
            else:
                if user_choice == "":
                    print('Error: please enter valid command\n')
                else:
                    user_choice = str(user_choice)
                
                    if "top sell" in user_choice or "most sell" in user_choice:
                        print('getinng top selling.....')
                        # updateDatabase()
                        # display top selling nft's
                        
                    elif "get collection event types" in user_choice or "get event collection" in user_choice:
                        print('getiting collection event types...')
                        # user_coll = input('enter the collection-slug name you like to add: ')
                        # user_event_type = input('enter the event type: ')

                    
                    
                    elif "add collection" in user_choice or "add a collection" in user_choice:
                        collection_slug = input("define collection slug $")
                        slug_status = AddNewCollection.check_slug(collection_slug)
                        AddNewCollection.write_json(collection_slug)
                        
                        
                        already_in_database = False
                        
                        # check path for file names
                        dir_list = os.listdir("data/backend/collection")
                        for i in dir_list:
                            if collection_slug in i:
                                already_in_database = True
                                break
                            
                        if already_in_database:
                            print('alread in database...')
                            #if most current and up to date
                            #   #print done
                            #else
                            #   #update database only whats missing
                            pass
                    
                    
                        
                        #check if collection slug exists: need to implement!
                        #else
                        #write to database
                        
                        
                        
                        endpoint = "https://api.opensea.io/v2/collection"
                        url = f"{endpoint}/{collection_slug}/nfts"
                        
                        
                        
                        
                        
                        
                        last_added_id = None
                        
                        if not already_in_database:
                            cursor = ''
                            calls = 0
                            counter = 0
                            s = Set()        
                            
                            result = dict()
                            result['nfts'] = []
                            result['custom'] = True
                            result['last_updated'] = datetime.now().strftime('%Y-%m-%d-T%H:%M:%S.%f')
                            
                            
                            while True:
                                headers = {
                                    "accept": "application/json",
                                    "X-API-KEY": UserSetting.get_api_key()
                                } 
                                
                                query = {"next": cursor}
                                
                                response = requests.get(url, headers=headers, params=query)
                                calls += 1
                                time.sleep(1)
                                
                                res1 = response.json()
                                
                                res2 = res1['nfts']
                                
                                try:
                                  cursor = res1['next']
                                except:
                                  print("no next page...")
                                  cursor = None
                            
                                
                                for i in res2:
                                    print('callz: ', calls)
                                    print("counter: ", counter)
                                    
                                    result['nfts'].append(i)
                                    if counter == 0:
                                        last_added_id = i['identifier']
                                    
                                    counter +=1
                                    print("set len: ", s.size() )
                                    print('\n\n\n\n\n')
                                    
                                    s.add(i['identifier'] )
                                    
                                if cursor == None:
                                    print('breaking...')
                                    break
                                else:
                                    print('----- next page -----')
                                 
                            result['length'] = s.size()
                            result['last_added_id'] = last_added_id
                            
                            # #write json files
                            file1 = open(f"data/backend/collection/collection_{collection_slug}.json", 'a')
                                    
                            temp1 = json.dumps(result, indent=2)
                            file1.write(temp1)
                            
                            file1.close()
    
                            
                            print('calls:', calls)
                            print('counter: ', counter)
                            print('len set:', s.size() )
                            print('error list: ', error_list)
                        else:
                            print("already in database")
                            f = open(f"data/backend/collection/collection_{collection_slug}.json")
                            z = json.load(f) 
                            
                            f.close()
                            print('done')



                        
                        
                        
                        


    



