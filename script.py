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
        if s2[it] != s1[it+diff]:
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
    best = {}
    for a in G.out_edges(v1, True):
        v2 = a[1]
        for a2 in G.out_edges(v2, True):
            if not ('sum' in best.keys()):
                best['sum'] = a2[2]['weight']
            if a2[2]['weight'] < best['sum']:
                best['sum'] = a2[2]['weight']
        best['sum'] += a[2]['weight']
        if not ('value' in best.keys()):
            best['value'] = best['sum']
        if best['sum'] <= best['value']:
            best['value'] = best['sum']
            best['v'] = v2
    return best['v'] or False


# Step 4.
# Finds a path starting with v1.
def find_sequence(v1):
    result = {
        'path': [],
        'size': 0,
    }     # first is path, then size and sequence length
    result['path'].append(v1)
    N = l           # sequence limit counter
    while N < n:    # TODO finda way to glue sequences into a string and add to result
        v2 = find_next(v1)
        if not v2:
            break
        result['path'].append(v2)
        N += calc_diff(v1, v2)
        v1 = v2
        result['size'] += 1
    result['length'] = N
    return result


# Step 5.
# Finds best path among all starting nodes
def find_best_sequence():
    best = {}
    for v in G.nodes(False):
        # TODO optimize
        seq = find_sequence(v)
        if not ('size' in best.keys()):
            best = seq
        if seq['size'] > best['size']:
            best = seq
    return best


# Test section.
best = find_best_sequence()
print(best['path'])
