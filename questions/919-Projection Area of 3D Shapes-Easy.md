#### 三维形体投影面积/Projection Area of 3D Shapes
**难度：** 简单/Easy

**Question：** 

<p>On a&nbsp;<code>N&nbsp;*&nbsp;N</code> grid, we place some&nbsp;<code>1 * 1 * 1&nbsp;</code>cubes that are axis-aligned with the x, y, and z axes.</p>

<p>Each value&nbsp;<code>v = grid[i][j]</code>&nbsp;represents a tower of&nbsp;<code>v</code>&nbsp;cubes placed on top of grid cell <code>(i, j)</code>.</p>

<p>Now we view the&nbsp;<em>projection</em>&nbsp;of these cubes&nbsp;onto the xy, yz, and zx planes.</p>

<p>A projection is like a shadow, that&nbsp;maps our 3 dimensional figure to a 2 dimensional plane.&nbsp;</p>

<p>Here, we are viewing the &quot;shadow&quot; when looking at the cubes from the top, the front, and the side.</p>

<p>Return the total area of all three projections.</p>

<p>&nbsp;</p>

<div>
<ul>
</ul>
</div>

<div>
<div>
<ul>
</ul>
</div>
</div>

<div>
<div>
<div>
<div>
<ul>
</ul>
</div>
</div>
</div>
</div>

<div>
<div>
<div>
<div>
<div>
<div>
<div>
<div>
<ul>
</ul>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[2]]</span>
<strong>Output: </strong><span id="example-output-1">5</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[[1,2],[3,4]]</span>
<strong>Output: </strong><span id="example-output-2">17</span>
<strong>Explanation: </strong>
Here are the three projections (&quot;shadows&quot;) of the shape made with each axis-aligned plane.
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/02/shadow.png" style="width: 749px; height: 200px;" />
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[[1,0],[0,2]]</span>
<strong>Output: </strong><span id="example-output-3">8</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[[1,1,1],[1,0,1],[1,1,1]]</span>
<strong>Output: </strong><span id="example-output-4">14</span>
</pre>

<div>
<p><strong>Example 5:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-5-1">[[2,2,2],[2,1,2],[2,2,2]]</span>
<strong>Output: </strong><span id="example-output-5">21</span>
</pre>

<p>&nbsp;</p>

<div>
<div>
<div>
<p><span><strong>Note:</strong></span></p>

<ul>
	<li><code>1 &lt;= grid.length = grid[0].length&nbsp;&lt;= 50</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 50</code></li>
</ul>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>


------

**题目：** 
<p>在&nbsp;<code>N&nbsp;*&nbsp;N</code>&nbsp;的网格中，我们放置了一些与 x，y，z 三轴对齐的&nbsp;<code>1 * 1 * 1</code>&nbsp;立方体。</p>

<p>每个值&nbsp;<code>v = grid[i][j]</code>&nbsp;表示 <code>v</code>&nbsp;个正方体叠放在单元格&nbsp;<code>(i, j)</code>&nbsp;上。</p>

<p>现在，我们查看这些立方体在 xy、yz&nbsp;和 zx&nbsp;平面上的<em>投影</em>。</p>

<p>投影就像影子，将三维形体映射到一个二维平面上。</p>

<p>在这里，从顶部、前面和侧面看立方体时，我们会看到&ldquo;影子&rdquo;。</p>

<p>返回所有三个投影的总面积。</p>

<p>&nbsp;</p>

<ul>
</ul>

<ul>
</ul>

<ul>
</ul>

<ul>
</ul>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[[2]]
<strong>输出：</strong>5
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[[1,2],[3,4]]
<strong>输出：</strong>17
<strong>解释：</strong>
这里有该形体在三个轴对齐平面上的三个投影(&ldquo;阴影部分&rdquo;)。
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/02/shadow.png" style="height: 200px; width: 749px;">
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[[1,0],[0,2]]
<strong>输出：</strong>8
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>[[1,1,1],[1,0,1],[1,1,1]]
<strong>输出：</strong>14
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>[[2,2,2],[2,1,2],[2,2,2]]
<strong>输出：</strong>21
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= grid.length = grid[0].length&nbsp;&lt;= 50</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 50</code></li>
</ul>

