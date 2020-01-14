#### 最短超级串/Find the Shortest Superstring
**难度：** 困难/Hard

**Question：** 

<p>Given an array A of strings, find any&nbsp;smallest string that contains each string in <code>A</code> as a&nbsp;substring.</p>

<p>We may assume that no string in <code>A</code> is substring of another string in <code>A</code>.</p>

<div>&nbsp;</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;alex&quot;,&quot;loves&quot;,&quot;leetcode&quot;]</span>
<strong>Output: </strong><span id="example-output-1">&quot;alexlovesleetcode&quot;</span>
<strong>Explanation: </strong>All permutations of &quot;alex&quot;,&quot;loves&quot;,&quot;leetcode&quot; would also be accepted.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[&quot;catg&quot;,&quot;ctaagt&quot;,&quot;gcta&quot;,&quot;ttca&quot;,&quot;atgcatc&quot;]</span>
<strong>Output: </strong><span id="example-output-2">&quot;gctaagttcatgcatc&quot;</span></pre>

<p>&nbsp;</p>
</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 12</code></li>
	<li><code>1 &lt;= A[i].length &lt;= 20</code></li>
</ol>

<div>
<div>&nbsp;</div>
</div>

------

**题目：** 
<p>给定一个字符串数组 <code>A</code>，找到以&nbsp;<code>A</code>&nbsp;中每个字符串作为子字符串的最短字符串。</p>

<p>我们可以假设 <code>A</code> 中没有字符串是 <code>A</code> 中另一个字符串的子字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[&quot;alex&quot;,&quot;loves&quot;,&quot;leetcode&quot;]
<strong>输出：</strong>&quot;alexlovesleetcode&quot;
<strong>解释：</strong>&quot;alex&quot;，&quot;loves&quot;，&quot;leetcode&quot; 的所有排列都会被接受。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[&quot;catg&quot;,&quot;ctaagt&quot;,&quot;gcta&quot;,&quot;ttca&quot;,&quot;atgcatc&quot;]
<strong>输出：</strong>&quot;gctaagttcatgcatc&quot;</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 12</code></li>
	<li><code>1 &lt;= A[i].length &lt;= 20</code></li>
</ol>

<p>&nbsp;</p>

