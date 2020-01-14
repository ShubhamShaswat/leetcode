#### 三等分/Three Equal Parts
**难度：** 困难/Hard

**Question：** 

<p>Given an array <code>A</code> of <code>0</code>s and <code>1</code>s, divide the array into 3 non-empty parts such that all of these parts represent the same binary value.</p>

<p>If it is possible, return <strong>any</strong> <code>[i, j]</code>&nbsp;with <code>i+1 &lt; j</code>, such that:</p>

<ul>
	<li><code>A[0], A[1], ..., A[i]</code> is the first part;</li>
	<li><code>A[i+1], A[i+2], ..., A[j-1]</code> is the second part, and</li>
	<li><code>A[j], A[j+1], ..., A[A.length - 1]</code> is the third part.</li>
	<li>All three parts have equal binary value.</li>
</ul>

<p>If it is not possible, return <code>[-1, -1]</code>.</p>

<p>Note that the entire part is used when considering what binary value it represents.&nbsp; For example, <code>[1,1,0]</code>&nbsp;represents <code>6</code>&nbsp;in decimal,&nbsp;not <code>3</code>.&nbsp; Also, leading zeros are allowed, so&nbsp;<code>[0,1,1]</code> and <code>[1,1]</code> represent the same value.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,0,1,0,1]</span>
<strong>Output: </strong><span id="example-output-1">[0,3]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,1,0,1,1]</span>
<strong>Output: </strong><span id="example-output-2">[-1,-1]</span></pre>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>3 &lt;= A.length &lt;= 30000</code></li>
	<li><code>A[i] == 0</code>&nbsp;or <code>A[i] == 1</code></li>
</ol>

<div>
<div>&nbsp;</div>
</div>

------

**题目：** 
<p>给定一个由 <code>0</code> 和 <code>1</code> 组成的数组&nbsp;<code>A</code>，将数组分成 3&nbsp;个非空的部分，使得所有这些部分表示相同的二进制值。</p>

<p>如果可以做到，请返回<strong>任何</strong>&nbsp;<code>[i, j]</code>，其中 <code>i+1 &lt; j</code>，这样一来：</p>

<ul>
	<li><code>A[0], A[1], ..., A[i]</code>&nbsp;组成第一部分；</li>
	<li><code>A[i+1], A[i+2], ..., A[j-1]</code>&nbsp;作为第二部分；</li>
	<li><code>A[j], A[j+1], ..., A[A.length - 1]</code> 是第三部分。</li>
	<li>这三个部分所表示的二进制值相等。</li>
</ul>

<p>如果无法做到，就返回&nbsp;<code>[-1, -1]</code>。</p>

<p>注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，<code>[1,1,0]</code>&nbsp;表示十进制中的&nbsp;<code>6</code>，而不会是&nbsp;<code>3</code>。此外，前导零也是被允许的，所以&nbsp;<code>[0,1,1]</code> 和&nbsp;<code>[1,1]</code>&nbsp;表示相同的值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[1,0,1,0,1]
<strong>输出：</strong>[0,3]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输出：</strong>[1,1,0,1,1]
<strong>输出：</strong>[-1,-1]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>3 &lt;= A.length &lt;= 30000</code></li>
	<li><code>A[i] == 0</code>&nbsp;或&nbsp;<code>A[i] == 1</code></li>
</ol>

<p>&nbsp;</p>

