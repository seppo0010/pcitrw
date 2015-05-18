### Btree

#### Example

##### Dictionary

Let's grab a dictionary, and insert in the first page an index that associates
each letter with the page that letter's first word is. Now, at the begin of
each letter, we can create another index for the combination of that letter and
the next one in the word, and so on.

Now we can find out each word by following the index letter by letter, without
any search.

![](02-05-btree.dictionary.png)

#### Properties

A Btree allows you to have a hierarchy of index to follow to get the element
you are looking for. The number of indices to follow grows with the number of
elements, but at a much slower rate.
