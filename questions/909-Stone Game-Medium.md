#### 石子游戏/Stone Game
**难度：** 中等/Medium

**Question：** 

<p>Alex and Lee play a game with piles of stones.&nbsp; There are an even number of&nbsp;piles <strong>arranged in a row</strong>, and each pile has a positive integer number of stones <code>piles[i]</code>.</p>

<p>The objective of the game is to end with the most&nbsp;stones.&nbsp; The total number of stones is odd, so there are no ties.</p>

<p>Alex and Lee take turns, with Alex starting first.&nbsp; Each turn, a player&nbsp;takes the entire pile of stones from either the beginning or the end of the row.&nbsp; This continues until there are no more piles left, at which point the person with the most stones wins.</p>

<p>Assuming Alex and Lee play optimally, return <code>True</code>&nbsp;if and only if Alex wins the game.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[5,3,4,5]</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation: </strong>
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>2 &lt;= piles.length &lt;= 500</code></li>
	<li><code>piles.length</code> is even.</li>
	<li><code>1 &lt;= piles[i] &lt;= 500</code></li>
	<li><code>sum(piles)</code> is odd.</li>
</ol>

------

**题目：** 
<p>亚历克斯和李用几堆石子在做游戏。偶数堆石子<strong>排成一行</strong>，每堆都有正整数颗石子&nbsp;<code>piles[i]</code>&nbsp;。</p>

<p>游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。</p>

<p>亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。</p>

<p>假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回&nbsp;<code>true</code>&nbsp;，当李赢得比赛时返回&nbsp;<code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>[5,3,4,5]
<strong>输出：</strong>true
<strong>解释：</strong>
亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>2 &lt;= piles.length &lt;= 500</code></li>
	<li><code>piles.length</code> 是偶数。</li>
	<li><code>1 &lt;= piles[i] &lt;= 500</code></li>
	<li><code>sum(piles)</code>&nbsp;是奇数。</li>
</ol>

