### Atomicity and Isolation

#### Example

##### Bank Transfer

If a bank cashier wants to transfer money between two accounts, there are
actually two operations: subtract the amount from one of the accounts and
add it to the other one.

For these operations to be considered atomic, they need to happen both or
neither. If money is added to one of the accounts, but the subtraction of the
other one fails (for lack of funds, for example) the addition needs to be
canceled.

For them to be considered isolated, nobody else should be able to check out the
balances of the accounts during the operations with one of them executed
and the other one not. Results must be available altogether.
