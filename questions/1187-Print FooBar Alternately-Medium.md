#### 交替打印FooBar/Print FooBar Alternately
**难度：** 中等/Medium

**Question：** 

<p>Suppose you are given the following code:</p>

<pre>
class FooBar {
  public void foo() {
&nbsp; &nbsp; for (int i = 0; i &lt; n; i++) {
&nbsp; &nbsp; &nbsp; print(&quot;foo&quot;);
&nbsp;   }
  }

  public void bar() {
&nbsp; &nbsp; for (int i = 0; i &lt; n; i++) {
&nbsp; &nbsp; &nbsp; print(&quot;bar&quot;);
&nbsp; &nbsp; }
  }
}
</pre>

<p>The same instance of <code>FooBar</code> will be passed to two different threads. Thread A will call&nbsp;<code>foo()</code> while thread B will call&nbsp;<code>bar()</code>.&nbsp;Modify the given program to output &quot;foobar&quot; <em>n</em> times.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<b>Input:</b> n = 1
<b>Output:</b> &quot;foobar&quot;
<strong>Explanation:</strong> There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar(). &quot;foobar&quot; is being output 1 time.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<b>Input:</b> n = 2
<b>Output:</b> &quot;foobarfoobar&quot;
<strong>Explanation:</strong> &quot;foobar&quot; is being output 2 times.
</pre>


------

**题目：** 
<p>我们提供一个类：</p>

<pre>
class FooBar {
  public void foo() {
&nbsp; &nbsp; for (int i = 0; i &lt; n; i++) {
&nbsp; &nbsp; &nbsp; print(&quot;foo&quot;);
&nbsp;   }
  }

  public void bar() {
&nbsp; &nbsp; for (int i = 0; i &lt; n; i++) {
&nbsp; &nbsp; &nbsp; print(&quot;bar&quot;);
&nbsp; &nbsp; }
  }
}
</pre>

<p>两个不同的线程将会共用一个 <code>FooBar</code>&nbsp;实例。其中一个线程将会调用&nbsp;<code>foo()</code>&nbsp;方法，另一个线程将会调用&nbsp;<code>bar()</code>&nbsp;方法。</p>

<p>请设计修改程序，以确保 &quot;foobar&quot; 被输出 n 次。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> n = 1
<strong>输出:</strong> &quot;foobar&quot;
<strong>解释:</strong> 这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，&quot;foobar&quot; 将被输出一次。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> n = 2
<strong>输出:</strong> &quot;foobarfoobar&quot;
<strong>解释:</strong> &quot;foobar&quot; 将被输出两次。
</pre>

