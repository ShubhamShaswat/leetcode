#### 不邻接植花/Flower Planting With No Adjacent
**难度：** 简单/Easy

**Question：** 

<p>You have <code>N</code> gardens, labelled <code>1</code> to <code>N</code>.&nbsp; In each garden, you want to plant one of 4 types of flowers.</p>

<p><code>paths[i] = [x, y]</code> describes the existence of a bidirectional path from garden <code>x</code> to garden <code>y</code>.</p>

<p>Also, there is no garden that has more than 3 paths coming into or leaving it.</p>

<p>Your task is to choose a flower type for each garden such that,&nbsp;for any two gardens connected by a path, they have different types of flowers.</p>

<p>Return <strong>any</strong> such a choice as an array <code>answer</code>, where&nbsp;<code>answer[i]</code> is the type of flower&nbsp;planted in the <code>(i+1)</code>-th garden.&nbsp; The flower types are denoted&nbsp;<font face="monospace">1</font>, <font face="monospace">2</font>, <font face="monospace">3</font>, or <font face="monospace">4</font>.&nbsp; It is guaranteed an answer exists.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-1-1">3</span>, paths = <span id="example-input-1-2">[[1,2],[2,3],[3,1]]</span>
<strong>Output: </strong><span id="example-output-1">[1,2,3]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-2-1">4</span>, paths = <span id="example-input-2-2">[[1,2],[3,4]]</span>
<strong>Output: </strong><span id="example-output-2">[1,2,1,2]</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-3-1">4</span>, paths = <span id="example-input-3-2">[[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]</span>
<strong>Output: </strong><span id="example-output-3">[1,2,3,4]</span>
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ul>
	<li><code><span>1 &lt;= N &lt;= 10000</span></code></li>
	<li><code><span>0 &lt;= paths.size &lt;= 20000</span></code></li>
	<li>No garden has 4 or more paths coming into or leaving it.</li>
	<li>It is guaranteed an answer exists.</li>
</ul>
</div>
</div>
</div>

------

**题目：** 
<p>有&nbsp;<code>N</code>&nbsp;个花园，按从&nbsp;<code>1</code>&nbsp;到&nbsp;<code>N</code>&nbsp;标记。在每个花园中，你打算种下四种花之一。</p>

<p><code>paths[i] = [x, y]</code>&nbsp;描述了花园&nbsp;<code>x</code> 到花园&nbsp;<code>y</code>&nbsp;的双向路径。</p>

<p>另外，没有花园有 3 条以上的路径可以进入或者离开。</p>

<p>你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。</p>

<p>以数组形式返回选择的方案作为答案&nbsp;<code>answer</code>，其中&nbsp;<code>answer[i]</code>&nbsp;为在第&nbsp;<code>(i+1)</code>&nbsp;个花园中种植的花的种类。花的种类用 &nbsp;1, 2, 3,&nbsp;4 表示。保证存在答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>N = 3, paths = [[1,2],[2,3],[3,1]]
<strong>输出：</strong>[1,2,3]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>N = 4, paths = [[1,2],[3,4]]
<strong>输出：</strong>[1,2,1,2]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
<strong>输出：</strong>[1,2,3,4]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= N &lt;= 10000</code></li>
	<li><code>0 &lt;= paths.size &lt;= 20000</code></li>
	<li>不存在花园有 4 条或者更多路径可以进入或离开。</li>
	<li>保证存在答案。</li>
</ul>

