#### 令牌放置/Bag of Tokens
**难度：** 中等/Medium

**Question：** 

<p>You have an initial power <code>P</code>, an initial score of <code>0</code> points, and a bag of tokens.</p>

<p>Each token can be used at most once, has a value <code>token[i]</code>, and has potentially two ways to use it.</p>

<ul>
	<li>If we have at least <code>token[i]</code> power, we may play the token face up, losing <code>token[i]</code> power, and gaining <code>1</code> point.</li>
	<li>If we have at least <code>1</code> point, we may play the token face down, gaining <code>token[i]</code> power, and losing <code>1</code> point.</li>
</ul>

<p>Return the largest number of points we can have after playing any number of tokens.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>tokens = <span id="example-input-1-1">[100]</span>, P = <span id="example-input-1-2">50</span>
<strong>Output: </strong><span id="example-output-1">0</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>tokens = <span id="example-input-2-1">[100,200]</span>, P = <span id="example-input-2-2">150</span>
<strong>Output: </strong><span id="example-output-2">1</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>tokens = <span id="example-input-3-1">[100,200,300,400]</span>, P = <span id="example-input-3-2">200</span>
<strong>Output: </strong><span id="example-output-3">2</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>tokens.length &lt;= 1000</code></li>
	<li><code>0 &lt;= tokens[i] &lt; 10000</code></li>
	<li><code>0 &lt;= P &lt; 10000</code></li>
</ol>
</div>
</div>
</div>


------

**题目：** 
<p>你的初始能量为&nbsp;<code>P</code>，初始分数为&nbsp;<code>0</code>，只有一包令牌。</p>

<p>令牌的值为&nbsp;<code>token[i]</code>，每个令牌最多只能使用一次，可能的两种使用方法如下：</p>

<ul>
	<li>如果你至少有&nbsp;<code>token[i]</code>&nbsp;点能量，可以将令牌置为正面朝上，失去&nbsp;<code>token[i]</code>&nbsp;点能量，并得到&nbsp;<code>1</code>&nbsp;分。</li>
	<li>如果我们至少有&nbsp;<code>1</code>&nbsp;分，可以将令牌置为反面朝上，获得&nbsp;<code>token[i]</code>&nbsp;点能量，并失去&nbsp;<code>1</code>&nbsp;分。</li>
</ul>

<p>在使用任意数量的令牌后，返回我们可以得到的最大分数。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>tokens = [100], P = 50
<strong>输出：</strong>0
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>tokens = [100,200], P = 150
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>tokens = [100,200,300,400], P = 200
<strong>输出：</strong>2
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>tokens.length &lt;= 1000</code></li>
	<li><code>0 &lt;= tokens[i] &lt; 10000</code></li>
	<li><code>0 &lt;= P &lt; 10000</code></li>
</ol>

