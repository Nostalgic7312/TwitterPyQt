import json

import pandas as pd

with open('data.json') as f:
    data = json.load(f)

links = pd.DataFrame(data['links'])
nodes = pd.DataFrame(data['nodes'])
categories = pd.DataFrame(data['categories'])

print(nodes['category'].value_counts())
print(links['source'].isin(nodes['id']).value_counts())
print(links['target'].isin(nodes['id']).value_counts())

nodes['id'] = 'a' + nodes['id']
links['source'] = 'a' + links['source']
links['target'] = 'a' + links['target']
print(nodes)
print(links)
# 统计各点的出度与入度作为symbolSize
merged_df = pd.merge(nodes[['id']], links.melt(), left_on='id', right_on='value')[['id', 'variable']]
counts = merged_df.groupby('id').size().reset_index(name='counts')
result = pd.merge(nodes[['id']], counts, on='id', how='left').fillna(0)
nodes['symbolSize'] = result['counts']

source_count = links.groupby('source').size().reset_index(name='source_count')
target_count = links.groupby('target').size().reset_index(name='target_count')
nodes = pd.merge(nodes, source_count, left_on='id', right_on='source', how='left')
nodes = pd.merge(nodes, target_count, left_on='id', right_on='target', how='left')
nodes.drop(columns=['source', 'target'], inplace=True)


# pd.set_option('display.max_columns', None)

def calculate_avg_target(row):
    # 获取当前id
    current_id = row['id']
    # 获取df2中source为当前id的所有行
    source_rows = links[links['source'] == current_id]
    # 获取所有target
    targets = source_rows['target']
    # 计算所有target在df1中对应的symbolSize的平均值
    avg_symbolSize = nodes[nodes['id'].isin(targets)]['symbolSize'].sum()
    return avg_symbolSize


def calculate_avg_source(row):
    # 获取当前id
    current_id = row['id']
    # 获取df2中source为当前id的所有行
    source_rows = links[links['target'] == current_id]
    # 获取所有target
    targets = source_rows['source']
    # 计算所有target在df1中对应的symbolSize的求和
    avg_symbolSize = nodes[nodes['id'].isin(targets)]['symbolSize'].sum()
    return avg_symbolSize


nodes['avg_symbolSize_s'] = nodes.apply(calculate_avg_target, axis=1)
nodes['avg_symbolSize_c'] = nodes.apply(calculate_avg_source, axis=1)

# 将nodes中的NaN替换为0
nodes.fillna(0, inplace=True)
# 将nodes中values中的0替换为100
nodes['values'] = nodes['values'].replace(0, 100)

nodes['EC'] = nodes['avg_symbolSize_s'] + nodes['avg_symbolSize_c']

nodes.drop(columns=['x', 'y', 'avg_symbolSize_s', 'avg_symbolSize_c', 'symbolSize'], inplace=True)


# temp = nodes['values']
# nodes.drop(labels=['values'], axis=1, inplace=True)
# nodes.insert(3, 'values', temp)
print(nodes.head(100))
nodes.to_json('nodes_parra.json', orient='records')
# nodes.to_csv('nodes_parra.csv', index=False)
# print(links)
# 用边连接的最大的节点作为边的权重
