import pandas as pd
import os
import networkx as nx
import graph_creation
import regex as re


# def compute_degree_centrality_measures(graph):
#     degree_centrality = nx.degree_centrality(graph)
#     top_10_degree = dict(sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:10])
    
#     return {"degree_centrality": top_10_degree}

def compute_degree_centrality_measures(graph):
    degree_centrality = nx.degree_centrality(graph)
    top_10_degree = {node: round(value, 5) for node, value in sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:10]}
    
    return {"degree_centrality": top_10_degree}
        
    
def compute_betweenness_centrality_measures(graph):
    betweenness_centrality = nx.betweenness_centrality(graph)
    top_10_betweenness = {node: round(value, 5) for node, value in sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:10]}

    return {"betweenness_centrality": top_10_betweenness}


def compute_eigenvector_centrality_measures(graph):
    eigenvector_centrality = nx.eigenvector_centrality(graph)
    top_10_eigenvector = {node: round(value, 5) for node, value in sorted(eigenvector_centrality.items(), key=lambda x: x[1], reverse=True)[:10]}

    return {"eigenvector_centrality": top_10_eigenvector}


#---------------------------------------------------------------------------


def get_degree_centrality_measure(csv_files):

    out_df = pd.DataFrame()
    
    for csv_file in csv_files:
        
        graph = graph_creation.read_csv_to_graph(csv_file)
        n_nodes = graph.number_of_nodes()
        centrality_measures = compute_degree_centrality_measures(graph)

        
        
        df_degree = pd.DataFrame.from_dict(centrality_measures['degree_centrality'],
                                    orient='index',
                                    columns=['Degree_Centrality']).rename_axis('Node_Label')
        df_degree["wdc"] = (df_degree["Degree_Centrality"] / (n_nodes - 1)) * 100
        pattern = r'(\d{4})_\w+(?=\.csv)'
        match = re.search(pattern, csv_file)
        if match:
            year = match.group(1)
            df_degree['year'] = year
        out_df = pd.concat([out_df, df_degree])    
        
    return out_df


def get_betweenness_centrality_measure(csv_files):

    out_df = pd.DataFrame()
    
    for csv_file in csv_files:
        
        graph = graph_creation.read_csv_to_graph(csv_file)
        n_nodes = graph.number_of_nodes()
        centrality_measures = compute_betweenness_centrality_measures(graph)

        df_betweenness = pd.DataFrame.from_dict(centrality_measures['betweenness_centrality'],
                                    orient='index',
                                    columns=['Betweenness_Centrality']).rename_axis('Node_Label')
        df_betweenness["wdc"] = (df_betweenness["Betweenness_Centrality"] / (n_nodes - 1)) * 100
        pattern = r'(\d{4})_\w+(?=\.csv)'
        match = re.search(pattern, csv_file)
        if match:
            year = match.group(1)
            df_betweenness['year'] = year
        out_df = pd.concat([out_df, df_betweenness])

    return out_df    



def get_eigenvector_centrality_measure(csv_files):

    out_df = pd.DataFrame()
    
    for csv_file in csv_files:
        
        graph = graph_creation.read_csv_to_graph(csv_file)
        n_nodes = graph.number_of_nodes()
        centrality_measures = compute_eigenvector_centrality_measures(graph)

        df_eigenvector = pd.DataFrame.from_dict(centrality_measures['eigenvector_centrality'],
                                    orient='index',
                                    columns=['Eigenvector_Centrality']).rename_axis('Node_Label')
        df_eigenvector["wdc"] = (df_eigenvector["Eigenvector_Centrality"] / (n_nodes - 1)) * 100
        pattern = r'(\d{4})_\w+(?=\.csv)'
        match = re.search(pattern, csv_file)
        if match:
            year = match.group(1)
            df_eigenvector['year'] = year
        out_df = pd.concat([out_df, df_eigenvector])

    return out_df