#### 负二进制转换/Convert to Base -2
**难度：** 中等/Medium

**Question：** 

<p>Given a number <code>N</code>, return a string consisting of <code>&quot;0&quot;</code>s and <code>&quot;1&quot;</code>s&nbsp;that represents its value in base <code><strong>-2</strong></code>&nbsp;(negative two).</p>

<p>The returned string must have no leading zeroes, unless the string is <code>&quot;0&quot;</code>.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">2</span>
<strong>Output: </strong><span id="example-output-1">&quot;110&quot;
<strong>Explantion:</strong> (-2) ^ 2 + (-2) ^ 1 = 2</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">3</span>
<strong>Output: </strong><span id="example-output-2">&quot;111&quot;
</span><span id="example-output-1"><strong>Explantion:</strong> (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0</span><span> = 3</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">4</span>
<strong>Output: </strong><span id="example-output-3">&quot;100&quot;
</span><span id="example-output-1"><strong>Explantion:</strong> (-2) ^ 2 = 4</span>
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ol>
	<li><span><code>0 &lt;= N &lt;= 10^9</code></span></li>
</ol>
</div>
</div>
</div>

------

**题目：** 
<p>给出数字&nbsp;<code>N</code>，返回由若干&nbsp;<code>&quot;0&quot;</code>&nbsp;和&nbsp;<code>&quot;1&quot;</code>组成的字符串，该字符串为 <code>N</code>&nbsp;的<strong>负二进制（<code>base -2</code>）</strong>表示。</p>

<p>除非字符串就是&nbsp;<code>&quot;0&quot;</code>，否则返回的字符串中不能含有前导零。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>2
<strong>输出：</strong>&quot;110&quot;
<strong>解释：</strong>(-2) ^ 2 + (-2) ^ 1 = 2
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>3
<strong>输出：</strong>&quot;111&quot;
<strong>解释：</strong>(-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>4
<strong>输出：</strong>&quot;100&quot;
<strong>解释：</strong>(-2) ^ 2 = 4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>0 &lt;= N &lt;= 10^9</code></li>
</ol>

