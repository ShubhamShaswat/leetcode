#### 等式方程的可满足性/Satisfiability of Equality Equations
**难度：** 中等/Medium

**Question：** 

<p>Given an array <font face="monospace">equations</font>&nbsp;of strings that represent relationships between variables, each string <code>equations[i]</code>&nbsp;has length <code>4</code> and takes one of two different forms: <code>&quot;a==b&quot;</code> or <code>&quot;a!=b&quot;</code>.&nbsp; Here, <code>a</code> and <code>b</code> are lowercase letters (not necessarily different) that represent one-letter variable names.</p>

<p>Return <code>true</code>&nbsp;if and only if it is possible to assign integers to variable names&nbsp;so as to satisfy all the given equations.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;a==b&quot;,&quot;b!=a&quot;]</span>
<strong>Output: </strong><span id="example-output-1">false</span>
<strong>Explanation: </strong>If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[&quot;b==a&quot;,&quot;a==b&quot;]</span>
<strong>Output: </strong><span id="example-output-2">true</span>
<strong>Explanation: </strong>We could assign a = 1 and b = 1 to satisfy both equations.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[&quot;a==b&quot;,&quot;b==c&quot;,&quot;a==c&quot;]</span>
<strong>Output: </strong><span id="example-output-3">true</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[&quot;a==b&quot;,&quot;b!=c&quot;,&quot;c==a&quot;]</span>
<strong>Output: </strong><span id="example-output-4">false</span>
</pre>

<div>
<p><strong>Example 5:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-5-1">[&quot;c==c&quot;,&quot;b==d&quot;,&quot;x!=z&quot;]</span>
<strong>Output: </strong><span id="example-output-5">true</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= equations.length &lt;= 500</code></li>
	<li><code>equations[i].length == 4</code></li>
	<li><code>equations[i][0]</code> and <code>equations[i][3]</code> are lowercase letters</li>
	<li><code>equations[i][1]</code> is either <code>&#39;=&#39;</code> or <code>&#39;!&#39;</code></li>
	<li><code>equations[i][2]</code> is&nbsp;<code>&#39;=&#39;</code></li>
</ol>
</div>
</div>
</div>
</div>
</div>


------

**题目：** 
<p>给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 <code>equations[i]</code> 的长度为 <code>4</code>，并采用两种不同的形式之一：<code>&quot;a==b&quot;</code> 或&nbsp;<code>&quot;a!=b&quot;</code>。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。</p>

<p>只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回&nbsp;<code>true</code>，否则返回 <code>false</code>。&nbsp;</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[&quot;a==b&quot;,&quot;b!=a&quot;]
<strong>输出：</strong>false
<strong>解释：</strong>如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输出：</strong>[&quot;b==a&quot;,&quot;a==b&quot;]
<strong>输入：</strong>true
<strong>解释：</strong>我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[&quot;a==b&quot;,&quot;b==c&quot;,&quot;a==c&quot;]
<strong>输出：</strong>true
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>[&quot;a==b&quot;,&quot;b!=c&quot;,&quot;c==a&quot;]
<strong>输出：</strong>false
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>[&quot;c==c&quot;,&quot;b==d&quot;,&quot;x!=z&quot;]
<strong>输出：</strong>true
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= equations.length &lt;= 500</code></li>
	<li><code>equations[i].length == 4</code></li>
	<li><code>equations[i][0]</code> 和&nbsp;<code>equations[i][3]</code>&nbsp;是小写字母</li>
	<li><code>equations[i][1]</code> 要么是&nbsp;<code>&#39;=&#39;</code>，要么是&nbsp;<code>&#39;!&#39;</code></li>
	<li><code>equations[i][2]</code>&nbsp;是&nbsp;<code>&#39;=&#39;</code></li>
</ol>

