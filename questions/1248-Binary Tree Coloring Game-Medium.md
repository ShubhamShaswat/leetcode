#### 二叉树着色游戏/Binary Tree Coloring Game
**难度：** 中等/Medium

**Question：** 

<p>Two players play a turn based game on a binary tree.&nbsp; We are given&nbsp;the <code>root</code> of this binary tree, and the number of nodes <code>n</code>&nbsp;in the tree.&nbsp; <code>n</code> is odd, and&nbsp;each node has a distinct value from <code>1</code> to <code>n</code>.</p>

<p>Initially, the first player names a value <code>x</code> with <code>1 &lt;= x &lt;= n</code>, and the second player names a value <code>y</code> with <code>1 &lt;= y &lt;= n</code> and <code>y != x</code>.&nbsp; The first player colors the node with value <code>x</code> red, and the second player colors the node with value <code>y</code> blue.</p>

<p>Then, the players take turns starting with the first player.&nbsp; In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an <strong>uncolored</strong> neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)</p>

<p>If (and only if)&nbsp;a player cannot choose such a node in this way, they must pass their turn.&nbsp; If both players pass their turn, the game ends, and the winner is the player that colored more nodes.</p>

<p>You are the second player.&nbsp; If it is possible to choose such a <code>y</code>&nbsp;to ensure you win the game, return <code>true</code>.&nbsp; If it is not possible, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/08/01/1480-binary-tree-coloring-game.png" style="width: 300px; height: 186px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
<strong>Output:</strong> true
<strong>Explanation: </strong>The second player can choose the node with value 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>root</code> is the root of a binary tree with <code>n</code> nodes and distinct node values from <code>1</code> to <code>n</code>.</li>
	<li><code>n</code> is odd.</li>
	<li><code>1 &lt;= x &lt;= n&nbsp;&lt;= 100</code></li>
</ul>


------

**题目：** 
<p>有两位极客玩家参与了一场「二叉树着色」的游戏。游戏中，给出二叉树的根节点&nbsp;<code>root</code>，树上总共有 <code>n</code> 个节点，且 <code>n</code> 为奇数，其中每个节点上的值从&nbsp;<code>1</code> 到&nbsp;<code>n</code>&nbsp;各不相同。</p>

<p>&nbsp;</p>

<p>游戏从「一号」玩家开始（「一号」玩家为红色，「二号」玩家为蓝色），最开始时，</p>

<p>「一号」玩家从 <code>[1, n]</code>&nbsp;中取一个值&nbsp;<code>x</code>（<code>1 &lt;= x &lt;= n</code>）；</p>

<p>「二号」玩家也从&nbsp;<code>[1, n]</code>&nbsp;中取一个值&nbsp;<code>y</code>（<code>1 &lt;= y &lt;= n</code>）且&nbsp;<code>y != x</code>。</p>

<p>「一号」玩家给值为&nbsp;<code>x</code>&nbsp;的节点染上红色，而「二号」玩家给值为&nbsp;<code>y</code>&nbsp;的节点染上蓝色。</p>

<p>&nbsp;</p>

<p>之后两位玩家轮流进行操作，每一回合，玩家选择一个他之前涂好颜色的节点，将所选节点一个 <strong>未着色 </strong>的邻节点（即左右子节点、或父节点）进行染色。</p>

<p>如果当前玩家无法找到这样的节点来染色时，他的回合就会被跳过。</p>

<p>若两个玩家都没有可以染色的节点时，游戏结束。着色节点最多的那位玩家获得胜利 ✌️。</p>

<p>&nbsp;</p>

<p>现在，假设你是「二号」玩家，根据所给出的输入，假如存在一个&nbsp;<code>y</code>&nbsp;值可以确保你赢得这场游戏，则返回&nbsp;<code>true</code>；若无法获胜，就请返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/08/04/1480-binary-tree-coloring-game.png" style="height: 186px; width: 300px;"></strong></p>

<pre><strong>输入：</strong>root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
<strong>输出：</strong>True
<strong>解释：</strong>第二个玩家可以选择值为 2 的节点。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>二叉树的根节点为&nbsp;<code>root</code>，树上由 <code>n</code> 个节点，节点上的值从 <code>1</code> 到 <code>n</code> 各不相同。</li>
	<li><code>n</code> 为奇数。</li>
	<li><code>1 &lt;= x &lt;= n&nbsp;&lt;= 100</code></li>
</ul>

