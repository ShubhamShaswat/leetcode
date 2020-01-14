#### 出现次数最多的子树元素和/Most Frequent Subtree Sum
**难度：** 中等/Medium

**Question：** 

<p>
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.
</p>

<p><b>Examples 1</b><br>
Input:
<pre>
  5
 /  \
2   -3
</pre>
return [2, -3, 4], since all the values happen only once, return all of them in any order.
</p>

<p><b>Examples 2</b><br>
Input:
<pre>
  5
 /  \
2   -5
</pre>
return [2], since 2 happens twice, however -5 only occur once.
</p>

<p><b>Note:</b>
You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
</p>

------

**题目：** 
<p>给出二叉树的根，找出出现次数最多的子树元素和。一个结点的子树元素和定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。然后求出出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的元素（不限顺序）。</p>

<p>&nbsp;</p>

<p><strong>示例 1</strong><br>
输入:</p>

<pre>  5
 /  \
2   -3
</pre>

<p>返回&nbsp;[2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。</p>

<p><strong>示例&nbsp;2</strong><br>
输入:</p>

<pre>  5
 /  \
2   -5
</pre>

<p>返回&nbsp;[2]，只有 2 出现两次，-5 只出现 1 次。</p>

<p>&nbsp;</p>

<p><strong>提示：</strong>&nbsp;假设任意子树元素和均可以用 32 位有符号整数表示。</p>

