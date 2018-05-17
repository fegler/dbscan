from my_pack.dbscan_setup import setups
from my_pack.clustering import cluster
import sys


# global variables
'''
input_file_name = sys.argv[1]
cluster_number = int(sys.argv[2])
eps = int(sys.argv[3])
minPts = int(sys.argv[4])
'''
input_file_name = '../data/input1.txt'
cluster_number = 8
eps = 15
minPts = 22

# setups : input file stream
# points : point class objects
points = setups(input_file_name)
cluster(cluster_number, eps, minPts, points)
#print(points)