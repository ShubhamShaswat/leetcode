#### “马”在棋盘上的概率/Knight Probability in Chessboard
**难度：** 中等/Medium

**Question：** 

<p>On an <code>N</code>x<code>N</code> chessboard, a knight starts at the <code>r</code>-th row and <code>c</code>-th column and attempts to make exactly <code>K</code> moves. The rows and columns are 0 indexed, so the top-left square is <code>(0, 0)</code>, and the bottom-right square is <code>(N-1, N-1)</code>.</p>

<p>A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.</p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/knight.png" style="width: 200px; height: 200px;" /></p>

<p>&nbsp;</p>

<p>Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.</p>

<p>The knight continues moving until it has made exactly <code>K</code> moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.</p>

<p>&nbsp;</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> 3, 2, 0, 0
<b>Output:</b> 0.0625
<b>Explanation:</b> There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ul>
	<li><code>N</code> will be between 1 and 25.</li>
	<li><code>K</code> will be between 0 and 100.</li>
	<li>The knight always initially starts on the board.</li>
</ul>


------

**题目：** 
<p>已知一个&nbsp;<code>N</code>x<code>N</code>&nbsp;的国际象棋棋盘，棋盘的行号和列号都是从 0 开始。即最左上角的格子记为&nbsp;<code>(0, 0)</code>，最右下角的记为&nbsp;<code>(N-1, N-1)</code>。&nbsp;</p>

<p>现有一个 &ldquo;马&rdquo;（也译作 &ldquo;骑士&rdquo;）位于&nbsp;<code>(r, c)</code>&nbsp;，并打算进行&nbsp;<code>K</code> 次移动。&nbsp;</p>

<p>如下图所示，国际象棋的 &ldquo;马&rdquo; 每一步先沿水平或垂直方向移动 2 个格子，然后向与之相垂直的方向再移动 1 个格子，共有 8 个可选的位置。</p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/knight.png" style="height: 200px; width: 200px;"></p>

<p>&nbsp;</p>

<p>现在 &ldquo;马&rdquo; 每一步都从可选的位置（包括棋盘外部的）中独立随机地选择一个进行移动，直到移动了&nbsp;<code>K</code>&nbsp;次或跳到了棋盘外面。</p>

<p>求移动结束后，&ldquo;马&rdquo; 仍留在棋盘上的概率。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入:</strong> 3, 2, 0, 0
<strong>输出:</strong> 0.0625
<strong>解释:</strong> 
输入的数据依次为 N, K, r, c
第 1 步时，有且只有 2 种走法令 &ldquo;马&rdquo; 可以留在棋盘上（跳到（1,2）或（2,1））。对于以上的两种情况，各自在第2步均有且只有2种走法令 &ldquo;马&rdquo; 仍然留在棋盘上。
所以 &ldquo;马&rdquo; 在结束后仍在棋盘上的概率为 0.0625。
</pre>

<p>&nbsp;</p>

<p><strong>注意：</strong></p>

<ul>
	<li><code>N</code> 的取值范围为 [1, 25]</li>
	<li><code>K</code>&nbsp;的取值范围为 [0, 100]</li>
	<li>开始时，&ldquo;马&rdquo; 总是位于棋盘上</li>
</ul>

