#### 在圆内随机生成点/Generate Random Point in a Circle
**难度：** 中等/Medium

**Question：** 

<p>Given the radius and x-y positions of the center of a circle, write a function <code>randPoint</code>&nbsp;which&nbsp;generates a uniform random&nbsp;point in the circle.</p>

<p>Note:</p>

<ol>
	<li>input and output values are&nbsp;in&nbsp;<a href="https://www.webopedia.com/TERM/F/floating_point_number.html" target="_blank">floating-point</a>.</li>
	<li>radius and x-y position of the center of the circle is passed into the class constructor.</li>
	<li>a point on the circumference of the circle is considered to be&nbsp;in the circle.</li>
	<li><code>randPoint</code>&nbsp;returns&nbsp;a size 2 array containing x-position and y-position of the random point, in that order.</li>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: 
</strong><span id="example-input-1-1">[&quot;Solution&quot;,&quot;randPoint&quot;,&quot;randPoint&quot;,&quot;randPoint&quot;]
</span><span id="example-input-1-2">[[1,0,0],[],[],[]]</span>
<strong>Output: </strong><span id="example-output-1">[null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: 
</strong><span id="example-input-2-1">[&quot;Solution&quot;,&quot;randPoint&quot;,&quot;randPoint&quot;,&quot;randPoint&quot;]
</span><span id="example-input-2-2">[[10,5,-7.5],[],[],[]]</span>
<strong>Output: </strong><span id="example-output-2">[null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]</span></pre>
</div>

<p><strong>Explanation of Input Syntax:</strong></p>

<p>The input is two lists:&nbsp;the subroutines called&nbsp;and their&nbsp;arguments.&nbsp;<code>Solution</code>&#39;s&nbsp;constructor has three arguments, the radius, x-position of the center, and y-position of the center of the circle. <code>randPoint</code> has no arguments.&nbsp;Arguments&nbsp;are&nbsp;always wrapped with a list, even if there aren&#39;t any.</p>
</div>


------

**题目：** 
<p>给定圆的半径和圆心的 x、y 坐标，写一个在圆中产生均匀随机点的函数&nbsp;<code>randPoint</code>&nbsp;。</p>

<p>说明:</p>

<ol>
	<li>输入值和输出值都将是<a href="https://baike.baidu.com/item/%E6%B5%AE%E7%82%B9%E6%95%B0/6162520">浮点数</a>。</li>
	<li>圆的半径和圆心的 x、y 坐标将作为参数传递给类的构造函数。</li>
	<li>圆周上的点也认为是在圆中。</li>
	<li><code>randPoint</code>&nbsp;返回一个包含随机点的x坐标和y坐标的大小为2的数组。</li>
</ol>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入: 
</strong>[&quot;Solution&quot;,&quot;randPoint&quot;,&quot;randPoint&quot;,&quot;randPoint&quot;]
[[1,0,0],[],[],[]]
<strong>输出: </strong>[null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入: 
</strong>[&quot;Solution&quot;,&quot;randPoint&quot;,&quot;randPoint&quot;,&quot;randPoint&quot;]
[[10,5,-7.5],[],[],[]]
<strong>输出: </strong>[null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]</pre>

<p><strong>输入语法说明：</strong></p>

<p>输入是两个列表：调用成员函数名和调用的参数。<code>Solution</code>&nbsp;的构造函数有三个参数，圆的半径、圆心的 x 坐标、圆心的 y 坐标。<code>randPoint</code>&nbsp;没有参数。输入参数是一个列表，即使参数为空，也会输入一个 [] 空列表。</p>

