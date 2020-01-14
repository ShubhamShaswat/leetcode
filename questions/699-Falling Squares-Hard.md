#### 掉落的方块/Falling Squares
**难度：** 困难/Hard

**Question：** 

<p>On an infinite number line (x-axis), we drop given squares in the order they are given.</p>

<p>The <code>i</code>-th square dropped (<code>positions[i] = (left, side_length)</code>) is a square with the left-most point being <code>positions[i][0]</code> and sidelength <code>positions[i][1]</code>.</p>

<p>The square is dropped with the bottom edge parallel to the number line, and from a higher height than all currently landed squares. We wait for each square to stick before dropping the next.</p>

<p>The squares are infinitely sticky on their bottom edge, and will remain fixed to any positive length surface they touch (either the number line or another square). Squares dropped adjacent to each other will not stick together prematurely.</p>
&nbsp;

<p>Return a list <code>ans</code> of heights. Each height <code>ans[i]</code> represents the current highest height of any square we have dropped, after dropping squares represented by <code>positions[0], positions[1], ..., positions[i]</code>.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [[1, 2], [2, 3], [6, 1]]
<b>Output:</b> [2, 5, 5]
<b>Explanation:</b>
</pre>

<p>After the first drop of <code>positions[0] = [1, 2]: _aa _aa ------- </code>The maximum height of any square is 2.</p>

<p>After the second drop of <code>positions[1] = [2, 3]: __aaa __aaa __aaa _aa__ _aa__ -------------- </code>The maximum height of any square is 5. The larger square stays on top of the smaller square despite where its center of gravity is, because squares are infinitely sticky on their bottom edge.</p>

<p>After the third drop of <code>positions[1] = [6, 1]: __aaa __aaa __aaa _aa _aa___a -------------- </code>The maximum height of any square is still 5. Thus, we return an answer of <code>[2, 5, 5]</code>.</p>

<p>&nbsp;</p>
&nbsp;

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [[100, 100], [200, 100]]
<b>Output:</b> [100, 100]
<b>Explanation:</b> Adjacent squares don&#39;t get stuck prematurely - only their bottom edge can stick to surfaces.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ul>
	<li><code>1 &lt;= positions.length &lt;= 1000</code>.</li>
	<li><code>1 &lt;= positions[i][0] &lt;= 10^8</code>.</li>
	<li><code>1 &lt;= positions[i][1] &lt;= 10^6</code>.</li>
</ul>

<p>&nbsp;</p>


------

**题目：** 
<p>在无限长的数轴（即 x 轴）上，我们根据给定的顺序放置对应的正方形方块。</p>

<p>第 <code>i</code> 个掉落的方块（<code>positions[i] = (left, side_length)</code>）是正方形，其中&nbsp;<code>left 表示该方块最左边的点位置(positions[i][0])，side_length 表示该方块的边长(positions[i][1])。</code></p>

<p>每个方块的底部边缘平行于数轴（即 x 轴），并且从一个比目前所有的落地方块更高的高度掉落而下。在上一个方块结束掉落，并保持静止后，才开始掉落新方块。</p>

<p>方块的底边具有非常大的粘性，并将保持固定在它们所接触的任何长度表面上（无论是数轴还是其他方块）。邻接掉落的边不会过早地粘合在一起，<code>因为只有底边才具有粘性。</code></p>

<p>&nbsp;</p>

<p>返回一个堆叠高度列表&nbsp;<code>ans</code> 。每一个堆叠高度&nbsp;<code>ans[i]</code>&nbsp;表示在通过&nbsp;<code>positions[0], positions[1], ..., positions[i]</code>&nbsp;表示的方块掉落结束后，目前所有已经落稳的方块堆叠的最高高度。</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> [[1, 2], [2, 3], [6, 1]]
<strong>输出:</strong> [2, 5, 5]
<strong>解释:

</strong>第一个方块 <code>positions[0] = [1, 2] </code>掉落：
<code>_aa
_aa
-------
</code>方块最大高度为 2 。

第二个方块 <code>positions[1] = [2, 3] </code>掉落：
<code>__aaa
__aaa
__aaa
_aa__
_aa__
--------------
</code>方块最大高度为5。
大的方块保持在较小的方块的顶部，不论它的重心在哪里，因为方块的底部边缘有非常大的粘性。

第三个方块 <code>positions[1] = [6, 1] </code>掉落：
<code>__aaa
__aaa
__aaa
_aa
_aa___a
-------------- 
</code>方块最大高度为5。

因此，我们返回结果<code>[2, 5, 5]。</code>
</pre>

<p>&nbsp;</p>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> [[100, 100], [200, 100]]
<strong>输出:</strong> [100, 100]
<strong>解释:</strong> 相邻的方块不会过早地卡住，只有它们的底部边缘才能粘在表面上。
</pre>

<p>&nbsp;</p>

<p><strong>注意:</strong></p>

<ul>
	<li><code>1 &lt;= positions.length &lt;= 1000</code>.</li>
	<li><code>1 &lt;= positions[i][0] &lt;= 10^8</code>.</li>
	<li><code>1 &lt;= positions[i][1] &lt;= 10^6</code>.</li>
</ul>

<p>&nbsp;</p>

