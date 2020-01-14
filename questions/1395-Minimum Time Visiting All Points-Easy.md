#### 访问所有点的最小时间/Minimum Time Visiting All Points
**难度：** 简单/Easy

**Question：** 

<p>On a plane there are <code>n</code> points with integer coordinates <code>points[i] = [xi, yi]</code>. Your task is to find the minimum time in seconds to visit all points.</p>

<p>You can move according to the next rules:</p>

<ul>
	<li>In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).</li>
	<li>You have to visit the points in the same order as they appear in the array.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/11/14/1626_example_1.PNG" style="width: 500px; height: 428px;" />
<pre>
<strong>Input:</strong> points = [[1,1],[3,4],[-1,0]]
<strong>Output:</strong> 7
<strong>Explanation: </strong>One optimal path is <strong>[1,1]</strong> -&gt; [2,2] -&gt; [3,3] -&gt; <strong>[3,4] </strong>-&gt; [2,3] -&gt; [1,2] -&gt; [0,1] -&gt; <strong>[-1,0]</strong>   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> points = [[3,2],[-2,2]]
<strong>Output:</strong> 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>points.length == n</code></li>
	<li><code>1 &lt;= n&nbsp;&lt;= 100</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-1000&nbsp;&lt;= points[i][0], points[i][1]&nbsp;&lt;= 1000</code></li>
</ul>


------

**题目：** 
<p>平面上有&nbsp;<code>n</code>&nbsp;个点，点的位置用整数坐标表示&nbsp;<code>points[i] = [xi, yi]</code>。请你计算访问所有这些点需要的最小时间（以秒为单位）。</p>

<p>你可以按照下面的规则在平面上移动：</p>

<ul>
	<li>每一秒沿水平或者竖直方向移动一个单位长度，或者跨过对角线（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。</li>
	<li>必须按照数组中出现的顺序来访问这些点。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/24/1626_example_1.png" style="height: 428px; width: 500px;"></p>

<pre><strong>输入：</strong>points = [[1,1],[3,4],[-1,0]]
<strong>输出：</strong>7
<strong>解释：</strong>一条最佳的访问路径是： <strong>[1,1]</strong> -&gt; [2,2] -&gt; [3,3] -&gt; <strong>[3,4] </strong>-&gt; [2,3] -&gt; [1,2] -&gt; [0,1] -&gt; <strong>[-1,0]</strong>   
从 [1,1] 到 [3,4] 需要 3 秒 
从 [3,4] 到 [-1,0] 需要 4 秒
一共需要 7 秒</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>points = [[3,2],[-2,2]]
<strong>输出：</strong>5
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>points.length == n</code></li>
	<li><code>1 &lt;= n&nbsp;&lt;= 100</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-1000&nbsp;&lt;= points[i][0], points[i][1]&nbsp;&lt;= 1000</code></li>
</ul>

