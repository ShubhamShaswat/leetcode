#### 不同的子序列 II/Distinct Subsequences II
**难度：** 困难/Hard

**Question：** 

<p>Given a string <code>S</code>, count the number of distinct, non-empty subsequences of <code>S</code> .</p>

<p>Since the result may be large, <strong>return the answer modulo <code>10^9 + 7</code></strong>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;abc&quot;</span>
<strong>Output: </strong><span id="example-output-1">7</span>
<span><strong>Explanation</strong>: The 7 distinct subsequences are &quot;a&quot;, &quot;b&quot;, &quot;c&quot;, &quot;ab&quot;, &quot;ac&quot;, &quot;bc&quot;, and &quot;abc&quot;.</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">&quot;aba&quot;</span>
<strong>Output: </strong><span id="example-output-2">6
</span><strong>Explanation</strong>: The 6 distinct subsequences are &quot;a&quot;, &quot;b&quot;, &quot;ab&quot;, &quot;ba&quot;, &quot;aa&quot; and &quot;aba&quot;.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">&quot;aaa&quot;</span>
<strong>Output: </strong><span id="example-output-3">3
</span><strong>Explanation</strong>: The 3 distinct subsequences are &quot;a&quot;, &quot;aa&quot; and &quot;aaa&quot;.
</pre>
</div>
</div>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>S</code> contains only lowercase letters.</li>
	<li><code>1 &lt;= S.length &lt;= 2000</code></li>
</ol>

<div>
<p>&nbsp;</p>

<div>
<div>&nbsp;</div>
</div>
</div>

------

**题目：** 
<p>给定一个字符串&nbsp;<code>S</code>，计算&nbsp;<code>S</code>&nbsp;的不同非空子序列的个数。</p>

<p>因为结果可能很大，所以<strong>返回答案模</strong><strong> <code>10^9 + 7</code></strong>.</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>&quot;abc&quot;
<strong>输出：</strong>7
<strong>解释：</strong>7 个不同的子序列分别是 &quot;a&quot;, &quot;b&quot;, &quot;c&quot;, &quot;ab&quot;, &quot;ac&quot;, &quot;bc&quot;, 以及 &quot;abc&quot;。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>&quot;aba&quot;
<strong>输出：</strong>6
<strong>解释：</strong>6 个不同的子序列分别是 &quot;a&quot;, &quot;b&quot;, &quot;ab&quot;, &quot;ba&quot;, &quot;aa&quot; 以及 &quot;aba&quot;。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>&quot;aaa&quot;
<strong>输出：</strong>3
<strong>解释：</strong>3 个不同的子序列分别是 &quot;a&quot;, &quot;aa&quot; 以及 &quot;aaa&quot;。
</pre>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>S</code>&nbsp;只包含小写字母。</li>
	<li><code>1 &lt;= S.length &lt;= 2000</code></li>
</ol>

<p>&nbsp;</p>

<p>&nbsp;</p>

