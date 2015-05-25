### CAP Theorem

#### Example

##### Civil Registry

Suppose a Civil Registry with five offices and phone lines between them.
There are different ways of organizing. We are going to look into two of them.

####### Highly available (AP)

Each of the offices can take new information from people and at the end of the day,
they will share it with all the other offices.

This could be a problem since it may allow incorrect information, for example if a
person is filed as dead in one office and then gets married in another one.
If there was a single office, this would never happen since that person's
registry will be kept up to date, but now we are allowing up to one day
old information.

Other possible problem is what happens if one office has a problem and some of
its information from the day is lost. People who already left the office do not know
the Registry lost it and will run into a problem in the future.

###### Highly consistent (CP)

In this other approach, any information change needs to be checked by all the
offices. This way, all the information is always correct, available in every office,
and no one is the single responsible for it.

Problems may appear when the phone lines are not working properly. If a single
office phone is broken, all offices will stop working.

##### Definition

It is said that a distributed database can only be highly available or highly
consistent. Different balances between both can be achieved for different use
cases.
