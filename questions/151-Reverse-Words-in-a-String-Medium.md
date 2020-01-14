#### 翻转字符串里的单词/Reverse Words in a String
**难度：** 中等/Medium

**Question：** 

<p>Given an input string, reverse the string word by word.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;<code>the sky is blue</code>&quot;
<strong>Output:&nbsp;</strong>&quot;<code>blue is sky the</code>&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot; &nbsp;hello world! &nbsp;&quot;
<strong>Output:&nbsp;</strong>&quot;world! hello&quot;
<strong>Explanation:</strong> Your reversed string should not contain leading or trailing spaces.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> &quot;a good &nbsp; example&quot;
<strong>Output:&nbsp;</strong>&quot;example good a&quot;
<strong>Explanation:</strong> You need to reduce multiple spaces between two words to a single space in the reversed string.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>A word is defined as a sequence of non-space characters.</li>
	<li>Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.</li>
	<li>You need to reduce multiple spaces between two words to a single space in the reversed string.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Follow up:</strong></p>

<p>For C programmers, try to solve it <em>in-place</em> in <em>O</em>(1) extra space.</p>

------

**题目：** 
<p>给定一个字符串，逐个翻转字符串中的每个单词。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入:</strong> &quot;<code>the sky is blue</code>&quot;
<strong>输出:&nbsp;</strong>&quot;<code>blue is sky the</code>&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入:</strong> &quot; &nbsp;hello world! &nbsp;&quot;
<strong>输出:&nbsp;</strong>&quot;world! hello&quot;
<strong>解释: </strong>输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入:</strong> &quot;a good &nbsp; example&quot;
<strong>输出:&nbsp;</strong>&quot;example good a&quot;
<strong>解释: </strong>如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
</pre>

<p>&nbsp;</p>

<p><strong>说明：</strong></p>

<ul>
	<li>无空格字符构成一个单词。</li>
	<li>输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。</li>
	<li>如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<p>请选用 C 语言的用户尝试使用&nbsp;<em>O</em>(1) 额外空间复杂度的原地解法。</p>

