#### 字符串中的查找与替换/Find And Replace in String
**难度：** 中等/Medium

**Question：** 

<p>To some string <code>S</code>, we will perform some&nbsp;replacement&nbsp;operations that replace groups of letters with new ones (not necessarily the same size).</p>

<p>Each replacement operation has <code>3</code> parameters: a starting index <code>i</code>, a source word&nbsp;<code>x</code>&nbsp;and a target word&nbsp;<code>y</code>.&nbsp; The rule is that if <code><font face="monospace">x</font></code>&nbsp;starts at position <code>i</code>&nbsp;in the <strong>original</strong> <strong>string</strong> <strong><code>S</code></strong>, then we will replace that occurrence of&nbsp;<code>x</code>&nbsp;with&nbsp;<code>y</code>.&nbsp; If not, we do nothing.</p>

<p>For example, if we have&nbsp;<code>S = &quot;abcd&quot;</code>&nbsp;and we have some replacement operation&nbsp;<code>i = 2, x = &quot;cd&quot;, y = &quot;ffff&quot;</code>, then because&nbsp;<code>&quot;cd&quot;</code>&nbsp;starts at position <code><font face="monospace">2</font></code>&nbsp;in the original string <code>S</code>, we will replace it with <code>&quot;ffff&quot;</code>.</p>

<p>Using another example on <code>S = &quot;abcd&quot;</code>, if we have both the replacement operation <code>i = 0, x = &quot;ab&quot;, y = &quot;eee&quot;</code>, as well as another replacement operation&nbsp;<code>i = 2, x = &quot;ec&quot;, y = &quot;ffff&quot;</code>, this second operation does nothing because in the original string&nbsp;<code>S[2] = &#39;c&#39;</code>, which doesn&#39;t match&nbsp;<code>x[0] = &#39;e&#39;</code>.</p>

<p>All these operations occur simultaneously.&nbsp; It&#39;s guaranteed that there won&#39;t be any overlap in replacement: for example,&nbsp;<code>S = &quot;abc&quot;, indexes = [0, 1],&nbsp;sources = [&quot;ab&quot;,&quot;bc&quot;]</code> is not a valid test case.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>S = &quot;abcd&quot;, indexes = [0,2], sources = [&quot;a&quot;,&quot;cd&quot;], targets = [&quot;eee&quot;,&quot;ffff&quot;]
<strong>Output: </strong>&quot;eeebffff&quot;
<strong>Explanation:</strong> &quot;a&quot; starts at index 0 in S, so it&#39;s replaced by &quot;eee&quot;.
&quot;cd&quot; starts at index 2 in S, so it&#39;s replaced by &quot;ffff&quot;.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>S = &quot;abcd&quot;, indexes = [0,2], sources = [&quot;ab&quot;,&quot;ec&quot;], targets = [&quot;eee&quot;,&quot;ffff&quot;]
<strong>Output: </strong>&quot;eeecd&quot;
<strong>Explanation:</strong> &quot;ab&quot; starts at index 0 in S, so it&#39;s replaced by &quot;eee&quot;. 
&quot;ec&quot; doesn&#39;t starts at index 2 in the <strong>original</strong> S, so we do nothing.
</pre>

<p>Notes:</p>

<ol>
	<li><code>0 &lt;=&nbsp;indexes.length =&nbsp;sources.length =&nbsp;targets.length &lt;= 100</code></li>
	<li><code>0&nbsp;&lt;&nbsp;indexes[i]&nbsp;&lt; S.length &lt;= 1000</code></li>
	<li>All characters in given inputs are lowercase letters.</li>
</ol>

<p>&nbsp;</p>


------

**题目：** 
<p>对于某些字符串 <code>S</code>，我们将执行一些替换操作，用新的字母组替换原有的字母组（不一定大小相同）。</p>

<p>每个替换操作具有 3 个参数：起始索引 <code>i</code>，源字 <code>x</code> 和目标字 <code>y</code>。规则是如果 <code>x</code> 从<strong>原始字符串 <code>S</code></strong> 中的位置 <code>i</code> 开始，那么我们将用 <code>y</code> 替换出现的 <code>x</code>。如果没有，我们什么都不做。</p>

<p>举个例子，如果我们有 <code>S&nbsp;= &ldquo;abcd&rdquo;</code> 并且我们有一些替换操作 <code>i = 2，x = &ldquo;cd&rdquo;，y = &ldquo;ffff&rdquo;</code>，那么因为 <code>&ldquo;cd&rdquo;</code> 从原始字符串 <code>S</code> 中的位置 <code>2</code> 开始，我们将用&nbsp;<code>&ldquo;ffff&rdquo;</code> 替换它。</p>

<p>再来看 <code>S = &ldquo;abcd&rdquo;</code> 上的另一个例子，如果我们有替换操作<code> i = 0，x = &ldquo;ab&rdquo;，y = &ldquo;eee&rdquo;</code>，以及另一个替换操作 <code>i = 2，x = &ldquo;ec&rdquo;，y = &ldquo;ffff&rdquo;</code>，那么第二个操作将不执行任何操作，因为原始字符串中&nbsp;<code>S[2] = &#39;c&#39;</code>，与 <code>x[0] = &#39;e&#39;</code> 不匹配。</p>

<p>所有这些操作同时发生。保证在替换时不会有任何重叠：&nbsp;<code>S = &quot;abc&quot;, indexes = [0, 1],&nbsp;sources = [&quot;ab&quot;,&quot;bc&quot;]</code> 不是有效的测试用例。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>S = &quot;abcd&quot;, indexes = [0,2], sources = [&quot;a&quot;,&quot;cd&quot;], targets = [&quot;eee&quot;,&quot;ffff&quot;]
<strong>输出：</strong>&quot;eeebffff&quot;
<strong>解释：
</strong>&quot;a&quot; 从 S 中的索引 0 开始，所以它被替换为 &quot;eee&quot;。
&quot;cd&quot; 从 S 中的索引 2 开始，所以它被替换为 &quot;ffff&quot;。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>S = &quot;abcd&quot;, indexes = [0,2], sources = [&quot;ab&quot;,&quot;ec&quot;], targets = [&quot;eee&quot;,&quot;ffff&quot;]
<strong>输出：</strong>&quot;eeecd&quot;
<strong>解释：
</strong>&quot;ab&quot; 从 S 中的索引 0 开始，所以它被替换为 &quot;eee&quot;。
&quot;ec&quot; 没有从<strong>原始的</strong> S 中的索引 2 开始，所以它没有被替换。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>0 &lt;=&nbsp;indexes.length =&nbsp;sources.length =&nbsp;targets.length &lt;= 100</code></li>
	<li><code>0&nbsp;&lt;&nbsp;indexes[i]&nbsp;&lt; S.length &lt;= 1000</code></li>
	<li>给定输入中的所有字符都是小写字母。</li>
</ol>

<p>&nbsp;</p>

