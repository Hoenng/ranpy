#!/usr/bin/env python3'
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:16:06 2020

@author: 
"""

class Person:   
      
    # init method or constructor    
    def __init__(self, name, age):   
        self.name = name
        self.age = age
      
    # Sample Method    
    def say_hi(self):   
        print('Hello, my name is', self.name, 'and I am', self.age)
      
p1 = Person('Nikhil', 24)   
p2 = Person('Abhinav', 63) 
p3 = Person('Anshul', 72) 
  
p1.say_hi()   
p2.say_hi() 
p3.say_hi()   
