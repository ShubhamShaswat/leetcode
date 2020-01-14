#### 细分图中的可到达结点/Reachable Nodes In Subdivided Graph
**难度：** 困难/Hard

**Question：** 

<p>Starting with an&nbsp;<strong>undirected</strong> graph (the &quot;original graph&quot;) with nodes from <code>0</code> to <code>N-1</code>, subdivisions are made to some of the edges.</p>

<p>The graph is given as follows: <code>edges[k]</code> is a list of integer pairs <code>(i, j, n)</code> such that <code>(i, j)</code> is an edge of the original graph,</p>

<p>and <code>n</code> is the total number of <strong>new</strong> nodes on that edge.&nbsp;</p>

<p>Then, the edge <code>(i, j)</code> is deleted from the original graph,&nbsp;<code>n</code>&nbsp;new nodes <code>(x_1, x_2, ..., x_n)</code> are added to the original graph,</p>

<p>and <code>n+1</code> new&nbsp;edges <code>(i, x_1), (x_1, x_2), (x_2, x_3), ..., (x_{n-1}, x_n), (x_n, j)</code>&nbsp;are added to the original&nbsp;graph.</p>

<p>Now, you start at node <code>0</code>&nbsp;from the original graph, and in each move, you travel along one&nbsp;edge.&nbsp;</p>

<p>Return how many nodes you can reach in at most <code>M</code> moves.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><code>edges </code>= <span id="example-input-1-1">[[0,1,10],[0,2,1],[1,2,2]]</span>, M = <span id="example-input-1-2">6</span>, N = <span id="example-input-1-3">3</span>
<strong>Output: </strong><span id="example-output-1">13</span>
<strong>Explanation: </strong>
The nodes that are reachable in the final graph after M = 6 moves are indicated below.
<span><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/01/origfinal.png" style="width: 487px; height: 200px;" /></span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><code>edges </code>= <span id="example-input-2-1">[[0,1,4],[1,2,6],[0,2,8],[1,3,1]]</span>, M = <span id="example-input-2-2">10</span>, N = <span id="example-input-2-3">4</span>
<strong>Output: </strong><span id="example-output-2">23</span></pre>

<p>&nbsp;</p>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= edges.length &lt;= 10000</code></li>
	<li><code>0 &lt;= edges[i][0] &lt;&nbsp;edges[i][1] &lt; N</code></li>
	<li>There does not exist any&nbsp;<code>i != j</code> for which <code>edges[i][0] == edges[j][0]</code> and <code>edges[i][1] == edges[j][1]</code>.</li>
	<li>The original graph&nbsp;has no parallel edges.</li>
	<li><code>0 &lt;= edges[i][2] &lt;= 10000</code></li>
	<li><code>0 &lt;= M &lt;= 10^9</code></li>
	<li><code><font face="monospace">1 &lt;= N &lt;= 3000</font></code></li>
	<li>A reachable node is a node that can be travelled to&nbsp;using at most&nbsp;M moves starting from&nbsp;node 0.</li>
</ol>

<div>
<div>&nbsp;</div>
</div>


------

**题目：** 
<p>从具有&nbsp;<code>0</code> 到 <code>N-1</code> 的结点的<strong>无向</strong>图（&ldquo;原始图&rdquo;）开始，对一些边进行细分。</p>

<p>该图给出如下：<code>edges[k]</code>&nbsp;是整数对&nbsp;<code>(i, j, n)</code>&nbsp;组成的列表，使&nbsp;<code>(i, j)</code> 是原始图的边。</p>

<p><code>n</code> 是该边上<strong>新</strong>结点的总数</p>

<p>然后，将边&nbsp;<code>(i, j)</code>&nbsp;从原始图中删除，将&nbsp;<code>n</code>&nbsp;个新结点&nbsp;<code>(x_1, x_2, ..., x_n)</code>&nbsp;添加到原始图中，</p>

<p>将&nbsp;<code>n+1</code>&nbsp;条新边&nbsp;<code>(i, x_1), (x_1, x_2), (x_2, x_3), ..., (x_{n-1}, x_n), (x_n, j)</code>&nbsp;添加到原始图中。</p>

<p>现在，你将从原始图中的结点&nbsp;<code>0</code>&nbsp;处出发，并且每次移动，你都将沿着一条边行进。</p>

<p>返回最多 <code>M</code> 次移动可以达到的结点数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong><code>edges </code>= [[0,1,10],[0,2,1],[1,2,2]], M = 6, N = 3
<strong>输出：</strong>13
<strong>解释：</strong>
在 M = 6 次移动之后在最终图中可到达的结点如下所示。
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/01/origfinal.png" style="height: 200px; width: 487px;">
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong><code>edges </code>= [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], M = 10, N = 4
<strong>输出：</strong>23</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>0 &lt;= edges.length &lt;= 10000</code></li>
	<li><code>0 &lt;= edges[i][0] &lt;&nbsp;edges[i][1] &lt; N</code></li>
	<li>不存在任何&nbsp;<code>i != j</code>&nbsp;情况下&nbsp;<code>edges[i][0] == edges[j][0]</code>&nbsp;且&nbsp;<code>edges[i][1] == edges[j][1]</code>.</li>
	<li>原始图没有平行的边。</li>
	<li><code>0 &lt;= edges[i][2] &lt;= 10000</code></li>
	<li><code>0 &lt;= M &lt;= 10^9</code></li>
	<li><code>1 &lt;= N &lt;= 3000</code></li>
	<li>可到达结点是可以从结点 <code>0</code> 开始使用最多 <code>M</code> 次移动到达的结点。</li>
</ol>

<p>&nbsp;</p>

