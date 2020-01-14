#### 比较版本号/Compare Version Numbers
**难度：** 中等/Medium

**Question：** 

<p>Compare two version numbers <em>version1</em> and <em>version2</em>.<br />
If <code><em>version1</em> &gt; <em>version2</em></code> return <code>1;</code>&nbsp;if <code><em>version1</em> &lt; <em>version2</em></code> return <code>-1;</code>otherwise return <code>0</code>.</p>

<p>You may assume that the version strings are non-empty and contain only digits and the <code>.</code> character.</p>
<p>The <code>.</code> character does not represent a decimal point and is used to separate number sequences.</p>
<p>For instance, <code>2.5</code> is not &quot;two and a half&quot; or &quot;half way to version three&quot;, it is the fifth second-level revision of the second first-level revision.</p>
<p>You may assume the default revision number for each level of a version number to be <code>0</code>. For example, version number <code>3.4</code> has a revision number of <code>3</code> and <code>4</code> for its first and second level revision number. Its third and fourth level revision number are both <code>0</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>
<pre>
<strong>Input:</strong> <code><em>version1</em></code> = &quot;0.1&quot;, <code><em>version2</em></code> = &quot;1.1&quot;
<strong>Output:</strong> -1</pre>

<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong><code><em>version1</em></code> = &quot;1.0.1&quot;, <code><em>version2</em></code> = &quot;1&quot;
<strong>Output:</strong> 1</pre>

<p><strong>Example 3:</strong></p>
<pre>
<strong>Input:</strong> <code><em>version1</em></code> = &quot;7.5.2.4&quot;, <code><em>version2</em></code> = &quot;7.5.3&quot;
<strong>Output:</strong> -1</pre>

<p><strong>Example 4:</strong></p>
<pre>
<strong>Input:</strong> <code><em>version1</em></code> = &quot;1.01&quot;, <code><em>version2</em></code> = &quot;1.001&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> Ignoring leading zeroes, both “01” and “001" represent the same number “1”</pre>

<p><strong>Example 5:</strong></p>
<pre>
<strong>Input:</strong> <code><em>version1</em></code> = &quot;1.0&quot;, <code><em>version2</em></code> = &quot;1.0.0&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> The first version number does not have a third level revision number, which means its third level revision number is default to "0"</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>
<ol>
<li>Version strings are composed of numeric strings separated by dots <code>.</code> and this numeric strings <strong>may</strong> have leading zeroes. </li>
<li>Version strings do not start or end with dots, and they will not be two consecutive dots.</li>
</ol>

------

**题目：** 
<p>比较两个版本号 <em>version1&nbsp;</em>和 <em>version2</em>。<br>
如果&nbsp;<code><em>version1&nbsp;</em>&gt;&nbsp;<em>version2</em></code>&nbsp;返回&nbsp;<code>1</code>，如果&nbsp;<code><em>version1&nbsp;</em>&lt;&nbsp;<em>version2</em></code> 返回 <code>-1</code>， 除此之外返回 <code>0</code>。</p>

<p>你可以假设版本字符串非空，并且只包含数字和&nbsp;<code>.</code> 字符。</p>

<p>&nbsp;<code>.</code> 字符不代表小数点，而是用于分隔数字序列。</p>

<p>例如，<code>2.5</code> 不是&ldquo;两个半&rdquo;，也不是&ldquo;差一半到三&rdquo;，而是第二版中的第五个小版本。</p>

<p>你可以假设版本号的每一级的默认修订版号为 <code>0</code>。例如，版本号 <code>3.4</code> 的第一级（大版本）和第二级（小版本）修订号分别为 <code>3</code> 和 <code>4</code>。其第三级和第四级修订号均为 <code>0</code>。<br>
&nbsp;</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> <code><em>version1</em></code> = &quot;0.1&quot;, <code><em>version2</em></code> = &quot;1.1&quot;
<strong>输出:</strong> -1</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入: </strong><code><em>version1</em></code> = &quot;1.0.1&quot;, <code><em>version2</em></code> = &quot;1&quot;
<strong>输出:</strong> 1</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong> <code><em>version1</em></code> = &quot;7.5.2.4&quot;, <code><em>version2</em></code> = &quot;7.5.3&quot;
<strong>输出:</strong> -1</pre>

<p><strong>示例&nbsp;4：</strong></p>

<pre><code><strong>输入：</strong><em>version1</em></code> = &quot;1.01&quot;, <code><em>version2</em></code> = &quot;1.001&quot;
<strong>输出：</strong>0
<strong>解释：</strong>忽略前导零，&ldquo;01&rdquo; 和 &ldquo;001&rdquo; 表示相同的数字 &ldquo;1&rdquo;。</pre>

<p><strong>示例 5：</strong></p>

<pre><code><strong>输入：</strong><em>version1</em></code> = &quot;1.0&quot;, <code><em>version2</em></code> = &quot;1.0.0&quot;
<strong>输出：</strong>0
<strong>解释：</strong><code><em>version1 </em></code>没有第三级修订号，这意味着它的第三级修订号默认为 &ldquo;0&rdquo;。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>版本字符串由以点&nbsp;（<code>.</code>）&nbsp;分隔的数字字符串组成。这个数字字符串<strong>可能</strong>有前导零。</li>
	<li>版本字符串不以点开始或结束，并且其中不会有两个连续的点。</li>
</ol>

