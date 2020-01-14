#### 子数组中占绝大多数的元素/Online Majority Element In Subarray
**难度：** 困难/Hard

**Question：** 

<p>Implementing the class <code>MajorityChecker</code>, which has the following API:</p>

<ul>
	<li><code>MajorityChecker(int[] arr)</code> constructs an instance of MajorityChecker with the given array <code>arr</code>;</li>
	<li><code>int query(int left, int right, int threshold)</code>&nbsp;has arguments&nbsp;such that:
	<ul>
		<li><code>0 &lt;= left&nbsp;&lt;= right&nbsp;&lt; arr.length</code> representing a subarray of <code>arr</code>;</li>
		<li><code>2 * threshold &gt; right - left + 1</code>, ie. the threshold is always a strict majority of the length of&nbsp;the subarray</li>
	</ul>
	</li>
</ul>

<p>Each&nbsp;<code>query(...)</code> returns the element in <code>arr[left], arr[left+1], ..., arr[right]</code> that occurs at least <code>threshold</code> times, or <code>-1</code> if no such element exists.</p>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
majorityChecker.query(0,5,4); // returns 1
majorityChecker.query(0,3,3); // returns -1
majorityChecker.query(2,3,2); // returns 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;=&nbsp;20000</code></li>
	<li><code>1 &lt;= arr[i]&nbsp;&lt;=&nbsp;20000</code></li>
	<li>For each query, <code>0 &lt;= left &lt;= right &lt; len(arr)</code></li>
	<li>For each query, <code>2 * threshold &gt; right - left + 1</code></li>
	<li>The number of queries is at most <code>10000</code></li>
</ul>

------

**题目：** 
<p>实现一个&nbsp;<code>MajorityChecker</code>&nbsp;的类，它应该具有下述几个 API：</p>

<ul>
	<li><code>MajorityChecker(int[] arr)</code>&nbsp;会用给定的数组 <code>arr</code>&nbsp;来构造一个 <code>MajorityChecker</code> 的实例。</li>
	<li><code>int query(int left, int right, int threshold)</code>&nbsp;有这么几个参数：
	<ul>
		<li><code>0 &lt;= left&nbsp;&lt;= right&nbsp;&lt; arr.length</code> 表示数组&nbsp;<code>arr</code>&nbsp;的子数组的长度。</li>
		<li><code>2 * threshold &gt; right - left + 1</code>，也就是说阈值 <code>threshold</code>&nbsp;始终比子序列长度的一半还要大。</li>
	</ul>
	</li>
</ul>

<p>每次查询&nbsp;<code>query(...)</code>&nbsp;会返回在&nbsp;<code>arr[left], arr[left+1], ..., arr[right]</code>&nbsp;中至少出现阈值次数&nbsp;<code>threshold</code>&nbsp;的元素，如果不存在这样的元素，就返回&nbsp;<code>-1</code>。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
majorityChecker.query(0,5,4); // 返回 1
majorityChecker.query(0,3,3); // 返回 -1
majorityChecker.query(2,3,2); // 返回 2
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;=&nbsp;20000</code></li>
	<li><code>1 &lt;= arr[i]&nbsp;&lt;=&nbsp;20000</code></li>
	<li>对于每次查询，<code>0 &lt;= left &lt;= right &lt; len(arr)</code></li>
	<li>对于每次查询，<code>2 * threshold &gt; right - left + 1</code></li>
	<li>查询次数最多为 <code>10000</code></li>
</ul>

