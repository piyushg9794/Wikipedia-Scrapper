import requests
from bs4 import BeautifulSoup
import pandas as pd
import pydot
import get_content.py


base_url = 'https://en.wikipedia.org'
Starting_url = '/wiki/Outline_of_statistics'
page = requests.get(base_url + Starting_url)
soup = BeautifulSoup(page.text, 'html.parser')

grp = pydot.Dot(graph_name='stats', graph_type='digraph')

sublink1, nodelist1 = get_content(soup, None)

for li in sublink1:
    for l in li:
        links = l['href']
        page = requests.get(base_url + links)
        next_soup = BeautifulSoup(page.text, 'html.parser')
        try:
            content = next_soup.find(id="toc")
            content_links = content.find_all('a')
            content_sublink_list=[]
            node_list=[]

            for (l,node_2) in zip(content_links,nodelist1):

                        link = l['href']
                        link = link[1:]
                        make_graph(node_list, link, node_2)
                        content = next_soup.find(id=link).parent
                        content = content.find_next_sibling()
                        content_sublink = content.find_all('a')
                        content_sublink_list.append(content_sublink)
        except:
            break
        
grp.write_png('wiki_grp.png')