#### 尽可能使字符串相等/Get Equal Substrings Within Budget
**难度：** 中等/Medium

**Question：** 

<p>You are given two strings <code>s</code> and <code>t</code> of the same length. You want to change <code>s</code> to <code>t</code>. Changing the <code>i</code>-th character of <code>s</code> to <code>i</code>-th character of <code>t</code> costs <code>|s[i] - t[i]|</code> that is, the absolute difference between the ASCII values of the characters.</p>

<p>You are also given an integer <code>maxCost</code>.</p>

<p>Return the maximum length of a substring of <code>s</code> that can be changed to be the same as the corresponding substring of <code>t</code>with a cost less than or equal to <code>maxCost</code>.</p>

<p>If there is no substring from&nbsp;<code>s</code> that can be changed to its corresponding substring from <code>t</code>, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcd&quot;, t = &quot;bcdf&quot;, maxCost = 3
<strong>Output:</strong> 3
<strong>Explanation: </strong>&quot;abc&quot; of s can change to &quot;bcd&quot;. That costs 3, so the maximum length is 3.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcd&quot;, t = &quot;cdef&quot;, maxCost = 3
<strong>Output:</strong> 1
<strong>Explanation: </strong>Each character in s costs 2 to change to charactor in <code>t, so the maximum length is 1.</code>
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcd&quot;, t = &quot;acde&quot;, maxCost = 0
<strong>Output:</strong> 1
<strong>Explanation: </strong>You can&#39;t make any change, so the maximum length is 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 10^5</code></li>
	<li><code>0 &lt;= maxCost &lt;= 10^6</code></li>
	<li><code>s</code> and&nbsp;<code>t</code> only contain lower case English letters.</li>
</ul>


------

**题目：** 
<p>给你两个长度相同的字符串，<code>s</code> 和 <code>t</code>。</p>

<p>将 <code>s</code>&nbsp;中的第&nbsp;<code>i</code>&nbsp;个字符变到&nbsp;<code>t</code>&nbsp;中的第 <code>i</code> 个字符需要&nbsp;<code>|s[i] - t[i]|</code>&nbsp;的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。</p>

<p>用于变更字符串的最大预算是&nbsp;<code>maxCost</code>。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。</p>

<p>如果你可以将 <code>s</code> 的子字符串转化为它在 <code>t</code> 中对应的子字符串，则返回可以转化的最大长度。</p>

<p>如果 <code>s</code> 中没有子字符串可以转化成 <code>t</code> 中对应的子字符串，则返回 <code>0</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;abcd&quot;, t = &quot;bcdf&quot;, cost = 3
<strong>输出：</strong>3
<strong>解释：</strong>s<strong> </strong>中的<strong> </strong>&quot;abc&quot; 可以变为 &quot;bcd&quot;。开销为 3，所以最大长度为 3。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;abcd&quot;, t = &quot;cdef&quot;, cost = 3
<strong>输出：</strong>1
<strong>解释：</strong>s 中的任一字符要想变成 t 中对应的字符，其开销都是 2。因此，最大长度为<code> 1。</code>
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;abcd&quot;, t = &quot;acde&quot;, cost = 0
<strong>输出：</strong>1
<strong>解释：</strong>你无法作出任何改动，所以最大长度为 1。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 10^5</code></li>
	<li><code>0 &lt;= maxCost &lt;= 10^6</code></li>
	<li><code>s</code> 和&nbsp;<code>t</code>&nbsp;都只含小写英文字母。</li>
</ul>

