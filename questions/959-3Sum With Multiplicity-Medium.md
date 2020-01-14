#### 三数之和的多种可能/3Sum With Multiplicity
**难度：** 中等/Medium

**Question：** 

<p>Given an integer array <code>A</code>, and an integer <code>target</code>, return the number of&nbsp;tuples&nbsp;<code>i, j, k</code>&nbsp; such that <code>i &lt; j &lt; k</code> and&nbsp;<code>A[i] + A[j] + A[k] == target</code>.</p>

<p><strong>As the answer can be very large, return it modulo&nbsp;<code>10^9 + 7</code></strong>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1,1,2,2,3,3,4,4,5,5]</span>, target = <span id="example-input-1-2">8</span>
<strong>Output: </strong><span id="example-output-1">20</span>
<strong>Explanation: </strong>
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[1,1,2,2,2,2]</span>, target = <span id="example-input-2-2">5</span>
<strong>Output: </strong><span id="example-output-2">12</span>
<strong>Explanation: </strong>
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
</pre>

<p>&nbsp;</p>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>3 &lt;= A.length &lt;= 3000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 100</code></li>
	<li><code>0 &lt;= target &lt;= 300</code></li>
</ol>

------

**题目：** 
<p>给定一个整数数组&nbsp;<code>A</code>，以及一个整数&nbsp;<code>target</code>&nbsp;作为目标值，返回满足 <code>i &lt; j &lt; k</code> 且&nbsp;<code>A[i] + A[j] + A[k] == target</code>&nbsp;的元组&nbsp;<code>i, j, k</code>&nbsp;的数量。</p>

<p>由于结果会非常大，请返回 <code>结果除以 10^9 + 7 的余数</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>A = [1,1,2,2,3,3,4,4,5,5], target = 8
<strong>输出：</strong>20
<strong>解释：</strong>
按值枚举（A[i]，A[j]，A[k]）：
(1, 2, 5) 出现 8 次；
(1, 3, 4) 出现 8 次；
(2, 2, 4) 出现 2 次；
(2, 3, 3) 出现 2 次。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>A = [1,1,2,2,2,2], target = 5
<strong>输出：</strong>12
<strong>解释：</strong>
A[i] = 1，A[j] = A[k] = 2 出现 12 次：
我们从 [1,1] 中选择一个 1，有 2 种情况，
从 [2,2,2,2] 中选出两个 2，有 6 种情况。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>3 &lt;= A.length &lt;= 3000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 100</code></li>
	<li><code>0 &lt;= target &lt;= 300</code></li>
</ol>

