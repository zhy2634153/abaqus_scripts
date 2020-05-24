#!/usr/bin/env python3
#-*-coding:utf-8-*-

from extract_K1_from_odb import *
import os

workdir = r"E:\workdir\ABAQUS\ECUST\SG_with_Crack\Crack_P"

# odb_names=[]
# substrs = ["submodel", "at", "ac", ".odb"]
# for file in os.listdir(workdir):
#     filepath = os.path.join(workdir, file)
#     if os.path.isfile(filepath):
#         if all(substr in file for substr in substrs):
#             odb_names.append(filepath.replace("/", "\\"))

# for odb_name in odb_names:
#     pass

# nodes for ac033_at{01,02,03,04,05}, ac05_at{01,02,03,04,05}
nodes = [(1,31,61),(1,31,61), (1,61,62,122),(1,41,42,82), (1,61,121), (1,31,61),(1,41,42,82),(1,41,42,82), (1,41,42,82), (1,41,81)]

i = 0
f = open("K1_results.txt", "w")
for ac in "033 05".split():
    for at in "01 02 03 04 05".split():
        odb_name = "{}\\SG_Cracks_P_Submodel_at{}_ac{}.odb".format(workdir, at, ac)

        result = extract_K1_from_odb(odb_name, nodes[i])
        f.write(odb_name+"\n")
        for j in range(len(nodes[i])):
        # for node in nodes[i]:
            f.write("Node {}\n".format(nodes[i][j]))
            f.write("coordinates\n {}\n".format(result[0][j]))
            f.write("K1 of contour_1~6\n")
            f.write("{}\n".format(result[1][6*j: 6*(j+1)]))
        i+=1

f.close()
