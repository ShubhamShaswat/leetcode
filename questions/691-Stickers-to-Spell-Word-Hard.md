#### 贴纸拼词/Stickers to Spell Word
**难度：** 困难/Hard

**Question：** 

<p>
We are given N different types of stickers.  Each sticker has a lowercase English word on it.
</p><p>
You would like to spell out the given <code>target</code> string by cutting individual letters from your collection of stickers and rearranging them.
</p><p>
You can use each sticker more than once if you want, and you have infinite quantities of each sticker.
</p><p>
What is the minimum number of stickers that you need to spell out the <code>target</code>?  If the task is impossible, return -1.
</p>

<p><b>Example 1:</b></p>
<p>Input:<pre>
["with", "example", "science"], "thehat"
</pre></p>

<p>Output:<pre>
3
</pre></p>

<p>Explanation:<pre>
We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
</pre></p>

<p><b>Example 2:</b></p>
<p>Input:<pre>
["notice", "possible"], "basicbasic"
</pre></p>

<p>Output:<pre>
-1
</pre></p>

<p>Explanation:<pre>
We can't form the target "basicbasic" from cutting letters from the given stickers.
</pre></p>

<p><b>Note:</b>
<li><code>stickers</code> has length in the range <code>[1, 50]</code>.</li>
<li><code>stickers</code> consists of lowercase English words (without apostrophes).</li>
<li><code>target</code> has length in the range <code>[1, 15]</code>, and consists of lowercase English letters.</li>
<li>In all test cases, all words were chosen <u>randomly</u> from the 1000 most common US English words, and the target was chosen as a concatenation of two random words.</li>
<li>The time limit may be more challenging than usual.  It is expected that a 50 sticker test case can be solved within 35ms on average.</li>
</p>

------

**题目：** 
<p>我们给出了 N 种不同类型的贴纸。每个贴纸上都有一个小写的英文单词。</p>

<p>你希望从自己的贴纸集合中裁剪单个字母并重新排列它们，从而拼写出给定的目标字符串 <code>target</code>。</p>

<p>如果你愿意的话，你可以不止一次地使用每一张贴纸，而且每一张贴纸的数量都是无限的。</p>

<p>拼出目标&nbsp;<code>target</code> 所需的最小贴纸数量是多少？如果任务不可能，则返回 -1。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p>输入：</p>

<pre>[&quot;with&quot;, &quot;example&quot;, &quot;science&quot;], &quot;thehat&quot;
</pre>

<p>输出：</p>

<pre>3
</pre>

<p>解释：</p>

<pre>我们可以使用 2 个 &quot;with&quot; 贴纸，和 1 个 &quot;example&quot; 贴纸。
把贴纸上的字母剪下来并重新排列后，就可以形成目标 &ldquo;thehat&ldquo; 了。
此外，这是形成目标字符串所需的最小贴纸数量。
</pre>

<p><strong>示例 2：</strong></p>

<p>输入：</p>

<pre>[&quot;notice&quot;, &quot;possible&quot;], &quot;basicbasic&quot;
</pre>

<p>输出：</p>

<pre>-1
</pre>

<p>解释：</p>

<pre>我们不能通过剪切给定贴纸的字母来形成目标&ldquo;basicbasic&rdquo;。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>stickers</code> 长度范围是&nbsp;<code>[1, 50]</code>。</li>
	<li><code>stickers</code> 由小写英文单词组成（不带撇号）。</li>
	<li><code>target</code> 的长度在&nbsp;<code>[1, 15]</code>&nbsp;范围内，由小写字母组成。</li>
	<li>在所有的测试案例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选取的，目标是两个随机单词的串联。</li>
	<li>时间限制可能比平时更具挑战性。预计 50 个贴纸的测试案例平均可在35ms内解决。</li>
</ul>

<p>&nbsp;</p>

