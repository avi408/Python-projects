# Assignment 3 Dictionaries
# A program that combines several dictionaries into a new dictionary with all the keys of the original dictionaries
"""If a key appears in more than one input dictionary, the value corresponding to that key in the new dictionary should
   be a list containing all the values encountered in the input dictionaries that correspond to that key."""
d1={'pet1':'dog','pet2':'cat','pet3':'mouse'}
d2={'pet1':'tiger','pet4':'lion','pet5':'leopard'}
d3={'pet6':'horse','pet7':'deer','pet1':'rhino'}
#key 'pet1' has three values which are put into a list l4= ['dog','tiger','rhino']
l1=d1['pet1']
l2=d2['pet1']
l3=d3['pet1']
l4=[]
l4.append(l1)
l4.append(l2)
l4.append(l3)
d4={}
d4.update(d1)
d4.update(d2)
d4.update(d3)
d4['pet1']=[l4]
print(d4)

