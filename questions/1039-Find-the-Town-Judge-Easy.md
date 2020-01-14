#### 找到小镇的法官/Find the Town Judge
**难度：** 简单/Easy

**Question：** 

<p>In a town, there are <code>N</code> people labelled from&nbsp;<code>1</code> to <code>N</code>.&nbsp; There is a rumor that one of these people is secretly the town judge.</p>

<p>If the&nbsp;town judge exists, then:</p>

<ol>
	<li>The town judge trusts nobody.</li>
	<li>Everybody (except for the town judge) trusts the town judge.</li>
	<li>There is exactly one person that satisfies properties 1 and 2.</li>
</ol>

<p>You are given <code>trust</code>, an array of pairs <code>trust[i] = [a, b]</code> representing that the person labelled <code>a</code> trusts the person labelled <code>b</code>.</p>

<p>If the town judge exists and can be identified, return the label of the town judge.&nbsp; Otherwise, return <code>-1</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-1-1">2</span>, trust = <span id="example-input-1-2">[[1,2]]</span>
<strong>Output: </strong><span id="example-output-1">2</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-2-1">3</span>, trust = <span id="example-input-2-2">[[1,3],[2,3]]</span>
<strong>Output: </strong><span id="example-output-2">3</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-3-1">3</span>, trust = <span id="example-input-3-2">[[1,3],[2,3],[3,1]]</span>
<strong>Output: </strong><span id="example-output-3">-1</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-4-1">3</span>, trust = <span id="example-input-4-2">[[1,2],[2,3]]</span>
<strong>Output: </strong><span id="example-output-4">-1</span>
</pre>

<div>
<p><strong>Example 5:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-5-1">4</span>, trust = <span id="example-input-5-2">[[1,3],[1,4],[2,3],[2,4],[4,3]]</span>
<strong>Output: </strong><span id="example-output-5">3</span></pre>

<p>&nbsp;</p>
</div>
</div>
</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 1000</code></li>
	<li><code>trust.length &lt;= 10000</code></li>
	<li><code>trust[i]</code> are all different</li>
	<li><code>trust[i][0] != trust[i][1]</code></li>
	<li><code>1 &lt;= trust[i][0], trust[i][1] &lt;= N</code></li>
</ol>


------

**题目：** 
<p>在一个小镇里，按从 <code>1</code> 到 <code>N</code> 标记了&nbsp;<code>N</code> 个人。传言称，这些人中有一个是小镇上的秘密法官。</p>

<p>如果小镇的法官真的存在，那么：</p>

<ol>
	<li>小镇的法官不相信任何人。</li>
	<li>每个人（除了小镇法官外）都信任小镇的法官。</li>
	<li>只有一个人同时满足属性 1 和属性 2 。</li>
</ol>

<p>给定数组&nbsp;<code>trust</code>，该数组由信任对 <code>trust[i] = [a, b]</code>&nbsp;组成，表示标记为 <code>a</code> 的人信任标记为 <code>b</code> 的人。</p>

<p>如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 <code>-1</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>N = 2, trust = [[1,2]]
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>N = 3, trust = [[1,3],[2,3]]
<strong>输出：</strong>3
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>N = 3, trust = [[1,3],[2,3],[3,1]]
<strong>输出：</strong>-1
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>N = 3, trust = [[1,2],[2,3]]
<strong>输出：</strong>-1
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
<strong>输出：</strong>3</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 1000</code></li>
	<li><code>trust.length &lt;= 10000</code></li>
	<li><code>trust[i]</code>&nbsp;是完全不同的</li>
	<li><code>trust[i][0] != trust[i][1]</code></li>
	<li><code>1 &lt;= trust[i][0], trust[i][1] &lt;= N</code></li>
</ol>

