#### 网格照明/Grid Illumination
**难度：** 困难/Hard

**Question：** 

<p>On a <code>N x N</code> grid of cells, each cell <code>(x, y)</code> with <code>0 &lt;= x &lt; N</code> and <code>0 &lt;= y &lt; N</code> has a lamp.</p>

<p>Initially, some number of lamps are on.&nbsp; <code>lamps[i]</code> tells us the location of the <code>i</code>-th lamp that is on.&nbsp; Each lamp that is on illuminates every square on its x-axis, y-axis, and both diagonals (similar to a Queen in chess).</p>

<p>For the i-th query&nbsp;<code>queries[i] = (x, y)</code>, the answer to the query is 1 if the cell (x, y) is illuminated, else 0.</p>

<p>After each query <code>(x, y)</code> [in the order given by <code>queries</code>], we turn off any&nbsp;lamps that are at cell <code>(x, y)</code>&nbsp;or are adjacent 8-directionally (ie., share a corner or edge with cell <code>(x, y)</code>.)</p>

<p>Return an array of answers.&nbsp; Each&nbsp;value <code>answer[i]</code> should be equal to the answer of the <code>i</code>-th query <code>queries[i]</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-1-1">5</span>, lamps = <span id="example-input-1-2">[[0,0],[4,4]]</span>, queries = <span id="example-input-1-3">[[1,1],[1,0]]</span>
<strong>Output: </strong><span id="example-output-1">[1,0]</span>
<strong>Explanation: </strong>
Before performing the first query we have both lamps [0,0] and [4,4] on.
The grid representing which cells are lit looks like this, where [0,0] is the top left corner, and [4,4] is the bottom right corner:
1 1 1 1 1
1 1 0 0 1
1 0 1 0 1
1 0 0 1 1
1 1 1 1 1
Then the query at [1, 1] returns 1 because the cell is lit.  After this query, the lamp at [0, 0] turns off, and the grid now looks like this:
1 0 0 0 1
0 1 0 0 1
0 0 1 0 1
0 0 0 1 1
1 1 1 1 1
Before performing the second query we have only the lamp [4,4] on.  Now the query at [1,0] returns 0, because the cell is no longer lit.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 10^9</code></li>
	<li><code>0 &lt;= lamps.length &lt;= 20000</code></li>
	<li><code>0 &lt;= queries.length &lt;= 20000</code></li>
	<li><code>lamps[i].length == queries[i].length == 2</code></li>
</ol>

------

**题目：** 
<p>在&nbsp;<code>N x N</code>&nbsp;的网格上，每个单元格&nbsp;<code>(x, y)</code>&nbsp;上都有一盏灯，其中&nbsp;<code>0 &lt;= x &lt; N</code>&nbsp;且&nbsp;<code>0 &lt;= y &lt; N</code> 。</p>

<p>最初，一定数量的灯是亮着的。<code>lamps[i]</code>&nbsp;告诉我们亮着的第 <code>i</code> 盏灯的位置。每盏灯都照亮其所在 x 轴、y 轴和两条对角线上的每个正方形（类似于国际象棋中的皇后）。</p>

<p>对于第 <code>i</code> 次查询&nbsp;<code>queries[i] = (x, y)</code>，如果单元格 (x, y) 是被照亮的，则查询结果为 1，否则为 0 。</p>

<p>在每个查询 <code>(x, y)</code> 之后 [按照查询的顺序]，我们关闭位于单元格 (x, y) 上或其相邻 8 个方向上（与单元格 (x, y) 共享一个角或边）的任何灯。</p>

<p>返回答案数组 <code>answer</code>。每个值 <code>answer[i]</code> 应等于第 <code>i</code>&nbsp;次查询&nbsp;<code>queries[i]</code>&nbsp;的结果。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
<strong>输出：</strong>[1,0]
<strong>解释： </strong>
在执行第一次查询之前，我们位于 [0, 0] 和 [4, 4] 灯是亮着的。
表示哪些单元格亮起的网格如下所示，其中 [0, 0] 位于左上角：
1 1 1 1 1
1 1 0 0 1
1 0 1 0 1
1 0 0 1 1
1 1 1 1 1
然后，由于单元格 [1, 1] 亮着，第一次查询返回 1。在此查询后，位于 [0，0] 处的灯将关闭，网格现在如下所示：
1 0 0 0 1
0 1 0 0 1
0 0 1 0 1
0 0 0 1 1
1 1 1 1 1
在执行第二次查询之前，我们只有 [4, 4] 处的灯亮着。现在，[1, 0] 处的查询返回 0，因为该单元格不再亮着。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 10^9</code></li>
	<li><code>0 &lt;= lamps.length &lt;= 20000</code></li>
	<li><code>0 &lt;= queries.length &lt;= 20000</code></li>
	<li><code>lamps[i].length == queries[i].length == 2</code></li>
</ol>

