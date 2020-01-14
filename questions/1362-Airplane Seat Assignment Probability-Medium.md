#### 飞机座位分配概率/Airplane Seat Assignment Probability
**难度：** 中等/Medium

**Question：** 

<p><code data-stringify-type="code">n</code>&nbsp;passengers board an airplane with exactly&nbsp;<code data-stringify-type="code">n</code>&nbsp;seats. The first passenger has lost the ticket and picks a seat randomly. But after that, the rest of passengers will:</p>

<ul>
	<li>Take their own seat if it is still available,&nbsp;</li>
	<li>Pick other seats randomly when they find their seat occupied&nbsp;</li>
</ul>

<p>What is the probability that the n-th person can get his own seat?</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1.00000
<strong>Explanation: </strong>The first person can only get the first seat.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 0.50000
<strong>Explanation: </strong>The second person has a probability of 0.5 to get the second seat (when first person gets the first seat).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10^5</code></li>
</ul>

------

**题目：** 
<p>有 <code>n</code> 位乘客即将登机，飞机正好有 <code>n</code> 个座位。第一位乘客的票丢了，他随便选了一个座位坐下。</p>

<p>剩下的乘客将会：</p>

<ul>
	<li>
	<p>如果他们自己的座位还空着，就坐到自己的座位上，</p>
	</li>
	<li>当他们自己的座位被占用时，随机选择其他座位</li>
</ul>

<p>第 <code>n</code>&nbsp;位乘客坐在自己的座位上的概率是多少？</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>1.00000
<strong>解释：</strong>第一个人只会坐在自己的位置上。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> n = 2
<strong>输出:</strong> 0.50000
<strong>解释：</strong>在第一个人选好座位坐下后，第二个人坐在自己的座位上的概率是 0.5。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10^5</code></li>
</ul>

