import numpy as np
import matplotlib.pyplot as plt
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: python plaid.py <name of edgelist file>"
        print "edgelist files like from snap.stanford.edu"
    edgelist_file = sys.argv[1]
    line_num = 0
    with open(edgelist_file) as edgelist_file:
        for line in edgelist_file:
            line_num += 1
            print line
            if line_num > 1000:
                break
