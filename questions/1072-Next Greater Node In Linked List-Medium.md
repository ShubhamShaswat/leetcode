#### 链表中的下一个更大节点/Next Greater Node In Linked List
**难度：** 中等/Medium

**Question：** 

<p>We are given a linked list with&nbsp;<code>head</code>&nbsp;as the first node.&nbsp; Let&#39;s number the&nbsp;nodes in the list: <code>node_1, node_2, node_3, ...</code> etc.</p>

<p>Each node may have a <em>next larger</em> <strong>value</strong>: for <code>node_i</code>,&nbsp;<code>next_larger(node_i)</code>&nbsp;is the <code>node_j.val</code> such that <code>j &gt; i</code>, <code>node_j.val &gt; node_i.val</code>, and <code>j</code> is the smallest possible choice.&nbsp; If such a <code>j</code>&nbsp;does not exist, the next larger value is <code>0</code>.</p>

<p>Return an array of integers&nbsp;<code>answer</code>, where <code>answer[i] = next_larger(node_{i+1})</code>.</p>

<p>Note that in the example <strong>inputs</strong>&nbsp;(not outputs) below, arrays such as <code>[2,1,5]</code>&nbsp;represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[2,1,5]</span>
<strong>Output: </strong><span id="example-output-1">[5,5,0]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[2,7,4,3,5]</span>
<strong>Output: </strong><span id="example-output-2">[7,0,5,5,0]</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[1,7,5,1,9,2,5,1]</span>
<strong>Output: </strong><span id="example-output-3">[7,9,9,9,0,5,0,0]</span>
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ol>
	<li><code><span>1 &lt;= node.val&nbsp;&lt;= 10^9</span></code><span>&nbsp;for each node in the linked list.</span></li>
	<li>The given list has length in the range <code>[0, 10000]</code>.</li>
</ol>
</div>
</div>
</div>

------

**题目：** 
<p>给出一个以头节点&nbsp;<code>head</code>&nbsp;作为第一个节点的链表。链表中的节点分别编号为：<code>node_1, node_2, node_3, ...</code> 。</p>

<p>每个节点都可能有下一个更大值（<em>next larger</em> <strong>value</strong>）：对于&nbsp;<code>node_i</code>，如果其&nbsp;<code>next_larger(node_i)</code>&nbsp;是&nbsp;<code>node_j.val</code>，那么就有&nbsp;<code>j &gt; i</code>&nbsp;且&nbsp;&nbsp;<code>node_j.val &gt; node_i.val</code>，而&nbsp;<code>j</code>&nbsp;是可能的选项中最小的那个。如果不存在这样的&nbsp;<code>j</code>，那么下一个更大值为&nbsp;<code>0</code>&nbsp;。</p>

<p>返回整数答案数组&nbsp;<code>answer</code>，其中&nbsp;<code>answer[i] = next_larger(node_{i+1})</code>&nbsp;。</p>

<p><strong><em>注意：</em></strong>在下面的示例中，诸如 <code>[2,1,5]</code> 这样的<strong>输入</strong>（不是输出）是链表的序列化表示，其头节点的值为&nbsp;2，第二个节点值为 1，第三个节点值为&nbsp;5 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[2,1,5]
<strong>输出：</strong>[5,5,0]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[2,7,4,3,5]
<strong>输出：</strong>[7,0,5,5,0]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[1,7,5,1,9,2,5,1]
<strong>输出：</strong>[7,9,9,9,0,5,0,0]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>对于链表中的每个节点，<code>1 &lt;= node.val&nbsp;&lt;= 10^9</code></li>
	<li>给定列表的长度在 <code>[0, 10000]</code>&nbsp;范围内</li>
</ol>

