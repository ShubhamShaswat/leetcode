#### 重构 2 行二进制矩阵/Reconstruct a 2-Row Binary Matrix
**难度：** 中等/Medium

**Question：** 

<p>Given the following details of a matrix with <code>n</code> columns and <code>2</code> rows :</p>

<ul>
	<li>The matrix is a binary matrix, which means each element in the matrix can be <code>0</code> or <code>1</code>.</li>
	<li>The sum of elements of the 0-th(upper) row is given as <code>upper</code>.</li>
	<li>The sum of elements of the 1-st(lower) row is given as <code>lower</code>.</li>
	<li>The sum of elements in the i-th column(0-indexed) is <code>colsum[i]</code>, where <code>colsum</code> is given as an integer array with length <code>n</code>.</li>
</ul>

<p>Your task is to reconstruct the matrix with <code>upper</code>, <code>lower</code> and <code>colsum</code>.</p>

<p>Return it as a 2-D integer array.</p>

<p>If there are more than one valid solution, any of them will be accepted.</p>

<p>If no valid solution exists, return an empty 2-D array.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> upper = 2, lower = 1, colsum = [1,1,1]
<strong>Output:</strong> [[1,1,0],[0,0,1]]
<strong>Explanation: </strong>[[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> upper = 2, lower = 3, colsum = [2,2,1,1]
<strong>Output:</strong> []
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
<strong>Output:</strong> [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= colsum.length &lt;= 10^5</code></li>
	<li><code>0 &lt;= upper, lower &lt;= colsum.length</code></li>
	<li><code>0 &lt;= colsum[i] &lt;= 2</code></li>
</ul>


------

**题目：** 
<p>给你一个&nbsp;<code>2</code>&nbsp;行 <code>n</code> 列的二进制数组：</p>

<ul>
	<li>矩阵是一个二进制矩阵，这意味着矩阵中的每个元素不是&nbsp;<code>0</code>&nbsp;就是&nbsp;<code>1</code>。</li>
	<li>第 <code>0</code> 行的元素之和为&nbsp;<code>upper</code>。</li>
	<li>第 <code>1</code> 行的元素之和为 <code>lower</code>。</li>
	<li>第 <code>i</code> 列（从 <code>0</code> 开始编号）的元素之和为&nbsp;<code>colsum[i]</code>，<code>colsum</code>&nbsp;是一个长度为&nbsp;<code>n</code>&nbsp;的整数数组。</li>
</ul>

<p>你需要利用&nbsp;<code>upper</code>，<code>lower</code>&nbsp;和&nbsp;<code>colsum</code>&nbsp;来重构这个矩阵，并以二维整数数组的形式返回它。</p>

<p>如果有多个不同的答案，那么任意一个都可以通过本题。</p>

<p>如果不存在符合要求的答案，就请返回一个空的二维数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>upper = 2, lower = 1, colsum = [1,1,1]
<strong>输出：</strong>[[1,1,0],[0,0,1]]
<strong>解释：</strong>[[1,0,1],[0,1,0]] 和 [[0,1,1],[1,0,0]] 也是正确答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>upper = 2, lower = 3, colsum = [2,2,1,1]
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
<strong>输出：</strong>[[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= colsum.length &lt;= 10^5</code></li>
	<li><code>0 &lt;= upper, lower &lt;= colsum.length</code></li>
	<li><code>0 &lt;= colsum[i] &lt;= 2</code></li>
</ul>

