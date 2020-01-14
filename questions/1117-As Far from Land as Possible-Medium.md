#### 地图分析/As Far from Land as Possible
**难度：** 中等/Medium

**Question：** 

<p>Given an N x N <code>grid</code>&nbsp;containing only values <code>0</code> and <code>1</code>, where&nbsp;<code>0</code> represents water&nbsp;and <code>1</code> represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.</p>

<p>The distance used in this problem is the <em>Manhattan distance</em>:&nbsp;the distance between two cells <code>(x0, y0)</code> and <code>(x1, y1)</code> is <code>|x0 - x1| + |y0 - y1|</code>.</p>

<p>If no land or water exists in the grid, return <code>-1</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/05/03/1336_ex1.JPG" style="width: 185px; height: 87px;" /></strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[1,0,1],[0,0,0],[1,0,1]]</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>
The cell (1, 1) is as far as possible from all the land with distance 2.
</pre>

<p><strong>Example 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/05/03/1336_ex2.JPG" style="width: 184px; height: 87px;" /></strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[[1,0,0],[0,0,0],[0,0,0]]</span>
<strong>Output: </strong><span id="example-output-2">4</span>
<strong>Explanation: </strong>
The cell (2, 2) is as far as possible from all the land with distance 4.
</pre>

<p>&nbsp;</p>

<p><span><strong>Note:</strong></span></p>

<ol>
	<li><span><code>1 &lt;= grid.length == grid[0].length&nbsp;&lt;= 100</code></span></li>
	<li><span><code>grid[i][j]</code>&nbsp;is <code>0</code> or <code>1</code></span></li>
</ol>


------

**题目：** 
<p>你现在手里有一份大小为&nbsp;N x N 的『地图』（网格）&nbsp;<code>grid</code>，上面的每个『区域』（单元格）都用&nbsp;<code>0</code>&nbsp;和&nbsp;<code>1</code>&nbsp;标记好了。其中&nbsp;<code>0</code>&nbsp;代表海洋，<code>1</code>&nbsp;代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。</p>

<p>我们这里说的距离是『曼哈顿距离』（&nbsp;Manhattan Distance）：<code>(x0, y0)</code> 和&nbsp;<code>(x1, y1)</code>&nbsp;这两个区域之间的距离是&nbsp;<code>|x0 - x1| + |y0 - y1|</code>&nbsp;。</p>

<p>如果我们的地图上只有陆地或者海洋，请返回&nbsp;<code>-1</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/08/17/1336_ex1.jpeg" style="height: 87px; width: 185px;"></strong></p>

<pre><strong>输入：</strong>[[1,0,1],[0,0,0],[1,0,1]]
<strong>输出：</strong>2
<strong>解释： </strong>
海洋区域 (1, 1) 和所有陆地区域之间的距离都达到最大，最大距离为 2。
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/08/17/1336_ex2.jpeg" style="height: 87px; width: 184px;"></strong></p>

<pre><strong>输入：</strong>[[1,0,0],[0,0,0],[0,0,0]]
<strong>输出：</strong>4
<strong>解释： </strong>
海洋区域 (2, 2) 和所有陆地区域之间的距离都达到最大，最大距离为 4。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= grid.length == grid[0].length&nbsp;&lt;= 100</code></li>
	<li><code>grid[i][j]</code>&nbsp;不是&nbsp;<code>0</code>&nbsp;就是&nbsp;<code>1</code></li>
</ol>

