#### 位1的个数/Number of 1 Bits
**难度：** 简单/Easy

**Question：** 

<p>Write a function that takes an unsigned integer and return&nbsp;the number of &#39;1&#39;&nbsp;bits it has (also known as the <a href="http://en.wikipedia.org/wiki/Hamming_weight" target="_blank">Hamming weight</a>).</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 00000000000000000000000000001011
<strong>Output:</strong> 3
<strong>Explanation: </strong>The input binary string <code><strong>00000000000000000000000000001011</strong>&nbsp;has a total of three &#39;1&#39; bits.</code>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 00000000000000000000000010000000
<strong>Output:</strong> 1
<strong>Explanation: </strong>The input binary string <strong>00000000000000000000000010000000</strong>&nbsp;has a total of one &#39;1&#39; bit.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> 11111111111111111111111111111101
<strong>Output:</strong> 31
<strong>Explanation: </strong>The input binary string <strong>11111111111111111111111111111101</strong> has a total of thirty one &#39;1&#39; bits.</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.</li>
	<li>In Java,&nbsp;the compiler represents the signed integers using <a href="https://en.wikipedia.org/wiki/Two%27s_complement" target="_blank">2&#39;s complement notation</a>. Therefore, in <strong>Example 3</strong>&nbsp;above the input represents the signed integer <code>-3</code>.</li>
</ul>

<p>&nbsp;</p>

<p><b>Follow up</b>:</p>

<p>If this function is called many times, how would you optimize it?</p>


------

**题目：** 
<p>编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 &lsquo;1&rsquo;&nbsp;的个数（也被称为<a href="https://baike.baidu.com/item/%E6%B1%89%E6%98%8E%E9%87%8D%E9%87%8F" target="_blank">汉明重量</a>）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>00000000000000000000000000001011
<strong>输出：</strong>3
<strong>解释：</strong>输入的二进制串 <code><strong>00000000000000000000000000001011</strong>&nbsp;中，共有三位为 &#39;1&#39;。</code>
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>00000000000000000000000010000000
<strong>输出：</strong>1
<strong>解释：</strong>输入的二进制串 <strong>00000000000000000000000010000000</strong>&nbsp;中，共有一位为 &#39;1&#39;。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>11111111111111111111111111111101
<strong>输出：</strong>31
<strong>解释：</strong>输入的二进制串 <strong>11111111111111111111111111111101</strong> 中，共有 31 位为 &#39;1&#39;。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。</li>
	<li>在 Java 中，编译器使用<a href="https://baike.baidu.com/item/二进制补码/5295284" target="_blank">二进制补码</a>记法来表示有符号整数。因此，在上面的&nbsp;<strong>示例 3</strong>&nbsp;中，输入表示有符号整数 <code>-3</code>。</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶</strong>:<br>
如果多次调用这个函数，你将如何优化你的算法？</p>

