#### 奇数值单元格的数目/Cells with Odd Values in a Matrix
**难度：** 简单/Easy

**Question：** 

<p>Given&nbsp;<code>n</code>&nbsp;and&nbsp;<code>m</code>&nbsp;which are the dimensions of a matrix initialized by zeros and given an array <code>indices</code>&nbsp;where <code>indices[i] = [ri, ci]</code>. For each pair of <code>[ri, ci]</code>&nbsp;you have to increment all cells in row <code>ri</code> and column <code>ci</code>&nbsp;by 1.</p>

<p>Return <em>the number of cells with odd values</em> in the matrix after applying the increment to all <code>indices</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/10/30/e1.png" style="width: 600px; height: 118px;" />
<pre>
<strong>Input:</strong> n = 2, m = 3, indices = [[0,1],[1,1]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/10/30/e2.png" style="width: 600px; height: 150px;" />
<pre>
<strong>Input:</strong> n = 2, m = 2, indices = [[1,1],[0,0]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 50</code></li>
	<li><code>1 &lt;= m &lt;= 50</code></li>
	<li><code>1 &lt;= indices.length &lt;= 100</code></li>
	<li><code>0 &lt;= indices[i][0] &lt;&nbsp;n</code></li>
	<li><code>0 &lt;= indices[i][1] &lt;&nbsp;m</code></li>
</ul>


------

**题目：** 
<p>给你一个&nbsp;<code>n</code>&nbsp;行&nbsp;<code>m</code>&nbsp;列的矩阵，最开始的时候，每个单元格中的值都是 <code>0</code>。</p>

<p>另有一个索引数组&nbsp;<code>indices</code>，<code>indices[i] = [ri, ci]</code>&nbsp;中的&nbsp;<code>ri</code> 和 <code>ci</code> 分别表示指定的行和列（从 <code>0</code> 开始编号）。</p>

<p>你需要将每对&nbsp;<code>[ri, ci]</code>&nbsp;指定的行和列上的所有单元格的值加 <code>1</code>。</p>

<p>请你在执行完所有&nbsp;<code>indices</code>&nbsp;指定的增量操作后，返回矩阵中 「奇数值单元格」 的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/06/e1.png" style="height: 118px; width: 600px;"></p>

<pre><strong>输入：</strong>n = 2, m = 3, indices = [[0,1],[1,1]]
<strong>输出：</strong>6
<strong>解释：</strong>最开始的矩阵是 [[0,0,0],[0,0,0]]。
第一次增量操作后得到 [[1,2,1],[0,1,0]]。
最后的矩阵是 [[1,3,1],[1,3,1]]，里面有 6 个奇数。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/06/e2.png" style="height: 150px; width: 600px;"></p>

<pre><strong>输入：</strong>n = 2, m = 2, indices = [[1,1],[0,0]]
<strong>输出：</strong>0
<strong>解释：</strong>最后的矩阵是 [[2,2],[2,2]]，里面没有奇数。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 50</code></li>
	<li><code>1 &lt;= m &lt;= 50</code></li>
	<li><code>1 &lt;= indices.length &lt;= 100</code></li>
	<li><code>0 &lt;= indices[i][0] &lt;&nbsp;n</code></li>
	<li><code>0 &lt;= indices[i][1] &lt;&nbsp;m</code></li>
</ul>

