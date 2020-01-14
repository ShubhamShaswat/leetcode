#### 合并石头的最低成本/Minimum Cost to Merge Stones
**难度：** 困难/Hard

**Question：** 

<p>There are <code>N</code> piles of stones arranged in a row.&nbsp; The <code>i</code>-th pile has <code>stones[i]</code> stones.</p>

<p>A <em>move</em> consists of merging <strong>exactly&nbsp;<code>K</code>&nbsp;consecutive</strong> piles into one pile, and the cost of this move is equal to the total number of stones in these <code>K</code> piles.</p>

<p>Find the minimum cost to merge all piles of stones into one pile.&nbsp; If it is impossible, return <code>-1</code>.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>stones = <span id="example-input-1-1">[3,2,4,1]</span>, K = <span id="example-input-1-2">2</span>
<strong>Output: </strong><span id="example-output-1">20</span>
<strong>Explanation: </strong>
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>stones = <span id="example-input-2-1">[3,2,4,1]</span>, K = <span id="example-input-2-2">3</span>
<strong>Output: </strong><span id="example-output-2">-1</span>
<strong>Explanation: </strong>After any merge operation, there are 2 piles left, and we can&#39;t merge anymore.  So the task is impossible.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>stones = <span id="example-input-3-1">[3,5,1,2,6]</span>, K = <span id="example-input-3-2">3</span>
<strong>Output: </strong><span id="example-output-3">25</span>
<strong>Explanation: </strong>
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ul>
	<li><code><span>1 &lt;= stones.length &lt;= 30</span></code></li>
	<li><code><span>2 &lt;= K &lt;= 30</span></code></li>
	<li><code><span>1 &lt;= stones[i] &lt;= 100</span></code></li>
</ul>
</div>
</div>
</div>

------

**题目：** 
<p>有 <code>N</code> 堆石头排成一排，第 <code>i</code> 堆中有&nbsp;<code>stones[i]</code>&nbsp;块石头。</p>

<p>每次<em>移动（move）</em>需要将<strong>连续的</strong>&nbsp;<code>K</code>&nbsp;堆石头合并为一堆，而这个移动的成本为这&nbsp;<code>K</code>&nbsp;堆石头的总数。</p>

<p>找出把所有石头合并成一堆的最低成本。如果不可能，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>stones = [3,2,4,1], K = 2
<strong>输出：</strong>20
<strong>解释：</strong>
从 [3, 2, 4, 1] 开始。
合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
合并 [4, 1]，成本为 5，剩下 [5, 5]。
合并 [5, 5]，成本为 10，剩下 [10]。
总成本 20，这是可能的最小值。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>stones = [3,2,4,1], K = 3
<strong>输出：</strong>-1
<strong>解释：</strong>任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。.
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>stones = [3,5,1,2,6], K = 3
<strong>输出：</strong>25
<strong>解释：</strong>
从 [3, 5, 1, 2, 6] 开始。
合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
合并 [3, 8, 6]，成本为 17，剩下 [17]。
总成本 25，这是可能的最小值。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= stones.length &lt;= 30</code></li>
	<li><code>2 &lt;= K &lt;= 30</code></li>
	<li><code>1 &lt;= stones[i] &lt;= 100</code></li>
</ul>

