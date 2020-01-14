#### 负二进制数相加/Adding Two Negabinary Numbers
**难度：** 中等/Medium

**Question：** 

<p>Given two numbers <code>arr1</code> and <code>arr2</code> in base <strong>-2</strong>, return the result of adding them together.</p>

<p>Each number is given in <em>array format</em>:&nbsp; as an array of 0s and 1s, from most significant bit to least significant bit.&nbsp; For example, <code>arr = [1,1,0,1]</code> represents the number <code>(-2)^3&nbsp;+ (-2)^2 + (-2)^0 = -3</code>.&nbsp; A number <code>arr</code> in <em>array format</em> is also guaranteed to have no leading zeros: either&nbsp;<code>arr == [0]</code> or <code>arr[0] == 1</code>.</p>

<p>Return the result of adding <code>arr1</code> and <code>arr2</code> in the same format: as an array of 0s and 1s with no leading zeros.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>arr1 = <span id="example-input-1-1">[1,1,1,1,1]</span>, arr2 = <span id="example-input-1-2">[1,0,1]</span>
<strong>Output: </strong><span id="example-output-1">[1,0,0,0,0]
</span><strong>Explanation: </strong>arr1 represents 11, arr2 represents 5, the output represents 16.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= arr1.length &lt;= 1000</code></li>
	<li><code>1 &lt;= arr2.length &lt;= 1000</code></li>
	<li><code>arr1</code> and <code>arr2</code> have no leading zeros</li>
	<li><code>arr1[i]</code> is <code>0</code> or <code>1</code></li>
	<li><code>arr2[i]</code> is <code>0</code> or <code>1</code></li>
</ol>


------

**题目：** 
<p>给出基数为 <strong>-2</strong>&nbsp;的两个数&nbsp;<code>arr1</code> 和&nbsp;<code>arr2</code>，返回两数相加的结果。</p>

<p>数字以&nbsp;<strong>数组形式&nbsp;</strong>给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列。例如，<code>arr&nbsp;= [1,1,0,1]</code>&nbsp;表示数字&nbsp;<code>(-2)^3&nbsp;+ (-2)^2 + (-2)^0 = -3</code>。<strong>数组形式&nbsp;</strong>的数字也同样不含前导零：以 <code>arr</code> 为例，这意味着要么&nbsp;<code>arr == [0]</code>，要么&nbsp;<code>arr[0] == 1</code>。</p>

<p>返回相同表示形式的 <code>arr1</code> 和 <code>arr2</code> 相加的结果。两数的表示形式为：不含前导零、由若干 0 和 1 组成的数组。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>arr1 = [1,1,1,1,1], arr2 = [1,0,1]
<strong>输出：</strong>[1,0,0,0,0]
<strong>解释：</strong>arr1 表示 11，arr2 表示 5，输出表示 16 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= arr1.length &lt;= 1000</code></li>
	<li><code>1 &lt;= arr2.length &lt;= 1000</code></li>
	<li><code>arr1</code> 和&nbsp;<code>arr2</code>&nbsp;都不含前导零</li>
	<li><code>arr1[i]</code> 为&nbsp;<code>0</code>&nbsp;或&nbsp;<code>1</code></li>
	<li><code>arr2[i]</code>&nbsp;为&nbsp;<code>0</code> 或&nbsp;<code>1</code></li>
</ol>

