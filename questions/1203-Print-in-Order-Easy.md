#### 按序打印/Print in Order
**难度：** 简单/Easy

**Question：** 

<p>Suppose we have a class:</p>

<pre>
public class Foo {
&nbsp; public void first() { print(&quot;first&quot;); }
&nbsp; public void second() { print(&quot;second&quot;); }
&nbsp; public void third() { print(&quot;third&quot;); }
}
</pre>

<p>The same instance of <code>Foo</code> will be passed to three different threads. Thread A will call <code>first()</code>, thread B will call <code>second()</code>, and thread C will call <code>third()</code>. Design a mechanism and modify the program&nbsp;to ensure that&nbsp;<code>second()</code>&nbsp;is executed after&nbsp;<code>first()</code>, and&nbsp;<code>third()</code> is executed after&nbsp;<code>second()</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<b>Input:</b> [1,2,3]
<b>Output:</b> &quot;firstsecondthird&quot;
<strong>Explanation:</strong> There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). &quot;firstsecondthird&quot; is the correct output.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<b>Input:</b> [1,3,2]
<b>Output:</b> &quot;firstsecondthird&quot;
<strong>Explanation:</strong> The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). &quot;firstsecondthird&quot; is the correct output.</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<p>We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seems to imply the ordering. The input format you see is mainly&nbsp;to ensure our tests&#39; comprehensiveness.</p>


------

**题目：** 
<p>我们提供了一个类：</p>

<pre>
public class Foo {
&nbsp; public void one() { print(&quot;one&quot;); }
&nbsp; public void two() { print(&quot;two&quot;); }
&nbsp; public void three() { print(&quot;three&quot;); }
}
</pre>

<p>三个不同的线程将会共用一个&nbsp;<code>Foo</code>&nbsp;实例。</p>

<ul>
	<li>线程 A 将会调用 <code>one()</code> 方法</li>
	<li>线程 B 将会调用&nbsp;<code>two()</code> 方法</li>
	<li>线程 C 将会调用 <code>three()</code> 方法</li>
</ul>

<p>请设计修改程序，以确保 <code>two()</code> 方法在 <code>one()</code> 方法之后被执行，<code>three()</code> 方法在 <code>two()</code> 方法之后被执行。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> [1,2,3]
<strong>输出:</strong> &quot;onetwothree&quot;
<strong>解释:</strong> 
有三个线程会被异步启动。
输入 [1,2,3] 表示线程 A 将会调用 one() 方法，线程 B 将会调用 two() 方法，线程 C 将会调用 three() 方法。
正确的输出是 &quot;onetwothree&quot;。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> [1,3,2]
<strong>输出:</strong> &quot;onetwothree&quot;
<strong>解释:</strong> 
输入 [1,3,2] 表示线程 A 将会调用 one() 方法，线程 B 将会调用 three() 方法，线程 C 将会调用 two() 方法。
正确的输出是 &quot;onetwothree&quot;。</pre>

<p>&nbsp;</p>

<p><strong>注意:</strong></p>

<p>尽管输入中的数字似乎暗示了顺序，但是我们并不保证线程在操作系统中的调度顺序。</p>

<p>你看到的输入格式主要是为了确保测试的全面性。</p>

