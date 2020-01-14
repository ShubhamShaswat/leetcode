#### 卡牌分组/X of a Kind in a Deck of Cards
**难度：** 简单/Easy

**Question：** 

<p>In a deck of cards, each card has an integer written on it.</p>

<p>Return <code>true</code> if and only if you can choose&nbsp;<code>X &gt;= 2</code> such that&nbsp;it is possible to split the entire deck&nbsp;into 1 or more groups of cards, where:</p>

<ul>
	<li>Each group has exactly <code>X</code> cards.</li>
	<li>All the cards in each group have the same integer.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,3,4,4,3,2,1]</span>
<strong>Output: </strong><span id="example-output-1">true
<strong>Explanation</strong>: Possible partition [1,1],[2,2],[3,3],[4,4]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,1,1,2,2,2,3,3]</span>
<strong>Output: </strong><span id="example-output-2">false
</span><span id="example-output-1"><strong>Explanation</strong>: No possible partition.</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[1]</span>
<strong>Output: </strong><span id="example-output-3">false
</span><span id="example-output-1"><strong>Explanation</strong>: No possible partition.</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[1,1]</span>
<strong>Output: </strong><span id="example-output-4">true
</span><span id="example-output-1"><strong>Explanation</strong>: Possible partition [1,1]</span>
</pre>

<div>
<p><strong>Example 5:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-5-1">[1,1,2,2,2,2]</span>
<strong>Output: </strong><span id="example-output-5">true
</span><span id="example-output-1"><strong>Explanation</strong>: Possible partition [1,1],[2,2],[2,2]</span>
</pre>
</div>
</div>
</div>
</div>

<p><br />
<strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= deck.length &lt;= 10000</code></li>
	<li><code>0 &lt;= deck[i] &lt;&nbsp;10000</code></li>
</ol>

<div>
<div>
<div>
<div>
<div>&nbsp;</div>
</div>
</div>
</div>
</div>


------

**题目：** 
<p>给定一副牌，每张牌上都写着一个整数。</p>

<p>此时，你需要选定一个数字 <code>X</code>，使我们可以将整副牌按下述规则分成 1 组或更多组：</p>

<ul>
	<li>每组都有&nbsp;<code>X</code>&nbsp;张牌。</li>
	<li>组内所有的牌上都写着相同的整数。</li>
</ul>

<p>仅当你可选的 <code>X &gt;= 2</code> 时返回&nbsp;<code>true</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[1,2,3,4,4,3,2,1]
<strong>输出：</strong>true
<strong>解释：</strong>可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[1,1,1,2,2,2,3,3]
<strong>输出：</strong>false
<strong>解释：</strong>没有满足要求的分组。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[1]
<strong>输出：</strong>false
<strong>解释：</strong>没有满足要求的分组。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>[1,1]
<strong>输出：</strong>true
<strong>解释：</strong>可行的分组是 [1,1]
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>[1,1,2,2,2,2]
<strong>输出：</strong>true
<strong>解释：</strong>可行的分组是 [1,1]，[2,2]，[2,2]
</pre>

<p><br>
<strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= deck.length &lt;= 10000</code></li>
	<li><code>0 &lt;= deck[i] &lt;&nbsp;10000</code></li>
</ol>

<p>&nbsp;</p>

