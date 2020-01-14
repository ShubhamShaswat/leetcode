#### 最小好进制/Smallest Good Base
**难度：** 困难/Hard

**Question：** 

<p>For an integer n, we call k&gt;=2 a <i><b>good base</b></i> of n, if all digits of n base k are 1.</p>

<p>Now given a string representing n, you should return the smallest good base of n in string format.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> &quot;13&quot;
<b>Output:</b> &quot;3&quot;
<b>Explanation:</b> 13 base 3 is 111.
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> &quot;4681&quot;
<b>Output:</b> &quot;8&quot;
<b>Explanation:</b> 4681 base 8 is 11111.
</pre>

<p>&nbsp;</p>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> &quot;1000000000000000000&quot;
<b>Output:</b> &quot;999999999999999999&quot;
<b>Explanation:</b> 1000000000000000000 base 999999999999999999 is 11.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The range of n is [3, 10^18].</li>
	<li>The string representing n is always valid and will not have leading zeros.</li>
</ol>

<p>&nbsp;</p>


------

**题目：** 
<p>对于给定的整数 n, 如果n的k（k&gt;=2）进制数的所有数位全为1，则称&nbsp;k（k&gt;=2）是 n 的一个<em><strong>好进制</strong></em>。</p>

<p>以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>&quot;13&quot;
<strong>输出：</strong>&quot;3&quot;
<strong>解释：</strong>13 的 3 进制是 111。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>&quot;4681&quot;
<strong>输出：</strong>&quot;8&quot;
<strong>解释：</strong>4681 的 8 进制是 11111。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>&quot;1000000000000000000&quot;
<strong>输出：</strong>&quot;999999999999999999&quot;
<strong>解释：</strong>1000000000000000000 的 999999999999999999 进制是 11。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>n的取值范围是&nbsp;[3, 10^18]。</li>
	<li>输入总是有效且没有前导 0。</li>
</ol>

<p>&nbsp;</p>

