#### 受标签影响的最大值/Largest Values From Labels
**难度：** 中等/Medium

**Question：** 

<p>We have a set of items: the <code>i</code>-th item has value <code>values[i]</code> and label <code>labels[i]</code>.</p>

<p>Then, we choose&nbsp;a subset <code>S</code> of these items, such that:</p>

<ul>
	<li><code>|S| &lt;= num_wanted</code></li>
	<li>For every label <code>L</code>, the number of items in <code>S</code> with&nbsp;label <code>L</code> is <code>&lt;= use_limit</code>.</li>
</ul>

<p>Return the largest possible sum of the subset <code>S</code>.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>values = <span id="example-input-1-1">[5,4,3,2,1]</span>, labels = <span id="example-input-1-2">[1,1,2,2,3]</span>, <code>num_wanted </code>= <span id="example-input-1-3">3</span>, use_limit = <span id="example-input-1-4">1</span>
<strong>Output: </strong><span id="example-output-1">9</span>
<strong>Explanation: </strong>The subset chosen is the first, third, and fifth item.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>values = <span id="example-input-2-1">[5,4,3,2,1]</span>, labels = <span id="example-input-2-2">[1,3,3,3,2]</span>, <code>num_wanted </code>= <span id="example-input-2-3">3</span>, use_limit = <span id="example-input-2-4">2</span>
<strong>Output: </strong><span id="example-output-2">12</span>
<strong>Explanation: </strong>The subset chosen is the first, second, and third item.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>values = <span id="example-input-3-1">[9,8,8,7,6]</span>, labels = <span id="example-input-3-2">[0,0,0,1,1]</span>, <code>num_wanted </code>= <span id="example-input-3-3">3</span>, use_limit = <span id="example-input-3-4">1</span>
<strong>Output:</strong>&nbsp;16
<strong>Explanation: </strong>The subset chosen is the first and fourth item.
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>values = <span id="example-input-4-1">[9,8,8,7,6]</span>, labels = <span id="example-input-4-2">[0,0,0,1,1]</span>, <code>num_wanted </code>= <span id="example-input-4-3">3</span>, use_limit = <span id="example-input-4-4">2</span>
<strong>Output: </strong><span id="example-output-4">24</span>
<strong>Explanation: </strong>The subset chosen is the first, second, and fourth item.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= values.length == labels.length &lt;= 20000</code></li>
	<li><code>0 &lt;= values[i], labels[i]&nbsp;&lt;= 20000</code></li>
	<li><code>1 &lt;= num_wanted, use_limit&nbsp;&lt;= values.length</code></li>
</ol>
</div>
</div>
</div>
</div>

------

**题目：** 
<p>我们有一个项的集合，其中第&nbsp;<code>i</code>&nbsp;项的值为&nbsp;<code>values[i]</code>，标签为&nbsp;<code>labels[i]</code>。</p>

<p>我们从这些项中选出一个子集&nbsp;<code>S</code>，这样一来：</p>

<ul>
	<li><code>|S| &lt;= num_wanted</code></li>
	<li>对于任意的标签 <code>L</code>，子集 <code>S</code> 中标签为 <code>L</code>&nbsp;的项的数目总满足&nbsp;<code>&lt;= use_limit</code>。</li>
</ul>

<p>返回子集&nbsp;<code>S</code>&nbsp;的最大可能的&nbsp;<strong>和</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>values = [5,4,3,2,1], labels = [1,1,2,2,3], <code>num_wanted </code>= 3, use_limit = 1
<strong>输出：</strong>9
<strong>解释：</strong>选出的子集是第一项，第三项和第五项。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>values = [5,4,3,2,1], labels = [1,3,3,3,2], <code>num_wanted </code>= 3, use_limit = 2
<strong>输出：</strong>12
<strong>解释：</strong>选出的子集是第一项，第二项和第三项。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>values = [9,8,8,7,6], labels = [0,0,0,1,1], <code>num_wanted </code>= 3, use_limit = 1
<strong>输出：</strong>16
<strong>解释：</strong>选出的子集是第一项和第四项。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>values = [9,8,8,7,6], labels = [0,0,0,1,1], <code>num_wanted </code>= 3, use_limit = 2
<strong>输出：</strong>24
<strong>解释：</strong>选出的子集是第一项，第二项和第四项。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= values.length == labels.length &lt;= 20000</code></li>
	<li><code>0 &lt;= values[i], labels[i]&nbsp;&lt;= 20000</code></li>
	<li><code>1 &lt;= num_wanted, use_limit&nbsp;&lt;= values.length</code></li>
</ol>

