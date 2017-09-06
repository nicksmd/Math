##### 1. Vector

$ \vec{u}.\vec{v} = u_1*v_1+u_2*v_2 = |\vec{u}||\vec{v}|cos(\theta)$

$|\vec{u}|^2 = \vec{u}.\vec{u}$

###### Linear combination

$a_1\vec{v_1}+...+a_m\vec{v_m}$

###### Span

$span(v_1,...,v_m) = \{a_1\vec{v_1}+...+a_m\vec{v_m} | a_1,...,a_m \in \mathbb{R} \}$

###### Linear independent

A list $(v_1,..,v_m)$ is linear independent if the only choice of $a_1,...,a_m \in \mathbb{R}$ that makes $a_1\vec{v_1}+...+a_m\vec{v_m}=0$ is $a_1=...=a_m=0$

###### Basic of V:

a list of vectors in V that

-  linear independent
-  span V

every $\vec{v} \in V$ can be written **uniquely** in form of a linear combination of the basic

###### Dim = len(basic)

###### Matrix

- Inverse matrix
  $ A^{-1} A = I$

  A is invertible if 

   - $det(A) \neq 0$
  - or we can not find a vector $x \neq 0$ that: Ax = 0
    *proof:* Ax = 0 <=> $A^{-1}Ax = 0$ <=> x = 0

- Singular matrix = matrix that is not invertible <=> det(A)=0

- Eigenvalue $\lambda$ and eigenvector $\vec{x}$ of a matrix A:

  ​       $Ax = \lambda x$

  How to find $\lambda$ and $\vec{x}$ of A:

  ​        $Ax = \lambda x$

  <=> $(A-\lambda I)x = 0$

  <=> $(A - \lambda I)\: is\: singular$

  <=> $det(A-\lambda I) = 0$

  find $\lambda$ then find x

- ​







