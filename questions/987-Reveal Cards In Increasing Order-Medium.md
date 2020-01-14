#### 按递增顺序显示卡牌/Reveal Cards In Increasing Order
**难度：** 中等/Medium

**Question：** 

<p>In a deck of cards, every card has a unique integer.&nbsp; You can order the deck in&nbsp;any order you want.</p>

<p>Initially, all the cards start face down (unrevealed) in one deck.</p>

<p>Now, you do the following steps repeatedly, until all cards are revealed:</p>

<ol>
	<li>Take the top card of the deck, reveal it, and take it out of the deck.</li>
	<li>If there are still cards in the deck, put the next top card of the deck at&nbsp;the bottom of the deck.</li>
	<li>If there are still unrevealed cards, go back to step 1.&nbsp; Otherwise, stop.</li>
</ol>

<p>Return an ordering of the deck that would reveal the cards&nbsp;in <strong>increasing order.</strong></p>

<p>The first entry in the answer is considered to be the top of the deck.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[17,13,11,2,3,5,7]</span>
<strong>Output: </strong><span id="example-output-1">[2,13,3,11,5,17,7]</span>
<strong>Explanation: </strong>
We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter), and reorder it.
After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
We reveal 13, and move 17 to the bottom.  The deck is now [17].
We reveal 17.
Since all the cards revealed are in increasing order, the answer is correct.
</pre>

<div>
<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 1000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 10^6</code></li>
	<li><code>A[i] != A[j]</code>&nbsp;for all&nbsp;<code>i != j</code></li>
</ol>
</div>
</div>


------

**题目：** 
<p>牌组中的每张卡牌都对应有一个唯一的整数。你可以按你想要的顺序对这套卡片进行排序。</p>

<p>最初，这些卡牌在牌组里是正面朝下的（即，未显示状态）。</p>

<p>现在，重复执行以下步骤，直到显示所有卡牌为止：</p>

<ol>
	<li>从牌组顶部抽一张牌，显示它，然后将其从牌组中移出。</li>
	<li>如果牌组中仍有牌，则将下一张处于牌组顶部的牌放在牌组的底部。</li>
	<li>如果仍有未显示的牌，那么返回步骤 1。否则，停止行动。</li>
</ol>

<p>返回能以<strong>递增顺序</strong>显示卡牌的牌组顺序。</p>

<p>答案中的第一张牌被认为处于牌堆顶部。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>[17,13,11,2,3,5,7]
<strong>输出：</strong>[2,13,3,11,5,17,7]
<strong>解释：
</strong>我们得到的牌组顺序为 [17,13,11,2,3,5,7]（这个顺序不重要），然后将其重新排序。
重新排序后，牌组以 [2,13,3,11,5,17,7] 开始，其中 2 位于牌组的顶部。
我们显示 2，然后将 13 移到底部。牌组现在是 [3,11,5,17,7,13]。
我们显示 3，并将 11 移到底部。牌组现在是 [5,17,7,13,11]。
我们显示 5，然后将 17 移到底部。牌组现在是 [7,13,11,17]。
我们显示 7，并将 13 移到底部。牌组现在是 [11,17,13]。
我们显示 11，然后将 17 移到底部。牌组现在是 [13,17]。
我们展示 13，然后将 17 移到底部。牌组现在是 [17]。
我们显示 17。
由于所有卡片都是按递增顺序排列显示的，所以答案是正确的。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 1000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 10^6</code></li>
	<li>对于所有的&nbsp;<code>i != j</code>，<code>A[i] != A[j]</code></li>
</ol>

