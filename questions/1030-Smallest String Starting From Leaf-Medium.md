#### 从叶结点开始的最小字符串/Smallest String Starting From Leaf
**难度：** 中等/Medium

**Question：** 

<p>Given the <code>root</code> of a binary tree, each node has a value from <code>0</code> to <code>25</code> representing the letters <code>&#39;a&#39;</code> to <code>&#39;z&#39;</code>: a value of <code>0</code> represents <code>&#39;a&#39;</code>, a value of <code>1</code> represents <code>&#39;b&#39;</code>, and so on.</p>

<p>Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.</p>

<p><em>(As a reminder, any shorter prefix of a string is lexicographically smaller: for example, <code>&quot;ab&quot;</code> is lexicographically smaller than <code>&quot;aba&quot;</code>.&nbsp; A leaf of a node is a node that has no children.)</em></p>

<div>
<div>
<p>&nbsp;</p>

<ol>
</ol>
</div>
</div>

<div>
<p><strong>Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/01/30/tree1.png" style="width: 160px; height: 107px;" /></strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[0,1,2,3,4,3,4]</span>
<strong>Output: </strong><span id="example-output-1">&quot;dba&quot;</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/01/30/tree2.png" style="width: 160px; height: 107px;" /></strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[25,1,3,1,3,0,2]</span>
<strong>Output: </strong><span id="example-output-2">&quot;adz&quot;</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/02/01/tree3.png" style="height: 170px; width: 172px;" /></strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[2,2,1,null,1,0,null,0]</span>
<strong>Output: </strong><span id="example-output-3">&quot;abc&quot;</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>The number of nodes in the given tree will be between <code>1</code> and <code>8500</code>.</li>
	<li>Each node in the tree will have a value between <code>0</code> and <code>25</code>.</li>
</ol>
</div>
</div>
</div>

------

**题目：** 
<p>给定一颗根结点为&nbsp;<code>root</code>&nbsp;的二叉树，书中的每个结点都有一个从&nbsp;<code>0</code> 到&nbsp;<code>25</code>&nbsp;的值，分别代表字母&nbsp;<code>&#39;a&#39;</code> 到&nbsp;<code>&#39;z&#39;</code>：值&nbsp;<code>0</code> 代表&nbsp;<code>&#39;a&#39;</code>，值&nbsp;<code>1</code>&nbsp;代表&nbsp;<code>&#39;b&#39;</code>，依此类推。</p>

<p>找出按字典序最小的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束。</p>

<p><em>（小贴士：字符串中任何较短的前缀在字典序上都是较小的：例如，在字典序上&nbsp;<code>&quot;ab&quot;</code> 比&nbsp;<code>&quot;aba&quot;</code>&nbsp;要小。叶结点是指没有子结点的结点。）</em></p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/02/tree1.png" style="height: 107px; width: 160px;"></strong></p>

<pre><strong>输入：</strong>[0,1,2,3,4,3,4]
<strong>输出：</strong>&quot;dba&quot;
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/02/tree2.png" style="height: 107px; width: 160px;"></strong></p>

<pre><strong>输入：</strong>[25,1,3,1,3,0,2]
<strong>输出：</strong>&quot;adz&quot;
</pre>

<p><strong>示例 3：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/02/tree3.png" style="height: 180px; width: 172px;"></strong></p>

<pre><strong>输入：</strong>[2,2,1,null,1,0,null,0]
<strong>输出：</strong>&quot;abc&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>给定树的结点数介于&nbsp;<code>1</code> 和&nbsp;<code>8500</code>&nbsp;之间。</li>
	<li>树中的每个结点都有一个介于&nbsp;<code>0</code>&nbsp;和&nbsp;<code>25</code>&nbsp;之间的值。</li>
</ol>

