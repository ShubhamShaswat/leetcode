#### 交换字符使得字符串相同/Minimum Swaps to Make Strings Equal
**难度：** 中等/Medium

**Question：** 

<p>You are given two strings&nbsp;<code>s1</code>&nbsp;and&nbsp;<code>s2</code>&nbsp;of equal length&nbsp;consisting of letters <code>&quot;x&quot;</code> and <code>&quot;y&quot;</code> <strong>only</strong>. Your task is to&nbsp;make these two strings equal to each other. You can swap any two characters that belong to <strong>different</strong> strings,&nbsp;which means: swap <code>s1[i]</code> and <code>s2[j]</code>.</p>

<p>Return&nbsp;the minimum number of swaps required&nbsp;to make&nbsp;<code>s1</code>&nbsp;and <code>s2</code> equal, or return&nbsp;<code>-1</code>&nbsp;if it is&nbsp;impossible to do so.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;xx&quot;, s2 = &quot;yy&quot;
<strong>Output:</strong> 1
<strong>Explanation: 
</strong>Swap s1[0] and s2[1], s1 = &quot;yx&quot;, s2 = &quot;yx&quot;.</pre>

<p><strong>Example 2:&nbsp;</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;xy&quot;, s2 = &quot;yx&quot;
<strong>Output:</strong> 2
<strong>Explanation: 
</strong>Swap s1[0] and s2[0], s1 = &quot;yy&quot;, s2 = &quot;xx&quot;.
Swap s1[0] and s2[1], s1 = &quot;xy&quot;, s2 = &quot;xy&quot;.
Note that you can&#39;t swap s1[0] and s1[1] to make s1 equal to &quot;yx&quot;, cause we can only swap chars in different strings.</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;xx&quot;, s2 = &quot;xy&quot;
<strong>Output:</strong> -1
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;xxyyxyxyxx&quot;, s2 = &quot;xyyxyxxxyx&quot;
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 1000</code></li>
	<li><code>s1, s2</code>&nbsp;only contain <code>&#39;x&#39;</code> or <code>&#39;y&#39;</code>.</li>
</ul>


------

**题目：** 
<p>有两个长度相同的字符串&nbsp;<code>s1</code> 和&nbsp;<code>s2</code>，且它们其中&nbsp;<strong>只含有</strong>&nbsp;字符&nbsp;<code>&quot;x&quot;</code> 和&nbsp;<code>&quot;y&quot;</code>，你需要通过「交换字符」的方式使这两个字符串相同。</p>

<p>每次「交换字符」的时候，你都可以在两个字符串中各选一个字符进行交换。</p>

<p>交换只能发生在两个不同的字符串之间，绝对不能发生在同一个字符串内部。也就是说，我们可以交换&nbsp;<code>s1[i]</code> 和&nbsp;<code>s2[j]</code>，但不能交换&nbsp;<code>s1[i]</code> 和&nbsp;<code>s1[j]</code>。</p>

<p>最后，请你返回使 <code>s1</code> 和 <code>s2</code> 相同的最小交换次数，如果没有方法能够使得这两个字符串相同，则返回&nbsp;<code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s1 = &quot;xx&quot;, s2 = &quot;yy&quot;
<strong>输出：</strong>1
<strong>解释：
</strong>交换 s1[0] 和 s2[1]，得到 s1 = &quot;yx&quot;，s2 = &quot;yx&quot;。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s1 = &quot;xy&quot;, s2 = &quot;yx&quot;
<strong>输出：</strong>2
<strong>解释：
</strong>交换 s1[0] 和 s2[0]，得到 s1 = &quot;yy&quot;，s2 = &quot;xx&quot; 。
交换 s1[0] 和 s2[1]，得到 s1 = &quot;xy&quot;，s2 = &quot;xy&quot; 。
注意，你不能交换 s1[0] 和 s1[1] 使得 s1 变成 &quot;yx&quot;，因为我们只能交换属于两个不同字符串的字符。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s1 = &quot;xx&quot;, s2 = &quot;xy&quot;
<strong>输出：</strong>-1
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>s1 = &quot;xxyyxyxyxx&quot;, s2 = &quot;xyyxyxxxyx&quot;
<strong>输出：</strong>4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 1000</code></li>
	<li><code>s1, s2</code>&nbsp;只包含&nbsp;<code>&#39;x&#39;</code>&nbsp;或&nbsp;<code>&#39;y&#39;</code>。</li>
</ul>

