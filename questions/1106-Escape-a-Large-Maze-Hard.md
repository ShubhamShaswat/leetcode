#### 逃离大迷宫/Escape a Large Maze
**难度：** 困难/Hard

**Question：** 

<p>In a 1 million by 1 million grid, the coordinates of each grid square are <code>(x, y)</code> with <code>0 &lt;= x, y &lt; 10^6</code>.</p>

<p>We start at the <code>source</code> square and want to reach the <code>target</code> square.&nbsp; Each move, we can walk to a 4-directionally adjacent square in the grid that isn&#39;t in the given list of <code>blocked</code> squares.</p>

<p>Return <code>true</code> if and only if it is possible to reach the target square through a sequence of moves.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>blocked = <span id="example-input-1-1">[[0,1],[1,0]]</span>, source = <span id="example-input-1-2">[0,0]</span>, target = <span id="example-input-1-3">[0,2]</span>
<strong>Output: </strong><span id="example-output-1">false</span>
<strong>Explanation: </strong>
The target square is inaccessible starting from the source square, because we can&#39;t walk outside the grid.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>blocked = <span id="example-input-2-1">[]</span>, source = <span id="example-input-2-2">[0,0]</span>, target = <span id="example-input-2-3">[999999,999999]</span>
<strong>Output: </strong><span id="example-output-2">true</span>
<strong>Explanation: </strong>
Because there are no blocked cells, it&#39;s possible to reach the target square.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= blocked.length &lt;= 200</code></li>
	<li><code>blocked[i].length == 2</code></li>
	<li><code>0 &lt;= blocked[i][j] &lt; 10^6</code></li>
	<li><code>source.length == target.length == 2</code></li>
	<li><code>0 &lt;= source[i][j], target[i][j] &lt; 10^6</code></li>
	<li><code>source != target</code></li>
</ol>


------

**题目：** 
<p>在一个 10^6 x 10^6 的网格中，每个网格块的坐标为&nbsp;<code>(x, y)</code>，其中&nbsp;<code>0 &lt;= x, y &lt; 10^6</code>。</p>

<p>我们从源方格&nbsp;<code>source</code>&nbsp;开始出发，意图赶往目标方格&nbsp;<code>target</code>。每次移动，我们都可以走到网格中在四个方向上相邻的方格，只要该方格不在给出的封锁列表&nbsp;<code>blocked</code>&nbsp;上。</p>

<p>只有在可以通过一系列的移动到达目标方格时才返回&nbsp;<code>true</code>。否则，返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
<strong>输出：</strong>false
<strong>解释：</strong>
从源方格无法到达目标方格，因为我们无法在网格中移动。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>blocked = [], source = [0,0], target = [999999,999999]
<strong>输出：</strong>true
<strong>解释：</strong>
因为没有方格被封锁，所以一定可以到达目标方格。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>0 &lt;= blocked.length &lt;= 200</code></li>
	<li><code>blocked[i].length == 2</code></li>
	<li><code>0 &lt;= blocked[i][j] &lt; 10^6</code></li>
	<li><code>source.length == target.length == 2</code></li>
	<li><code>0 &lt;= source[i][j], target[i][j] &lt; 10^6</code></li>
	<li><code>source != target</code></li>
</ol>

