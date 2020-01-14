#### 最长湍流子数组/Longest Turbulent Subarray
**难度：** 中等/Medium

**Question：** 

<p>A subarray <code>A[i], A[i+1], ..., A[j]</code>&nbsp;of <code>A</code> is said to be <em>turbulent</em> if and only if:</p>

<ul>
	<li>For <code>i &lt;= k &lt; j</code>, <code>A[k] &gt; A[k+1]</code> when <code>k</code> is odd, and <code>A[k] &lt; A[k+1]</code> when <code>k</code> is even;</li>
	<li><strong>OR</strong>, for <code>i &lt;= k &lt; j</code>, <code>A[k] &gt; A[k+1]</code> when <code>k</code> is even, and <code>A[k] &lt; A[k+1]</code> when <code>k</code> is odd.</li>
</ul>

<p>That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.</p>

<p>Return the <strong>length</strong> of a&nbsp;maximum size turbulent subarray of A.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[9,4,2,10,7,8,8,1,9]</span>
<strong>Output: </strong><span id="example-output-1">5</span>
<strong>Explanation: </strong>(A[1] &gt; A[2] &lt; A[3] &gt; A[4] &lt; A[5])
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[4,8,12,16]</span>
<strong>Output: </strong><span id="example-output-2">2</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[100]</span>
<strong>Output: </strong><span id="example-output-3">1</span>
</pre>
</div>
</div>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 40000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10^9</code></li>
</ol>

------

**题目：** 
<p>当 <code>A</code>&nbsp;的子数组&nbsp;<code>A[i], A[i+1], ..., A[j]</code>&nbsp;满足下列条件时，我们称其为<em>湍流子数组</em>：</p>

<ul>
	<li>若&nbsp;<code>i &lt;= k &lt; j</code>，当 <code>k</code>&nbsp;为奇数时，&nbsp;<code>A[k] &gt; A[k+1]</code>，且当 <code>k</code> 为偶数时，<code>A[k] &lt; A[k+1]</code>；</li>
	<li><strong>或 </strong>若&nbsp;<code>i &lt;= k &lt; j</code>，当 <code>k</code> 为偶数时，<code>A[k] &gt; A[k+1]</code>&nbsp;，且当 <code>k</code>&nbsp;为奇数时，&nbsp;<code>A[k] &lt; A[k+1]</code>。</li>
</ul>

<p>也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。</p>

<p>返回 <code>A</code> 的最大湍流子数组的<strong>长度</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[9,4,2,10,7,8,8,1,9]
<strong>输出：</strong>5
<strong>解释：</strong>(A[1] &gt; A[2] &lt; A[3] &gt; A[4] &lt; A[5])
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[4,8,12,16]
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[100]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 40000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10^9</code></li>
</ol>

