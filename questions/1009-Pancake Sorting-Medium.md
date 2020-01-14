#### 煎饼排序/Pancake Sorting
**难度：** 中等/Medium

**Question：** 

<p>Given an array <code>A</code>, we can perform a&nbsp;<em>pancake flip</em>:&nbsp;We choose some positive integer&nbsp;<code><strong>k</strong> &lt;= A.length</code>, then reverse the order of the first <strong>k</strong> elements of <code>A</code>.&nbsp; We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array <code>A</code>.</p>

<p>Return the k-values corresponding to a sequence of pancake flips that sort <code>A</code>.&nbsp; Any&nbsp;valid answer that sorts the array within <code>10 * A.length</code> flips will be judged as correct.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[3,2,4,1]</span>
<strong>Output: </strong><span id="example-output-1">[4,2,4,3]</span>
<strong>Explanation: </strong>
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,2,3]</span>
<strong>Output: </strong><span id="example-output-2">[]</span>
<strong>Explanation: </strong>The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.
</pre>

<p>&nbsp;</p>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 100</code></li>
	<li><code>A[i]</code> is a permutation of <code>[1, 2, ..., A.length]</code></li>
</ol>


------

**题目：** 
<p>给定数组&nbsp;<code>A</code>，我们可以对其进行<em>煎饼翻转</em>：我们选择一些正整数&nbsp;<code><strong>k</strong>&nbsp;&lt;= A.length</code>，然后反转 <code>A</code> 的前 <strong>k</strong>&nbsp;个元素的顺序。我们要执行零次或多次煎饼翻转（按顺序一次接一次地进行）以完成对数组 <code>A</code> 的排序。</p>

<p>返回能使&nbsp;<code>A</code> 排序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转次数在&nbsp;<code>10 * A.length</code> 范围内的有效答案都将被判断为正确。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[3,2,4,1]
<strong>输出：</strong>[4,2,4,3]
<strong>解释：</strong>
我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
初始状态 A = [3, 2, 4, 1]
第一次翻转后 (k=4): A = [1, 4, 2, 3]
第二次翻转后 (k=2): A = [4, 1, 2, 3]
第三次翻转后 (k=4): A = [3, 2, 1, 4]
第四次翻转后 (k=3): A = [1, 2, 3, 4]，此时已完成排序。 
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[1,2,3]
<strong>输出：</strong>[]
<strong>解释：
</strong>输入已经排序，因此不需要翻转任何内容。
请注意，其他可能的答案，如[3，3]，也将被接受。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 100</code></li>
	<li><code>A[i]</code> 是&nbsp;<code>[1, 2, ..., A.length]</code>&nbsp;的排列</li>
</ol>

