## Consistency

### Example

#### Civil Registry

A civil registry keeps records of citizen's vital events like births, marriages
and deaths.

To define the Civil Registry as a consistent database, we need to make sure
of the following:

* Data inserted is always valid. For example, nobody can die more than once,
and only people who was born can get married.

* Any data that is written, will be stored and available when reading
afterwards. No sheet can be lost or ignored.

We can say instead it is eventually consistent if we loosen the immediacy of
the availability of written data. For example, if we have different offices
where the events can be registered, a birth that is written in one may not be
known in the other office until they eventually sync up. This must happen at
some point, but its frequency can be arbitrarily set.
