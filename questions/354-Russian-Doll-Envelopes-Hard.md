#### 俄罗斯套娃信封问题/Russian Doll Envelopes
**难度：** 困难/Hard

**Question：** 

<p>You have a number of envelopes with widths and heights given as a pair of integers <code>(w, h)</code>. One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.</p>

<p>What is the maximum number of envelopes can you Russian doll? (put one inside other)</p>

<p><b>Note:</b><br />
Rotation is not allowed.</p>

<p><strong>Example:</strong></p>

<div>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[[5,4],[6,4],[6,7],[2,3]]</span>
<strong>Output: </strong><span id="example-output-1">3 
<strong>Explanation: T</strong></span>he maximum number of envelopes you can Russian doll is <code>3</code> ([2,3] =&gt; [5,4] =&gt; [6,7]).
</pre>
</div>


------

**题目：** 
<p>给定一些标记了宽度和高度的信封，宽度和高度以整数对形式&nbsp;<code>(w, h)</code>&nbsp;出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。</p>

<p>请计算最多能有多少个信封能组成一组&ldquo;俄罗斯套娃&rdquo;信封（即可以把一个信封放到另一个信封里面）。</p>

<p><strong>说明:</strong><br>
不允许旋转信封。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> envelopes = <code>[[5,4],[6,4],[6,7],[2,3]]</code>
<strong>输出:</strong> 3 
<strong>解释:</strong> 最多信封的个数为 <code>3, 组合为: </code>[2,3] =&gt; [5,4] =&gt; [6,7]。
</pre>
