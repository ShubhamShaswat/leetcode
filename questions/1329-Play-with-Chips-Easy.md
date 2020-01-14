#### 玩筹码/Play with Chips
**难度：** 简单/Easy

**Question：** 

<p>There are some chips, and the i-th chip is at position <code>chips[i]</code>.</p>

<p>You can perform any of the two following types of moves <strong>any number of times</strong> (possibly&nbsp;zero) <strong>on any chip</strong>:</p>

<ul>
	<li>Move the <code>i</code>-th chip&nbsp;by&nbsp;2 units to the left or to the right with a cost of <strong>0</strong>.</li>
	<li>Move&nbsp;the <code>i</code>-th chip&nbsp;by&nbsp;1 unit to the left or to the right with a cost of&nbsp;<strong>1</strong>.</li>
</ul>

<p>There can be two or more chips&nbsp;at the same position initially.</p>

<p>Return the&nbsp;minimum cost needed to move all the chips to the same position (any position).</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> chips = [1,2,3]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Second chip will be moved to positon 3 with cost 1. First chip will be moved to position 3 with cost 0. Total cost is 1.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> chips = [2,2,2,3,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Both fourth and fifth chip will be moved to position two with cost 1. Total minimum cost will be 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= chips.length &lt;= 100</code></li>
	<li><code>1 &lt;= chips[i] &lt;= 10^9</code></li>
</ul>


------

**题目：** 
<p>数轴上放置了一些筹码，每个筹码的位置存在数组&nbsp;<code>chips</code>&nbsp;当中。</p>

<p>你可以对 <strong>任何筹码</strong> 执行下面两种操作之一（<strong>不限操作次数</strong>，0 次也可以）：</p>

<ul>
	<li>将第 <code>i</code> 个筹码向左或者右移动 2 个单位，代价为 <strong>0</strong>。</li>
	<li>将第 <code>i</code> 个筹码向左或者右移动 1 个单位，代价为 <strong>1</strong>。</li>
</ul>

<p>最开始的时候，同一位置上也可能放着两个或者更多的筹码。</p>

<p>返回将所有筹码移动到同一位置（任意位置）上所需要的最小代价。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>chips = [1,2,3]
<strong>输出：</strong>1
<strong>解释：</strong>第二个筹码移动到位置三的代价是 1，第一个筹码移动到位置三的代价是 0，总代价为 1。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>chips = [2,2,2,3,3]
<strong>输出：</strong>2
<strong>解释：</strong>第四和第五个筹码移动到位置二的代价都是 1，所以最小总代价为 2。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= chips.length &lt;= 100</code></li>
	<li><code>1 &lt;= chips[i] &lt;= 10^9</code></li>
</ul>

