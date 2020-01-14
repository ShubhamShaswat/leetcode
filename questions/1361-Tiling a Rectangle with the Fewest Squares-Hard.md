#### 铺瓷砖/Tiling a Rectangle with the Fewest Squares
**难度：** 困难/Hard

**Question：** 

<p>Given a rectangle of size&nbsp;<code>n</code>&nbsp;x <code><font face="monospace">m</font></code>, find the minimum number of integer-sided squares that tile the rectangle.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/10/17/sample_11_1592.png" style="width: 154px; height: 106px;" /></p>

<pre>
<strong>Input:</strong> n = 2, m = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> <code>3</code> squares are necessary to cover the rectangle.
<code>2</code> (squares of <code>1x1</code>)
<code>1</code> (square of <code>2x2</code>)</pre>

<p><strong>Example 2:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/10/17/sample_22_1592.png" style="width: 224px; height: 126px;" /></p>

<pre>
<strong>Input:</strong> n = 5, m = 8
<strong>Output:</strong> 5
</pre>

<p><strong>Example 3:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/10/17/sample_33_1592.png" style="width: 224px; height: 189px;" /></p>

<pre>
<strong>Input:</strong> n = 11, m = 13
<strong>Output:</strong> 6
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 13</code></li>
	<li><code>1 &lt;= m&nbsp;&lt;=&nbsp;13</code></li>
</ul>


------

**题目：** 
<p>你是一位施工队的工长，根据设计师的要求准备为一套设计风格独特的房子进行室内装修。</p>

<p>房子的客厅大小为&nbsp;<code>n</code>&nbsp;x <code>m</code>，为保持极简的风格，需要使用尽可能少的 <strong>正方形</strong> 瓷砖来铺盖地面。</p>

<p>假设正方形瓷砖的规格不限，边长都是整数。</p>

<p>请你帮设计师计算一下，最少需要用到多少块方形瓷砖？</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/25/sample_11_1592.png" style="height: 106px; width: 154px;"></p>

<pre><strong>输入：</strong>n = 2, m = 3
<strong>输出：</strong>3
<code><strong>解释：</strong>3</code> 块地砖就可以铺满卧室。
<code>     2</code> 块 <code>1x1 地砖</code>
<code>     1</code> 块 <code>2x2 地砖</code></pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/25/sample_22_1592.png" style="height: 126px; width: 224px;"></p>

<pre><strong>输入：</strong>n = 5, m = 8
<strong>输出：</strong>5
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/25/sample_33_1592.png" style="height: 189px; width: 224px;"></p>

<pre><strong>输入：</strong>n = 11, m = 13
<strong>输出：</strong>6
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 13</code></li>
	<li><code>1 &lt;= m&nbsp;&lt;=&nbsp;13</code></li>
</ul>

