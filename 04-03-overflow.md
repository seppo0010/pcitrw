### Overflow

#### Example

##### Back to the Future time machine panel

In the film Back to the Future the Doc creates a time machine that can travel
to any time in the past or in the future. But if we see the control board we
might notice a possible problem.

![](04-03-overflow.bttf-panel.jpg)

The year is represented by an LCD display with four numbers. If we try to go to
any year after 9,999 or before -999 it will not be represented! If we try to
write it, the numbers will actually be written in the hour box instead.

#### Definition

An "overflow" happens when we want to represent a number that is too big or too
small for the space it has available.
