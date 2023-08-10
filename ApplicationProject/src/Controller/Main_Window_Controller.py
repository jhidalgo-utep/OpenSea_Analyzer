# -*- coding: utf-8 -*-

import time
import requests
import json
import os
from datetime import datetime
from DataStructure.Set import Set
from Model.Add_New_Collection import AddNewCollection
from StartUp.User_Setting import UserSetting

# Objects
UserSetting = UserSetting()
# AddNewCollection = AddNewCollection()

class Main_Window_Controller(object):
    def __init__(self):
        self.custom = True
        
    def execute(user_choice):
        print_loading_screen()
        error_list = 0
        
        if user_choice == "":
            print('Error: please enter valid command\n')
        else:
            user_choice = str(user_choice)
        
            if "top sell" in user_choice or "most sell" in user_choice:
                print('getinng top selling.....')
                # updateDatabase()
                # display top selling nft's
                
            elif "END" in user_choice or "STOP" in user_choice:
                print('ending program...')
                
            elif "collection stats" in user_choice:
                print('getting colelction stats...')
                
                
            elif "get collection event types" in user_choice or "get event collection" in user_choice:
                print('getiting collection event types...')
                # user_coll = input('enter the collection-slug name you like to add: ')
                # user_event_type = input('enter the event type: ')

            
            
            elif "add collection" in user_choice or "add a collection" in user_choice:
                collection_slug = input("define collection slug $").strip()
                AddNewCollection.execute(collection_slug)
                
                # slug_status = AddNewCollection.check_slug(collection_slug)
                # AddNewCollection.write_json(collection_slug)
                
                
                already_in_database = False
                
                # check path for file names
                dir_list = os.listdir("data/backend/collection")
                for i in dir_list:
                    if collection_slug in i:
                        already_in_database = True
                        print('already in db...')
                        
                        # READ JSON slugs file
                        # file1 = open(f"data/backend/slug/slug_name.json", 'r')
                        
                        with open(f"data/backend/slug/slug_name.txt", "r") as data_file:    
                            old_data = data_file.read()
                            
                        old_data = old_data.split(',')
                        list1 = []
                        
                        for i in old_data:
                            print(i.strip() )
                            list1.append(i.strip() )
                        
                        if collection_slug not in list1:
                            list1.append(collection_slug)
                        data_file.close()
                        
                        with open(f"data/backend/slug/slug_name.txt", 'w') as outfile:
                            for i in range(len(list1)):
                                outfile.write(list1[i])
                                if i != len(list1)-1:
                                    outfile.write(', ')
                        outfile.close()
                        
                        
                        found = False
                        

                        
                        if found:
                            print('found')
                            pass
                        else:
                            print('writing slug name')
                            # #write json files
                            # file2 = open(f"data/backend/slug/slug_name.json", 'a')
                            
                            
                            # file2.write('{collection_slug}')
                            # file2.close()
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
                    

def print_loading_screen():
    time.sleep(.2)
    print('...')
    time.sleep(.5)
    print('..')
    time.sleep(1.4)
    print('.')
    time.sleep(.3)
    print('...')
    time.sleep(.9)
    print('.....')
    time.sleep(.3)
    print()
    

