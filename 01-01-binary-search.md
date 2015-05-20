### Binary Search

#### Example

##### Dictionary

A person wants to look for a word in an English dictionary.
They may open the book in any page, choose any word in it and compare it
with the word they are looking for. Since the words are sorted they know in
which way to proceed. They can now do this process over and over again
until finding the wanted word.

Doing these steps will lead to the result sooner or later. But if
instead of comparing any word, they compare with the word that is
exactly in the middle of the acceptable range, the number of required
comparisons is as low as it can be.

![](01-01-binary-search.horse.png)

#### Guess Who?

The same idea can be applied to the children's game Guess Who?. The
best strategy is to ask a question that will drop half of the
possibilities.

On the other hand, asking a very specific question, it is very likely to get
little information in most cases, and a lot in a few.

#### Properties

Binary Search is a list of steps that we can do to find a result in a
collection. It is called "binary" because after each step, we should be able to
keep only about half of the items in the collection.

In general, it is used on a list of sorted items, like words or numbers.
But the same idea can be used any time we want to localize something, and we
can reduce half of the possible results at a time.

Since half of the possibilities are dropped after each comparison, it is
pretty fast to find what we are looking for in not so many steps. For a million
items, we can localize any one in up to twenty comparisons. And for a
thousand millions, up to 30.
