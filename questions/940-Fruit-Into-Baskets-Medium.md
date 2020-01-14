#### 水果成篮/Fruit Into Baskets
**难度：** 中等/Medium

**Question：** 

<p>In a row of trees, the <code>i</code>-th tree&nbsp;produces&nbsp;fruit with type&nbsp;<code>tree[i]</code>.</p>

<p>You <strong>start at any tree&nbsp;of your choice</strong>, then repeatedly perform the following steps:</p>

<ol>
	<li>Add one piece of fruit from this tree to your baskets.&nbsp; If you cannot, stop.</li>
	<li>Move to the next tree to the right of the current tree.&nbsp; If there is no tree to the right, stop.</li>
</ol>

<p>Note that you do not have any choice after the initial choice of starting tree:&nbsp;you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.</p>

<p>You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.</p>

<p>What is the total amount of fruit you can collect with this procedure?</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,1]</span>
<strong>Output: </strong><span id="example-output-1">3</span>
<strong><span>Explanation: </span></strong><span>We can collect [1,2,1].</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[0,1,2,2]</span>
<strong>Output: </strong><span id="example-output-2">3
</span><strong><span>Explanation: </span></strong><span>We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[1,2,3,2,2]</span>
<strong>Output: </strong><span id="example-output-3">4
</span><strong><span>Explanation: </span></strong><span>We can collect [2,3,2,2].</span>
<span>If we started at the first tree, we would only collect [1, 2].</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[3,3,3,1,2,1,1,2,3,3,4]</span>
<strong>Output: </strong>5<span id="example-output-4">
</span><strong><span>Explanation: </span></strong><span>We can collect [1,2,1,1,2].</span>
<span>If we started at the first tree or the eighth tree, we would only collect 4 fruits.</span>
</pre>

<p>&nbsp;</p>
</div>
</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= tree.length &lt;= 40000</code></li>
	<li><code>0 &lt;= tree[i] &lt; tree.length</code></li>
</ol>


------

**题目：** 
<p>在一排树中，第 <code>i</code> 棵树产生&nbsp;<code>tree[i]</code> 型的水果。<br>
你可以<strong>从你选择的任何树开始</strong>，然后重复执行以下步骤：</p>

<ol>
	<li>把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。</li>
	<li>移动到当前树右侧的下一棵树。如果右边没有树，就停下来。</li>
</ol>

<p>请注意，在选择一颗树后，你没有任何选择：你必须执行步骤 1，然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。</p>

<p>你有两个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。<br>
用这个程序你能收集的水果总量是多少？</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[1,2,1]
<strong>输出：</strong>3
<strong>解释：</strong>我们可以收集 [1,2,1]。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[0,1,2,2]
<strong>输出：</strong>3
<strong>解释：</strong>我们可以收集 [1,2,2].
如果我们从第一棵树开始，我们将只能收集到 [0, 1]。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[1,2,3,2,2]
<strong>输出：</strong>4
<strong>解释：</strong>我们可以收集 [2,3,2,2].
如果我们从第一棵树开始，我们将只能收集到 [1, 2]。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>[3,3,3,1,2,1,1,2,3,3,4]
<strong>输出：</strong>5
<strong>解释：</strong>我们可以收集 [1,2,1,1,2].
如果我们从第一棵树或第八棵树开始，我们将只能收集到 4 个水果。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= tree.length &lt;= 40000</code></li>
	<li><code>0 &lt;= tree[i] &lt; tree.length</code></li>
</ol>

