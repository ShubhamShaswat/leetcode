#### 非重叠矩形中的随机点/Random Point in Non-overlapping Rectangles
**难度：** 中等/Medium

**Question：** 

<p>Given a list of <strong>non-overlapping</strong>&nbsp;axis-aligned rectangles <code>rects</code>, write a function <code>pick</code> which randomly and uniformily picks an <strong>integer point</strong> in the space&nbsp;covered by the rectangles.</p>

<p>Note:</p>

<ol>
	<li>An <strong>integer point</strong>&nbsp;is a point that has integer coordinates.&nbsp;</li>
	<li>A point&nbsp;on the perimeter&nbsp;of a rectangle is&nbsp;<strong>included</strong> in the space covered by the rectangles.&nbsp;</li>
	<li><code>i</code>th rectangle = <code>rects[i]</code> =&nbsp;<code>[x1,y1,x2,y2]</code>, where <code>[x1, y1]</code>&nbsp;are the integer coordinates of the bottom-left corner, and <code>[x2, y2]</code>&nbsp;are the integer coordinates of the top-right corner.</li>
	<li>length and width of each rectangle does not exceed <code>2000</code>.</li>
	<li><code>1 &lt;= rects.length&nbsp;&lt;= 100</code></li>
	<li><code>pick</code> return a point as an array of integer coordinates&nbsp;<code>[p_x, p_y]</code></li>
	<li><code>pick</code> is called at most <code>10000</code>&nbsp;times.</li>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: 
</strong><span id="example-input-1-1">[&quot;Solution&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;]
</span><span id="example-input-1-2">[[[[1,1,5,5]]],[],[],[]]</span>
<strong>Output: 
</strong><span id="example-output-1">[null,[4,1],[4,1],[3,3]]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: 
</strong><span id="example-input-2-1">[&quot;Solution&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;]
</span><span id="example-input-2-2">[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]</span>
<strong>Output: 
</strong><span id="example-output-2">[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]</span></pre>
</div>

<div>
<p><strong>Explanation of Input Syntax:</strong></p>

<p>The input is two lists:&nbsp;the subroutines called&nbsp;and their&nbsp;arguments.&nbsp;<code>Solution</code>&#39;s&nbsp;constructor has one argument, the array of rectangles <code>rects</code>. <code>pick</code>&nbsp;has no arguments.&nbsp;Arguments&nbsp;are&nbsp;always wrapped with a list, even if there aren&#39;t any.</p>
</div>
</div>

<div>
<div>&nbsp;</div>
</div>


------

**题目：** 
<p>给定一个非重叠轴对齐矩形的列表 <code>rects</code>，写一个函数 <code>pick</code> 随机均匀地选取矩形覆盖的空间中的整数点。</p>

<p>提示：</p>

<ol>
	<li><strong>整数点</strong>是具有整数坐标的点。</li>
	<li>矩形周边上的点包含在矩形覆盖的空间中。</li>
	<li>第 <code>i</code> 个矩形 <code>rects [i] = [x1，y1，x2，y2]</code>，其中&nbsp;<code>[x1，y1]</code> 是左下角的整数坐标，<code>[x2，y2]</code> 是右上角的整数坐标。</li>
	<li>每个矩形的长度和宽度不超过 2000。</li>
	<li><code>1 &lt;= rects.length&nbsp;&lt;= 100</code></li>
	<li><code>pick</code> 以整数坐标数组&nbsp;<code>[p_x, p_y]</code>&nbsp;的形式返回一个点。</li>
	<li><code>pick</code> 最多被调用10000次。</li>
</ol>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入: 
</strong>[&quot;Solution&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;]
[[[[1,1,5,5]]],[],[],[]]
<strong>输出: 
</strong>[null,[4,1],[4,1],[3,3]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入: 
</strong>[&quot;Solution&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
<strong>输出: 
</strong>[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]</pre>

<p>&nbsp;</p>

<p><strong>输入语法的说明：</strong></p>

<p>输入是两个列表：调用的子例程及其参数。<code>Solution</code> 的构造函数有一个参数，即矩形数组 <code>rects</code>。<code>pick</code> 没有参数。参数总是用列表包装的，即使没有也是如此。</p>

<p>&nbsp;</p>

