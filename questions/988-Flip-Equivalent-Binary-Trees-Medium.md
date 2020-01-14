#### 翻转等价二叉树/Flip Equivalent Binary Trees
**难度：** 中等/Medium

**Question：** 

<p>For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.</p>

<p>A binary tree X&nbsp;is <em>flip equivalent</em> to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.</p>

<p>Write a function that determines whether two binary trees&nbsp;are <em>flip equivalent</em>.&nbsp; The trees are given by root nodes <code>root1</code> and <code>root2</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>root1 = <span id="example-input-1-1">[1,2,3,4,5,6,null,null,null,7,8]</span>, root2 = <span id="example-input-1-2">[1,3,2,null,6,4,5,null,null,null,null,8,7]</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation: </strong>We flipped at nodes with values 1, 3, and 5.
<img alt="Flipped Trees Diagram" src="https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png" style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;; width: 455px; height: 200px;" />
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>Each tree will have at most <code>100</code> nodes.</li>
	<li>Each value in each tree will be a unique&nbsp;integer in the range <code>[0, 99]</code>.</li>
</ol>

<div>
<p>&nbsp;</p>
</div>


------

**题目：** 
<p>我们可以为二叉树 T 定义一个翻转操作，如下所示：选择任意节点，然后交换它的左子树和右子树。</p>

<p>只要经过一定次数的翻转操作后，能使 X 等于 Y，我们就称二叉树 X <em>翻转等价</em>于二叉树 Y。</p>

<p>编写一个判断两个二叉树是否是<em>翻转等价</em>的函数。这些树由根节点&nbsp;<code>root1</code> 和 <code>root2</code>&nbsp;给出。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
<strong>输出：</strong>true
<strong>解释：</strong>We flipped at nodes with values 1, 3, and 5.
<img alt="Flipped Trees Diagram" src="https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png" style="">
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>每棵树最多有&nbsp;<code>100</code>&nbsp;个节点。</li>
	<li>每棵树中的每个值都是唯一的、在 <code>[0, 99]</code>&nbsp;范围内的整数。</li>
</ol>

<p>&nbsp;</p>

