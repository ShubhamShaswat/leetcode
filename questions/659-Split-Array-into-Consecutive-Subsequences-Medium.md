#### 分割数组为连续子序列/Split Array into Consecutive Subsequences
**难度：** 中等/Medium

**Question：** 

<p>Given an array <code>nums</code>&nbsp;sorted in ascending order, return <code>true</code> if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers&nbsp;and has length at least 3.</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [1,2,3,3,4,5]
<b>Output:</b> True
<b>Explanation:</b>
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [1,2,3,3,4,4,5,5]
<b>Output:</b> True
<b>Explanation:</b>
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

</pre>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> [1,2,3,4,4,5]
<b>Output:</b> False
</pre>

<p>&nbsp;</p>

<p><b>Constraints:</b></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10000</code></li>
</ul>

<p>&nbsp;</p>


------

**题目：** 
<p>输入一个按升序排序的整数数组（可能包含重复数字），你需要将它们分割成几个子序列，其中每个子序列至少包含三个连续整数。返回你是否能做出这样的分割？</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> [1,2,3,3,4,5]
<strong>输出:</strong> True
<strong>解释:</strong>
你可以分割出这样两个连续子序列 : 
1, 2, 3
3, 4, 5
</pre>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> [1,2,3,3,4,4,5,5]
<strong>输出:</strong> True
<strong>解释:</strong>
你可以分割出这样两个连续子序列 : 
1, 2, 3, 4, 5
3, 4, 5
</pre>

<p>&nbsp;</p>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入:</strong> [1,2,3,4,4,5]
<strong>输出:</strong> False
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>输入的数组长度范围为 [1, 10000]</li>
</ol>

<p>&nbsp;</p>

