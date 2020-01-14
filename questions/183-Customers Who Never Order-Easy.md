#### 从不订购的客户/Customers Who Never Order
**难度：** 简单/Easy

**Question：** 

<p>Suppose that a website contains two tables, the <code>Customers</code> table and the <code>Orders</code> table. Write a SQL query to find all customers who never order anything.</p>

<p>Table: <code>Customers</code>.</p>

<pre>
+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
</pre>

<p>Table: <code>Orders</code>.</p>

<pre>
+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
</pre>

<p>Using the above tables as example, return the following:</p>

<pre>
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
</pre>


------

**题目：** 
<p>某网站包含两个表，<code>Customers</code> 表和 <code>Orders</code> 表。编写一个 SQL 查询，找出所有从不订购任何东西的客户。</p>

<p><code>Customers</code> 表：</p>

<pre>+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
</pre>

<p><code>Orders</code> 表：</p>

<pre>+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
</pre>

<p>例如给定上述表格，你的查询应返回：</p>

<pre>+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
</pre>

