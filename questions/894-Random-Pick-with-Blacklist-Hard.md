#### 黑名单中的随机数/Random Pick with Blacklist
**难度：** 困难/Hard

**Question：** 

<p>Given a blacklist&nbsp;<code>B</code> containing unique integers&nbsp;from <code>[0, N)</code>, write a function to return a uniform random integer from <code>[0, N)</code> which is <strong>NOT</strong>&nbsp;in <code>B</code>.</p>

<p>Optimize it such that it minimizes the call to system&rsquo;s <code>Math.random()</code>.</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 1000000000</code></li>
	<li><code>0 &lt;= B.length &lt; min(100000, N)</code></li>
	<li><code>[0, N)</code>&nbsp;does NOT include N. See <a href="https://en.wikipedia.org/wiki/Interval_(mathematics)" target="_blank">interval notation</a>.</li>
</ol>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: 
</strong><span id="example-input-1-1">[&quot;Solution&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;]
</span><span id="example-input-1-2">[[1,[]],[],[],[]]</span>
<strong>Output: </strong><span id="example-output-1">[null,0,0,0]</span>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: 
</strong><span id="example-input-2-1">[&quot;Solution&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;]
</span><span id="example-input-2-2">[[2,[]],[],[],[]]</span>
<strong>Output: </strong><span id="example-output-2">[null,1,1,1]</span>
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: 
</strong><span id="example-input-3-1">[&quot;Solution&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;]
</span><span id="example-input-3-2">[[3,[1]],[],[],[]]</span>
<strong>Output: </strong><span id="example-output-3">[null,0,0,2]</span>
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: 
</strong><span id="example-input-4-1">[&quot;Solution&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;]
</span><span id="example-input-4-2">[[4,[2]],[],[],[]]</span>
<strong>Output: </strong><span id="example-output-4">[null,1,3,1]</span>
</pre>

<p><strong>Explanation of Input Syntax:</strong></p>

<p>The input is two lists:&nbsp;the subroutines called&nbsp;and their&nbsp;arguments.&nbsp;<code>Solution</code>&#39;s&nbsp;constructor has two arguments,&nbsp;<code>N</code> and the blacklist <code>B</code>. <code>pick</code> has no arguments.&nbsp;Arguments&nbsp;are&nbsp;always wrapped with a list, even if there aren&#39;t any.</p>


------

**题目：** 
<p>给定一个包含 [0，n ) 中独特的整数的黑名单 B，写一个函数从 [ 0，n ) 中返回一个<strong>不在</strong> B 中的随机整数。</p>

<p>对它进行优化使其尽量少调用系统方法 <code>Math.random()</code> 。</p>

<p><strong>提示:</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 1000000000</code></li>
	<li><code>0 &lt;= B.length &lt; min(100000, N)</code></li>
	<li><code>[0, N)</code>&nbsp;不包含&nbsp;N，详细参见&nbsp;<a href="https://en.wikipedia.org/wiki/Interval_(mathematics)" target="_blank">interval notation</a>&nbsp;。</li>
</ol>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入: 
</strong>[&quot;Solution&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;]
[[1,[]],[],[],[]]
<strong>输出: </strong>[null,0,0,0]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: 
</strong>[&quot;Solution&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;]
[[2,[]],[],[],[]]
<strong>输出: </strong>[null,1,1,1]
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入: 
</strong>[&quot;Solution&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;]
[[3,[1]],[],[],[]]
<strong>Output: </strong>[null,0,0,2]
</pre>

<p><strong>示例 4:</strong></p>

<pre>
<strong>输入: 
</strong>[&quot;Solution&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;]
[[4,[2]],[],[],[]]
<strong>输出: </strong>[null,1,3,1]
</pre>

<p><strong>输入语法说明：</strong></p>

<p>输入是两个列表：调用成员函数名和调用的参数。<code>Solution</code>的构造函数有两个参数，<code>N</code>&nbsp;和黑名单&nbsp;<code>B</code>。<code>pick</code>&nbsp;没有参数，输入参数是一个列表，即使参数为空，也会输入一个 [] 空列表。</p>

