#### 花括号展开 II/Brace Expansion II
**难度：** 困难/Hard

**Question：** 

<p>Under a grammar given below, strings can represent a set of lowercase words.&nbsp; Let&#39;s&nbsp;use <code>R(expr)</code>&nbsp;to denote the <strong>set</strong> of words the expression represents.</p>

<p>Grammar can best be understood through simple examples:</p>

<ul>
	<li>Single letters represent a singleton set containing that word.
	<ul>
		<li><code>R(&quot;a&quot;) = {&quot;a&quot;}</code></li>
		<li><code>R(&quot;w&quot;) = {&quot;w&quot;}</code></li>
	</ul>
	</li>
	<li>When we take a comma delimited list of 2 or more expressions, we take the union of possibilities.
	<ul>
		<li><code>R(&quot;{a,b,c}&quot;) = {&quot;a&quot;,&quot;b&quot;,&quot;c&quot;}</code></li>
		<li><code>R(&quot;{{a,b},{b,c}}&quot;) = {&quot;a&quot;,&quot;b&quot;,&quot;c&quot;}</code>&nbsp;(notice the final set only contains each word at most once)</li>
	</ul>
	</li>
	<li>When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
	<ul>
		<li><code>R(&quot;{a,b}{c,d}&quot;) = {&quot;ac&quot;,&quot;ad&quot;,&quot;bc&quot;,&quot;bd&quot;}</code></li>
		<li><code>R(&quot;a{b,c}{d,e}f{g,h}&quot;)&nbsp;= {&quot;abdfg&quot;, &quot;abdfh&quot;, &quot;abefg&quot;, &quot;abefh&quot;, &quot;acdfg&quot;, &quot;acdfh&quot;, &quot;acefg&quot;, &quot;acefh&quot;}</code></li>
	</ul>
	</li>
</ul>

<p>Formally, the 3 rules for our grammar:</p>

<ul>
	<li>For every lowercase letter <code>x</code>, we have <code>R(x) = {x}</code></li>
	<li>For expressions <code>e_1, e_2, ... , e_k</code>&nbsp;with <code>k &gt;= 2</code>, we have <code>R({e_1,e_2,...}) = R(e_1)&nbsp;&cup; R(e_2)&nbsp;&cup; ...</code></li>
	<li>For&nbsp;expressions <code>e_1</code> and <code>e_2</code>, we have <code>R(e_1 + e_2) = {a + b for (a, b) in&nbsp;R(e_1)&nbsp;&times; R(e_2)}</code>, where + denotes concatenation, and &times; denotes the cartesian product.</li>
</ul>

<p>Given an <code>expression</code> representing a set of words under the given grammar, return the&nbsp;sorted list of words that the expression represents.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;{a,b}{c,{d,e}}&quot;</span>
<strong>Output: </strong><span id="example-output-1">[&quot;ac&quot;,&quot;ad&quot;,&quot;ae&quot;,&quot;bc&quot;,&quot;bd&quot;,&quot;be&quot;]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span>&quot;{{a,z},a{b,c},{ab,z}}&quot;</span>
<strong>Output: </strong><span>[&quot;a&quot;,&quot;ab&quot;,&quot;ac&quot;,&quot;z&quot;]</span>
<strong>Explanation: </strong>Each distinct word is written only once in the final answer.
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ol>
	<li><code>1 &lt;= expression.length &lt;= 60</code></li>
	<li><code>expression[i]</code> consists of <code>&#39;{&#39;</code>, <code>&#39;}&#39;</code>, <code>&#39;,&#39;</code>or lowercase English letters.</li>
	<li>The given&nbsp;<code>expression</code>&nbsp;represents a set of words based on the grammar given in the description.</li>
</ol>
</div>
</div>


------

**题目：** 
<p>如果你熟悉 Shell 编程，那么一定了解过花括号展开，它可以用来生成任意字符串。</p>

<p>花括号展开的表达式可以看作一个由 <strong>花括号</strong>、<strong>逗号</strong> 和 <strong>小写英文字母</strong> 组成的字符串，定义下面几条语法规则：</p>

<ul>
	<li>如果只给出单一的元素&nbsp;<code>x</code>，那么表达式表示的字符串就只有&nbsp;<code>&quot;x&quot;</code>。&nbsp;

	<ul>
		<li>例如，表达式 <code>{a}</code>&nbsp;表示字符串 <code>&quot;a&quot;</code>。</li>
		<li>而表达式 <code>{ab}</code>&nbsp;就表示字符串 <code>&quot;ab&quot;</code>。</li>
	</ul>
	</li>
	<li>当两个或多个表达式并列，以逗号分隔时，我们取这些表达式中元素的并集。
	<ul>
		<li>例如，表达式&nbsp;<code>{a,b,c}</code> 表示字符串&nbsp;<code>&quot;a&quot;,&quot;b&quot;,&quot;c&quot;</code>。</li>
		<li>而表达式 <code>{a,b},{b,c}</code>&nbsp;也可以表示字符串&nbsp;<code>&quot;a&quot;,&quot;b&quot;,&quot;c&quot;</code>。</li>
	</ul>
	</li>
	<li>要是两个或多个表达式相接，中间没有隔开时，我们从这些表达式中各取一个元素依次连接形成字符串。
	<ul>
		<li>例如，表达式 <code>{a,b}{c,d}</code> 表示字符串&nbsp;<code>&quot;ac&quot;,&quot;ad&quot;,&quot;bc&quot;,&quot;bd&quot;</code>。</li>
	</ul>
	</li>
	<li>表达式之间允许嵌套，单一元素与表达式的连接也是允许的。
	<ul>
		<li>例如，表达式&nbsp;<code>a{b,c,d}</code> 表示字符串&nbsp;<code>&quot;ab&quot;,&quot;ac&quot;,&quot;ad&quot;​​​​​​</code>。</li>
		<li>例如，表达式&nbsp;<code>{a{b,c}}{{d,e}f{g,h}}</code> 可以代换为&nbsp;<code>{ab,ac}{dfg,dfh,efg,efh}</code>，表示字符串&nbsp;<code>&quot;abdfg&quot;, &quot;abdfh&quot;, &quot;abefg&quot;, &quot;abefh&quot;, &quot;acdfg&quot;, &quot;acdfh&quot;, &quot;acefg&quot;, &quot;acefh</code>&quot;。</li>
	</ul>
	</li>
</ul>

<p>给出表示基于给定语法规则的表达式&nbsp;<code>expression</code>，返回它所表示的所有字符串组成的有序列表。</p>

<p>假如你希望以「集合」的概念了解此题，也可以通过点击 &ldquo;<strong>显示英文描述</strong>&rdquo; 获取详情。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>&quot;{a,b}{c{d,e}}&quot;
<strong>输出：</strong>[&quot;acd&quot;,&quot;ace&quot;,&quot;bcd&quot;,&quot;bce&quot;]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>&quot;{{a,z}, a{b,c}, {ab,z}}&quot;
<strong>输出：</strong>[&quot;a&quot;,&quot;ab&quot;,&quot;ac&quot;,&quot;z&quot;]
<strong>解释：</strong>输出中 <strong>不应 </strong>出现重复的组合结果。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= expression.length &lt;= 50</code></li>
	<li><code>expression[i]</code> 由 <code>&#39;{&#39;</code>，<code>&#39;}&#39;</code>，<code>&#39;,&#39;</code>&nbsp;或小写英文字母组成</li>
	<li>给出的表达式&nbsp;<code>expression</code>&nbsp;用以表示一组基于题目描述中语法构造的字符串</li>
</ol>

