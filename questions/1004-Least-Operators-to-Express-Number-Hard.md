#### 表示数字的最少运算符/Least Operators to Express Number
**难度：** 困难/Hard

**Question：** 

<p>Given a single positive integer <code>x</code>, we will write an expression of the form <code>x (op1) x (op2) x (op3) x ...</code>&nbsp;where each operator <code>op1</code>, <code>op2</code>, etc. is either addition, subtraction, multiplication, or division (<code>+</code>, <code>-</code>, <code>*</code>, or <code>/)</code>.&nbsp; For example, with <code>x = 3</code>, we might write <code>3 * 3 / 3 + 3 - 3</code>&nbsp;which is a value of <font face="monospace">3</font>.</p>

<p>When writing such an expression, we adhere to the following conventions:</p>

<ol>
	<li>The division operator (<code>/</code>) returns rational numbers.</li>
	<li>There are no parentheses placed anywhere.</li>
	<li>We use the usual order of operations: multiplication and division happens before addition and subtraction.</li>
	<li>It&#39;s not allowed to use the unary negation&nbsp;operator (<code>-</code>).&nbsp; For example, &quot;<code>x&nbsp;- x</code>&quot;&nbsp;is a valid expression as it only uses subtraction, but &quot;<code>-x +&nbsp;x</code>&quot; is not because it uses negation.</li>
</ol>

<p>We would like to write an expression with the least number of operators such that the expression equals the given <code>target</code>.&nbsp; Return the least number of operators used.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>x = <span id="example-input-1-1">3</span>, target = <span id="example-input-1-2">19</span>
<strong>Output: </strong><span id="example-output-1">5</span>
<strong>Explanation: </strong><span id="example-output-1">3 * 3 + 3 * 3 + 3 / 3.  The expression contains 5 operations.</span>
</pre>

<p><strong>Example 2:</strong></p>

<div>
<pre>
<strong>Input: </strong>x = <span id="example-input-2-1">5</span>, target = <span id="example-input-2-2">501</span>
<strong>Output: </strong><span id="example-output-2">8</span>
<strong>Explanation: </strong><span id="example-output-1">5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.  The expression contains 8 operations.</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>x = <span id="example-input-3-1">100</span>, target = <span id="example-input-3-2">100000000</span>
<strong>Output: </strong><span id="example-output-3">3</span>
<strong>Explanation: </strong><span id="example-output-1">100 * 100 * 100 * 100.  The expression contains 3 operations.</span></pre>

<p>&nbsp;</p>
</div>
</div>
</div>

<p><strong>Note:</strong></p>

<ul>
	<li><code>2 &lt;= x &lt;= 100</code></li>
	<li><code>1 &lt;= target &lt;= 2 * 10^8</code></li>
</ul>

<div>
<div>
<div>&nbsp;</div>
</div>
</div>


------

**题目：** 
<p>给定一个正整数 <code>x</code>，我们将会写出一个形如&nbsp;<code>x (op1) x (op2) x (op3) x ...</code>&nbsp;的表达式，其中每个运算符&nbsp;<code>op1</code>，<code>op2</code>，&hellip; 可以是加、减、乘、除（<code>+</code>，<code>-</code>，<code>*</code>，或是&nbsp;<code>/</code>）之一。例如，对于&nbsp;<code>x = 3</code>，我们可以写出表达式&nbsp;<code>3 * 3 / 3 + 3 - 3</code>，该式的值为 3 。</p>

<p>在写这样的表达式时，我们需要遵守下面的惯例：</p>

<ol>
	<li>除运算符（<code>/</code>）返回有理数。</li>
	<li>任何地方都没有括号。</li>
	<li>我们使用通常的操作顺序：乘法和除法发生在加法和减法之前。</li>
	<li>不允许使用一元否定运算符（<code>-</code>）。例如，&ldquo;<code>x - x</code>&rdquo; 是一个有效的表达式，因为它只使用减法，但是 &ldquo;<code>-x + x</code>&rdquo; 不是，因为它使用了否定运算符。&nbsp;</li>
</ol>

<p>我们希望编写一个能使表达式等于给定的目标值 <code>target</code> 且运算符最少的表达式。返回所用运算符的最少数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>x = 3, target = 19
<strong>输出：</strong>5
<strong>解释：</strong>3 * 3 + 3 * 3 + 3 / 3 。表达式包含 5 个运算符。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>x = 5, target = 501
<strong>输出：</strong>8
<strong>解释：</strong>5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5 。表达式包含 8 个运算符。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>x = 100, target = 100000000
<strong>输出：</strong>3
<strong>解释：</strong>100 * 100 * 100 * 100 。表达式包含 3 个运算符。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= x &lt;= 100</code></li>
	<li><code>1 &lt;= target &lt;= 2 * 10^8</code></li>
</ul>

<p>&nbsp;</p>

