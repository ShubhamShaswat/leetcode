#### 可被 5 整除的二进制前缀/Binary Prefix Divisible By 5
**难度：** 简单/Easy

**Question：** 

<p>Given an array <code>A</code> of <code>0</code>s and <code>1</code>s, consider <code>N_i</code>: the i-th subarray from <code>A[0]</code> to <code>A[i]</code>&nbsp;interpreted&nbsp;as a binary number (from most-significant-bit to least-significant-bit.)</p>

<p>Return a list of booleans&nbsp;<code>answer</code>, where <code>answer[i]</code> is <code>true</code>&nbsp;if and only if <code>N_i</code>&nbsp;is divisible by 5.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[0,1,1]</span>
<strong>Output: </strong><span id="example-output-1">[true,false,false]</span>
<strong>Explanation: </strong>
The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,1,1]</span>
<strong>Output: </strong><span id="example-output-2">[false,false,false]</span>
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[0,1,1,1,1,1]</span>
<strong>Output: </strong><span id="example-output-3">[true,false,false,false,true,false]</span>
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[1,1,1,0,1]</span>
<strong>Output: </strong><span id="example-output-4">[false,false,false,false,false]</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 30000</code></li>
	<li><code>A[i]</code> is <code>0</code> or <code>1</code></li>
</ol>


------

**题目：** 
<p>给定由若干&nbsp;<code>0</code>&nbsp;和&nbsp;<code>1</code>&nbsp;组成的数组 <code>A</code>。我们定义&nbsp;<code>N_i</code>：从&nbsp;<code>A[0]</code> 到&nbsp;<code>A[i]</code>&nbsp;的第 <code>i</code>&nbsp;个子数组被解释为一个二进制数（从最高有效位到最低有效位）。</p>

<p>返回布尔值列表&nbsp;<code>answer</code>，只有当&nbsp;<code>N_i</code>&nbsp;可以被 <code>5</code>&nbsp;整除时，答案&nbsp;<code>answer[i]</code> 为&nbsp;<code>true</code>，否则为 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[0,1,1]
<strong>输出：</strong>[true,false,false]
<strong>解释：</strong>
输入数字为 0, 01, 011；也就是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为真。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[1,1,1]
<strong>输出：</strong>[false,false,false]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[0,1,1,1,1,1]
<strong>输出：</strong>[true,false,false,false,true,false]
</pre>

<p><strong>示例&nbsp;4：</strong></p>

<pre><strong>输入：</strong>[1,1,1,0,1]
<strong>输出：</strong>[false,false,false,false,false]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 30000</code></li>
	<li><code>A[i]</code> 为&nbsp;<code>0</code>&nbsp;或&nbsp;<code>1</code></li>
</ol>

