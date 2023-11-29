# Let's review!

<br>

Based on what you know so far, Write a program that stores these three fruits!
<br>

<img src="/gallery/article/fruits.svg" width="512" height="512">

<br>

~~~swift
var firstFruit: String = "Watermelon"
var secondFruit: String = "Mango"
var thirdFruit: String = "Apple"
~~~

<br>

In this example, variables are used to store these fruits. While this works, it is not practical for the following reasons.

<br>

* **Very Messy**: It's highly repetitive.
* **Zero Flexibility**: You can't add or remove a fruit.
* **Hard to use**: Using this code will be a nightmare.

<br>

# Introduction to Arrays

<br>

An array is a <u>list of related values that are referenced by an index</u> (an index is just a whole number). This provides a convenient way to organize and access multiple elements of the same data type.

<br>

At their core, Arrays are just an abstraction over memory. 

<br>

<img src="/gallery/article/inner.png" width="768" height="768">

<br>

### Notice

<br>

Being that an array index is a whole number, the first element has an index of 0.

<br>

# How to create arrays

<br>

## Specifying Type

<br>

To define an array type in Swift, enclose a type within a pair of square brackets. This enclosed type specifies the only kind of data that the array can hold. It's important to note that this type can be any defined type including array types.

<br>

Here are **SOME** valid examples of array types.

<br>

```swift
[String]       // An array of strings
[Bool]         // An array of booleans
[Int]          // An array of integers
[[Int]]        // An array of arrays of integers
```

<br>

## Instantiating

<br>

To actually create an array use a pair of square brackets and add values in between the two brackets with each value seperated by commas unless it's the last element or the only element. Arrays with no values at all are empty. 

<br>

```swift
[]              // An empty array
[1, 2, 3, 4]    // An array of integers
["Hi", "Bye"]   // An array of strings
```

<br>

# Your first array

<br>

Let's go back to our fruit example.

<br>

Instead of using variables, let's use arrays to represent these fruits.

<br>


```swift
var fruits: [String] = ["Watermelon", "Mango", "Apple"]
```

<br>

Not only does this code look cleaner, It also comes with several other advantages including (but not limited to)

- Being able to add and remove elements
- Being able to see how many elements are present
- Being able to reverse the order of the elements

<br>

# Creating More Arrays

<br>

Imagine a list of animals.               

<br>

* &emsp;&emsp; The entry for the first animal on the list is a <u>Dog</u>.             
* &emsp;&emsp; The entry for the second animal on the list is left <u>blank</u>.         
* &emsp;&emsp; The entry for the third animal on the list is a <u>Cat</u>.             
* &emsp;&emsp; The entry for the fourth animal on the list is also left <u>blank</u>.     

<br>

Let's represent each animal as a <code class="language-swift">String</code> and a blank space as <code class="language-swift">nil</code>. 

<br>

<img src="/gallery/article/array.png" width="256" height="256">

<br>

An array that abides by such representations should look simmlar to the following example.

<br>

~~~swift
let array: [String?] = ["Dog", nil, "Cat", nil]
~~~

<br>

<!--

1. This code is very messy.
2. Adding and Removing new Animals isn't going to be easy.
3. "Iterating" over all the elements will be painful.

<br>
-->

<!-- Add more... -->
