#### 元音拼写检查器/Vowel Spellchecker
**难度：** 中等/Medium

**Question：** 

<p>Given a&nbsp;<code>wordlist</code>, we want to implement a spellchecker that converts a query word into a correct word.</p>

<p>For a given <code>query</code> word, the spell checker handles two categories of spelling mistakes:</p>

<ul>
	<li>Capitalization: If the query matches a word in the wordlist (<strong>case-insensitive</strong>), then the query word is returned with the same case as the case in the wordlist.

	<ul>
		<li>Example: <code>wordlist = [&quot;yellow&quot;]</code>, <code>query = &quot;YellOw&quot;</code>: <code>correct = &quot;yellow&quot;</code></li>
		<li>Example: <code>wordlist = [&quot;Yellow&quot;]</code>, <code>query = &quot;yellow&quot;</code>: <code>correct = &quot;Yellow&quot;</code></li>
		<li>Example: <code>wordlist = [&quot;yellow&quot;]</code>, <code>query = &quot;yellow&quot;</code>: <code>correct = &quot;yellow&quot;</code></li>
	</ul>
	</li>
	<li>Vowel Errors: If after replacing the vowels (&#39;a&#39;, &#39;e&#39;, &#39;i&#39;, &#39;o&#39;, &#39;u&#39;) of the query word with any vowel individually, it matches a word in the wordlist (<strong>case-insensitive</strong>), then the query word is returned with the same case as the match in the wordlist.
	<ul>
		<li>Example: <code>wordlist = [&quot;YellOw&quot;]</code>, <code>query = &quot;yollow&quot;</code>: <code>correct = &quot;YellOw&quot;</code></li>
		<li>Example: <code>wordlist = [&quot;YellOw&quot;]</code>, <code>query = &quot;yeellow&quot;</code>: <code>correct = &quot;&quot;</code> (no match)</li>
		<li>Example: <code>wordlist = [&quot;YellOw&quot;]</code>, <code>query = &quot;yllw&quot;</code>: <code>correct = &quot;&quot;</code> (no match)</li>
	</ul>
	</li>
</ul>

<p>In addition, the spell checker operates under the following precedence rules:</p>

<ul>
	<li>When the query exactly matches a word in the wordlist (<strong>case-sensitive</strong>), you should return the same word back.</li>
	<li>When the query matches a word up to capitlization, you should return the first such match in the wordlist.</li>
	<li>When the query matches a word up to vowel errors, you should return the first such match in the wordlist.</li>
	<li>If the query has no matches in the wordlist, you should return the empty string.</li>
</ul>

<p>Given some <code>queries</code>, return a&nbsp;list of words <code>answer</code>, where <code>answer[i]</code>&nbsp;is&nbsp;the correct word for <code>query = queries[i]</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>wordlist = <span id="example-input-1-1">[&quot;KiTe&quot;,&quot;kite&quot;,&quot;hare&quot;,&quot;Hare&quot;]</span>, queries = <span id="example-input-1-2">[&quot;kite&quot;,&quot;Kite&quot;,&quot;KiTe&quot;,&quot;Hare&quot;,&quot;HARE&quot;,&quot;Hear&quot;,&quot;hear&quot;,&quot;keti&quot;,&quot;keet&quot;,&quot;keto&quot;]</span>
<strong>Output: </strong><span id="example-output-1">[&quot;kite&quot;,&quot;KiTe&quot;,&quot;KiTe&quot;,&quot;Hare&quot;,&quot;hare&quot;,&quot;&quot;,&quot;&quot;,&quot;KiTe&quot;,&quot;&quot;,&quot;KiTe&quot;]</span></pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>1 &lt;= wordlist.length &lt;= 5000</code></li>
	<li><code>1 &lt;= queries.length &lt;= 5000</code></li>
	<li><code>1 &lt;= wordlist[i].length &lt;= 7</code></li>
	<li><code>1 &lt;= queries[i].length &lt;= 7</code></li>
	<li>All strings in <code>wordlist</code> and <code>queries</code> consist only of <strong>english</strong>&nbsp;letters.</li>
</ul>


------

**题目：** 
<p>在给定单词列表&nbsp;<code>wordlist</code>&nbsp;的情况下，我们希望实现一个拼写检查器，将查询单词转换为正确的单词。</p>

<p>对于给定的查询单词&nbsp;<code>query</code>，拼写检查器将会处理两类拼写错误：</p>

<ul>
	<li>大小写：如果查询匹配单词列表中的某个单词（<strong>不区分大小写</strong>），则返回的正确单词与单词列表中的大小写相同。

	<ul>
		<li>例如：<code>wordlist = [&quot;yellow&quot;]</code>, <code>query = &quot;YellOw&quot;</code>: <code>correct = &quot;yellow&quot;</code></li>
		<li>例如：<code>wordlist = [&quot;Yellow&quot;]</code>, <code>query = &quot;yellow&quot;</code>: <code>correct = &quot;Yellow&quot;</code></li>
		<li>例如：<code>wordlist = [&quot;yellow&quot;]</code>, <code>query = &quot;yellow&quot;</code>: <code>correct = &quot;yellow&quot;</code></li>
	</ul>
	</li>
	<li>元音错误：如果在将查询单词中的元音（&lsquo;a&rsquo;、&lsquo;e&rsquo;、&lsquo;i&rsquo;、&lsquo;o&rsquo;、&lsquo;u&rsquo;）分别替换为任何元音后，能与单词列表中的单词匹配（<strong>不区分大小写</strong>），则返回的正确单词与单词列表中的匹配项大小写相同。
	<ul>
		<li>例如：<code>wordlist = [&quot;YellOw&quot;]</code>, <code>query = &quot;yollow&quot;</code>: <code>correct = &quot;YellOw&quot;</code></li>
		<li>例如：<code>wordlist = [&quot;YellOw&quot;]</code>, <code>query = &quot;yeellow&quot;</code>: <code>correct = &quot;&quot;</code> （无匹配项）</li>
		<li>例如：<code>wordlist = [&quot;YellOw&quot;]</code>, <code>query = &quot;yllw&quot;</code>: <code>correct = &quot;&quot;</code> （无匹配项）</li>
	</ul>
	</li>
</ul>

<p>此外，拼写检查器还按照以下优先级规则操作：</p>

<ul>
	<li>当查询完全匹配单词列表中的某个单词（<strong>区分大小写</strong>）时，应返回相同的单词。</li>
	<li>当查询匹配到大小写问题的单词时，您应该返回单词列表中的第一个这样的匹配项。</li>
	<li>当查询匹配到元音错误的单词时，您应该返回单词列表中的第一个这样的匹配项。</li>
	<li>如果该查询在单词列表中没有匹配项，则应返回空字符串。</li>
</ul>

<p>给出一些查询 <code>queries</code>，返回一个单词列表 <code>answer</code>，其中 <code>answer[i]</code> 是由查询 <code>query = queries[i]</code> 得到的正确单词。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>wordlist = [&quot;KiTe&quot;,&quot;kite&quot;,&quot;hare&quot;,&quot;Hare&quot;], queries = [&quot;kite&quot;,&quot;Kite&quot;,&quot;KiTe&quot;,&quot;Hare&quot;,&quot;HARE&quot;,&quot;Hear&quot;,&quot;hear&quot;,&quot;keti&quot;,&quot;keet&quot;,&quot;keto&quot;]
<strong>输出：</strong>[&quot;kite&quot;,&quot;KiTe&quot;,&quot;KiTe&quot;,&quot;Hare&quot;,&quot;hare&quot;,&quot;&quot;,&quot;&quot;,&quot;KiTe&quot;,&quot;&quot;,&quot;KiTe&quot;]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= wordlist.length &lt;= 5000</code></li>
	<li><code>1 &lt;= queries.length &lt;= 5000</code></li>
	<li><code>1 &lt;= wordlist[i].length &lt;= 7</code></li>
	<li><code>1 &lt;= queries[i].length &lt;= 7</code></li>
	<li><code>wordlist</code> 和&nbsp;<code>queries</code>&nbsp;中的所有字符串仅由<strong>英文</strong>字母组成。</li>
</ol>

