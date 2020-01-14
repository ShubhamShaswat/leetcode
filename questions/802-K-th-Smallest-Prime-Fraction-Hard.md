#### 第 K 个最小的素数分数/K-th Smallest Prime Fraction
**难度：** 困难/Hard

**Question：** 

<p>A sorted list <code>A</code> contains 1, plus some number of primes.&nbsp; Then, for every p &lt; q in the list, we consider the fraction p/q.</p>

<p>What is the <code>K</code>-th smallest fraction considered?&nbsp; Return your answer as an array of ints, where <code>answer[0] = p</code> and <code>answer[1] = q</code>.</p>

<pre>
<strong>Examples:</strong>
<strong>Input:</strong> A = [1, 2, 3, 5], K = 3
<strong>Output:</strong> [2, 5]
<strong>Explanation:</strong>
The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
The third fraction is 2/5.

<strong>Input:</strong> A = [1, 7], K = 1
<strong>Output:</strong> [1, 7]
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>A</code> will have length between <code>2</code> and <code>2000</code>.</li>
	<li>Each <code>A[i]</code> will be between <code>1</code> and <code>30000</code>.</li>
	<li><code>K</code> will be between <code>1</code> and <code>A.length * (A.length - 1) / 2</code>.</li>
</ul>

------

**题目：** 
<p>一个已排序好的表&nbsp;<code>A</code>，其包含 1 和其他一些素数.&nbsp; 当列表中的每一个 p&lt;q 时，我们可以构造一个分数 p/q 。</p>

<p>那么第&nbsp;<code>k</code>&nbsp;个最小的分数是多少呢?&nbsp; 以整数数组的形式返回你的答案, 这里&nbsp;<code>answer[0] = p</code>&nbsp;且&nbsp;<code>answer[1] = q</code>.</p>

<pre>
<strong>示例:</strong>
<strong>输入:</strong> A = [1, 2, 3, 5], K = 3
<strong>输出:</strong> [2, 5]
<strong>解释:</strong>
已构造好的分数,排序后如下所示:
1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
很明显第三个最小的分数是 2/5.

<strong>输入:</strong> A = [1, 7], K = 1
<strong>输出:</strong> [1, 7]
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>A</code> 的取值范围在 <code>2</code> &mdash; <code>2000</code>.</li>
	<li>每个&nbsp;<code>A[i]</code> 的值在 <code>1</code> &mdash;<code>30000</code>.</li>
	<li><code>K</code> 取值范围为 <code>1</code> &mdash;<code>A.length * (A.length - 1) / 2</code></li>
</ul>

