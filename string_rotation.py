# -*- coding: utf-8 -*-
"""String rotation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13Bl0LTqAMvehwwte_Xlra2C6O37Wg8nx
"""

def check_rotation(string1,string2):
  if len(string1)==0 or len(string2)==0:
    return False
  if len(string1)!=len(string2):
    return False
  xy=string1+string2
  if string2.lower() in xy.lower():
    return True
  return False

check_rotation('waterbottle','erbottlewat')
