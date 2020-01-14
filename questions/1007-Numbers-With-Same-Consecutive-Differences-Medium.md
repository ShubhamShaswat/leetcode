#### 连续差相同的数字/Numbers With Same Consecutive Differences
**难度：** 中等/Medium

**Question：** 

<p>Return all <strong>non-negative</strong> integers of length <code>N</code> such that the absolute difference between every two consecutive digits is <code>K</code>.</p>

<p>Note that <strong>every</strong> number in the answer <strong>must not</strong> have leading zeros <strong>except</strong> for the number <code>0</code> itself. For example, <code>01</code> has one leading zero and is invalid, but <code>0</code> is valid.</p>

<p>You may return the answer in any order.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-1-1">3</span>, K = <span id="example-input-1-2">7</span>
<strong>Output: </strong><span id="example-output-1">[181,292,707,818,929]</span>
<strong>Explanation: </strong>Note that 070 is not a valid number, because it has leading zeroes.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-2-1">2</span>, K = <span id="example-input-2-2">1</span>
<strong>Output: </strong><span id="example-output-2">[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]</span></pre>

<p>&nbsp;</p>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 9</code></li>
	<li><code>0 &lt;= K &lt;= 9</code></li>
</ol>


------

**题目：** 
<p>返回所有长度为 <code>N</code> 且满足其每两个连续位上的数字之间的差的绝对值为 <code>K</code>&nbsp;的<strong>非负整数</strong>。</p>

<p>请注意，<strong>除了</strong>数字 <code>0</code> 本身之外，答案中的每个数字都<strong>不能</strong>有前导零。例如，<code>01</code>&nbsp;因为有一个前导零，所以是无效的；但 <code>0</code>&nbsp;是有效的。</p>

<p>你可以按任何顺序返回答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>N = 3, K = 7
<strong>输出：</strong>[181,292,707,818,929]
<strong>解释：</strong>注意，070 不是一个有效的数字，因为它有前导零。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>N = 2, K = 1
<strong>输出：</strong>[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 9</code></li>
	<li><code>0 &lt;= K &lt;= 9</code></li>
</ol>

