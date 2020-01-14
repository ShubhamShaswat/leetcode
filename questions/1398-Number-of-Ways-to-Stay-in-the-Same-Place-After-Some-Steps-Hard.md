#### 停在原地的方案数/Number of Ways to Stay in the Same Place After Some Steps
**难度：** 困难/Hard

**Question：** 

<p>You have a pointer at index <code>0</code> in an array of size <code><font face="monospace">arrLen</font></code>. At each step, you can move 1 position to the left, 1 position to the right&nbsp;in the array or stay in the same place&nbsp; (The pointer should not be placed outside the array at any time).</p>

<p>Given two integers&nbsp;<code>steps</code> and <code>arrLen</code>, return the number of&nbsp;ways such that your pointer still at index <code>0</code> after <strong>exactly </strong><code><font face="monospace">steps</font></code>&nbsp;steps.</p>

<p>Since the answer&nbsp;may be too large,&nbsp;return it <strong>modulo</strong>&nbsp;<code>10^9 + 7</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> steps = 3, arrLen = 2
<strong>Output:</strong> 4
<strong>Explanation: </strong>There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> steps = 2, arrLen = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are 2 differents ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> steps = 4, arrLen = 2
<strong>Output:</strong> 8
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= steps &lt;= 500</code></li>
	<li><code>1 &lt;= arrLen&nbsp;&lt;= 10^6</code></li>
</ul>


------

**题目：** 
<p>有一个长度为&nbsp;<code>arrLen</code>&nbsp;的数组，开始有一个指针在索引&nbsp;<code>0</code> 处。</p>

<p>每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。</p>

<p>给你两个整数&nbsp;<code>steps</code> 和&nbsp;<code>arrLen</code> ，请你计算并返回：在恰好执行&nbsp;<code>steps</code>&nbsp;次操作以后，指针仍然指向索引&nbsp;<code>0</code> 处的方案数。</p>

<p>由于答案可能会很大，请返回方案数 <strong>模</strong>&nbsp;<code>10^9 + 7</code> 后的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>steps = 3, arrLen = 2
<strong>输出：</strong>4
<strong>解释：</strong>3 步后，总共有 4 种不同的方法可以停在索引 0 处。
向右，向左，不动
不动，向右，向左
向右，不动，向左
不动，不动，不动
</pre>

<p><strong>示例&nbsp; 2：</strong></p>

<pre><strong>输入：</strong>steps = 2, arrLen = 4
<strong>输出：</strong>2
<strong>解释：</strong>2 步后，总共有 2 种不同的方法可以停在索引 0 处。
向右，向左
不动，不动
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>steps = 4, arrLen = 2
<strong>输出：</strong>8
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= steps &lt;= 500</code></li>
	<li><code>1 &lt;= arrLen&nbsp;&lt;= 10^6</code></li>
</ul>

