import pandas as pd
import networkx as nx



def read_csv_to_graph(file_path):
    df = pd.read_csv(file_path)
    
    # Drop duplicate edges
    #df.drop_duplicates(subset=['source', 'target'], inplace=True)

    G = nx.from_pandas_edgelist(df, source='source', target='target', create_using=nx.DiGraph)

    return G 