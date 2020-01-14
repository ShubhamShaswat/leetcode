#### 分割回文串 III/Palindrome Partitioning III
**难度：** 困难/Hard

**Question：** 

<p>You are given a string&nbsp;<code>s</code> containing lowercase letters and an integer <code>k</code>. You need to :</p>

<ul>
	<li>First, change some characters of <code>s</code>&nbsp;to other lowercase English letters.</li>
	<li>Then divide <code>s</code>&nbsp;into <code>k</code> non-empty disjoint substrings such that each substring is palindrome.</li>
</ul>

<p>Return the minimal number of characters that you need to change&nbsp;to divide the string.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abc&quot;, k = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong>&nbsp;You can split the string into &quot;ab&quot; and &quot;c&quot;, and change 1 character in &quot;ab&quot; to make it palindrome.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aabbc&quot;, k = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong>&nbsp;You can split the string into &quot;aa&quot;, &quot;bb&quot; and &quot;c&quot;, all of them are palindrome.</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;leetcode&quot;, k = 8
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= s.length &lt;= 100</code>.</li>
	<li><code>s</code>&nbsp;only contains lowercase English letters.</li>
</ul>

------

**题目：** 
<p>给你一个由小写字母组成的字符串&nbsp;<code>s</code>，和一个整数&nbsp;<code>k</code>。</p>

<p>请你按下面的要求分割字符串：</p>

<ul>
	<li>首先，你可以将&nbsp;<code>s</code>&nbsp;中的部分字符修改为其他的小写英文字母。</li>
	<li>接着，你需要把&nbsp;<code>s</code>&nbsp;分割成&nbsp;<code>k</code>&nbsp;个非空且不相交的子串，并且每个子串都是回文串。</li>
</ul>

<p>请返回以这种方式分割字符串所需修改的最少字符数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;abc&quot;, k = 2
<strong>输出：</strong>1
<strong>解释：</strong>你可以把字符串分割成 &quot;ab&quot; 和 &quot;c&quot;，并修改 &quot;ab&quot; 中的 1 个字符，将它变成回文串。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;aabbc&quot;, k = 3
<strong>输出：</strong>0
<strong>解释：</strong>你可以把字符串分割成 &quot;aa&quot;、&quot;bb&quot; 和 &quot;c&quot;，它们都是回文串。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;leetcode&quot;, k = 8
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code>&nbsp;中只含有小写英文字母。</li>
</ul>

