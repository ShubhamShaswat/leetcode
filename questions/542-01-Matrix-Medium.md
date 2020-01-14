#### 01 矩阵/01 Matrix
**难度：** 中等/Medium

**Question：** 

<p>Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.</p>

<p>The distance between two adjacent cells is 1.</p>

<p>&nbsp;</p>

<p><b>Example 1: </b></p>

<pre>
<strong>Input:</strong>
[[0,0,0],
 [0,1,0],
 [0,0,0]]

<strong>Output:</strong>
[[0,0,0],
&nbsp;[0,1,0],
&nbsp;[0,0,0]]
</pre>

<p><b>Example 2: </b></p>

<pre>
<b>Input:</b>
[[0,0,0],
 [0,1,0],
 [1,1,1]]

<strong>Output:</strong>
[[0,0,0],
 [0,1,0],
 [1,2,1]]
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The number of elements of the given matrix will not exceed 10,000.</li>
	<li>There are at least one 0 in the given matrix.</li>
	<li>The cells are adjacent in only four directions: up, down, left and right.</li>
</ol>


------

**题目：** 
<p>给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。</p>

<p>两个相邻元素间的距离为 1 。</p>

<p><strong>示例 1: </strong><br />
输入:</p>

<pre>
0 0 0
0 1 0
0 0 0
</pre>

<p>输出:</p>

<pre>
0 0 0
0 1 0
0 0 0
</pre>

<p><strong>示例 2: </strong><br />
输入:</p>

<pre>
0 0 0
0 1 0
1 1 1
</pre>

<p>输出:</p>

<pre>
0 0 0
0 1 0
1 2 1
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>给定矩阵的元素个数不超过 10000。</li>
	<li>给定矩阵中至少有一个元素是 0。</li>
	<li>矩阵中的元素只在四个方向上相邻: 上、下、左、右。</li>
</ol>

