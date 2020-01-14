#### 最佳观光组合/Best Sightseeing Pair
**难度：** 中等/Medium

**Question：** 

<p>Given an array <code>A</code> of positive integers, <code>A[i]</code> represents the value of the <code>i</code>-th sightseeing spot, and two&nbsp;sightseeing spots <code>i</code> and <code>j</code>&nbsp;have distance <code>j - i</code>&nbsp;between them.</p>

<p>The <em>score</em>&nbsp;of a pair (<code>i &lt; j</code>) of sightseeing spots is (<code>A[i] + A[j] + i&nbsp;- j)</code> : the sum of the values of the sightseeing spots, <strong>minus</strong> the distance between them.</p>

<p>Return the maximum score of a pair of sightseeing spots.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[8,1,5,2,6]</span>
<strong>Output: </strong><span id="example-output-1">11
<strong>Explanation:</strong> i = 0, j = 2, </span><code>A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11</code>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>2 &lt;= A.length &lt;= 50000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 1000</code></li>
</ol>

------

**题目：** 
<p>给定正整数数组&nbsp;<code>A</code>，<code>A[i]</code>&nbsp;表示第 <code>i</code> 个观光景点的评分，并且两个景点&nbsp;<code>i</code> 和&nbsp;<code>j</code>&nbsp;之间的距离为&nbsp;<code>j - i</code>。</p>

<p>一对景点（<code>i &lt; j</code>）组成的观光组合的得分为（<code>A[i] + A[j] + i&nbsp;- j</code>）：景点的评分之和<strong>减去</strong>它们两者之间的距离。</p>

<p>返回一对观光景点能取得的最高分。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>[8,1,5,2,6]
<strong>输出：</strong>11
<strong>解释：</strong>i = 0, j = 2, <code>A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11</code>
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>2 &lt;= A.length &lt;= 50000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 1000</code></li>
</ol>

