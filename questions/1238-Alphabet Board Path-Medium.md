#### 字母板上的路径/Alphabet Board Path
**难度：** 中等/Medium

**Question：** 

<p>On an alphabet board, we start at position <code>(0, 0)</code>, corresponding to character&nbsp;<code>board[0][0]</code>.</p>

<p>Here, <code>board = [&quot;abcde&quot;, &quot;fghij&quot;, &quot;klmno&quot;, &quot;pqrst&quot;, &quot;uvwxy&quot;, &quot;z&quot;]</code>, as shown in the diagram below.</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/07/28/azboard.png" style="width: 250px; height: 317px;" /></p>

<p>We may make the following moves:</p>

<ul>
	<li><code>&#39;U&#39;</code> moves our position up one row, if the position exists on the board;</li>
	<li><code>&#39;D&#39;</code> moves our position down one row, if the position exists on the board;</li>
	<li><code>&#39;L&#39;</code> moves our position left one column, if the position exists on the board;</li>
	<li><code>&#39;R&#39;</code> moves our position right one column, if the position exists on the board;</li>
	<li><code>&#39;!&#39;</code>&nbsp;adds the character <code>board[r][c]</code> at our current position <code>(r, c)</code>&nbsp;to the&nbsp;answer.</li>
</ul>

<p>(Here, the only positions that exist on the board are positions with letters on them.)</p>

<p>Return a sequence of moves that makes our answer equal to <code>target</code>&nbsp;in the minimum number of moves.&nbsp; You may return any path that does so.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> target = "leet"
<strong>Output:</strong> "DDR!UURRR!!DDD!"
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> target = "code"
<strong>Output:</strong> "RR!DDRR!UUL!R!"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= target.length &lt;= 100</code></li>
	<li><code>target</code> consists only of English lowercase letters.</li>
</ul>

------

**题目：** 
<p>我们从一块字母板上的位置&nbsp;<code>(0, 0)</code>&nbsp;出发，该坐标对应的字符为&nbsp;<code>board[0][0]</code>。</p>

<p>在本题里，字母板为<code>board = [&quot;abcde&quot;, &quot;fghij&quot;, &quot;klmno&quot;, &quot;pqrst&quot;, &quot;uvwxy&quot;, &quot;z&quot;]</code>.</p>

<p>我们可以按下面的指令规则行动：</p>

<ul>
	<li>如果方格存在，<code>&#39;U&#39;</code>&nbsp;意味着将我们的位置上移一行；</li>
	<li>如果方格存在，<code>&#39;D&#39;</code>&nbsp;意味着将我们的位置下移一行；</li>
	<li>如果方格存在，<code>&#39;L&#39;</code>&nbsp;意味着将我们的位置左移一列；</li>
	<li>如果方格存在，<code>&#39;R&#39;</code>&nbsp;意味着将我们的位置右移一列；</li>
	<li><code>&#39;!&#39;</code>&nbsp;会把在我们当前位置 <code>(r, c)</code> 的字符&nbsp;<code>board[r][c]</code>&nbsp;添加到答案中。</li>
</ul>

<p>返回指令序列，用最小的行动次数让答案和目标&nbsp;<code>target</code>&nbsp;相同。你可以返回任何达成目标的路径。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>target = &quot;leet&quot;
<strong>输出：</strong>&quot;DDR!UURRR!!DDD!&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>target = &quot;code&quot;
<strong>输出：</strong>&quot;RR!DDRR!UUL!R!&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= target.length &lt;= 100</code></li>
	<li><code>target</code>&nbsp;仅含有小写英文字母。</li>
</ul>

