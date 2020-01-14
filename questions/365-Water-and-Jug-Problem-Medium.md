#### 水壶问题/Water and Jug Problem
**难度：** 中等/Medium

**Question：** 

<p>You are given two jugs with capacities <i>x</i> and <i>y</i> litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly <i>z</i> litres using these two jugs.</p>

<p>If <i>z</i> liters of water is measurable, you must have <i>z</i> liters of water contained within <b>one or both buckets</b> by the end.</p>

<p>Operations allowed:</p>

<ul>
	<li>Fill any of the jugs completely with water.</li>
	<li>Empty any of the jugs.</li>
	<li>Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.</li>
</ul>

<p><b>Example 1:</b> (From the famous <a href="https://www.youtube.com/watch?v=BVtQNK_ZUJg" target="_blank"><i>&quot;Die Hard&quot;</i> example</a>)</p>

<pre>
Input: x = 3, y = 5, z = 4
Output: True
</pre>

<p><b>Example 2:</b></p>

<pre>
Input: x = 2, y = 6, z = 5
Output: False
</pre>

------

**题目：** 
<p>有两个容量分别为&nbsp;<em>x</em>升 和<em> y</em>升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好&nbsp;<em>z</em>升 的水？</p>

<p>如果可以，最后请用以上水壶中的一或两个来盛放取得的&nbsp;<em>z升&nbsp;</em>水。</p>

<p>你允许：</p>

<ul>
	<li>装满任意一个水壶</li>
	<li>清空任意一个水壶</li>
	<li>从一个水壶向另外一个水壶倒水，直到装满或者倒空</li>
</ul>

<p><strong>示例 1:</strong> (From the famous <a href="https://www.youtube.com/watch?v=BVtQNK_ZUJg"><em>&quot;Die Hard&quot;</em> example</a>)</p>

<pre>输入: x = 3, y = 5, z = 4
输出: True
</pre>

<p><strong>示例 2:</strong></p>

<pre>输入: x = 2, y = 6, z = 5
输出: False
</pre>

