#### 螺旋矩阵 III/Spiral Matrix III
**难度：** 中等/Medium

**Question：** 

<p>On a 2 dimensional grid with <code>R</code> rows and <code>C</code> columns, we start at <code>(r0, c0)</code> facing east.</p>

<p>Here, the north-west corner of the grid is at the&nbsp;first row and column, and the south-east corner of the grid is at the last row and column.</p>

<p>Now, we walk in a clockwise spiral shape to visit every position in this grid.&nbsp;</p>

<p>Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.)&nbsp;</p>

<p>Eventually, we reach all <code>R * C</code> spaces of the grid.</p>

<p>Return a list of coordinates representing the positions of the grid in the order they were visited.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>R = <span id="example-input-1-1">1</span>, C = <span id="example-input-1-2">4</span>, r0 = <span id="example-input-1-3">0</span>, c0 = <span id="example-input-1-4">0</span>
<strong>Output: </strong><span id="example-output-1">[[0,0],[0,1],[0,2],[0,3]]</span>

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_1.png" style="width: 174px; height: 99px;" />
</pre>

<p>&nbsp;</p>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>R = <span id="example-input-2-1">5</span>, C = <span id="example-input-2-2">6</span>, r0 = <span id="example-input-2-3">1</span>, c0 = <span id="example-input-2-4">4</span>
<strong>Output: </strong><span id="example-output-2">[[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]</span>

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_2.png" style="width: 202px; height: 142px;" />
</pre>

<div>
<div>
<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= R &lt;= 100</code></li>
	<li><code>1 &lt;= C &lt;= 100</code></li>
	<li><code>0 &lt;= r0 &lt; R</code></li>
	<li><code>0 &lt;= c0 &lt; C</code></li>
</ol>
</div>
</div>

------

**题目：** 
<p>在&nbsp;<code>R</code>&nbsp;行&nbsp;<code>C</code>&nbsp;列的矩阵上，我们从&nbsp;<code>(r0, c0)</code>&nbsp;面朝东面开始</p>

<p>这里，网格的西北角位于第一行第一列，网格的东南角位于最后一行最后一列。</p>

<p>现在，我们以顺时针按螺旋状行走，访问此网格中的每个位置。</p>

<p>每当我们移动到网格的边界之外时，我们会继续在网格之外行走（但稍后可能会返回到网格边界）。</p>

<p>最终，我们到过网格的所有&nbsp;<code>R * C</code>&nbsp;个空间。</p>

<p>按照访问顺序返回表示网格位置的坐标列表。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>R = 1, C = 4, r0 = 0, c0 = 0
<strong>输出：</strong>[[0,0],[0,1],[0,2],[0,3]]

<img alt="" src="https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/08/24/example_1.png" style="height: 99px; width: 174px;">
</pre>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>R = 5, C = 6, r0 = 1, c0 = 4
<strong>输出：</strong>[[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

<img alt="" src="https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/08/24/example_2.png" style="height: 142px; width: 202px;">
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= R &lt;= 100</code></li>
	<li><code>1 &lt;= C &lt;= 100</code></li>
	<li><code>0 &lt;= r0 &lt; R</code></li>
	<li><code>0 &lt;= c0 &lt; C</code></li>
</ol>

