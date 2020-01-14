#### 最短的桥/Shortest Bridge
**难度：** 中等/Medium

**Question：** 

<p>In a given 2D binary array <code>A</code>, there are two islands.&nbsp; (An island is a 4-directionally connected group of&nbsp;<code>1</code>s not connected to any other 1s.)</p>

<p>Now, we may change <code>0</code>s to <code>1</code>s so as to connect the two islands together to form 1 island.</p>

<p>Return the smallest number of <code>0</code>s that must be flipped.&nbsp; (It is guaranteed that the answer is at least 1.)</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[0,1],[1,0]]</span>
<strong>Output: </strong>1
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[[0,1,0],[0,0,0],[0,0,1]]</span>
<strong>Output: </strong>2
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]</span>
<strong>Output: </strong><span id="example-output-3">1</span></pre>

<p>&nbsp;</p>
</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length =&nbsp;A[0].length &lt;= 100</code></li>
	<li><code>A[i][j] == 0</code> or <code>A[i][j] == 1</code></li>
</ol>

<div>
<div>
<div>&nbsp;</div>
</div>
</div>

------

**题目：** 
<p>在给定的二维二进制数组&nbsp;<code>A</code>&nbsp;中，存在两座岛。（岛是由四面相连的 <code>1</code> 形成的一个最大组。）</p>

<p>现在，我们可以将&nbsp;<code>0</code>&nbsp;变为&nbsp;<code>1</code>，以使两座岛连接起来，变成一座岛。</p>

<p>返回必须翻转的&nbsp;<code>0</code> 的最小数目。（可以保证答案至少是 1。）</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[[0,1],[1,0]]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[[0,1,0],[0,0,0],[0,0,1]]
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
<strong>输出：</strong>1</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length =&nbsp;A[0].length &lt;= 100</code></li>
	<li><code>A[i][j] == 0</code> 或&nbsp;<code>A[i][j] == 1</code></li>
</ol>

<p>&nbsp;</p>

