# Reference and Value Types 

<br>

Before we get into any particular type, We need to discuss the two different classes of types.

<br>

- **Value types** store the value as it is. 
- **Reference types** store the memory address of where the value is. 

<br>

# Basic Types

<br>

## Integers

<img src="/gallery/types/Integers.svg">

<br>

Integers are just **whole numbers** and are **value types**.

<br>

In Swift, you can create an integer with the type <code class="language-swift">Int</code> type.

<br>

### Unsigned Integers

<br>

Swift allows you to compromise negative numbers for more positive numbers.

<br>

These are called Unsigned Integers and declared with the <code class="language-swift">UInt</code> type.

<br>

### Integer Bit-lengths

<br>

The Standard <code class="language-swift">Int</code> type has the same bit-length as your CPU. Which will either be 32 or 64 bits long.

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

Floating Point numbers have restricted/fixed decimal points which can lead to some unusal equation calculations especially so with the <code class="language-swift">Float</code> type.

<br>

Thus, It is **recommended that you use <code class="language-swift">Double</code>** when using floating point numbers. 

<br>

```swift
Float  // Floating Point numbers (precision of at least 6 decimal digits)
Double // Floating Point numbers (precision of at least 15 decimal digits)
```

<br>

### Confusing thing about Floats

<br>

Although <code class="language-swift">8</code> is an integer, <code class="language-swift">8.0</code> is a Float, despite both <code class="language-swift">8</code> and <code class="language-swift">8.0</code> being mathmatically equivlent. 