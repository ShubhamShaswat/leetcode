#### 二叉树的完全性检验/Check Completeness of a Binary Tree
**难度：** 中等/Medium

**Question：** 

<p>Given a binary tree, determine if it is a <em>complete binary tree</em>.</p>

<p><u><b>Definition of a complete binary tree from <a href="http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees" target="_blank">Wikipedia</a>:</b></u><br />
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2<sup>h</sup> nodes inclusive at the last level h.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-1.png" style="width: 180px; height: 145px;" /></strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,3,4,5,6]</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<span><strong>Explanation: </strong></span>Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-2.png" style="width: 200px; height: 145px;" /></strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,2,3,4,5,null,7]</span>
<strong>Output: </strong><span id="example-output-2">false</span>
<strong>Explanation: </strong>The node with value 7 isn&#39;t as far left as possible.<span>
</span></pre>

<div>&nbsp;</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li>The tree will have between 1 and 100 nodes.</li>
</ol>


------

**题目：** 
<p>给定一个二叉树，确定它是否是一个<em>完全二叉树</em>。</p>

<p><strong><a href="https://baike.baidu.com/item/完全二叉树/7773232?fr=aladdin" target="_blank">百度百科</a>中对完全二叉树的定义如下：</strong></p>

<p>若设二叉树的深度为 h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。（注：第 h 层可能包含 1~&nbsp;2<sup>h</sup>&nbsp;个节点。）</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/complete-binary-tree-1.png" style="height: 145px; width: 180px;"></p>

<pre><strong>输入：</strong>[1,2,3,4,5,6]
<strong>输出：</strong>true
<strong>解释：</strong>最后一层前的每一层都是满的（即，结点值为 {1} 和 {2,3} 的两层），且最后一层中的所有结点（{4,5,6}）都尽可能地向左。
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/complete-binary-tree-2.png"></strong></p>

<pre><strong>输入：</strong>[1,2,3,4,5,null,7]
<strong>输出：</strong>false
<strong>解释：</strong>值为 7 的结点没有尽可能靠向左侧。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>树中将会有 1 到 100 个结点。</li>
</ol>

