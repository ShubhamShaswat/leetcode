#### 长按键入/Long Pressed Name
**难度：** 简单/Easy

**Question：** 

<p>Your friend is typing his <code>name</code>&nbsp;into a keyboard.&nbsp; Sometimes, when typing a character <code>c</code>, the key might get <em>long pressed</em>, and the character will be typed 1 or more times.</p>

<p>You examine the <code>typed</code>&nbsp;characters of the keyboard.&nbsp; Return <code>True</code> if it is possible that it was your friends name, with some characters (possibly none) being long pressed.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>name = <span id="example-input-1-1">&quot;alex&quot;</span>, typed = <span id="example-input-1-2">&quot;aaleex&quot;</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation: </strong>'a' and 'e' in 'alex' were long pressed.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>name = <span id="example-input-2-1">&quot;saeed&quot;</span>, typed = <span id="example-input-2-2">&quot;ssaaedd&quot;</span>
<strong>Output: </strong><span id="example-output-2">false</span>
<strong>Explanation: </strong>'e' must have been pressed twice, but it wasn't in the typed output.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>name = <span id="example-input-3-1">&quot;leelee&quot;</span>, typed = <span id="example-input-3-2">&quot;lleeelee&quot;</span>
<strong>Output: </strong><span id="example-output-3">true</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>name = <span id="example-input-4-1">&quot;laiden&quot;</span>, typed = <span id="example-input-4-2">&quot;laiden&quot;</span>
<strong>Output: </strong><span id="example-output-4">true</span>
<strong>Explanation: </strong>It's not necessary to long press any character.
</pre>

<p>&nbsp;</p>
</div>
</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>name.length &lt;= 1000</code></li>
	<li><code>typed.length &lt;= 1000</code></li>
	<li>The characters of <code>name</code> and <code>typed</code> are lowercase letters.</li>
</ol>

<div>
<p>&nbsp;</p>

<div>
<div>
<div>&nbsp;</div>
</div>
</div>
</div>

------

**题目：** 
<p>你的朋友正在使用键盘输入他的名字&nbsp;<code>name</code>。偶尔，在键入字符&nbsp;<code>c</code>&nbsp;时，按键可能会被<em>长按</em>，而字符可能被输入 1 次或多次。</p>

<p>你将会检查键盘输入的字符&nbsp;<code>typed</code>。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回&nbsp;<code>True</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>name = &quot;alex&quot;, typed = &quot;aaleex&quot;
<strong>输出：</strong>true
<strong>解释：</strong>&#39;alex&#39; 中的 &#39;a&#39; 和 &#39;e&#39; 被长按。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>name = &quot;saeed&quot;, typed = &quot;ssaaedd&quot;
<strong>输出：</strong>false
<strong>解释：</strong>&#39;e&#39; 一定需要被键入两次，但在 typed 的输出中不是这样。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>name = &quot;leelee&quot;, typed = &quot;lleeelee&quot;
<strong>输出：</strong>true
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>name = &quot;laiden&quot;, typed = &quot;laiden&quot;
<strong>输出：</strong>true
<strong>解释：</strong>长按名字中的字符并不是必要的。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>name.length &lt;= 1000</code></li>
	<li><code>typed.length &lt;= 1000</code></li>
	<li><code>name</code> 和&nbsp;<code>typed</code>&nbsp;的字符都是小写字母。</li>
</ol>

<p>&nbsp;</p>

<p>&nbsp;</p>

