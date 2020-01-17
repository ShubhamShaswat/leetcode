#### ?????/Is Graph Bipartite?
**??:** ??/Medium

**Question:** 

<p>Given an undirected&nbsp;<code>graph</code>, return <code>true</code> if and only if it is bipartite.</p>

<p>Recall that a graph is <em>bipartite</em> if we can split it&#39;s set of nodes into two independent&nbsp;subsets A and B such that every edge in the graph has one node in A and another node in B.</p>

<p>The graph is given in the following form: <code>graph[i]</code> is a list of indexes <code>j</code> for which the edge between nodes <code>i</code> and <code>j</code> exists.&nbsp; Each node is an integer between <code>0</code> and <code>graph.length - 1</code>.&nbsp; There are no self edges or parallel edges: <code>graph[i]</code> does not contain <code>i</code>, and it doesn&#39;t contain any element twice.</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> [[1,3], [0,2], [1,3], [0,2]]
<strong>Output:</strong> true
<strong>Explanation:</strong> 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
</pre>

<pre>
<strong>Example 2:</strong>
<strong>Input:</strong> [[1,2,3], [0,2], [0,1,3], [0,2]]
<strong>Output:</strong> false
<strong>Explanation:</strong> 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>graph</code> will have length in range <code>[1, 100]</code>.</li>
	<li><code>graph[i]</code> will contain integers in range <code>[0, graph.length - 1]</code>.</li>
	<li><code>graph[i]</code> will not contain <code>i</code> or duplicate values.</li>
	<li>The graph is undirected: if any element <code>j</code> is in <code>graph[i]</code>, then <code>i</code> will be in <code>graph[j]</code>.</li>
</ul>


------

**??:** 
<p>???????<code>graph</code>,???????????<code>true</code>?</p>

<p>????????????????????????A?B,??????????????????A??,????B??,?????????????</p>

<p><code>graph</code>??????????,<code>graph[i]</code>???????<code>i</code>?????????????????<code>0</code>?<code>graph.length-1</code>?????????????????:&nbsp;<code>graph[i]</code>&nbsp;????<code>i</code>,??<code>graph[i]</code>????????</p>

<pre>
<code>
<strong>?? 1:</strong>
??<strong>:</strong> [[1,3], [0,2], [1,3], [0,2]]
<strong>??:</strong> true
<strong>??:</strong> 
?????:
0----1
|    |
|    |
3----2
???????????: {0, 2} ? {1, 3}?
</code></pre>

<pre>
<code>
<strong>?? 2:</strong>
<strong>??:</strong> [[1,2,3], [0,2], [0,1,3], [0,2]]
<strong>??:</strong> false
<strong>??:</strong> 
?????:
0----1
| \  |
|  \ |
3----2
??????????????????
</code></pre>

<p><strong>??:</strong></p>

<ul>
	<li><code>graph</code> ?????? <code>[1, 100]</code>?</li>
	<li><code>graph[i]</code> ???????? <code>[0, graph.length - 1]</code>?</li>
	<li><code>graph[i]</code> ???? <code>i</code> ????????</li>
	<li>?????: ??<code>j</code> ? <code>graph[i]</code>??, ?? <code>i</code> ??? <code>graph[j]</code>???</li>
</ul>
