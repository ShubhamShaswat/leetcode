#### 一和零/Ones and Zeroes
**难度：** 中等/Medium

**Question：** 

<p>In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.</p>

<p>For now, suppose you are a dominator of <b>m</b> <code>0s</code> and <b>n</b> <code>1s</code> respectively. On the other hand, there is an array with strings consisting of only <code>0s</code> and <code>1s</code>.</p>

<p>Now your task is to find the maximum number of strings that you can form with given <b>m</b> <code>0s</code> and <b>n</b> <code>1s</code>. Each <code>0</code> and <code>1</code> can be used at most <b>once</b>.</p>

<p><b>Note:</b></p>

<ol>
	<li>The given numbers of <code>0s</code> and <code>1s</code> will both not exceed <code>100</code></li>
	<li>The size of given string array won&#39;t exceed <code>600</code>.</li>
</ol>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> Array = {&quot;10&quot;, &quot;0001&quot;, &quot;111001&quot;, &quot;1&quot;, &quot;0&quot;}, m = 5, n = 3
<b>Output:</b> 4

<b>Explanation:</b> This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are &ldquo;10,&rdquo;0001&rdquo;,&rdquo;1&rdquo;,&rdquo;0&rdquo;
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> Array = {&quot;10&quot;, &quot;0&quot;, &quot;1&quot;}, m = 1, n = 1
<b>Output:</b> 2

<b>Explanation:</b> You could form &quot;10&quot;, but then you&#39;d have nothing left. Better form &quot;0&quot; and &quot;1&quot;.
</pre>

<p>&nbsp;</p>


------

**题目：** 
<p>在计算机界中，我们总是追求用有限的资源获取最大的收益。</p>

<p>现在，假设你分别支配着 <strong>m</strong> 个&nbsp;<code>0</code>&nbsp;和 <strong>n</strong> 个&nbsp;<code>1</code>。另外，还有一个仅包含&nbsp;<code>0</code>&nbsp;和&nbsp;<code>1</code>&nbsp;字符串的数组。</p>

<p>你的任务是使用给定的&nbsp;<strong>m</strong> 个&nbsp;<code>0</code>&nbsp;和 <strong>n</strong> 个&nbsp;<code>1</code>&nbsp;，找到能拼出存在于数组中的字符串的最大数量。每个&nbsp;<code>0</code>&nbsp;和&nbsp;<code>1</code>&nbsp;至多被使用<strong>一次</strong>。</p>

<p><strong>注意:</strong></p>

<ol>
	<li>给定&nbsp;<code>0</code>&nbsp;和&nbsp;<code>1</code>&nbsp;的数量都不会超过&nbsp;<code>100</code>。</li>
	<li>给定字符串数组的长度不会超过&nbsp;<code>600</code>。</li>
</ol>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> Array = {&quot;10&quot;, &quot;0001&quot;, &quot;111001&quot;, &quot;1&quot;, &quot;0&quot;}, m = 5, n = 3
<strong>输出:</strong> 4

<strong>解释:</strong> 总共 4 个字符串可以通过 5 个 0 和 3 个 1 拼出，即 &quot;10&quot;,&quot;0001&quot;,&quot;1&quot;,&quot;0&quot; 。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> Array = {&quot;10&quot;, &quot;0&quot;, &quot;1&quot;}, m = 1, n = 1
<strong>输出:</strong> 2

<strong>解释:</strong> 你可以拼出 &quot;10&quot;，但之后就没有剩余数字了。更好的选择是拼出 &quot;0&quot; 和 &quot;1&quot; 。
</pre>

