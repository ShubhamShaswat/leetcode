#### 分隔数组以得到最大和/Partition Array for Maximum Sum
**难度：** 中等/Medium

**Question：** 

<p>Given an integer array <code>A</code>, you partition the array into (contiguous) subarrays of length at most <code>K</code>.&nbsp; After partitioning, each subarray has their values changed to become the maximum value of that subarray.</p>

<p>Return the largest sum of the given array after partitioning.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1,15,7,9,2,5,10]</span>, K = <span id="example-input-1-2">3</span>
<strong>Output: </strong><span id="example-output-1">84
</span><strong>Explanation</strong>: A becomes [15,15,15,9,10,10,10]</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= K &lt;= A.length&nbsp;&lt;= 500</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10^6</code></li>
</ol>


------

**题目：** 
<p>给出整数数组&nbsp;<code>A</code>，将该数组分隔为长度最多为 K 的几个（连续）子数组。分隔完成后，每个子数组的中的值都会变为该子数组中的最大值。</p>

<p>返回给定数组完成分隔后的最大和。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>A = [1,15,7,9,2,5,10], K = 3
<strong>输出：</strong>84
<strong>解释：</strong>A 变为 [15,15,15,9,10,10,10]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= K &lt;= A.length&nbsp;&lt;= 500</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10^6</code></li>
</ol>

