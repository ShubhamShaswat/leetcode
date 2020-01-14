#### K 次串联后最大子数组之和/K-Concatenation Maximum Sum
**难度：** 中等/Medium

**Question：** 

<p>Given an integer array <code>arr</code>&nbsp;and an integer <code>k</code>, modify the array by repeating it <code>k</code> times.</p>

<p>For example, if <code>arr&nbsp;= [1, 2]</code> and <code>k = 3 </code>then the modified array will be <code>[1, 2, 1, 2, 1, 2]</code>.</p>

<p>Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be <code>0</code>&nbsp;and its sum in that case is <code>0</code>.</p>

<p>As the answer can be very large, return the answer&nbsp;<strong>modulo</strong>&nbsp;<code>10^9 + 7</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2], k = 3
<strong>Output:</strong> 9
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,-2,1], k = 5
<strong>Output:</strong> 2
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [-1,-2], k = 7
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10^5</code></li>
	<li><code>1 &lt;= k &lt;= 10^5</code></li>
	<li><code>-10^4 &lt;= arr[i] &lt;= 10^4</code></li>
</ul>


------

**题目：** 
<p>给你一个整数数组&nbsp;<code>arr</code>&nbsp;和一个整数&nbsp;<code>k</code>。</p>

<p>首先，我们要对该数组进行修改，即把原数组 <code>arr</code> 重复&nbsp;<code>k</code>&nbsp;次。</p>

<blockquote>
<p>举个例子，如果&nbsp;<code>arr&nbsp;= [1, 2]</code> 且 <code>k = 3</code>，那么修改后的数组就是&nbsp;<code>[1, 2, 1, 2, 1, 2]</code>。</p>
</blockquote>

<p>然后，请你返回修改后的数组中的最大的子数组之和。</p>

<p>注意，子数组长度可以是 <code>0</code>，在这种情况下它的总和也是 <code>0</code>。</p>

<p>由于&nbsp;<strong>结果可能会很大</strong>，所以需要 <strong>模（mod）</strong>&nbsp;<code>10^9 + 7</code>&nbsp;后再返回。&nbsp;</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [1,2], k = 3
<strong>输出：</strong>9
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [1,-2,1], k = 5
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [-1,-2], k = 7
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10^5</code></li>
	<li><code>1 &lt;= k &lt;= 10^5</code></li>
	<li><code>-10^4 &lt;= arr[i] &lt;= 10^4</code></li>
</ul>

