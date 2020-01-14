#### 四叉树交集/Quad Tree Intersection
**难度：** 简单/Easy

**Question：** 

<p>A quadtree is a tree data in which each internal node has exactly four children: <code>topLeft</code>, <code>topRight</code>, <code>bottomLeft</code> and <code>bottomRight</code>. Quad trees are often used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions.</p>

<p>We want to store True/False information in our quad tree. The quad tree is used to represent a <code>N * N</code> boolean grid. For each node, it will be subdivided into four children nodes <strong>until the values in the region it represents are all the same</strong>. Each node has another two boolean attributes : <code>isLeaf</code> and <code>val</code>. <code>isLeaf</code> is true if and only if the node is a leaf node. The <code>val</code> attribute for a leaf node contains the value of the region it represents.</p>

<p>For example, below are two quad trees A and B:</p>

<pre>
A:
+-------+-------+   T: true
|       |       |   F: false
|   T   |   T   |
|       |       |
+-------+-------+
|       |       |
|   F   |   F   |
|       |       |
+-------+-------+
topLeft: T
topRight: T
bottomLeft: F
bottomRight: F

B:               
+-------+---+---+
|       | F | F |
|   T   +---+---+
|       | T | T |
+-------+---+---+
|       |       |
|   T   |   F   |
|       |       |
+-------+-------+
topLeft: T
topRight:
     topLeft: F
     topRight: F
     bottomLeft: T
     bottomRight: T
bottomLeft: T
bottomRight: F
</pre>

<p>&nbsp;</p>

<p>Your task is to implement a function that will take two quadtrees and return a quadtree that represents the logical OR (or union) of the two trees.</p>

<pre>
A:                 B:                 C (A or B):
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       | F | F |  |       |       |
|   T   |   T   |  |   T   +---+---+  |   T   |   T   |
|       |       |  |       | T | T |  |       |       |
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       |       |  |       |       |
|   F   |   F   |  |   T   |   F   |  |   T   |   F   |
|       |       |  |       |       |  |       |       |
+-------+-------+  +-------+-------+  +-------+-------+
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li>Both <code>A</code> and <code>B</code>&nbsp;represent grids of size <code>N * N</code>.</li>
	<li><code>N</code> is guaranteed to be a power of 2.</li>
	<li>If you want to know more about the quad tree, you can refer to its <a href="https://en.wikipedia.org/wiki/Quadtree">wiki</a>.</li>
	<li>The logic OR operation is defined as this: &quot;A or B&quot; is true if <code>A is true</code>, or if <code>B is true</code>, or if <code>both A and B are true</code>.</li>
</ol>


------

**题目：** 
<p>四叉树是一种树数据，其中每个结点恰好有四个子结点：<code>topLeft</code>、<code>topRight</code>、<code>bottomLeft</code>&nbsp;和&nbsp;<code>bottomRight</code>。四叉树通常被用来划分一个二维空间，递归地将其细分为四个象限或区域。</p>

<p>我们希望在四叉树中存储 True/False 信息。四叉树用来表示 <code>N * N</code> 的布尔网格。对于每个结点, 它将被等分成四个孩子结点<strong>直到这个区域内的值都是相同的</strong>。每个节点都有另外两个布尔属性：<code>isLeaf</code>&nbsp;和&nbsp;<code>val</code>。当这个节点是一个叶子结点时&nbsp;<code>isLeaf</code>&nbsp;为真。<code>val</code>&nbsp;变量储存叶子结点所代表的区域的值。</p>

<p>例如，下面是两个四叉树 A 和 B：</p>

<pre>A:
+-------+-------+   T: true
|       |       |   F: false
|   T   |   T   |
|       |       |
+-------+-------+
|       |       |
|   F   |   F   |
|       |       |
+-------+-------+
topLeft: T
topRight: T
bottomLeft: F
bottomRight: F

B:               
+-------+---+---+
|       | F | F |
|   T   +---+---+
|       | T | T |
+-------+---+---+
|       |       |
|   T   |   F   |
|       |       |
+-------+-------+
topLeft: T
topRight:
     topLeft: F
     topRight: F
     bottomLeft: T
     bottomRight: T
bottomLeft: T
bottomRight: F
</pre>

<p>&nbsp;</p>

<p>你的任务是实现一个函数，该函数根据两个四叉树返回表示这两个四叉树的逻辑或(或并)的四叉树。</p>

<pre>A:                 B:                 C (A or B):
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       | F | F |  |       |       |
|   T   |   T   |  |   T   +---+---+  |   T   |   T   |
|       |       |  |       | T | T |  |       |       |
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       |       |  |       |       |
|   F   |   F   |  |   T   |   F   |  |   T   |   F   |
|       |       |  |       |       |  |       |       |
+-------+-------+  +-------+-------+  +-------+-------+
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;都表示大小为&nbsp;<code>N * N</code>&nbsp;的网格。</li>
	<li><code>N</code>&nbsp;将确保是 2 的整次幂。</li>
	<li>如果你想了解更多关于四叉树的知识，你可以参考这个&nbsp;<a href="https://en.wikipedia.org/wiki/Quadtree">wiki</a>&nbsp;页面。</li>
	<li>逻辑或的定义如下：如果&nbsp;<code>A 为 True</code> ，或者&nbsp;<code>B 为 True</code> ，或者&nbsp;<code>A 和 B 都为 True</code>，则 &quot;A 或 B&quot; 为 True。</li>
</ol>

