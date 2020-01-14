#### 打印零与奇偶数/Print Zero Even Odd
**难度：** 中等/Medium

**Question：** 

<p>Suppose you are given the following code:</p>

<pre>
class ZeroEvenOdd {
&nbsp; public ZeroEvenOdd(int n) { ... }&nbsp;     // constructor
  public void zero(printNumber) { ... }  // only output 0&#39;s
  public void even(printNumber) { ... }  // only output even numbers
  public void odd(printNumber) { ... }   // only output odd numbers
}
</pre>

<p>The same instance of <code>ZeroEvenOdd</code> will be passed to three different threads:</p>

<ol>
	<li>Thread A will call&nbsp;<code>zero()</code>&nbsp;which should only output 0&#39;s.</li>
	<li>Thread B will call&nbsp;<code>even()</code>&nbsp;which should only ouput even numbers.</li>
	<li>Thread C will call <code>odd()</code>&nbsp;which should only output odd numbers.</li>
</ol>

<p>Each of the threads is given a&nbsp;<code>printNumber</code> method to output&nbsp;an integer. Modify the given program to output the series&nbsp;<code>010203040506</code>... where the length of the series must be 2<em>n</em>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<b>Input:</b> n = 2
<b>Output:</b> &quot;0102&quot;
<strong>Explanation:</strong> There are three threads being fired asynchronously. One of them calls zero(), the other calls even(), and the last one calls odd(). &quot;0102&quot; is the correct output.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<b>Input:</b> n = 5
<b>Output:</b> &quot;0102030405&quot;
</pre>


------

**题目：** 
<p>假设有这么一个类：</p>

<pre>class ZeroEvenOdd {
&nbsp; public ZeroEvenOdd(int n) { ... }&nbsp;     // 构造函数
  public void zero(printNumber) { ... }  // 仅打印出 0
  public void even(printNumber) { ... }  // 仅打印出 偶数
  public void odd(printNumber) { ... }   // 仅打印出 奇数
}
</pre>

<p>相同的一个&nbsp;<code>ZeroEvenOdd</code>&nbsp;类实例将会传递给三个不同的线程：</p>

<ol>
	<li>线程 A 将调用&nbsp;<code>zero()</code>，它只输出 0 。</li>
	<li>线程 B 将调用&nbsp;<code>even()</code>，它只输出偶数。</li>
	<li>线程 C 将调用&nbsp;<code>odd()</code>，它只输出奇数。</li>
</ol>

<p>每个线程都有一个&nbsp;<code>printNumber</code> 方法来输出一个整数。请修改给出的代码以输出整数序列&nbsp;<code>010203040506</code>... ，其中序列的长度必须为 2<em>n</em>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 2
<strong>输出：</strong>&quot;0102&quot;
<strong>说明：</strong>三条线程异步执行，其中一个调用 zero()，另一个线程调用 even()，最后一个线程调用odd()。正确的输出为 &quot;0102&quot;。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 5
<strong>输出：</strong>&quot;0102030405&quot;
</pre>

