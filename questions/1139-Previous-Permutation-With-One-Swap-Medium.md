#### 交换一次的先前排列/Previous Permutation With One Swap
**难度：** 中等/Medium

**Question：** 

<p>Given an array <code>A</code> of positive integers (not necessarily distinct), return the lexicographically largest permutation that is smaller than <code>A</code>, that can be <strong>made with one swap</strong> (A <em>swap</em> exchanges the positions of two numbers <code>A[i]</code> and <code>A[j]</code>).&nbsp; If it cannot be done, then return the same array.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[3,2,1]
<strong>Output: </strong>[3,1,2]
<strong>Explanation: </strong>Swapping 2 and 1.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[1,1,5]
<strong>Output: </strong>[1,1,5]
<strong>Explanation: </strong>This is already the smallest permutation.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>[1,9,4,6,7]
<strong>Output: </strong>[1,7,4,6,9]
<strong>Explanation: </strong>Swapping 9 and 7.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>[3,1,1,3]
<strong>Output: </strong>[1,3,1,3]
<strong>Explanation: </strong>Swapping 1 and 3.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 10000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 10000</code></li>
</ol>


------

**题目：** 
<p>给你一个正整数的数组 <code>A</code>（其中的元素不一定完全不同），请你返回可在&nbsp;<strong>一次交换</strong>（交换两数字 <code>A[i]</code> 和 <code>A[j]</code> 的位置）后得到的、按字典序排列小于 <code>A</code> 的最大可能排列。</p>

<p>如果无法这么操作，就请返回原数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[3,2,1]
<strong>输出：</strong>[3,1,2]
<strong>解释：</strong>
交换 2 和 1
</pre>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[1,1,5]
<strong>输出：</strong>[1,1,5]
<strong>解释： </strong>
这已经是最小排列
</pre>

<p>&nbsp;</p>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[1,9,4,6,7]
<strong>输出：</strong>[1,7,4,6,9]
<strong>解释：</strong>
交换 9 和 7
</pre>

<p>&nbsp;</p>

<p><strong>示例&nbsp;4：</strong></p>

<pre><strong>输入：</strong>[3,1,1,3]
<strong>输出：</strong>[1,3,1,3]
<strong>解释：
</strong>交换 1 和 3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 10000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 10000</code></li>
</ol>

