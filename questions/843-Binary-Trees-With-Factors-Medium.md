#### 带因子的二叉树/Binary Trees With Factors
**难度：** 中等/Medium

**Question：** 

<p>Given an array of unique integers, each integer is strictly greater than 1.</p>

<p>We make a binary tree using these integers&nbsp;and each number may be used for any number of times.</p>

<p>Each non-leaf node&#39;s&nbsp;value should be equal to the product of the values of it&#39;s children.</p>

<p>How many binary trees can we make?&nbsp; Return the answer <strong>modulo 10 ** 9 + 7</strong>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <code>A = [2, 4]</code>
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can make these trees: <code>[2], [4], [4, 2, 2]</code></pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <code>A = [2, 4, 5, 10]</code>
<strong>Output:</strong> <code>7</code>
<strong>Explanation:</strong> We can make these trees: <code>[2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2]</code>.</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;=&nbsp;1000</code>.</li>
	<li><code>2 &lt;=&nbsp;A[i]&nbsp;&lt;=&nbsp;10 ^ 9</code>.</li>
</ol>


------

**题目：** 
<p>给出一个含有不重复整数元素的数组，每个整数均大于 1。</p>

<p>我们用这些整数来构建二叉树，每个整数可以使用任意次数。</p>

<p>其中：每个非叶结点的值应等于它的两个子结点的值的乘积。</p>

<p>满足条件的二叉树一共有多少个？返回的结果应<strong>模除 10 ** 9 + 7</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> <code>A = [2, 4]</code>
<strong>输出:</strong> 3
<strong>解释:</strong> 我们可以得到这些二叉树: <code>[2], [4], [4, 2, 2]</code></pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> <code>A = [2, 4, 5, 10]</code>
<strong>输出:</strong> <code>7</code>
<strong>解释:</strong> 我们可以得到这些二叉树: <code>[2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2]</code>.</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;=&nbsp;1000.</code></li>
	<li><code>2 &lt;=&nbsp;A[i]&nbsp;&lt;=&nbsp;10 ^ 9</code>.</li>
</ol>

