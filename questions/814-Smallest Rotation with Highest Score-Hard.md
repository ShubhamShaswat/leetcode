#### 得分最高的最小轮调/Smallest Rotation with Highest Score
**难度：** 困难/Hard

**Question：** 

<p>&nbsp;Given an array <code>A</code>, we may rotate it by a non-negative integer <code>K</code> so that the array becomes <code>A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1]</code>.&nbsp; Afterward, any entries that are less than or equal to their index are worth 1 point.&nbsp;</p>

<p>For example, if we have <code>[2, 4, 1, 3, 0]</code>, and we rotate by <code>K = 2</code>, it becomes <code>[1, 3, 0, 2, 4]</code>.&nbsp; This is worth 3 points because 1 &gt; 0 [no points], 3 &gt; 1 [no points], 0 &lt;= 2 [one point], 2 &lt;= 3 [one point], 4 &lt;= 4 [one point].</p>

<p>Over all possible rotations, return the rotation index K that corresponds to the highest score we could receive.&nbsp; If there are multiple answers, return the smallest such index K.</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> [2, 3, 1, 4, 0]
<strong>Output:</strong> 3
<strong>Explanation: </strong> 
Scores for each K are listed below: 
K = 0,  A = [2,3,1,4,0],    score 2
K = 1,  A = [3,1,4,0,2],    score 3
K = 2,  A = [1,4,0,2,3],    score 3
K = 3,  A = [4,0,2,3,1],    score 4
K = 4,  A = [0,2,3,1,4],    score 3
</pre>

<p>So we should choose K = 3, which has the highest score.</p>

<p>&nbsp;</p>

<pre>
<strong>Example 2:</strong>
<strong>Input:</strong> [1, 3, 0, 2, 4]
<strong>Output:</strong> 0
<strong>Explanation: </strong> A will always have 3 points no matter how it shifts.
So we will choose the smallest K, which is 0.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>A</code>&nbsp;will have&nbsp;length at most <code>20000</code>.</li>
	<li><code>A[i]</code> will be in the range <code>[0, A.length]</code>.</li>
</ul>


------

**题目：** 
<p>给定一个数组&nbsp;<code>A</code>，我们可以将它按一个非负整数 <code>K</code>&nbsp;进行轮调，这样可以使数组变为&nbsp;<code>A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1]</code>&nbsp;的形式。此后，任何值小于或等于其索引的项都可以记作一分。</p>

<p>例如，如果数组为&nbsp;<code>[2, 4, 1, 3, 0]</code>，我们按&nbsp;<code>K = 2</code>&nbsp;进行轮调后，它将变成&nbsp;<code>[1, 3, 0, 2, 4]</code>。这将记作 3 分，因为 1 &gt; 0 [no points], 3 &gt; 1 [no points], 0 &lt;= 2 [one point], 2 &lt;= 3 [one point], 4 &lt;= 4 [one point]。</p>

<p>在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调索引 K。如果有多个答案，返回满足条件的最小的索引 K。</p>

<pre><strong>示例 1：</strong>
<strong>输入：</strong>[2, 3, 1, 4, 0]
<strong>输出：</strong>3
<strong>解释：</strong>
下面列出了每个 K 的得分：
K = 0,  A = [2,3,1,4,0],    score 2
K = 1,  A = [3,1,4,0,2],    score 3
K = 2,  A = [1,4,0,2,3],    score 3
K = 3,  A = [4,0,2,3,1],    score 4
K = 4,  A = [0,2,3,1,4],    score 3
所以我们应当选择&nbsp;K = 3，得分最高。</pre>

<p>&nbsp;</p>

<pre><strong>示例 2：</strong>
<strong>输入：</strong>[1, 3, 0, 2, 4]
<strong>输出：</strong>0
<strong>解释：</strong>
A 无论怎么变化总是有 3 分。
所以我们将选择最小的 K，即 0。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>A</code>&nbsp;的长度最大为&nbsp;<code>20000</code>。</li>
	<li><code>A[i]</code> 的取值范围是&nbsp;<code>[0, A.length]</code>。</li>
</ul>

