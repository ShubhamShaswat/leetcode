#### 数组形式的整数加法/Add to Array-Form of Integer
**难度：** 简单/Easy

**Question：** 

<p>For a non-negative integer <code>X</code>, the&nbsp;<em>array-form of <code>X</code></em>&nbsp;is an array of its digits in left to right order.&nbsp; For example, if <code>X = 1231</code>, then the array form is&nbsp;<code>[1,2,3,1]</code>.</p>

<p>Given the array-form <code>A</code> of a non-negative&nbsp;integer <code>X</code>, return the array-form of the integer <code>X+K</code>.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1,2,0,0]</span>, K = 34
<strong>Output: </strong><span id="example-output-1">[1,2,3,4]</span>
<strong>Explanation: </strong>1200 + 34 = 1234
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[2,7,4]</span>, K = <span id="example-input-2-2">181</span>
<strong>Output: </strong><span id="example-output-2">[4,5,5]</span>
<strong>Explanation: </strong>274 + 181 = 455
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">[2,1,5]</span>, K = <span id="example-input-3-2">806</span>
<strong>Output: </strong><span id="example-output-3">[1,0,2,1]</span>
<strong>Explanation: </strong>215 + 806 = 1021
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-4-1">[9,9,9,9,9,9,9,9,9,9]</span>, K = <span id="example-input-4-2">1</span>
<strong>Output: </strong><span id="example-output-4">[1,0,0,0,0,0,0,0,0,0,0]</span>
<strong>Explanation: </strong>9999999999 + 1 = 10000000000
</pre>

<p>&nbsp;</p>

<p><strong>Note：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 10000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 9</code></li>
	<li><code>0 &lt;= K &lt;= 10000</code></li>
	<li>If <code>A.length &gt; 1</code>, then <code>A[0] != 0</code></li>
</ol>
</div>
</div>
</div>
</div>

------

**题目：** 
<p>对于非负整数&nbsp;<code>X</code>&nbsp;而言，<em><code>X</code></em>&nbsp;的<em>数组形式</em>是每位数字按从左到右的顺序形成的数组。例如，如果&nbsp;<code>X = 1231</code>，那么其数组形式为&nbsp;<code>[1,2,3,1]</code>。</p>

<p>给定非负整数 <code>X</code> 的数组形式&nbsp;<code>A</code>，返回整数&nbsp;<code>X+K</code>&nbsp;的数组形式。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>A = [1,2,0,0], K = 34
<strong>输出：</strong>[1,2,3,4]
<strong>解释：</strong>1200 + 34 = 1234
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>A = [2,7,4], K = 181
<strong>输出：</strong>[4,5,5]
<strong>解释：</strong>274 + 181 = 455
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>A = [2,1,5], K = 806
<strong>输出：</strong>[1,0,2,1]
<strong>解释：</strong>215 + 806 = 1021
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>A = [9,9,9,9,9,9,9,9,9,9], K = 1
<strong>输出：</strong>[1,0,0,0,0,0,0,0,0,0,0]
<strong>解释：</strong>9999999999 + 1 = 10000000000
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 10000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 9</code></li>
	<li><code>0 &lt;= K &lt;= 10000</code></li>
	<li>如果&nbsp;<code>A.length &gt; 1</code>，那么&nbsp;<code>A[0] != 0</code></li>
</ol>

