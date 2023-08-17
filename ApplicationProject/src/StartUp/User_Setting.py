# -*- coding: utf-8 -*-

class UserSetting(object):
    def __init__(self):
        self.name = "music nfts profile"
        self.dev_mode = True
        self.access_number = "14g146aaf03d45o24"
        self.api_key = "<INSERT YOUR OPEN SEA - API KEY HERE>"
        self.unique_number = 1424
        self.public = True
        self.custom = True
    

    def get_name(self):
        return self.name
    
    def get_access_number(self):
        return self.access_number
    
    def get_api_key(self):
        return self.api_key
    
    def get_unique_number(self):
        return self.unique_number
    
    def get_dev_mode(self):
        return self.dev_mode
    
    