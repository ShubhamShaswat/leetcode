#### 有序队列/Orderly Queue
**难度：** 困难/Hard

**Question：** 

<p>A string <code>S</code> of lowercase letters is given.&nbsp; Then, we may make any number of <em>moves</em>.</p>

<p>In each move, we&nbsp;choose one&nbsp;of the first <code>K</code> letters (starting from the left), remove it,&nbsp;and place it at the end of the string.</p>

<p>Return the lexicographically smallest string we could have after any number of moves.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-1-1">&quot;cba&quot;</span>, K = <span id="example-input-1-2">1</span>
<strong>Output: </strong><span id="example-output-1">&quot;acb&quot;</span>
<strong>Explanation: </strong>
In the first move, we move the 1st character (&quot;c&quot;) to the end, obtaining the string &quot;bac&quot;.
In the second move, we move the 1st character (&quot;b&quot;) to the end, obtaining the final result &quot;acb&quot;.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-2-1">&quot;baaca&quot;</span>, K = <span id="example-input-2-2">3</span>
<strong>Output: </strong><span id="example-output-2">&quot;aaabc&quot;</span>
<strong>Explanation: </strong>
In the first move, we move the 1st character (&quot;b&quot;) to the end, obtaining the string &quot;aacab&quot;.
In the second move, we move the 3rd character (&quot;c&quot;) to the end, obtaining the final result &quot;aaabc&quot;.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= K &lt;= S.length&nbsp;&lt;= 1000</code></li>
	<li><code>S</code>&nbsp;consists of lowercase letters only.</li>
</ol>
</div>
</div>


------

**题目：** 
<p>给出了一个由小写字母组成的字符串 <code>S</code>。然后，我们可以进行任意次数的<em>移动</em>。</p>

<p>在每次移动中，我们选择前 <code>K</code> 个字母中的一个（从左侧开始），将其从原位置移除，并放置在字符串的末尾。</p>

<p>返回我们在任意次数的移动之后可以拥有的按字典顺序排列的最小字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>S = &quot;cba&quot;, K = 1
<strong>输出：</strong>&quot;acb&quot;
<strong>解释：</strong>
在第一步中，我们将第一个字符（&ldquo;c&rdquo;）移动到最后，获得字符串 &ldquo;bac&rdquo;。
在第二步中，我们将第一个字符（&ldquo;b&rdquo;）移动到最后，获得最终结果 &ldquo;acb&rdquo;。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>S = &quot;baaca&quot;, K = 3
<strong>输出：</strong>&quot;aaabc&quot;
<strong>解释：
</strong>在第一步中，我们将第一个字符（&ldquo;b&rdquo;）移动到最后，获得字符串 &ldquo;aacab&rdquo;。
在第二步中，我们将第三个字符（&ldquo;c&rdquo;）移动到最后，获得最终结果 &ldquo;aaabc&rdquo;。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= K &lt;= S.length&nbsp;&lt;= 1000</code></li>
	<li><code>S</code>&nbsp;只由小写字母组成。</li>
</ol>

