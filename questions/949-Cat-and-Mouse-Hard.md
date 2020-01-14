#### 猫和老鼠/Cat and Mouse
**难度：** 困难/Hard

**Question：** 

<p>A game on an <strong>undirected</strong> graph is played by two players, Mouse and Cat, who alternate turns.</p>

<p>The graph is given as follows: <code>graph[a]</code> is a list of all nodes <code>b</code> such that <code>ab</code> is an edge of the graph.</p>

<p>Mouse starts at node 1 and goes first, Cat starts at node 2 and goes second, and there is a Hole at node 0.</p>

<p>During each player&#39;s turn, they <strong>must</strong> travel along one&nbsp;edge of the graph that meets where they are.&nbsp; For example, if the Mouse is at node <code>1</code>, it <strong>must</strong> travel to any node in <code>graph[1]</code>.</p>

<p>Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)</p>

<p>Then, the game can end in 3 ways:</p>

<ul>
	<li>If ever the Cat occupies the same node as the Mouse, the Cat wins.</li>
	<li>If ever the Mouse reaches the Hole, the Mouse wins.</li>
	<li>If ever a position is repeated (ie.&nbsp;the players are in the same position as a previous turn, and&nbsp;it is the same player&#39;s turn to move), the game is a draw.</li>
</ul>

<p>Given a <code>graph</code>, and assuming both players play optimally, return <code>1</code>&nbsp;if the game is won by Mouse, <code>2</code>&nbsp;if the game is won by Cat, and <code>0</code>&nbsp;if the game is a draw.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]</span>
<strong>Output: </strong><span id="example-output-1">0
<strong>Explanation:</strong>
</span>4---3---1
|&nbsp; &nbsp;|
2---5
&nbsp;\&nbsp;/
&nbsp; 0
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>3 &lt;= graph.length &lt;= 50</code></li>
	<li>It is guaranteed that <code>graph[1]</code> is non-empty.</li>
	<li>It is guaranteed that <code>graph[2]</code> contains a non-zero element.&nbsp;</li>
</ol>
</div>


------

**题目：** 
<p>两个玩家分别扮演猫（Cat）和老鼠（Mouse）在<strong>无向</strong>图上进行游戏，他们轮流行动。</p>

<p>该图按下述规则给出：<code>graph[a]</code>&nbsp;是所有结点 <code>b</code> 的列表，使得 <code>ab</code> 是图的一条边。</p>

<p>老鼠从结点 1 开始并率先出发，猫从结点 2 开始且随后出发，在结点 0 处有一个洞。</p>

<p>在每个玩家的回合中，他们<strong>必须</strong>沿着与他们所在位置相吻合的图的一条边移动。例如，如果老鼠位于结点 <code>1</code>，那么它只能移动到&nbsp;<code>graph[1]</code>&nbsp;中的（任何）结点去。</p>

<p>此外，猫无法移动到洞（结点 0）里。</p>

<p>然后，游戏在出现以下三种情形之一时结束：</p>

<ul>
	<li>如果猫和老鼠占据相同的结点，猫获胜。</li>
	<li>如果老鼠躲入洞里，老鼠获胜。</li>
	<li>如果某一位置重复出现（即，玩家们的位置和移动顺序都与上一个回合相同），游戏平局。</li>
</ul>

<p>给定&nbsp;<code>graph</code>，并假设两个玩家都以最佳状态参与游戏，如果老鼠获胜，则返回&nbsp;<code>1</code>；如果猫获胜，则返回 <code>2</code>；如果平局，则返回 <code>0</code>。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>[[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
<strong>输出：</strong>0
<strong>解释：</strong>
4---3---1
|&nbsp; &nbsp;|
2---5
&nbsp;\&nbsp;/
&nbsp; 0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>3 &lt;= graph.length &lt;= 200</code></li>
	<li>保证 <code>graph[1]</code>&nbsp;非空。</li>
	<li>保证&nbsp;<code>graph[2]</code>&nbsp;包含非零元素。</li>
</ol>

