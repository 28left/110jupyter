---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3.9.4 64-bit
  language: python
  name: python3
---
# Factoring Techniques

## Pull out Common Factors

```{admonition} Common factors
:class: info

The act of pulling out common factors from a sum can be thought of as applying the distributive property of multiplication in reverse.

$$AB + AC = A(B+C)$$

e.g., $21 + 14 = 7\cdot 3 + 7\cdot 2 = 7(3+2)$
```

### Example 1

```{admonition} Factoring
:class: tip

Factor $10x^5 + 15x^4$ by pulling out common factors.
```

```{dropdown} **Step 1:** Determine the factors common to both terms.

- Constant factors: $10$ and $15$ are both multiples of $5$.
- Powers of $x$: the smallest power of $x$ is $4$.

Therefore, the factor common to both terms is $5x^4$.
```

```{dropdown} **Step 2:** Pull out the common factor of $5x^4$.

\begin{align*}
10x^5 + 15x^4 
&= 5x^4\cdot 2x  + 5x^4\cdot3  && \hbox{Write each term as a multiple of $5x^4$} \\
&= 5x^4(2x + 3) && \hbox{Pull out common factor}
\end{align*}
```


### Example 2

```{admonition} Factoring
:class: tip
Factor 

$$4x^3(2x^3+1)^5 + 30x^6(2x^3+1)^4$$ 

by first pulling out common factors.
```

```{dropdown} **Step 1:** Determine the factors common to both terms.

- Constant factors: $4$ and $30$ are both multiples of $2$.
- Powers of $x$: the smallest power of $x$ is $3$.
- Powers of $2x^3+1$: the smallest power of $2x^3+1$ is $4$.

Therefore, the factor common to both terms is $2x^3(2x^3+1)^4$.
```

```{dropdown} **Step 2:** Pull out the common factor of $2x^3(2x^3+1)^4$.

\begin{align*}
& 4x^3(2x^3+1)^5 + 30x^6(2x^3+1)^4 \\
&= 2x^3(2x^3+1)^4\cdot 2(2x^3+1) + 2x^3(2x^3+1)^4 \cdot 15x^3 \\%&& \hbox{Write each term as a multiple of $2x^3(2x^3+1)^4$}\\
&= 2x^3(2x^3+1)^4[2(2x^3+1) + 15x^3] && \hbox{Pull out common factor}\\
&= 2x^3(2x^3+1)^4(4x^3+2 + 15x^3) && \hbox{Simplify expression inside $[ ~ ]$}\\
&= 2x^3(2x^3+1)^4(19x^3+2)
\end{align*}
```


### Example 3

```{admonition} Factoring
:class: tip
Factor 

$$4x^3(2x^3+1)^{1/2} + 3x^6(2x^3+1)^{-1/2}$$ 

by first pulling out common factors.
```

```{dropdown} **Step 1:** Determine the factors common to both terms.

- Constant factors: $4$ and $3$ do not have any factors in common.
- Powers of $x$: the smallest power of $x$ is $3$.
- Powers of $2x^3+1$: the smallest power of $2x^3+1$ is $-1/2$.

Therefore, the factor common to both terms is $x^3(2x^3+1)^{-1/2}$.
```

```{dropdown} **Step 2:** Pull out the common factor of $x^3(2x^3+1)^{-1/2}$.

\begin{align*}
& 4x^3(2x^3+1)^{1/2} + 3x^6(2x^3+1)^{-1/2} \\ \\ 
&= x^3(2x^3+1)^{-1/2}\cdot 4(2x^3+1) + x^3(2x^3+1)^{-1/2} \cdot 3x^3 \\ \\
&= x^3(2x^3+1)^{-1/2}[4(2x^3+1) + 3x^3] && \hbox{Pull out common factor}\\ \\
&= x^3(2x^3+1)^{-1/2}(8x^3+4 + 3x^3) && \hbox{Simplify expression inside $[ ~ ]$}\\ \\
&= x^3(2x^3+1)^{-1/2}(11x^3+4) && \hbox{Combine like terms}\\ \\
&= \frac{x^3(11x^3+4)}{\sqrt{2x^3+1}}
\end{align*}
```


## Difference of Squares

```{admonition} Applying FOIL to product $(A+B)(A-B)$.
:class: info

When applying the FOIL technique to a product of the form $(A+B)(A-B)$, we get the following result.

\begin{align*}
(A+B)(A-B)
&= A\cdot A - A\cdot B + B\cdot A - B\cdot B \\
&= A^2 \cancel{- AB} \cancel{+ AB} - B^2\\
&= A^2 - B^2
\end{align*}

We refer to $A^2-B^2$ as a difference of squares and can reinterpret the above calculation as a way to factor any difference of squares.

$$
\boxed{A^2-B^2 = (A+B)(A-B)}
$$
```


### Example 4

```{admonition} Applying difference of squares
:class: tip

Factor $x^2-25$.
```

```{dropdown} **Step 1:** Rewrite the expression as a difference of squares.

$$x^2 - 25 = x^2 - 5^2$$
```

```{dropdown} **Step 2:** Apply the difference of squares formula with $A=x$ and $B=5$.

\begin{align*}
x^2 - 25
&= x^2 - 5^2 && \hbox{Step 1} \\
&= (x+5)(x-5) && \hbox{Difference of squares}
\end{align*}
```



### Example 5

```{admonition} Applying difference of squares
:class: tip

Factor $9x^3-4x^5$.
```

```{dropdown} **Step 1:** Determine the factors common to both terms.

- Constant factors: $9$ and $-4$ do not have any factors in common.
- Powers of $x$: the smallest power of $x$ is $3$.

Therefore, the factor common to both terms is $x^3$.
```

```{dropdown} **Step 2:** Pull out the common factor of $x^3$.

\begin{align*}
9x^3-4x^5 
&= x^3(9) - x^3(4x^2)\\
&= x^3(9-4x^2) && \hbox{Pull out common factor}
\end{align*}
```

```{dropdown} **Step 3:** Apply difference of squares with $A=3$ and $B=2x$.

\begin{align*}
9x^3-4x^5
&= x^3(9-4x^2) && \hbox{Step 2}\\
&=  x^3[3^2-(2x)^2] && \hbox{Step 3} \\
&= x^3(3+2x)(3-2x) && \hbox{Difference of squares}
\end{align*}
```


## AC Grouping Method

The AC grouping method is a technique for factoring certain quadratic expressions of the form

$$ax^2 + bx + c.$$

The process is broken down into the following five steps.

```{admonition} Steps of the AC Grouping Method.
:class: info

1. Find two integers, $r$ and $s$, that multiply to $a\times c$ and sum to $b$.
2. Replace $bx$ with $rx$ + $sx$.
3. Group terms with common factors.
4. Pull out common factors from each group.
5. Pull out common factor.
```

### Example 6

```{admonition} Applying AC grouping
:class: tip

Factor $6x^2 + 7x - 5$ using the AC grouping method.
```

```{dropdown} **Step 1:** Find two integers that multiply to $6(-5) = -30$ and sum to $7$.

Since the product is negative, the two numbers must have opposite signs.  And since the sum is positive, the larger number in absolute value, must be positive.

| Product equals $-30$ | Sum equals $7$? |
| -------------------- | ------------------ |
| $-1 \times 30 = -30$ | $-1 + 30 = 29$ &nbsp;&nbsp;&nbsp; *NO* | 
| $-2 \times 15 =-30$  | $-2 + 15 = 13$ &nbsp;&nbsp;&nbsp; *NO* |
| $-3 \times 10 =-30$  | $-3 + 10 = 7$ &nbsp;&nbsp;&nbsp; **YES** |
```

```{dropdown} **Step 2:** Since $7 = -3+10$, replace the linear term, $7x$, with  $-3x+10x$.

$$6x^2 - 3x + 10x - 5$$
```

```{dropdown} **Step 3:** Group terms with common factors.

$$(6x^2 - 3x) + (10x - 5)$$
```

```{dropdown} **Step 4:** Pull out common factors from each group.

$$3x(2x-1) +  5(2x-1)$$
```

```{dropdown} **Step 5:** Pull out common factor of $2x-1$.

$$(2x-1)(3x+5)$$

Therefore,

$$6x^2 + 7x - 5 = (2x-1)(3x+5)$$
```

```{dropdown} Check Your Work.
:title: bg-warning font-weight-bold

After factoring a polynomial, it's always a good idea to check your work by expanding the product using the distributive property of multiplication and/or the FOIL method:

\begin{align*}
(2x-1)(3x+5)
&= (2x)(3x) + (2x)(5) + (-1)(3x) + (-1)(5) && \hbox{FOIL}\\
&= 6x^2 + 10x - 3x - 5 && \hbox{Simplify}\\
&= 6x^2 + 7x -5  && \hbox{Combine like terms}
\end{align*}
```


### Example 7

```{admonition} Applying AC grouping
:class: tip

Factor $x^2 - 13x + 36$ using the AC grouping method.
```

```{dropdown} **Step 1:** Find two integers that multiply to $1\times 36 = 36$ and sum to $-13$.

Since the product is positive, the two numbers must have the same sign.  And since the sum is negative, both numbers must be negative.
| Product equals $36$ | Sum equals $-13$? |
| ------------------- | ----------------- |
| $-1 \times -36$     |  NO  |
| $-2 \times -18$     |  NO  |
| $-3 \times -12$     |  NO  |
| $-4 \times -9$      | **YES** | 
```

```{dropdown} **Step 2:** Since $-13 = -4-9$, replace the linear term, $-13x$, with  $-4x-9x$.

$$x^2 - 4x - 9x + 36$$
```

```{dropdown} **Step 3:** Group terms with common factors.

$$(x^2 - 4x) + (-9x + 36)$$
```

```{dropdown} **Step 4:** Pull out common factors from each group.

$$x(x-4) +  (-9)(x-4)$$
```

```{dropdown} **Step 5:** Pull out common factor of $x-4$.

$$(x-4)(x-9)$$

Therefore,

$$x^2 - 13x + 36 = (x-4)(x-9)$$
```

```{dropdown} Check Your Work.
:title: bg-warning font-weight-bold

\begin{align*}
(x-4)(x-9)
&= x^2 -9x -4x + 36 && \hbox{FOIL}\\
&= x^2 - 13x + 36 && \hbox{Combine like terms}
\end{align*}
```



## A Special Case of the AC Grouping Method

```{admonition} Important Observation
:class: danger
If the coefficient of $x^2$ is one (i.e., $a=1$ in $ax^2 + bx + c$), then Step 1 of the $AC$ grouping method is to find two numbers that multiply to $c$ and sum to $b$. Once these numbers have been found, then the factorization can be written as

$$x^2 + bx + c = (x+r)(x+s)$$

where $r+s = b$ and $rs = c$.
```


(01_02_example8)=
### Example 8

```{admonition} AC grouping
:class: tip

Factor $x^2 - 4x - 12$.
```


```{dropdown} **Step 1:** Find two integers that multiply to $-12$ and sum to $-4$.

Since the product is negative, the two numbers must have opposite signs.  And since the sum is negative, the larger number in absolute value, must be negative.
| Product equals $-12$ | Sum equals $-4$? |
| -------------------- | ---------------- |
| $1 \times -12$       | NO |
| $2 \times -6$        | **YES** |
```


```{dropdown} **Step 2:** Apply special case of AC Grouping.

Since the coefficient of $x^2$ is one, then the factorization is given by

$$x^2 - 4x - 12 = (x+2)(x-6).$$
```

```{dropdown} Check Your Work.
:title: bg-warning font-weight-bold

\begin{align*}
(x+2)(x-6)
&= x^2 -6x +2x - 12 && \hbox{FOIL}\\
&= x^2 - 4x - 12 && \hbox{Combine like terms}
\end{align*}
```


### Example 9

```{admonition} AC grouping and pulling out common factors
:class: tip

Factor $7x^4 + 35x^3 + 42x^2$.
```


```{dropdown} **Step 1:** Determine the factors common to both terms.

- Constant factors: $7$, $35$, and $42$ are all multiples of $7$.
- Powers of $x$: the smallest power of $x$ is $2$.

Therefore, the factor common to all three terms is $7x^2$.
```

```{dropdown} **Step 2:** Pull out the common factor of $7x^2$.

\begin{align*}
7x^4 + 35x^3 + 42x^2
&= 7x^2(x^2) + 7x^2(5x) + 7x^2(6) \\ 
&= 7x^2(x^2 + 5x + 6) && \hbox{Pull out common factor}
\end{align*}
```

```{dropdown} **Step 3:** Factor $x^2 + 5x + 6$ by finding two integers that multiply to $6$ and sum to $5$.

| Product equals $6$ | Sum equals $5$? |
| ------------------ | --------------- |
| $1 \times 6$       | NO | 
| $2 \times 3$       | **YES** |

Therefore,
\begin{align*}
7x^4 + 35x^3 + 42x^2
&= 7x^2(x^2 + 5x + 6) && \hbox{Step 2} \\
&= 7x^2(x+2)(x+3) && \hbox{AC grouping}
\end{align*}
```


```{dropdown} Check Your Work.
:title: bg-warning font-weight-bold

\begin{align*}
7x^2(x+2)(x+3)
&= 7x^2(x^2 + 3x + 2x + 6) && \hbox{FOIL}\\
&= 7x^2(x^2 + 5x + 6) && \hbox{Combine like terms}\\ 
&= 7x^2(x^2) + 7x^2(5x) + 7x^2(6) && \hbox{Distribute $7x^2$}\\
&= 7x^4 + 35x^3 + 42x^2 && \hbox{Simplify}
\end{align*}
```



