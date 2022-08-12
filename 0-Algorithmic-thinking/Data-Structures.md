<<<[[Big-O-Notation]] | [[Logarithms]]>>>
--|--
# Data Structures for Coding Interviews

## Computer science in plain English

To really understand how data structures _work_, we're going to derive each of them from scratch. Starting with bits.

Don't worry—we'll skip the convoluted academic jargon and proofs.

We'll cover:
-   [[Data-Structures#Random Access Memory RAM|Random Access Memory]]
-   [[Data-Structures#Binary numbers|Binary Numbers]]
-   [[Data-Structures#Fixed-width integers |Fixed-Width Integers]]
-   [[Data-Structures#Arrays|Arrays]]
-   [[Data-Structures#Strings|Strings]]
-   [[Data-Structures#Pointers|Pointers]]
-   [[Data-Structures#Dynamic arrays|Dynamic arrays]]
-   [[Data-Structures#Linked lists|Linked lists]]
-   [[Data-Structures#Hash tables|Hash tables]]

## Random Access Memory (RAM)
---

When a computer is running code, it needs to keep track of _variables_ (numbers, strings, arrays, etc.).

Variables are stored in **random access memory** (**RAM**). We sometimes call RAM "working memory" or just "memory."

>RAM is _not_ where mp3s and apps get stored. In addition to "memory," your computer has **storage** (sometimes called "persistent storage" or "disk"). While _memory_ is where we keep the variables our functions allocate as they crunch data for us, _storage_ is where we keep _files_ like mp3s, videos, Word documents, and even executable programs or apps.
>
>Memory (or RAM) is faster but has less space, while storage (or "disk") is slower but has more space. A modern laptop might have ~500GB of storage but only ~16GB of RAM.

Think of RAM like a really tall bookcase with a _lot_ of shelves. Like, _billions_ of shelves.

![A column of empty RAM slots.](https://www.interviewcake.com/images/svgs/cs_for_hackers__ram_empty_no_indices.svg?bust=210)

> It just keeps going down. Again, picture _billions_ of these shelves.

The shelves are numbered.

![A column of empty RAM slots with indices.](https://www.interviewcake.com/images/svgs/cs_for_hackers__ram_empty_with_indices.svg?bust=210)

We call a shelf's number its **address**.

Each shelf holds 8 **bits**. A _bit_ is a tiny electrical switch that can be turned "on" or "off." But instead of calling it "on" or "off" we call it 1 or 0.

![A column of RAM slots filled with various bits that make up bytes.](https://www.interviewcake.com/images/svgs/cs_for_hackers__ram_bits.svg?bust=210)

8 bits is called a **byte**. So each shelf has one byte (8 bits) of storage.

Of course, we also have a processor that does all the real work inside our computer:

![A section of RAM connected to the computer's processor, which does most of the heavy lifting.](https://www.interviewcake.com/images/svgs/cs_for_hackers__ram_processor.svg?bust=210)

It's connected to a **memory controller**. The memory controller does the actual reading and writing to and from RAM. It has a _direct connection_ to each shelf of RAM.

![The computer's processor connected to a memory controller, which does the actual reading and writing to and from RAM.](https://www.interviewcake.com/images/svgs/cs_for_hackers__ram_memory_controller.svg?bust=210)

That _direct connection_ is important. It means we can access address 0 and then immediately access address 918,873 without having to "climb down" our massive bookshelf of RAM.

That's why we call it Random Access Memory (RAM)—we can _Access_ the bits at any _Random_ address in _Memory_ right away.

> Spinning hard drives don't have this "random access" superpower, because there's no direct connection to each byte on the disk. Instead, there's a reader—called a **head**—that moves along the surface of a spinning storage disk (like the needle on a record player). Reading bytes that are far apart takes longer because you have to wait for the head to physically move along the disk.

Even though the memory controller can jump between far-apart memory addresses quickly, programs _tend to_ access memory that's nearby. **So computers are tuned to get an extra speed boost when reading memory addresses that're close to each other**. Here's how it works:

The processor has a **cache** where it stores a copy of stuff it's recently read from RAM.

![A series of caches inside of the memory controller, where the processor stores what it has recently read from RAM.](https://www.interviewcake.com/images/svgs/cs_for_hackers__ram_cache.svg?bust=210)

> Actually, it has a _series_ of caches. But we can picture them all lumped together as one cache like this.

This cache is much faster to read from than RAM, so the processor saves time whenever it can read something from cache instead of going out to RAM.

**When the processor asks for the contents of a given memory address, the memory controller _also_ sends the contents of a handful of _nearby_ memory addresses.** And the processor puts _all_ of it in the cache.

So if the processor asks for the contents of address 951, then 952, then 953, then 954...it'll go out to RAM once for that first read, and the subsequent reads will come straight from the super-fast cache.

But if the processor asks to read address 951, then address 362, then address 419...then the cache won't help, and it'll have to go all the way out to RAM for each read.

So reading from sequential memory addresses is faster than jumping around.

## Binary numbers
---

Let's put those bits to use. Let's store some stuff. Starting with numbers.

The number system we usually use (the one you probably learned in elementary school) is called **base 10**, because each digit has _ten_ possible values (1, 2, 3, 4, 5, 6, 7, 8, 9, and 0).

But computers don't have digits with ten possible values. They have _bits_ with _two_ possible values. So they use **base 2** numbers.

Base 10 is also called **decimal**. Base 2 is also called **binary**.

To understand binary, let's take a closer look at how decimal numbers work. Take the number "101" in decimal:

![In base 10, the digits 101 represent 1 hundred, 0 tens, and 1 one.](https://www.interviewcake.com/images/svgs/cs_for_hackers__binary_numbers_base_10_101.svg?bust=210)

Notice we have two "1"s here, but they don't _mean_ the same thing. The leftmost "1" _means_ 100, and the rightmost "1" _means_ 1. That's because the leftmost "1" is in the hundreds place, while the rightmost "1" is in the ones place. And the "0" between them is in the tens place.

![In base 10, the digits 101 represent 1 hundred, 0 tens, and 1 one.](https://www.interviewcake.com/images/svgs/cs_for_hackers__binary_numbers_base_10_digits.svg?bust=210)

**So this "101" in base 10 is telling us we have "1 hundred, 0 tens, and 1 one."**

![In base 10, the digits 101 represent 1 hundred, 0 tens, and 1 one, which add to give the value one hundred and one.](https://www.interviewcake.com/images/svgs/cs_for_hackers__binary_numbers_base_10.svg?bust=210)

Notice how the _places_ in base 10 (ones place, tens place, hundreds place, etc.) are _sequential powers of 10_:

-   10^0=1100=1
-   10^1=10101=10
-   10^2=100102=100
-   10^3=1000103=1000
-   etc.

**The places in _binary_ (base 2) are sequential powers of _2_:**

-   2^0=120=1
-   2^1=221=2
-   2^2=422=4
-   2^3=823=8
-   etc.

So let's take that same "101" but this time let's read it as a _binary_ number:

![In base 2, the digits 101 represent 1 four, 0 twos, and 1 one.](https://www.interviewcake.com/images/svgs/cs_for_hackers__binary_numbers_base_2_digits.svg?bust=210)

Reading this from right to left: we have a 1 in the ones place, a 0 in the twos place, and a 1 in the fours place. So our total is 4 + 0 + 1 which is 5.

![In base 2, the digits 101 represent 1 four, 0 twos, and 1 one, which add to give the value five.](https://www.interviewcake.com/images/svgs/cs_for_hackers__binary_numbers_base_2.svg?bust=210)

Here's how we'd count up to 12 in binary:

**Decimal**|**Binary**
--|--
0|0000
1|0001
2|0010
3|0011
4|0100
5|0101
6|0110
7|0111
8|1000
9|1001
10|1010
11|1011
12|1100

So far we've been talking about **unsigned integers** ("unsigned" means non-negative, and "integer" means a whole number, not a fraction or decimal). Storing other numbers isn't hard though. Here's how some other numbers _could_ be stored:

**Fractions:** Store _two_ numbers: the numerator and the denominator.

**Decimals:** Also two numbers: 1) the number with the decimal point taken out, and 2) the _position_ where the decimal point goes (how many digits over from the leftmost digit).

**Negative Numbers:** Reserve the leftmost bit for expressing the sign of the number. 0 for positive and 1 for negative.

In reality we usually do something slightly fancier for each of these. But these approaches _work_, and they show how we can express some complex stuff with just 1s and 0s.

>We've talked about base 10 and base 2...you may have also seen **base 16**, also called **hexadecimal** or **hex**.
>
>In hex, our possible values for each digit are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, and f. Hex numbers are often prefixed with "0x" or "#".
>
>In CSS, colors are sometimes expressed in hex. Interview Cake's signature blue color is "#5bc0de".

## Fixed-width integers
---

How many different numbers can we express with 1 byte (8 bits)?

2^8=25628=256 different numbers. _How did we know to take 2^828?_ ↴

>What happens if we have the number 255 in an 8-bit unsigned integer (1111 1111 in binary) and we add 1? The answer (256) needs a 9th bit (1 0000 0000). But we only have 8 bits!
>
>This is called an **integer overflow**. At best, we might just get an error. At worst, our computer might compute the correct answer but then just throw out the 9th bit, giving us _zero_ (0000 0000) instead of 256 (1 0000 0000)! (Python actually notices that the result won't fit and automatically allocates more bits to store the larger number.)

The 256 possibilities we get with 1 byte are pretty limiting. So **we usually use 4 or 8 bytes (32 or 64 bits) for storing integers**.

-   32-bit integers have 2^{32}232 possible values—more than _4 billion_
-   64-bit integers have 2^{64}264 possible values—more than _10 billion billion_ (10^{19}1019).

> **"How come I've never had to think about how many bits my integers are?"** Maybe you _have_ but just didn't know it.
> 
> Have you ever noticed how in some languages (like Java and C) sometimes numbers are Integers and sometimes they're Longs? The difference is the number of bits (in Java, Integers are 32 bits and Longs are 64).
> 
> Ever created a table in SQL? When you specify that a column will hold integers, you have to specify how many bytes: 1 byte (tinyint), 2 bytes (smallint), 4 bytes (int), or 8 bytes (bigint).

>**When is 32 bits not enough? When you're counting views on a viral video**. YouTube famously ran into trouble when the Gangnam Style video hit over 2^{31}231 views, [forcing them to upgrade their view counts from 32-bit to 64-bit signed integers](http://arstechnica.com/business/2014/12/gangnam-style-overflows-int_max-forces-youtube-to-go-64-bit/).

Most integers are **fixed-width** or **fixed-length**, which means the number of bits they take up doesn't change.

It's usually safe to assume an integer is fixed-width unless you're told otherwise. Variable-size numbers _exist_, but they're only used in special cases.

If we have a 64-bit fixed-length integer, it doesn't matter if that integer is 0 or 193,457—it still takes up the same amount of space in RAM: 64 bits.

> **Are you familiar with big O notation?** It's a tool we use for talking about how much time an algorithm takes to run or how much space a data structure takes up in RAM. It's pretty simple:
> 
> **O(1)O(1)** or **constant** means the time or space stays about the same even as the dataset gets bigger and bigger.
> 
> **O(n)O(n)** or **linear** means the time or space grows proportionally as the dataset grows.
> 
> So O(1)O(1) space is much smaller than O(n)O(n) space. And O(1)O(1) _time_ is much faster than O(n)O(n) time.
> 
> That's all you need for this piece. But if you're curious, you can read [our whole big O explainer here](https://www.interviewcake.com/big-o-notation-time-and-space-complexity).

In big O notation, we say **fixed-width integers take up _constant space_ or O(1)O(1) space.**

And _because_ they have a constant number of bits, **most simple operations on fixed-width integers (addition, subtraction, multiplication, division) take constant _time_ (O(1)O(1) time)**.

So fixed-width integers are very space efficient and time efficient.

But that efficiency comes at a cost—_their values are limited_. Specifically, they're limited to 2^n2n possibilities, where nn is the number of bits.

So there's a tradeoff. As we'll see, that's a trend in data structures—to get a nice property, we'll often have to lose something.

## Arrays
---
Ok, so we know how to store individual numbers. Let's talk about storing _several numbers_.

That's right, things are starting to _heat up_.

Suppose we wanted to keep a count of how many bottles of kombucha we drink every day.

Let's store each day's kombucha count in an 8-bit, fixed-width, unsigned integer. That should be plenty—we're not likely to get through more than 256 (2^828) bottles in a _single day_, right?

And let's store the kombucha counts right next to each other in RAM, starting at memory address 0:

![A stack of RAM in which we store kombucha counts starting at index 0.](https://www.interviewcake.com/images/svgs/cs_for_hackers__array_kombucha_counts.svg?bust=210)

Bam. That's an **array**. RAM is _basically_ an array already.

Just like with RAM, the elements of an array are numbered. We call that number the **index** of the array element (plural: indices). In _this_ example, each array element's index is the same as its address in RAM.

But that's not usually true. Suppose another program like Spotify had already stored some information at memory address 2:

![A column of 9 RAM slots representing an array. The row at index 2 is highlighted because it is being used by Spotify.](https://www.interviewcake.com/images/svgs/cs_for_hackers__array5_occupied.svg?bust=210)

We'd have to start our array below it, for example at memory address 3. So index 0 in our array would be at memory address 3, and index 1 would be at memory address 4, etc.:

![A column of 9 RAM slots representing an array. The row at index 2 is highlighted, and the rows at indices 3 through 7 are selected with a bracket.](https://www.interviewcake.com/images/svgs/cs_for_hackers__array5.svg?bust=210)

Suppose we wanted to get the kombucha count at index 4 in our array. How do we figure out what _address in memory_ to go to? Simple math:

Take the array's starting address (3), add the index we're looking for (4), and that's the address of the item we're looking for. 3 + 4 = 7. In general, for getting the nnth item in our array:

\text{address of nth item in array} =address of nth item in array=\text{address of array start} + naddress of array start+n

This works out nicely because the size of the addressed memory slots and the size of each kombucha count are _both_ 1 byte. So a slot in our array corresponds to a slot in RAM.

But that's not always the case. In fact, it's _usually not_ the case. We _usually_ use _64-bit_ integers.

So how do we build an array of _64-bit_ (8 byte) integers on top of our _8-bit_ (1 byte) memory slots?

We simply give each array index _8_ address slots instead of 1:

![A column of RAM slots representing an array of 64-bit integers. Every 8 buckets of RAM represents one integer.](https://www.interviewcake.com/images/svgs/cs_for_hackers__array64_long.svg?bust=210)

So we can still use simple math to grab the start of the nthnth item in our array—just gotta throw in some multiplication:

\text{address of nth item in array} =address of nth item in array=\text{address of array start} + (n * \text{size of each item in bytes})address of array start+(n∗size of each item in bytes)

Don't worry—adding this multiplication doesn't really slow us down. Remember: addition, subtraction, multiplication, and division of fixed-width integers takes O(1)O(1) time. So _all_ the math we're using here to get the address of the nnth item in the array takes O(1)O(1) time.

And remember how we said the memory controller has a _direct connection_ to each slot in RAM? That means we can read the stuff at any given memory address in O(1)O(1) time.

![A memory controller connected to a section of RAM.](https://www.interviewcake.com/images/svgs/cs_for_hackers__arrays_no_processor_ram_memory_controller.svg?bust=210)

**Together, this means looking up the contents of a given array index is O(1)O(1) time.** This fast lookup capability is the most important property of arrays.

But the formula we used to get the address of the nnth item in our array only works _if_:

1.  **Each item in the array is the _same size_** (takes up the same number of bytes).
2.  **The array is _uninterrupted_ (contiguous) in memory**. There can't be any gaps in the array...like to "skip over" a memory slot Spotify was already using.

These things make our formula for finding the nnth item _work_ because they make our array _predictable_. We can _predict_ exactly where in memory the nnth element of our array will be.

But they also constrain what kinds of things we can put in an array. Every item has to be the same size. And if our array is going to store a _lot_ of stuff, we'll need a _bunch_ of uninterrupted free space in RAM. Which gets hard when most of our RAM is already occupied by other programs (like Spotify).

That's the tradeoff. Arrays have fast lookups (O(1)O(1) time), but each item in the array needs to be the same size, and you need a big block of uninterrupted free memory to store the array.

## Strings
---

Okay, let's store some words.

A series of _characters_ (letters, punctuation, etc.) is called a **string**.

We already know one way to store a _series of things_—arrays. But how can an array store _characters_ instead of numbers?

Easy. Let's define a mapping between numbers and characters. Let's say "A" is 1 (or 0000 0001 in binary), "B" is 2 (or 0000 0010 in binary), etc. Bam. Now we have characters.

This mapping of numbers to characters is called a **character encoding**. One common character encoding is "ASCII". Here's how the alphabet is encoded in ASCII:
![[Pasted image 20220812123418.png]]
You get the idea. So since we can express characters as 8-bit integers, we can express _strings_ as _arrays_ of 8-bit numbers characters.

![Three illustrations of the string "NICE": one in binary, one in base 10, and one in ASCII.](https://www.interviewcake.com/images/svgs/cs_for_hackers__strings_nice_array.svg?bust=210)

## Pointers
---
Remember how we said every item in an array had to be the same size? Let's dig into that a little more.

Suppose we wanted to store a bunch of ideas for baby names. Because we've got some _really_ cute ones.

Each name is a string. Which is really an array. And now we want to store _those arrays_ in an array. _Whoa_.

Now, what if our baby names have different lengths? That'd violate our rule that all the items in an array need to be the same size!

We could put our baby names in arbitrarily large arrays (say, 13 characters each), and just use a special character to mark the end of the string within each array...

![Strings represented in RAM as arrays of 13 characters, with the end of the strings being denoted by a special "null" character. The last 8 rows are marked as wasted space because the name Bill (along with the null character) only takes up 5 out of 13 available characters.](https://www.interviewcake.com/images/svgs/cs_for_hackers__pointers_baby_names.svg?bust=210)

>"Wigglesworth" is a cute baby name, right?

But look at all that wasted space after "Bill". And what if we wanted to store a string that was _more_ than 13 characters? We'd be out of luck.

There's a better way. Instead of storing the strings right inside our array, let's just put the strings wherever we can fit them in memory. Then we'll have each element in our array hold the _address in memory_ of its corresponding string. Each address is an integer, so really our outer array is just an array of integers. We can call each of these integers a **pointer**, since it points to another spot in memory.

![An array of names represented in RAM. The names are stored out of order, but an array holds the address in memory of each of name with arrows pointing from the number to the memory address.](https://www.interviewcake.com/images/svgs/cs_for_hackers__pointers_pointer_array.svg?bust=210)

>The pointers are marked with a * at the beginning.

Pretty clever, right? This fixes _both_ the disadvantages of arrays:

1.  The items don't have to be the same length—each string can be as long or as short as we want.
2.  We don't need enough uninterrupted free memory to store all our strings next to each other—we can place each of them separately, wherever there's space in RAM.

We fixed it! No more tradeoffs. Right?

Nope. Now we have a _new_ tradeoff:

Remember how the memory controller sends the contents of _nearby_ memory addresses to the processor with each read? And the processor caches them? So reading sequential addresses in RAM is _faster_ because we can get most of those reads right from the cache?

![A series of caches inside of the memory controller, where the processor stores what it has recently read from RAM.](https://www.interviewcake.com/images/svgs/cs_for_hackers__ram_cache.svg?bust=210)

Our original array was very **cache-friendly**, because everything was sequential. So reading from the 0th index, then the 1st index, then the 2nd, etc. got an extra speedup from the processor cache.

**But the pointers in this array make it _not_ cache-friendly**, because the baby names are scattered randomly around RAM. So reading from the 0th index, then the 1st index, etc. doesn't get that extra speedup from the cache.

That's the tradeoff. This pointer-based array requires less uninterrupted memory and can accommodate elements that aren't all the same size, _but_ it's _slower_ because it's not cache-friendly.

>This slowdown isn't reflected in the big O time cost. Lookups in this pointer-based array are _still_ O(1)O(1) time.

## Dynamic arrays
---

Let's build a very simple word processor. What data structure should we use to store the text as our user writes it?

Strings are stored as arrays, right? So we should use an array?

Here's where that gets tricky: **when we allocate an array in a low-level language like C or Java, we have to specify upfront _how many indices_ we want our array to have.**

There's a reason for this—the computer has to reserve space in memory for the array and commit to not letting anything else use that space. We can't have some other program overwriting the elements in our array!

The computer can't reserve _all_ its memory for a single array. So we have to tell it how much to reserve.

But for our word processor, we don't know ahead of time how long the user's document is going to be! So what can we do?

Just make an array and program it to resize itself when it runs out of space! This is called a **dynamic array**, and it's built on top of a normal array.

>Python, Ruby, and JavaScript use dynamic arrays for their default array-like data structures. In Python, they're called "lists." Other languages have both. For example, in Java, array is a static array (whose size we have to define ahead of time) and ArrayList is a dynamic array.

Here's how it works:

When you allocate a dynamic array, your dynamic array implementation makes an _underlying static array_. The starting size depends on the implementation—let's say our implementation uses 10 indices:

![A blank dynamic array created by default with 10 indices.](https://www.interviewcake.com/images/svgs/cs_for_hackers__dynamic_arrays_10_indices.svg?bust=210)

Say you append 4 items to your dynamic array:

![The same dynamic array storing the word "Dear."](https://www.interviewcake.com/images/svgs/cs_for_hackers__dynamic_arrays_dear.svg?bust=210)

At this point, our dynamic array contains 4 items. It has a length of 4. But the _underlying array_ has a length of 10.

We'd say this dynamic array's **size** is 4 and its **capacity** is 10.

![Our dynamic array now has a size of 4 and a capacity of 10.](https://www.interviewcake.com/images/svgs/cs_for_hackers__dynamic_arrays_size_and_capacity.svg?bust=210)

The dynamic array stores an end_index to keep track of where the dynamic array ends and the extra capacity begins.

![The end_index of our dynamic array is marked at index 3, where the last letter of the word "Dear" is stored.](https://www.interviewcake.com/images/svgs/cs_for_hackers__dynamic_arrays_end_index.svg?bust=210)

If you keep appending, at some point you'll use up the full capacity of the underlying array:

![After adding 6 characters to form the string "Dear Mothe," the end_index of our dynamic array is now marked at index 9, meaning the dynamic array is full.](https://www.interviewcake.com/images/svgs/cs_for_hackers__dynamic_arrays_array_sweatin.svg?bust=210)

Next time you append, the dynamic array implementation will do a few things under the hood to make it work:

**1. Make a new, bigger array.** Usually twice as big.

Why not just _extend_ the existing array? Because that memory might already be taken. Say we have Spotify open and it's using a handful of memory addresses right after the end of our old array. We'll have to skip that memory and reserve the next 20 uninterrupted memory slots for our new array:

![A new dynamic array, twice as big as the old dynamic array, is created in order to make more room.](https://www.interviewcake.com/images/svgs/cs_for_hackers__dynamic_arrays_new_array.svg?bust=210)

**2. Copy _each_ element from the old array into the new array.**

![Each element from the old dynamic array is copied into the new dynamic array.](https://www.interviewcake.com/images/svgs/cs_for_hackers__dynamic_arrays_copy_array.svg?bust=210)

**3. Free up the old array.** This tells the operating system, "you can use this memory for something else now."

![The old array is forgotten because it is no longer necessary.](https://www.interviewcake.com/images/svgs/cs_for_hackers__dynamic_arrays_free_old_array.svg?bust=210)

**4. Append your new item.**

![The new element, the letter "r," is finally appended to our new array.](https://www.interviewcake.com/images/svgs/cs_for_hackers__dynamic_arrays_append_item.svg?bust=210)

We could call these special appends "doubling" appends since they require us to make a new array that's (usually) double the size of the old one.

Appending an item to an array is usually an O(1)O(1) time operation, but **a single doubling append is an O(n)O(n) time operation since we have to copy all nn items from our array.**

Does that mean an append operation on a dynamic array is always worst-case O(n)O(n) time? Yes. So if we make an empty dynamic array and append nn items, that has some crazy time cost like O(n^2)O(n2) or O(n!)O(n!)?!?! Not quite.

While the time cost of each special O(n)O(n) doubling append _doubles_ each time, the _number of O(1)O(1) appends_ you get until the _next doubling_ append _also_ doubles. This kind of "cancels out," and we can say each append has an _average_ cost or **amortized cost** of O(1)O(1). ↴

Given this, in industry we usually wave our hands and say dynamic arrays have a time cost of O(1)O(1) for appends, even though strictly speaking that's only true for the _average_ case or the _amortized_ cost.

In an interview, if we were worried about that O(n)O(n)-time worst-case cost of appends, we might try to use a normal, non-dynamic array.

**The _advantage_ of dynamic arrays over arrays is that you don't have to specify the size ahead of time, but the _disadvantage_ is that some appends can be expensive**. That's the tradeoff.

But what if we wanted the best of both worlds...

## Linked lists
---
Our word processor is definitely going to need fast appends—appending to the document is like the _main thing_ you do with a word processor.

Can we build a data structure that can store a string, has fast appends, _and_ doesn't require you to say how long the string will be ahead of time?

Let's focus first on not having to know the length of our string ahead of time. Remember how we used _pointers_ to get around length issues with our array of baby names?

What if we pushed that idea even further?

What if each _character_ in our string were a _two-index array_ with:

1.  the character itself
2.  a pointer to the next character

![An example of a linked list storing the string "DEAR." Each element of the linked list is an array composed of two items: a character and a pointer that points to the next element.](https://www.interviewcake.com/images/svgs/cs_for_hackers__linked_lists_sample.svg?bust=210)

We would call each of these two-item arrays a **node** and we'd call this series of nodes a **linked list**.

Here's how we'd actually implement it in memory:

![The same linked list represented in RAM, showing the nodes scattered in memory but connected by pointers.](https://www.interviewcake.com/images/svgs/cs_for_hackers__linked_lists_in_memory.svg?bust=210)

Notice how we're free to store our nodes wherever we can find two open slots in memory. They don't have to be next to each other. They don't even have to be _in order_:

![The same linked list represented in RAM. This time the characters are stored out of order to show that the pointers still keep everything in place.](https://www.interviewcake.com/images/svgs/cs_for_hackers__linked_lists_in_memory_out_of_order.svg?bust=210)

>"But that's not cache-friendly," you may be thinking. Good point! We'll get to that.

The first node of a linked list is called the **head**, and the last node is usually called the **tail**.

>Confusingly, some people prefer to use "tail" to refer to _everything after the head_ of a linked list. In an interview it's fine to use either definition. Briefly say which definition you're using, just to be clear.

It's important to have a pointer variable referencing the head of the list—otherwise we'd be unable to find our way back to the start of the list!

We'll also sometimes keep a pointer to the tail. That comes in handy when we want to add something new to the end of the linked list. In fact, let's try that out:

Suppose we had the string "LOG" stored in a linked list:

![A linked list with head and tail pointers storing the word "LOG." The *head points to the first character "L," and the tail points to the last letter "G."](https://www.interviewcake.com/images/svgs/cs_for_hackers__linked_lists_log_string.svg?bust=210)

Suppose we wanted to add an "S" to the end, to make it "LOGS". How would we do that?

Easy. We just put it in a new node:

![A linked list with head and tail pointers storing the word "LOG." A new unconnected node storing the character "S" is added to the bottom and bolded.](https://www.interviewcake.com/images/svgs/cs_for_hackers__linked_lists_log_string_add_node.svg?bust=210)

And tweak some pointers:

1. Grab the last letter, which is "G". Our tail pointer lets us do this in O(1)O(1) time.

![A linked list with head and tail pointers storing the word "LOG." The *tail pointer and the character "G" are bolded.](https://www.interviewcake.com/images/svgs/cs_for_hackers__linked_lists_logs_string_grab_last_letter.svg?bust=210)

2. Point the last letter's next to the letter we're appending ("S").

![A linked list with head and tail pointers storing the word "LOG." The "G"'s *next pointer is bolded and pointing to the appended "S".](https://www.interviewcake.com/images/svgs/cs_for_hackers__linked_lists_logs_string_point_next.svg?bust=210)

3. Update the tail pointer to point to our _new_ last letter, "S".

![A linked list with head and tail pointers storing the word "LOGS." The *tail pointer is now pointed to the new last letter: "S".](https://www.interviewcake.com/images/svgs/cs_for_hackers__linked_lists_logs_string_tweak_pointers.svg?bust=210)

That's O(1)O(1) time.

>Why is it O(1)O(1) time? Because the runtime doesn't get bigger if the string gets bigger. No matter how many characters are in our string, we still just have to tweak a couple pointers for any append.

Now, what if instead of a linked list, our string had been a _dynamic array_? We might not have any room at the end, forcing us to do one of those doubling operations to make space:

![A dynamic array containing the word "LOG" going through a doubling operation to make space for an appended letter.](https://www.interviewcake.com/images/svgs/cs_for_hackers__linked_lists_log_string_doubled_array.svg?bust=210)

So with a dynamic array, our append would have a _worst-case_ time cost of O(n)O(n).

**Linked lists have worst-case O(1)O(1)-time appends, which is better than the worst-case O(n)O(n) time of dynamic arrays.**

>That _worst-case_ part is important. The _average case_ runtime for appends to linked lists and dynamic arrays is the same: O(1)O(1).

Now, what if we wanted to _pre_pend something to our string? Let's say we wanted to put a "B" at the beginning.

For our linked list, it's just as easy as appending. Create the node:

![A linked list with head and tail pointers storing the word "LOGS." A new unconnected node storing the character "B" is added to the top and bolded.](https://www.interviewcake.com/images/svgs/cs_for_hackers__linked_lists_logs_string_add_node.svg?bust=210)

And tweak some pointers:

1.  Point "B"'s next to "L".
2.  Point the head to "B".

![A linked list with head and tail pointers storing the word "LOGS." The "B"'s *next pointer is bolded and pointing to the letter "L," and the *head pointer is bolded and pointing to the prepended letter "B".](https://www.interviewcake.com/images/svgs/cs_for_hackers__linked_lists_blogs_string_tweak_pointers.svg?bust=210)

Bam. O(1)O(1) time again.

But if our string were a _dynamic array_...

![A dynamic array storing the string "LOGS."](https://www.interviewcake.com/images/svgs/cs_for_hackers__linked_lists_log_string_dynamic_array.svg?bust=210)

And we wanted to add in that "B":

![A dynamic array storing the string "LOGS." A bolded "B" is added above the array.](https://www.interviewcake.com/images/svgs/cs_for_hackers__linked_lists_log_string_dynamic_array_add_b.svg?bust=210)

Eep. We have to _make room_ for the "B"!

We have to move _each character_ one space down:

![A dynamic array storing the string "LOGS" with the letter "B" floating above. The "S" is bolded with an arrow attached showing how the character is being moved one index up.](https://www.interviewcake.com/images/svgs/cs_for_hackers__linked_lists_log_string_dynamic_array_move_s.svg?bust=210)

![A dynamic array storing the string "LOGS" with the letter "B" floating above. The "G" is bolded with an arrow attached showing how the character is being moved one index up.](https://www.interviewcake.com/images/svgs/cs_for_hackers__linked_lists_log_string_dynamic_array_move_g.svg?bust=210)

![A dynamic array storing the string "LOGS" with the letter "B" floating above. The "O" is bolded with an arrow attached showing how the character is being moved one index up.](https://www.interviewcake.com/images/svgs/cs_for_hackers__linked_lists_log_string_dynamic_array_move_o.svg?bust=210)

![A dynamic array storing the string "LOGS" with the letter "B" floating above. The "L" is bolded with an arrow attached showing how the character is being moved one index up.](https://www.interviewcake.com/images/svgs/cs_for_hackers__linked_lists_log_string_dynamic_array_move_l.svg?bust=210)

_Now_ we can drop the "B" in there:

![A dynamic array storing the string "LOGS" with the letter "B" floating above. The "B" is bolded with an arrow attached showing how the character is now being placed in the first index.](https://www.interviewcake.com/images/svgs/cs_for_hackers__linked_lists_log_string_dynamic_array_chars_moved.svg?bust=210)

What's our time cost here?

It's all in the step where we made room for the first letter. We had to move _all nn_ characters in our string. One at a time. That's O(n)O(n) time.

**So linked lists have faster _pre_pends (O(1)O(1) time) than dynamic arrays (O(n)O(n) time).**

>No "worst case" caveat this time—prepends for dynamic arrays are _always_ O(n)O(n) time. And prepends for linked lists are _always_ O(1)O(1) time.

These quick appends and prepends for linked lists come from the fact that linked list nodes can go anywhere in memory. They don't have to sit right next to each other the way items in an array do.

So if linked lists are so great, why do we usually store strings in an array? **Because [arrays have O(1)O(1)-time lookups](https://www.interviewcake.com/article/python3/data-structures-coding-interview?course=fc1&section=algorithmic-thinking#constant-time-array-lookups).** And those constant-time lookups _come from_ the fact that all the array elements are lined up next to each other in memory.

Lookups with a linked list are more of a process, because we have no way of knowing where the iith node is in memory. So we have to walk through the linked list node by node, counting as we go, until we hit the iith item.

```python
def get_ith_item_in_linked_list(head, i):
	if i < 0:        
		raise ValueError("i can't be negative: %d" % i)     

	current_node = head     
	current_position = 0    

	while current_node:         
		if current_position == i:
			# Found it!             
			return current_node          

		# Move on to the next node         
		current_node = current_node.next         
		current_position += 1      

	raise ValueError('List has fewer than i + 1 (%d) nodes' % (i + 1))`

```

That's i + 1i+1 steps down our linked list to get to the iith node (we made our function zero-based to match indices in arrays). **So linked lists have O(i)O(i)-time lookups.** Much slower than the O(1)O(1)-time lookups for arrays and dynamic arrays.

Not only that—**walking down a linked list is _not_ cache-friendly.** Because the next node could be _anywhere_ in memory, we don't get any benefit from the processor cache. This means lookups in a linked list are even slower.

So the tradeoff with linked lists is they have faster prepends and faster appends than dynamic arrays, _but_ they have slower lookups.

## Hash tables
---
Quick lookups are often really important. For that reason, we tend to use arrays (O(1)O(1)-time lookups) much more often than linked lists (O(i)O(i)-time lookups).

For example, suppose we wanted to count how many times each ASCII character appears in [Romeo and Juliet](https://raw.githubusercontent.com/GITenberg/The-Tragedy-of-Romeo-and-Juliet_1112/master/1112.txt). How would we store those counts?

We can use arrays in a clever way here. Remember—characters are just numbers. In ASCII (a common character encoding) 'A' is 65, 'B' is 66, etc.

So we can use the character('s number value) as the _index_ in our array, and store the _count_ for that character _at that index_ in the array:

![An array showing indices 63 through 68. To the left of the indices are the ASCII characters that correspond to the numeric indices with arrows pointing from each character to its corresponding number.](https://www.interviewcake.com/images/svgs/cs_for_hackers__hash_tables_chars_to_ints.svg?bust=210)

With this array, we can look up (and edit) the count for any character in constant time. Because we can access any index in our array in constant time.

Something interesting is happening here—this array isn't just a list of values. This array is storing _two_ things: characters and counts. The characters are _implied_ by the indices.

**So we can think of an array as a _table_ with _two columns_...except you don't really get to pick the values in one column (the indices)—they're always 0, 1, 2, 3, etc.**

But what if we wanted to put _any_ value in that column and still get quick lookups?

Suppose we wanted to count the number of times each _word_ appears in Romeo and Juliet. Can we adapt our array?

Translating a _character_ into an array index was easy. But we'll have to do something more clever to translate a _word_ (a string) into an array index...

![A blank array except for the value 20 stored at index 9. To the left the array is the word "lies" with an arrow pointing to the right at diamond with a question mark in the middle. The diamond points to the 9th index of the array.](https://www.interviewcake.com/images/svgs/cs_for_hackers__hash_tables_lies_key_unlabeled.svg?bust=210)

Here's one way we could do it:

Grab the number value for each character and add those up.

![The word "lies" in quotes. Arrows point from each character down to their corresponding number values, which are separated by plus signs and shown in sum to equal 429.](https://www.interviewcake.com/images/svgs/cs_for_hackers__hash_tables_lies_chars.svg?bust=210)

The result is 429. But what if we only have _30_ slots in our array? We'll use a common trick for forcing a number into a specific range: the modulus operator (%). ↴ Modding our sum by 30 ensures we get a whole number that's less than 30 (and at least 0):

429 \: \% \: 30 = 9429%30=9

Bam. That'll get us from a word (or any string) to an array index.

This data structure is called a **hash table** or **hash map**. In our hash table, the _counts_ are the **values** and the _words_ ("lies," etc.) are the **keys** (analogous to the _indices_ in an array). The process we used to translate a key into an array index is called a **hashing function**.

![A blank array except for a 20, labeled as the value, stored at index 9. To the left the array is the word "lies," labeled as the key, with an arrow pointing to the right at diamond with a question mark in the middle, labeled as the hashing function. The diamond points to the 9th index of the array.](https://www.interviewcake.com/images/svgs/cs_for_hackers__hash_tables_lies_key_labeled.svg?bust=210)

> The hashing functions used in modern systems get pretty complicated—the one we used here is a simplified example.

> Note that our quick lookups are only in one direction—we can quickly get the value for a given key, but the only way to get the key for a given value is to walk through all the values and keys.
> 
> Same thing with arrays—we can quickly look up the value at a given index, but the only way to figure out the index for a given value is to walk through the whole array.

One problem—what if two keys hash to the same index in our array? Look at "lies" and "foes":

![The word "lies" in quotes and the word "foes" in quotes. Arrows point from the characters of each word to their corresponding number values. The sum of the characters of both words is shown to equal 429.](https://www.interviewcake.com/images/svgs/cs_for_hackers__hash_tables_lies_and_foes_addition.svg?bust=210)

They both sum up to 429! So of course they'll have the same answer when we mod by 30:

429 \: \% \: 30 = 9429%30=9

So our hashing function gives us the same answer for "lies" and "foes." This is called a **hash collision**. There are a few different strategies for dealing with them.

Here's a common one: instead of storing the actual values in our array, let's have each array slot hold a _pointer_ to a _linked list_ holding the counts for all the words that hash to that index:

![An array storing pointers. Three of the pointers have arrows pointing to linked lists to the right of the array.](https://www.interviewcake.com/images/svgs/cs_for_hackers__hash_tables_hash_collision.svg?bust=210)

One problem—how do we know which count is for "lies" and which is for "foes"? To fix this, we'll store the _word_ as well as the count in each linked list node:

![An array storing pointers. The pointer at index 9 has an arrow pointing to a linked list to the right of the array. Each linked list node now stores the word as well as its count and a pointer.](https://www.interviewcake.com/images/svgs/cs_for_hackers__hash_tables_hash_collision_key_val.svg?bust=210)

"But wait!" you may be thinking, "Now lookups in our hash table take O(n)O(n) time in the worst case, since we have to walk down a linked list." That's true! You could even say that in the worst case _every_ key creates a hash collision, so our whole hash table _degrades to a linked list_.

In industry though, we usually wave our hands and say **collisions are rare enough that on _average_ lookups in a hash table are O(1)O(1) time**. And there are fancy algorithms that keep the number of collisions low and keep the lengths of our linked lists nice and short.

But that's sort of the tradeoff with hash tables. You get fast lookups by key...except _some_ lookups could be slow. And of course, you only get those fast lookups in one direction—looking up the _key_ for a given _value_ still takes O(n)O(n) time.

## Summary
---
**Arrays** have O(1)O(1)-time lookups. But you need enough _uninterrupted_ space in RAM to store the whole array. And the array items need to be the same size.

But if your array stores **pointers** to the actual array items (like we did with our list of baby names), you can get around both those weaknesses. You can store each array item wherever there's space in RAM, and the array items can be different sizes. The tradeoff is that now your array is _slower_ because it's not cache-friendly.

Another problem with arrays is you have to specify their sizes ahead of time. There are two ways to get around this: **dynamic arrays** and **linked lists**. Linked lists have faster appends and prepends than dynamic arrays, but dynamic arrays have faster lookups.

Fast lookups are really useful, especially if you can look things up not just by _indices_ (0, 1, 2, 3, etc.) but by arbitrary _keys_ ("lies", "foes"...any _string_). That's what **hash tables** are for. The only problem with hash tables is they have to deal with hash collisions, which means _some_ lookups _could_ be a bit slow.

**Each data structure has tradeoffs. You can't have it all.**

So you have to know _what's important_ in the problem you're working on. What does your data structure need to do _quickly_? Is it lookups by index? Is it appends or prepends?

Once you know what's important, you can pick the data structure that does it best.

<<<[[Big-O-Notation]] | [[Logarithms]]>>>
--|--
