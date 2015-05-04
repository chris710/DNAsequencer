import networkx as nx
# TODO import sequences from a file
sequences = ['ATGC','TGCA','GCGG','CAGG','AGGT','GGTC','GTCC','CCAT','CATA']
l = len(sequences[1])   # single sequence length

G = nx.DiGraph()    # main graph

# Step 1.
# Create vertices in a graph.
for s in sequences:
    G.add_node(s)

# Step 2.
# Create arches between vertices.
def calc_diff(s1,s2):
    d = 1
    it = 0
    while it+d < l:    # TODO correct to l-3 later.
        if s1[it] != s2[it+d]:
            d += 1
            it = 0
            continue
        it += 1
    return d

for v1 in G.nodes(False):
    for v2 in G.nodes(False):
        if v1 == v2:
            continue
        diff = calc_diff(v1, v2)
        if diff < l:
            G.add_edge(v1, v2, weight=diff)

# Step 3.
# Find one step of the path.
