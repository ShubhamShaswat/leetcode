#### 设计循环队列/Design Circular Queue
**难度：** 中等/Medium

**Question：** 

<p>Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called &quot;Ring Buffer&quot;.</p>

<p>One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.</p>

<p>Your implementation should support following operations:</p>

<ul>
	<li><code>MyCircularQueue(k)</code>: Constructor, set the size of the queue to be k.</li>
	<li><code>Front</code>: Get the front item from the queue. If the queue is empty, return -1.</li>
	<li><code>Rear</code>: Get the last item from the queue. If the queue is empty, return -1.</li>
	<li><code>enQueue(value)</code>: Insert an element into the circular queue. Return true if the operation is successful.</li>
	<li><code>deQueue()</code>: Delete an element from the circular queue. Return true if the operation is successful.</li>
	<li><code>isEmpty()</code>: Checks whether the circular queue is empty or not.</li>
	<li><code>isFull()</code>: Checks whether the circular queue is full or not.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
circularQueue.enQueue(1); &nbsp;// return true
circularQueue.enQueue(2); &nbsp;// return true
circularQueue.enQueue(3); &nbsp;// return true
circularQueue.enQueue(4); &nbsp;// return false, the queue is full
circularQueue.Rear(); &nbsp;// return 3
circularQueue.isFull(); &nbsp;// return true
circularQueue.deQueue(); &nbsp;// return true
circularQueue.enQueue(4); &nbsp;// return true
circularQueue.Rear(); &nbsp;// return 4
</pre>
&nbsp;

<p><strong>Note:</strong></p>

<ul>
	<li>All values will be in the range of [0, 1000].</li>
	<li>The number of operations will be in the range of&nbsp;[1, 1000].</li>
	<li>Please do not use the built-in Queue library.</li>
</ul>


------

**题目：** 
<p>设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为&ldquo;环形缓冲器&rdquo;。</p>

<p>循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。</p>

<p>你的实现应该支持如下操作：</p>

<ul>
	<li><code>MyCircularQueue(k)</code>: 构造器，设置队列长度为 k 。</li>
	<li><code>Front</code>: 从队首获取元素。如果队列为空，返回 -1 。</li>
	<li><code>Rear</code>: 获取队尾元素。如果队列为空，返回 -1 。</li>
	<li><code>enQueue(value)</code>: 向循环队列插入一个元素。如果成功插入则返回真。</li>
	<li><code>deQueue()</code>: 从循环队列中删除一个元素。如果成功删除则返回真。</li>
	<li><code>isEmpty()</code>: 检查循环队列是否为空。</li>
	<li><code>isFull()</code>: 检查循环队列是否已满。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>MyCircularQueue circularQueue = new MycircularQueue(3); // 设置长度为 3

circularQueue.enQueue(1); &nbsp;// 返回 true

circularQueue.enQueue(2); &nbsp;// 返回 true

circularQueue.enQueue(3); &nbsp;// 返回 true

circularQueue.enQueue(4); &nbsp;// 返回 false，队列已满

circularQueue.Rear(); &nbsp;// 返回 3

circularQueue.isFull(); &nbsp;// 返回 true

circularQueue.deQueue(); &nbsp;// 返回 true

circularQueue.enQueue(4); &nbsp;// 返回 true

circularQueue.Rear(); &nbsp;// 返回 4
&nbsp;</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>所有的值都在 0&nbsp;至 1000 的范围内；</li>
	<li>操作数将在 1 至 1000 的范围内；</li>
	<li>请不要使用内置的队列库。</li>
</ul>

