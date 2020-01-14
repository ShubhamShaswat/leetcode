#### RLE 迭代器/RLE Iterator
**难度：** 中等/Medium

**Question：** 

<p>Write an iterator that iterates through a run-length encoded sequence.</p>

<p>The iterator is initialized by <code>RLEIterator(int[] A)</code>, where <code>A</code> is a run-length encoding of some&nbsp;sequence.&nbsp; More specifically,&nbsp;for all even <code>i</code>,&nbsp;<code>A[i]</code> tells us the number of times that the non-negative integer value <code>A[i+1]</code> is repeated in the sequence.</p>

<p>The iterator supports one function:&nbsp;<code>next(int n)</code>, which exhausts the next <code>n</code> elements&nbsp;(<code>n &gt;= 1</code>) and returns the last element exhausted in this way.&nbsp; If there is no element left to exhaust, <code>next</code>&nbsp;returns <code>-1</code> instead.</p>

<p>For example, we start with <code>A = [3,8,0,9,2,5]</code>, which is a run-length encoding of the sequence <code>[8,8,8,5,5]</code>.&nbsp; This is because the sequence can be read as&nbsp;&quot;three eights, zero nines, two fives&quot;.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;RLEIterator&quot;,&quot;next&quot;,&quot;next&quot;,&quot;next&quot;,&quot;next&quot;]</span>, <span id="example-input-1-2">[[[3,8,0,9,2,5]],[2],[1],[1],[2]]</span>
<strong>Output: </strong><span id="example-output-1">[null,8,8,5,-1]</span>
<strong>Explanation: </strong>
RLEIterator is initialized with RLEIterator([3,8,0,9,2,5]).
This maps to the sequence [8,8,8,5,5].
RLEIterator.next is then called 4 times:

.next(2) exhausts 2 terms of the sequence, returning 8.  The remaining sequence is now [8, 5, 5].

.next(1) exhausts 1 term of the sequence, returning 8.  The remaining sequence is now [5, 5].

.next(1) exhausts 1 term of the sequence, returning 5.  The remaining sequence is now [5].

.next(2) exhausts 2 terms, returning -1.  This is because the first term exhausted was 5,
but the second term did not exist.  Since the last term exhausted does not exist, we return -1.

</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt;= 1000</code></li>
	<li><code>A.length</code>&nbsp;is an even integer.</li>
	<li><code>0 &lt;= A[i] &lt;= 10^9</code></li>
	<li>There are at most <code>1000</code> calls to <code>RLEIterator.next(int n)</code> per test case.</li>
	<li>Each call to&nbsp;<code>RLEIterator.next(int n)</code>&nbsp;will have <code>1 &lt;= n &lt;= 10^9</code>.</li>
</ol>


------

**题目：** 
<p>编写一个遍历游程编码序列的迭代器。</p>

<p>迭代器由 <code>RLEIterator(int[] A)</code> 初始化，其中&nbsp;<code>A</code>&nbsp;是某个序列的游程编码。更具体地，对于所有偶数 <code>i</code>，<code>A[i]</code> 告诉我们在序列中重复非负整数值 <code>A[i + 1]</code> 的次数。</p>

<p>迭代器支持一个函数：<code>next(int n)</code>，它耗尽接下来的&nbsp; <code>n</code> 个元素（<code>n &gt;= 1</code>）并返回以这种方式耗去的最后一个元素。如果没有剩余的元素可供耗尽，则&nbsp; <code>next</code>&nbsp;返回&nbsp;<code>-1</code> 。</p>

<p>例如，我们以&nbsp;<code>A = [3,8,0,9,2,5]</code>&nbsp;开始，这是序列&nbsp;<code>[8,8,8,5,5]</code>&nbsp;的游程编码。这是因为该序列可以读作 &ldquo;三个八，零个九，两个五&rdquo;。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>[&quot;RLEIterator&quot;,&quot;next&quot;,&quot;next&quot;,&quot;next&quot;,&quot;next&quot;], [[[3,8,0,9,2,5]],[2],[1],[1],[2]]
<strong>输出：</strong>[null,8,8,5,-1]
<strong>解释：</strong>
RLEIterator 由 RLEIterator([3,8,0,9,2,5]) 初始化。
这映射到序列 [8,8,8,5,5]。
然后调用 RLEIterator.next 4次。

.next(2) 耗去序列的 2 个项，返回 8。现在剩下的序列是 [8, 5, 5]。

.next(1) 耗去序列的 1 个项，返回 8。现在剩下的序列是 [5, 5]。

.next(1) 耗去序列的 1 个项，返回 5。现在剩下的序列是 [5]。

.next(2) 耗去序列的 2 个项，返回 -1。 这是由于第一个被耗去的项是 5，
但第二个项并不存在。由于最后一个要耗去的项不存在，我们返回 -1。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt;= 1000</code></li>
	<li><code>A.length</code>&nbsp;是偶数。</li>
	<li><code>0 &lt;= A[i] &lt;= 10^9</code></li>
	<li>每个测试用例最多调用&nbsp;<code>1000</code>&nbsp;次&nbsp;<code>RLEIterator.next(int n)</code>。</li>
	<li>每次调用&nbsp;<code>RLEIterator.next(int n)</code>&nbsp;都有&nbsp;<code>1 &lt;= n &lt;= 10^9</code>&nbsp;。</li>
</ol>

