#### 矩形区域不超过 K 的最大数值和/Max Sum of Rectangle No Larger Than K
**难度：** 困难/Hard

**Question：** 

<p>Given a non-empty 2D matrix <i>matrix</i> and an integer <i>k</i>, find the max sum of a rectangle in the <i>matrix</i> such that its sum is no larger than <i>k</i>.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input: </strong>matrix = <span id="example-input-1-1">[[1,0,1],[0,-2,3]]</span>, k = <span id="example-input-1-2">2</span>
<strong>Output: </strong><span id="example-output-1">2 
<strong>Explanation:</strong></span>&nbsp;Because the sum of rectangle <code>[[0, 1], [-2, 3]]</code> is 2,
&nbsp;            and 2 is the max number no larger than k (k = 2).</pre>

<p><b>Note:</b></p>

<ol>
	<li>The rectangle inside the matrix must have an area &gt; 0.</li>
	<li>What if the number of rows is much larger than the number of columns?</li>
</ol>

------

**题目：** 
<p>给定一个非空二维矩阵&nbsp;<em>matrix&nbsp;</em>和一个整数<em> k</em>，找到这个矩阵内部不大于 <em>k</em> 的最大矩形和。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入: </strong>matrix = [[1,0,1],[0,-2,3]], k = 2
<strong>输出: </strong>2 
<strong>解释:</strong>&nbsp;矩形区域&nbsp;<code>[[0, 1], [-2, 3]]</code>&nbsp;的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
</pre>

<p><strong>说明：</strong></p>

<ol>
	<li>矩阵内的矩形区域面积必须大于 0。</li>
	<li>如果行数远大于列数，你将如何解答呢？</li>
</ol>

