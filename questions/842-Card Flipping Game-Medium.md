#### 翻转卡片游戏/Card Flipping Game
**难度：** 中等/Medium

**Question：** 

<p>On a table are <code>N</code> cards, with a positive integer printed on the front and back of each card (possibly different).</p>

<p>We flip any number of cards, and after we choose one&nbsp;card.&nbsp;</p>

<p>If the number <code>X</code> on the back of the chosen&nbsp;card is not on the front of any card, then this number X is good.</p>

<p>What is the smallest number that is good?&nbsp; If no number is good, output <code>0</code>.</p>

<p>Here, <code>fronts[i]</code> and <code>backs[i]</code> represent the number on the front and back of card <code>i</code>.&nbsp;</p>

<p>A&nbsp;flip swaps the front and back numbers, so the value on the front is now on the back and vice versa.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
<strong>Output:</strong> <code>2</code>
<strong>Explanation:</strong> If we flip the second card, the fronts are <code>[1,3,4,4,7]</code> and the backs are <code>[1,2,4,1,3]</code>.
We choose the second card, which has number 2 on the back, and it isn&#39;t on the front of any card, so <code>2</code> is good.</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= fronts.length == backs.length&nbsp;&lt;=&nbsp;1000</code>.</li>
	<li><code>1 &lt;=&nbsp;fronts[i]&nbsp;&lt;= 2000</code>.</li>
	<li><code>1 &lt;= backs[i]&nbsp;&lt;= 2000</code>.</li>
</ol>


------

**题目：** 
<p>在桌子上有 <code>N</code> 张卡片，每张卡片的正面和背面都写着一个正数（正面与背面上的数有可能不一样）。</p>

<p>我们可以先翻转任意张卡片，然后选择其中一张卡片。</p>

<p>如果选中的那张卡片背面的数字 <code>X</code> 与任意一张卡片的正面的数字都不同，那么这个数字是我们想要的数字。</p>

<p>哪个数是这些想要的数字中最小的数（找到这些数中的最小值）呢？如果没有一个数字符合要求的，输出 0。</p>

<p>其中, <code>fronts[i]</code>&nbsp;和&nbsp;<code>backs[i]</code>&nbsp;分别代表第&nbsp;<code>i</code>&nbsp;张卡片的正面和背面的数字。</p>

<p>如果我们通过翻转卡片来交换正面与背面上的数，那么当初在正面的数就变成背面的数，背面的数就变成正面的数。</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
<strong>输出：</strong><code>2</code>
<strong>解释：</strong>假设我们翻转第二张卡片，那么在正面的数变成了 <code>[1,3,4,4,7]</code> ， 背面的数变成了 <code>[1,2,4,1,3]。</code>
接着我们选择第二张卡片，因为现在该卡片的背面的数是 2，2 与任意卡片上正面的数都不同，所以 2 就是我们想要的数字。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= fronts.length == backs.length&nbsp;&lt;=&nbsp;1000</code></li>
	<li><code>1 &lt;=&nbsp;fronts[i]&nbsp;&lt;= 2000</code></li>
	<li><code>1 &lt;= backs[i]&nbsp;&lt;= 2000</code></li>
</ol>

