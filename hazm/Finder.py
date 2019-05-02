#!/usr/bin/env python3
# coding: utf-8
from __future__ import unicode_literals

import sys, codecs
from os import path


#Open the file
data_path = path.join(path.dirname(__file__), 'data')
default_words = path.join(data_path, 'words.dat')

words_file=default_words
fobj = open(words_file)
text = fobj.read().strip().split()

#Conditions
def finder(word):
    while True:
        s = word #input("Enter a string: ") #Takes input of a string from user
        if s == "": #if no value is entered for the string
            continue
        if s in text: #string in present in the text file
            return True
            break
        else: #string is absent in the text file
            return False#print("No such string found,try again")
            continue
fobj.close()
