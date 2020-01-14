#### 删列造序/Delete Columns to Make Sorted
**难度：** 简单/Easy

**Question：** 

<p>We are given an array&nbsp;<code>A</code> of <code>N</code> lowercase letter strings, all of the same length.</p>

<p>Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.</p>

<p>For example, if we have an array <code>A = [&quot;</code><code>abcdef</code><code>&quot;,&quot;uvwxyz&quot;]</code> and deletion indices <code>{0, 2, 3}</code>, then the final array after deletions is <code>[&quot;bef&quot;, &quot;vyz&quot;]</code>,&nbsp;and the remaining columns of <code>A</code> are&nbsp;<code>[&quot;b&quot;</code><code>,&quot;</code><code>v&quot;]</code>, <code>[&quot;e&quot;,&quot;y&quot;]</code>, and <code>[&quot;f&quot;,&quot;z&quot;]</code>.&nbsp; (Formally, the <code>c</code>-th column is <code>[A[0][c], A[1][c], ..., A[A.length-1][c]]</code>.)</p>

<p>Suppose we chose a set of deletion indices <code>D</code> such that after deletions, each remaining column in A is in <strong>non-decreasing</strong> sorted order.</p>

<p>Return the minimum possible value of <code>D.length</code>.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;cba&quot;,&quot;daf&quot;,&quot;ghi&quot;]</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong>
After choosing D = {1}, each column [&quot;c&quot;,&quot;d&quot;,&quot;g&quot;] and [&quot;a&quot;,&quot;f&quot;,&quot;i&quot;] are in non-decreasing sorted order.
If we chose D = {}, then a column [&quot;b&quot;,&quot;a&quot;,&quot;h&quot;] would not be in non-decreasing sorted order.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[&quot;a&quot;,&quot;b&quot;]</span>
<strong>Output: </strong><span id="example-output-2">0</span>
<strong>Explanation: </strong>D = {}
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[&quot;zyx&quot;,&quot;wvu&quot;,&quot;tsr&quot;]</span>
<strong>Output: </strong><span id="example-output-3">3</span>
<strong>Explanation: </strong>D = {0, 1, 2}
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 100</code></li>
	<li><code>1 &lt;= A[i].length &lt;= 1000</code></li>
</ol>
</div>
</div>
</div>


------

**题目：** 
<p>给定由&nbsp;<code>N</code>&nbsp;个小写字母字符串组成的数组 <code>A</code>，其中每个字符串长度相等。</p>

<p><strong>删除</strong> 操作的定义是：选出一组要删掉的列，删去&nbsp;<code>A</code> 中对应列中的所有字符，形式上，第 <code>n</code>&nbsp;列为&nbsp;<code>[A[0][n], A[1][n], ..., A[A.length-1][n]]</code>）。</p>

<p>比如，有&nbsp;<code>A = [&quot;abcdef&quot;, &quot;uvwxyz&quot;]</code>，</p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/07/06/944_1.png" style="height: 48px; width: 300px;"></p>

<p>要删掉的列为&nbsp;<code>{0, 2, 3}</code>，删除后 <code>A</code>&nbsp;为<code>[&quot;bef&quot;, &quot;vyz&quot;]</code>， <code>A</code>&nbsp;的列分别为<code>[&quot;b&quot;,&quot;v&quot;], [&quot;e&quot;,&quot;y&quot;], [&quot;f&quot;,&quot;z&quot;]</code>。</p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/07/06/944_2.png" style="height: 76px; width: 300px;"></p>

<p>你需要选出一组要删掉的列&nbsp;<code>D</code>，对&nbsp;<code>A</code> 执行删除操作，使 <code>A</code> 中剩余的每一列都是 <strong>非降序</strong>&nbsp;排列的，然后请你返回&nbsp;<code>D.length</code>&nbsp;的最小可能值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[&quot;cba&quot;, &quot;daf&quot;, &quot;ghi&quot;]
<strong>输出：</strong>1
<strong>解释：</strong>
当选择 D = {1}，删除后 A 的列为：[&quot;c&quot;,&quot;d&quot;,&quot;g&quot;] 和 [&quot;a&quot;,&quot;f&quot;,&quot;i&quot;]，均为非降序排列。
若选择 D = {}，那么 A 的列 [&quot;b&quot;,&quot;a&quot;,&quot;h&quot;] 就不是非降序排列了。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[&quot;a&quot;, &quot;b&quot;]
<strong>输出：</strong>0
<strong>解释：</strong>D = {}
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[&quot;zyx&quot;, &quot;wvu&quot;, &quot;tsr&quot;]
<strong>输出：</strong>3
<strong>解释：</strong>D = {0, 1, 2}
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 100</code></li>
	<li><code>1 &lt;= A[i].length &lt;= 1000</code></li>
</ol>

