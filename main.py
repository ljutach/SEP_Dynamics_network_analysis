import pandas as pd
import os
import networkx as nx
import graph_creation
import centrality_measures
import graphs_meta
import csv

csv_dataset_path = "SEP_dataset"
list_of_csv_files = []

for filename in os.listdir(csv_dataset_path):
    if filename.endswith('.csv'):
        list_of_csv_files.append(os.path.join(csv_dataset_path, filename))

list_of_csv_files = sorted(list_of_csv_files)






degree_table = centrality_measures.get_degree_centrality_measure(list_of_csv_files)\
.pivot_table(index='Node_Label', columns='year', values='Degree_Centrality')
degree_table["n"] = degree_table.count(axis=1)
degree_table = degree_table.sort_values(by=["n","Node_Label"], ascending=False)
degree_table = degree_table[degree_table.n.gt(1)]
degree_table = degree_table.drop(columns=["n"])
# print("\ndegree centrality table:")
# print("\n" + str(degree_table.drop(columns=["n"])))

degree_table.to_csv("degree_centrality_table.csv", index=True)

betweenness_table = centrality_measures.get_betweenness_centrality_measure(list_of_csv_files)\
.pivot_table(index='Node_Label', columns='year', values='Betweenness_Centrality')
betweenness_table["n"] = betweenness_table.count(axis=1)
betweenness_table = betweenness_table.sort_values(by=["n", "Node_Label"], ascending=False)
betweenness_table = betweenness_table[betweenness_table.n.gt(1)]
betweenness_table = betweenness_table.drop(columns=["n"])
# print("\nbetweenness centrality table:")
# print("\n" + str(betweenness_table))

betweenness_table.to_csv("betweenness_table.csv", index=True)



eigenvector_table = centrality_measures.get_eigenvector_centrality_measure(list_of_csv_files)\
.pivot_table(index='Node_Label', columns='year', values='Eigenvector_Centrality')
eigenvector_table["n"] = eigenvector_table.count(axis=1)
eigenvector_table = eigenvector_table.sort_values(by=["n", "Node_Label"], ascending=False)
eigenvector_table = eigenvector_table[eigenvector_table.n.gt(1)]
eigenvector_table = eigenvector_table.drop(columns=["n"])
print(eigenvector_table)
# print("\neigenvector centrality table:")
# print("\n" + str(eigenvector_table.drop(columns=["n"])))

eigenvector_table.to_csv("eigenvector_centrality_table.csv", index=True)





data = []

for csv_file in list_of_csv_files:
    network_name = csv_file.split('/')[-1].split('.')[0]  

    graph_info = graphs_meta.graph_meta(csv_file)

    data.append({'Network Name': network_name,
                 'Number of Nodes': graph_info[1],  
                 'Number of Edges': graph_info[2]})

result_df = pd.DataFrame(data)

#print(result_df)


for csv_file in list_of_csv_files:
    output_df = pd.DataFrame()
    output_df = graphs_meta.graph_meta(csv_file)
    print(output_df)












# degree_table = centrality_measures.get_degree_centrality_measure(list_of_csv_files)\
# .pivot_table(index='Node_Label', columns='year', values='Degree_Centrality')
# degree_table["n"] = degree_table.count(axis=1)
# degree_table = degree_table.sort_values(by=["n", "Node_Label"], ascending=False)
# degree_table = degree_table[degree_table.n.gt(2)]
# print("\ndegree centrality table:")
# print("\n" + str(degree_table))