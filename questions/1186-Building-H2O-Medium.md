#### H2O 生成/Building H2O
**难度：** 中等/Medium

**Question：** 

<p>There are two kinds of threads, <code>oxygen</code> and <code>hydrogen</code>. Your goal is to group these threads to form water molecules.&nbsp;There is a barrier where each thread has to&nbsp;wait until a complete molecule can be formed. Hydrogen and oxygen threads will be given <code>releaseHydrogen</code>&nbsp;and <code>releaseOxygen</code>&nbsp;methods respectively, which will allow them to pass the barrier. These threads should pass the barrier in groups of three, and they must be able to immediately bond with each other to form a water molecule.&nbsp;You must guarantee that all the threads from one molecule bond <em>before</em> any other threads from the next molecule do.</p>

<p>In other words:</p>

<ul>
	<li>If an oxygen thread arrives at the barrier when no hydrogen threads are present, it has to wait for two hydrogen threads.</li>
	<li>If a hydrogen thread arrives at the barrier when no other threads are present, it has to wait for an oxygen thread and another hydrogen thread.</li>
</ul>

<p>We don&rsquo;t have to worry about matching the threads up explicitly; that is, the threads do not necessarily know which other threads they are paired up with. The key is just that threads pass the barrier in complete sets; thus, if we examine the sequence of threads that bond and divide them into groups of three, each group should contain one oxygen and two hydrogen threads.</p>

<p>Write synchronization code for oxygen and hydrogen molecules that enforces these constraints.</p>

<div>
<p>&nbsp;</p>
</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;HOH&quot;</span>
<strong>Output: </strong><span id="example-output-1">&quot;HHO&quot;
<strong>Explanation:</strong> &quot;HOH&quot; and &quot;OHH&quot; are also valid answers.</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;OOHHHH&quot;</span>
<strong>Output: </strong><span id="example-output-1">&quot;HHOHHO&quot;
<strong>Explanation:</strong> &quot;HOHHHO&quot;, &quot;OHHHHO&quot;, &quot;HHOHOH&quot;, &quot;HOHHOH&quot;, &quot;OHHHOH&quot;, &quot;HHOOHH&quot;, &quot;HOHOHH&quot; and &quot;OHHOHH&quot; are also valid answers.</span>
</pre>
</div>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>Total length of input string will be 3<em>n</em>, where 1 &le;&nbsp;<em>n</em>&nbsp;&le; 20.</li>
	<li>Total number of <code>H</code> will be 2<em>n</em>&nbsp;in the input string.</li>
	<li>Total number of <code>O</code> will&nbsp;be <em>n</em>&nbsp;in the input&nbsp;string.</li>
</ul>


------

**题目：** 
<p>现在有两种线程，氢 <code>oxygen</code> 和氧 <code>hydrogen</code>，你的目标是组织这两种线程来产生水分子。</p>

<p>存在一个屏障（barrier）使得每个线程必须等候直到一个完整水分子能够被产生出来。</p>

<p>氢和氧线程会被分别给予 <code>releaseHydrogen</code> 和 <code>releaseOxygen</code> 方法来允许它们突破屏障。</p>

<p>这些线程应该三三成组突破屏障并能立即组合产生一个水分子。</p>

<p>你必须保证产生一个水分子所需线程的结合必须发生在下一个水分子产生之前。</p>

<p>换句话说:</p>

<ul>
	<li>如果一个氧线程到达屏障时没有氢线程到达，它必须等候直到两个氢线程到达。</li>
	<li>如果一个氢线程到达屏障时没有其它线程到达，它必须等候直到一个氧线程和另一个氢线程到达。</li>
</ul>

<p>书写满足这些限制条件的氢、氧线程同步代码。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入: </strong>&quot;HOH&quot;
<strong>输出: </strong>&quot;HHO&quot;
<strong>解释:</strong> &quot;HOH&quot; 和 &quot;OHH&quot; 依然都是有效解。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: </strong>&quot;OOHHHH&quot;
<strong>输出: </strong>&quot;HHOHHO&quot;
<strong>解释:</strong> &quot;HOHHHO&quot;, &quot;OHHHHO&quot;, &quot;HHOHOH&quot;, &quot;HOHHOH&quot;, &quot;OHHHOH&quot;, &quot;HHOOHH&quot;, &quot;HOHOHH&quot; 和 &quot;OHHOHH&quot; 依然都是有效解。
</pre>

<p>&nbsp;</p>

<p><strong>限制条件:</strong></p>

<ul>
	<li>输入字符串的总长将会是 3<em>n</em>, 1 &le;&nbsp;<em>n</em>&nbsp;&le; 50；</li>
	<li>输入字符串中的 &ldquo;H&rdquo; 总数将会是 2n；</li>
	<li>输入字符串中的 &ldquo;O&rdquo; 总数将会是 n。</li>
</ul>

