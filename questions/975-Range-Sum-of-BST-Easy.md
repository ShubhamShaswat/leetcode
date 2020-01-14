#### 二叉搜索树的范围和/Range Sum of BST
**难度：** 简单/Easy

**Question：** 

<p>Given the <code>root</code> node of a binary search tree, return the sum of values of all nodes with value between <code>L</code> and <code>R</code> (inclusive).</p>

<p>The binary search tree is guaranteed to have unique values.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-1-1">[10,5,15,3,7,null,18]</span>, L = <span id="example-input-1-2">7</span>, R = <span id="example-input-1-3">15</span>
<strong>Output: </strong><span id="example-output-1">32</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-2-1">[10,5,15,3,7,13,18,1,null,6]</span>, L = <span id="example-input-2-2">6</span>, R = <span id="example-input-2-3">10</span>
<strong>Output: </strong><span id="example-output-2">23</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>The number of nodes in the tree is at most <code>10000</code>.</li>
	<li>The final answer is guaranteed to be less than <code>2^31</code>.</li>
</ol>
</div>
</div>

------

**题目：** 
<p>给定二叉搜索树的根结点&nbsp;<code>root</code>，返回 <code>L</code> 和 <code>R</code>（含）之间的所有结点的值的和。</p>

<p>二叉搜索树保证具有唯一的值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>root = [10,5,15,3,7,null,18], L = 7, R = 15
<strong>输出：</strong>32
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre><strong>输入：</strong>root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
<strong>输出：</strong>23
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>树中的结点数量最多为&nbsp;<code>10000</code>&nbsp;个。</li>
	<li>最终的答案保证小于&nbsp;<code>2^31</code>。</li>
</ol>

