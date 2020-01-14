#### 掷骰子的N种方法/Number of Dice Rolls With Target Sum
**难度：** 中等/Medium

**Question：** 

<p>You have <code>d</code> dice, and each die has <code>f</code> faces numbered <code>1, 2, ..., f</code>.</p>

<p>Return the number of possible ways (out of <code>f<sup>d</sup></code>&nbsp;total ways) <strong>modulo <code>10^9 + 7</code></strong> to roll the dice so the sum of the face up numbers equals <code>target</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> d = 1, f = 6, target = 3
<strong>Output:</strong> 1
<strong>Explanation: </strong>
You throw one die with 6 faces.  There is only one way to get a sum of 3.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> d = 2, f = 6, target = 7
<strong>Output:</strong> 6
<strong>Explanation: </strong>
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> d = 2, f = 5, target = 10
<strong>Output:</strong> 1
<strong>Explanation: </strong>
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> d = 1, f = 2, target = 3
<strong>Output:</strong> 0
<strong>Explanation: </strong>
You throw one die with 2 faces.  There is no way to get a sum of 3.
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> d = 30, f = 30, target = 500
<strong>Output:</strong> 222616187
<strong>Explanation: </strong>
The answer must be returned modulo 10^9 + 7.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= d, f &lt;= 30</code></li>
	<li><code>1 &lt;= target &lt;= 1000</code></li>
</ul>

------

**题目：** 
<p>这里有&nbsp;<code>d</code>&nbsp;个一样的骰子，每个骰子上都有&nbsp;<code>f</code>&nbsp;个面，分别标号为&nbsp;<code>1, 2, ..., f</code>。</p>

<p>我们约定：掷骰子的得到总点数为各骰子面朝上的数字的总和。</p>

<p>如果需要掷出的总点数为&nbsp;<code>target</code>，请你计算出有多少种不同的组合情况（所有的组合情况总共有 <code>f^d</code> 种），<strong>模&nbsp;<code>10^9 + 7</code></strong>&nbsp;后返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>d = 1, f = 6, target = 3
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>d = 2, f = 6, target = 7
<strong>输出：</strong>6
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>d = 2, f = 5, target = 10
<strong>输出：</strong>1
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>d = 1, f = 2, target = 3
<strong>输出：</strong>0
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>d = 30, f = 30, target = 500
<strong>输出：</strong>222616187</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= d, f &lt;= 30</code></li>
	<li><code>1 &lt;= target &lt;= 1000</code></li>
</ul>

