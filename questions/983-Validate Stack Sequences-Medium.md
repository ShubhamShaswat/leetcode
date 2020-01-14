#### 验证栈序列/Validate Stack Sequences
**难度：** 中等/Medium

**Question：** 

<p>Given two sequences <code>pushed</code> and <code>popped</code>&nbsp;<strong>with distinct values</strong>,&nbsp;return <code>true</code> if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>pushed = <span id="example-input-1-1">[1,2,3,4,5]</span>, popped = <span id="example-input-1-2">[4,5,3,2,1]</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation: </strong>We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -&gt; 4,
push(5), pop() -&gt; 5, pop() -&gt; 3, pop() -&gt; 2, pop() -&gt; 1
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>pushed = <span id="example-input-2-1">[1,2,3,4,5]</span>, popped = <span id="example-input-2-2">[4,3,5,1,2]</span>
<strong>Output: </strong><span id="example-output-2">false</span>
<strong>Explanation: </strong>1 cannot be popped before 2.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= pushed.length == popped.length &lt;= 1000</code></li>
	<li><code>0 &lt;= pushed[i], popped[i] &lt; 1000</code></li>
	<li><code>pushed</code> is a permutation of <code>popped</code>.</li>
	<li><code>pushed</code> and <code>popped</code> have distinct values.</li>
</ol>
</div>
</div>

------

**题目：** 
<p>给定&nbsp;<code>pushed</code>&nbsp;和&nbsp;<code>popped</code>&nbsp;两个序列，每个序列中的 <strong>值都不重复</strong>，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 <code>true</code>；否则，返回 <code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
<strong>输出：</strong>true
<strong>解释：</strong>我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -&gt; 4,
push(5), pop() -&gt; 5, pop() -&gt; 3, pop() -&gt; 2, pop() -&gt; 1
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
<strong>输出：</strong>false
<strong>解释：</strong>1 不能在 2 之前弹出。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>0 &lt;= pushed.length == popped.length &lt;= 1000</code></li>
	<li><code>0 &lt;= pushed[i], popped[i] &lt; 1000</code></li>
	<li><code>pushed</code>&nbsp;是&nbsp;<code>popped</code>&nbsp;的排列。</li>
</ol>

