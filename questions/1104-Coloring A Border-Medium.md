#### 边框着色/Coloring A Border
**难度：** 中等/Medium

**Question：** 

<p>Given a 2-dimensional&nbsp;<code>grid</code> of integers, each value in the grid represents the color of the grid square at that location.</p>

<p>Two squares belong to the same <em>connected component</em> if and only if they have the same color and are next to each other in any of the 4 directions.</p>

<p>The&nbsp;<em>border</em> of a connected component is&nbsp;all the squares in the connected component that are&nbsp;either 4-directionally adjacent to&nbsp;a square not in the component, or on the boundary of the grid (the first or last row or column).</p>

<p>Given a square at location&nbsp;<code>(r0, c0)</code>&nbsp;in the grid and a <code>color</code>, color the&nbsp;border of the connected component of that square with the given <code>color</code>, and return the final <code>grid</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>grid = <span id="example-input-1-1">[[1,1],[1,2]]</span>, r0 = <span id="example-input-1-2">0</span>, c0 = <span id="example-input-1-3">0</span>, color = <span id="example-input-1-4">3</span>
<strong>Output: </strong><span id="example-output-1">[[3, 3], [3, 2]]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>grid = <span id="example-input-2-1">[[1,2,2],[2,3,2]]</span>, r0 = <span id="example-input-2-2">0</span>, c0 = <span id="example-input-2-3">1</span>, color = <span id="example-input-2-4">3</span>
<strong>Output: </strong><span id="example-output-2">[[1, 3, 3], [2, 3, 3]]</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>grid = <span id="example-input-3-1">[[1,1,1],[1,1,1],[1,1,1]]</span>, r0 = <span id="example-input-3-2">1</span>, c0 = <span id="example-input-3-3">1</span>, color = <span id="example-input-3-4">2</span>
<strong>Output: </strong><span id="example-output-3">[[2, 2, 2], [2, 1, 2], [2, 2, 2]]</span></pre>
</div>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= grid.length &lt;= 50</code></li>
	<li><code>1 &lt;= grid[0].length &lt;= 50</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 1000</code></li>
	<li><code>0 &lt;= r0 &lt; grid.length</code></li>
	<li><code>0 &lt;= c0 &lt; grid[0].length</code></li>
	<li><code>1 &lt;= color &lt;= 1000</code></li>
</ol>

------

**题目：** 
<p>给出一个二维整数网格&nbsp;<code>grid</code>，网格中的每个值表示该位置处的网格块的颜色。</p>

<p>只有当两个网格块的颜色相同，而且在四个方向中任意一个方向上相邻时，它们属于同一<strong>连通分量</strong>。</p>

<p>连通分量的<strong>边界</strong>是指连通分量中的所有与不在分量中的正方形相邻（四个方向上）的所有正方形，或者在网格的边界上（第一行/列或最后一行/列）的所有正方形。</p>

<p>给出位于&nbsp;<code>(r0, c0)</code>&nbsp;的网格块和颜色&nbsp;<code>color</code>，使用指定颜色&nbsp;<code>color</code>&nbsp;为所给网格块的连通分量的边界进行着色，并返回最终的网格&nbsp;<code>grid</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
<strong>输出：</strong>[[3, 3], [3, 2]]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
<strong>输出：</strong>[[1, 3, 3], [2, 3, 3]]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
<strong>输出：</strong>[[2, 2, 2], [2, 1, 2], [2, 2, 2]]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= grid.length &lt;= 50</code></li>
	<li><code>1 &lt;= grid[0].length &lt;= 50</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 1000</code></li>
	<li><code>0 &lt;= r0 &lt; grid.length</code></li>
	<li><code>0 &lt;= c0 &lt; grid[0].length</code></li>
	<li><code>1 &lt;= color &lt;= 1000</code></li>
</ol>

<p>&nbsp;</p>

