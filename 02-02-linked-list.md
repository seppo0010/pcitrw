### Linked List

#### Example

##### Field trip

In a school field trip, stand all children in a line and ask them to remember
who is to their right. Now, you remember who is in each of the sides.

Now at any point, you can ask the first child to point to the second, and then
ask the second for the third, and so on. If you get to the last child then you
are sure that your list is complete.

![](02-02-linked-list.field-trip.png)

#### Properties

In this case, it is easy to add something at any point in the list. If the
list is sorted, you can find where the item needs to be added and just ask the
previous item point to the new value and the new value to what the item was
pointing at.

It is hard, though, to identify a item by its position. If you want to know
the position of a item, you have to start from the first and count until you
get to it.
