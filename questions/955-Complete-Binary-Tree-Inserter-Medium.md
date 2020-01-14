#### 完全二叉树插入器/Complete Binary Tree Inserter
**难度：** 中等/Medium

**Question：** 

<p>A <em>complete</em> binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.</p>

<p>Write a data structure&nbsp;<code>CBTInserter</code>&nbsp;that is initialized with a complete binary tree and supports the following operations:</p>

<ul>
	<li><code>CBTInserter(TreeNode root)</code> initializes the data structure on a given tree&nbsp;with head node <code>root</code>;</li>
	<li><code>CBTInserter.insert(int v)</code> will insert a <code>TreeNode</code>&nbsp;into the tree with value <code>node.val =&nbsp;v</code>&nbsp;so that the tree remains complete, <strong>and returns the value of the parent of the inserted <code>TreeNode</code></strong>;</li>
	<li><code>CBTInserter.get_root()</code> will return the head node of the tree.</li>
</ul>

<ol>
</ol>

<div>
<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>inputs = <span id="example-input-1-1">[&quot;CBTInserter&quot;,&quot;insert&quot;,&quot;get_root&quot;]</span>, inputs = <span id="example-input-1-2">[[[1]],[2],[]]</span>
<strong>Output: </strong><span id="example-output-1">[null,1,[1,2]]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>inputs = <span id="example-input-2-1">[&quot;CBTInserter&quot;,&quot;insert&quot;,&quot;insert&quot;,&quot;get_root&quot;]</span>, inputs = <span id="example-input-2-2">[[[1,2,3,4,5,6]],[7],[8],[]]</span>
<strong>Output: </strong><span id="example-output-2">[null,3,4,[1,2,3,4,5,6,7,8]]</span></pre>
</div>

<div>
<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>The initial given tree is complete and contains between <code>1</code> and <code>1000</code> nodes.</li>
	<li><code>CBTInserter.insert</code> is called at most <code>10000</code> times per test case.</li>
	<li>Every value of a given or inserted node is between <code>0</code> and <code>5000</code>.</li>
</ol>
</div>
</div>

<div>
<p>&nbsp;</p>

<div>&nbsp;</div>
</div>


------

**题目：** 
<p>完全二叉树是每一层（除最后一层外）都是完全填充（即，结点数达到最大）的，并且所有的结点都尽可能地集中在左侧。</p>

<p>设计一个用完全二叉树初始化的数据结构&nbsp;<code>CBTInserter</code>，它支持以下几种操作：</p>

<ul>
	<li><code>CBTInserter(TreeNode root)</code>&nbsp;使用头结点为&nbsp;<code>root</code>&nbsp;的给定树初始化该数据结构；</li>
	<li><code>CBTInserter.insert(int v)</code> 将&nbsp;<code>TreeNode</code>&nbsp;插入到存在值为&nbsp;<code>node.val =&nbsp;v</code>&nbsp; 的树中以使其保持完全二叉树的状态，<strong>并返回插入的 <code>TreeNode</code>&nbsp;的父结点的值</strong>；</li>
	<li><code>CBTInserter.get_root()</code> 将返回树的头结点。</li>
</ul>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>inputs = [&quot;CBTInserter&quot;,&quot;insert&quot;,&quot;get_root&quot;], inputs = [[[1]],[2],[]]
<strong>输出：</strong>[null,1,[1,2]]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>inputs = [&quot;CBTInserter&quot;,&quot;insert&quot;,&quot;insert&quot;,&quot;get_root&quot;], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
<strong>输出：</strong>[null,3,4,[1,2,3,4,5,6,7,8]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>最初给定的树是完全二叉树，且包含&nbsp;<code>1</code>&nbsp;到&nbsp;<code>1000</code>&nbsp;个结点。</li>
	<li>每个测试用例最多调用&nbsp;<code>CBTInserter.insert</code>&nbsp; 操作&nbsp;<code>10000</code>&nbsp;次。</li>
	<li>给定结点或插入结点的每个值都在&nbsp;<code>0</code>&nbsp;到&nbsp;<code>5000</code>&nbsp;之间。</li>
</ol>

