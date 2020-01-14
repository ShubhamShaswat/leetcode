#### 分割数组/Partition Array into Disjoint Intervals
**难度：** 中等/Medium

**Question：** 

<p>Given an array <code>A</code>, partition it&nbsp;into two (contiguous) subarrays&nbsp;<code>left</code>&nbsp;and <code>right</code>&nbsp;so that:</p>

<ul>
	<li>Every element in <code>left</code>&nbsp;is less than or equal to every element in <code>right</code>.</li>
	<li><code>left</code> and <code>right</code> are non-empty.</li>
	<li><code>left</code>&nbsp;has the smallest possible size.</li>
</ul>

<p>Return the <strong>length</strong> of <code>left</code> after such a partitioning.&nbsp; It is guaranteed that such a partitioning exists.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[5,0,3,8,6]</span>
<strong>Output: </strong><span id="example-output-1">3</span>
<strong>Explanation: </strong>left = [5,0,3], right = [8,6]
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,1,1,0,6,12]</span>
<strong>Output: </strong><span id="example-output-2">4</span>
<strong>Explanation: </strong>left = [1,1,1,0], right = [6,12]
</pre>

<p>&nbsp;</p>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>2 &lt;= A.length&nbsp;&lt;= 30000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10^6</code></li>
	<li>It is guaranteed there is at least one way to partition <code>A</code> as described.</li>
</ol>

<div>
<div>&nbsp;</div>
</div>


------

**题目：** 
<p>给定一个数组&nbsp;<code>A</code>，将其划分为两个不相交（没有公共元素）的连续子数组&nbsp;<code>left</code>&nbsp;和&nbsp;<code>right</code>，&nbsp;使得：</p>

<ul>
	<li><code>left</code>&nbsp;中的每个元素都小于或等于&nbsp;<code>right</code>&nbsp;中的每个元素。</li>
	<li><code>left</code> 和&nbsp;<code>right</code>&nbsp;都是非空的。</li>
	<li><code>left</code>&nbsp;要尽可能小。</li>
</ul>

<p>在完成这样的分组后返回&nbsp;<code>left</code>&nbsp;的<strong>长度</strong>。可以保证存在这样的划分方法。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[5,0,3,8,6]
<strong>输出：</strong>3
<strong>解释：</strong>left = [5,0,3]，right = [8,6]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[1,1,1,0,6,12]
<strong>输出：</strong>4
<strong>解释：</strong>left = [1,1,1,0]，right = [6,12]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>2 &lt;= A.length&nbsp;&lt;= 30000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10^6</code></li>
	<li>可以保证至少有一种方法能够按题目所描述的那样对 <code>A</code> 进行划分。</li>
</ol>

<p>&nbsp;</p>

