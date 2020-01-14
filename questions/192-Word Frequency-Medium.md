#### 统计词频/Word Frequency
**难度：** 中等/Medium

**Question：** 

<p>Write a bash script to calculate the frequency of each word in a text file <code>words.txt</code>.</p>

<p>For simplicity sake, you may assume:</p>

<ul>
	<li><code>words.txt</code> contains only lowercase characters and space <code>&#39; &#39;</code> characters.</li>
	<li>Each word must consist of lowercase characters only.</li>
	<li>Words are separated by one or more whitespace characters.</li>
</ul>

<p><strong>Example:</strong></p>

<p>Assume that <code>words.txt</code> has the following content:</p>

<pre>
the day is sunny the the
the sunny is is
</pre>

<p>Your script should output the following, sorted by descending frequency:</p>

<pre>
the 4
is 3
sunny 2
day 1
</pre>

<p><b>Note:</b></p>

<ul>
	<li>Don&#39;t worry about handling ties, it is guaranteed that each word&#39;s frequency count is unique.</li>
	<li>Could you write it in one-line using <a href="http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-4.html">Unix pipes</a>?</li>
</ul>


------

**题目：** 
<p>写一个 bash 脚本以统计一个文本文件&nbsp;<code>words.txt</code>&nbsp;中每个单词出现的频率。</p>

<p>为了简单起见，你可以假设：</p>

<ul>
	<li><code>words.txt</code>只包括小写字母和&nbsp;<code>&#39; &#39;</code>&nbsp;。</li>
	<li>每个单词只由小写字母组成。</li>
	<li>单词间由一个或多个空格字符分隔。</li>
</ul>

<p><strong>示例:</strong></p>

<p>假设 <code>words.txt</code> 内容如下：</p>

<pre>the day is sunny the the
the sunny is is
</pre>

<p>你的脚本应当输出（以词频降序排列）：</p>

<pre>the 4
is 3
sunny 2
day 1
</pre>

<p><strong>说明:</strong></p>

<ul>
	<li>不要担心词频相同的单词的排序问题，每个单词出现的频率都是唯一的。</li>
	<li>你可以使用一行&nbsp;<a href="http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-4.html">Unix pipes</a>&nbsp;实现吗？</li>
</ul>

