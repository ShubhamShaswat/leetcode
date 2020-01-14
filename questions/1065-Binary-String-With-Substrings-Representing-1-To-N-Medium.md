#### 子串能表示从 1 到 N 数字的二进制串/Binary String With Substrings Representing 1 To N
**难度：** 中等/Medium

**Question：** 

<p>Given a binary string <code>S</code> (a string consisting only of &#39;0&#39; and &#39;1&#39;s) and a positive integer <code>N</code>, return true if and only if for every integer X from 1 to N, the binary representation of X is a substring of S.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-1-1">&quot;0110&quot;</span>, N = <span id="example-input-1-2">3</span>
<strong>Output: </strong><span id="example-output-1">true</span>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-2-1">&quot;0110&quot;</span>, N = <span id="example-input-2-2">4</span>
<strong>Output: </strong><span id="example-output-2">false</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= S.length &lt;= 1000</code></li>
	<li><code>1 &lt;= N &lt;= 10^9</code></li>
</ol>


------

**题目：** 
<p>给定一个二进制字符串&nbsp;<code>S</code>（一个仅由若干&nbsp;&#39;0&#39; 和 &#39;1&#39; 构成的字符串）和一个正整数&nbsp;<code>N</code>，如果对于从 <code>1</code> 到 <code>N</code> 的每个整数 <code>X</code>，其二进制表示都是&nbsp;<code>S</code> 的子串，就返回 <code>true</code>，否则返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>S = &quot;0110&quot;, N = 3
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>S = &quot;0110&quot;, N = 4
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= S.length &lt;= 1000</code></li>
	<li><code>1 &lt;= N &lt;= 10^9</code></li>
</ol>

