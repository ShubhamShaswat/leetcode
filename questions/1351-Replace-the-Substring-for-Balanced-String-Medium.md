#### 替换子串得到平衡字符串/Replace the Substring for Balanced String
**难度：** 中等/Medium

**Question：** 

<p>You are given a string containing only 4&nbsp;kinds of characters <code>&#39;Q&#39;,</code> <code>&#39;W&#39;, &#39;E&#39;</code> and&nbsp;<code>&#39;R&#39;</code>.</p>

<p>A string is said to be&nbsp;<strong>balanced</strong><em>&nbsp;</em>if each of its characters appears&nbsp;<code>n/4</code> times where <code>n</code> is the length of the string.</p>

<p>Return the minimum length of the substring that can be replaced with <strong>any</strong> other string of the same length to make the original string <code>s</code>&nbsp;<strong>balanced</strong>.</p>

<p>Return 0 if the string is already <strong>balanced</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;QWER&quot;
<strong>Output:</strong> 0
<strong>Explanation: </strong>s is already balanced.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;QQWE&quot;
<strong>Output:</strong> 1
<strong>Explanation: </strong>We need to replace a &#39;Q&#39; to &#39;R&#39;, so that &quot;RQWE&quot; (or &quot;QRWE&quot;) is balanced.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;QQQW&quot;
<strong>Output:</strong> 2
<strong>Explanation: </strong>We can replace the first &quot;QQ&quot; to &quot;ER&quot;. 
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;QQQQ&quot;
<strong>Output:</strong> 3
<strong>Explanation: </strong>We can replace the last 3 &#39;Q&#39; to make s = &quot;QWER&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10^5</code></li>
	<li><code>s.length</code> is a multiple of <code>4</code></li>
	<li><code>s&nbsp;</code>contains only <code>&#39;Q&#39;</code>, <code>&#39;W&#39;</code>, <code>&#39;E&#39;</code> and&nbsp;<code>&#39;R&#39;</code>.</li>
</ul>


------

**题目：** 
<p>有一个只含有&nbsp;<code>&#39;Q&#39;, &#39;W&#39;, &#39;E&#39;,&nbsp;&#39;R&#39;</code>&nbsp;四种字符，且长度为 <code>n</code>&nbsp;的字符串。</p>

<p>假如在该字符串中，这四个字符都恰好出现&nbsp;<code>n/4</code>&nbsp;次，那么它就是一个「平衡字符串」。</p>

<p>&nbsp;</p>

<p>给你一个这样的字符串 <code>s</code>，请通过「替换一个子串」的方式，使原字符串 <code>s</code> 变成一个「平衡字符串」。</p>

<p>你可以用和「待替换子串」长度相同的&nbsp;<strong>任何</strong> 其他字符串来完成替换。</p>

<p>请返回待替换子串的最小可能长度。</p>

<p>如果原字符串自身就是一个平衡字符串，则返回 <code>0</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;QWER&quot;
<strong>输出：</strong>0
<strong>解释：</strong>s 已经是平衡的了。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;QQWE&quot;
<strong>输出：</strong>1
<strong>解释：</strong>我们需要把一个 &#39;Q&#39; 替换成 &#39;R&#39;，这样得到的 &quot;RQWE&quot; (或 &quot;QRWE&quot;) 是平衡的。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;QQQW&quot;
<strong>输出：</strong>2
<strong>解释：</strong>我们可以把前面的 &quot;QQ&quot; 替换成 &quot;ER&quot;。 
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>s = &quot;QQQQ&quot;
<strong>输出：</strong>3
<strong>解释：</strong>我们可以替换后 3 个 &#39;Q&#39;，使 s = &quot;QWER&quot;。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10^5</code></li>
	<li><code>s.length</code>&nbsp;是&nbsp;<code>4</code>&nbsp;的倍数</li>
	<li><code>s</code>&nbsp;中只含有&nbsp;<code>&#39;Q&#39;</code>, <code>&#39;W&#39;</code>, <code>&#39;E&#39;</code>,&nbsp;<code>&#39;R&#39;</code>&nbsp;四种字符</li>
</ul>

