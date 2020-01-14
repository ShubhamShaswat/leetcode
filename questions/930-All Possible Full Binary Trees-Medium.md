#### 所有可能的满二叉树/All Possible Full Binary Trees
**难度：** 中等/Medium

**Question：** 

<p>A <em>full binary tree</em>&nbsp;is a binary tree where each node has exactly 0 or 2&nbsp;children.</p>

<p>Return a list of all possible full binary trees with <code>N</code> nodes.&nbsp; Each element of the answer is the root node of one possible tree.</p>

<p>Each <code>node</code> of each&nbsp;tree in the answer <strong>must</strong> have <code>node.val = 0</code>.</p>

<p>You may return the final list of trees in any order.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">7</span>
<strong>Output: </strong><span id="example-output-1">[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]</span>
<strong>Explanation:</strong>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/22/fivetrees.png" style="width: 700px; height: 400px;" />
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>1 &lt;= N &lt;= 20</code></li>
</ul>


------

**题目：** 
<p><em>满二叉树</em>是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。</p>

<p>返回包含 <code>N</code> 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。</p>

<p>答案中每个树的每个<code>结点</code>都<strong>必须</strong>有 <code>node.val=0</code>。</p>

<p>你可以按任何顺序返回树的最终列表。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>7
<strong>输出：</strong>[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
<strong>解释：</strong>
<img alt="" src="https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/08/24/fivetrees.png" style="height: 400px; width: 700px;">
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= N &lt;= 20</code></li>
</ul>

