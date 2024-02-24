## Recursive Descent Parsing
<Br>

#### จัดทำโดย

##### นาย กิตติกานต์ มากผล 6410450087
##### นาย นิสิต นะมิตร 6410451148
##### นาย พีรสิษฐ์ พลอยอร่าม 6410451237
##### นาย ศิวกร ภาสว่าง 6410451423
<br>
<br>

- ให้ = แทน -> ใน Gramma
    - เช่น e = t | t+e คือ e -> t | t+e
- Input 'exit' for end Gramma

``` Bash
# Run Default
$ python3 main.py
```
#### Input
``` Bash
# Input Gramma
Input Gramma: E=T|T+E
Input Gramma: T=int|int*T|(E)
Input Gramma: exit

# Input Token Stream
Input Token: (int)
```

#### Output
```BASH

    Gramma is:
    ------------------

    E -> T | T+E | 

    T -> int | int*T | (E) | 

    ------------------

    Token Stream is: (int)

    ------------------------------------
    Gramma[T] Token is: ( Index is: [0]
    Status: Mismatch: T is not ( ! backtrack...

    Gramma[T] Token is: ( Index is: [0]
    Status: Mismatch: T is not ( ! backtrack...

    Gramma[+] Token is: ( Index is: [0]
    Status: Mismatch: + is not ( ! backtrack...

    Gramma[E] Token is: ( Index is: [0]
    Status: Mismatch: E is not ( ! backtrack...

    Gramma[i] Token is: ( Index is: [0]
    Status: Mismatch: i is not ( ! backtrack...

    Gramma[n] Token is: ( Index is: [0]
    Status: Mismatch: n is not ( ! backtrack...

    Gramma[t] Token is: ( Index is: [0]
    Status: Mismatch: t is not ( ! backtrack...

    Gramma[i] Token is: ( Index is: [0]
    Status: Mismatch: i is not ( ! backtrack...

    Gramma[n] Token is: ( Index is: [0]
    Status: Mismatch: n is not ( ! backtrack...

    Gramma[t] Token is: ( Index is: [0]
    Status: Mismatch: t is not ( ! backtrack...

    Gramma[*] Token is: ( Index is: [0]
    Status: Mismatch: * is not ( ! backtrack...

    Gramma[T] Token is: ( Index is: [0]
    Status: Mismatch: T is not ( ! backtrack...

    Gramma[(] Token is: ( Index is: [0]
    Status: Match! Advance Input

    Gramma[E] Token is: i Index is: [1]
    Status: Mismatch: E is not i ! backtrack...

    Gramma[)] Token is: i Index is: [1]
    Status: Mismatch: ) is not i ! backtrack...

    ------------------------------------
    Gramma[T] Token is: i Index is: [1]
    Status: Mismatch: T is not i ! backtrack...

    Gramma[T] Token is: i Index is: [1]
    Status: Mismatch: T is not i ! backtrack...

    Gramma[+] Token is: i Index is: [1]
    Status: Mismatch: + is not i ! backtrack...

    Gramma[E] Token is: i Index is: [1]
    Status: Mismatch: E is not i ! backtrack...

    Gramma[i] Token is: i Index is: [1]
    Status: Match! Advance Input

    Gramma[n] Token is: n Index is: [2]
    Status: Match! Advance Input

    Gramma[t] Token is: t Index is: [3]
    Status: Match! Advance Input

    Gramma[i] Token is: ) Index is: [4]
    Status: Mismatch: i is not ) ! backtrack...

    Gramma[n] Token is: ) Index is: [4]
    Status: Mismatch: n is not ) ! backtrack...

    Gramma[t] Token is: ) Index is: [4]
    Status: Mismatch: t is not ) ! backtrack...

    Gramma[*] Token is: ) Index is: [4]
    Status: Mismatch: * is not ) ! backtrack...

    Gramma[T] Token is: ) Index is: [4]
    Status: Mismatch: T is not ) ! backtrack...

    Gramma[(] Token is: ) Index is: [4]
    Status: Mismatch: ( is not ) ! backtrack...

    Gramma[E] Token is: ) Index is: [4]
    Status: Mismatch: E is not ) ! backtrack...

    Gramma[)] Token is: ) Index is: [4]
    Status: Match! Advance Input

    ------------------------------------
    End of input, accept
```