#### 子数组的最小值之和/Sum of Subarray Minimums
**难度：** 中等/Medium

**Question：** 

<p>Given an array of integers <code>A</code>, find the sum of <code>min(B)</code>, where <code>B</code> ranges over&nbsp;every (contiguous) subarray of <code>A</code>.</p>

<p>Since the answer may be large, <strong>return the answer modulo <code>10^9 + 7</code>.</strong></p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[3,1,2,4]</span>
<strong>Output: </strong><span id="example-output-1">17</span>
<strong>Explanation:</strong> Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.&nbsp; Sum is 17.</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 30000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 30000</code></li>
</ol>

<div>
<p>&nbsp;</p>
</div>


------

**题目：** 
<p>给定一个整数数组 <code>A</code>，找到 <code>min(B)</code>&nbsp;的总和，其中 <code>B</code> 的范围为&nbsp;<code>A</code> 的每个（连续）子数组。</p>

<p>由于答案可能很大，因此<strong>返回答案模 <code>10^9 + 7</code></strong>。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>[3,1,2,4]
<strong>输出：</strong>17
<strong>解释：
子数组为 </strong>[3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。 
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A &lt;= 30000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 30000</code></li>
</ol>

<p>&nbsp;</p>

