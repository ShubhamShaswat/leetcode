#### 节点与其祖先之间的最大差值/Maximum Difference Between Node and Ancestor
**难度：** 中等/Medium

**Question：** 

<p>Given the <code>root</code> of a binary tree, find the maximum value <code>V</code> for which there exists <strong>different</strong> nodes <code>A</code> and <code>B</code> where <code>V = |A.val - B.val|</code>&nbsp;and <code>A</code> is an ancestor of <code>B</code>.</p>

<p>(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/09/09/2whqcep.jpg" style="height: 230px; width: 300px;" /></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[8,3,10,1,6,null,14,null,null,4,7,13]</span>
<strong>Output: </strong><span id="example-output-1">7</span>
<strong>Explanation: </strong>
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>The number of nodes in the tree is between <code>2</code> and <code>5000</code>.</li>
	<li>Each node will have value between <code>0</code> and <code>100000</code>.</li>
</ol>


------

**题目：** 
<p>给定二叉树的根节点&nbsp;<code>root</code>，找出存在于不同节点&nbsp;<code>A</code> 和&nbsp;<code>B</code>&nbsp;之间的最大值 <code>V</code>，其中&nbsp;<code>V = |A.val - B.val|</code>，且&nbsp;<code>A</code>&nbsp;是&nbsp;<code>B</code>&nbsp;的祖先。</p>

<p>（如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/04/12/2whqcep.jpg" style="height: 230px; width: 300px;"></p>

<pre><strong>输入：</strong>[8,3,10,1,6,null,14,null,null,4,7,13]
<strong>输出：</strong>7
<strong>解释： </strong>
我们有大量的节点与其祖先的差值，其中一些如下：
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
在所有可能的差值中，最大值 7 由 |8 - 1| = 7 得出。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>树中的节点数在&nbsp;<code>2</code>&nbsp;到&nbsp;<code>5000</code>&nbsp;之间。</li>
	<li>每个节点的值介于&nbsp;<code>0</code>&nbsp;到&nbsp;<code>100000</code>&nbsp;之间。</li>
</ol>

