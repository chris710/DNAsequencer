import networkx as nx
import sys
import csv
import time

sequences = []

# Loading sequences from a file.
filename = sys.argv[1]
f = open(filename, 'r')
for line in f:
        sequences.append(line[:-1])
file_info  = filename.split('.')
if '-' in filename:
    n = int(file_info[1][0:file_info[1].find('-')])     # complete sequence length
elif '+' in filename:
    n = int(file_info[1][0:file_info[1].find('+')])          # complete sequence length

l = len(sequences[1])   # single sequence length
G = nx.DiGraph()        # main graph

# Step 1.
# Create vertices in a graph.
for s in sequences:
    G.add_node(s, visited=False)    # implement checking if node was visited


# Step 2.
# Create arches between vertices.
def calc_diff(s1, s2):
    diff = 1
    it = 0
    while it+diff < l-2:
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
        if diff < l-3:
            G.add_edge(v1, v2, weight=diff)


# Step 3.
# Find one step of the path.
def find_next(v1):
    best = {}
    for a in G.out_edges(v1[0], True):
        v2 = a[1]
        visited = G.node[a[1]]['visited']
        for a2 in G.out_edges(v2, True):
            weight = a2[2]['weight']
            if visited:
                weight += 1
            if not ('sum' in best.keys()):
                best['sum'] = a2[2]['weight']
            if weight < best['sum']:
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
        'str': v1[0],
    }     # first is path, then size and sequence length
    result['path'].append(v1)
    # v1[1]['visited'] = True    # check as visited
    G.node[v1[0]]['visited'] = True    # check as visited
    N = l           # sequence limit counter
    while N < n:
        v2_name = find_next(v1)
        v2_visited = G.node[v2_name]
        v2 = (v2_name, v2_visited)
        if not v2[0]:
            break
        result['path'].append(v2)
        diff = calc_diff(v1[0], v2[0])
        N += diff
        result['str'] += v2[0][-diff:]
        if not v2_visited['visited']:
            result['size'] += 1     # increase only if not visited
        G.node[v2_name]['visited'] = True   # check as visited
        v1 = v2
    result['length'] = N
    return result


# Step 5.
# Finds best path among all starting nodes.
def find_best_sequence():
    best = {}
    counter = 0
    for v in G.nodes(True):
        counter += 1
        reset_visited()     # reset visited flags
        print ("%.2f" % float(float(counter)/len(sequences)*100) + ' %')    # show percentage
        if check_first(v):
            seq = find_sequence(v)
            if not ('size' in best.keys()):
                best = seq
            if seq['size'] > best['size']:
                best = seq
            # print(best['path'])   # for debugging purposes
        # print('miss')     # for debugging purposes
    return best


# Resets visited flags
def reset_visited():
    for v in G.nodes(True):
        v[1]['visited'] = False     # check as visited

# Checks whether a node can be used as a starting point.
def check_first(v):
    for a in G.in_edges(v[0], True):
        if a[2]['weight'] == 1:
            return False
    return True

# Test section.
best = find_best_sequence()

print(best['str'])
print(str(best['size'])+"/"+str(len(sequences))+" max")
print("%.2f" % float(best['size']/float(len(sequences))*100)+"% efficiency")

with open('stat.csv', 'ab') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow([filename, best['size'], len(sequences), float(best['size']/float(len(sequences))*100), time.clock()])
