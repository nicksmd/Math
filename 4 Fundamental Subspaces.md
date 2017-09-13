$A_{m,n} => rref(A) = R$

$Rank(A)=r$

Some concepts:

- row echelon form (ref):

  - The first non-zero element of each row is 1 (leading entry)
  - Each leading entry is in a column to the right of the leading entry in the previous row.
  - Rows with all zero elements, if any, are below rows having a non-zero element.

- reduced row echelon form (rref):

  - The matrix is in row echelon form

  - The leading entry in each row is the only non-zero entry in its column.

    $\begin{bmatrix} &1 &2 &3 &4 \\  &0  &0  &1 &3 \\  &0  &0  &0 &1 \\  &0  &0  &0 &0\end{bmatrix}$

    is a ref.

    $\begin{bmatrix} &1 &2 &0 &0 \\  &0  &0  &1 &0 \\  &0  &0  &0 &1 \\  &0  &0  &0 &0\end{bmatrix}$

    is a rref.

    ​

- rref and ref is obtained by apply elimination operation to A.

- pivot columns of reff: the cols that contains leading entry 

- free columns of reff: the cols of reff that are not pivot cols. 

- pivot rows of reff:  the rows that contains leading entry

  #### The four fundamental subspaces of matrix A.

  suppose: $rref(A) = \begin{bmatrix} &1 &3 &5 &0 &7\\  &0  &0  &0 &1 &2 \\  &0  &0  &0 &0 &0\end{bmatrix}$

  ###### 1. Column space $C(A)$:

  $dim(C(A)) = r$

  $basis(C(A)) = \text{pivot columns of reff(A)}$

  proof:

  - If we look at the pivot columns only, we see the r by r identity matrix (in other words, there is no way to combine its rows to give the zero row (except by the combination with all coefficients zero)) => r pivot rows are independent. (1)

  - Every other (free) columns is a combination of the pivot columns (it is because of the property of rref) (2)

    (1) (2) => q.e.d

    **Note that** elimination operations do change the column space of A: $C(A) \neq C(rref(A))$ (because you can see that most of column of rref(A) ends up with 0, this is not true with A)

  ######  2. Row space $C(A^T)$:

  $dim(C(A^T)) = r$

  $basis(C(A^T)) = \text{pivot rows of rref(A)}$

  proof:

  - If we look at the pivot columns only, we see the r by r identity matrix (in other words, there is no way to combine its rows to give the zero row (except by the combination with all coefficients zero)) => r pivot rows are independent. (1)

    $rref(A) = \begin{bmatrix} &1^* &3 &5 &0^* &7\\  &0^*  &0  &0 &1^* &2 \\  &0  &0  &0 &0 &0\end{bmatrix}$

  - Because elimination operation does not change the row space of A => pivot rows of rref(A) span the row space of A. (2)

    (1), (2) => q.e.d 

    ​

  **Lemma**: The number of independent columns equals the number of independent rows.

  The above proof give us the conclusion that: number of independent rows of A is r.

  We need to prove that number of independent cols of A is also r:

  - Ax = 0 <=> Rx = 0

  - let $p$ be the basis of C(A), and $q$ be the basis of C(R), we have:

    Ax = 0 <=> $p.x = 0$

    Rx = 0 <=> $q.x = 0$

    => p = q

    => len(p) = len(q)

    => q.e.d

  ###### 3. Null space $N(A)$:

  $dim(N(A)) = n-r$

  $basis(N(A)) = \text{special solutions of Ax=0}$

  proof:

  - the special solution is independent because they contain a identity matrix
  - all the solutions is a combination of special solutions: we only need to multiply free variable with a proper scalar, other variable can be determined by equation $rref(A).x=0$

  ###### 4. Left null space $N(A^T)$:

  $dim(N(A^T)) = m-r$

  ​

  ​

  ​

  ​

  ​

  ​



