import numpy as np
import matplotlib.pyplot as plt
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: python plaid.py <name of edgelist file>"
        print "edgelist files like from snap.stanford.edu"
        print "big memory problems with the really really huge nets, tho"
        sys.exit(1)
    print "this is a sample of the first 2000 nodes of 8000 node network"
    print "but you can see it's fractal"
    edgelist_file = sys.argv[1]
    adjmat = np.zeros((2000, 2000))
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
            if fst < 2000 and snd < 2000:
                adjmat[fst, snd] = 1
    plt.imshow(adjmat, cmap='Greys')
    plt.title("Plaid network")
    plt.show()
