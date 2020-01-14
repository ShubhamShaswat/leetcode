#### 特殊等价字符串组/Groups of Special-Equivalent Strings
**难度：** 简单/Easy

**Question：** 

<p>You are given an array <code>A</code> of strings.</p>

<p>A <em>move&nbsp;onto <code>S</code></em> consists of swapping any two even indexed characters of <code>S</code>, or any two odd indexed characters of <code>S</code>.</p>

<p>Two strings <code>S</code> and <code>T</code> are&nbsp;<em>special-equivalent</em>&nbsp;if after any number of <em>moves onto <code>S</code></em>, <code>S == T</code>.</p>

<p>For example, <code>S = &quot;zzxy&quot;</code> and <code>T = &quot;xyzz&quot;</code> are special-equivalent because we may make the moves <code>&quot;zzxy&quot; -&gt; &quot;xzzy&quot; -&gt; &quot;xyzz&quot;</code>&nbsp;that swap <code>S[0]</code> and <code>S[2]</code>, then <code>S[1]</code> and <code>S[3]</code>.</p>

<p>Now, a <em>group of special-equivalent strings from <code>A</code></em>&nbsp;is a non-empty subset of&nbsp;A such that:</p>

<ol>
	<li>Every pair of strings in the group are special equivalent, and;</li>
	<li>The group is the largest size possible (ie., there isn&#39;t a string S not in the group such that S is special equivalent to every string in the group)</li>
</ol>

<p>Return the number of groups of special-equivalent strings from <code>A</code>.</p>

<div>&nbsp;</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;abcd&quot;,&quot;cdab&quot;,&quot;cbad&quot;,&quot;xyzz&quot;,&quot;zzxy&quot;,&quot;zzyx&quot;]</span>
<strong>Output: </strong><span id="example-output-1">3</span>
<strong>Explanation: </strong>
One group is [&quot;abcd&quot;, &quot;cdab&quot;, &quot;cbad&quot;], since they are all pairwise special equivalent, and none of the other strings are all pairwise special equivalent to these.

The other two groups are [&quot;xyzz&quot;, &quot;zzxy&quot;] and [&quot;zzyx&quot;].  Note that in particular, &quot;zzxy&quot; is not special equivalent to &quot;zzyx&quot;.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[&quot;abc&quot;,&quot;acb&quot;,&quot;bac&quot;,&quot;bca&quot;,&quot;cab&quot;,&quot;cba&quot;]</span>
<strong>Output: </strong><span id="example-output-2">3</span></pre>

<p>&nbsp;</p>
</div>
</div>

<div>
<div>
<div>
<div>
<p><strong>Note:</strong></p>

<ul>
	<li><code>1 &lt;= A.length &lt;= 1000</code></li>
	<li><code>1 &lt;= A[i].length &lt;= 20</code></li>
	<li>All <code>A[i]</code> have the same length.</li>
	<li>All <code>A[i]</code> consist of only lowercase letters.</li>
</ul>
</div>
</div>
</div>
</div>


------

**题目：** 
<p>你将得到一个字符串数组 <code>A</code>。</p>

<p>如果经过任意次数的移动，S == T，那么两个字符串 <code>S</code> 和 <code>T</code> 是<strong>特殊等价</strong>的。</p>

<p>一次<strong>移动</strong>包括选择两个索引 <code>i</code> 和 <code>j</code>，且&nbsp;<code>i ％ 2 == j ％ 2</code>，交换 <code>S[j]</code> 和 <code>S [i]</code>。</p>

<p>现在规定，<strong><code>A</code> 中的特殊等价字符串组</strong>是 <code>A</code> 的非空子集 <code>S</code>，这样不在 <code>S</code> 中的任何字符串与 <code>S</code> 中的任何字符串都不是特殊等价的。</p>

<p>返回 <code>A</code>&nbsp;中特殊等价字符串组的数量。</p>

<p>&nbsp;</p>

<ul>
</ul>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[&quot;a&quot;,&quot;b&quot;,&quot;c&quot;,&quot;a&quot;,&quot;c&quot;,&quot;c&quot;]
<strong>输出：</strong>3
<strong>解释：</strong>3<strong> </strong>组 [&quot;a&quot;,&quot;a&quot;]，[&quot;b&quot;]，[&quot;c&quot;,&quot;c&quot;,&quot;c&quot;]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[&quot;aa&quot;,&quot;bb&quot;,&quot;ab&quot;,&quot;ba&quot;]
<strong>输出：</strong>4
<strong>解释：</strong>4 组 [&quot;aa&quot;]，[&quot;bb&quot;]，[&quot;ab&quot;]，[&quot;ba&quot;]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[&quot;abc&quot;,&quot;acb&quot;,&quot;bac&quot;,&quot;bca&quot;,&quot;cab&quot;,&quot;cba&quot;]
<strong>输出：</strong>3
<strong>解释：</strong>3 组 [&quot;abc&quot;,&quot;cba&quot;]，[&quot;acb&quot;,&quot;bca&quot;]，[&quot;bac&quot;,&quot;cab&quot;]
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>[&quot;abcd&quot;,&quot;cdab&quot;,&quot;adcb&quot;,&quot;cbad&quot;]
<strong>输出：</strong>1
<strong>解释：</strong>1 组 [&quot;abcd&quot;,&quot;cdab&quot;,&quot;adcb&quot;,&quot;cbad&quot;]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= A.length &lt;= 1000</code></li>
	<li><code>1 &lt;= A[i].length &lt;= 20</code></li>
	<li>所有&nbsp;<code>A[i]</code>&nbsp;都具有相同的长度。</li>
	<li>所有&nbsp;<code>A[i]</code>&nbsp;都只由小写字母组成。</li>
</ul>

