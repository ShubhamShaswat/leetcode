#### 由斜杠划分区域/Regions Cut By Slashes
**难度：** 中等/Medium

**Question：** 

<p>In a N x N&nbsp;<code>grid</code> composed of 1 x 1 squares, each 1 x 1 square consists of a <code>/</code>, <code>\</code>, or blank space.&nbsp; These characters divide the square into contiguous regions.</p>

<p>(Note that backslash characters are escaped, so a <code>\</code>&nbsp;is represented as <code>&quot;\\&quot;</code>.)</p>

<p>Return the number of regions.</p>

<p>&nbsp;</p>

<div>
<div>
<div>
<div>
<div>
<ol>
</ol>
</div>
</div>
</div>
</div>
</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:
</strong><span id="example-input-1-1">[
&nbsp; &quot; /&quot;,
&nbsp; &quot;/ &quot;
]</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/1.png" style="width: 82px; height: 82px;" />
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:
</strong><span id="example-input-2-1">[
&nbsp; &quot; /&quot;,
&nbsp; &quot;  &quot;
]</span>
<strong>Output: </strong><span id="example-output-2">1</span>
<strong>Explanation: </strong>The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/2.png" style="width: 82px; height: 82px;" />
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:
</strong><span id="example-input-3-1">[
&nbsp; &quot;\\/&quot;,
&nbsp; &quot;/\\&quot;
]</span>
<strong>Output: </strong><span id="example-output-3">4</span>
<strong>Explanation: </strong>(Recall that because \ characters are escaped, &quot;\\/&quot; refers to \/, and &quot;/\\&quot; refers to /\.)
The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/3.png" style="width: 82px; height: 82px;" />
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:
</strong><span id="example-input-4-1">[
&nbsp; &quot;/\\&quot;,
&nbsp; &quot;\\/&quot;
]</span>
<strong>Output: </strong><span id="example-output-4">5</span>
<strong>Explanation: </strong>(Recall that because \ characters are escaped, &quot;/\\&quot; refers to /\, and &quot;\\/&quot; refers to \/.)
The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/4.png" style="width: 82px; height: 82px;" />
</pre>

<div>
<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:
</strong><span id="example-input-5-1">[
&nbsp; &quot;//&quot;,
&nbsp; &quot;/ &quot;
]</span>
<strong>Output: </strong><span id="example-output-5">3</span>
<strong>Explanation: </strong>The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/5.png" style="width: 82px; height: 82px;" />
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= grid.length == grid[0].length &lt;= 30</code></li>
	<li><code>grid[i][j]</code> is either <code>&#39;/&#39;</code>, <code>&#39;\&#39;</code>, or <code>&#39; &#39;</code>.</li>
</ol>
</div>
</div>
</div>
</div>
</div>

------

**题目：** 
<p>在由 1 x 1 方格组成的 N x N 网格&nbsp;<code>grid</code> 中，每个 1 x 1&nbsp;方块由 <code>/</code>、<code>\</code> 或空格构成。这些字符会将方块划分为一些共边的区域。</p>

<p>（请注意，反斜杠字符是转义的，因此 <code>\</code> 用 <code>&quot;\\&quot;</code>&nbsp;表示。）。</p>

<p>返回区域的数目。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：
</strong>[
&nbsp; &quot; /&quot;,
&nbsp; &quot;/ &quot;
]
<strong>输出：</strong>2
<strong>解释：</strong>2x2 网格如下：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/1.png"></pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：
</strong>[
&nbsp; &quot; /&quot;,
&nbsp; &quot;  &quot;
]
<strong>输出：</strong>1
<strong>解释：</strong>2x2 网格如下：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/2.png"></pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：
</strong>[
&nbsp; &quot;\\/&quot;,
&nbsp; &quot;/\\&quot;
]
<strong>输出：</strong>4
<strong>解释：</strong>（回想一下，因为 \ 字符是转义的，所以 &quot;\\/&quot; 表示 \/，而 &quot;/\\&quot; 表示 /\。）
2x2 网格如下：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/3.png"></pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：
</strong>[
&nbsp; &quot;/\\&quot;,
&nbsp; &quot;\\/&quot;
]
<strong>输出：</strong>5
<strong>解释：</strong>（回想一下，因为 \ 字符是转义的，所以 &quot;/\\&quot; 表示 /\，而 &quot;\\/&quot; 表示 \/。）
2x2 网格如下：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/4.png"></pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：
</strong>[
&nbsp; &quot;//&quot;,
&nbsp; &quot;/ &quot;
]
<strong>输出：</strong>3
<strong>解释：</strong>2x2 网格如下：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/5.png">
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= grid.length == grid[0].length &lt;= 30</code></li>
	<li><code>grid[i][j]</code> 是&nbsp;<code>&#39;/&#39;</code>、<code>&#39;\&#39;</code>、或&nbsp;<code>&#39; &#39;</code>。</li>
</ol>

