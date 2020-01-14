#### 破解保险箱/Cracking the Safe
**难度：** 困难/Hard

**Question：** 

<p>There is a box protected by a password. The password is a sequence of&nbsp;<code>n</code> digits&nbsp;where each digit can be one of the first <code>k</code> digits <code>0, 1, ..., k-1</code>.</p>

<p>While entering a password,&nbsp;the last <code>n</code> digits entered will automatically be matched against the correct password.</p>

<p>For example, assuming the correct password is <code>&quot;345&quot;</code>,&nbsp;if you type <code>&quot;012345&quot;</code>, the box will open because the correct password matches the suffix of the entered password.</p>

<p>Return any password of <strong>minimum length</strong> that is guaranteed to open the box at some point of entering it.</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> n = 1, k = 2
<b>Output:</b> &quot;01&quot;
<b>Note:</b> &quot;10&quot; will be accepted too.
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> n = 2, k = 2
<b>Output:</b> &quot;00110&quot;
<b>Note:</b> &quot;01100&quot;, &quot;10011&quot;, &quot;11001&quot; will be accepted too.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li><code>n</code> will be in the range <code>[1, 4]</code>.</li>
	<li><code>k</code> will be in the range <code>[1, 10]</code>.</li>
	<li><code>k^n</code> will be at most <code>4096</code>.</li>
</ol>

<p>&nbsp;</p>


------

**题目：** 
<p>有一个需要密码才能打开的保险箱。密码是&nbsp;<code>n</code> 位数, 密码的每一位是&nbsp;<code>k</code>&nbsp;位序列&nbsp;<code>0, 1, ..., k-1</code>&nbsp;中的一个 。</p>

<p>你可以随意输入密码，保险箱会自动记住最后&nbsp;<code>n</code>&nbsp;位输入，如果匹配，则能够打开保险箱。</p>

<p>举个例子，假设密码是&nbsp;<code>&quot;345&quot;</code>，你可以输入&nbsp;<code>&quot;012345&quot;</code>&nbsp;来打开它，只是你输入了 6&nbsp;个字符.</p>

<p>请返回一个能打开保险箱的最短字符串。</p>

<p>&nbsp;</p>

<p><strong>示例1:</strong></p>

<pre><strong>输入:</strong> n = 1, k = 2
<strong>输出:</strong> &quot;01&quot;
<strong>说明:</strong> &quot;10&quot;也可以打开保险箱。
</pre>

<p>&nbsp;</p>

<p><strong>示例2:</strong></p>

<pre><strong>输入:</strong> n = 2, k = 2
<strong>输出:</strong> &quot;00110&quot;
<strong>说明: </strong>&quot;01100&quot;, &quot;10011&quot;, &quot;11001&quot; 也能打开保险箱。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>n</code> 的范围是&nbsp;<code>[1, 4]</code>。</li>
	<li><code>k</code> 的范围是&nbsp;<code>[1, 10]</code>。</li>
	<li><code>k^n</code> 最大可能为&nbsp;<code>4096</code>。</li>
</ol>

<p>&nbsp;</p>

