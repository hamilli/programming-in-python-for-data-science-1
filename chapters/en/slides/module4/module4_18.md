---
type: slides
---

# Python operations

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We have already been a witness to a few of Python’s arithmetic
operators, but there are a few on this list that you have to to see:

| Operator |  Description   |
| :------: | :------------: |
|   `+`    |    addition    |
|   `-`    |  subtraction   |
|   `*`    | multiplication |
|   `/`    |    division    |
|   `**`   | exponentiation |

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s apply these to the Python types we have learned and observe the
results.

## Numeric Operations

These operators act as expected on numeric types:

And `int` plus a `float` results in a `float`:

``` python
6 + 5.7
```

```out
11.7
```

And the subtraction of 2 values of type `int` results with a type `int`:

``` python
15 - 7
```

```out
8
```

Exponents can be calculated with `**` with `int` values:

``` python
2 ** 3
```

```out
8
```

And `float` datatypes:

``` python
2.2 ** 5
```

```out
51.53632000000002
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Bool

These operations work as expected with numeric values but let’s put on
concentration on what happens with the other data types and structures.
What happens when we try to add up `bool` values?

``` python
True + True 
```

```out
2
```

``` python
True * 4
```

```out
4
```

We see that `True` values as cast as a value of `1` and False as a value
of `0` when they undergo operations:

``` python
False * 2 + True
```

```out
1
```

``` python
False + 4
```

```out
4
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Str

Strings react rather interestingly with the addition operator.  
For instance, when we add strings we add the sequence from one end to
the other:

``` python
'The monster under my bed' + ' is named Mike' 
```

```out
'The monster under my bed is named Mike'
```

But we cannot multiply, divide or subtract them.

``` python
'The monster under my bed' - ' is named Mike' 
```

```out
Error in py_call_impl(callable, dots$args, dots$keywords): TypeError: unsupported operand type(s) for -: 'str' and 'str'

Detailed traceback: 
  File "<string>", line 1, in <module>
```

``` python
'The monster under my bed' / ' is named Mike' 
```

```out
Error in py_call_impl(callable, dots$args, dots$keywords): TypeError: unsupported operand type(s) for /: 'str' and 'str'

Detailed traceback: 
  File "<string>", line 1, in <module>
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We saw that we can operate on `float` and `int` values together but what
about `str` and numeric values?

``` python
'The monster under my bed' + 1200
```

```out
Error in py_call_impl(callable, dots$args, dots$keywords): TypeError: can only concatenate str (not "int") to str

Detailed traceback: 
  File "<string>", line 1, in <module>
```

That does not work, however, if we transform cast the numeric to a
string, we can concatenate the two together:

``` python
'The monster under my bed' + str(1200)
```

```out
'The monster under my bed1200'
```

How about with other data structure like **lists**, **tuples** and
**dictionaries**?

What about multiplication?

``` python
'The monster under my bed' * 3
```

```out
'The monster under my bedThe monster under my bedThe monster under my bed'
```

We can multiply strings and it concatenates the strings together\! Since
we multiplied by 3, the string is repeated 3 times.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## List

If we add lists, similarly to strings, the elements are combine to
create a single list containing the elements of both lists.

``` python
list1 = [1, 2.0, 3, 4.5] + ['nine', 'ten', 'eleven', 'twelve']
```

We can add, but other operators are not supported.

``` python
[1, 2.0, 3, 4.5] * [5, 6, 7, 8]
```

```out
Error in py_call_impl(callable, dots$args, dots$keywords): TypeError: can't multiply sequence by non-int of type 'list'

Detailed traceback: 
  File "<string>", line 1, in <module>
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Boolean Operators

When we’ve filtered our data we’ve seen different boolean operators
however we have yet to see all that is available.

| Operator  | Description                      |
| :-------: | :------------------------------- |
| `x == y`  | is x equal to y?                 |
| `x != y`  | is x not equal to y?             |
|  `x > y`  | is x greater than y?             |
| `x >= y`  | is x greater than or equal to y? |
|  `x < y`  | is x less than y?                |
| `x <= y`  | is x less than or equal to y?    |
| `x is y`  | is x the same object as y?       |
| `x and y` | are x and y both true?           |
| `x or y`  | is at least one of x and y true? |
|  `not x`  | is x false?                      |

Let’s explores these a bit more.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s start with 2 base statements:

``` python
'dogs' != 'cats'
```

```out
True
```

``` python
6 > 7
```

```out
False
```

We can combine them to explore `and`, `or` and `not` operators.

``` python
(6 < 7) and ('dogs' == 'cats')
```

```out
False
```

Since both statements are not true, the “and” statement is False.

``` python
(6 < 7) or ('dogs' == 'cats')
```

```out
True
```

Since one statement is true the combine “or” statement is True.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We know that `('dogs' == 'cats')` is False so a `not` operator gives us
a True value because it confirms the fact the statement is False.

``` python
not ('dogs' == 'cats')
```

```out
True
```

While we know `(6 < 7)` is True:

``` python
not  (6 < 7)
```

```out
False
```

Seeing if the statement is False will result in a False statement since
`(6 < 7)` is True.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

How can we translate this to dataframes? Have you ever wondered why we
can do summary statistics on some columns and not others? We are going
to explore this in the next section.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

# Let’s practice what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />