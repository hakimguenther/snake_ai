import math as math

#pos1 and pos2 are tuples
def euclideDistance(pos1,pos2):
    return math.sqrt((pos2[0]-pos1[0])**2+(pos2[1]-pos1[1])**2)