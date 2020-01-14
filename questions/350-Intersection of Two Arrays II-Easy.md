#### 两个数组的交集 II/Intersection of Two Arrays II
**难度：** 简单/Easy

**Question：** 

<p>Given two arrays, write a function to compute their intersection.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>nums1 = <span id="example-input-1-1">[1,2,2,1]</span>, nums2 = <span id="example-input-1-2">[2,2]</span>
<strong>Output: </strong><span id="example-output-1">[2,2]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>nums1 = <span id="example-input-2-1">[4,9,5]</span>, nums2 = <span id="example-input-2-2">[9,4,9,8,4]</span>
<strong>Output: </strong><span id="example-output-2">[4,9]</span></pre>
</div>

<p><b>Note:</b></p>

<ul>
	<li>Each element in the result should appear as many times as it shows in both arrays.</li>
	<li>The result can be in any order.</li>
</ul>

<p><b>Follow up:</b></p>

<ul>
	<li>What if the given array is already sorted? How would you optimize your algorithm?</li>
	<li>What if <i>nums1</i>&#39;s size is small compared to <i>nums2</i>&#39;s size? Which algorithm is better?</li>
	<li>What if elements of <i>nums2</i> are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?</li>
</ul>


------

**题目：** 
<p>给定两个数组，编写一个函数来计算它们的交集。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入: </strong>nums1 = [1,2,2,1], nums2 = [2,2]
<strong>输出: </strong>[2,2]
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入: </strong>nums1 = [4,9,5], nums2 = [9,4,9,8,4]
<strong>输出: </strong>[4,9]</pre>

<p><strong>说明：</strong></p>

<ul>
	<li>输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。</li>
	<li>我们可以不考虑输出结果的顺序。</li>
</ul>

<p><strong><strong>进阶:</strong></strong></p>

<ul>
	<li>如果给定的数组已经排好序呢？你将如何优化你的算法？</li>
	<li>如果&nbsp;<em>nums1&nbsp;</em>的大小比&nbsp;<em>nums2&nbsp;</em>小很多，哪种方法更优？</li>
	<li>如果&nbsp;<em>nums2&nbsp;</em>的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？</li>
</ul>

