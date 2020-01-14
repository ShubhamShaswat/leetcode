#### 丑数 III/Ugly Number III
**难度：** 中等/Medium

**Question：** 

<p>Write a program to find the&nbsp;<code>n</code>-th ugly number.</p>

<p>Ugly numbers are<strong>&nbsp;positive integers</strong>&nbsp;which are divisible by&nbsp;<code>a</code>&nbsp;<strong>or</strong>&nbsp;<code>b</code>&nbsp;<strong>or</strong> <code>c</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3, a = 2, b = 3, c = 5
<strong>Output:</strong> 4
<strong>Explanation: </strong>The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 4, a = 2, b = 3, c = 4
<strong>Output:</strong> 6
<strong>Explanation: </strong>The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 5, a = 2, b = 11, c = 13
<strong>Output:</strong> 10
<strong>Explanation: </strong>The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> n = 1000000000, a = 2, b = 217983653, c = 336916467
<strong>Output:</strong> 1999999984
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n, a, b, c &lt;= 10^9</code></li>
	<li><code>1 &lt;= a * b * c &lt;= 10^18</code></li>
	<li>It&#39;s guaranteed that the result will be in range&nbsp;<code>[1,&nbsp;2 * 10^9]</code></li>
</ul>


------

**题目：** 
<p>请你帮忙设计一个程序，用来找出第&nbsp;<code>n</code>&nbsp;个丑数。</p>

<p>丑数是可以被&nbsp;<code>a</code>&nbsp;<strong>或</strong>&nbsp;<code>b</code>&nbsp;<strong>或</strong> <code>c</code>&nbsp;整除的 <strong>正整数</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 3, a = 2, b = 3, c = 5
<strong>输出：</strong>4
<strong>解释：</strong>丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 4, a = 2, b = 3, c = 4
<strong>输出：</strong>6
<strong>解释：</strong>丑数序列为 2, 3, 4, 6, 8, 9, 12... 其中第 4 个是 6。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 5, a = 2, b = 11, c = 13
<strong>输出：</strong>10
<strong>解释：</strong>丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>n = 1000000000, a = 2, b = 217983653, c = 336916467
<strong>输出：</strong>1999999984
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n, a, b, c &lt;= 10^9</code></li>
	<li><code>1 &lt;= a * b * c &lt;= 10^18</code></li>
	<li>本题结果在&nbsp;<code>[1,&nbsp;2 * 10^9]</code>&nbsp;的范围内</li>
</ul>

