* **Multiominal Coefficients**:

    ![](https://latex.codecogs.com/gif.latex?\binom{n}{n_{1},&space;n_{2},&space;..,&space;n_{m}}&space;=\frac{n!}{n_{1}!n_{2}!...n_{m}!})

    Distribute n people to m group with respectively sizes: n1,n2...,nm

    Example: 4 people a,b,c,d => 2 groups, each group has 2 people:
    - (ab)(cd)
    - (ac)(bd)
    - (ad)(bc)
    - (bc)(ad)
    - (bd)(ac)
    - (cd)(ab)

    Result:

    ![](https://latex.codecogs.com/gif.latex?\frac{4!}{2!2!}=6)

* **Number of vector (x1,x2..,xm) that**:
    - ![](https://latex.codecogs.com/gif.latex?x_{i}&space;>=0)
    - ![](https://latex.codecogs.com/gif.latex?x_{1}&plus;x_{2}&plus;...&plus;x_{m}=n)

    is:

    ![](https://latex.codecogs.com/gif.latex?\binom{n&plus;m-1}{m-1})

    If ![](https://latex.codecogs.com/gif.latex?x_{i}&space;>=1):

    ![](https://latex.codecogs.com/gif.latex?\binom{n-1}{m-1})

    Example: If 8 identical blackboards are to be divided among
4 schools, how many divisions are possible?:

    x1+x2+x3+x4=8

    ![](https://latex.codecogs.com/gif.latex?=\binom{8&plus;4-1}{4-1})

    if each school has to receive at least 1 blackboards:

    ![](https://latex.codecogs.com/gif.latex?=\binom{8-1}{4-1})

* **Number of vector (x1,x2..,xm) that:**
    - ![](https://latex.codecogs.com/gif.latex?x_{i}&space;>=0)
    - ![](https://latex.codecogs.com/gif.latex?x_{1}&plus;x_{2}&plus;...&plus;x_{m}=n)
    - ![](https://latex.codecogs.com/gif.latex?x_{i}&space;>=&space;min_{i}&space;,&space;i=1..m)

    ![](https://latex.codecogs.com/gif.latex?\binom{n'&plus;m-1}{m-1})

    with

    ![](https://latex.codecogs.com/gif.latex?n'&space;=&space;n&space;-&space;\sum_{i=1}^{m}min_{i})

* **Binomial coefficient:**

    ![](https://latex.codecogs.com/gif.latex?\binom{n}{k}&space;=&space;\frac{n!}{(n-k)!k!})

    ![](https://latex.codecogs.com/gif.latex?\binom{n}{k}&space;=&space;\binom{n-1}{k-1}&space;&plus;&space;\binom{n-1}{k})

    ![](https://latex.codecogs.com/gif.latex?(x&plus;y)^{n}&space;=&space;\sum_{k=0}^{n}\binom{n}{k}x^{k}y^{n-k})

*
