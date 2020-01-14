#### 按列翻转得到最大值等行数/Flip Columns For Maximum Number of Equal Rows
**难度：** 中等/Medium

**Question：** 

<p>Given a <code>matrix</code> consisting of 0s and 1s, we may choose any number of columns in the matrix and flip <strong>every</strong>&nbsp;cell in that column.&nbsp; Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.</p>

<p>Return the maximum number of rows that have all values equal after some number of flips.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[0,1],[1,1]]</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong>After flipping no values, 1 row has all values equal.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[[0,1],[1,0]]</span>
<strong>Output: </strong><span id="example-output-2">2</span>
<strong>Explanation: </strong>After flipping values in the first column, both rows have equal values.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[[0,0,0],[0,0,1],[1,1,0]]</span>
<strong>Output: </strong><span id="example-output-3">2</span>
<strong>Explanation: </strong>After flipping values in the first two columns, the last two rows have equal values.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= matrix.length &lt;= 300</code></li>
	<li><code>1 &lt;= matrix[i].length &lt;= 300</code></li>
	<li>All <code>matrix[i].length</code>&#39;s are equal</li>
	<li><code>matrix[i][j]</code> is&nbsp;<code>0</code> or <code>1</code></li>
</ol>
</div>
</div>
</div>


------

**题目：** 
<p>给定由若干 0 和 1 组成的矩阵&nbsp;<code>matrix</code>，从中选出任意数量的列并翻转其上的&nbsp;<strong>每个&nbsp;</strong>单元格。翻转后，单元格的值从 0 变成 1，或者从 1 变为 0 。</p>

<p>返回经过一些翻转后，行上所有值都相等的最大行数。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[[0,1],[1,1]]
<strong>输出：</strong>1
<strong>解释：</strong>不进行翻转，有 1 行所有值都相等。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[[0,1],[1,0]]
<strong>输出：</strong>2
<strong>解释：</strong>翻转第一列的值之后，这两行都由相等的值组成。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[[0,0,0],[0,0,1],[1,1,0]]
<strong>输出：</strong>2
<strong>解释：</strong>翻转前两列的值之后，后两行由相等的值组成。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= matrix.length &lt;= 300</code></li>
	<li><code>1 &lt;= matrix[i].length &lt;= 300</code></li>
	<li>所有 <code>matrix[i].length</code>&nbsp;都相等</li>
	<li><code>matrix[i][j]</code> 为&nbsp;<code>0</code> 或&nbsp;<code>1</code></li>
</ol>

