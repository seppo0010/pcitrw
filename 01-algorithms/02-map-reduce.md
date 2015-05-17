### Map/Reduce

#### Example

##### Elections

When a small group of people want to have an election where the vote is secret,
each will write down their desired output, gather all together, shuffle and
count the matching results.

This algorithm does not scale up well, since a big group of people will take a
long time to cast all votes and count them. Luckily, this is a problem that has
already been solved by modern democratic states: they divide the people in
groups, each group will cast their votes, a group member will count the results
and summarize them in a single sheet of paper. All those sheets of paper are
then submitted to a central person who adds up the votes to find the winner.

The act of counting each individual vote and write down a summary is called
"map", while making an overall summary of all summaries is called "reduce".

#### Properties

The benefit of map/reduce is to divide a big problem into smaller ones that can
be parallelized.
