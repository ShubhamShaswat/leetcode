#### 分割平衡字符串/Split a String in Balanced Strings
**难度：** 简单/Easy

**Question：** 

<p><i data-stringify-type="italic">Balanced</i>&nbsp;strings are those who have equal quantity of &#39;L&#39; and &#39;R&#39; characters.</p>

<p>Given a balanced string&nbsp;<code data-stringify-type="code">s</code>&nbsp;split it in the maximum amount of balanced strings.</p>

<p>Return the maximum amount of splitted balanced strings.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;RLRRLLRLRL&quot;
<strong>Output:</strong> 4
<strong>Explanation: </strong>s can be split into &quot;RL&quot;, &quot;RRLL&quot;, &quot;RL&quot;, &quot;RL&quot;, each substring contains same number of &#39;L&#39; and &#39;R&#39;.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;RLLLLRRRLR&quot;
<strong>Output:</strong> 3
<strong>Explanation: </strong>s can be split into &quot;RL&quot;, &quot;LLLRRR&quot;, &quot;LR&quot;, each substring contains same number of &#39;L&#39; and &#39;R&#39;.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;LLLLRRRR&quot;
<strong>Output:</strong> 1
<strong>Explanation: </strong>s can be split into &quot;LLLLRRRR&quot;.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;RLRRRLLRLL&quot;
<strong>Output:</strong> 2
<strong>Explanation: </strong>s can be split into &quot;RL&quot;, &quot;RRRLLRLL&quot;, since each substring contains an equal number of &#39;L&#39; and &#39;R&#39;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i] = &#39;L&#39; or &#39;R&#39;</code></li>
</ul>


------

**题目：** 
<p>在一个「平衡字符串」中，&#39;L&#39; 和 &#39;R&#39; 字符的数量是相同的。</p>

<p>给出一个平衡字符串&nbsp;<code>s</code>，请你将它分割成尽可能多的平衡字符串。</p>

<p>返回可以通过分割得到的平衡字符串的最大数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;RLRRLLRLRL&quot;
<strong>输出：</strong>4
<strong>解释：</strong>s 可以分割为 &quot;RL&quot;, &quot;RRLL&quot;, &quot;RL&quot;, &quot;RL&quot;, 每个子字符串中都包含相同数量的 &#39;L&#39; 和 &#39;R&#39;。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;RLLLLRRRLR&quot;
<strong>输出：</strong>3
<strong>解释：</strong>s 可以分割为 &quot;RL&quot;, &quot;LLLRRR&quot;, &quot;LR&quot;, 每个子字符串中都包含相同数量的 &#39;L&#39; 和 &#39;R&#39;。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;LLLLRRRR&quot;
<strong>输出：</strong>1
<strong>解释：</strong>s 只能保持原样 &quot;LLLLRRRR&quot;.
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i] = &#39;L&#39; 或 &#39;R&#39;</code></li>
</ul>

