#### 播放列表的数量/Number of Music Playlists
**难度：** 困难/Hard

**Question：** 

<p>Your music player contains <code>N</code>&nbsp;different songs and she wants to listen to <code>L</code><strong> </strong>(not necessarily different) songs during your trip. &nbsp;You&nbsp;create&nbsp;a playlist so&nbsp;that:</p>

<ul>
	<li>Every song is played at least once</li>
	<li>A song can only be played again only if&nbsp;<code>K</code>&nbsp;other songs have been played</li>
</ul>

<p>Return the number of possible playlists.&nbsp; <strong>As the answer can be very large, return it modulo <code>10^9 + 7</code></strong>.</p>

<p>&nbsp;</p>

<div>
<div>
<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-1-1">3</span>, L = <span id="example-input-1-2">3</span>, K = <span id="example-input-1-3">1</span>
<strong>Output: </strong><span id="example-output-1">6
<strong>Explanation</strong>: </span><span>There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-2-1">2</span>, L = <span id="example-input-2-2">3</span>, K = <span id="example-input-2-3">0</span>
<strong>Output: </strong><span id="example-output-2">6
</span><span id="example-output-1"><strong>Explanation</strong>: </span><span>There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2]</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-3-1">2</span>, L = <span id="example-input-3-2">3</span>, K = <span id="example-input-3-3">1</span>
<strong>Output: </strong><span id="example-output-3">2
<strong>Explanation</strong>: </span><span>There are 2 possible playlists. [1, 2, 1], [2, 1, 2]</span>
</pre>
</div>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= K &lt; N &lt;= L &lt;= 100</code></li>
</ol>
</div>
</div>
</div>

------

**题目：** 
<p>你的音乐播放器里有&nbsp;<code>N</code>&nbsp;首不同的歌，在旅途中，你的旅伴想要听 <code>L</code>&nbsp;首歌（不一定不同，即，允许歌曲重复）。请你为她按如下规则创建一个播放列表：</p>

<ul>
	<li>每首歌至少播放一次。</li>
	<li>一首歌只有在其他 <code>K</code> 首歌播放完之后才能再次播放。</li>
</ul>

<p>返回可以满足要求的播放列表的数量。<strong>由于答案可能非常大，请返回它模&nbsp;<code>10^9 + 7</code>&nbsp;的结果。</strong></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>N = 3, L = 3, K = 1
<strong>输出：</strong>6
<strong>解释：</strong>有 6 种可能的播放列表。[1, 2, 3]，[1, 3, 2]，[2, 1, 3]，[2, 3, 1]，[3, 1, 2]，[3, 2, 1].
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>N = 2, L = 3, K = 0
<strong>输出：</strong>6
<strong>解释：</strong>有 6 种可能的播放列表。[1, 1, 2]，[1, 2, 1]，[2, 1, 1]，[2, 2, 1]，[2, 1, 2]，[1, 2, 2]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>N = 2, L = 3, K = 1
<strong>输出：</strong>2
<strong>解释：</strong>有 2 种可能的播放列表。[1, 2, 1]，[2, 1, 2]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>0 &lt;= K &lt; N &lt;= L &lt;= 100</code></li>
</ol>

