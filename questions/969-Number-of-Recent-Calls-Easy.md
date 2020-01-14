#### 最近的请求次数/Number of Recent Calls
**难度：** 简单/Easy

**Question：** 

<p>Write a class <code>RecentCounter</code> to count recent requests.</p>

<p>It has only one method:&nbsp;<code>ping(int t)</code>, where t represents some time in milliseconds.</p>

<p>Return the number of <code>ping</code>s that have been made from 3000 milliseconds ago until now.</p>

<p>Any ping with time in <code>[t - 3000, t]</code> will count, including the current ping.</p>

<p>It is guaranteed that every call to <code>ping</code> uses a strictly larger value of&nbsp;<code>t</code> than before.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>inputs = <span id="example-input-1-1">[&quot;RecentCounter&quot;,&quot;ping&quot;,&quot;ping&quot;,&quot;ping&quot;,&quot;ping&quot;]</span>, inputs = <span id="example-input-1-2">[[],[1],[100],[3001],[3002]]</span>
<strong>Output: </strong><span id="example-output-1">[null,1,2,3,3]</span></pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>Each test case will have at most <code>10000</code> calls to <code>ping</code>.</li>
	<li>Each test case will call&nbsp;<code>ping</code> with strictly increasing values of <code>t</code>.</li>
	<li>Each call to ping will have <code>1 &lt;= t &lt;= 10^9</code>.</li>
</ol>

<div>
<p>&nbsp;</p>
</div>

------

**题目：** 
<p>写一个&nbsp;<code>RecentCounter</code>&nbsp;类来计算最近的请求。</p>

<p>它只有一个方法：<code>ping(int t)</code>，其中&nbsp;<code>t</code>&nbsp;代表以毫秒为单位的某个时间。</p>

<p>返回从 3000 毫秒前到现在的&nbsp;<code>ping</code>&nbsp;数。</p>

<p>任何处于&nbsp;<code>[t - 3000, t]</code>&nbsp;时间范围之内的 <code>ping</code>&nbsp;都将会被计算在内，包括当前（指 <code>t</code>&nbsp;时刻）的 <code>ping</code>。</p>

<p>保证每次对 <code>ping</code> 的调用都使用比之前更大的 <code>t</code> 值。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>inputs = [&quot;RecentCounter&quot;,&quot;ping&quot;,&quot;ping&quot;,&quot;ping&quot;,&quot;ping&quot;], inputs = [[],[1],[100],[3001],[3002]]
<strong>输出：</strong>[null,1,2,3,3]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>每个测试用例最多调用&nbsp;<code>10000</code>&nbsp;次&nbsp;<code>ping</code>。</li>
	<li>每个测试用例会使用严格递增的 <code>t</code> 值来调用&nbsp;<code>ping</code>。</li>
	<li>每次调用 <code>ping</code>&nbsp;都有&nbsp;<code>1 &lt;= t &lt;= 10^9</code>。</li>
</ol>

<p>&nbsp;</p>

