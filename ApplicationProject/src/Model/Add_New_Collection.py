# -*- coding: utf-8 -*-

class AddNewCollection(object):
    def __init__(self):
        self.custom = True
        
    def write_json(self, user_slug):
        print(user_slug)
    
    def slug_status(self, user_slug):
        pass
        # if slug error doesnt exist return 4
        #elif slug exist and new slug return 1
        #elif slug exist and slug been added but not fully updated return 2
        #elif slug exist and slug been added and fully updated return 3
    
    def execute(user_slug):
        pass