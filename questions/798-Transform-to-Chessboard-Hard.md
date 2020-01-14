#### 变为棋盘/Transform to Chessboard
**难度：** 困难/Hard

**Question：** 

<p>An N x N <code>board</code> contains only <code>0</code>s and <code>1</code>s. In each move, you can swap any 2 rows with each other, or any 2 columns with each other.</p>

<p>What is the minimum number of moves to transform the board into a &quot;chessboard&quot; - a board where no <code>0</code>s and no <code>1</code>s are 4-directionally adjacent? If the task is impossible, return -1.</p>

<pre>
<strong>Examples:</strong>
<strong>Input:</strong> board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
One potential sequence of moves is shown below, from left to right:

0110     1010     1010
0110 --&gt; 1010 --&gt; 0101
1001     0101     1010
1001     0101     0101

The first move swaps the first and second column.
The second move swaps the second and third row.


<strong>Input:</strong> board = [[0, 1], [1, 0]]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
Also note that the board with 0 in the top left corner,
01
10

is also a valid chessboard.

<strong>Input:</strong> board = [[1, 0], [1, 0]]
<strong>Output:</strong> -1
<strong>Explanation:</strong>
No matter what sequence of moves you make, you cannot end with a valid chessboard.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>board</code> will have the same number of rows and columns, a number in the range <code>[2, 30]</code>.</li>
	<li><code>board[i][j]</code> will be only <code>0</code>s or <code>1</code>s.</li>
</ul>


------

**题目：** 
<p>一个 N&nbsp;x N的 <code>board</code>&nbsp;仅由&nbsp;<code>0</code>&nbsp;和&nbsp;<code>1</code>&nbsp;组成&nbsp;。每次移动，你能任意交换两列或是两行的位置。</p>

<p>输出将这个矩阵变为 &ldquo;棋盘&rdquo; 所需的最小移动次数。&ldquo;棋盘&rdquo; 是指任意一格的上下左右四个方向的值均与本身不同的矩阵。如果不存在可行的变换，输出 -1。</p>

<pre><strong>示例:</strong>
<strong>输入:</strong> board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
<strong>输出:</strong> 2
<strong>解释:</strong>
一种可行的变换方式如下，从左到右：

0110     1010     1010
0110 --&gt; 1010 --&gt; 0101
1001     0101     1010
1001     0101     0101

第一次移动交换了第一列和第二列。
第二次移动交换了第二行和第三行。


<strong>输入:</strong> board = [[0, 1], [1, 0]]
<strong>输出:</strong> 0
<strong>解释:</strong>
注意左上角的格值为0时也是合法的棋盘，如：

01
10

也是合法的棋盘.

<strong>输入:</strong> board = [[1, 0], [1, 0]]
<strong>输出:</strong> -1
<strong>解释:</strong>
任意的变换都不能使这个输入变为合法的棋盘。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>board</code>&nbsp;是方阵，且行列数的范围是<code>[2, 30]</code>。</li>
	<li><code>board[i][j]</code>&nbsp;将只包含&nbsp;<code>0</code>或&nbsp;<code>1</code>。</li>
</ul>

