#### 给定数字能组成的最大时间/Largest Time for Given Digits
**难度：** 简单/Easy

**Question：** 

<p>Given an array of 4 digits, return the largest 24 hour time that can be made.</p>

<p>The smallest 24 hour time is 00:00, and the largest is 23:59.&nbsp; Starting from 00:00, a time is larger if more time has elapsed since midnight.</p>

<p>Return the answer as a string of length 5.&nbsp; If no valid time can be made, return an empty string.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,3,4]</span>
<strong>Output: </strong><span id="example-output-1">&quot;23:41&quot;</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[5,5,5,5]</span>
<strong>Output: </strong><span id="example-output-2">&quot;&quot;</span>
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ol>
	<li><code>A.length == 4</code></li>
	<li><code>0 &lt;= A[i] &lt;= 9</code></li>
</ol>
</div>
</div>

------

**题目：** 
<p>给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。</p>

<p>最小的 24 小时制时间是&nbsp;00:00，而最大的是&nbsp;23:59。从 00:00 （午夜）开始算起，过得越久，时间越大。</p>

<p>以长度为 5 的字符串返回答案。如果不能确定有效时间，则返回空字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[1,2,3,4]
<strong>输出：</strong>&quot;23:41&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[5,5,5,5]
<strong>输出：</strong>&quot;&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>A.length == 4</code></li>
	<li><code>0 &lt;= A[i] &lt;= 9</code></li>
</ol>

