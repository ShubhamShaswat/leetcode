#### 二进制矩阵中的最短路径/Shortest Path in Binary Matrix
**难度：** 中等/Medium

**Question：** 

<p>In an N by N square grid, each cell is either empty (0) or blocked (1).</p>

<p>A&nbsp;<em>clear&nbsp;path from top-left to bottom-right</em>&nbsp;has length <code>k</code> if and only if it is composed of cells <code>C_1, C_2, ..., C_k</code>&nbsp;such that:</p>

<ul>
	<li>Adjacent cells <code>C_i</code> and <code>C_{i+1}</code> are connected 8-directionally (ie., they are different and&nbsp;share an edge or corner)</li>
	<li><code>C_1</code> is at location <code>(0, 0)</code> (ie. has value <code>grid[0][0]</code>)</li>
	<li><code>C_k</code>&nbsp;is at location <code>(N-1, N-1)</code> (ie. has value <code>grid[N-1][N-1]</code>)</li>
	<li>If <code>C_i</code> is located at&nbsp;<code>(r, c)</code>, then <code>grid[r][c]</code> is empty (ie.&nbsp;<code>grid[r][c] ==&nbsp;0</code>).</li>
</ul>

<p>Return the length of the shortest such clear path from top-left to bottom-right.&nbsp; If such a path does not exist, return -1.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[0,1],[1,0]]
<img alt="" src="https://assets.leetcode.com/uploads/2019/08/04/example1_1.png" style="width: 151px; height: 152px;" />
</span>
<strong>Output: </strong>2
<img alt="" src="https://assets.leetcode.com/uploads/2019/08/04/example1_2.png" style="width: 151px; height: 152px;" />
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[[0,0,0],[1,1,0],[1,1,0]]
<img alt="" src="https://assets.leetcode.com/uploads/2019/08/04/example2_1.png" style="width: 151px; height: 152px;" />
</span>
<strong>Output:</strong> 4
<img alt="" src="https://assets.leetcode.com/uploads/2019/08/04/example2_2.png" style="width: 151px; height: 152px;" />
</pre>

<p>&nbsp;</p>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= grid.length == grid[0].length &lt;= 100</code></li>
	<li><code>grid[r][c]</code> is <code>0</code> or <code>1</code></li>
</ol>


------

**题目：** 
<p>在一个&nbsp;N &times;&nbsp;N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。</p>

<p>一条从左上角到右下角、长度为 <code>k</code> 的畅通路径，由满足下述条件的单元格&nbsp;<code>C_1, C_2, ..., C_k</code>&nbsp;组成：</p>

<ul>
	<li>相邻单元格&nbsp;<code>C_i</code> 和&nbsp;<code>C_{i+1}</code>&nbsp;在八个方向之一上连通（此时，<code>C_i</code> 和&nbsp;<code>C_{i+1}</code>&nbsp;不同且共享边或角）</li>
	<li><code>C_1</code> 位于&nbsp;<code>(0, 0)</code>（即，值为&nbsp;<code>grid[0][0]</code>）</li>
	<li><code>C_k</code>&nbsp;位于&nbsp;<code>(N-1, N-1)</code>（即，值为&nbsp;<code>grid[N-1][N-1]</code>）</li>
	<li>如果 <code>C_i</code> 位于&nbsp;<code>(r, c)</code>，则 <code>grid[r][c]</code>&nbsp;为空（即，<code>grid[r][c] ==&nbsp;0</code>）</li>
</ul>

<p>返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[[0,1],[1,0]]
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/06/16/example1_1.png" style="height: 151px; width: 150px;">
<strong>输出：</strong>2
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/06/16/example1_2.png" style="height: 151px; width: 150px;">
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[[0,0,0],[1,1,0],[1,1,0]]
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/06/16/example2_1.png" style="height: 146px; width: 150px;">
<strong>输出：</strong>4
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/06/16/example2_2.png" style="height: 151px; width: 150px;">
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= grid.length == grid[0].length &lt;= 100</code></li>
	<li><code>grid[i][j]</code> 为&nbsp;<code>0</code> 或&nbsp;<code>1</code></li>
</ol>

