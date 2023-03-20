import json

import pandas as pd

with open('data.json') as f:
    data = json.load(f)

links = pd.DataFrame(data['links'])
nodes = pd.DataFrame(data['nodes'])
categories = pd.DataFrame(data['categories'])

print(nodes)
print(links)

print(nodes['category'].value_counts())
print(links['source'].isin(nodes['id']).value_counts())
print(links['target'].isin(nodes['id']).value_counts())

nodes['id'] = 'a' + nodes['id']
links['source'] = 'a' + links['source']
links['target'] = 'a' + links['target']

# 统计各点的出度与入度作为symbolSize
merged_df = pd.merge(nodes[['id']], links.melt(), left_on='id', right_on='value')[['id', 'variable']]
counts = merged_df.groupby('id').size().reset_index(name='counts')
result = pd.merge(nodes[['id']], counts, on='id', how='left').fillna(0)
nodes['symbolSize'] = result['counts']

print(nodes)

# 用边连接的最大的节点作为边的权重
links['max_symbolSize'] = links.apply(lambda row: max(nodes.loc[nodes['id'] == row['source'], 'symbolSize'].max(),
                                                      nodes.loc[nodes['id'] == row['target'], 'symbolSize'].max()),
                                      axis=1)

links['sourceSize'] = links.apply(lambda row: nodes.loc[nodes['id'] == row['source'], 'symbolSize'].max(), axis=1)
links['targetSize'] = links.apply(lambda row: nodes.loc[nodes['id'] == row['target'], 'symbolSize'].max(), axis=1)
print(links)

print(len(links[links['targetSize'] + links['sourceSize'] > 800]))


# links.to_csv('a_links.csv', index=False)
# nodes.to_csv('a_nodes.csv', index=False)
#
# links.to_json('links.json',orient='records')
# nodes.to_json('nodes.json',orient='records')
def printScale():
    print('-----------------种子节点在source的比例------------------')
    print(nodes[nodes['category'] == 0]['id'].isin(links['source']).value_counts())
    print('-----------------种子节点在target的比例------------------')
    print(nodes[nodes['category'] == 0]['id'].isin(links['target']).value_counts())

    print('-----------------直接节点在source的比例------------------')
    print(nodes[nodes['category'] == 1]['id'].isin(links['source']).value_counts())
    print('-----------------直接节点在target的比例------------------')
    print(nodes[nodes['category'] == 1]['id'].isin(links['target']).value_counts())

    print('-----------------下属节点在source的比例------------------')
    print(nodes[nodes['category'] == 2]['id'].isin(links['source']).value_counts())
    print('-----------------下属节点在target的比例------------------')
    print(nodes[nodes['category'] == 2]['id'].isin(links['target']).value_counts())

    print('-----------------疑似节点在source的比例------------------')
    print(nodes[nodes['category'] == 3]['id'].isin(links['source']).value_counts())
    print('-----------------疑似节点在target的比例------------------')
    print(nodes[nodes['category'] == 3]['id'].isin(links['target']).value_counts())

# printScale()
