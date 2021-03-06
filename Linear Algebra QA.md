##### 1. Why Gauss elimination does not change the null space of matrix A?

let M be the product of elementary matrixes of A.

- suppose $x \in N(A)$, so Ax = 0. we have:

  ​		$MAx = M(Ax) = M.0 = 0$

  so $x \in N(MA)$ as well.

- suppose $y \in N(MA)$, so (MA).y=0. we have:

  ​		$Ay = M^{-1} MAy = M^{-1}.0=0$

  so $y \in N(A)$ as well.

That means when you apply Gauss elimination, you do change the solution space. 

##### 2. Why every elementary is invertible?

https://en.wikipedia.org/wiki/Elementary_matrix

https://math.vanderbilt.edu/sapirmv/msapir/prleelementary.html

##### 3. If n vectors are independent, is their span $R^n$ ?

Yes. Here is why:

**Proposition.** Let W be a subspace of a finite-dimensional vector space V. If $dim(⁡W)=dim(⁡V)$, then W=V.

If we are given linearly independent $\{v_1,...,v_n\}∈R^n$, then  $span\{v_1,...,v_n\}$ is an n-dimensional subspace of $R^n$. Since $dim(R^n)=n$, the proposition implies that $span\{v_1,...,v_n\}=R^n$

#####4. Proof: A invertible <=> A's columns are independent & A is squared.

​        $A = [v_1,v_2,v_3 ..., v_n] : v_i \text{is column vector}$ 

- Suppose A is invertible => A is squared

  $Ax=0 <=> A^{-1}Ax=A^{-1}0 <=> x = 0$

  => q.e.d

- Suppose A's columns are independent & A is squared.

  $\{v_1, v_2,..., v_n\}$ are independent => $\{v_1, v_2,..., v_n\}$ is a basis of $R^n$ (see Q3). So:

  $I_n = A* \begin{bmatrix} &b_{1,1}  &...  b_{1,n} \\  &b_{2,1}  &...  b_{2,n} \\  &...  &  & \\  &b_{n,1}  &...  b_{n,n} \end{bmatrix} = A*B => B=A^{-1}$ 

##### 5. Proof: A's columns are independent => $A^TA$ invertible.

- $A^TA $ is squared.

- A's columns are independent <=> N(A)={0}. Let $\vec{v} \in N(A^TA)$ .We have: 
  $$
  \begin{array}{lllllll}
         \:\:\:\:\:\:\:\:\:\:\:A^TA.\vec{v}=\vec{0} \\
  <=> v^TA^TAv=v^T.\vec{0} = 0 \\
  <=> (Av)^T.(Av) =0 \\
  <=> Av = 0 \\
  <=> \begin{cases} \vec{v}=\vec{0} \\ \vec{v} \in N(A)\end{cases} \\
  <=> N(A) = N(A^TA) = \{0\}
  \end{array}
  $$



=> q.e.d

##### 6. Proof: Orthonormal set of vector are independent.

https://www.quora.com/Is-an-orthonormal-set-of-vectors-a-linearly-independent-set/answer/Supreeth-Narasimhaswamy

##### 7. Why different eigenvalues produce independent eigenvectors?

Suppose we have k = 2 eigenvalues and some combination of $x_1 \text{ and } x_2$ produces 0:

$c_1x_1+c_2x_2=0 ~~~(1)$. We will prove that $c_1=c_2=0$:

$Ac_1x_1+Ac_2x_2=0 <=> c_1\lambda_1x_1+c_2\lambda_2x_2=0 ~~~(2)$

Subtract $(1)\lambda_2 \text{ to } (2)$:

$x_1c_1(\lambda_1-\lambda_2)=0 <=> c_1=0$ because $x_1 \neq 0$ and eigenvalues are different.

Similarly, we can show that $c_2=0$. This same argument extends to any number of eigenvalue.

##### 8. Why A is singular <=> A has an eigenvalue equal 0?

Because: $ det(A) = \lambda_1..\lambda_n $

##### Eigenvectors of a symmetric matrix A corresponding to different eigenvalues are orthogonal.

http://www.maths.manchester.ac.uk/~peter/MATH10212/notes10.pdf



 	



















