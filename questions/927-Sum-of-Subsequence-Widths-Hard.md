#### 子序列宽度之和/Sum of Subsequence Widths
**难度：** 困难/Hard

**Question：** 

<p>Given an array of integers <code>A</code>, consider all non-empty subsequences of <code>A</code>.</p>

<p>For any sequence S, let the&nbsp;<em>width</em>&nbsp;of S be the difference between the maximum and minimum element of S.</p>

<p>Return the sum of the widths of all subsequences of A.&nbsp;</p>

<p>As the answer may be very large, <strong>return the answer modulo 10^9 + 7</strong>.</p>

<div>
<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[2,1,3]</span>
<strong>Output: </strong><span id="example-output-1">6</span>
<strong>Explanation:
</strong>Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>1 &lt;= A.length &lt;= 20000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 20000</code></li>
</ul>
</div>


------

**题目：** 
<p>给定一个整数数组 <code>A</code> ，考虑 <code>A</code> 的所有非空子序列。</p>

<p>对于任意序列 S ，设 S 的宽度是 S 的最大元素和最小元素的差。</p>

<p>返回 A 的所有子序列的宽度之和。</p>

<p>由于答案可能非常大，请<strong>返回答案模 10^9+7</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>[2,1,3]
<strong>输出：</strong>6
<strong>解释：
</strong>子序列为 [1]，[2]，[3]，[2,1]，[2,3]，[1,3]，[2,1,3] 。
相应的宽度是 0，0，0，1，1，2，2 。
这些宽度之和是 6 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= A.length &lt;= 20000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 20000</code></li>
</ul>

