#### 第 N 个神奇数字/Nth Magical Number
**难度：** 困难/Hard

**Question：** 

<p>A positive integer&nbsp;is <em>magical</em>&nbsp;if it is divisible by either <font face="monospace">A</font>&nbsp;or <font face="monospace">B</font>.</p>

<p>Return the <font face="monospace">N</font>-th magical number.&nbsp; Since the answer may be very large, <strong>return it modulo </strong><code>10^9 + 7</code>.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-1-1">1</span>, A = <span id="example-input-1-2">2</span>, B = <span id="example-input-1-3">3</span>
<strong>Output: </strong><span id="example-output-1">2</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-2-1">4</span>, A = <span id="example-input-2-2">2</span>, B = <span id="example-input-2-3">3</span>
<strong>Output: </strong><span id="example-output-2">6</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-3-1">5</span>, A = <span id="example-input-3-2">2</span>, B = <span id="example-input-3-3">4</span>
<strong>Output: </strong><span id="example-output-3">10</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-4-1">3</span>, A = <span id="example-input-4-2">6</span>, B = <span id="example-input-4-3">4</span>
<strong>Output: </strong><span id="example-output-4">8</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= N&nbsp;&lt;= 10^9</code></li>
	<li><code>2 &lt;= A&nbsp;&lt;= 40000</code></li>
	<li><code>2 &lt;= B&nbsp;&lt;= 40000</code></li>
</ol>
</div>
</div>
</div>
</div>


------

**题目：** 
<p>如果正整数可以被 A 或 B 整除，那么它是神奇的。</p>

<p>返回第 N 个神奇数字。由于答案可能非常大，<strong>返回它模&nbsp;</strong><code>10^9 + 7</code>&nbsp;<strong>的结果</strong>。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>N = 1, A = 2, B = 3
<strong>输出：</strong>2
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre><strong>输入：</strong>N = 4, A = 2, B = 3
<strong>输出：</strong>6
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>N = 5, A = 2, B = 4
<strong>输出：</strong>10
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>N = 3, A = 6, B = 4
<strong>输出：</strong>8
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= N&nbsp;&lt;= 10^9</code></li>
	<li><code>2 &lt;= A&nbsp;&lt;= 40000</code></li>
	<li><code>2 &lt;= B&nbsp;&lt;= 40000</code></li>
</ol>

