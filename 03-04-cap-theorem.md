### CAP Theorem

#### Example

##### Civil Registry

Supose a Civil Registry with five offices and phone lines between them.
There are different ways of organizing. We are going to analyze two extremes.

####### Highly available (AP)

Each of the offices can take new data from people and at the end of the day,
they will share the information they received with all the other offices.

This could be a problem since it may allow invalid data, for example if a
person is registered as dead in one office and the married in another one.
If there was a single office, this would never happen since that person's
registry will be kept up to date, but now we are allowing up to one day of
stale information.

Other possible problem is what happens if one office suffers an accident or a
natural disaster and some of its data from the day is lost. People who already
left the office do not know the Registry lost it and will run into a problem
in the future.

###### Highly consistent (CP)

In this other approach, any data change needs to be coordinated by all the
offices. This way, all the data is always valid, available in every office,
and no single one is responsible for its durability.

Problems may appear when the phone network becomes unreliable. If a single
office phone is broken, all offices will stop working.

##### Properties

It is said that a distributed database can only be highly available or highly
consistent. Different balances between both can be achieved, as a compromise,
for different use cases.
