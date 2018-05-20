from my_pack.dbscan_setup import file_input,output_file_setup
from my_pack.clustering import dbscan
import sys


input_file_name = sys.argv[1]
file_name = input_file_name[:(len(input_file_name) - 4)]
cluster_number = int(sys.argv[2])
eps = float(sys.argv[3])
minPts = int(sys.argv[4])

points = file_input(input_file_name)

result = dbscan(cluster_number, eps, minPts, points)

output_file_setup(file_name, cluster_number, result)