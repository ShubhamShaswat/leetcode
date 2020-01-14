#### 公平的糖果交换/Fair Candy Swap
**难度：** 简单/Easy

**Question：** 

<p>Alice and Bob have candy bars of different sizes: <code>A[i]</code> is the size of the <code>i</code>-th bar of candy that Alice has, and <code>B[j]</code> is the size of the <code>j</code>-th bar of candy that Bob has.</p>

<p>Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total&nbsp;amount of candy.&nbsp; (<em>The total amount of candy&nbsp;a person has is the sum of the sizes of candy&nbsp;bars they have.</em>)</p>

<p>Return an integer array <code>ans</code>&nbsp;where <code>ans[0]</code> is the size of the candy bar that Alice must exchange, and <code>ans[1]</code> is the size of the candy bar that Bob must exchange.</p>

<p>If there are multiple answers, you may return any one of them.&nbsp; It is guaranteed an answer exists.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1,1]</span>, B = <span id="example-input-1-2">[2,2]</span>
<strong>Output: </strong><span id="example-output-1">[1,2]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[1,2]</span>, B = <span id="example-input-2-2">[2,3]</span>
<strong>Output: </strong><span id="example-output-2">[1,2]</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">[2]</span>, B = <span id="example-input-3-2">[1,3]</span>
<strong>Output: </strong><span id="example-output-3">[2,3]</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-4-1">[1,2,5]</span>, B = <span id="example-input-4-2">[2,4]</span>
<strong>Output: </strong><span id="example-output-4">[5,4]</span>
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ul>
	<li><span><code>1 &lt;= A.length &lt;= 10000</code></span></li>
	<li><span><code>1 &lt;= B.length &lt;= 10000</code></span></li>
	<li><code><span>1 &lt;= A[i] &lt;= 100000</span></code></li>
	<li><code><span>1 &lt;= B[i] &lt;= 100000</span></code></li>
	<li>It is guaranteed that Alice and Bob have different total amounts of&nbsp;candy.</li>
	<li>It is guaranteed there exists an&nbsp;answer.</li>
</ul>
</div>
</div>
</div>
</div>


------

**题目：** 
<p>爱丽丝和鲍勃有不同大小的糖果棒：<code>A[i]</code> 是爱丽丝拥有的第 <code>i</code>&nbsp;块糖的大小，<code>B[j]</code> 是鲍勃拥有的第 <code>j</code>&nbsp;块糖的大小。</p>

<p>因为他们是朋友，所以他们想交换一个糖果棒，这样交换后，他们都有相同的糖果总量。<em>（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）</em></p>

<p>返回一个整数数组 <code>ans</code>，其中 <code>ans[0]</code> 是爱丽丝必须交换的糖果棒的大小，<code>ans[1]</code>&nbsp;是 Bob 必须交换的糖果棒的大小。</p>

<p>如果有多个答案，你可以返回其中任何一个。保证答案存在。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>A = [1,1], B = [2,2]
<strong>输出：</strong>[1,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>A = [1,2], B = [2,3]
<strong>输出：</strong>[1,2]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>A = [2], B = [1,3]
<strong>输出：</strong>[2,3]
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>A = [1,2,5], B = [2,4]
<strong>输出：</strong>[5,4]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= A.length &lt;= 10000</code></li>
	<li><code>1 &lt;= B.length &lt;= 10000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 100000</code></li>
	<li><code>1 &lt;= B[i] &lt;= 100000</code></li>
	<li>保证爱丽丝与鲍勃的糖果总量不同。</li>
	<li>答案肯定存在。</li>
</ul>

