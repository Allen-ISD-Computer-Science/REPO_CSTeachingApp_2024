# Introduction to Object Oriented Programming (OOP)

<br>

OOP otherwise known as Object Oriented Programming is a programming paradigm (model) based on a concept called Objects.

<br>

*We will be using OOP to refer to Object Oriented Programming in this lesson.*

<br>

Prior to this lesson we used a different programming paradigm called procedural programming where data is stored individually in an unorganized manner.

<br>

This could potentially create a massive headache for developors working on larger projects.

<br>

## The basics of OOP

<br>

There are four basic concepts that pertain to objects.

<br>

1. Properties
2. Methods
3. Inheritence
4. Polymorphism

<br>

### Properties

<br>

Properties are quite simple to understand.

<br>

Properties are the actual data within an object.

<br>

*Another way to think about properties is as the "variables" of the object.*

<br>

```swift
class User {
    var username: String // This is a username property
    var password: String // This is a password property
}
```

<br>

### Methods

<br>

Methods are also quite simple to understand.

<br>

Methods are functions within an object.

<br>

```swift
class User {
    var username: String // This is a username property
    var password: String // This is a password property

    // Init Method
    init(username: String, password: String) {
        self.username = username
        self.password = password
    }

    // Login Method
    func login() {
        print("\(username) has logged in with password \(password)")
        return
    }
}
```

<br>

#### Initialization Methods

<br>

An Initialization method (or "`init` method" for short) is a method to setup an object.

<!-- Add more about Initialization -->

<br>

## Inheritence

<br>

Inheritence allows objects to adopt properties from or even base themselves from another object.

<br>

<img src="/gallery/oop/dog-tree.png" width="512" height="512">

<!--
class User {
    var username: String = "a" // This is a username property
    var password: String = "a" // This is a password property

    /*
    init(username: String, password: String) {
        self.username = username
        self.password = password
    }
    */

    func login() {
        print("\(username) has logged in with password \(String(repeating: "*", count: password.count))")
        return
    }
}


let User1 = User() // (username: "Alice", password: "1234")
let User2 = User() // (username: "Bob", password: "5678")
User1.login()
User2.login()
-->