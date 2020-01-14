#### 最长字符串链/Longest String Chain
**难度：** 中等/Medium

**Question：** 

<p>Given a list of words, each word consists of English lowercase letters.</p>

<p>Let&#39;s say <code>word1</code> is a predecessor of <code>word2</code>&nbsp;if and only if we can add exactly one letter anywhere in <code>word1</code> to make it equal to <code>word2</code>.&nbsp; For example,&nbsp;<code>&quot;abc&quot;</code>&nbsp;is a predecessor of <code>&quot;abac&quot;</code>.</p>

<p>A <em>word chain&nbsp;</em>is a sequence of words <code>[word_1, word_2, ..., word_k]</code>&nbsp;with <code>k &gt;= 1</code>,&nbsp;where <code>word_1</code> is a predecessor of <code>word_2</code>, <code>word_2</code> is a predecessor of <code>word_3</code>, and so on.</p>

<p>Return the longest possible length of a word chain with words chosen from the given list of <code>words</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;a&quot;,&quot;b&quot;,&quot;ba&quot;,&quot;bca&quot;,&quot;bda&quot;,&quot;bdca&quot;]</span>
<strong>Output: </strong><span id="example-output-1">4
<strong>Explanation</strong>: one of </span>the longest word chain is &quot;a&quot;,&quot;ba&quot;,&quot;bda&quot;,&quot;bdca&quot;.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 16</code></li>
	<li><code>words[i]</code> only consists of English lowercase letters.</li>
</ol>

<div>
<p>&nbsp;</p>
</div>

------

**题目：** 
<p>给出一个单词列表，其中每个单词都由小写英文字母组成。</p>

<p>如果我们可以在&nbsp;<code>word1</code>&nbsp;的任何地方添加一个字母使其变成&nbsp;<code>word2</code>，那么我们认为&nbsp;<code>word1</code>&nbsp;是&nbsp;<code>word2</code>&nbsp;的前身。例如，<code>&quot;abc&quot;</code>&nbsp;是&nbsp;<code>&quot;abac&quot;</code>&nbsp;的前身。</p>

<p><strong>词链</strong>是单词&nbsp;<code>[word_1, word_2, ..., word_k]</code>&nbsp;组成的序列，<code>k &gt;= 1</code>，其中&nbsp;<code>word_1</code>&nbsp;是&nbsp;<code>word_2</code>&nbsp;的前身，<code>word_2</code>&nbsp;是&nbsp;<code>word_3</code>&nbsp;的前身，依此类推。</p>

<p>从给定单词列表 <code>words</code> 中选择单词组成词链，返回词链的最长可能长度。<br>
&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>[&quot;a&quot;,&quot;b&quot;,&quot;ba&quot;,&quot;bca&quot;,&quot;bda&quot;,&quot;bdca&quot;]
<strong>输出：</strong>4
<strong>解释：</strong>最长单词链之一为 &quot;a&quot;,&quot;ba&quot;,&quot;bda&quot;,&quot;bdca&quot;。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 16</code></li>
	<li><code>words[i]</code>&nbsp;仅由小写英文字母组成。</li>
</ol>

<p>&nbsp;</p>

