#### 超级回文数/Super Palindromes
**难度：** 困难/Hard

**Question：** 

<p>Let&#39;s say a positive integer is a&nbsp;<em>superpalindrome</em>&nbsp;if it is a palindrome, and it is also the square of a palindrome.</p>

<p>Now, given two positive&nbsp;integers <code>L</code> and <code>R</code> (represented as strings), return the number of superpalindromes in the inclusive range <code>[L, R]</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>L = <span id="example-input-1-1">&quot;4&quot;</span>, R = <span id="example-input-1-2">&quot;1000&quot;</span>
<strong>Output: </strong>4
<span><strong>Explanation</strong>: </span>4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= len(L) &lt;= 18</code></li>
	<li><code>1 &lt;= len(R) &lt;= 18</code></li>
	<li><code>L</code> and <code>R</code> are strings representing integers in the range <code>[1, 10^18)</code>.</li>
	<li><code>int(L) &lt;= int(R)</code></li>
</ol>

<div>
<p>&nbsp;</p>
</div>


------

**题目：** 
<p>如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为超级回文数。</p>

<p>现在，给定两个正整数&nbsp;<code>L</code> 和&nbsp;<code>R</code> （以字符串形式表示），返回包含在范围 <code>[L, R]</code> 中的超级回文数的数目。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>L = &quot;4&quot;, R = &quot;1000&quot;
<strong>输出：</strong>4
<strong>解释：
</strong>4，9，121，以及 484 是超级回文数。
注意 676 不是一个超级回文数： 26 * 26 = 676，但是 26 不是回文数。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= len(L) &lt;= 18</code></li>
	<li><code>1 &lt;= len(R) &lt;= 18</code></li>
	<li><code>L</code> 和&nbsp;<code>R</code>&nbsp;是表示&nbsp;<code>[1, 10^18)</code>&nbsp;范围的整数的字符串。</li>
	<li><code>int(L) &lt;= int(R)</code></li>
</ol>

<p>&nbsp;</p>

