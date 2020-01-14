#### 按字典序排在最后的子串/Last Substring in Lexicographical Order
**难度：** 困难/Hard

**Question：** 

<p>Given a string <code>s</code>, return the last substring of <code>s</code> in lexicographical order.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;abab&quot;</span>
<strong>Output: </strong><span id="example-output-1">&quot;bab&quot;</span>
<strong>Explanation: </strong>The substrings are [&quot;a&quot;, &quot;ab&quot;, &quot;aba&quot;, &quot;abab&quot;, &quot;b&quot;, &quot;ba&quot;, &quot;bab&quot;]. The lexicographically maximum substring is &quot;bab&quot;.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">&quot;leetcode&quot;</span>
<strong>Output: </strong><span id="example-output-2">&quot;tcode&quot;</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= s.length &lt;= 4&nbsp;* 10^5</code></li>
	<li><font face="monospace">s</font> contains only lowercase English letters.</li>
</ol>


------

**题目：** 
<p>给你一个字符串&nbsp;<code>s</code>，找出它的所有子串并按字典序排列，返回排在最后的那个子串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>&quot;abab&quot;
<strong>输出：</strong>&quot;bab&quot;
<strong>解释：</strong>我们可以找出 7 个子串 [&quot;a&quot;, &quot;ab&quot;, &quot;aba&quot;, &quot;abab&quot;, &quot;b&quot;, &quot;ba&quot;, &quot;bab&quot;]。按字典序排在最后的子串是 &quot;bab&quot;。
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre><strong>输入：</strong>&quot;leetcode&quot;
<strong>输出：</strong>&quot;tcode&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= s.length &lt;= 4 * 10^5</code></li>
	<li>s 仅含有小写英文字符。</li>
</ol>

