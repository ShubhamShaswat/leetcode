#### 查找集群内的「关键连接」/Critical Connections in a Network
**难度：** 困难/Hard

**Question：** 

<p>There are&nbsp;<code>n</code> servers numbered from&nbsp;<code>0</code>&nbsp;to&nbsp;<code>n-1</code> connected by&nbsp;undirected server-to-server <code>connections</code> forming a network where <code>connections[i] = [a, b]</code>&nbsp;represents a connection between servers <code>a</code>&nbsp;and <code>b</code>. Any server can reach any other server directly or indirectly through the network.</p>

<p>A <em>critical connection</em>&nbsp;is a connection that, if removed, will make some server unable to reach some other server.</p>

<p>Return all critical connections in the network in any order.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/03/1537_ex1_2.png" style="width: 198px; height: 248px;" /></strong></p>

<pre>
<strong>Input:</strong> n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
<strong>Output:</strong> [[1,3]]
<strong>Explanation:</strong> [[3,1]] is also accepted.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10^5</code></li>
	<li><code>n-1 &lt;= connections.length &lt;= 10^5</code></li>
	<li><code>connections[i][0] != connections[i][1]</code></li>
	<li>There are no repeated connections.</li>
</ul>


------

**题目：** 
<p>力扣数据中心有&nbsp;<code>n</code>&nbsp;台服务器，分别按从&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n-1</code>&nbsp;的方式进行了编号。</p>

<p>它们之间以「服务器到服务器」点对点的形式相互连接组成了一个内部集群，其中连接&nbsp;<code>connections</code> 是无向的。</p>

<p>从形式上讲，<code>connections[i] = [a, b]</code>&nbsp;表示服务器 <code>a</code>&nbsp;和 <code>b</code>&nbsp;之间形成连接。任何服务器都可以直接或者间接地通过网络到达任何其他服务器。</p>

<p>「关键连接」是在该集群中的重要连接，也就是说，假如我们将它移除，便会导致某些服务器无法访问其他服务器。</p>

<p>请你以任意顺序返回该集群内的所有 「关键连接」。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/original_images/critical-connections-in-a-network.png" style="width: 150px;"></strong></p>

<pre><strong>输入：</strong>n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
<strong>输出：</strong>[[1,3]]
<strong>解释：</strong>[[3,1]] 也是正确的。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10^5</code></li>
	<li><code>n-1 &lt;= connections.length &lt;= 10^5</code></li>
	<li><code>connections[i][0] != connections[i][1]</code></li>
	<li>不存在重复的连接</li>
</ul>

