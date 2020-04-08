import requests
from bs4 import BeautifulSoup
import pandas as pd
import pydot
import make_graph.py

def get_content(some_soup, prev_node_list):
    
    try:
        content = some_soup.find(id="toc")
        content_links = content.find_all('a')
        content_sublink_list=[]
        node_list=[]

        if prev_node_list == None:
            node_2= None

            for l in content_links:

                link = l['href']
                link = link[1:]
                make_graph(node_list, link, node_2)
                content = some_soup.find(id=link).parent
                content = content.find_next_sibling()
                content_sublink = content.find_all('a')
                content_sublink_list.append(content_sublink)

        else:
            
            try:

                for (l,node_2) in zip(content_links, prev_node_list):

                    link = l['href']
                    link = link[1:]
                    make_graph(node_list, link, node_2)
                    content = some_soup.find(id=link).parent
                    content = content.find_next_sibling()
                    content_sublink = content.find_all('a')
                    content_sublink_list.append(content_sublink)
            except:
                return

        return content_sublink_list, node_list
    
    except:
        return