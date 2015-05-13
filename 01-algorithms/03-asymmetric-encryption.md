### Asymmetric Encryption

#### Example

##### Coffers and keys

Before the telegraph was created, the only way to transmit a message was to
send an object with the message. The question is how to make sure nobody except
the recipient reads the message. If the sender can agree with them in advance,
they can give them a key to a coffer, and then send a message inside the
coffer. We will assume the coffer cannot be opened without the key.

Now there is a post office that keeps open coffers whose keys belong to anyone
interested in receiving messages. When a person wants to send a private
message, they will ask the library for a coffer. Now they will include their
message in that coffer, and inside it another coffer, to which they own the
key, open. The recipient can now reply privately in this second coffer.

#### Properties

With this system, anyone can establish a secure connection with anyone
registered in the library, or if they can somehow make a secure connection
once, temporarily.
