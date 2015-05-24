### Atomicity and Isolation

#### Example

##### Bank Transfer

If a banker wants to move money between two accounts, there are
actually two operations: take the amount from one of the accounts and
add it to the other one.

For these operations to be considered atomic, they need to happen both or
none of them. If money is added to one of the accounts, but the reduction in the
other one does not go through (not enough funds, for example) the first
operation needs to be taken back.

For them to be considered isolated, nobody else should be able to check out the
balances of the accounts after one operation but before the another one.
Results must be available as one.
