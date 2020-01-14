#### Bigram 分词/Occurrences After Bigram
**难度：** 简单/Easy

**Question：** 

<p>Given words <code>first</code> and <code>second</code>, consider occurrences in some&nbsp;<code>text</code> of the form &quot;<code>first second third</code>&quot;, where <code>second</code> comes immediately after <code>first</code>, and <code>third</code> comes immediately after <code>second</code>.</p>

<p>For each such occurrence, add &quot;<code>third</code>&quot; to the answer, and return the answer.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>text = <span id="example-input-1-1">&quot;alice is a good girl she is a good student&quot;</span>, first = <span id="example-input-1-2">&quot;a&quot;</span>, second = <span id="example-input-1-3">&quot;good&quot;</span>
<strong>Output: </strong><span id="example-output-1">[&quot;girl&quot;,&quot;student&quot;]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>text = <span id="example-input-2-1">&quot;we will we will rock you&quot;</span>, first = <span id="example-input-2-2">&quot;we&quot;</span>, second = <span id="example-input-2-3">&quot;will&quot;</span>
<strong>Output: </strong><span id="example-output-2">[&quot;we&quot;,&quot;rock&quot;]</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= text.length &lt;= 1000</code></li>
	<li><code>text</code> consists of space separated words, where each word consists of lowercase English letters.</li>
	<li><code>1 &lt;= first.length, second.length &lt;= 10</code></li>
	<li><code>first</code> and <code>second</code> consist of lowercase English letters.</li>
</ol>
</div>


------

**题目：** 
<p>给出第一个词&nbsp;<code>first</code> 和第二个词&nbsp;<code>second</code>，考虑在某些文本&nbsp;<code>text</code>&nbsp;中可能以 &quot;<code>first second third</code>&quot; 形式出现的情况，其中&nbsp;<code>second</code>&nbsp;紧随&nbsp;<code>first</code>&nbsp;出现，<code>third</code>&nbsp;紧随&nbsp;<code>second</code>&nbsp;出现。</p>

<p>对于每种这样的情况，将第三个词 &quot;<code>third</code>&quot; 添加到答案中，并返回答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>text = &quot;alice is a good girl she is a good student&quot;, first = &quot;a&quot;, second = &quot;good&quot;
<strong>输出：</strong>[&quot;girl&quot;,&quot;student&quot;]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>text = &quot;we will we will rock you&quot;, first = &quot;we&quot;, second = &quot;will&quot;
<strong>输出：</strong>[&quot;we&quot;,&quot;rock&quot;]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= text.length &lt;= 1000</code></li>
	<li><code>text</code>&nbsp;由一些用空格分隔的单词组成，每个单词都由小写英文字母组成</li>
	<li><code>1 &lt;= first.length, second.length &lt;= 10</code></li>
	<li><code>first</code> 和&nbsp;<code>second</code>&nbsp;由小写英文字母组成</li>
</ol>

