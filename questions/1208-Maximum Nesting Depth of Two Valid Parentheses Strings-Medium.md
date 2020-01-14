#### 有效括号的嵌套深度/Maximum Nesting Depth of Two Valid Parentheses Strings
**难度：** 中等/Medium

**Question：** 

<p>A string is a <em>valid parentheses string</em>&nbsp;(denoted VPS) if and only if it consists of <code>&quot;(&quot;</code> and <code>&quot;)&quot;</code> characters only, and:</p>

<ul>
	<li>It is the empty string, or</li>
	<li>It can be written as&nbsp;<code>AB</code>&nbsp;(<code>A</code>&nbsp;concatenated with&nbsp;<code>B</code>), where&nbsp;<code>A</code>&nbsp;and&nbsp;<code>B</code>&nbsp;are VPS&#39;s, or</li>
	<li>It can be written as&nbsp;<code>(A)</code>, where&nbsp;<code>A</code>&nbsp;is a VPS.</li>
</ul>

<p>We can&nbsp;similarly define the <em>nesting depth</em> <code>depth(S)</code> of any VPS <code>S</code> as follows:</p>

<ul>
	<li><code>depth(&quot;&quot;) = 0</code></li>
	<li><code>depth(A + B) = max(depth(A), depth(B))</code>, where <code>A</code> and <code>B</code> are VPS&#39;s</li>
	<li><code>depth(&quot;(&quot; + A + &quot;)&quot;) = 1 + depth(A)</code>, where <code>A</code> is a VPS.</li>
</ul>

<p>For example,&nbsp; <code>&quot;&quot;</code>,&nbsp;<code>&quot;()()&quot;</code>, and&nbsp;<code>&quot;()(()())&quot;</code>&nbsp;are VPS&#39;s (with nesting depths 0, 1, and 2), and <code>&quot;)(&quot;</code> and <code>&quot;(()&quot;</code> are not VPS&#39;s.</p>

<p>&nbsp;</p>

<p>Given a VPS <font face="monospace">seq</font>, split it into two disjoint subsequences <code>A</code> and <code>B</code>, such that&nbsp;<code>A</code> and <code>B</code> are VPS&#39;s (and&nbsp;<code>A.length + B.length = seq.length</code>).</p>

<p>Now choose <strong>any</strong> such <code>A</code> and <code>B</code> such that&nbsp;<code>max(depth(A), depth(B))</code> is the minimum possible value.</p>

<p>Return an <code>answer</code> array (of length <code>seq.length</code>) that encodes such a&nbsp;choice of <code>A</code> and <code>B</code>:&nbsp; <code>answer[i] = 0</code> if <code>seq[i]</code> is part of <code>A</code>, else <code>answer[i] = 1</code>.&nbsp; Note that even though multiple answers may exist, you may return any of them.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> seq = &quot;(()())&quot;
<strong>Output:</strong> [0,1,1,1,1,0]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> seq = &quot;()(())()&quot;
<strong>Output:</strong> [0,0,0,1,1,0,1,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= seq.size &lt;= 10000</code></li>
</ul>


------

**题目：** 
<p><strong>有效括号字符串</strong> 仅由&nbsp;<code>&quot;(&quot;</code> 和&nbsp;<code>&quot;)&quot;</code>&nbsp;构成，并符合下述几个条件之一：</p>

<ul>
	<li>空字符串</li>
	<li>连接，可以记作&nbsp;<code>AB</code>（<code>A</code> 与 <code>B</code> 连接），其中&nbsp;<code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;都是有效括号字符串</li>
	<li>嵌套，可以记作&nbsp;<code>(A)</code>，其中&nbsp;<code>A</code>&nbsp;是有效括号字符串</li>
</ul>

<p>类似地，我们可以定义任意有效括号字符串 <code>s</code> 的 <strong>嵌套深度</strong>&nbsp;<code>depth(S)</code>：</p>

<ul>
	<li><code>s</code> 为空时，<code>depth(&quot;&quot;) = 0</code></li>
	<li><code>s</code> 为 <code>A</code> 与 <code>B</code> 连接时，<code>depth(A + B) = max(depth(A), depth(B))</code>，其中&nbsp;<code>A</code> 和&nbsp;<code>B</code>&nbsp;都是有效括号字符串</li>
	<li><code>s</code> 为嵌套情况，<code>depth(&quot;(&quot; + A + &quot;)&quot;) = 1 + depth(A)</code>，其中 A 是有效括号字符串</li>
</ul>

<p>例如：<code>&quot;&quot;</code>，<code>&quot;()()&quot;</code>，和&nbsp;<code>&quot;()(()())&quot;</code>&nbsp;都是有效括号字符串，嵌套深度分别为 0，1，2，而&nbsp;<code>&quot;)(&quot;</code> 和&nbsp;<code>&quot;(()&quot;</code>&nbsp;都不是有效括号字符串。</p>

<p>&nbsp;</p>

<p>给你一个有效括号字符串 <code>seq</code>，将其分成两个不相交的子序列&nbsp;<code>A</code> 和&nbsp;<code>B</code>，且&nbsp;<code>A</code> 和&nbsp;<code>B</code>&nbsp;满足有效括号字符串的定义（注意：<code>A.length + B.length = seq.length</code>）。</p>

<p>现在，你需要从中选出 <strong>任意</strong>&nbsp;一组有效括号字符串&nbsp;<code>A</code> 和&nbsp;<code>B</code>，使&nbsp;<code>max(depth(A), depth(B))</code>&nbsp;的可能取值最小。</p>

<p>返回长度为&nbsp;<code>seq.length</code> 答案数组&nbsp;<code>answer</code>&nbsp;，选择&nbsp;<code>A</code>&nbsp;还是&nbsp;<code>B</code>&nbsp;的编码规则是：如果&nbsp;<code>seq[i]</code>&nbsp;是&nbsp;<code>A</code>&nbsp;的一部分，那么&nbsp;<code>answer[i] = 0</code>。否则，<code>answer[i] = 1</code>。即便有多个满足要求的答案存在，你也只需返回&nbsp;<strong>一个</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>seq = &quot;(()())&quot;
<strong>输出：</strong>[0,1,1,1,1,0]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>seq = &quot;()(())()&quot;
<strong>输出：</strong>[0,0,0,1,1,0,1,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= text.size &lt;= 10000</code></li>
</ul>

