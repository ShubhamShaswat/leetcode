#### 随机翻转矩阵/Random Flip Matrix
**难度：** 中等/Medium

**Question：** 

<p>You are given the number of rows <code>n_rows</code>&nbsp;and number of columns <code>n_cols</code>&nbsp;of a&nbsp;2D&nbsp;binary matrix&nbsp;where all values are initially 0.&nbsp;Write a function <code>flip</code>&nbsp;which chooses&nbsp;a 0 value&nbsp;<a href="https://en.wikipedia.org/wiki/Discrete_uniform_distribution" target="_blank">uniformly at random</a>,&nbsp;changes it to 1,&nbsp;and then returns the position <code>[row.id, col.id]</code> of that value. Also, write a function <code>reset</code> which sets all values back to 0.&nbsp;<strong>Try to minimize the number of calls to system&#39;s Math.random()</strong> and optimize the time and&nbsp;space complexity.</p>

<p>Note:</p>

<ol>
	<li><code>1 &lt;= n_rows, n_cols&nbsp;&lt;= 10000</code></li>
	<li><code>0 &lt;= row.id &lt; n_rows</code> and <code>0 &lt;= col.id &lt; n_cols</code></li>
	<li><code>flip</code>&nbsp;will not be called when the matrix has no&nbsp;0 values left.</li>
	<li>the total number of calls to&nbsp;<code>flip</code>&nbsp;and <code>reset</code>&nbsp;will not exceed&nbsp;1000.</li>
</ol>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: 
</strong><span id="example-input-1-1">[&quot;Solution&quot;,&quot;flip&quot;,&quot;flip&quot;,&quot;flip&quot;,&quot;flip&quot;]
</span><span id="example-input-1-2">[[2,3],[],[],[],[]]</span>
<strong>Output: </strong><span id="example-output-1">[null,[0,1],[1,2],[1,0],[1,1]]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: 
</strong><span id="example-input-2-1">[&quot;Solution&quot;,&quot;flip&quot;,&quot;flip&quot;,&quot;reset&quot;,&quot;flip&quot;]
</span><span id="example-input-2-2">[[1,2],[],[],[],[]]</span>
<strong>Output: </strong><span id="example-output-2">[null,[0,0],[0,1],null,[0,0]]</span></pre>
</div>

<p><strong>Explanation of Input Syntax:</strong></p>

<p>The input is two lists:&nbsp;the subroutines called&nbsp;and their&nbsp;arguments. <code>Solution</code>&#39;s constructor&nbsp;has two arguments, <code>n_rows</code> and <code>n_cols</code>.&nbsp;<code>flip</code>&nbsp;and <code>reset</code> have&nbsp;no&nbsp;arguments.&nbsp;Arguments&nbsp;are&nbsp;always wrapped with a list, even if there aren&#39;t any.</p>


------

**题目：** 
<p>题中给出一个 <code>n</code> 行 <code>n</code> 列的二维矩阵<code> (n_rows,n_cols)</code>，且所有值被初始化为 0。要求编写一个 <code>flip</code> 函数，<a href="https://en.wikipedia.org/wiki/Discrete_uniform_distribution">均匀随机</a>的将矩阵中的 0 变为 1，并返回该值的位置下标 <code>[row_id,col_id]</code>；同样编写一个 <code>reset</code> 函数，将所有的值都重新置为 0。<strong>尽量最少调用随机函数 Math.random()</strong>，并且优化时间和空间复杂度。</p>

<p>注意:</p>

<p>1.1 &lt;= n_rows, n_cols &lt;= 10000</p>

<p>2. 0 &lt;= row.id &lt; n_rows 并且 0 &lt;= col.id &lt; n_cols</p>

<p>3.当矩阵中没有值为 0 时，不可以调用 flip 函数</p>

<p>4.调用 flip 和 reset 函数的次数加起来不会超过 1000 次</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入: 
</strong>[&quot;Solution&quot;,&quot;flip&quot;,&quot;flip&quot;,&quot;flip&quot;,&quot;flip&quot;]
[[2,3],[],[],[],[]]
<strong>输出: </strong>[null,[0,1],[1,2],[1,0],[1,1]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入: 
</strong>[&quot;Solution&quot;,&quot;flip&quot;,&quot;flip&quot;,&quot;reset&quot;,&quot;flip&quot;]
[[1,2],[],[],[],[]]
<strong>输出: </strong>[null,[0,0],[0,1],null,[0,0]]</pre>

<p><strong>输入语法解释：</strong></p>

<p>输入包含两个列表：被调用的子程序和他们的参数。<code>Solution</code> 的构造函数有两个参数，分别为 <code>n_rows</code> 和 <code>n_cols</code>。<code>flip</code>&nbsp;和 <code>reset</code> 没有参数，参数总会以列表形式给出，哪怕该列表为空</p>

