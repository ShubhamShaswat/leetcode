#### 二倍数对数组/Array of Doubled Pairs
**难度：** 中等/Medium

**Question：** 

<p>Given an array of integers <code>A</code>&nbsp;with even length, return <code>true</code> if and only if it is possible to reorder it such that <code>A[2 * i + 1] = 2 * A[2 * i]</code> for every <code>0 &lt;=&nbsp;i &lt; len(A) / 2</code>.</p>

<p>&nbsp;</p>

<div>
<div>
<div>
<ol>
</ol>
</div>
</div>
</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[3,1,3,6]</span>
<strong>Output: </strong><span id="example-output-1">false</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[2,1,2,6]</span>
<strong>Output: </strong><span id="example-output-2">false</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[4,-2,2,-4]</span>
<strong>Output: </strong><span id="example-output-3">true</span>
<strong>Explanation: </strong><span id="example-output-3">We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[1,2,4,16,8,4]</span>
<strong>Output: </strong><span id="example-output-4">false</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt;= 30000</code></li>
	<li><code>A.length</code> is even</li>
	<li><code>-100000 &lt;= A[i] &lt;= 100000</code></li>
</ol>
</div>
</div>
</div>
</div>


------

**题目：** 
<p>给定一个长度为偶数的整数数组&nbsp;<code>A</code>，只有对&nbsp;<code>A</code>&nbsp;进行重组后可以满足 &ldquo;对于每个 <code>0 &lt;=&nbsp;i &lt; len(A) / 2</code>，都有 <code>A[2 * i + 1] = 2 * A[2 * i]</code>&rdquo;&nbsp;时，返回 <code>true</code>；否则，返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[3,1,3,6]
<strong>输出：</strong>false
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[2,1,2,6]
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[4,-2,2,-4]
<strong>输出：</strong>true
<strong>解释：</strong>我们可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>[1,2,4,16,8,4]
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt;= 30000</code></li>
	<li><code>A.length</code>&nbsp;为偶数</li>
	<li><code>-100000 &lt;= A[i] &lt;= 100000</code></li>
</ol>

