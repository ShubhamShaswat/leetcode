#### 查询无效交易/Invalid Transactions
**难度：** 中等/Medium

**Question：** 

<p>A transaction is <em>possibly invalid</em> if:</p>

<ul>
	<li>the amount exceeds $1000, or;</li>
	<li>if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.</li>
</ul>

<p>Each transaction string <code>transactions[i]</code>&nbsp;consists of&nbsp;comma separated values representing&nbsp;the name, time (in minutes), amount, and city of the transaction.</p>

<p>Given a list of <code>transactions</code>,&nbsp;return a list of transactions that are possibly invalid.&nbsp; You may return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> transactions = [&quot;alice,20,800,mtv&quot;,&quot;alice,50,100,beijing&quot;]
<strong>Output:</strong> [&quot;alice,20,800,mtv&quot;,&quot;alice,50,100,beijing&quot;]
<strong>Explanation:</strong> The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> transactions = [&quot;alice,20,800,mtv&quot;,&quot;alice,50,1200,mtv&quot;]
<strong>Output:</strong> [&quot;alice,50,1200,mtv&quot;]
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> transactions = [&quot;alice,20,800,mtv&quot;,&quot;bob,50,1200,mtv&quot;]
<strong>Output:</strong> [&quot;bob,50,1200,mtv&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>transactions.length &lt;= 1000</code></li>
	<li>Each <code>transactions[i]</code> takes the form <code>&quot;{name},{time},{amount},{city}&quot;</code></li>
	<li>Each <code>{name}</code> and <code>{city}</code>&nbsp;consist of&nbsp;lowercase English letters, and have lengths between <code>1</code> and <code>10</code>.</li>
	<li>Each <code>{time}</code> consist of&nbsp;digits, and represent an integer between <code>0</code> and <code>1000</code>.</li>
	<li>Each <code>{amount}</code>&nbsp;consist of&nbsp;digits, and represent an integer between <code>0</code> and <code>2000</code>.</li>
</ul>


------

**题目：** 
<p>如果出现下述两种情况，交易 <strong>可能无效</strong>：</p>

<ul>
	<li>交易金额超过 &yen;1000</li>
	<li>或者，它和另一个城市中同名的另一笔交易相隔不超过 60 分钟（包含 60 分钟整）</li>
</ul>

<p>每个交易字符串&nbsp;<code>transactions[i]</code>&nbsp;由一些用逗号分隔的值组成，这些值分别表示交易的名称，时间（以分钟计），金额以及城市。</p>

<p>给你一份交易清单&nbsp;<code>transactions</code>，返回可能无效的交易列表。你可以按任何顺序返回答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>transactions = [&quot;alice,20,800,mtv&quot;,&quot;alice,50,100,beijing&quot;]
<strong>输出：</strong>[&quot;alice,20,800,mtv&quot;,&quot;alice,50,100,beijing&quot;]
<strong>解释：</strong>第一笔交易是无效的，因为第二笔交易和它间隔不超过 60 分钟、名称相同且发生在不同的城市。同样，第二笔交易也是无效的。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>transactions = [&quot;alice,20,800,mtv&quot;,&quot;alice,50,1200,mtv&quot;]
<strong>输出：</strong>[&quot;alice,50,1200,mtv&quot;]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>transactions = [&quot;alice,20,800,mtv&quot;,&quot;bob,50,1200,mtv&quot;]
<strong>输出：</strong>[&quot;bob,50,1200,mtv&quot;]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>transactions.length &lt;= 1000</code></li>
	<li>每笔交易&nbsp;<code>transactions[i]</code>&nbsp;按&nbsp;<code>&quot;{name},{time},{amount},{city}&quot;</code>&nbsp;的格式进行记录</li>
	<li>每个交易名称&nbsp;<code>{name}</code>&nbsp;和城市&nbsp;<code>{city}</code>&nbsp;都由小写英文字母组成，长度在&nbsp;<code>1</code>&nbsp;到&nbsp;<code>10</code>&nbsp;之间</li>
	<li>每个交易时间&nbsp;<code>{time}</code>&nbsp;由一些数字组成，表示一个&nbsp;<code>0</code>&nbsp;到&nbsp;<code>1000</code>&nbsp;之间的整数</li>
	<li>每笔交易金额&nbsp;<code>{amount}</code>&nbsp;由一些数字组成，表示一个&nbsp;<code>0</code> 到&nbsp;<code>2000</code>&nbsp;之间的整数</li>
</ul>

