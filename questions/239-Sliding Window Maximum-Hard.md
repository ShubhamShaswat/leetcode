#### 滑动窗口最大值/Sliding Window Maximum
**难度：** 困难/Hard

**Question：** 

<p>Given an array <em>nums</em>, there is a sliding window of size <em>k</em> which is moving from the very left of the array to the very right. You can only see the <em>k</em> numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> <em>nums</em> = <code>[1,3,-1,-3,5,3,6,7]</code>, and <em>k</em> = 3
<strong>Output: </strong><code>[3,3,5,5,6,7] 
<strong>Explanation: 
</strong></code>
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       <strong>3</strong>
 1 [3  -1  -3] 5  3  6  7       <strong>3</strong>
 1  3 [-1  -3  5] 3  6  7      <strong> 5</strong>
 1  3  -1 [-3  5  3] 6  7       <strong>5</strong>
 1  3  -1  -3 [5  3  6] 7       <strong>6</strong>
 1  3  -1  -3  5 [3  6  7]      <strong>7</strong>
</pre>

<p><strong>Note: </strong><br />
You may assume <em>k</em> is always valid, 1 &le; k &le; input array&#39;s size for non-empty array.</p>

<p><strong>Follow up:</strong><br />
Could you solve it in linear time?</p>

------

**题目：** 
<p>给定一个数组 <em>nums</em>，有一个大小为&nbsp;<em>k&nbsp;</em>的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 <em>k</em>&nbsp;个数字。滑动窗口每次只向右移动一位。</p>

<p>返回滑动窗口中的最大值。</p>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> <em>nums</em> = <code>[1,3,-1,-3,5,3,6,7]</code>, 和 <em>k</em> = 3
<strong>输出: </strong><code>[3,3,5,5,6,7] 
<strong>解释: 
</strong></code>
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<p>你可以假设 <em>k </em>总是有效的，在输入数组不为空的情况下，1 &le; k &le;&nbsp;输入数组的大小。</p>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<p>你能在线性时间复杂度内解决此题吗？</p>

