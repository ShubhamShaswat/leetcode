#### 坏了的计算器/Broken Calculator
**难度：** 中等/Medium

**Question：** 

<p>On a broken calculator that has a number showing on its display, we can perform two operations:</p>

<ul>
	<li><strong>Double</strong>: Multiply the number on the display by 2, or;</li>
	<li><strong>Decrement</strong>: Subtract 1 from the number on the display.</li>
</ul>

<p>Initially, the calculator is displaying the number <code>X</code>.</p>

<p>Return the minimum number of operations needed to display the number <code>Y</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>X = <span id="example-input-1-1">2</span>, Y = <span id="example-input-1-2">3</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>Use double operation and then decrement operation {2 -&gt; 4 -&gt; 3}.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>X = <span id="example-input-2-1">5</span>, Y = <span id="example-input-2-2">8</span>
<strong>Output: </strong><span id="example-output-2">2</span>
<strong>Explanation: </strong>Use decrement and then double {5 -&gt; 4 -&gt; 8}.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>X = <span id="example-input-3-1">3</span>, Y = <span id="example-input-3-2">10</span>
<strong>Output: </strong><span id="example-output-3">3</span>
<strong>Explanation: </strong> Use double, decrement and double {3 -&gt; 6 -&gt; 5 -&gt; 10}.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>X = <span id="example-input-4-1">1024</span>, Y = <span id="example-input-4-2">1</span>
<strong>Output: </strong><span id="example-output-4">1023</span>
<strong>Explanation: </strong>Use decrement operations 1023 times.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= X &lt;= 10^9</code></li>
	<li><code>1 &lt;= Y &lt;= 10^9</code></li>
</ol>

------

**题目：** 
<p>在显示着数字的坏计算器上，我们可以执行以下两种操作：</p>

<ul>
	<li><strong>双倍（Double）：</strong>将显示屏上的数字乘 2；</li>
	<li><strong>递减（Decrement）：</strong>将显示屏上的数字减 1 。</li>
</ul>

<p>最初，计算器显示数字&nbsp;<code>X</code>。</p>

<p>返回显示数字&nbsp;<code>Y</code>&nbsp;所需的最小操作数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>X = 2, Y = 3
<strong>输出：</strong>2
<strong>解释：</strong>先进行双倍运算，然后再进行递减运算 {2 -&gt; 4 -&gt; 3}.
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>X = 5, Y = 8
<strong>输出：</strong>2
<strong>解释：</strong>先递减，再双倍 {5 -&gt; 4 -&gt; 8}.
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>X = 3, Y = 10
<strong>输出：</strong>3
<strong>解释：</strong>先双倍，然后递减，再双倍 {3 -&gt; 6 -&gt; 5 -&gt; 10}.
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>X = 1024, Y = 1
<strong>输出：</strong>1023
<strong>解释：</strong>执行递减运算 1023 次
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= X &lt;= 10^9</code></li>
	<li><code>1 &lt;= Y &lt;= 10^9</code></li>
</ol>

