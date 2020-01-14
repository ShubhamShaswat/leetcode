#### 建立四叉树/Construct Quad Tree
**难度：** 中等/Medium

**Question：** 

<p>We want to use quad trees to store an <code>N x N</code> boolean grid. Each cell in the grid can only be true or false. The root node represents the whole grid. For each node, it will be subdivided into four children nodes <strong>until the values in the region it represents are all the same</strong>.</p>

<p>Each node has another two boolean attributes : <code>isLeaf</code> and <code>val</code>. <code>isLeaf</code> is true if and only if the node is a leaf node. The <code>val</code> attribute for a leaf node contains the value of the region it represents.</p>

<p>Your task is to use a quad tree to represent a given grid. The following example may help you understand the problem better:</p>

<p>Given the <code>8 x 8</code> grid below, we want to construct the corresponding quad tree:</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/01/962_grid.png" style="height:27%; max-height:300px; max-width:299px; width:27%" /></p>

<p>It can be divided according to the definition above:</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/01/962_grid_divided.png" style="height:100%; max-height:300px; max-width:1107px; width:100%" /></p>

<p>&nbsp;</p>

<p>The corresponding quad tree should be as following, where each node is represented as a <code>(isLeaf, val)</code> pair.</p>

<p>For the non-leaf&nbsp;nodes,&nbsp;<code>val</code> can be arbitrary, so it is represented as <code>*</code>.</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/01/962_quad_tree.png" style="height:100%; max-height:300px; max-width:836px; width:100%" /></p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>N</code> is less than <code>1000</code> and guaranteened to be a power of 2.</li>
	<li>If you want to know more about the quad tree, you can refer to its <a href="https://en.wikipedia.org/wiki/Quadtree">wiki</a>.</li>
</ol>


------

**题目：** 
<p>我们想要使用一棵四叉树来储存一个&nbsp;<code>N x N</code> 的布尔值网络。网络中每一格的值只会是真或假。树的根结点代表整个网络。对于每个结点, 它将被分等成四个孩子结点<strong>直到这个区域内的值都是相同的.</strong></p>

<p>每个结点还有另外两个布尔变量:&nbsp;<code>isLeaf</code> 和&nbsp;<code>val</code>。<code>isLeaf</code> 当这个节点是一个叶子结点时为真。<code>val</code>&nbsp;变量储存叶子结点所代表的区域的值。</p>

<p>你的任务是使用一个四叉树表示给定的网络。下面的例子将有助于你理解这个问题：</p>

<p>给定下面这个<code>8 x 8</code>&nbsp;网络，我们将这样建立一个对应的四叉树：</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/01/962_grid.png" style="height:27%; width:27%" /></p>

<p>由上文的定义，它能被这样分割：</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/01/962_grid_divided.png" style="height:100%; width:100%" /></p>

<p>&nbsp;</p>

<p>对应的四叉树应该像下面这样，每个结点由一对&nbsp;<code>(isLeaf, val)</code>&nbsp;所代表.</p>

<p>对于非叶子结点，<code>val</code>&nbsp;可以是任意的，所以使用&nbsp;<code>*</code>&nbsp;代替。</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/01/962_quad_tree.png" style="height:100%; width:100%" /></p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>N</code>&nbsp;将小于&nbsp;<code>1000</code>&nbsp;且确保是 2 的整次幂。</li>
	<li>如果你想了解更多关于四叉树的知识，你可以参考这个&nbsp;<a href="https://en.wikipedia.org/wiki/Quadtree">wiki</a>&nbsp;页面。</li>
</ol>

