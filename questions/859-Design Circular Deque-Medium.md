#### 设计循环双端队列/Design Circular Deque
**难度：** 中等/Medium

**Question：** 

<p>Design your implementation of the circular double-ended queue (deque).</p>

<p>Your implementation should support following operations:</p>

<ul>
	<li><code>MyCircularDeque(k)</code>: Constructor, set the size of the deque to be k.</li>
	<li><code>insertFront()</code>: Adds an item at the front of Deque. Return true if the operation is successful.</li>
	<li><code>insertLast()</code>: Adds an item at the rear of Deque. Return true if the operation is successful.</li>
	<li><code>deleteFront()</code>: Deletes an item from the front of Deque. Return true if the operation is successful.</li>
	<li><code>deleteLast()</code>: Deletes an item from the rear of Deque. Return true if the operation is successful.</li>
	<li><code>getFront()</code>: Gets the front item from the Deque. If the deque is empty, return -1.</li>
	<li><code>getRear()</code>: Gets the last item from Deque. If the deque is empty, return -1.</li>
	<li><code>isEmpty()</code>: Checks whether Deque is empty or not.&nbsp;</li>
	<li><code>isFull()</code>: Checks whether Deque is full or not.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
circularDeque.insertLast(1);			// return true
circularDeque.insertLast(2);			// return true
circularDeque.insertFront(3);			// return true
circularDeque.insertFront(4);			// return false, the queue is full
circularDeque.getRear();  			// return 2
circularDeque.isFull();				// return true
circularDeque.deleteLast();			// return true
circularDeque.insertFront(4);			// return true
circularDeque.getFront();			// return 4
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>All values will be in the range of [0, 1000].</li>
	<li>The number of operations will be in the range of&nbsp;[1, 1000].</li>
	<li>Please do not use the built-in Deque library.</li>
</ul>


------

**题目：** 
<p>设计实现双端队列。<br>
你的实现需要支持以下操作：</p>

<ul>
	<li>MyCircularDeque(k)：构造函数,双端队列的大小为k。</li>
	<li>insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。</li>
	<li>insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。</li>
	<li>deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。</li>
	<li>deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。</li>
	<li>getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。</li>
	<li>getRear()：获得双端队列的最后一个元素。&nbsp;如果双端队列为空，返回 -1。</li>
	<li>isEmpty()：检查双端队列是否为空。</li>
	<li>isFull()：检查双端队列是否满了。</li>
</ul>

<p><strong>示例：</strong></p>

<pre>MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
circularDeque.insertLast(1);			        // 返回 true
circularDeque.insertLast(2);			        // 返回 true
circularDeque.insertFront(3);			        // 返回 true
circularDeque.insertFront(4);			        // 已经满了，返回 false
circularDeque.getRear();  				// 返回 2
circularDeque.isFull();				        // 返回 true
circularDeque.deleteLast();			        // 返回 true
circularDeque.insertFront(4);			        // 返回 true
circularDeque.getFront();				// 返回 4
&nbsp;</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>所有值的范围为 [1, 1000]</li>
	<li>操作次数的范围为 [1, 1000]</li>
	<li>请不要使用内置的双端队列库。</li>
</ul>

