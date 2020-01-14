#### 行相等的最少多米诺旋转/Minimum Domino Rotations For Equal Row
**难度：** 中等/Medium

**Question：** 

<p>In a row of dominoes, <code>A[i]</code> and <code>B[i]</code> represent the top and bottom halves of the <code>i</code>-th domino.&nbsp; (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)</p>

<p>We may rotate the <code>i</code>-th domino, so that <code>A[i]</code> and <code>B[i]</code> swap values.</p>

<p>Return the minimum number of rotations so that all the values in <code>A</code> are the same, or all the values in <code>B</code>&nbsp;are the same.</p>

<p>If it cannot be done, return <code>-1</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/03/08/domino.png" style="height: 161px; width: 200px;" /></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[2,1,2,4,2,2]</span>, B = <span id="example-input-1-2">[5,2,6,2,3,2]</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[3,5,1,2,3]</span>, B = <span id="example-input-2-2">[3,6,3,3,4]</span>
<strong>Output: </strong><span id="example-output-2">-1</span>
<strong>Explanation: </strong>
In this case, it is not possible to rotate the dominoes to make one row of values equal.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A[i], B[i] &lt;= 6</code></li>
	<li><code>2 &lt;= A.length == B.length &lt;= 20000</code></li>
</ol>


------

**题目：** 
<p>在一排多米诺骨牌中，<code>A[i]</code> 和 <code>B[i]</code>&nbsp;分别代表第 i 个多米诺骨牌的上半部分和下半部分。（一个多米诺是两个从 1 到 6 的数字同列平铺形成的&nbsp;&mdash;&mdash; 该平铺的每一半上都有一个数字。）</p>

<p>我们可以旋转第&nbsp;<code>i</code>&nbsp;张多米诺，使得&nbsp;<code>A[i]</code> 和&nbsp;<code>B[i]</code>&nbsp;的值交换。</p>

<p>返回能使 <code>A</code> 中所有值或者 <code>B</code> 中所有值都相同的最小旋转次数。</p>

<p>如果无法做到，返回&nbsp;<code>-1</code>.</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/03/08/domino.png" style="height: 161px; width: 200px;"></p>

<pre><strong>输入：</strong>A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
<strong>输出：</strong>2
<strong>解释：</strong>
图一表示：在我们旋转之前， A 和 B 给出的多米诺牌。
如果我们旋转第二个和第四个多米诺骨牌，我们可以使上面一行中的每个值都等于 2，如图二所示。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>A = [3,5,1,2,3], B = [3,6,3,3,4]
<strong>输出：</strong>-1
<strong>解释：</strong>
在这种情况下，不可能旋转多米诺牌使一行的值相等。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A[i], B[i] &lt;= 6</code></li>
	<li><code>2 &lt;= A.length == B.length &lt;= 20000</code></li>
</ol>

