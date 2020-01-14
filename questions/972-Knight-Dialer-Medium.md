#### 骑士拨号器/Knight Dialer
**难度：** 中等/Medium

**Question：** 

<p>A chess knight can move as indicated in the chess diagram below:</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2018/10/12/knight.png" style="width: 150px; height: 150px;" />&nbsp;.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<img alt="" src="https://assets.leetcode.com/uploads/2018/10/30/keypad.png" style="width: 134px; height: 150px;" /></p>

<p>&nbsp;</p>

<p>This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes <code>N-1</code> hops.&nbsp; Each hop must be from one key to another numbered key.</p>

<p>Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing <code>N</code> digits total.</p>

<p>How many distinct numbers can you dial in this manner?</p>

<p>Since the answer may be large, <strong>output the answer&nbsp;modulo <code>10^9 + 7</code></strong>.</p>

<p>&nbsp;</p>

<ul>
</ul>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">1</span>
<strong>Output: </strong><span id="example-output-1">10</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">2</span>
<strong>Output: </strong><span id="example-output-2">20</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">3</span>
<strong>Output: </strong><span id="example-output-3">46</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>1 &lt;= N &lt;= 5000</code></li>
</ul>
</div>
</div>
</div>


------

**题目：** 
<p>国际象棋中的骑士可以按下图所示进行移动：</p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/11/03/knight.png" style="height: 150px; width: 150px;">&nbsp;.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/11/03/keypad.png" style="height: 150px; width: 134px;"></p>

<p><br>
这一次，我们将&nbsp;&ldquo;骑士&rdquo; 放在电话拨号盘的任意数字键（如上图所示）上，接下来，骑士将会跳&nbsp;N-1 步。每一步必须是从一个数字键跳到另一个数字键。</p>

<p>每当它落在一个键上（包括骑士的初始位置），都会拨出键所对应的数字，总共按下&nbsp;<code>N</code> 位数字。</p>

<p>你能用这种方式拨出多少个不同的号码？</p>

<p>因为答案可能很大，<strong>所以输出答案模&nbsp;<code>10^9 + 7</code></strong>。</p>

<p>&nbsp;</p>

<ul>
</ul>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>1
<strong>输出：</strong>10
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>2
<strong>输出：</strong>20
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>3
<strong>输出：</strong>46
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= N &lt;= 5000</code></li>
</ul>

