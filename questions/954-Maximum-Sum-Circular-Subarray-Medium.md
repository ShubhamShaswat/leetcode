#### 环形子数组的最大和/Maximum Sum Circular Subarray
**难度：** 中等/Medium

**Question：** 

<p>Given a <strong>circular&nbsp;array</strong>&nbsp;<strong>C</strong> of integers represented by&nbsp;<code>A</code>, find the maximum possible sum of a non-empty subarray of <strong>C</strong>.</p>

<p>Here, a&nbsp;<em>circular&nbsp;array</em> means the end of the array connects to the beginning of the array.&nbsp; (Formally, <code>C[i] = A[i]</code> when <code>0 &lt;= i &lt; A.length</code>, and <code>C[i+A.length] = C[i]</code>&nbsp;when&nbsp;<code>i &gt;= 0</code>.)</p>

<p>Also, a subarray may only include each element of the fixed buffer <code>A</code> at most once.&nbsp; (Formally, for a subarray <code>C[i], C[i+1], ..., C[j]</code>, there does not exist <code>i &lt;= k1, k2 &lt;= j</code> with <code>k1 % A.length&nbsp;= k2 % A.length</code>.)</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,-2,3,-2]</span>
<strong>Output: </strong><span id="example-output-1">3
<strong>Explanation: </strong>Subarray [3] has maximum sum 3</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[5,-3,5]</span>
<strong>Output: </strong><span id="example-output-2">10
</span><span id="example-output-3"><strong>Explanation:</strong>&nbsp;</span><span id="example-output-1">Subarray [5,5] has maximum sum </span><span>5 + 5 = 10</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[3,-1,2,-1]</span>
<strong>Output: </strong><span id="example-output-3">4
<strong>Explanation:</strong>&nbsp;</span><span id="example-output-1">Subarray [2,-1,3] has maximum sum </span><span>2 + (-1) + 3 = 4</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[3,-2,2,-3]</span>
<strong>Output: </strong><span id="example-output-4">3
</span><span id="example-output-3"><strong>Explanation:</strong>&nbsp;</span><span id="example-output-1">Subarray [3] and [3,-2,2] both have maximum sum </span><span>3</span>
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-5-1">[-2,-3,-1]</span>
<strong>Output: </strong><span id="example-output-5">-1
</span><span id="example-output-3"><strong>Explanation:</strong>&nbsp;</span><span id="example-output-1">Subarray [-1] has maximum sum -1</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note: </strong></p>

<ol>
	<li><code>-30000 &lt;= A[i] &lt;= 30000</code></li>
	<li><code>1 &lt;= A.length &lt;= 30000</code></li>
</ol>
</div>
</div>
</div>
</div>


------

**题目：** 
<p>给定一个由整数数组 <code>A</code>&nbsp;表示的<strong>环形数组 <code>C</code></strong>，求 <code><strong>C</strong></code>&nbsp;的非空子数组的最大可能和。</p>

<p>在此处，<em>环形数组</em>意味着数组的末端将会与开头相连呈环状。（形式上，当<code>0 &lt;= i &lt; A.length</code>&nbsp;时&nbsp;<code>C[i] = A[i]</code>，而当&nbsp;<code>i &gt;= 0</code>&nbsp;时&nbsp;<code>C[i+A.length] = C[i]</code>）</p>

<p>此外，子数组最多只能包含固定缓冲区 <code>A</code>&nbsp;中的每个元素一次。（形式上，对于子数组&nbsp;<code>C[i], C[i+1], ..., C[j]</code>，不存在&nbsp;<code>i &lt;= k1, k2 &lt;= j</code>&nbsp;其中&nbsp;<code>k1 % A.length&nbsp;= k2 % A.length</code>）</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[1,-2,3,-2]
<strong>输出：</strong>3
<strong>解释：</strong>从子数组 [3] 得到最大和 3
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[5,-3,5]
<strong>输出：</strong>10
<strong>解释：</strong>从子数组 [5,5] 得到最大和 5 + 5 = 10
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[3,-1,2,-1]
<strong>输出：</strong>4
<strong>解释：</strong>从子数组 [2,-1,3] 得到最大和 2 + (-1) + 3 = 4
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>[3,-2,2,-3]
<strong>输出：</strong>3
<strong>解释：</strong>从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>[-2,-3,-1]
<strong>输出：</strong>-1
<strong>解释：</strong>从子数组 [-1] 得到最大和 -1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>-30000 &lt;= A[i] &lt;= 30000</code></li>
	<li><code>1 &lt;= A.length &lt;= 30000</code></li>
</ol>

