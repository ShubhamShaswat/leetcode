#### 最小差值 I/Smallest Range I
**难度：** 简单/Easy

**Question：** 

<p>Given an array <code>A</code> of integers, for each integer <code>A[i]</code> we may choose any <code>x</code> with <code>-K &lt;= x &lt;= K</code>, and add <code>x</code> to <code>A[i]</code>.</p>

<p>After this process, we have some array <code>B</code>.</p>

<p>Return the smallest possible difference between the maximum value of <code>B</code>&nbsp;and the minimum value of <code>B</code>.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1]</span>, K = <span id="example-input-1-2">0</span>
<strong>Output: </strong><span id="example-output-1">0
<strong>Explanation</strong>: B = [1]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[0,10]</span>, K = <span id="example-input-2-2">2</span>
<strong>Output: </strong><span id="example-output-2">6
</span><span id="example-output-1"><strong>Explanation</strong>: B = [2,8]</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">[1,3,6]</span>, K = <span id="example-input-3-2">3</span>
<strong>Output: </strong><span id="example-output-3">0
</span><span id="example-output-1"><strong>Explanation</strong>: B = [3,3,3] or B = [4,4,4]</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 10000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10000</code></li>
	<li><code>0 &lt;= K &lt;= 10000</code></li>
</ol>
</div>
</div>
</div>

------

**题目：** 
<p>给定一个整数数组 <code>A</code>，对于每个整数 <code>A[i]</code>，我们可以选择任意&nbsp;<code>x</code> 满足&nbsp;<code>-K &lt;= x &lt;= K</code>，并将&nbsp;<code>x</code>&nbsp;加到&nbsp;<code>A[i]</code>&nbsp;中。</p>

<p>在此过程之后，我们得到一些数组&nbsp;<code>B</code>。</p>

<p>返回 <code>B</code>&nbsp;的最大值和 <code>B</code>&nbsp;的最小值之间可能存在的最小差值。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>A = [1], K = 0
<strong>输出：</strong>0
<strong>解释：</strong>B = [1]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>A = [0,10], K = 2
<strong>输出：</strong>6
<strong>解释：</strong>B = [2,8]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>A = [1,3,6], K = 3
<strong>输出：</strong>0
<strong>解释：</strong>B = [3,3,3] 或 B = [4,4,4]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 10000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10000</code></li>
	<li><code>0 &lt;= K &lt;= 10000</code></li>
</ol>

