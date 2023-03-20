import asyncio
import json



import pyecharts.options as opts
from pyecharts.charts import Graph

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.apache.org/examples/editor.html?c=graph-npm

目前无法实现的功能:

1、暂无
"""





# 获取官方的数据
with open('data.json') as f:
    data = json.loads(f.read())
    # print(temp)

nodes = [
    {
        "x": node["x"],
        "y": node["y"],
        "id": node["id"],
        "name": node["name"],
        "symbolSize": node["symbolSize"],
        "itemStyle": {"normal": {"color": 'rgb(0,0,0)'}},
    }
    for node in data["nodes"]
]

edges = [
    {"source": edge["source"], "target": edge["target"]} for edge in data["links"]
]

(
    Graph()
    .add(
        series_name="",
        nodes=nodes,
        links=edges,
        layout="none",
        is_roam=True,
        is_focusnode=True,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=0.5, curve=0.3, opacity=0.7),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="NPM Dependencies"))
    .render("npm_dependencies.html")
)
