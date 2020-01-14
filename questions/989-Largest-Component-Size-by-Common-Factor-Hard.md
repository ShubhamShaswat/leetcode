#### 按公因数计算最大组件大小/Largest Component Size by Common Factor
**难度：** 困难/Hard

**Question：** 

<p>Given a non-empty&nbsp;array of unique positive integers <code>A</code>, consider the following graph:</p>

<ul>
	<li>There are <code>A.length</code> nodes, labelled <code>A[0]</code> to <code>A[A.length - 1];</code></li>
	<li>There is an edge between <code>A[i]</code> and <code>A[j]</code>&nbsp;if and only if&nbsp;<code>A[i]</code> and <code>A[j]</code> share a common factor greater than 1.</li>
</ul>

<p>Return the size of the largest connected component in the graph.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[4,6,15,35]</span>
<strong>Output: </strong><span id="example-output-1">4</span>
<span><img alt="" src="https://assets.leetcode.com/uploads/2018/12/01/ex1.png" style="width: 257px; height: 50px;" /></span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[20,50,9,63]</span>
<strong>Output: </strong><span id="example-output-2">2</span>
<span><img alt="" src="https://assets.leetcode.com/uploads/2018/12/01/ex2.png" style="width: 293px; height: 50px;" /></span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[2,3,6,7,4,12,21,39]</span>
<strong>Output: </strong><span id="example-output-3">8</span>
<span><img alt="" src="https://assets.leetcode.com/uploads/2018/12/01/ex3.png" style="width: 346px; height: 180px;" /></span>
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 20000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 100000</code></li>
</ol>
</div>
</div>
</div>


------

**题目：** 
<p>给定一个由不同正整数的组成的非空数组 <code>A</code>，考虑下面的图：</p>

<ul>
	<li>有&nbsp;<code>A.length</code>&nbsp;个节点，按从&nbsp;<code>A[0]</code>&nbsp;到&nbsp;<code>A[A.length - 1]</code>&nbsp;标记；</li>
	<li>只有当 <code>A[i]</code> 和 <code>A[j]</code> 共用一个大于 1 的公因数时，<code>A[i]</code>&nbsp;和 <code>A[j]</code> 之间才有一条边。</li>
</ul>

<p>返回图中最大连通组件的大小。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[4,6,15,35]
<strong>输出：</strong>4
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-uploads/uploads/2018/12/01/ex1.png" style="height: 37px; width: 255px;"><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/01/ex1.png" style="height: 50px; width: 257px;">
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[20,50,9,63]
<strong>输出：</strong>2
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/01/ex2.png" style="height: 50px; width: 293px;">
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[2,3,6,7,4,12,21,39]
<strong>输出：</strong>8
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/01/ex3.png" style="height: 180px; width: 346px;">
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 20000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 100000</code></li>
</ol>

