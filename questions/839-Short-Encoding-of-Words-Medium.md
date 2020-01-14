#### 单词的压缩编码/Short Encoding of Words
**难度：** 中等/Medium

**Question：** 

<p>Given a list of words, we may encode it by writing a reference string <code>S</code> and a list of indexes <code>A</code>.</p>

<p>For example, if the list of words is <code>[&quot;time&quot;, &quot;me&quot;, &quot;bell&quot;]</code>, we can write it as <code>S = &quot;time#bell#&quot;</code>&nbsp;and <code>indexes = [0, 2, 5]</code>.</p>

<p>Then for each index, we will recover the word by reading from the reference string from that index until we reach a <code>&quot;#&quot;</code> character.</p>

<p>What is the length of the shortest reference string S possible that encodes the given words?</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> words = <code>[&quot;time&quot;, &quot;me&quot;, &quot;bell&quot;]</code>
<strong>Output:</strong> 10
<strong>Explanation:</strong> S = <code>&quot;time#bell#&quot; and indexes = [0, 2, 5</code>].
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= words.length&nbsp;&lt;= 2000</code>.</li>
	<li><code>1 &lt;=&nbsp;words[i].length&nbsp;&lt;= 7</code>.</li>
	<li>Each word&nbsp;has only&nbsp;lowercase letters.</li>
</ol>


------

**题目：** 
<p>给定一个单词列表，我们将这个列表编码成一个索引字符串&nbsp;<code>S</code>&nbsp;与一个索引列表 <code>A</code>。</p>

<p>例如，如果这个列表是 <code>[&quot;time&quot;, &quot;me&quot;, &quot;bell&quot;]</code>，我们就可以将其表示为 <code>S = &quot;time#bell#&quot;</code> 和 <code>indexes = [0, 2, 5]</code>。</p>

<p>对于每一个索引，我们可以通过从字符串 <code>S</code>&nbsp;中索引的位置开始读取字符串，直到 &quot;#&quot; 结束，来恢复我们之前的单词列表。</p>

<p>那么成功对给定单词列表进行编码的最小字符串长度是多少呢？</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入:</strong> words = <code>[&quot;time&quot;, &quot;me&quot;, &quot;bell&quot;]</code>
<strong>输出:</strong> 10
<strong>说明:</strong> S = <code>&quot;time#bell#&quot; ， indexes = [0, 2, 5</code>] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= words.length&nbsp;&lt;= 2000</code></li>
	<li><code>1 &lt;=&nbsp;words[i].length&nbsp;&lt;= 7</code></li>
	<li>每个单词都是小写字母 。</li>
</ol>

