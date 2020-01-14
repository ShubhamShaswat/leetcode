#### 最后一块石头的重量 II/Last Stone Weight II
**难度：** 中等/Medium

**Question：** 

<p>We have a collection of rocks, each rock has a positive integer weight.</p>

<p>Each turn, we choose <strong>any two rocks</strong>&nbsp;and smash them together.&nbsp; Suppose the stones have weights <code>x</code> and <code>y</code> with <code>x &lt;= y</code>.&nbsp; The result of this smash is:</p>

<ul>
	<li>If <code>x == y</code>, both stones are totally destroyed;</li>
	<li>If <code>x != y</code>, the stone of weight <code>x</code> is totally destroyed, and the stone of weight <code>y</code> has new weight <code>y-x</code>.</li>
</ul>

<p>At the end, there is at most 1 stone left.&nbsp; Return the <strong>smallest possible</strong> weight of this stone (the weight is&nbsp;0 if there are no stones left.)</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[2,7,4,1,8,1]
<strong>Output: </strong>1
<strong>Explanation: </strong>
We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0 so the array converts to [1] then that&#39;s the optimal value.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= stones.length &lt;= 30</code></li>
	<li><code>1 &lt;= stones[i] &lt;= 100</code></li>
</ol>

------

**题目：** 
<p>有一堆石头，每块石头的重量都是正整数。</p>

<p>每一回合，从中选出<strong>任意两块石头</strong>，然后将它们一起粉碎。假设石头的重量分别为&nbsp;<code>x</code> 和&nbsp;<code>y</code>，且&nbsp;<code>x &lt;= y</code>。那么粉碎的可能结果如下：</p>

<ul>
	<li>如果&nbsp;<code>x == y</code>，那么两块石头都会被完全粉碎；</li>
	<li>如果&nbsp;<code>x != y</code>，那么重量为&nbsp;<code>x</code>&nbsp;的石头将会完全粉碎，而重量为&nbsp;<code>y</code>&nbsp;的石头新重量为&nbsp;<code>y-x</code>。</li>
</ul>

<p>最后，最多只会剩下一块石头。返回此石头<strong>最小的可能重量</strong>。如果没有石头剩下，就返回 <code>0</code>。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>[2,7,4,1,8,1]
<strong>输出：</strong>1
<strong>解释：</strong>
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= stones.length &lt;= 30</code></li>
	<li><code>1 &lt;= stones[i] &lt;= 1000</code></li>
</ol>

