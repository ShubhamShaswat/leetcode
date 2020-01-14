#### 克隆图/Clone Graph
**难度：** 中等/Medium

**Question：** 

<p>Given&nbsp;a reference of a node in a&nbsp;<strong><a href="https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph" target="_blank">connected</a></strong>&nbsp;undirected graph, return a <a href="https://en.wikipedia.org/wiki/Object_copying#Deep_copy" target="_blank"><strong>deep copy</strong></a> (clone) of the graph. Each node in the graph contains a val (<code>int</code>) and a list (<code>List[Node]</code>) of its neighbors.</p>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png" style="width: 500px;height:550px" /></p>

<pre>
<strong>Input:
</strong>{&quot;$id&quot;:&quot;1&quot;,&quot;neighbors&quot;:[{&quot;$id&quot;:&quot;2&quot;,&quot;neighbors&quot;:[{&quot;$ref&quot;:&quot;1&quot;},{&quot;$id&quot;:&quot;3&quot;,&quot;neighbors&quot;:[{&quot;$ref&quot;:&quot;2&quot;},{&quot;$id&quot;:&quot;4&quot;,&quot;neighbors&quot;:[{&quot;$ref&quot;:&quot;3&quot;},{&quot;$ref&quot;:&quot;1&quot;}],&quot;val&quot;:4}],&quot;val&quot;:3}],&quot;val&quot;:2},{&quot;$ref&quot;:&quot;4&quot;}],&quot;val&quot;:1}

<strong>Explanation:</strong>
Node 1&#39;s value is 1, and it has two neighbors: Node 2 and 4.
Node 2&#39;s value is 2, and it has two neighbors: Node 1 and 3.
Node 3&#39;s value is 3, and it has two neighbors: Node 2 and 4.
Node 4&#39;s value is 4, and it has two neighbors: Node 1 and 3.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>The number of nodes will be between 1 and 100.</li>
	<li>The undirected&nbsp;graph is a <a href="https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)#Simple_graph" target="_blank">simple graph</a>,&nbsp;which means no repeated edges and no self-loops in the graph.</li>
	<li>Since the graph is undirected, if node <em>p</em>&nbsp;has node <em>q</em>&nbsp;as&nbsp;neighbor, then node <em>q</em>&nbsp;must have node <em>p</em>&nbsp;as neighbor too.</li>
	<li>You must return the <strong>copy of the given node</strong> as a reference to the cloned graph.</li>
</ol>

------

**题目：** 
<p>给定无向<a href="https://baike.baidu.com/item/连通图/6460995?fr=aladdin" target="_blank"><strong>连通</strong></a>图中一个节点的引用，返回该图的<a href="https://baike.baidu.com/item/深拷贝/22785317?fr=aladdin" target="_blank"><strong>深拷贝</strong></a>（克隆）。图中的每个节点都包含它的值 <code>val</code>（<code>Int</code>） 和其邻居的列表（<code>list[Node]</code>）。</p>

<p><strong>示例：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/113_sample.png" style="height: 149px; width: 200px;"></p>

<pre><strong>输入：
</strong>{&quot;$id&quot;:&quot;1&quot;,&quot;neighbors&quot;:[{&quot;$id&quot;:&quot;2&quot;,&quot;neighbors&quot;:[{&quot;$ref&quot;:&quot;1&quot;},{&quot;$id&quot;:&quot;3&quot;,&quot;neighbors&quot;:[{&quot;$ref&quot;:&quot;2&quot;},{&quot;$id&quot;:&quot;4&quot;,&quot;neighbors&quot;:[{&quot;$ref&quot;:&quot;3&quot;},{&quot;$ref&quot;:&quot;1&quot;}],&quot;val&quot;:4}],&quot;val&quot;:3}],&quot;val&quot;:2},{&quot;$ref&quot;:&quot;4&quot;}],&quot;val&quot;:1}

<strong>解释：</strong>
节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
节点 4 的值是 4，它有两个邻居：节点 1 和 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>节点数介于 1 到 100 之间。</li>
	<li>无向图是一个<a href="https://baike.baidu.com/item/简单图/1680528?fr=aladdin" target="_blank">简单图</a>，这意味着图中没有重复的边，也没有自环。</li>
	<li>由于图是无向的，如果节点 <em>p</em> 是节点 <em>q</em> 的邻居，那么节点 <em>q</em> 也必须是节点 <em>p</em>&nbsp;的邻居。</li>
	<li>必须将<strong>给定节点的拷贝</strong>作为对克隆图的引用返回。</li>
</ol>

