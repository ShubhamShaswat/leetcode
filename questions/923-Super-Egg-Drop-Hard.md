#### 鸡蛋掉落/Super Egg Drop
**难度：** 困难/Hard

**Question：** 

<p>You are given <code>K</code> eggs, and you have access to a building with <code>N</code> floors from <code>1</code> to <code>N</code>.&nbsp;</p>

<p>Each egg is identical in function, and if an egg breaks, you cannot drop it&nbsp;again.</p>

<p>You know that there exists a floor <code>F</code> with <code>0 &lt;= F &lt;= N</code> such that any egg dropped at a floor higher than <code>F</code> will break, and any egg dropped at or below floor <code>F</code> will not break.</p>

<p>Each <em>move</em>, you may take an egg (if you have an unbroken one) and drop it from any floor <code>X</code> (with&nbsp;<code>1 &lt;= X &lt;= N</code>).&nbsp;</p>

<p>Your goal is to know&nbsp;<strong>with certainty</strong>&nbsp;what the value of <code>F</code> is.</p>

<p>What is the minimum number of moves that you need to know with certainty&nbsp;what <code>F</code> is, regardless of the initial value of <code>F</code>?</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>K = <span id="example-input-1-1">1</span>, N = <span id="example-input-1-2">2</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn&#39;t break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>K = <span id="example-input-2-1">2</span>, N = 6
<strong>Output: </strong><span id="example-output-2">3</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>K = <span id="example-input-3-1">3</span>, N = <span id="example-input-3-2">14</span>
<strong>Output: </strong><span id="example-output-3">4</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= K &lt;= 100</code></li>
	<li><code>1 &lt;= N &lt;= 10000</code></li>
</ol>
</div>
</div>
</div>


------

**题目：** 
<p>你将获得&nbsp;<code>K</code>&nbsp;个鸡蛋，并可以使用一栋从&nbsp;<code>1</code>&nbsp;到&nbsp;<code>N</code>&nbsp;&nbsp;共有 <code>N</code>&nbsp;层楼的建筑。</p>

<p>每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。</p>

<p>你知道存在楼层&nbsp;<code>F</code> ，满足&nbsp;<code>0 &lt;= F &lt;= N</code> 任何从高于 <code>F</code>&nbsp;的楼层落下的鸡蛋都会碎，从&nbsp;<code>F</code>&nbsp;楼层或比它低的楼层落下的鸡蛋都不会破。</p>

<p>每次<em>移动</em>，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层&nbsp;<code>X</code>&nbsp;扔下（满足&nbsp;<code>1 &lt;= X &lt;= N</code>）。</p>

<p>你的目标是<strong>确切地</strong>知道 <code>F</code> 的值是多少。</p>

<p>无论 <code>F</code> 的初始值如何，你确定 <code>F</code> 的值的最小移动次数是多少？</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>K = 1, N = 2
<strong>输出：</strong>2
<strong>解释：</strong>
鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
如果它没碎，那么我们肯定知道 F = 2 。
因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>K = 2, N = 6
<strong>输出：</strong>3
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>K = 3, N = 14
<strong>输出：</strong>4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= K &lt;= 100</code></li>
	<li><code>1 &lt;= N &lt;= 10000</code></li>
</ol>

