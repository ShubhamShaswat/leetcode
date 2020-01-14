#### 两句话中的不常见单词/Uncommon Words from Two Sentences
**难度：** 简单/Easy

**Question：** 

<p>We are given two sentences <code>A</code> and <code>B</code>.&nbsp; (A <em>sentence</em>&nbsp;is a string of space separated words.&nbsp; Each <em>word</em> consists only of lowercase letters.)</p>

<p>A word is <em>uncommon</em>&nbsp;if it appears exactly once in one of the sentences, and does not appear in the other sentence.</p>

<p>Return a list of all uncommon words.&nbsp;</p>

<p>You may return the list in any order.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">&quot;this apple is sweet&quot;</span>, B = <span id="example-input-1-2">&quot;this apple is sour&quot;</span>
<strong>Output: </strong><span id="example-output-1">[&quot;sweet&quot;,&quot;sour&quot;]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">&quot;apple apple&quot;</span>, B = <span id="example-input-2-2">&quot;banana&quot;</span>
<strong>Output: </strong><span id="example-output-2">[&quot;banana&quot;]</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt;= 200</code></li>
	<li><code>0 &lt;= B.length &lt;= 200</code></li>
	<li><code>A</code> and <code>B</code> both contain only spaces and lowercase letters.</li>
</ol>
</div>
</div>


------

**题目：** 
<p>给定两个句子&nbsp;<code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;。&nbsp;（<em>句子</em>是一串由空格分隔的单词。每个<em>单词</em>仅由小写字母组成。）</p>

<p>如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是<em>不常见的</em>。</p>

<p>返回所有不常用单词的列表。</p>

<p>您可以按任何顺序返回列表。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>A = &quot;this apple is sweet&quot;, B = &quot;this apple is sour&quot;
<strong>输出：</strong>[&quot;sweet&quot;,&quot;sour&quot;]
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre><strong>输入：</strong>A = &quot;apple apple&quot;, B = &quot;banana&quot;
<strong>输出：</strong>[&quot;banana&quot;]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt;= 200</code></li>
	<li><code>0 &lt;= B.length &lt;= 200</code></li>
	<li><code>A</code> 和&nbsp;<code>B</code>&nbsp;都只包含空格和小写字母。</li>
</ol>

