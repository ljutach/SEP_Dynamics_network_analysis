import pandas as pd
import networkx as nx



def graph_meta(file_path):
    df = pd.read_csv(file_path)

    G = nx.from_pandas_edgelist(df, source='source', target='target', create_using=nx.DiGraph)
    
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()

    return G, num_nodes, num_edges