#### N 天后的牢房/Prison Cells After N Days
**难度：** 中等/Medium

**Question：** 

<p>There are 8 prison cells in a row, and each cell is either occupied or vacant.</p>

<p>Each day, whether the cell is occupied or vacant changes according to the following rules:</p>

<ul>
	<li>If a cell has two adjacent neighbors that are both occupied or both vacant,&nbsp;then the cell becomes occupied.</li>
	<li>Otherwise, it becomes vacant.</li>
</ul>

<p>(Note that because the prison is a row, the first and the last cells in the row can&#39;t have two adjacent neighbors.)</p>

<p>We describe the current state of the prison&nbsp;in the following way:&nbsp;<code>cells[i] == 1</code> if the <code>i</code>-th cell is occupied, else <code>cells[i] == 0</code>.</p>

<p>Given the initial state of the prison, return the state of the prison after <code>N</code> days (and <code>N</code> such changes described above.)</p>

<p>&nbsp;</p>

<div>
<ol>
</ol>
</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>cells = <span id="example-input-1-1">[0,1,0,1,1,0,0,1]</span>, N = <span id="example-input-1-2">7</span>
<strong>Output: </strong><span id="example-output-1">[0,0,1,1,0,0,0,0]</span>
<strong>Explanation: 
</strong><span id="example-output-1">The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]</span>

</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>cells = <span id="example-input-2-1">[1,0,0,1,0,0,1,0]</span>, N = <span id="example-input-2-2">1000000000</span>
<strong>Output: </strong><span id="example-output-2">[0,0,1,1,1,1,1,0]</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>cells.length == 8</code></li>
	<li><code>cells[i]</code> is in <code>{0, 1}</code></li>
	<li><code>1 &lt;= N &lt;= 10^9</code></li>
</ol>
</div>
</div>


------

**题目：** 
<p>8 间牢房排成一排，每间牢房不是有人住就是空着。</p>

<p>每天，无论牢房是被占用或空置，都会根据以下规则进行更改：</p>

<ul>
	<li>如果一间牢房的两个相邻的房间都被占用或都是空的，那么该牢房就会被占用。</li>
	<li>否则，它就会被空置。</li>
</ul>

<p>（请注意，由于监狱中的牢房排成一行，所以行中的第一个和最后一个房间无法有两个相邻的房间。）</p>

<p>我们用以下方式描述监狱的当前状态：如果第 <code>i</code> 间牢房被占用，则 <code>cell[i]==1</code>，否则 <code>cell[i]==0</code>。</p>

<p>根据监狱的初始状态，在 <code>N</code> 天后返回监狱的状况（和上述 N 种变化）。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>cells = [0,1,0,1,1,0,0,1], N = 7
<strong>输出：</strong>[0,0,1,1,0,0,0,0]
<strong>解释：
</strong>下表概述了监狱每天的状况：
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>cells = [1,0,0,1,0,0,1,0], N = 1000000000
<strong>输出：</strong>[0,0,1,1,1,1,1,0]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>cells.length == 8</code></li>
	<li><code>cells[i]</code>&nbsp;的值为 <code>0</code> 或 <code>1</code>&nbsp;</li>
	<li><code>1 &lt;= N &lt;= 10^9</code></li>
</ol>

