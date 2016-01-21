import numpy as np
import matplotlib.pyplot as plt
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: python plaid.py <name of edgelist file>"
        print "edgelist files like from snap.stanford.edu"
    edgelist_file = sys.argv[1]
    adjmat = np.zeros((1000, 1000))
    line_num = 0
    with open(edgelist_file) as edgelist_file:
        for line in edgelist_file:
            line_num += 1
            if line[0] == "#":
                continue
            if line_num % 10000 == 0:
                print line_num
            fst, snd = line.strip().split()
            fst, snd = int(fst), int(snd)
            if fst < 1000 and snd < 1000:
                adjmat[fst, snd] = 1
    plt.imshow(adjmat)
    plt.show()
