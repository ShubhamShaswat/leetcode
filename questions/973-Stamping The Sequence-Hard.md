#### 戳印序列/Stamping The Sequence
**难度：** 困难/Hard

**Question：** 

<p>You want to form a <code>target</code>&nbsp;string of <strong>lowercase letters</strong>.</p>

<p>At the beginning, your sequence is <code>target.length</code>&nbsp;<code>&#39;?&#39;</code> marks.&nbsp; You also have a <code>stamp</code>&nbsp;of lowercase letters.</p>

<p>On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.&nbsp; You can make up to <code>10 * target.length</code> turns.</p>

<p>For example, if the initial sequence is <font face="monospace">&quot;?????&quot;</font>, and your stamp is <code>&quot;abc&quot;</code>,&nbsp; then you may make <font face="monospace">&quot;abc??&quot;, &quot;?abc?&quot;, &quot;??abc&quot;&nbsp;</font>in the first turn.&nbsp; (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)</p>

<p>If the sequence is possible to stamp, then return an array of&nbsp;the index of the left-most letter being stamped at each turn.&nbsp; If the sequence is not possible to stamp, return an empty array.</p>

<p>For example, if the sequence is <font face="monospace">&quot;ababc&quot;</font>, and the stamp is <code>&quot;abc&quot;</code>, then we could return the answer <code>[0, 2]</code>, corresponding to the moves <font face="monospace">&quot;?????&quot; -&gt; &quot;abc??&quot; -&gt; &quot;ababc&quot;</font>.</p>

<p>Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within <code>10 * target.length</code>&nbsp;moves.&nbsp; Any answers specifying more than this number of moves&nbsp;will not be accepted.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>stamp = <span id="example-input-1-1">&quot;abc&quot;</span>, target = <span id="example-input-1-2">&quot;ababc&quot;</span>
<strong>Output: </strong><span id="example-output-1">[0,2]</span>
([1,0,2] would also be accepted as an answer, as well as some other answers.)
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>stamp = <span id="example-input-2-1">&quot;</span><span id="example-input-2-2">abca</span><span>&quot;</span>, target = <span id="example-input-2-2">&quot;</span><span>aabcaca&quot;</span>
<strong>Output: </strong><span id="example-output-2">[3,0,1]</span>
</pre>

<div>
<p>&nbsp;</p>

<p><strong>Note:</strong></p>
</div>
</div>

<ol>
	<li><code>1 &lt;= stamp.length &lt;= target.length &lt;= 1000</code></li>
	<li><code>stamp</code> and <code>target</code> only contain lowercase letters.</li>
</ol>

------

**题目：** 
<p>你想要用<strong>小写字母</strong>组成一个目标字符串&nbsp;<code>target</code>。&nbsp;</p>

<p>开始的时候，序列由&nbsp;<code>target.length</code>&nbsp;个&nbsp;<code>&#39;?&#39;</code>&nbsp;记号组成。而你有一个小写字母印章&nbsp;<code>stamp</code>。</p>

<p>在每个回合，你可以将印章放在序列上，并将序列中的每个字母替换为印章上的相应字母。你最多可以进行&nbsp;<code>10 * target.length</code>&nbsp; 个回合。</p>

<p>举个例子，如果初始序列为 &quot;?????&quot;，而你的印章 <code>stamp</code>&nbsp;是&nbsp;<code>&quot;abc&quot;</code>，那么在第一回合，你可以得到&nbsp;&quot;abc??&quot;、&quot;?abc?&quot;、&quot;??abc&quot;。（请注意，印章必须完全包含在序列的边界内才能盖下去。）</p>

<p>如果可以印出序列，那么返回一个数组，该数组由每个回合中被印下的最左边字母的索引组成。如果不能印出序列，就返回一个空数组。</p>

<p>例如，如果序列是 &quot;ababc&quot;，印章是 <code>&quot;abc&quot;</code>，那么我们就可以返回与操作&nbsp;&quot;?????&quot; -&gt; &quot;abc??&quot; -&gt; &quot;ababc&quot; 相对应的答案 <code>[0, 2]</code>；</p>

<p>另外，如果可以印出序列，那么需要保证可以在 <code>10 * target.length</code>&nbsp;个回合内完成。任何超过此数字的答案将不被接受。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>stamp = &quot;abc&quot;, target = &quot;ababc&quot;
<strong>输出：</strong>[0,2]
（[1,0,2] 以及其他一些可能的结果也将作为答案被接受）
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>stamp = &quot;abca&quot;, target = &quot;aabcaca&quot;
<strong>输出：</strong>[3,0,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= stamp.length &lt;= target.length &lt;= 1000</code></li>
	<li><code>stamp</code> 和&nbsp;<code>target</code>&nbsp;只包含小写字母。</li>
</ol>

