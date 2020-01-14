#### 找出给定方程的正整数解/Find Positive Integer Solution for a Given Equation
**难度：** 简单/Easy

**Question：** 

<p>Given a&nbsp;function&nbsp; <code>f(x, y)</code>&nbsp;and a value <code>z</code>, return all positive integer&nbsp;pairs <code>x</code> and <code>y</code> where <code>f(x,y) == z</code>.</p>

<p>The function is constantly increasing, i.e.:</p>

<ul>
	<li><code>f(x, y) &lt; f(x + 1, y)</code></li>
	<li><code>f(x, y) &lt; f(x, y + 1)</code></li>
</ul>

<p>The function interface is defined like this:&nbsp;</p>

<pre>
interface CustomFunction {
public:
&nbsp; // Returns positive integer f(x, y) for any given positive integer x and y.
&nbsp; int f(int x, int y);
};
</pre>

<p>For custom testing purposes you&#39;re given an integer <code>function_id</code> and a target <code>z</code> as input, where <code>function_id</code> represent one function from an secret internal list, on the examples you&#39;ll know only two functions from the list. &nbsp;</p>

<p>You may return the solutions in any order.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> function_id = 1, z = 5
<strong>Output:</strong> [[1,4],[2,3],[3,2],[4,1]]
<strong>Explanation:</strong>&nbsp;function_id = 1 means that f(x, y) = x + y</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> function_id = 2, z = 5
<strong>Output:</strong> [[1,5],[5,1]]
<strong>Explanation:</strong>&nbsp;function_id = 2 means that f(x, y) = x * y
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= function_id &lt;= 9</code></li>
	<li><code>1 &lt;= z &lt;= 100</code></li>
	<li>It&#39;s guaranteed that the solutions of <code>f(x, y) == z</code> will be on the range <code>1 &lt;= x, y &lt;= 1000</code></li>
	<li>It&#39;s also guaranteed that <code>f(x, y)</code> will fit in 32 bit signed integer if <code>1 &lt;= x, y &lt;= 1000</code></li>
</ul>


------

**题目：** 
<p>给出一个函数&nbsp;&nbsp;<code>f(x, y)</code>&nbsp;和一个目标结果&nbsp;<code>z</code>，请你计算方程&nbsp;<code>f(x,y) == z</code>&nbsp;所有可能的正整数 <strong>数对</strong>&nbsp;<code>x</code> 和 <code>y</code>。</p>

<p>给定函数是严格单调的，也就是说：</p>

<ul>
	<li><code>f(x, y) &lt; f(x + 1, y)</code></li>
	<li><code>f(x, y) &lt; f(x, y + 1)</code></li>
</ul>

<p>函数接口定义如下：</p>

<pre>interface CustomFunction {
public:
&nbsp; // Returns positive integer f(x, y) for any given positive integer x and y.
&nbsp; int f(int x, int y);
};
</pre>

<p>如果你想自定义测试，你可以输入整数&nbsp;<code>function_id</code>&nbsp;和一个目标结果&nbsp;<code>z</code>&nbsp;作为输入，其中&nbsp;<code>function_id</code>&nbsp;表示一个隐藏函数列表中的一个函数编号，题目只会告诉你列表中的 <code>2</code> 个函数。 &nbsp;</p>

<p>你可以将满足条件的 <strong>结果数对</strong> 按任意顺序返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>function_id = 1, z = 5
<strong>输出：</strong>[[1,4],[2,3],[3,2],[4,1]]
<strong>解释：</strong>function_id = 1 表示 f(x, y) = x + y</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>function_id = 2, z = 5
<strong>输出：</strong>[[1,5],[5,1]]
<strong>解释：</strong>function_id = 2 表示 f(x, y) = x * y
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= function_id &lt;= 9</code></li>
	<li><code>1 &lt;= z &lt;= 100</code></li>
	<li>题目保证&nbsp;<code>f(x, y) == z</code>&nbsp;的解处于&nbsp;<code>1 &lt;= x, y &lt;= 1000</code>&nbsp;的范围内。</li>
	<li>在 <code>1 &lt;= x, y &lt;= 1000</code>&nbsp;的前提下，题目保证&nbsp;<code>f(x, y)</code>&nbsp;是一个&nbsp;32 位有符号整数。</li>
</ul>

