#### 太平洋大西洋水流问题/Pacific Atlantic Water Flow
**难度：** 中等/Medium

**Question：** 

<p>Given an <code>m x n</code> matrix of non-negative integers representing the height of each unit cell in a continent, the &quot;Pacific ocean&quot; touches the left and top edges of the matrix and the &quot;Atlantic ocean&quot; touches the right and bottom edges.</p>

<p>Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.</p>

<p>Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.</p>

<p><b>Note:</b></p>

<ol>
	<li>The order of returned grid coordinates does not matter.</li>
	<li>Both <i>m</i> and <i>n</i> are less than 150.</li>
</ol>

<p>&nbsp;</p>

<p><b>Example:</b></p>

<pre>
Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
</pre>

<p>&nbsp;</p>


------

**题目：** 
<p>给定一个 <code>m x n</code> 的非负整数矩阵来表示一片大陆上各个单元格的高度。&ldquo;太平洋&rdquo;处于大陆的左边界和上边界，而&ldquo;大西洋&rdquo;处于大陆的右边界和下边界。</p>

<p>规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。</p>

<p>请找出那些水流既可以流动到&ldquo;太平洋&rdquo;，又能流动到&ldquo;大西洋&rdquo;的陆地单元的坐标。</p>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>输出坐标的顺序不重要</li>
	<li><em>m</em> 和 <em>n</em> 都小于150</li>
</ol>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<p>&nbsp;</p>

<pre>
给定下面的 5x5 矩阵:

  太平洋 ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * 大西洋

返回:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).
</pre>

<p>&nbsp;</p>

