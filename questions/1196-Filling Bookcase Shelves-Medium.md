#### 填充书架/Filling Bookcase Shelves
**难度：** 中等/Medium

**Question：** 

<p>We have a sequence of <code>books</code>: the <code>i</code>-th book has thickness <code>books[i][0]</code> and height <code>books[i][1]</code>.</p>

<p>We want to place these books <strong>in order</strong>&nbsp;onto bookcase shelves that have total width <code>shelf_width</code>.</p>

<p>We choose&nbsp;some of the books to place on this shelf (such that the sum of their thickness is <code>&lt;= shelf_width</code>), then build another level of shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down.&nbsp; We repeat this process until there are no more books to place.</p>

<p>Note again that at each step of the above&nbsp;process, <u>the order of the books we place is the same order as the given sequence of books</u>.&nbsp; For example, if we have an ordered list of 5&nbsp;books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.</p>

<p>Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/06/24/shelves.png" style="width: 250px; height: 370px;" />
<pre>
<strong>Input:</strong> books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
<strong>Output:</strong> 6
<strong>Explanation:</strong>
The sum of the heights of the 3 shelves are 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= books.length &lt;= 1000</code></li>
	<li><code>1 &lt;= books[i][0] &lt;= shelf_width &lt;= 1000</code></li>
	<li><code>1 &lt;= books[i][1] &lt;= 1000</code></li>
</ul>


------

**题目：** 
<p>附近的家居城促销，你买回了一直心仪的可调节书架，打算把自己的书都整理到新的书架上。</p>

<p>你把要摆放的书 <code>books</code>&nbsp;都整理好，叠成一摞：从上往下，第 <code>i</code>&nbsp;本书的厚度为 <code>books[i][0]</code>，高度为 <code>books[i][1]</code>。</p>

<p><strong>按顺序</strong>&nbsp;将这些书摆放到总宽度为&nbsp;<code>shelf_width</code> 的书架上。</p>

<p>先选几本书放在书架上（它们的厚度之和小于等于书架的宽度 <code>shelf_width</code>），然后再建一层书架。重复这个过程，直到把所有的书都放在书架上。</p>

<p>需要注意的是，在上述过程的每个步骤中，<strong>摆放书的顺序与你整理好的顺序相同</strong>。 例如，如果这里有 5 本书，那么可能的一种摆放情况是：第一和第二本书放在第一层书架上，第三本书放在第二层书架上，第四和第五本书放在最后一层书架上。</p>

<p>每一层所摆放的书的最大高度就是这一层书架的层高，书架整体的高度为各层高之和。</p>

<p>以这种方式布置书架，返回书架整体可能的最小高度。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/06/28/shelves.png" style="width: 150px;"></p>

<pre><strong>输入：</strong>books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
<strong>输出：</strong>6
<strong>解释：</strong>
3 层书架的高度和为 1 + 3 + 2 = 6 。
第 2 本书不必放在第一层书架上。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= books.length &lt;= 1000</code></li>
	<li><code>1 &lt;= books[i][0] &lt;= shelf_width &lt;= 1000</code></li>
	<li><code>1 &lt;= books[i][1] &lt;= 1000</code></li>
</ul>

