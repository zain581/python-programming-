# -*- coding: utf-8 -*-
#The task you mentioned involves determining whether two strings are
#permutations of each other. A permutation is a rearrangement of the characters in a string.
def check_permutation(string1,string2):
  if len(string1)!=len(string2):
    return False
  for i in string1:
    if i not in string2:
      return False
  return True

check_permutation("silent","listew")
