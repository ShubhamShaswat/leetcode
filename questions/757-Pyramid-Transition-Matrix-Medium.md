#### 金字塔转换矩阵/Pyramid Transition Matrix
**难度：** 中等/Medium

**Question：** 

<p>We are stacking blocks to form a pyramid. Each block has a color which is a one letter string.</p>

<p>We are allowed to place any color block <code>C</code> on top of two adjacent blocks of colors <code>A</code> and <code>B</code>, if and only if <code>ABC</code> is an allowed triple.</p>

<p>We start with a bottom row of <code>bottom</code>, represented as a single string. We also start with a list of allowed triples <code>allowed</code>. Each allowed triple is represented as a string of length 3.</p>

<p>Return true if we can build the pyramid all the way to the top, otherwise false.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> bottom = &quot;BCD&quot;, allowed = [&quot;BCG&quot;, &quot;CDE&quot;, &quot;GEA&quot;, &quot;FFF&quot;]
<b>Output:</b> true
<b>Explanation:</b>
We can stack the pyramid like this:
    A
   / \
  G   E
 / \ / \
B   C   D

We are allowed to place G on top of B and C because BCG is an allowed triple.  Similarly, we can place E on top of C and D, then A on top of G and E.</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> bottom = &quot;AABA&quot;, allowed = [&quot;AAA&quot;, &quot;AAB&quot;, &quot;ABA&quot;, &quot;ABB&quot;, &quot;BAC&quot;]
<b>Output:</b> false
<b>Explanation:</b>
We can&#39;t stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li><code>bottom</code> will be a string with length in range <code>[2, 8]</code>.</li>
	<li><code>allowed</code> will have length in range <code>[0, 200]</code>.</li>
	<li>Letters in all strings will be chosen from the set <code>{&#39;A&#39;, &#39;B&#39;, &#39;C&#39;, &#39;D&#39;, &#39;E&#39;, &#39;F&#39;, &#39;G&#39;}</code>.</li>
</ol>

<p>&nbsp;</p>


------

**题目：** 
<p>现在，我们用一些方块来堆砌一个金字塔。 每个方块用仅包含一个字母的字符串表示。</p>

<p>使用三元组表示金字塔的堆砌规则如下：</p>

<p>对于三元组(A, B, C) ，&ldquo;C&rdquo;为顶层方块，方块&ldquo;A&rdquo;、&ldquo;B&rdquo;分别作为方块&ldquo;C&rdquo;下一层的的左、右子块。当且仅当(A, B, C)是被允许的三元组，我们才可以将其堆砌上。</p>

<p>初始时，给定金字塔的基层&nbsp;<code>bottom</code>，用一个字符串表示。一个允许的三元组列表&nbsp;<code>allowed</code>，每个三元组用一个长度为 3 的字符串表示。</p>

<p>如果可以由基层一直堆到塔尖就返回 true，否则返回 false。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> bottom = &quot;BCD&quot;, allowed = [&quot;BCG&quot;, &quot;CDE&quot;, &quot;GEA&quot;, &quot;FFF&quot;]
<strong>输出:</strong> true
<strong>解析:</strong>
可以堆砌成这样的金字塔:
    A
   / \
  G   E
 / \ / \
B   C   D

因为符合(&#39;B&#39;, &#39;C&#39;, &#39;G&#39;), (&#39;C&#39;, &#39;D&#39;, &#39;E&#39;) 和 (&#39;G&#39;, &#39;E&#39;, &#39;A&#39;) 三种规则。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> bottom = &quot;AABA&quot;, allowed = [&quot;AAA&quot;, &quot;AAB&quot;, &quot;ABA&quot;, &quot;ABB&quot;, &quot;BAC&quot;]
<strong>输出:</strong> false
<strong>解析:</strong>
无法一直堆到塔尖。
注意, 允许存在像 (A, B, C) 和 (A, B, D) 这样的三元组，其中 C != D。
</pre>

<p>&nbsp;</p>

<p><strong>注意：</strong></p>

<ol>
	<li><code>bottom</code> 的长度范围在&nbsp;<code>[2, 8]</code>。</li>
	<li><code>allowed</code> 的长度范围在<code>[0, 200]</code>。</li>
	<li>方块的标记字母范围为<code>{&#39;A&#39;, &#39;B&#39;, &#39;C&#39;, &#39;D&#39;, &#39;E&#39;, &#39;F&#39;, &#39;G&#39;}</code>。</li>
</ol>

