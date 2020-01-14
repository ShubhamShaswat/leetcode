#### 翻转二叉树以匹配先序遍历/Flip Binary Tree To Match Preorder Traversal
**难度：** 中等/Medium

**Question：** 

<p>Given a binary tree with <code>N</code> nodes, each node has a different value from&nbsp;<code>{1, ..., N}</code>.</p>

<p>A node in this binary tree can be <em>flipped</em>&nbsp;by swapping the left child and the right child of that node.</p>

<p>Consider the sequence of&nbsp;<code>N</code> values reported by a preorder traversal starting from the root.&nbsp; Call such a sequence of <code>N</code> values the&nbsp;<em>voyage</em>&nbsp;of the tree.</p>

<p>(Recall that a <em>preorder traversal</em>&nbsp;of a node means we report the current node&#39;s value, then preorder-traverse the left child, then preorder-traverse the right child.)</p>

<p>Our goal is to flip the <strong>least number</strong> of nodes in the tree so that the voyage of the tree matches the <code>voyage</code> we are given.</p>

<p>If we can do so, then return a&nbsp;list&nbsp;of the values of all nodes flipped.&nbsp; You may return the answer in any order.</p>

<p>If we cannot do so, then return the list <code>[-1]</code>.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/01/02/1219-01.png" style="width: 88px; height: 120px;" /></strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-1-1">[1,2]</span>, voyage = <span id="example-input-1-2">[2,1]</span>
<strong>Output: </strong><span id="example-output-1">[-1]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/01/02/1219-02.png" style="width: 127px; height: 120px;" /></strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-2-1">[1,2,3]</span>, voyage = <span id="example-input-2-2">[1,3,2]</span>
<strong>Output: </strong><span id="example-output-2">[1]</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/01/02/1219-02.png" style="width: 127px; height: 120px;" /></strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-3-1">[1,2,3]</span>, voyage = <span id="example-input-3-2">[1,2,3]</span>
<strong>Output: </strong><span id="example-output-3">[]</span>
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 100</code></li>
</ol>
</div>
</div>
</div>


------

**题目：** 
<p>给定一个有 <code>N</code> 个节点的二叉树，每个节点都有一个不同于其他节点且处于 <code>{1, ..., N}</code> 中的值。</p>

<p>通过交换节点的左子节点和右子节点，可以翻转该二叉树中的节点。</p>

<p>考虑从根节点开始的先序遍历报告的 <code>N</code> 值序列。将这一 <code>N</code> 值序列称为树的行程。</p>

<p>（回想一下，节点的先序遍历意味着我们报告当前节点的值，然后先序遍历左子节点，再先序遍历右子节点。）</p>

<p>我们的目标是翻转<strong>最少的</strong>树中节点，以便树的行程与给定的行程&nbsp;<code>voyage</code>&nbsp;相匹配。&nbsp;</p>

<p>如果可以，则返回翻转的所有节点的值的列表。你可以按任何顺序返回答案。</p>

<p>如果不能，则返回列表 <code>[-1]</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/01/05/1219-01.png" style="height: 120px; width: 88px;"></strong></p>

<pre><strong>输入：</strong>root = [1,2], voyage = [2,1]
<strong>输出：</strong>[-1]
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/01/05/1219-02.png" style="height: 120px; width: 127px;"></strong></p>

<pre><strong>输入：</strong>root = [1,2,3], voyage = [1,3,2]
<strong>输出：</strong>[1]
</pre>

<p><strong>示例 3：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/01/05/1219-02.png" style="height: 120px; width: 127px;"></strong></p>

<pre><strong>输入：</strong>root = [1,2,3], voyage = [1,2,3]
<strong>输出：</strong>[]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 100</code></li>
</ol>

