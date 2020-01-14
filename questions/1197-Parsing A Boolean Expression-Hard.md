#### 解析布尔表达式/Parsing A Boolean Expression
**难度：** 困难/Hard

**Question：** 

<p>Return the result of evaluating a given boolean <code>expression</code>, represented as a string.</p>

<p>An expression can either be:</p>

<ul>
	<li><code>&quot;t&quot;</code>, evaluating to <code>True</code>;</li>
	<li><code>&quot;f&quot;</code>, evaluating to <code>False</code>;</li>
	<li><code>&quot;!(expr)&quot;</code>, evaluating to the logical NOT of the inner expression <code>expr</code>;</li>
	<li><code>&quot;&amp;(expr1,expr2,...)&quot;</code>, evaluating to the logical AND of 2 or more inner expressions <code>expr1, expr2, ...</code>;</li>
	<li><code>&quot;|(expr1,expr2,...)&quot;</code>, evaluating to the logical OR of 2 or more inner expressions <code>expr1, expr2, ...</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> expression = &quot;!(f)&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> expression = &quot;|(f,t)&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> expression = &quot;&amp;(t,f)&quot;
<strong>Output:</strong> false
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> expression = &quot;|(&amp;(t,f,t),!(t))&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= expression.length &lt;= 20000</code></li>
	<li><code>expression[i]</code>&nbsp;consists of characters in <code>{&#39;(&#39;, &#39;)&#39;, &#39;&amp;&#39;, &#39;|&#39;, &#39;!&#39;, &#39;t&#39;, &#39;f&#39;, &#39;,&#39;}</code>.</li>
	<li><code>expression</code> is a valid expression representing a boolean, as given in the description.</li>
</ul>


------

**题目：** 
<p>给你一个以字符串形式表述的&nbsp;<a href="https://baike.baidu.com/item/%E5%B8%83%E5%B0%94%E8%A1%A8%E8%BE%BE%E5%BC%8F/1574380?fr=aladdin" target="_blank">布尔表达式</a>（boolean） <code>expression</code>，返回该式的运算结果。</p>

<p>有效的表达式需遵循以下约定：</p>

<ul>
	<li><code>&quot;t&quot;</code>，运算结果为 <code>True</code></li>
	<li><code>&quot;f&quot;</code>，运算结果为 <code>False</code></li>
	<li><code>&quot;!(expr)&quot;</code>，运算过程为对内部表达式 <code>expr</code> 进行逻辑 <strong>非的运算</strong>（NOT）</li>
	<li><code>&quot;&amp;(expr1,expr2,...)&quot;</code>，运算过程为对 2 个或以上内部表达式 <code>expr1, expr2, ...</code> 进行逻辑 <strong>与的运算</strong>（AND）</li>
	<li><code>&quot;|(expr1,expr2,...)&quot;</code>，运算过程为对 2 个或以上内部表达式 <code>expr1, expr2, ...</code> 进行逻辑 <strong>或的运算</strong>（OR）</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>expression = &quot;!(f)&quot;
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>expression = &quot;|(f,t)&quot;
<strong>输出：</strong>true
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>expression = &quot;&amp;(t,f)&quot;
<strong>输出：</strong>false
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>expression = &quot;|(&amp;(t,f,t),!(t))&quot;
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= expression.length &lt;= 20000</code></li>
	<li><code>expression[i]</code> 由 <code>{&#39;(&#39;, &#39;)&#39;, &#39;&amp;&#39;, &#39;|&#39;, &#39;!&#39;, &#39;t&#39;, &#39;f&#39;, &#39;,&#39;}</code> 中的字符组成。</li>
	<li><code>expression</code> 是以上述形式给出的有效表达式，表示一个布尔值。</li>
</ul>

