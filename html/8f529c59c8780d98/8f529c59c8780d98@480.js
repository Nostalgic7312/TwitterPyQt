function _1(md){return(
md`# Force-Directed Tree

A [force-directed layout](/@d3/force-directed-graph) of a tree using [*hierarchy*.links](https://github.com/d3/d3-hierarchy/blob/master/README.md#node_links).`
)}

function _chart(linksData,nodesData,d3,width,height,drag,invalidation)
{
  let links = linksData.filter(d => d.sourceSize + d.targetSize >500)
  // links.forEach(link => {
  //   // 假设link.source和link.target分别表示连线两端的节点
  //   const source = link.source;
  //   const target = link.target;

  //   // 为source节点添加neighbors属性
  //   if (!source.neighbors) {
  //       source.neighbors = [];
  //   }
  //   source.neighbors.push(target);

  //   // 为target节点添加neighbors属性
  //   if (!target.neighbors) {
  //       target.neighbors = [];
  //   }
  //   target.neighbors.push(source);
  // });
  let nodes = nodesData;
  let chargeScale=d3.scaleLinear().domain(d3.extent(nodes,d=>d.symbolSize)).range([-5,-125])
  let sizeScale=d3.scaleSqrt().domain(d3.extent(nodes,d=>d.symbolSize)).range([1,15])
  let strengthScale=d3.scaleLinear().domain(d3.extent(links,d=>d.targetSize+d.sourceSize)).range([0,1])
  // 创建模拟系统
  const simulation = d3.forceSimulation(nodes)
      .force("link", d3.forceLink(links).id(d => d.id).distance(10).strength(.01))
      .force("charge", d3.forceManyBody().strength(d=>chargeScale(d.symbolSize)))
      .force("x", d3.forceX())
      .force("y", d3.forceY())

  // 添加svg
  const svg = d3.create("svg")
      .attr("viewBox", [-width / 2, -height / 2, width, height])
      .call(d3.zoom().on("zoom", (event) => {
        node.attr("transform", event.transform);
        link.attr("transform", event.transform);
        text.attr('transform',event.transform)
      }));

  // 添加边
  let link = svg.append("g")
      .attr("stroke", "#999")
      .attr("stroke-opacity", 0.7)
    .selectAll("line")
    .data(links)
    .join("line")
    // .attr('fill',d=>{
    //   return  d.sourceSize+d.targetSize>1000?'#fff':'#000'
    // })
  let linkF=link.filter(d => d.sourceSize + d.targetSize >800)
  // .style("visibility", "none")
  // .attr("stroke-width", 0);
  
 // 添加节点
  const nodeColor=["#e21818","#00235b","#ffdd83","#98dfd6"];
  const node = svg.append("g")
      .attr("fill", "#fff")
      .attr("stroke", "#000")
      .attr("stroke-width", 1.5)
      .selectAll("circle")
      .data(nodes)
      .join("circle")
      .attr("fill", d => nodeColor[d.category])
      .attr('stroke-width',.5)
      .attr("r", d=>sizeScale(d.symbolSize))
      .call(drag(simulation))

  // 添加鼠标悬停事件
    node.on("mouseover", (event, d) => {
      node
        .transition()
        .duration(1000)
        .style("opacity", n => isConnected(d, n) ? 1 : 0.1);
      
      text
        .transition()
        .duration(1000)
        .style("display", n => isConnected(d, n)&n.symbolSize > 400||n==d? "block" : "none");
      
      // linkF=link.filter(l => l.source === d || l.target === d)
      
      linkF
        .transition()
        .duration(1000)
        .style("opacity", l => l.source === d || l.target === d ? 1 : 0.1);

      
      // 过滤出与当前节点相关联的边
      // const relatedLinks = linksData.filter();
      // // 创建它们的line元素，并设置样式或属性
      // linkF.enter()
      //   .append("line")
      //   .data(relatedLinks)
      //   .attr("x1", d => d.source.x)
      //   .attr("y1", d => d.source.y)
      //   .attr("x2", d => d.target.x)
      //   .attr("y2", d => d.target.y)
      //   .style("stroke", "red")
      //   .style("stroke-width", 3);
    })
    .on("mouseout", () => {
        node
          .transition()
          .duration(1000)
          .style("opacity", 1);
        text
        .transition()
        .duration(1000)
        .style("display", d => d.symbolSize > 1000 ? "block" : "none");
      
        linkF
          .transition()
          .duration(1000)
          .style("opacity", 1);
    });

function isConnected(a, b) {
    return linkedByIndex[`${a.index},${b.index}`] || linkedByIndex[`${b.index},${a.index}`] || a.index === b.index;
  // 使用深度优先搜索算法遍历图中所有与a直接或间接相关联的节点
    // const stack = [a];
    // const visited = new Set();
    // while (stack.length > 0) {
    //     const current = stack.pop();
    //     if (current === b) return true;
    //     visited.add(current);
    //     for (const neighbor of current.neighbors) {
    //         if (!visited.has(neighbor)) {
    //             stack.push(neighbor);
    //         }
    //     }
    // }
    // return false;
}

const linkedByIndex = {};
links.forEach(d => {
    linkedByIndex[`${d.source.index},${d.target.index}`] = true;
});


  // 添加图例
  const legend = svg.append("g")
    .attr("transform", "translate(-250,-470)");

  const legendData = nodeColor.map((color, i) => ({color: color, category: i}));

  const legendEntry = legend.selectAll("g")
    .data(legendData)
    .enter()
    .append("g")
    .attr("transform", (d,i) => `translate(${i*120},0)`);

  let isClick=false
  legendEntry.on("click", function(event, d) {
      const selectedNodes = d3.selectAll("circle").filter(n => n.category === d.category);
      const noselecteNdoes=d3.selectAll("circle").filter(n => n.category !== d.category);
      if(!isClick){
        selectedNodes.transition()
          .duration(1000)
          .style("opacity", 1);
    
        noselecteNdoes.transition()
          .duration(1000)
          .style("opacity", .1);
        isClick=true
      }else{
        selectedNodes.transition()
          .duration(1000)
          .style("opacity", 1);
      }
      
  });
  let rwidth = 20;
  let rheight = 20;
  let rradius = 5;
  
  const pathData = d3.path();
  pathData.moveTo(rradius, 0);
  pathData.lineTo(rwidth - rradius, 0);
  pathData.quadraticCurveTo(rwidth, 0, rwidth, rradius);
  pathData.lineTo(rwidth, rheight - rradius);
  pathData.quadraticCurveTo(rwidth, rheight, rwidth - rradius, rheight);
  pathData.lineTo(rradius,rheight);
  pathData.quadraticCurveTo(0,rheight ,0 ,rheight - rradius);
  pathData.lineTo(0,rradius);
  pathData.quadraticCurveTo(0 ,0 ,rradius ,0);

  legendEntry.append("path")
      .attr("d", pathData.toString())
      .attr("fill", d => d.color)
  
  legendEntry.append("text")
      .text(d => `Category ${d.category}`)
      .attr("x", 25)
      .attr("y", 15);

  // 添加标题
  // node.append("title")
  //     .text(d => d.name)
  
  // 添加默认文本
  const text = svg.append("g")
  .attr("fill", "#000")
  .selectAll("text")
  .data(nodes)
  .join("text")
  .text(d => d.name)
  .attr("x", d => d.x)
  .attr("y", d => d.y)
  .style("font-size", "12px")
  .style("display", d => d.symbolSize > 1000 ? "block" : "none")
  .style("text-anchor", "middle") // 水平居中对齐
  .style("dominant-baseline", "central")
  .style ("pointer-events" , "none")
  // .transition()
  // .duration(1000)
  
  simulation.on("tick", () => {
    linkF
        .attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);

    node
        .attr("cx", d => d.x)
        .attr("cy", d => d.y);

      // 更新text元素的位置
    text.attr("x", d => d.x ) 
        .attr("y", d => d.y ); 
  });

  invalidation.then(() => simulation.stop());

  return svg.node();
}


function _nodesData(FileAttachment){return(
FileAttachment("nodes.json").json()
)}

function _linksData(FileAttachment){return(
FileAttachment("links.json").json()
)}

function _height(){return(
1000
)}

function _drag(d3){return(
simulation => {
  
  function dragstarted(event, d) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
  }
  
  function dragged(event, d) {
    d.fx = event.x;
    d.fy = event.y;
  }
  
  function dragended(event, d) {
    if (!event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
  }
  
  return d3.drag()
      .on("start", dragstarted)
      .on("drag", dragged)
      .on("end", dragended);
}
)}

function _d3(require){return(
require("d3@6")
)}

export default function define(runtime, observer) {
  const main = runtime.module();
  function toString() { return this.url; }
  const fileAttachments = new Map([
    ["links.json", {url: new URL("./files/eb6e99b2ddd28fc9a34b48830cea7743c38c0015a150267fc071e0c9e69b54c3fba54c83a35271df72f71fe7f136476ddd35ce35cb7b6da3503931d15f3d698d.json", import.meta.url), mimeType: "application/json", toString}],
    ["nodes.json", {url: new URL("./files/e6216489dff6de95b92d61fb6f18a488aefbc85e62fdc8d8e7ce773697b75fd4995d725cabe81acf7fdac0904a6e51ed3fdaa46318584edc68059b2783e313a3.json", import.meta.url), mimeType: "application/json", toString}]
  ]);
  main.builtin("FileAttachment", runtime.fileAttachments(name => fileAttachments.get(name)));
  main.variable(observer()).define(["md"], _1);
  main.variable(observer("chart")).define("chart", ["linksData","nodesData","d3","width","height","drag","invalidation"], _chart);
  main.variable(observer("nodesData")).define("nodesData", ["FileAttachment"], _nodesData);
  main.variable(observer("linksData")).define("linksData", ["FileAttachment"], _linksData);
  main.variable(observer("height")).define("height", _height);
  main.variable(observer("drag")).define("drag", ["d3"], _drag);
  main.variable(observer("d3")).define("d3", ["require"], _d3);
  return main;
}
