#### 蛇梯棋/Snakes and Ladders
**难度：** 中等/Medium

**Question：** 

<p>On an N x N <code>board</code>, the numbers from <code>1</code> to <code>N*N</code> are written&nbsp;<em>boustrophedonically</em>&nbsp;<strong>starting from the bottom&nbsp;left of the board</strong>, and alternating direction each row.&nbsp; For example, for a 6 x 6 board, the numbers are written as follows:</p>

<pre>
<img alt="" src="https://assets.leetcode.com/uploads/2018/09/23/snakes.png" style="width: 254px; height: 200px;" />
</pre>

<p>You start on square <code>1</code> of the board (which is always in the last row and&nbsp;first column).&nbsp; Each move, starting from square <code>x</code>, consists of the following:</p>

<ul>
	<li>You choose a destination square <code>S</code> with number&nbsp;<code>x+1</code>, <code>x+2</code>, <code>x+3</code>, <code>x+4</code>, <code>x+5</code>, or <code>x+6</code>, provided this&nbsp;number is&nbsp;<code>&lt;=&nbsp;N*N</code>.

	<ul>
		<li>(This choice simulates the result of a standard 6-sided die roll: ie., there are always <strong>at most 6 destinations, regardless of the size of the board</strong>.)</li>
	</ul>
	</li>
	<li>If <code>S</code>&nbsp;has a snake or ladder, you move to the destination of that snake or ladder.&nbsp; Otherwise, you move to <code>S</code>.</li>
</ul>

<p>A board square on row <code>r</code> and column <code>c</code>&nbsp;has a &quot;snake or ladder&quot; if <code>board[r][c] != -1</code>.&nbsp; The destination of that snake or ladder is <code>board[r][c]</code>.</p>

<p>Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of another&nbsp;snake or ladder, you do <strong>not</strong> continue moving.&nbsp; (For example, if the board is `[[4,-1],[-1,3]]`, and on the first move your destination square is `2`, then you finish your first move at&nbsp;`3`, because you do <strong>not</strong> continue moving to `4`.)</p>

<p>Return the least number of moves required to reach square <font face="monospace">N*N</font>.&nbsp; If it is not possible, return <code>-1</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
<strong>Output: </strong>4
<strong>Explanation: </strong>
At the beginning, you start at square 1 [at row 5, column 0].
You decide to move to square 2, and must take the ladder to square 15.
You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
You then decide to move to square 14, and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>2 &lt;= board.length = board[0].length&nbsp;&lt;= 20</code></li>
	<li><code>board[i][j]</code>&nbsp;is between <code>1</code> and <code>N*N</code> or is equal to <code>-1</code>.</li>
	<li>The board&nbsp;square with number <code>1</code> has no snake or ladder.</li>
	<li>The board square with number <code>N*N</code> has no snake or ladder.</li>
</ol>


------

**题目：** 
<p>在一块 N x N 的棋盘&nbsp;<code>board</code>&nbsp;上，<strong>从棋盘的左下角开始</strong>，每一行交替方向，按从&nbsp;<code>1</code> 到 <code>N*N</code>&nbsp;的数字给方格编号。例如，对于一块 6 x 6 大小的棋盘，可以编号如下：</p>

<pre><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/01/31/snakes.png" style="height: 200px; width: 254px;">
</pre>

<p>玩家从棋盘上的方格&nbsp;<code>1</code> （总是在最后一行、第一列）开始出发。</p>

<p>每一次从方格&nbsp;<code>x</code>&nbsp;起始的移动都由以下部分组成：</p>

<ul>
	<li>你选择一个目标方块 <code>S</code>，它的编号是 <code>x+1</code>，<code>x+2</code>，<code>x+3</code>，<code>x+4</code>，<code>x+5</code>，或者 <code>x+6</code>，只要这个数字&nbsp;<code>&lt;= N*N</code>。</li>
	<li>如果 <code>S</code> 有一个蛇或梯子，你就移动到那个蛇或梯子的目的地。否则，你会移动到 <code>S</code>。&nbsp;</li>
</ul>

<p>在 <code>r</code> 行 <code>c</code> 列上的方格里有 &ldquo;蛇&rdquo; 或 &ldquo;梯子&rdquo;；如果 <code>board[r][c] != -1</code>，那个蛇或梯子的目的地将会是 <code>board[r][c]</code>。</p>

<p>注意，你每次移动最多只能爬过蛇或梯子一次：就算目的地是另一条蛇或梯子的起点，你也不会继续移动。</p>

<p>返回达到方格 N*N 所需的最少移动次数，如果不可能，则返回 <code>-1</code>。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>[
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
<strong>输出：</strong>4
<strong>解释：</strong>
首先，从方格 1 [第 5 行，第 0 列] 开始。
你决定移动到方格 2，并必须爬过梯子移动到到方格 15。
然后你决定移动到方格 17 [第 3 行，第 5 列]，必须爬过蛇到方格 13。
然后你决定移动到方格 14，且必须通过梯子移动到方格 35。
然后你决定移动到方格 36, 游戏结束。
可以证明你需要至少 4 次移动才能到达第 N*N 个方格，所以答案是 4。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>2 &lt;= board.length = board[0].length&nbsp;&lt;= 20</code></li>
	<li><code>board[i][j]</code>&nbsp;介于&nbsp;<code>1</code>&nbsp;和&nbsp;<code>N*N</code>&nbsp;之间或者等于&nbsp;<code>-1</code>。</li>
	<li>编号为&nbsp;<code>1</code>&nbsp;的方格上没有蛇或梯子。</li>
	<li>编号为&nbsp;<code>N*N</code>&nbsp;的方格上没有蛇或梯子。</li>
</ol>

