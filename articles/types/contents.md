# Reference and Value Types 

<br>

Before we get into any particular type, We need to discuss the two different classes of types.

<br>

- **Value types** store the value as it is. This means that when you assign a value type to a variable, a copy of the value is made 
- **Reference types** store the memory address of where the value is. This means when you work with a reference type, assigning it to a variable doesn't create a new copy of the value, but instead it points to the original values location in memory.

<br>

# Basic Types

<br>

## Integers

<img src="/gallery/types/Integers.svg">

<br>

Integers are **whole numbers**. They are categorized as **value types** in swift you create an integer using the **Int** type.

<br>

In Swift, you can create an integer with the type <code class="language-swift">Int</code> type.

<br>

### Unsigned Integers

<br>

Swift allows you to represent negative numbers as positive numbers when using unsigned integer types. This means that you can use unsigned integers to store values that would normally be considered negative, treating them as positive values. These are declared using the **UInt** type.
<br>

These are called Unsigned Integers and declared with the <code class="language-swift">UInt</code> type.

<br>

### Integer Bit-lengths

<br>

The Standard <code class="language-swift">Int</code> type has the same bit-length as your CPU. Which will usually be either be 32 or 64 bits long.

<br>

However, You can have Integers with different bit-lengths with the following types. Even if it's bigger than the CPUs bit-length.

<br>

```swift
Int8  // Integers (min: –128, max: 127)
Int16 // Integers (min: –32768, max: 32767)
Int32 // Integers (min: –2147483648, max: 2147483647)
Int64 // Integers (min: -9223372036854775808, max: 9223372036854775807)
```

<br>

Like the <code class="language-swift">Int</code> type, The <code class="language-swift">UInt</code> type has the same bit-length as your CPU. Which will either be 32 or 64 bits long.

<br>

```swift
UInt8   // Unsigned Integers (min: 0, max: 255)
UInt16  // Unsigned Integers (min: 0, max: 65535)
UInt32  // Unsigned Integers (min: 0, max: 4294967295)
UInt64  // Unsigned Integers (min: 0, max: 18446744073709551615)
```

<br>

## Floats

<br>

Floating Point numbers are **decimal numbers** and are **value types**.

<br>

Floating Point numbers in Swift can be represented by two types: <code class="language-swift">Float</code> (small) and <code class="language-swift">Double</code> (large).

<br>

Floating Point numbers have restricted/fixed decimal points which can lead to some unusual equation calculations especially with the <code class="language-swift">Float</code> type.

<br>

It is **recommended that you use <code class="language-swift">Double</code>** when using floating point numbers. 

<br>

```swift
Float  // Floating Point numbers (precision of at least 6 decimal digits)
Double // Floating Point numbers (precision of at least 15 decimal digits)
```

<br>

### Confusing thing about Floats

<br>

Although <code class="language-swift">8</code> is an integer, when writen as <code class="language-swift">8.0</code> it is a Float, despite both <code class="language-swift">8</code> and <code class="language-swift">8.0</code> both being mathematically equivalent. 

<br>

### Strings

<br>

**Strings in Swift:**

Strings are a very important and fundamental data type in Swift. It is used to represent groups of characters. They can contain **Letters**, **Numbers**, **Symbols**, and **Emojis**


Strings can be created by using **Double Quotes**  <code class="language-swift">(" ")</code> or **Triple quotes** <code class="language-swift">(""" """)</code>
These strings can be assigned to variables by using the keywords **let** and **var**

Example of Strings being assigned to variables:
```swift
let greeting = "Hello, World!"
var name = "John"
```

<br>


### Booleans

<br>

Booleans are data types that represent  <code class="language-swift">true</code> or  <code class="language-swift">false</code> values. These are Value types, meaning that when you assign a Boolean to a variable, a copy of the value is made.


In Swift, you create a Boolean using the type **Bool**

Example of Booleans usage: 
```swift
let isTrue: Bool = true
let isFalse: Bool = false
```

<br>