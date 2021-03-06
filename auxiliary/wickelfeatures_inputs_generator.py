'''
This function creates a txt file containing all 460 possible input units as generated
by the dictionary of nodes algorithm
'''

import pickle

lista = [['int', 'int', 'int'],
 ['int', 'cont', 'int'],
 ['int', 'vowel', 'int'],
 ['int', 'd1', 'int'],
 ['int', 'd2', 'int'],
 ['int', 'front', 'int'],
 ['int', 'middle', 'int'],
 ['int', 'back', 'int'],
 ['int', 'b1', 'int'],
 ['int', 'b2', 'int'],
 ['int', 'int', 'cont'],
 ['int', 'cont', 'cont'],
 ['int', 'vowel', 'cont'],
 ['int', 'd1', 'cont'],
 ['int', 'd2', 'cont'],
 ['int', 'front', 'cont'],
 ['int', 'middle', 'cont'],
 ['int', 'back', 'cont'],
 ['int', 'b1', 'cont'],
 ['int', 'b2', 'cont'],
 ['int', 'int', 'vowel'],
 ['int', 'cont', 'vowel'],
 ['int', 'vowel', 'vowel'],
 ['int', 'd1', 'vowel'],
 ['int', 'd2', 'vowel'],
 ['int', 'front', 'vowel'],
 ['int', 'middle', 'vowel'],
 ['int', 'back', 'vowel'],
 ['int', 'b1', 'vowel'],
 ['int', 'b2', 'vowel'],
 ['cont', 'int', 'int'],
 ['cont', 'cont', 'int'],
 ['cont', 'vowel', 'int'],
 ['cont', 'd1', 'int'],
 ['cont', 'd2', 'int'],
 ['cont', 'front', 'int'],
 ['cont', 'middle', 'int'],
 ['cont', 'back', 'int'],
 ['cont', 'b1', 'int'],
 ['cont', 'b2', 'int'],
 ['cont', 'int', 'cont'],
 ['cont', 'cont', 'cont'],
 ['cont', 'vowel', 'cont'],
 ['cont', 'd1', 'cont'],
 ['cont', 'd2', 'cont'],
 ['cont', 'front', 'cont'],
 ['cont', 'middle', 'cont'],
 ['cont', 'back', 'cont'],
 ['cont', 'b1', 'cont'],
 ['cont', 'b2', 'cont'],
 ['cont', 'int', 'vowel'],
 ['cont', 'cont', 'vowel'],
 ['cont', 'vowel', 'vowel'],
 ['cont', 'd1', 'vowel'],
 ['cont', 'd2', 'vowel'],
 ['cont', 'front', 'vowel'],
 ['cont', 'middle', 'vowel'],
 ['cont', 'back', 'vowel'],
 ['cont', 'b1', 'vowel'],
 ['cont', 'b2', 'vowel'],
 ['vowel', 'int', 'int'],
 ['vowel', 'cont', 'int'],
 ['vowel', 'vowel', 'int'],
 ['vowel', 'd1', 'int'],
 ['vowel', 'd2', 'int'],
 ['vowel', 'front', 'int'],
 ['vowel', 'middle', 'int'],
 ['vowel', 'back', 'int'],
 ['vowel', 'b1', 'int'],
 ['vowel', 'b2', 'int'],
 ['vowel', 'int', 'cont'],
 ['vowel', 'cont', 'cont'],
 ['vowel', 'vowel', 'cont'],
 ['vowel', 'd1', 'cont'],
 ['vowel', 'd2', 'cont'],
 ['vowel', 'front', 'cont'],
 ['vowel', 'middle', 'cont'],
 ['vowel', 'back', 'cont'],
 ['vowel', 'b1', 'cont'],
 ['vowel', 'b2', 'cont'],
 ['vowel', 'int', 'vowel'],
 ['vowel', 'cont', 'vowel'],
 ['vowel', 'vowel', 'vowel'],
 ['vowel', 'd1', 'vowel'],
 ['vowel', 'd2', 'vowel'],
 ['vowel', 'front', 'vowel'],
 ['vowel', 'middle', 'vowel'],
 ['vowel', 'back', 'vowel'],
 ['vowel', 'b1', 'vowel'],
 ['vowel', 'b2', 'vowel'],
 ['d1', 'int', 'd1'],
 ['d1', 'cont', 'd1'],
 ['d1', 'vowel', 'd1'],
 ['d1', 'd1', 'd1'],
 ['d1', 'd2', 'd1'],
 ['d1', 'front', 'd1'],
 ['d1', 'middle', 'd1'],
 ['d1', 'back', 'd1'],
 ['d1', 'b1', 'd1'],
 ['d1', 'b2', 'd1'],
 ['d1', 'int', 'd2'],
 ['d1', 'cont', 'd2'],
 ['d1', 'vowel', 'd2'],
 ['d1', 'd1', 'd2'],
 ['d1', 'd2', 'd2'],
 ['d1', 'front', 'd2'],
 ['d1', 'middle', 'd2'],
 ['d1', 'back', 'd2'],
 ['d1', 'b1', 'd2'],
 ['d1', 'b2', 'd2'],
 ['d2', 'int', 'd1'],
 ['d2', 'cont', 'd1'],
 ['d2', 'vowel', 'd1'],
 ['d2', 'd1', 'd1'],
 ['d2', 'd2', 'd1'],
 ['d2', 'front', 'd1'],
 ['d2', 'middle', 'd1'],
 ['d2', 'back', 'd1'],
 ['d2', 'b1', 'd1'],
 ['d2', 'b2', 'd1'],
 ['d2', 'int', 'd2'],
 ['d2', 'cont', 'd2'],
 ['d2', 'vowel', 'd2'],
 ['d2', 'd1', 'd2'],
 ['d2', 'd2', 'd2'],
 ['d2', 'front', 'd2'],
 ['d2', 'middle', 'd2'],
 ['d2', 'back', 'd2'],
 ['d2', 'b1', 'd2'],
 ['d2', 'b2', 'd2'],
 ['front', 'int', 'front'],
 ['front', 'cont', 'front'],
 ['front', 'vowel', 'front'],
 ['front', 'd1', 'front'],
 ['front', 'd2', 'front'],
 ['front', 'front', 'front'],
 ['front', 'middle', 'front'],
 ['front', 'back', 'front'],
 ['front', 'b1', 'front'],
 ['front', 'b2', 'front'],
 ['front', 'int', 'middle'],
 ['front', 'cont', 'middle'],
 ['front', 'vowel', 'middle'],
 ['front', 'd1', 'middle'],
 ['front', 'd2', 'middle'],
 ['front', 'front', 'middle'],
 ['front', 'middle', 'middle'],
 ['front', 'back', 'middle'],
 ['front', 'b1', 'middle'],
 ['front', 'b2', 'middle'],
 ['front', 'int', 'back'],
 ['front', 'cont', 'back'],
 ['front', 'vowel', 'back'],
 ['front', 'd1', 'back'],
 ['front', 'd2', 'back'],
 ['front', 'front', 'back'],
 ['front', 'middle', 'back'],
 ['front', 'back', 'back'],
 ['front', 'b1', 'back'],
 ['front', 'b2', 'back'],
 ['middle', 'int', 'front'],
 ['middle', 'cont', 'front'],
 ['middle', 'vowel', 'front'],
 ['middle', 'd1', 'front'],
 ['middle', 'd2', 'front'],
 ['middle', 'front', 'front'],
 ['middle', 'middle', 'front'],
 ['middle', 'back', 'front'],
 ['middle', 'b1', 'front'],
 ['middle', 'b2', 'front'],
 ['middle', 'int', 'middle'],
 ['middle', 'cont', 'middle'],
 ['middle', 'vowel', 'middle'],
 ['middle', 'd1', 'middle'],
 ['middle', 'd2', 'middle'],
 ['middle', 'front', 'middle'],
 ['middle', 'middle', 'middle'],
 ['middle', 'back', 'middle'],
 ['middle', 'b1', 'middle'],
 ['middle', 'b2', 'middle'],
 ['middle', 'int', 'back'],
 ['middle', 'cont', 'back'],
 ['middle', 'vowel', 'back'],
 ['middle', 'd1', 'back'],
 ['middle', 'd2', 'back'],
 ['middle', 'front', 'back'],
 ['middle', 'middle', 'back'],
 ['middle', 'back', 'back'],
 ['middle', 'b1', 'back'],
 ['middle', 'b2', 'back'],
 ['back', 'int', 'front'],
 ['back', 'cont', 'front'],
 ['back', 'vowel', 'front'],
 ['back', 'd1', 'front'],
 ['back', 'd2', 'front'],
 ['back', 'front', 'front'],
 ['back', 'middle', 'front'],
 ['back', 'back', 'front'],
 ['back', 'b1', 'front'],
 ['back', 'b2', 'front'],
 ['back', 'int', 'middle'],
 ['back', 'cont', 'middle'],
 ['back', 'vowel', 'middle'],
 ['back', 'd1', 'middle'],
 ['back', 'd2', 'middle'],
 ['back', 'front', 'middle'],
 ['back', 'middle', 'middle'],
 ['back', 'back', 'middle'],
 ['back', 'b1', 'middle'],
 ['back', 'b2', 'middle'],
 ['back', 'int', 'back'],
 ['back', 'cont', 'back'],
 ['back', 'vowel', 'back'],
 ['back', 'd1', 'back'],
 ['back', 'd2', 'back'],
 ['back', 'front', 'back'],
 ['back', 'middle', 'back'],
 ['back', 'back', 'back'],
 ['back', 'b1', 'back'],
 ['back', 'b2', 'back'],
 ['b1', 'int', 'b1'],
 ['b1', 'cont', 'b1'],
 ['b1', 'vowel', 'b1'],
 ['b1', 'd1', 'b1'],
 ['b1', 'd2', 'b1'],
 ['b1', 'front', 'b1'],
 ['b1', 'middle', 'b1'],
 ['b1', 'back', 'b1'],
 ['b1', 'b1', 'b1'],
 ['b1', 'b2', 'b1'],
 ['b1', 'int', 'b2'],
 ['b1', 'cont', 'b2'],
 ['b1', 'vowel', 'b2'],
 ['b1', 'd1', 'b2'],
 ['b1', 'd2', 'b2'],
 ['b1', 'front', 'b2'],
 ['b1', 'middle', 'b2'],
 ['b1', 'back', 'b2'],
 ['b1', 'b1', 'b2'],
 ['b1', 'b2', 'b2'],
 ['b2', 'int', 'b1'],
 ['b2', 'cont', 'b1'],
 ['b2', 'vowel', 'b1'],
 ['b2', 'd1', 'b1'],
 ['b2', 'd2', 'b1'],
 ['b2', 'front', 'b1'],
 ['b2', 'middle', 'b1'],
 ['b2', 'back', 'b1'],
 ['b2', 'b1', 'b1'],
 ['b2', 'b2', 'b1'],
 ['b2', 'int', 'b2'],
 ['b2', 'cont', 'b2'],
 ['b2', 'vowel', 'b2'],
 ['b2', 'd1', 'b2'],
 ['b2', 'd2', 'b2'],
 ['b2', 'front', 'b2'],
 ['b2', 'middle', 'b2'],
 ['b2', 'back', 'b2'],
 ['b2', 'b1', 'b2'],
 ['b2', 'b2', 'b2'],
 ['int', 'int', '#'],
 ['int', 'cont', '#'],
 ['int', 'vowel', '#'],
 ['int', 'd1', '#'],
 ['int', 'd2', '#'],
 ['int', 'front', '#'],
 ['int', 'middle', '#'],
 ['int', 'back', '#'],
 ['int', 'b1', '#'],
 ['int', 'b2', '#'],
 ['cont', 'int', '#'],
 ['cont', 'cont', '#'],
 ['cont', 'vowel', '#'],
 ['cont', 'd1', '#'],
 ['cont', 'd2', '#'],
 ['cont', 'front', '#'],
 ['cont', 'middle', '#'],
 ['cont', 'back', '#'],
 ['cont', 'b1', '#'],
 ['cont', 'b2', '#'],
 ['vowel', 'int', '#'],
 ['vowel', 'cont', '#'],
 ['vowel', 'vowel', '#'],
 ['vowel', 'd1', '#'],
 ['vowel', 'd2', '#'],
 ['vowel', 'front', '#'],
 ['vowel', 'middle', '#'],
 ['vowel', 'back', '#'],
 ['vowel', 'b1', '#'],
 ['vowel', 'b2', '#'],
 ['d1', 'int', '#'],
 ['d1', 'cont', '#'],
 ['d1', 'vowel', '#'],
 ['d1', 'd1', '#'],
 ['d1', 'd2', '#'],
 ['d1', 'front', '#'],
 ['d1', 'middle', '#'],
 ['d1', 'back', '#'],
 ['d1', 'b1', '#'],
 ['d1', 'b2', '#'],
 ['d2', 'int', '#'],
 ['d2', 'cont', '#'],
 ['d2', 'vowel', '#'],
 ['d2', 'd1', '#'],
 ['d2', 'd2', '#'],
 ['d2', 'front', '#'],
 ['d2', 'middle', '#'],
 ['d2', 'back', '#'],
 ['d2', 'b1', '#'],
 ['d2', 'b2', '#'],
 ['front', 'int', '#'],
 ['front', 'cont', '#'],
 ['front', 'vowel', '#'],
 ['front', 'd1', '#'],
 ['front', 'd2', '#'],
 ['front', 'front', '#'],
 ['front', 'middle', '#'],
 ['front', 'back', '#'],
 ['front', 'b1', '#'],
 ['front', 'b2', '#'],
 ['middle', 'int', '#'],
 ['middle', 'cont', '#'],
 ['middle', 'vowel', '#'],
 ['middle', 'd1', '#'],
 ['middle', 'd2', '#'],
 ['middle', 'front', '#'],
 ['middle', 'middle', '#'],
 ['middle', 'back', '#'],
 ['middle', 'b1', '#'],
 ['middle', 'b2', '#'],
 ['back', 'int', '#'],
 ['back', 'cont', '#'],
 ['back', 'vowel', '#'],
 ['back', 'd1', '#'],
 ['back', 'd2', '#'],
 ['back', 'front', '#'],
 ['back', 'middle', '#'],
 ['back', 'back', '#'],
 ['back', 'b1', '#'],
 ['back', 'b2', '#'],
 ['b1', 'int', '#'],
 ['b1', 'cont', '#'],
 ['b1', 'vowel', '#'],
 ['b1', 'd1', '#'],
 ['b1', 'd2', '#'],
 ['b1', 'front', '#'],
 ['b1', 'middle', '#'],
 ['b1', 'back', '#'],
 ['b1', 'b1', '#'],
 ['b1', 'b2', '#'],
 ['b2', 'int', '#'],
 ['b2', 'cont', '#'],
 ['b2', 'vowel', '#'],
 ['b2', 'd1', '#'],
 ['b2', 'd2', '#'],
 ['b2', 'front', '#'],
 ['b2', 'middle', '#'],
 ['b2', 'back', '#'],
 ['b2', 'b1', '#'],
 ['b2', 'b2', '#'],
 ['#', 'int', 'int'],
 ['#', 'int', 'cont'],
 ['#', 'int', 'vowel'],
 ['#', 'int', 'd1'],
 ['#', 'int', 'd2'],
 ['#', 'int', 'front'],
 ['#', 'int', 'middle'],
 ['#', 'int', 'back'],
 ['#', 'int', 'b1'],
 ['#', 'int', 'b2'],
 ['#', 'cont', 'int'],
 ['#', 'cont', 'cont'],
 ['#', 'cont', 'vowel'],
 ['#', 'cont', 'd1'],
 ['#', 'cont', 'd2'],
 ['#', 'cont', 'front'],
 ['#', 'cont', 'middle'],
 ['#', 'cont', 'back'],
 ['#', 'cont', 'b1'],
 ['#', 'cont', 'b2'],
 ['#', 'vowel', 'int'],
 ['#', 'vowel', 'cont'],
 ['#', 'vowel', 'vowel'],
 ['#', 'vowel', 'd1'],
 ['#', 'vowel', 'd2'],
 ['#', 'vowel', 'front'],
 ['#', 'vowel', 'middle'],
 ['#', 'vowel', 'back'],
 ['#', 'vowel', 'b1'],
 ['#', 'vowel', 'b2'],
 ['#', 'd1', 'int'],
 ['#', 'd1', 'cont'],
 ['#', 'd1', 'vowel'],
 ['#', 'd1', 'd1'],
 ['#', 'd1', 'd2'],
 ['#', 'd1', 'front'],
 ['#', 'd1', 'middle'],
 ['#', 'd1', 'back'],
 ['#', 'd1', 'b1'],
 ['#', 'd1', 'b2'],
 ['#', 'd2', 'int'],
 ['#', 'd2', 'cont'],
 ['#', 'd2', 'vowel'],
 ['#', 'd2', 'd1'],
 ['#', 'd2', 'd2'],
 ['#', 'd2', 'front'],
 ['#', 'd2', 'middle'],
 ['#', 'd2', 'back'],
 ['#', 'd2', 'b1'],
 ['#', 'd2', 'b2'],
 ['#', 'front', 'int'],
 ['#', 'front', 'cont'],
 ['#', 'front', 'vowel'],
 ['#', 'front', 'd1'],
 ['#', 'front', 'd2'],
 ['#', 'front', 'front'],
 ['#', 'front', 'middle'],
 ['#', 'front', 'back'],
 ['#', 'front', 'b1'],
 ['#', 'front', 'b2'],
 ['#', 'middle', 'int'],
 ['#', 'middle', 'cont'],
 ['#', 'middle', 'vowel'],
 ['#', 'middle', 'd1'],
 ['#', 'middle', 'd2'],
 ['#', 'middle', 'front'],
 ['#', 'middle', 'middle'],
 ['#', 'middle', 'back'],
 ['#', 'middle', 'b1'],
 ['#', 'middle', 'b2'],
 ['#', 'back', 'int'],
 ['#', 'back', 'cont'],
 ['#', 'back', 'vowel'],
 ['#', 'back', 'd1'],
 ['#', 'back', 'd2'],
 ['#', 'back', 'front'],
 ['#', 'back', 'middle'],
 ['#', 'back', 'back'],
 ['#', 'back', 'b1'],
 ['#', 'back', 'b2'],
 ['#', 'b1', 'int'],
 ['#', 'b1', 'cont'],
 ['#', 'b1', 'vowel'],
 ['#', 'b1', 'd1'],
 ['#', 'b1', 'd2'],
 ['#', 'b1', 'front'],
 ['#', 'b1', 'middle'],
 ['#', 'b1', 'back'],
 ['#', 'b1', 'b1'],
 ['#', 'b1', 'b2'],
 ['#', 'b2', 'int'],
 ['#', 'b2', 'cont'],
 ['#', 'b2', 'vowel'],
 ['#', 'b2', 'd1'],
 ['#', 'b2', 'd2'],
 ['#', 'b2', 'front'],
 ['#', 'b2', 'middle'],
 ['#', 'b2', 'back'],
 ['#', 'b2', 'b1'],
 ['#', 'b2', 'b2']]

with open("nodes.txt", "wb") as file:
     pickle.dump(lista, file)
