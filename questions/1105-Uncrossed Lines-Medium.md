#### 不相交的线/Uncrossed Lines
**难度：** 中等/Medium

**Question：** 

<p>We write the integers of <code>A</code> and <code>B</code>&nbsp;(in the order they are given) on two separate horizontal lines.</p>

<p>Now, we may draw <em>connecting lines</em>: a straight line connecting two numbers <code>A[i]</code> and <code>B[j]</code>&nbsp;such that:</p>

<ul>
	<li><code>A[i] == B[j]</code>;</li>
	<li>The line we draw does not intersect any other connecting (non-horizontal) line.</li>
</ul>

<p>Note that a connecting lines cannot intersect even at the endpoints:&nbsp;each number can only belong to one connecting line.</p>

<p>Return the maximum number of connecting lines we can draw in this way.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/04/26/142.png" style="width: 100px; height: 72px;" />
<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1,4,2]</span>, B = <span id="example-input-1-2">[1,2,4]</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[2,5,1,2,5]</span>, B = <span id="example-input-2-2">[10,5,2,1,5,2]</span>
<strong>Output: </strong><span id="example-output-2">3</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">[1,3,7,1,7,5]</span>, B = <span id="example-input-3-2">[1,9,2,5,1]</span>
<strong>Output: </strong><span id="example-output-3">2</span></pre>

<p>&nbsp;</p>
</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 500</code></li>
	<li><code>1 &lt;= B.length &lt;= 500</code></li>
	<li><code><font face="monospace">1 &lt;= A[i], B[i] &lt;= 2000</font></code></li>
</ol>


------

**题目：** 
<p>我们在两条独立的水平线上按给定的顺序写下&nbsp;<code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;中的整数。</p>

<p>现在，我们可以绘制一些连接两个数字&nbsp;<code>A[i]</code>&nbsp;和&nbsp;<code>B[j]</code>&nbsp;的直线，只要&nbsp;<code>A[i] == B[j]</code>，且我们绘制的直线不与任何其他连线（非水平线）相交。</p>

<p>以这种方法绘制线条，并返回我们可以绘制的最大连线数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/04/28/142.png" style="height: 72px; width: 100px;"></strong></p>

<pre><strong>输入：</strong>A = [1,4,2], B = [1,2,4]
<strong>输出：</strong>2
<strong>解释：
</strong>我们可以画出两条不交叉的线，如上图所示。
我们无法画出第三条不相交的直线，因为从 A[1]=4 到 B[2]=4 的直线将与从 A[2]=2 到 B[1]=2 的直线相交。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>A = [2,5,1,2,5], B = [10,5,2,1,5,2]
<strong>输出：</strong>3
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>A = [1,3,7,1,7,5], B = [1,9,2,5,1]
<strong>输出：</strong>2</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 500</code></li>
	<li><code>1 &lt;= B.length &lt;= 500</code></li>
	<li><code>1 &lt;= A[i], B[i] &lt;= 2000</code></li>
</ol>

<p>&nbsp;</p>

