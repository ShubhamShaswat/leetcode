#### 单词子集/Word Subsets
**难度：** 中等/Medium

**Question：** 

<p>We are given two arrays <code>A</code> and <code>B</code> of words.&nbsp; Each word is a string of lowercase letters.</p>

<p>Now, say that&nbsp;word <code>b</code> is a subset of word <code>a</code><strong>&nbsp;</strong>if every letter in <code>b</code> occurs in <code>a</code>, <strong>including multiplicity</strong>.&nbsp; For example, <code>&quot;wrr&quot;</code> is a subset of <code>&quot;warrior&quot;</code>, but is not a subset of <code>&quot;world&quot;</code>.</p>

<p>Now say a word <code>a</code> from <code>A</code> is <em>universal</em> if for every <code>b</code> in <code>B</code>, <code>b</code>&nbsp;is a subset of <code>a</code>.&nbsp;</p>

<p>Return a list of all universal words in <code>A</code>.&nbsp; You can return the words in any order.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;]</span>, B = <span id="example-input-1-2">[&quot;e&quot;,&quot;o&quot;]</span>
<strong>Output: </strong><span id="example-output-1">[&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;]</span>, B = <span id="example-input-2-2">[&quot;l&quot;,&quot;e&quot;]</span>
<strong>Output: </strong><span id="example-output-2">[&quot;apple&quot;,&quot;google&quot;,&quot;leetcode&quot;]</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">[&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;]</span>, B = <span id="example-input-3-2">[&quot;e&quot;,&quot;oo&quot;]</span>
<strong>Output: </strong><span id="example-output-3">[&quot;facebook&quot;,&quot;google&quot;]</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-4-1">[&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;]</span>, B = <span id="example-input-4-2">[&quot;lo&quot;,&quot;eo&quot;]</span>
<strong>Output: </strong><span id="example-output-4">[&quot;google&quot;,&quot;leetcode&quot;]</span>
</pre>

<div>
<p><strong>Example 5:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-5-1">[&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;]</span>, B = <span id="example-input-5-2">[&quot;ec&quot;,&quot;oc&quot;,&quot;ceo&quot;]</span>
<strong>Output: </strong><span id="example-output-5">[&quot;facebook&quot;,&quot;leetcode&quot;]</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length, B.length &lt;= 10000</code></li>
	<li><code>1 &lt;= A[i].length, B[i].length&nbsp;&lt;= 10</code></li>
	<li><code>A[i]</code> and <code>B[i]</code> consist only of lowercase letters.</li>
	<li>All words in <code>A[i]</code> are unique: there isn&#39;t <code>i != j</code> with <code>A[i] == A[j]</code>.</li>
</ol>
</div>
</div>
</div>
</div>
</div>


------

**题目：** 
<p>我们给出两个单词数组 <code>A</code>&nbsp;和&nbsp;<code>B</code>。每个单词都是一串小写字母。</p>

<p>现在，如果&nbsp;<code>b</code> 中的每个字母都出现在 <code>a</code> 中，<strong>包括重复出现的字母</strong>，那么称单词 <code>b</code> 是单词 <code>a</code> 的子集。 例如，&ldquo;wrr&rdquo; 是 &ldquo;warrior&rdquo; 的子集，但不是 &ldquo;world&rdquo; 的子集。</p>

<p>如果对 <code>B</code> 中的每一个单词&nbsp;<code>b</code>，<code>b</code> 都是 <code>a</code> 的子集，那么我们称&nbsp;<code>A</code> 中的单词 <code>a</code> 是<em>通用的</em>。</p>

<p>你可以按任意顺序以列表形式返回&nbsp;<code>A</code> 中所有的通用单词。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>A = [&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;], B = [&quot;e&quot;,&quot;o&quot;]
<strong>输出：</strong>[&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>A = [&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;], B = [&quot;l&quot;,&quot;e&quot;]
<strong>输出：</strong>[&quot;apple&quot;,&quot;google&quot;,&quot;leetcode&quot;]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>A = [&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;], B = [&quot;e&quot;,&quot;oo&quot;]
<strong>输出：</strong>[&quot;facebook&quot;,&quot;google&quot;]
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>A = [&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;], B = [&quot;lo&quot;,&quot;eo&quot;]
<strong>输出：</strong>[&quot;google&quot;,&quot;leetcode&quot;]
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>A = [&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;], B = [&quot;ec&quot;,&quot;oc&quot;,&quot;ceo&quot;]
<strong>输出：</strong>[&quot;facebook&quot;,&quot;leetcode&quot;]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length, B.length &lt;= 10000</code></li>
	<li><code>1 &lt;= A[i].length, B[i].length&nbsp;&lt;= 10</code></li>
	<li><code>A[i]</code>&nbsp;和&nbsp;<code>B[i]</code>&nbsp;只由小写字母组成。</li>
	<li><code>A[i]</code>&nbsp;中所有的单词都是独一无二的，也就是说不存在&nbsp;<code>i != j</code>&nbsp;使得&nbsp;<code>A[i] == A[j]</code>。</li>
</ol>

