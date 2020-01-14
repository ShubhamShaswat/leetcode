#### 优美的排列 II/Beautiful Arrangement II
**难度：** 中等/Medium

**Question：** 

<p>
Given two integers <code>n</code> and <code>k</code>, you need to construct a list which contains <code>n</code> different positive integers ranging from <code>1</code> to <code>n</code> and obeys the following requirement: <br/>

Suppose this list is [a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, ... , a<sub>n</sub>], then the list [|a<sub>1</sub> - a<sub>2</sub>|, |a<sub>2</sub> - a<sub>3</sub>|, |a<sub>3</sub> - a<sub>4</sub>|, ... , |a<sub>n-1</sub> - a<sub>n</sub>|] has exactly <code>k</code> distinct integers.
</p>

<p>
If there are multiple answers, print any of them.
</p>

<p><b>Example 1:</b><br/>
<pre>
<b>Input:</b> n = 3, k = 1
<b>Output:</b> [1, 2, 3]
<b>Explanation:</b> The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> n = 3, k = 2
<b>Output:</b> [1, 3, 2]
<b>Explanation:</b> The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The <code>n</code> and <code>k</code> are in the range 1 <= k < n <= 10<sup>4</sup>.</li>
</ol>
</p>

------

**题目：** 
<p>给定两个整数&nbsp;<code>n</code>&nbsp;和&nbsp;<code>k</code>，你需要实现一个数组，这个数组包含从&nbsp;<code>1</code>&nbsp;到&nbsp;<code>n</code>&nbsp;的 <code>n</code>&nbsp;个不同整数，同时满足以下条件：</p>

<p>① 如果这个数组是 [a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, ... , a<sub>n</sub>] ，那么数组&nbsp;[|a<sub>1</sub> - a<sub>2</sub>|, |a<sub>2</sub> - a<sub>3</sub>|, |a<sub>3</sub> - a<sub>4</sub>|, ... , |a<sub>n-1</sub> - a<sub>n</sub>|] 中应该有且仅有&nbsp;k 个不同整数；.</p>

<p>② 如果存在多种答案，你只需实现并返回其中任意一种.</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> n = 3, k = 1
<strong>输出:</strong> [1, 2, 3]
<strong>解释:</strong> [1, 2, 3] 包含 3 个范围在 1-3 的不同整数， 并且 [1, 1] 中有且仅有 1 个不同整数 : 1
</pre>

<p>&nbsp;</p>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> n = 3, k = 2
<strong>输出:</strong> [1, 3, 2]
<strong>解释:</strong> [1, 3, 2] 包含 3 个范围在 1-3 的不同整数， 并且 [2, 1] 中有且仅有 2 个不同整数: 1 和 2
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ol>
	<li>&nbsp;<code>n</code>&nbsp;和&nbsp;<code>k</code>&nbsp;满足条件&nbsp;1 &lt;= k &lt; n &lt;= 10<sup>4</sup>.</li>
</ol>

<p>&nbsp;</p>

