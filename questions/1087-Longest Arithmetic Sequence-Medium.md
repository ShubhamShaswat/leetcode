#### 最长等差数列/Longest Arithmetic Sequence
**难度：** 中等/Medium

**Question：** 

<p>Given an array <code>A</code> of integers, return the <strong>length</strong> of the longest arithmetic subsequence in <code>A</code>.</p>

<p>Recall that a <em>subsequence</em> of <code>A</code> is a list <code>A[i_1], A[i_2], ..., A[i_k]</code> with <code>0 &lt;= i_1 &lt; i_2 &lt; ... &lt; i_k &lt;= A.length - 1</code>, and that a sequence <code>B</code>&nbsp;is <em>arithmetic</em> if <code>B[i+1] - B[i]</code> are all the same value (for <code>0 &lt;= i &lt; B.length - 1</code>).</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[3,6,9,12]</span>
<strong>Output: </strong><span id="example-output-1">4</span>
<strong>Explanation: </strong>
The whole array is an arithmetic sequence with steps of length = 3.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[9,4,7,2,10]</span>
<strong>Output: </strong><span id="example-output-2">3</span>
<strong>Explanation: </strong>
The longest arithmetic subsequence is [4,7,10].
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[20,1,15,3,10,5,8]</span>
<strong>Output: </strong><span id="example-output-3">4</span>
<strong>Explanation: </strong>
The longest arithmetic subsequence is [20,15,10,5].
</pre>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>2 &lt;= A.length &lt;= 2000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10000</code></li>
</ol>
</div>

------

**题目：** 
<p>给定一个整数数组&nbsp;<code>A</code>，返回 <code>A</code>&nbsp;中最长等差子序列的<strong>长度</strong>。</p>

<p>回想一下，<code>A</code>&nbsp;的子序列是列表&nbsp;<code>A[i_1], A[i_2], ..., A[i_k]</code> 其中&nbsp;<code>0 &lt;= i_1 &lt; i_2 &lt; ... &lt; i_k &lt;= A.length - 1</code>。并且如果&nbsp;<code>B[i+1] - B[i]</code>(&nbsp;<code>0 &lt;= i &lt; B.length - 1</code>) 的值都相同，那么序列&nbsp;<code>B</code>&nbsp;是等差的。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[3,6,9,12]
<strong>输出：</strong>4
<strong>解释： </strong>
整个数组是公差为 3 的等差数列。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[9,4,7,2,10]
<strong>输出：</strong>3
<strong>解释：</strong>
最长的等差子序列是 [4,7,10]。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[20,1,15,3,10,5,8]
<strong>输出：</strong>4
<strong>解释：</strong>
最长的等差子序列是 [20,15,10,5]。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>2 &lt;= A.length &lt;= 2000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10000</code></li>
</ol>

