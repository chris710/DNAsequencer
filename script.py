import networkx as nx

# TODO import sequences from a file
sequences = ['ATGC','TGCA','GCGG','CAGG','AGGT','GGTC','GTCC','CCAT','CATA']
n = 13                  # complete sequence length
l = len(sequences[1])   # single sequence length
G = nx.DiGraph()        # main graph


# Step 1.
# Create vertices in a graph.
for s in sequences:
    G.add_node(s)


# Step 2.
# Create arches between vertices.
def calc_diff(s1, s2):
    diff = 1
    it = 0
    while it+diff < l:    # TODO correct to l-3 later.
        if s1[it] != s2[it+diff]:
            diff += 1
            it = 0
            continue
        it += 1
    return diff


for v1 in G.nodes(False):
    for v2 in G.nodes(False):
        if v1 == v2:
            continue
        diff = calc_diff(v1, v2)
        if diff < l:
            G.add_edge(v1, v2, weight=diff)


# Step 3.
# Find one step of the path.
def find_next(v1):
    best = []
    for a in G.out_edges(v1):
        v2 = a[1]
        for a2 in G.out_edges(v2):
            if not best['sum']:
                best['sum'] = a2['weight']
            if a2['weight'] < best['sum']:
                best['sum'] = a2['weight']
        best['sum'] += a['weight']
        if not best['value']:
            best['value'] = best['sum']
        if best['sum'] < best['value']:
            best['value'] = best['sum']
            best['v'] = v2
    return best['v']


# Step 4.
# Finds a path starting with v1.
def find_sequence(v1):
    result = []     # first is path, then size and sequence length
    result[0].append(v1)
    N = l           # temp counter
    while N < n:
        v2 = find_next(v2)
        result[0].append(v2)
        N += calc_diff(v1, v2)
        v1 = v2
        result[1] += 1
    result[2] = N
    return result


# Step 5.
# Finds best path among all starting nodes