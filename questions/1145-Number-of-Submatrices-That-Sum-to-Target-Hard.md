#### 元素和为目标值的子矩阵数量/Number of Submatrices That Sum to Target
**难度：** 困难/Hard

**Question：** 

<p>Given a <code>matrix</code>, and a <code>target</code>, return the number of non-empty submatrices that sum to <font face="monospace">target</font>.</p>

<p>A submatrix <code>x1, y1, x2, y2</code> is the set of all cells <code>matrix[x][y]</code> with <code>x1 &lt;= x &lt;= x2</code> and <code>y1 &lt;= y &lt;= y2</code>.</p>

<p>Two submatrices <code>(x1, y1, x2, y2)</code> and <code>(x1&#39;, y1&#39;, x2&#39;, y2&#39;)</code> are different if they have some coordinate&nbsp;that is different: for example, if <code>x1 != x1&#39;</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>matrix = <span id="example-input-1-1">[[0,1,0],[1,1,1],[0,1,0]]</span>, target = <span id="example-input-1-2">0</span>
<strong>Output: </strong><span id="example-output-1">4</span>
<strong>Explanation: </strong>The four 1x1 submatrices that only contain 0.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>matrix = <span id="example-input-2-1">[[1,-1],[-1,1]]</span>, target = <span id="example-input-2-2">0</span>
<strong>Output: </strong><span id="example-output-2">5</span>
<strong>Explanation: </strong>The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
</pre>
</div>

<p>&nbsp;</p>

<p><strong><strong>Note:</strong></strong></p>

<ol>
	<li><code>1 &lt;= matrix.length &lt;= 300</code></li>
	<li><code>1 &lt;= matrix[0].length &lt;= 300</code></li>
	<li><code>-1000 &lt;= matrix[i] &lt;= 1000</code></li>
	<li><code>-10^8 &lt;= target &lt;= 10^8</code></li>
</ol>


------

**题目：** 
<p>给出矩阵&nbsp;<code>matrix</code>&nbsp;和目标值&nbsp;<code>target</code>，返回元素总和等于目标值的非空子矩阵的数量。</p>

<p>子矩阵&nbsp;<code>x1, y1, x2, y2</code>&nbsp;是满足 <code>x1 &lt;= x &lt;= x2</code>&nbsp;且&nbsp;<code>y1 &lt;= y &lt;= y2</code>&nbsp;的所有单元&nbsp;<code>matrix[x][y]</code>&nbsp;的集合。</p>

<p>如果&nbsp;<code>(x1, y1, x2, y2)</code> 和&nbsp;<code>(x1&#39;, y1&#39;, x2&#39;, y2&#39;)</code>&nbsp;两个子矩阵中部分坐标不同（如：<code>x1 != x1&#39;</code>），那么这两个子矩阵也不同。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
<strong>输出：</strong>4
<strong>解释：</strong>四个只含 0 的 1x1 子矩阵。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>matrix = [[1,-1],[-1,1]], target = 0
<strong>输出：</strong>5
<strong>解释：</strong>两个 1x2 子矩阵，加上两个 2x1 子矩阵，再加上一个 2x2 子矩阵。
</pre>

<p>&nbsp;</p>

<p><strong><strong>提示：</strong></strong></p>

<ol>
	<li><code>1 &lt;= matrix.length &lt;= 300</code></li>
	<li><code>1 &lt;= matrix[0].length &lt;= 300</code></li>
	<li><code>-1000 &lt;= matrix[i] &lt;= 1000</code></li>
	<li><code>-10^8 &lt;= target &lt;= 10^8</code></li>
</ol>

