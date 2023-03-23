import json

import pandas as pd

with open('data.json') as f:
    data = json.load(f)

links = pd.DataFrame(data['links'])
nodes = pd.DataFrame(data['nodes'])
categories = pd.DataFrame(data['categories'])

nodes['id'] = 'a' + nodes['id']
links['source'] = 'a' + links['source']
links['target'] = 'a' + links['target']

# 统计各点的出度与入度作为symbolSize
merged_df = pd.merge(nodes[['id']], links.melt(), left_on='id', right_on='value')[['id', 'variable']]
counts = merged_df.groupby('id').size().reset_index(name='counts')
result = pd.merge(nodes[['id']], counts, on='id', how='left').fillna(0)
nodes['symbolSize'] = result['counts']

nodes = nodes.drop(columns=['x', 'y'])
nodes['name'] = 'node.' + nodes['category'].astype(str) + '.' + nodes['name'].astype(str)

links = links.merge(nodes[['id', 'name']], left_on='source', right_on='id', how='left')
links = links.rename(columns={'name': 'source_name'})
links = links.drop('id', axis=1)
links = links.merge(nodes[['id', 'name']], left_on='target', right_on='id', how='left')
links = links.rename(columns={'name': 'target_name'})
links = links.drop('id', axis=1)
links = links.drop(columns=['source', 'target'])
nodes = nodes.drop(columns=['category', 'id'])

targets = links.groupby("source_name")["target_name"].apply(list)
nodes["targets"] = nodes["name"].map(targets)

pd.set_option('display.max_columns', None)
nodes.rename(columns={'symbolSize': 'size', 'targets': 'imports'}, inplace=True)
print(nodes)
nodes.to_csv('nodes_arc.csv', index=False)
nodes.to_json('nodes_arc.json', orient='records')
