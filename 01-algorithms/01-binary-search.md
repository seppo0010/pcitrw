## Binary Search

### Dictionary

I want to look for a word in an English dictionary. An intuitive way to do it
is to open the dictionary in a random page look for any word, compare it with
the word I'm looking for and see if it has to be before or after that one.
Then, I repeat the process and on every step the search range gets smaller
until I find out the word I was looking for.

Instead of looking for a random page, the fastest way for any word is to grab
the word in the exact middle. This way each step will discard exactly half of
the options available. Picking a random word has a small chance of discarding
most of the words and a high chance of discarding few. Choosing half ensures
the maximum number of steps.

### Guess Who?

The same algorithm can be applied to the children game Guess Who?. The optimal
strategy is to ask a question that will discard half of the options.

If you go to the opposite extreme, and ask a very specific question, it is
a high-risk, high-rewards scenario. It is very likely you have obtained little
information in most cases, but in some few you guessed correctly.
