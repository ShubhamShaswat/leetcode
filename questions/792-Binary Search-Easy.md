#### 二分查找/Binary Search
**难度：** 简单/Easy

**Question：** 

<p>Given a <strong>sorted</strong> (in ascending order) integer array <code>nums</code> of <code>n</code> elements and a <code>target</code> value, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index, otherwise return <code>-1</code>.</p>

<p><br />
<strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <code>nums</code> = [-1,0,3,5,9,12], <code>target</code> = 9
<strong>Output:</strong> 4
<strong>Explanation:</strong> 9 exists in <code>nums</code> and its index is 4

</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <code>nums</code> = [-1,0,3,5,9,12], <code>target</code> = 2
<strong>Output:</strong> -1
<strong>Explanation:</strong> 2 does not exist in <code>nums</code> so return -1
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>You may assume that all elements in <code>nums</code> are unique.</li>
	<li><code>n</code> will be in the range <code>[1, 10000]</code>.</li>
	<li>The value of each element in <code>nums</code> will be in the range <code>[-9999, 9999]</code>.</li>
</ol>


------

**题目：** 
<p>给定一个&nbsp;<code>n</code>&nbsp;个元素有序的（升序）整型数组&nbsp;<code>nums</code> 和一个目标值&nbsp;<code>target</code> &nbsp;，写一个函数搜索&nbsp;<code>nums</code>&nbsp;中的 <code>target</code>，如果目标值存在返回下标，否则返回 <code>-1</code>。</p>

<p><br>
<strong>示例 1:</strong></p>

<pre><strong>输入:</strong> <code>nums</code> = [-1,0,3,5,9,12], <code>target</code> = 9
<strong>输出:</strong> 4
<strong>解释:</strong> 9 出现在 <code>nums</code> 中并且下标为 4
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> <code>nums</code> = [-1,0,3,5,9,12], <code>target</code> = 2
<strong>输出:</strong> -1
<strong>解释:</strong> 2 不存在 <code>nums</code> 中因此返回 -1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>你可以假设 <code>nums</code>&nbsp;中的所有元素是不重复的。</li>
	<li><code>n</code>&nbsp;将在&nbsp;<code>[1, 10000]</code>之间。</li>
	<li><code>nums</code>&nbsp;的每个元素都将在&nbsp;<code>[-9999, 9999]</code>之间。</li>
</ol>

