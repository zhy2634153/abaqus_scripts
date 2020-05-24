#!/usr/bin/env python3
#-*-coding:utf-8-*-

from abaqus import *

def extract_K1_from_odb(odb_name, nodes):
    """
    extract coordinates and K1 at the nodes in tuple nodes from odb named odb_name
    """
    odb = session.openOdb(odb_name)
    step = odb.steps.values()[-1]
    historyOutputs = step.historyRegions["ElementSet . ALL ELEMENTS"].historyOutputs
    
    result = [[],[]]
    for node in nodes:
        coord_x = historyOutputs["X at SIF_CRACK-1_CRACK_1-F{}_".format(node)].data[0][1]
        coord_y = historyOutputs["Y at SIF_CRACK-1_CRACK_1-F{}_".format(node)].data[0][1]
        coord_z = historyOutputs["Z at SIF_CRACK-1_CRACK_1-F{}_".format(node)].data[0][1]
        result[0].append((coord_x, coord_y, coord_z))
        for i in range(6):
            result[1].append(historyOutputs["K1 at SIF_CRACK-1_CRACK_1-F{}__Contour_{}".format(node, i+1)].data[0][1])
    odb.close()
    return result

if __name__ == "__main__":
    odb_name = "SG_Cracks_P_Submodel_at01_ac033.odb"
    nodes = (1,61,31)
    extract_K1_from_odb(odb_name, nodes)
