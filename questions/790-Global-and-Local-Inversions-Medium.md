#### 全局倒置与局部倒置/Global and Local Inversions
**难度：** 中等/Medium

**Question：** 

<p>We have some permutation <code>A</code> of <code>[0, 1, ..., N - 1]</code>, where <code>N</code> is the length of <code>A</code>.</p>

<p>The number of (global) inversions is the number of <code>i &lt; j</code> with <code>0 &lt;= i &lt; j &lt; N</code> and <code>A[i] &gt; A[j]</code>.</p>

<p>The number of local inversions is the number of <code>i</code> with <code>0 &lt;= i &lt; N</code> and <code>A[i] &gt; A[i+1]</code>.</p>

<p>Return <code>true</code>&nbsp;if and only if the number of global inversions is equal to the number of local inversions.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> A = [1,0,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> There is 1 global inversion, and 1 local inversion.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> A = [1,2,0]
<strong>Output:</strong> false
<strong>Explanation:</strong> There are 2 global inversions, and 1 local inversion.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>A</code> will be a permutation of <code>[0, 1, ..., A.length - 1]</code>.</li>
	<li><code>A</code> will have length in range <code>[1, 5000]</code>.</li>
	<li>The time limit for this problem has been reduced.</li>
</ul>


------

**题目：** 
<p>数组&nbsp;<code>A</code>&nbsp;是&nbsp;<code>[0, 1, ..., N - 1]</code>&nbsp;的一种排列，<code>N</code> 是数组&nbsp;<code>A</code>&nbsp;的长度。全局倒置指的是 <code>i,j</code>&nbsp;满足&nbsp;<code>0 &lt;= i &lt; j &lt; N</code> 并且&nbsp;<code>A[i] &gt; A[j]</code>&nbsp;，局部倒置指的是 <code>i</code> 满足&nbsp;<code>0 &lt;= i &lt; N</code>&nbsp;并且&nbsp;<code>A[i] &gt; A[i+1]</code>&nbsp;。</p>

<p>当数组&nbsp;<code>A</code>&nbsp;中全局倒置的数量等于局部倒置的数量时，返回 <code>true</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> A = [1,0,2]
<strong>输出:</strong> true
<strong>解释:</strong> 有 1 个全局倒置，和 1 个局部倒置。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> A = [1,2,0]
<strong>输出:</strong> false
<strong>解释:</strong> 有 2 个全局倒置，和 1 个局部倒置。
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>A</code> 是&nbsp;<code>[0, 1, ..., A.length - 1]</code>&nbsp;的一种排列</li>
	<li><code>A</code> 的长度在&nbsp;<code>[1, 5000]</code>之间</li>
	<li>这个问题的时间限制已经减少了。</li>
</ul>

