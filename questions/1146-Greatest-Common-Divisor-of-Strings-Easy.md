#### 字符串的最大公因子/Greatest Common Divisor of Strings
**难度：** 简单/Easy

**Question：** 

<p>For strings <code>S</code> and <code>T</code>, we say &quot;<code>T</code> divides <code>S</code>&quot; if and only if <code>S = T + ... + T</code>&nbsp; (<code>T</code> concatenated with itself 1 or more times)</p>

<p>Return the largest string <code>X</code> such that <code>X</code> divides <font face="monospace">str1</font>&nbsp;and <code>X</code> divides <font face="monospace">str2</font>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>str1 = <span id="example-input-1-1">&quot;ABCABC&quot;</span>, str2 = <span id="example-input-1-2">&quot;ABC&quot;</span>
<strong>Output: </strong><span id="example-output-1">&quot;ABC&quot;</span>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>str1 = <span id="example-input-2-1">&quot;ABABAB&quot;</span>, str2 = <span id="example-input-2-2">&quot;ABAB&quot;</span>
<strong>Output: </strong><span id="example-output-2">&quot;AB&quot;</span>
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>str1 = <span id="example-input-3-1">&quot;LEET&quot;</span>, str2 = <span id="example-input-3-2">&quot;CODE&quot;</span>
<strong>Output: </strong><span id="example-output-3">&quot;&quot;</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= str1.length &lt;= 1000</code></li>
	<li><code>1 &lt;= str2.length &lt;= 1000</code></li>
	<li><code>str1[i]</code> and <code>str2[i]</code> are English uppercase letters.</li>
</ol>


------

**题目：** 
<p>对于字符串&nbsp;<code>S</code> 和&nbsp;<code>T</code>，只有在 <code>S = T + ... + T</code>（<code>T</code>&nbsp;与自身连接 1 次或多次）时，我们才认定&nbsp;&ldquo;<code>T</code> 能除尽 <code>S</code>&rdquo;。</p>

<p>返回字符串&nbsp;<code>X</code>，要求满足&nbsp;<code>X</code> 能除尽 <code>str1</code> 且&nbsp;<code>X</code> 能除尽 <code>str2</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>str1 = &quot;ABCABC&quot;, str2 = &quot;ABC&quot;
<strong>输出：</strong>&quot;ABC&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>str1 = &quot;ABABAB&quot;, str2 = &quot;ABAB&quot;
<strong>输出：</strong>&quot;AB&quot;
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>str1 = &quot;LEET&quot;, str2 = &quot;CODE&quot;
<strong>输出：</strong>&quot;&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= str1.length &lt;= 1000</code></li>
	<li><code>1 &lt;= str2.length &lt;= 1000</code></li>
	<li><code>str1[i]</code> 和&nbsp;<code>str2[i]</code> 为大写英文字母</li>
</ol>

