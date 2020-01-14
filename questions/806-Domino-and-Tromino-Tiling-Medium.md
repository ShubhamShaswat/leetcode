#### 多米诺和托米诺平铺/Domino and Tromino Tiling
**难度：** 中等/Medium

**Question：** 

<p>We have two types of tiles: a 2x1 domino shape, and an &quot;L&quot; tromino shape. These shapes may be rotated.</p>

<pre>
XX  &lt;- domino

XX  &lt;- &quot;L&quot; tromino
X
</pre>

<p>Given N, how many ways are there to tile a 2 x N board? <strong>Return your answer modulo 10^9 + 7</strong>.</p>

<p>(In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.)</p>


<pre>
<strong>Example:</strong>
<strong>Input:</strong> 3
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
The five different ways are listed below, different letters indicates different tiles:
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>N&nbsp; will be in range <code>[1, 1000]</code>.</li>
</ul>

<p>&nbsp;</p>


------

**题目：** 
<p>有两种形状的瓷砖：一种是&nbsp;2x1 的多米诺形，另一种是形如&nbsp;&quot;L&quot; 的托米诺形。两种形状都可以旋转。</p>

<pre>
XX  &lt;- 多米诺

XX  &lt;- &quot;L&quot; 托米诺
X
</pre>

<p>给定&nbsp;N 的值，有多少种方法可以平铺&nbsp;2 x N 的面板？<strong>返回值 mod 10^9 + 7</strong>。</p>

<p>（平铺指的是每个正方形都必须有瓷砖覆盖。两个平铺不同，当且仅当面板上有四个方向上的相邻单元中的两个，使得恰好有一个平铺有一个瓷砖占据两个正方形。）</p>

<pre>
<strong>示例:</strong>
<strong>输入:</strong> 3
<strong>输出:</strong> 5
<strong>解释:</strong> 
下面列出了五种不同的方法，不同字母代表不同瓷砖：
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>N&nbsp; 的范围是&nbsp;<code>[1, 1000]</code></li>
</ul>

<p>&nbsp;</p>

