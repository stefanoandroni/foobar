# Note

## Find condition
Find the condition on x and y that guarantees not to enter an infinite loop.

### Observe

**1st Step**  
```
 f(x, y) = (2x, y-x) == (a, a)        x < y        (a, a)
```

$` 2x=y-x `$  
$` x = \frac{1}{3} `$

**2nd Step**  
```
f(x, y) = (2x, y-x) == (a, 3a)        x < y        (a, 3a)
```

$`
\begin{equation*}
    \begin{cases}
        2x=a \\
        y-x=3a 
    \end{cases}
    \begin{cases}
        //  \\
        y-x=6x 
    \end{cases}
    \begin{cases}
        //  \\
        x = \frac{1}{7} y 
    \end{cases}
\end{equation*}
`$

**3rd Step**  
```
f(x, y) = (2x, y-x) == (a, 7a)        x < y        (a, 7a)
```

$`
\begin{equation*}
    \begin{cases}
        2x=a \\
        y-x=7a 
    \end{cases}
    \begin{cases}
        //  \\
        y-x=14x 
    \end{cases}
    \begin{cases}
        //  \\
        x = \frac{1}{15} y 
    \end{cases}
\end{equation*}
`$

**4th Step**  
```
f(x, y) = (2x, y-x) == (a, 15a)        x < y        (a, 15a)
```

$`
\begin{equation*}
    \begin{cases}
        2x=a \\
        y-x=15a 
    \end{cases}
    \begin{cases}
        //  \\
        y-x=30x 
    \end{cases}
    \begin{cases}
        //  \\
        x = \frac{1}{31} y 
    \end{cases}
\end{equation*}
`$

**...**  

### Sequence

$\frac{y}{x}$ 1, 3, 7, 15, ...

### Find sequence formula

<table>

  <tr>
    <th>S(n) - S(n-1)</th>
    <td><small></small></td>
    <td><small>2</small></td>
    <td><small>4</small></td>
    <td><small>8</small></td>
    <td><small>...</small></td>
  </tr>
  <tr>
    <th>S(n)</th>
    <td><b>1</b></td>
    <td><b>3</b></td>
    <td><b>7</b></td>
    <td><b>15</b></td>
    <td><small>...</small></td>
  </tr>
    <tr>
    <th>n</th>
    <td><small>0</small></td>
    <td><small>1</small></td>
    <td><small>2</small></td>
    <td><small>3</small></td>
    <td><small>...</small></td>
    </tr>
</table>

**Recursive Formula**  
$`S(0)=1`$  
$`S(n)=S(n-1)+2^n`$

**Solve recursive formula**  
$`
\begin{equation}
\begin{split}
S(n) & = S(n-1)+2^n = \\
 & = S(n-2)+2^{n-1}+2^n= \\
 & = S(n-3)+2^{n-2}+2^{n-1}+2^n= \\
 & = ... = \\
 & = S(0)+2^1+...+2^{n-1}+2^n= \\
 & = 2^0+2^1+...+2^{n-1}+2^n= \\
 & = \sum_{i=0}^n 2^i = \\
 & = 2^{n+1}-1 \\
\end{split}
\end{equation}
`$  

### Conclusion
x and y (with $`x < y`$) lead to an infinite loop iff:  

$`\frac{y}{x} \neq 2^{n+1}-1 \qquad ∀ n\in N \cup \{0\}`$