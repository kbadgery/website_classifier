# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:33:25 2021

@author: Kip
"""

from bs4 import BeautifulSoup

with open('temp_data\\preprod-coldstart-scraping\\7mesh.com', 'r') as file:
    data = file.read()
      
  
soup = BeautifulSoup(data, 'html.parser')     
   
def     