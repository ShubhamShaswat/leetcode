#### 不浪费原料的汉堡制作方案/Number of Burgers with No Waste of Ingredients
**难度：** 中等/Medium

**Question：** 

<p>Given two integers <code>tomatoSlices</code>&nbsp;and <code>cheeseSlices</code>. The ingredients of different burgers are as follows:</p>

<ul>
	<li><strong>Jumbo Burger:</strong> 4 tomato slices&nbsp;and 1 cheese slice.</li>
	<li><strong>Small Burger:</strong> 2 Tomato slices&nbsp;and 1 cheese slice.</li>
</ul>

<p>Return <code>[total_jumbo, total_small]</code> so that the number of remaining <code>tomatoSlices</code>&nbsp;equal to 0 and the number of remaining <code>cheeseSlices</code> equal to 0. If it is not possible to make the remaining <code>tomatoSlices</code>&nbsp;and <code>cheeseSlices</code> equal to 0 return <code>[]</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> tomatoSlices = 16, cheeseSlices = 7
<strong>Output:</strong> [1,6]
<strong>Explantion:</strong> To make one jumbo burger and 6 small burgers we need 4*1 + 2*6 = 16 tomato and 1 + 6 = 7 cheese. There will be no remaining ingredients.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> tomatoSlices = 17, cheeseSlices = 4
<strong>Output:</strong> []
<strong>Explantion:</strong> There will be no way to use all ingredients to make small and jumbo burgers.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> tomatoSlices = 4, cheeseSlices = 17
<strong>Output:</strong> []
<strong>Explantion:</strong> Making 1 jumbo burger there will be 16 cheese remaining and making 2 small burgers there will be 15 cheese remaining.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> tomatoSlices = 0, cheeseSlices = 0
<strong>Output:</strong> [0,0]
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> tomatoSlices = 2, cheeseSlices = 1
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= tomatoSlices &lt;= 10^7</code></li>
	<li><code>0 &lt;= cheeseSlices &lt;= 10^7</code></li>
</ul>

------

**题目：** 
<p>圣诞活动预热开始啦，汉堡店推出了全新的汉堡套餐。为了避免浪费原料，请你帮他们制定合适的制作计划。</p>

<p>给你两个整数&nbsp;<code>tomatoSlices</code>&nbsp;和&nbsp;<code>cheeseSlices</code>，分别表示番茄片和奶酪片的数目。不同汉堡的原料搭配如下：</p>

<ul>
	<li><strong>巨无霸汉堡：</strong>4 片番茄和 1 片奶酪</li>
	<li><strong>小皇堡：</strong>2 片番茄和&nbsp;1 片奶酪</li>
</ul>

<p>请你以&nbsp;<code>[total_jumbo, total_small]</code>（[巨无霸汉堡总数，小皇堡总数]）的格式返回恰当的制作方案，使得剩下的番茄片&nbsp;<code>tomatoSlices</code>&nbsp;和奶酪片&nbsp;<code>cheeseSlices</code>&nbsp;的数量都是&nbsp;<code>0</code>。</p>

<p>如果无法使剩下的番茄片&nbsp;<code>tomatoSlices</code>&nbsp;和奶酪片&nbsp;<code>cheeseSlices</code>&nbsp;的数量为&nbsp;<code>0</code>，就请返回&nbsp;<code>[]</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>tomatoSlices = 16, cheeseSlices = 7
<strong>输出：</strong>[1,6]
<strong>解释：</strong>制作 1 个巨无霸汉堡和 6 个小皇堡需要 4*1 + 2*6 = 16 片番茄和 1 + 6 = 7 片奶酪。不会剩下原料。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>tomatoSlices = 17, cheeseSlices = 4
<strong>输出：</strong>[]
<strong>解释：</strong>只制作小皇堡和巨无霸汉堡无法用光全部原料。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>tomatoSlices = 4, cheeseSlices = 17
<strong>输出：</strong>[]
<strong>解释：</strong>制作 1 个巨无霸汉堡会剩下 16 片奶酪，制作 2 个小皇堡会剩下 15 片奶酪。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>tomatoSlices = 0, cheeseSlices = 0
<strong>输出：</strong>[0,0]
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>tomatoSlices = 2, cheeseSlices = 1
<strong>输出：</strong>[0,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= tomatoSlices &lt;= 10^7</code></li>
	<li><code>0 &lt;= cheeseSlices &lt;= 10^7</code></li>
</ul>

