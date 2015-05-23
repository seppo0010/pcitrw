### Btree

#### Example

##### Dictionary

Let's take a dictionary and add at the beginning a new page that associates
each letter with the page that letter's first word is. Now, at the begin of
each letter, we can create another page for the that letter and the next one
in the word, and so on.

Now we can find out each word by following the pages we just added, letter by
letter.

![](02-05-btree.dictionary.png)

#### Properties

Each of these pages we are adding is called an "index". A Btree allows you to 
follow index after index until getting the item you are looking for.
The number of indexes to follow grows with the number of items, but at a much
slower rate.
