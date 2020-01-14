#### 子数组按位或操作/Bitwise ORs of Subarrays
**难度：** 中等/Medium

**Question：** 

<p>We have an array <code>A</code> of non-negative integers.</p>

<p>For every (contiguous) subarray <code>B =&nbsp;[A[i], A[i+1], ..., A[j]]</code> (with <code>i &lt;= j</code>), we take the bitwise OR of all the elements in <code>B</code>, obtaining a result <font face="monospace"><code>A[i] | A[i+1] | ... | A[j]</code>.</font></p>

<p>Return the number of possible&nbsp;results.&nbsp; (Results that occur more than once are only counted once in the final answer.)</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[0]</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong>
There is only one possible result: 0.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,1,2]</span>
<strong>Output: </strong><span id="example-output-2">3</span>
<strong>Explanation: </strong>
The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[1,2,4]</span>
<strong>Output: </strong><span id="example-output-3">6</span>
<strong>Explanation: </strong>
The possible results are 1, 2, 3, 4, 6, and 7.
</pre>
</div>
</div>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 50000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10^9</code></li>
</ol>


------

**题目：** 
<p>我们有一个非负整数数组&nbsp;<code>A</code>。</p>

<p>对于每个（连续的）子数组&nbsp;<code>B =&nbsp;[A[i], A[i+1], ..., A[j]]</code> （&nbsp;<code>i &lt;= j</code>），我们对&nbsp;<code>B</code>&nbsp;中的每个元素进行按位或操作，获得结果&nbsp;<code>A[i] | A[i+1] | ... | A[j]</code>。</p>

<p>返回可能结果的数量。 （多次出现的结果在最终答案中仅计算一次。）</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[0]
<strong>输出：</strong>1
<strong>解释：</strong>
只有一个可能的结果 0 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[1,1,2]
<strong>输出：</strong>3
<strong>解释：</strong>
可能的子数组为 [1]，[1]，[2]，[1, 1]，[1, 2]，[1, 1, 2]。
产生的结果为 1，1，2，1，3，3 。
有三个唯一值，所以答案是 3 。
</pre>

<p><strong>示例&nbsp;3：</strong></p>

<pre><strong>输入：</strong>[1,2,4]
<strong>输出：</strong>6
<strong>解释：</strong>
可能的结果是 1，2，3，4，6，以及 7 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 50000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10^9</code></li>
</ol>

