#### 删列造序 II/Delete Columns to Make Sorted II
**难度：** 中等/Medium

**Question：** 

<p>We are given an array&nbsp;<code>A</code> of <code>N</code> lowercase letter strings, all of the same length.</p>

<p>Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.</p>

<p>For example, if we have an array <code>A = [&quot;abcdef&quot;,&quot;uvwxyz&quot;]</code> and deletion indices <code>{0, 2, 3}</code>, then the final array after deletions is <code>[&quot;bef&quot;,&quot;vyz&quot;]</code>.</p>

<p>Suppose we chose a set of deletion indices <code>D</code> such that after deletions, the final array has its elements in <strong>lexicographic</strong> order (<code>A[0] &lt;= A[1] &lt;= A[2] ... &lt;= A[A.length - 1]</code>).</p>

<p>Return the minimum possible value of <code>D.length</code>.</p>

<p>&nbsp;</p>

<div>
<div>
<ol>
</ol>
</div>
</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;ca&quot;,&quot;bb&quot;,&quot;ac&quot;]</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong>
After deleting the first column, A = [&quot;a&quot;, &quot;b&quot;, &quot;c&quot;].
Now A is in lexicographic order (ie. A[0] &lt;= A[1] &lt;= A[2]).
We require at least 1 deletion since initially A was not in lexicographic order, so the answer is 1.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span>[&quot;xc&quot;,&quot;yb&quot;,&quot;za&quot;]</span>
<strong>Output: </strong><span id="example-output-2">0</span>
<strong>Explanation: </strong>
A is already in lexicographic order, so we don&#39;t need to delete anything.
Note that the rows of A are not necessarily in lexicographic order:
ie. it is NOT necessarily true that (A[0][0] &lt;= A[0][1] &lt;= ...)
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[&quot;zyx&quot;,&quot;wvu&quot;,&quot;tsr&quot;]</span>
<strong>Output: </strong><span id="example-output-3">3</span>
<strong>Explanation: </strong>
We have to delete every column.
</pre>

<p>&nbsp;</p>

<div>
<div>
<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 100</code></li>
	<li><code>1 &lt;= A[i].length &lt;= 100</code></li>
</ol>
</div>
</div>
</div>
</div>
</div>


------

**题目：** 
<p>给定由&nbsp;<code>N</code>&nbsp;个小写字母字符串组成的数组&nbsp;<code>A</code>，其中每个字符串长度相等。</p>

<p>选取一个删除索引序列，对于&nbsp;<code>A</code>&nbsp;中的每个字符串，删除对应每个索引处的字符。</p>

<p>比如，有&nbsp;<code>A = [&quot;abcdef&quot;, &quot;uvwxyz&quot;]</code>，删除索引序列&nbsp;<code>{0, 2, 3}</code>，删除后&nbsp;<code>A</code>&nbsp;为<code>[&quot;bef&quot;, &quot;vyz&quot;]</code>。</p>

<p>假设，我们选择了一组删除索引&nbsp;<code>D</code>，那么在执行删除操作之后，最终得到的数组的元素是按 <strong>字典序</strong>（<code>A[0] &lt;= A[1] &lt;= A[2] ... &lt;= A[A.length - 1]</code>）排列的，然后请你返回&nbsp;<code>D.length</code>&nbsp;的最小可能值。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[&quot;ca&quot;,&quot;bb&quot;,&quot;ac&quot;]
<strong>输出：</strong>1
<strong>解释： </strong>
删除第一列后，A = [&quot;a&quot;, &quot;b&quot;, &quot;c&quot;]。
现在 A 中元素是按字典排列的 (即，A[0] &lt;= A[1] &lt;= A[2])。
我们至少需要进行 1 次删除，因为最初 A 不是按字典序排列的，所以答案是 1。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[&quot;xc&quot;,&quot;yb&quot;,&quot;za&quot;]
<strong>输出：</strong>0
<strong>解释：</strong>
A 的列已经是按字典序排列了，所以我们不需要删除任何东西。
注意 A 的行不需要按字典序排列。
也就是说，A[0][0] &lt;= A[0][1] &lt;= ... 不一定成立。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[&quot;zyx&quot;,&quot;wvu&quot;,&quot;tsr&quot;]
<strong>输出：</strong>3
<strong>解释：</strong>
我们必须删掉每一列。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 100</code></li>
	<li><code>1 &lt;= A[i].length &lt;= 100</code></li>
</ol>

