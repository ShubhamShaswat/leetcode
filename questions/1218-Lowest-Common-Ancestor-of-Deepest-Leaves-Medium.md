#### 最深叶节点的最近公共祖先/Lowest Common Ancestor of Deepest Leaves
**难度：** 中等/Medium

**Question：** 

<p>Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.</p>

<p>Recall that:</p>

<ul>
	<li>The node of a binary tree is a <em>leaf</em> if and only if it has no children</li>
	<li>The <em>depth</em> of the root of the tree is 0, and if the depth of a node is <code>d</code>, the depth of each of its children&nbsp;is&nbsp;<code>d+1</code>.</li>
	<li>The <em>lowest common ancestor</em> of a set <code>S</code> of nodes is the node <code>A</code> with the largest depth such that every node in S is in the subtree with root <code>A</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> root = [1,2,3]
<strong>Output:</strong> [1,2,3]
<strong>Explanation:</strong> 
The deepest leaves are the nodes with values 2 and 3.
The lowest common ancestor of these leaves is the node with value 1.
The answer returned is a TreeNode object (not an array) with serialization &quot;[1,2,3]&quot;.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1,2,3,4]
<strong>Output:</strong> [4]
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [1,2,3,4,5]
<strong>Output:</strong> [2,4,5]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The given tree will have between 1 and 1000 nodes.</li>
	<li>Each node of the tree will have a distinct value between 1 and 1000.</li>
</ul>


------

**题目：** 
<p>给你一个有根节点的二叉树，找到它最深的叶节点的最近公共祖先。</p>

<p>回想一下：</p>

<ul>
	<li><strong>叶节点</strong> 是二叉树中没有子节点的节点</li>
	<li>树的根节点的&nbsp;<strong>深度&nbsp;</strong>为&nbsp;<code>0</code>，如果某一节点的深度为&nbsp;<code>d</code>，那它的子节点的深度就是&nbsp;<code>d+1</code></li>
	<li>如果我们假定 <code>A</code> 是一组节点&nbsp;<code>S</code>&nbsp;的 <strong>最近公共祖先</strong>，<code>S</code>&nbsp;中的每个节点都在以 <code>A</code> 为根节点的子树中，且 <code>A</code>&nbsp;的深度达到此条件下可能的最大值。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>root = [1,2,3]
<strong>输出：</strong>[1,2,3]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>root = [1,2,3,4]
<strong>输出：</strong>[4]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>root = [1,2,3,4,5]
<strong>输出：</strong>[2,4,5]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>给你的树中将有&nbsp;1 到 1000 个节点。</li>
	<li>树中每个节点的值都在 1 到 1000 之间。</li>
</ul>

