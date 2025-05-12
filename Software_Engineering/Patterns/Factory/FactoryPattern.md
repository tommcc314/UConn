## Factory Pattern

A factory excels at generating instances of an interface, usually implemented by multiple classes. In this example, we have three different types of users: Readers, Contributors and FullUsers. Each has different permissions which must be set. The Factory creates the appropriate user based on input and returns a user of the desired type.