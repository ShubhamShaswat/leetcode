#### Range 模块/Range Module
**难度：** 困难/Hard

**Question：** 

<p>A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner.</p>

<p><li><code>addRange(int left, int right)</code> Adds the half-open interval <code>[left, right)</code>, tracking every real number in that interval.  Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval <code>[left, right)</code> that are not already tracked.</li></p>

<p><li><code>queryRange(int left, int right)</code> Returns true if and only if every real number in the interval <code>[left, right)</code>
 is currently being tracked.</li></p>

<p><li><code>removeRange(int left, int right)</code> Stops tracking every real number currently being tracked in the interval <code>[left, right)</code>.</li></p>

<p><b>Example 1:</b><br />
<pre>
<b>addRange(10, 20)</b>: null
<b>removeRange(14, 16)</b>: null
<b>queryRange(10, 14)</b>: true (Every number in [10, 14) is being tracked)
<b>queryRange(13, 15)</b>: false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
<b>queryRange(16, 17)</b>: true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
</pre>
</p>

<p><b>Note:</b>
<li>A half open interval <code>[left, right)</code> denotes all real numbers <code>left <= x < right</code>.</li>

<li><code>0 < left < right < 10^9</code> in all calls to <code>addRange, queryRange, removeRange</code>.</li>
<li>The total number of calls to <code>addRange</code> in a single test case is at most <code>1000</code>.</li>
<li>The total number of calls to <code>queryRange</code> in a single test case is at most <code>5000</code>.</li>
<li>The total number of calls to <code>removeRange</code> in a single test case is at most <code>1000</code>.</li>
</p>

------

**题目：** 
<p>Range 模块是跟踪数字范围的模块。你的任务是以一种有效的方式设计和实现以下接口。</p>

<ul>
	<li><code>addRange(int left, int right)</code> 添加半开区间&nbsp;<code>[left, right)</code>，跟踪该区间中的每个实数。添加与当前跟踪的数字部分重叠的区间时，应当添加在区间&nbsp;<code>[left, right)</code>&nbsp;中尚未跟踪的任何数字到该区间中。</li>
	<li><code>queryRange(int left, int right)</code>&nbsp;只有在当前正在跟踪区间&nbsp;<code>[left, right)</code>&nbsp;中的每一个实数时，才返回 true。</li>
	<li><code>removeRange(int left, int right)</code>&nbsp;停止跟踪区间&nbsp;<code>[left, right)</code>&nbsp;中当前正在跟踪的每个实数。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>addRange(10, 20)</strong>: null
<strong>removeRange(14, 16)</strong>: null
<strong>queryRange(10, 14)</strong>: true （区间 [10, 14) 中的每个数都正在被跟踪）
<strong>queryRange(13, 15)</strong>: false （未跟踪区间 [13, 15) 中像 14, 14.03, 14.17 这样的数字）
<strong>queryRange(16, 17)</strong>: true （尽管执行了删除操作，区间 [16, 17) 中的数字 16 仍然会被跟踪）
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>半开区间&nbsp;<code>[left, right)</code>&nbsp;表示所有满足&nbsp;<code>left &lt;= x &lt; right</code>&nbsp;的实数。</li>
	<li>对&nbsp;<code>addRange, queryRange, removeRange</code>&nbsp;的所有调用中&nbsp;<code>0 &lt; left &lt; right &lt; 10^9</code>。</li>
	<li>在单个测试用例中，对&nbsp;<code>addRange</code>&nbsp;的调用总数不超过&nbsp;<code>1000</code>&nbsp;次。</li>
	<li>在单个测试用例中，对&nbsp; <code>queryRange</code> 的调用总数不超过 <code>5000</code> 次。</li>
	<li>在单个测试用例中，对 <code>removeRange</code> 的调用总数不超过&nbsp;<code>1000</code>&nbsp;次。</li>
</ul>

<p>&nbsp;</p>

