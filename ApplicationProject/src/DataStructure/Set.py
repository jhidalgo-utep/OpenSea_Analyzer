# -*- coding: utf-8 -*-


class Set(object):
    def __init__(self):
        self.list = []
    
    def add(self, item):
        if item not in self.list:
            self.list.append(item)
    
    def size(self):
        return len(self.list) 
    
    def display(self):
        for i in self.list:
            print(i, end=', ')