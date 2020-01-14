#### 猜字谜/Number of Valid Words for Each Puzzle
**难度：** 困难/Hard

**Question：** 

With respect to a given <code>puzzle</code> string, a <code>word</code> is <em>valid</em>&nbsp;if both the following conditions are satisfied:
<ul>
	<li><code>word</code> contains the first letter of <code>puzzle</code>.</li>
	<li>For each letter in <code>word</code>, that letter is in <code>puzzle</code>.<br />
	For example, if the puzzle is &quot;abcdefg&quot;, then valid words are &quot;faced&quot;, &quot;cabbage&quot;, and &quot;baggage&quot;; while invalid words are &quot;beefed&quot; (doesn&#39;t include &quot;a&quot;) and &quot;based&quot; (includes &quot;s&quot; which isn&#39;t in the puzzle).</li>
</ul>
Return an array <code>answer</code>, where <code>answer[i]</code> is the number of words in the given word list&nbsp;<code>words</code> that are valid with respect to the puzzle <code>puzzles[i]</code>.
<p>&nbsp;</p>
<p><strong>Example :</strong></p>

<pre>
<strong>Input:</strong> 
words = [&quot;aaaa&quot;,&quot;asas&quot;,&quot;able&quot;,&quot;ability&quot;,&quot;actt&quot;,&quot;actor&quot;,&quot;access&quot;], 
puzzles = [&quot;aboveyz&quot;,&quot;abrodyz&quot;,&quot;abslute&quot;,&quot;absoryz&quot;,&quot;actresz&quot;,&quot;gaswxyz&quot;]
<strong>Output:</strong> [1,1,3,2,4,0]
<strong>Explanation:</strong>
1 valid word&nbsp;for &quot;aboveyz&quot; : &quot;aaaa&quot; 
1 valid word&nbsp;for &quot;abrodyz&quot; : &quot;aaaa&quot;
3 valid words for &quot;abslute&quot; : &quot;aaaa&quot;, &quot;asas&quot;, &quot;able&quot;
2 valid words for&nbsp;&quot;absoryz&quot; : &quot;aaaa&quot;, &quot;asas&quot;
4 valid words for&nbsp;&quot;actresz&quot; : &quot;aaaa&quot;, &quot;asas&quot;, &quot;actt&quot;, &quot;access&quot;
There&#39;re&nbsp;no valid words for&nbsp;&quot;gaswxyz&quot; cause none of the words in the list contains letter &#39;g&#39;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 10^5</code></li>
	<li><code>4 &lt;= words[i].length &lt;= 50</code></li>
	<li><code>1 &lt;= puzzles.length &lt;= 10^4</code></li>
	<li><code>puzzles[i].length == 7</code></li>
	<li><code>words[i][j]</code>, <code>puzzles[i][j]</code> are English lowercase letters.</li>
	<li>Each <code>puzzles[i] </code>doesn&#39;t contain repeated characters.</li>
</ul>


------

**题目：** 
<p>外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。</p>

<p>字谜的迷面&nbsp;<code>puzzle</code> 按字符串形式给出，如果一个单词&nbsp;<code>word</code>&nbsp;符合下面两个条件，那么它就可以算作谜底：</p>

<ul>
	<li>单词&nbsp;<code>word</code>&nbsp;中包含谜面&nbsp;<code>puzzle</code>&nbsp;的第一个字母。</li>
	<li>单词&nbsp;<code>word</code>&nbsp;中的每一个字母都可以在谜面&nbsp;<code>puzzle</code>&nbsp;中找到。<br>
	例如，如果字谜的谜面是 &quot;abcdefg&quot;，那么可以作为谜底的单词有 &quot;faced&quot;, &quot;cabbage&quot;, 和 &quot;baggage&quot;；而 &quot;beefed&quot;（不含字母 &quot;a&quot;）以及&nbsp;&quot;based&quot;（其中的 &quot;s&quot; 没有出现在谜面中）。</li>
</ul>

<p>返回一个答案数组&nbsp;<code>answer</code>，数组中的每个元素&nbsp;<code>answer[i]</code>&nbsp;是在给出的单词列表 <code>words</code> 中可以作为字谜迷面&nbsp;<code>puzzles[i]</code>&nbsp;所对应的谜底的单词数目。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>
words = [&quot;aaaa&quot;,&quot;asas&quot;,&quot;able&quot;,&quot;ability&quot;,&quot;actt&quot;,&quot;actor&quot;,&quot;access&quot;], 
puzzles = [&quot;aboveyz&quot;,&quot;abrodyz&quot;,&quot;abslute&quot;,&quot;absoryz&quot;,&quot;actresz&quot;,&quot;gaswxyz&quot;]
<strong>输出：</strong>[1,1,3,2,4,0]
<strong>解释：</strong>
1 个单词可以作为 &quot;aboveyz&quot; 的谜底 : &quot;aaaa&quot; 
1 个单词可以作为 &quot;abrodyz&quot; 的谜底 : &quot;aaaa&quot;
3 个单词可以作为 &quot;abslute&quot; 的谜底 : &quot;aaaa&quot;, &quot;asas&quot;, &quot;able&quot;
2 个单词可以作为&nbsp;&quot;absoryz&quot; 的谜底 : &quot;aaaa&quot;, &quot;asas&quot;
4 个单词可以作为&nbsp;&quot;actresz&quot; 的谜底 : &quot;aaaa&quot;, &quot;asas&quot;, &quot;actt&quot;, &quot;access&quot;
没有单词可以作为&nbsp;&quot;gaswxyz&quot; 的谜底，因为列表中的单词都不含字母 &#39;g&#39;。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 10^5</code></li>
	<li><code>4 &lt;= words[i].length &lt;= 50</code></li>
	<li><code>1 &lt;= puzzles.length &lt;= 10^4</code></li>
	<li><code>puzzles[i].length == 7</code></li>
	<li><code>words[i][j]</code>, <code>puzzles[i][j]</code>&nbsp;都是小写英文字母。</li>
	<li>每个&nbsp;<code>puzzles[i]</code>&nbsp;所包含的字符都不重复。</li>
</ul>

