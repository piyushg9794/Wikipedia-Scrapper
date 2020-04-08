import requests
from bs4 import BeautifulSoup
import pandas as pd
import pydot

def make_graph(node_list, node_a, node_b):
    
    node_a = pydot.Node(node_a)
    grp.add_node(node_a)
    node_list.append(node_a)
    
    if node_b!= None:
        edge = pydot.Edge(node_a, node_b)
        grp.add_edge(edge)
        