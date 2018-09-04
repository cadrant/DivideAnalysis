# -*- coding: utf-8 -*-
from collections import Counter
import random

def create_graph():
    #with open("exampleMinCut.txt") as f:
    with open("kargerMinCut.txt") as f:
        G={}
        vertex_lines = f.readlines();
        for line in vertex_lines:
            fields = [int(field) for field in line.strip().split('\t')];
            G[fields[0]] = fields[1:]
    return G

'''While there are more than 2 vertices:
 pick a remaining edge (u,v) uniformly at random
 merge (or contract) u and v into a single vertex
 remove self-loops
return cut represented by final 2 vertices.
'''
def find_min_cut(O):

    G = O.copy()
       
    while True:
        vertices = G.keys()

        # The last edge
        if len(vertices) <= 2:
            break
        # Pick a random edge u, v
        # This is not a uniformly random edge
        u = random.choice(list(G.keys()))
        v = random.choice(G[u])

        # It is only the contracting edges that are lost
        # Contract v into u
        # Substitute u for v in all of v's neighbors (including u)
        for n in G[v]:
            G[n] = [u if x == v else x for x in G[n]]
        # Combine u and v
        G[u] = G[u] + G[v]

        # Remove all references to u in G[u].  These are self loops.
        G[u] = [x for x in G[u] if x != u]

        del G[v]
    return G
        
cuts = []           
O = create_graph()

for x in range(0,800):
    min_cut = find_min_cut(O)
    mcv = min_cut.keys()
    mcv.sort()
    print str(x) + ": = " + str(mcv)
    cuts.append(str(mcv))

#print cuts
cnt = Counter(cuts)
#print cnt
print cnt.most_common(1)
#print cnt[0]
#print cnt[1]
#print cnt[2]

'''
with open("min_cuts.txt",mode='w') as of:
    for min_cut in cuts:
        of.write("%s\n" % min_cut)
'''
