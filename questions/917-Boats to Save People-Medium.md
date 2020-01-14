#### 救生艇/Boats to Save People
**难度：** 中等/Medium

**Question：** 

<p>The <code>i</code>-th person has weight <code>people[i]</code>, and each boat can carry a maximum weight of <code>limit</code>.</p>

<p>Each boat carries at most 2 people at the same time, provided the sum of the&nbsp;weight of those people is at most <code>limit</code>.</p>

<p>Return the minimum number of boats to carry every given person.&nbsp; (It is guaranteed each person can be carried by a boat.)</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>people = <span id="example-input-1-1">[1,2]</span>, limit = <span id="example-input-1-2">3</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong>1 boat (1, 2)
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>people = <span id="example-input-2-1">[3,2,2,1]</span>, limit = <span id="example-input-2-2">3</span>
<strong>Output: </strong><span id="example-output-2">3</span>
<strong>Explanation</strong>: 3 boats (1, 2), (2) and (3)
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>people = <span id="example-input-3-1">[3,5,3,4]</span>, limit = <span id="example-input-3-2">5</span>
<strong>Output: </strong><span id="example-output-3">4</span>
<strong>Explanation</strong>: 4 boats (3), (3), (4), (5)</pre>

<p><strong>Note</strong>:</p>

<ul>
	<li><code>1 &lt;=&nbsp;people.length &lt;= 50000</code></li>
	<li><code>1 &lt;= people[i] &lt;=&nbsp;limit &lt;= 30000</code></li>
</ul>
</div>
</div>
</div>


------

**题目：** 
<p>第&nbsp;<code>i</code>&nbsp;个人的体重为&nbsp;<code>people[i]</code>，每艘船可以承载的最大重量为&nbsp;<code>limit</code>。</p>

<p>每艘船最多可同时载两人，但条件是这些人的重量之和最多为&nbsp;<code>limit</code>。</p>

<p>返回载到每一个人所需的最小船数。(保证每个人都能被船载)。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>people = [1,2], limit = 3
<strong>输出：</strong>1
<strong>解释：</strong>1 艘船载 (1, 2)
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>people = [3,2,2,1], limit = 3
<strong>输出：</strong>3
<strong>解释：</strong>3 艘船分别载 (1, 2), (2) 和 (3)
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>people = [3,5,3,4], limit = 5
<strong>输出：</strong>4
<strong>解释：</strong>4 艘船分别载 (3), (3), (4), (5)</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;people.length &lt;= 50000</code></li>
	<li><code>1 &lt;= people[i] &lt;=&nbsp;limit &lt;= 30000</code></li>
</ul>

