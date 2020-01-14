#### 复写零/Duplicate Zeros
**难度：** 简单/Easy

**Question：** 

<p>Given a fixed length&nbsp;array <code>arr</code> of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.</p>

<p>Note that elements beyond the length of the original array are not written.</p>

<p>Do the above modifications to the input array <strong>in place</strong>, do not return anything from your function.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,0,2,3,0,4,5,0]</span>
<strong>Output: </strong>null
<strong>Explanation: </strong>After calling your function, the <strong>input</strong> array is modified to: <span id="example-output-1">[1,0,0,2,3,0,0,4]</span>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,2,3]</span>
<strong>Output: </strong>null
<strong>Explanation: </strong>After calling your function, the <strong>input</strong> array is modified to: <span id="example-output-2">[1,2,3]</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= arr.length &lt;= 10000</code></li>
	<li><code>0 &lt;= arr[i] &lt;= 9</code></li>
</ol>

------

**题目：** 
<p>给你一个长度固定的整数数组&nbsp;<code>arr</code>，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。</p>

<p>注意：请不要在超过该数组长度的位置写入元素。</p>

<p>要求：请对输入的数组&nbsp;<strong>就地&nbsp;</strong>进行上述修改，不要从函数返回任何东西。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[1,0,2,3,0,4,5,0]
<strong>输出：</strong>null
<strong>解释：</strong>调用函数后，<strong>输入</strong>的数组将被修改为：[1,0,0,2,3,0,0,4]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[1,2,3]
<strong>输出：</strong>null
<strong>解释：</strong>调用函数后，<strong>输入</strong>的数组将被修改为：[1,2,3]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= arr.length &lt;= 10000</code></li>
	<li><code>0 &lt;= arr[i] &lt;= 9</code></li>
</ol>

