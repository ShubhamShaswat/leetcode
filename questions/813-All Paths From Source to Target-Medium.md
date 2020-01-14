#### 所有可能的路径/All Paths From Source to Target
**难度：** 中等/Medium

**Question：** 

<p>Given a directed, acyclic graph of <code>N</code> nodes.&nbsp; Find all possible paths from node <code>0</code> to node <code>N-1</code>, and return them in any order.</p>

<p>The graph is given as follows:&nbsp; the nodes are 0, 1, ..., graph.length - 1.&nbsp; graph[i] is a list of all nodes j for which the edge (i, j) exists.</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> [[1,2], [3], [3], []] 
<strong>Output:</strong> [[0,1,3],[0,2,3]] 
<strong>Explanation:</strong> The graph looks like this:
0---&gt;1
|    |
v    v
2---&gt;3
There are two paths: 0 -&gt; 1 -&gt; 3 and 0 -&gt; 2 -&gt; 3.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>The number of nodes in the graph will be in the range <code>[2, 15]</code>.</li>
	<li>You can print different paths in any order, but you should keep the order of nodes inside one path.</li>
</ul>

------

**题目：** 
<p>给一个有&nbsp;<code>n</code>&nbsp;个结点的有向无环图，找到所有从&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n-1</code>&nbsp;的路径并输出（不要求按顺序）</p>

<p>二维数组的第 i 个数组中的单元都表示有向图中 i 号结点所能到达的下一些结点（译者注：有向图是有方向的，即规定了a&rarr;b你就不能从b&rarr;a）空就是没有下一个结点了。</p>

<pre><strong>示例:</strong>
<strong>输入:</strong> [[1,2], [3], [3], []] 
<strong>输出:</strong> [[0,1,3],[0,2,3]] 
<strong>解释:</strong> 图是这样的:
0---&gt;1
|    |
v    v
2---&gt;3
这有两条路: 0 -&gt; 1 -&gt; 3 和 0 -&gt; 2 -&gt; 3.
</pre>

<p><strong>提示:</strong></p>

<ul>
	<li>结点的数量会在范围&nbsp;<code>[2, 15]</code>&nbsp;内。</li>
	<li>你可以把路径以任意顺序输出，但在路径内的结点的顺序必须保证。</li>
</ul>

