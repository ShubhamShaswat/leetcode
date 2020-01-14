#### 移除无效的括号/Minimum Remove to Make Valid Parentheses
**难度：** 中等/Medium

**Question：** 

<p>Given a string <font face="monospace">s</font>&nbsp;of&nbsp;<code>&#39;(&#39;</code>&nbsp;,&nbsp;<code>&#39;)&#39;</code>&nbsp;and lowercase English characters.&nbsp;</p>

<p>Your task is to remove the minimum number of parentheses (&nbsp;<code>&#39;(&#39;</code>&nbsp;or&nbsp;<code>&#39;)&#39;</code>,&nbsp;in any positions ) so that the resulting <em>parentheses string</em> is valid and return <strong>any</strong> valid string.</p>

<p>Formally, a <em>parentheses string</em> is valid if and only if:</p>

<ul>
	<li>It is the empty string, contains only lowercase characters, or</li>
	<li>It can be written as&nbsp;<code>AB</code>&nbsp;(<code>A</code>&nbsp;concatenated with&nbsp;<code>B</code>), where&nbsp;<code>A</code>&nbsp;and&nbsp;<code>B</code>&nbsp;are valid strings, or</li>
	<li>It can be written as&nbsp;<code>(A)</code>, where&nbsp;<code>A</code>&nbsp;is a valid string.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;lee(t(c)o)de)&quot;
<strong>Output:</strong> &quot;lee(t(c)o)de&quot;
<strong>Explanation:</strong> &quot;lee(t(co)de)&quot; , &quot;lee(t(c)ode)&quot; would also be accepted.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a)b(c)d&quot;
<strong>Output:</strong> &quot;ab(c)d&quot;
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;))((&quot;
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> An empty string is also valid.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(a(b(c)d)&quot;
<strong>Output:</strong> &quot;a(b(c)d)&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10^5</code></li>
	<li><code>s[i]</code>&nbsp;is one&nbsp;of&nbsp;&nbsp;<code>&#39;(&#39;</code> , <code>&#39;)&#39;</code> and&nbsp;lowercase English letters<code>.</code></li>
</ul>

------

**题目：** 
<p>给你一个由 <code>&#39;(&#39;</code>、<code>&#39;)&#39;</code> 和小写字母组成的字符串 <code>s</code>。</p>

<p>你需要从字符串中删除最少数目的 <code>&#39;(&#39;</code> 或者 <code>&#39;)&#39;</code>&nbsp;（可以删除任意位置的括号)，使得剩下的「括号字符串」有效。</p>

<p>请返回任意一个合法字符串。</p>

<p>有效「括号字符串」应当符合以下&nbsp;<strong>任意一条&nbsp;</strong>要求：</p>

<ul>
	<li>空字符串或只包含小写字母的字符串</li>
	<li>可以被写作&nbsp;<code>AB</code>（<code>A</code>&nbsp;连接&nbsp;<code>B</code>）的字符串，其中&nbsp;<code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;都是有效「括号字符串」</li>
	<li>可以被写作&nbsp;<code>(A)</code>&nbsp;的字符串，其中&nbsp;<code>A</code>&nbsp;是一个有效的「括号字符串」</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;lee(t(c)o)de)&quot;
<strong>输出：</strong>&quot;lee(t(c)o)de&quot;
<strong>解释：</strong>&quot;lee(t(co)de)&quot; , &quot;lee(t(c)ode)&quot; 也是一个可行答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;a)b(c)d&quot;
<strong>输出：</strong>&quot;ab(c)d&quot;
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;))((&quot;
<strong>输出：</strong>&quot;&quot;
<strong>解释：</strong>空字符串也是有效的
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>s = &quot;(a(b(c)d)&quot;
<strong>输出：</strong>&quot;a(b(c)d)&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10^5</code></li>
	<li><code>s[i]</code>&nbsp;可能是&nbsp;<code>&#39;(&#39;</code>、<code>&#39;)&#39;</code>&nbsp;或英文小写字母</li>
</ul>

