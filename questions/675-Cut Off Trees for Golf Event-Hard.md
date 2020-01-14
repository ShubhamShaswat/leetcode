#### 为高尔夫比赛砍树/Cut Off Trees for Golf Event
**难度：** 困难/Hard

**Question：** 

<p>You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:</p>

<ol>
	<li><code>0</code> represents the <code>obstacle</code> can&#39;t be reached.</li>
	<li><code>1</code> represents the <code>ground</code> can be walked through.</li>
	<li><code>The place with number bigger than 1</code> represents a <code>tree</code> can be walked through, and this positive number represents the tree&#39;s height.</li>
</ol>

<p>&nbsp;</p>

<p>You are asked to cut off <b>all</b> the trees in this forest in the order of tree&#39;s height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).</p>

<p>You will start from the point (0, 0) and you should output the minimum steps <b>you need to walk</b> to cut off all the trees. If you can&#39;t cut off all the trees, output -1 in that situation.</p>

<p>You are guaranteed that no two <code>trees</code> have the same height and there is at least one tree needs to be cut off.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
<b>Output:</b> 6
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
<b>Output:</b> -1
</pre>

<p>&nbsp;</p>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
<b>Output:</b> 6
<b>Explanation:</b> You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
</pre>

<p>&nbsp;</p>

<p><b>Hint</b>: size of the given matrix will not exceed 50x50.</p>


------

**题目：** 
<p>你被请来给一个要举办高尔夫比赛的树林砍树. 树林由一个非负的二维数组表示， 在这个数组中：</p>

<ol>
	<li><code>0</code> 表示障碍，无法触碰到.</li>
	<li><code>1</code>&nbsp;表示可以行走的地面.</li>
	<li><code>比1大的数</code>&nbsp;表示一颗允许走过的树的高度.</li>
</ol>

<p>你被要求按照树的高度从低向高砍掉所有的树，每砍过一颗树，树的高度变为1。</p>

<p>你将从（0，0）点开始工作，你应该返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 -1 。</p>

<p>可以保证的是，没有两棵树的高度是相同的，并且至少有一颗树需要你砍。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong> 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
<strong>输出:</strong> 6
</pre>

<p>&nbsp;</p>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
<strong>输出:</strong> -1
</pre>

<p>&nbsp;</p>

<p><strong>示例&nbsp;3:</strong></p>

<pre>
<strong>输入:</strong> 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
<strong>输出:</strong> 6

<strong>解释:</strong> (0,0) 位置的树，你可以直接砍去，不用算步数
</pre>

<p>&nbsp;</p>

<p><strong>提示</strong>: 矩阵大小不会超过 50x50 。</p>

