# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:57:13 2019

@author: Agnieszka
"""

Verben = (["sein","to be"],["bekommen","to get"],["geben","to give"], ["leben","to live"],["machen","to make"],["gehen","to walk"],["benutzen","to use"],["essen","to eat"],["denken","to think"],["kommen","to come"],["haben","to have"], ["tun","to do"],["sagen","to say"],["gehen","to go"],["wissen","to know"],["sehen","to see"],["wollen","to want"],["finden","to find"],["erzählen","to tell"],["fragen","to ask"],["versuchen","to try"],["anrufen","to call"])

for Verb in Verben:
    i=0
    eingabe = input('Das Verb '+Verb[i]+' heißt auf Englisch: ')
    if eingabe == Verb[i+1]:
        print('Das ist richtig')
    else:
        print('Das ist leider falsch')

'''        


import random

Verben = (["sein","to be"],["bekommen","to get"],["geben","to give"], ["leben","to live"],["machen","to make"],["gehen","to walk"],["benutzen","to use"],["essen","to eat"],["denken","to think"],["kommen","to come"],["haben","to have"], ["tun","to do"],["sagen","to say"],["gehen","to go"],["wissen","to know"],["sehen","to see"],["wollen","to want"],["finden","to find"],["erzählen","to tell"],["fragen","to ask"],["versuchen","to try"],["anrufen","to call"])
i=0
sum1 = 0
sum2 = 0

#random.shuffle(Verben)

for Verb in Verben:
    eingabe = input('Das Verb '+Verb[i]+' heißt auf Englisch: ')
    if eingabe == Verb[i+1]:
        print('Das ist richtig')
        sum1 = sum1+1
    else:
        print('Das ist leider falsch')
        sum2 = sum2+1
        
print('Anzahl der richtigen Antworten: ', sum1)
print('Anzahl der falschen Antworten: ', sum2)

'''