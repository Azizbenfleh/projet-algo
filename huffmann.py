# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:19:10 2023

@author: hp
"""

def determine_alphabet_and_frequencies(text):
    frequency = {}
    for i in range(97,123) :
        frequency[chr(i)]=0
    for char in text:
          if char in frequency.keys():
            frequency[char] += 1
    frequency = {k: v for k, v in frequency.items() if v > 0}
    frequency_list = [(char, count) for char, count in frequency.items()]
    frequency_list.sort(key=lambda x: (x[1], ord(x[0])))
    with open("text_freq.txt", "w") as freq_file:
        freq_file.write(str(len(frequency_list)) + "\n")
        for char, count in frequency_list:
            freq_file.write(char + " " + str(count) + "\n")

    return frequency_list

class HuffmanNode:
 def __init__(self, freq, char=None):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None
        
 def __lt__(self,other):
     if self.freq<other.freq:
         return(True)
     elif self.freq>other.freq:
         return(False)


 def __gt__(self,other):
     if self.freq<other.freq:
         return(False)
     elif self.freq>other.freq:
         return(True)
    
 def __eq__(self,other):
     if self.freq==other.freq:
         if ord(self.char)<ord(other.char):
             return(True)
         else:
             return(False)
 def is_leaf(self):
        return self.left is None and self.right is None
 def has_left_child(self):
     return(not(self.left is None))
 def has_right_child(self):
     return(not(self.right is None))


def cree_arbre(freq_list):
    nodes = [HuffmanNode(freq, char) for (char, freq) in freq_list]
    while len(nodes) > 1:
        node1 = min(nodes)
        nodes.remove(node1)
        node2 = min(nodes, key=lambda node: node.freq)
        nodes.remove(node2)
        new_node = HuffmanNode(node1.freq + node2.freq)
        new_node.left = node1
        new_node.right = node2
        nodes.append(new_node)
    return nodes[0]


dict={}
def parcours_en_profondeur(node, code=""):

    if node.is_leaf():
        dict[node.char]=code

    if node.has_left_child():
        parcours_en_profondeur(node.left, code + "0")

    if node.has_right_child():
        parcours_en_profondeur(node.right, code + "1")
    

def determiner_taux_de_compression (volume_texte_initial, volume_text_cmp):
    taux_de_compression  = 1 - volume_text_cmp / volume_texte_initial
    return taux_de_compression


def determiner_nbr_moy_de_bits(text, text_compresse):
    total_bits = len(text_compresse) * 8
    total_chars = len(text)
    nbr_moy_bits= total_bits / total_chars
    return nbr_moy_bits
    








#text = 'Alice was beginning to get very tired of sitting by her sister'


alpha=open("C:\\Users\\hp\\OneDrive\\Bureau\\alice.txt","r")
lines=alpha.read().splitlines()
text=""
for j in range(len(lines)):
    text+=lines[j]
l = determine_alphabet_and_frequencies(text)        
print (l)       
tree=cree_arbre(l)


parcours_en_profondeur(tree, code="")
print(dict)

textcomp=""
for i in dict.values():
    textcomp+=i
print(textcomp)

bytes_data = bytes(textcomp, 'utf-8')
with open('textcomp.bin', 'wb') as file_comp:
    file_comp.write(bytes_data)

print(determiner_nbr_moy_de_bits(text, textcomp))
