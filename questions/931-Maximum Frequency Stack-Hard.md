#### 最大频率栈/Maximum Frequency Stack
**难度：** 困难/Hard

**Question：** 

<p>Implement <code>FreqStack</code>, a class which simulates the operation of a stack-like data structure.</p>

<p><code>FreqStack</code>&nbsp;has two functions:</p>

<ul>
	<li><code>push(int x)</code>, which pushes an integer <code>x</code> onto the stack.</li>
	<li><code>pop()</code>, which <strong>removes</strong> and returns the most frequent element in the stack.
	<ul>
		<li>If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.</li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>
<span id="example-input-1-1">[&quot;FreqStack&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;pop&quot;,&quot;pop&quot;,&quot;pop&quot;,&quot;pop&quot;]</span>,
<span id="example-input-1-2">[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]</span>
<strong>Output: </strong><span id="example-output-1">[null,null,null,null,null,null,null,5,7,5,4]</span>
<strong>Explanation</strong>:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -&gt; returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -&gt; returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -&gt; returns 5.
The stack becomes [5,7,4].

pop() -&gt; returns 4.
The stack becomes [5,7].
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>Calls to <code>FreqStack.push(int x)</code>&nbsp;will be such that <code>0 &lt;= x &lt;= 10^9</code>.</li>
	<li>It is guaranteed that <code>FreqStack.pop()</code> won&#39;t be called if the stack has zero elements.</li>
	<li>The total number of <code>FreqStack.push</code> calls will not exceed <code>10000</code> in a single test case.</li>
	<li>The total number of <code>FreqStack.pop</code>&nbsp;calls will not exceed <code>10000</code> in a single test case.</li>
	<li>The total number of <code>FreqStack.push</code> and <code>FreqStack.pop</code> calls will not exceed <code>150000</code> across all test cases.</li>
</ul>

<div>
<p>&nbsp;</p>
</div>


------

**题目：** 
<p>实现 <code>FreqStack</code>，模拟类似栈的数据结构的操作的一个类。</p>

<p><code>FreqStack</code>&nbsp;有两个函数：</p>

<ul>
	<li><code>push(int x)</code>，将整数&nbsp;<code>x</code>&nbsp;推入栈中。</li>
	<li><code>pop()</code>，它<strong>移除</strong>并返回栈中出现最频繁的元素。
	<ul>
		<li>如果最频繁的元素不只一个，则移除并返回最接近栈顶的元素。</li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>
[&quot;FreqStack&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;pop&quot;,&quot;pop&quot;,&quot;pop&quot;,&quot;pop&quot;],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
<strong>输出：</strong>[null,null,null,null,null,null,null,5,7,5,4]
<strong>解释：</strong>
执行六次 .push 操作后，栈自底向上为 [5,7,5,7,4,5]。然后：

pop() -&gt; 返回 5，因为 5 是出现频率最高的。
栈变成 [5,7,5,7,4]。

pop() -&gt; 返回 7，因为 5 和 7 都是频率最高的，但 7 最接近栈顶。
栈变成 [5,7,5,4]。

pop() -&gt; 返回 5 。
栈变成 [5,7,4]。

pop() -&gt; 返回 4 。
栈变成 [5,7]。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>对&nbsp;<code>FreqStack.push(int x)</code>&nbsp;的调用中&nbsp;<code>0 &lt;= x &lt;= 10^9</code>。</li>
	<li>如果栈的元素数目为零，则保证不会调用&nbsp; <code>FreqStack.pop()</code>。</li>
	<li>单个测试样例中，对&nbsp;<code>FreqStack.push</code>&nbsp;的总调用次数不会超过&nbsp;<code>10000</code>。</li>
	<li>单个测试样例中，对&nbsp;<code>FreqStack.pop</code>&nbsp;的总调用次数不会超过&nbsp;<code>10000</code>。</li>
	<li>所有测试样例中，对&nbsp;<code>FreqStack.push</code>&nbsp;和 <code>FreqStack.pop</code>&nbsp;的总调用次数不会超过&nbsp;<code>150000</code>。</li>
</ul>

<p>&nbsp;</p>

