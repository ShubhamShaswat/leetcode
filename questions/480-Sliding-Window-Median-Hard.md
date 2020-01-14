#### 滑动窗口中位数/Sliding Window Median
**难度：** 困难/Hard

**Question：** 

<p>Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.</p>
Examples: <br />
<p><code>[2,3,4]</code> , the median is <code>3</code></p>
<p><code>[2,3]</code>, the median is <code>(2 + 3) / 2 = 2.5</code> </p>

<p>Given an array <i>nums</i>, there is a sliding window of size <i>k</i> which is moving from the very left of the array to the very right. You can only see the <i>k</i> numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.</p>

<p>For example,<br>
Given <i>nums</i> = <code>[1,3,-1,-3,5,3,6,7]</code>, and <i>k</i> = 3.</p>

<pre>
Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
</pre>

<p>Therefore, return the median sliding window as <code>[1,-1,-1,3,5,6]</code>.</p>

<p><b>Note: </b><br>
You may assume <code>k</code> is always valid, ie: <code>k</code> is always smaller than input array's size for non-empty array.</p>

------

**题目：** 
<p>中位数是有序序列最中间的那个数。如果序列的大小是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。</p>

<p>例如：</p>

<p><code>[2,3,4]</code>，中位数是&nbsp;<code>3</code></p>

<p><code>[2,3]</code>，中位数是 <code>(2 + 3) / 2 = 2.5</code></p>

<p>给出一个数组 nums，有一个大小为 <em>k</em> 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口移动 1 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。</p>

<p>例如：</p>

<p>给出&nbsp;<em>nums</em> = <code>[1,3,-1,-3,5,3,6,7]</code>，以及&nbsp;<em>k</em> = 3。</p>

<pre>
窗口位置                      中位数
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
</pre>

<p>&nbsp;因此，返回该滑动窗口的中位数数组&nbsp;<code>[1,-1,-1,3,5,6]</code>。</p>

<p><strong>提示：</strong><br />
假设<code>k</code>是合法的，即：<code>k</code> 始终小于输入的非空数组的元素个数.</p>
