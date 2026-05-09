# 目录

[TOC]

# 第1章 预备知识：定义、定理、引理汇总

## §1.1 基本代数结构

### 定义 1.1 (笛卡尔积)  
设 $A$ 和 $B$ 是两个非空集合，我们把集合
\[ A \times B = \{(a,b) \mid a \in A, b \in B\} \]
称为集合 $A$ 和 $B$ 的 **笛卡尔积**。如果 $A = B$，也可简记为 $A^2$。


### 定义 1.2 (代数系统 / 代数结构)  
一个非空集合 $X$ 和与 $X$ 相关的若干代数运算 $f_1,\ldots,f_k$ 组成的系统称为 **代数系统**（简称代数系），记作 $\langle X \colon f_1,\ldots,f_k\rangle$。  
在此基础上，把定义在集合上的运算具有某些特定性质的一类代数系统称为 **代数结构**。


### 定义 1.3 (群 / 半群 / 含幺半群 / Abel 群)  
若运算 $\circ$ 满足结合律，则称代数系统 $\langle G\colon\circ\rangle$ 为 **半群**；  
若在半群基础上存在单位元，则称之为 **含幺半群**；  
若在含幺半群基础上每个元素存在逆元，则称之为 **群**；  
若在群的基础上运算还满足交换律，则称之为 **Abel 群**（也称 **交换群**）。


### 定理 1.1 (群的单位元逆元唯一)  

1. 群的单位元唯一；  
2. 群中每个元素的逆元唯一。

### 证明
1. 设 $e_1$ 和 $e_2$ 都是群 $G$ 的单位元，则 $e_1 = e_1 \circ e_2 = e_2$。  
2. 设 $b$ 和 $c$ 都是 $a$ 的逆元，则  
   $b = b \circ e = b \circ (a \circ c) = (b \circ a) \circ c = e \circ c = c$。


### 定义 1.4 (域)  
代数系统 $\langle F\colon+,\circ\rangle$ 称为一个 **域**，如果：

1. $\langle F\colon+\rangle$ 是交换群，其单位元记作 $0$；
2. $\langle F\setminus\{0\}\colon\circ\rangle$ 是交换群；
3. 运算 $\circ$ 对 $+$ 满足左、右分配律。


### 定理 1.2 (数域的充要条件)  
关于数域，有如下两个结论：

1. 数集 $F$ 对数的加法和乘法构成数域的充要条件为：$F$ 包含 $0,1$ 且对数的加、减、乘、除（除数不为 $0$）运算封闭；
2. 任何数域都包含有理数域 $\mathbf{Q}$，即 $\mathbf{Q}$ 是最小的数域。

### 证明
（略，见原文详细论证）


### 定义 1.5 (环 / 除环 / 交换环)  
代数系统 $\langle R\colon+,\circ\rangle$ 称为一个 **环**，如果：

1. $\langle R\colon+\rangle$ 是交换群，单位元记作 $0$；
2. $\langle R\colon\circ\rangle$ 是幺半群；
3. 运算 $\circ$ 对 $+$ 满足左、右分配律。

若进一步每个非 $0$ 元素关于 $\circ$ 都有逆元，则称之为 **除环**。  
若 $\circ$ 运算满足交换律，则称为 **交换环**。  
交换除环即为域。


## §1.2 复数域的引入

### 定理 1.3 (复数乘法构造)  
平面点集 $\mathbf{R}^2$ 上存在唯一的乘法 $\circ$，满足：

1. (单位元) $\vec{u}\circ\vec{e}_1=\vec{e}_1\circ\vec{u}=\vec{u},\enspace\forall\vec{u}\in\mathbf{R}^2$；
2. (长度可乘性) $\lvert\vec{u}\circ\vec{v}\rvert=\lvert\vec{u}\rvert\lvert\vec{v}\rvert$。

此乘法满足交换律，且使得 $\langle\mathbf{R}^2\colon+,\circ\rangle$ 成为域。

### 证明
（略，见原文推导过程，得到乘法定义 $(a,b)\circ(c,d)=(ac-bd,ad+bc)$）


### 定理 1.4 (复数模的三角不等式)  
设 $z, w \in \mathbf{C}$，则有 $|z + w| \leqslant |z| + |w|$。


### 定理 1.5 (共轭复数的性质)  
设 $z = (a, b) \in \mathbf{C}$，称 $\overline{z} = (a, -b)$ 为 $z$ 的共轭复数，则 $\overline{z} z = |z|^2$。


## §1.3 等价关系

### 定义 1.6 (等价关系)  
集合 $A$ 中关系 $R$ 若满足以下条件，则称 $R$ 为 $A$ 的一个 **等价关系**：

1. (自反性) $\forall a\in A, \enspace a\,R\,a$；
2. (对称性) 若 $a\,R\,b$，则 $b\,R\,a$；
3. (传递性) 若 $a\,R\,b$，$b\,R\,c$，则 $a\,R\,c$。

若 $a\,R\,b$，则称 $a$，$b$ 关于 $R$ 是等价的。$A$ 中所有与 $a$ 等价的元素集合 $\overline{a}=\{b\in A \mid b\,R\,a\}$ 称为 $a$ 所在的 **等价类**，$a$ 称为这个等价类的代表元素。


### 定义 1.7 (分划)  
若集合 $A$ 的子集族 $\{A_i\}$ 满足：  

1. $\bigcup_i A_i = A$；  
2. $i \neq j$ 时 $A_i \cap A_j = \varnothing$，  
   则称 $\{A_i\}$ 为 $A$ 的一个 **分划**。


### 定理 1.6 (等价类构成分划)  
设 $R$ 是集合 $A$ 的等价关系，则由所有不同的等价类构成的子集族 $\{\overline{a}\}$ 是 $A$ 的分划。反之，基于分划可在 $A$ 中定义等价关系。

### 引理 1.1 (等价引理)  
设 $R$ 是集合 $A$ 的等价关系，$a,b\in A$，则 $\overline{a}=\overline{b} \iff a\,R\,b$。

### 证明
充分性：若 $\overline{a}=\overline{b}$，则 $a \in \overline{b}$，故 $a\,R\,b$。  
必要性：若 $a\,R\,b$，则 $\forall c \in \overline{a}$ 有 $c\,R\,a$，由传递性 $c\,R\,b$，故 $c \in \overline{b}$，所以 $\overline{a} \subseteq \overline{b}$；同理 $\overline{b} \subseteq \overline{a}$。


### 推论 1.1 (等价类的互斥性)  
设 $R$ 是集合 $A$ 的等价关系，$a,b\in A$，则下面二者必成立其一：

1. $\overline{a}\cap\overline{b}=\varnothing$；
2. $\overline{a}=\overline{b}$。

### 证明
若 $\overline{a}\cap\overline{b}\neq\varnothing$，则存在 $x \in \overline{a} \cap \overline{b}$，于是 $x\,R\,a$ 且 $x\,R\,b$，由对称性 $a\,R\,x$，由传递性 $a\,R\,b$，再由引理 1.1 得 $\overline{a}=\overline{b}$。


### 定义 1.8 (商集)  
设 $R$ 是集合 $A$ 的等价关系，以关于 $R$ 的等价类为元素的集族 $\{\overline{a}\}$ 称为 $A$ 对 $R$ 的 **商集**，记为 $A/R$。  
映射 $\pi(a) = \overline{a}, \enspace \forall a\in A$ 称为 $A$ 到 $A/R$ 上的 **自然映射**。


### 定义 1.9 (运算的相容性 / 良定义)  
设 $A$ 是一个集合，$R$ 是 $A$ 上的一个等价关系，若 $A$ 上有二元运算 $+$，且在 $A/R$ 上以 $\overline{a}\oplus\overline{b}=\overline{a+b}$ 继承运算，则称 $\oplus$ 与 $R$ **相容**（或称在 $A/R$ 上是 **良定义** 的）当且仅当 $a\,R\,b$，$c\,R\,d$ 时有 $\overline{a}\oplus\overline{c}=\overline{b}\oplus\overline{d}$。


### 定理 1.7 (模 $n$ 同余与加乘运算相容)  
模 $n$ 同余关系 $R$ 与加法 $\oplus$ 和乘法 $\circ$ 相容。

### 证明
（仅证加法）设 $a\,R\,b$，$c\,R\,d$，则可设 $b=a+kn$，$d=c+ln$，则  
$\overline{b}\oplus\overline{d}=\overline{b+d}=\overline{a+c+(k+l)n}=\overline{a+c}=\overline{a}\oplus\overline{c}$。


## §1.4 高斯-若当消元法

### 定义 1.10 (线性方程组)  
由 $m$ 个线性方程组成的 $n$ 元线性方程组可表示为：
\[
\begin{cases}
\begin{aligned}
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n &= b_1 \\
a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n &= b_2 \\
&\qquad\vdots \\
a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n &= b_m
\end{aligned}
\end{cases}
\]


### 定义 1.11 ($n$ 元笛卡尔积 / 笛卡尔幂)  
设 $A_i~(1\leqslant i\leqslant n)$ 是一族集合，集合
\[ \prod_{i=1}^n A_i = \{(a_1, a_2, \cdots, a_n) \mid a_i\in A_i\} \]
称为集族 $\{A_i\}$ 的 **$n$ 元笛卡尔积**。  
当所有 $A_i = A$ 时，记 $A^n = \prod_{i=1}^n A$ 为集合 $A$ 的 $n$ 次 **笛卡尔幂**。


### 定义 1.12 ($n$ 元实向量 / 零向量)  
$\mathbf{R}^n$ 中的元素 $(x_1, x_2, \cdots, x_n)$ 称为 **$n$ 元实向量**，$x_i$ 称为向量的第 $i$ 个分量。若所有分量为 $0$，则称为 **零向量**。  
类似可定义 $n$ 元复向量。


### 定义 1.13 (矩阵)  
域 $\mathbf{F}$ 中的 $m \times n$ 个元素 $a_{ij}$ 排成 $m$ 行 $n$ 列的矩形数表，称为域 $\mathbf{F}$ 上的一个 $m\times n$ **矩阵**，记作 $(a_{ij})_{m \times n}$。


### 定义 1.14 (矩阵的转置)  
设 $A = (a_{ij})_{m \times n}$，则 $A$ 的 **转置矩阵** $A^\mathrm{T}$ 是一个 $n \times m$ 矩阵，满足 $(A^\mathrm{T})_{ij} = a_{ji}$。


### 定义 1.15 (系数矩阵 / 齐次与非齐次线性方程组)  
线性方程组的系数构成的矩阵称为 **系数矩阵** $A$。若右端常数项全为 $0$，即 $\vec{b} = \vec{0}$，则称为 **齐次线性方程组**，否则为 **非齐次线性方程组**。


### 定义 1.16 (增广矩阵 / 阶梯矩阵 / 简化阶梯矩阵)  

- **增广矩阵**：$(A,\vec{b})$，即在系数矩阵 $A$ 右侧增加一列 $\vec{b}$。  
- **阶梯矩阵**：系数全零行在最下方，且非零行的第一个非零元素（主元素）所在列随行数增加严格右移。  
- **简化阶梯矩阵**：阶梯矩阵中每个主元素为 $1$，且主元素所在列的其余元素全为 $0$。


### 定理 1.8 (线性方程组的矩阵与向量表示)  
线性方程组可表示为：

1. 矩阵形式：$AX = \vec{b}$，其中 $X = (x_1,\ldots,x_n)^\mathrm{T}$；
2. 向量形式：$x_1\vec{\beta}_1 + x_2\vec{\beta}_2 + \cdots + x_n\vec{\beta}_n = \vec{b}$，其中 $\vec{\beta}_i$ 是 $A$ 的第 $i$ 列。


### 定理 1.9 (矩阵左乘列向量的运算规则)  
设 $A = (\vec{\beta}_1, \vec{\beta}_2, \ldots, \vec{\beta}_n)$，$X = (x_1, x_2, \ldots, x_n)^\mathrm{T}$，则
\[ AX = x_1\vec{\beta}_1 + x_2\vec{\beta}_2 + \cdots + x_n\vec{\beta}_n. \]


## 隐含在例题与习题中的重要结论

### 定理 1.10 (数域的结构定理)  
任何数域都包含有理数域 $\mathbf{Q}$，且 $\mathbf{Q}$ 是最小的数域。


### 定理 1.11 (有限域的构造)  
设 $\mathbf{Z}_n$ 是整数模 $n$ 同余类的集合，定义加法 $\oplus$ 和乘法 $\circ$ 为：
\[ \overline{a} \oplus \overline{b} = \overline{a+b}, \quad \overline{a} \circ \overline{b} = \overline{ab}. \]
则 $\langle \mathbf{Z}_n \colon \oplus, \circ \rangle$ 是域当且仅当 $n$ 是素数。


### 定理 1.12 (三维实数向量空间无法构成域)  
$\mathbf{R}^3$ 上不存在同时满足以下性质的乘法运算：

1. 存在单位元 $\vec{e}_1$；
2. 乘法交换；
3. 长度可乘（即 $|\vec{u} \cdot \vec{v}| = |\vec{u}| |\vec{v}|$）。


### 定理 1.13 (等价关系的替代定义)  
若集合 $A$ 上的二元关系 $R$ 满足：

1. $a\,R\,a,\enspace\forall a\in A$；
2. $\forall a,b,c\in A$，若 $a\,R\,b$ 且 $a\,R\,c$，则 $b\,R\,c$，
   则 $R$ 为 $A$ 上的等价关系。


### 定理 1.14 (零环)  
设 $A$ 是一个 Abel 群（加法运算），定义乘法为 $ab = 0,\enspace\forall a,b\in A$，则 $A$ 构成一个环，且其加法单位元与乘法单位元相同（这样的环称为 **零环**）。


### 算法 1.1 (高斯-若当消元法)  
求解线性方程组的系统步骤：

1. 写出增广矩阵 $(A, \vec{b})$；
2. 通过初等行变换化为阶梯矩阵；
3. 进一步化为简化阶梯矩阵；
4. 根据简化阶梯矩阵判断解的情况：
   - 有唯一解：主元个数等于未知数个数，且无非零常数行；
   - 无解：出现形如 $(0,\ldots,0 \mid c)$（$c \neq 0$）的行；
   - 有无穷解：主元个数小于未知数个数，且无矛盾方程。


**公式 1.1 (复数乘法公式)**  
$(a,b)\circ(c,d) = (ac-bd, ad+bc)$，对应复数乘法 $(a+b\mathrm{i})(c+d\mathrm{i}) = (ac-bd) + (ad+bc)\mathrm{i}$。


**公式 1.2 (共轭复数模公式)**  
$z \overline{z} = |z|^2$。


### 方法 1.1 (等价类的划分方法)  
给定等价关系 $R$，商集 $A/R$ 的元素是 $A$ 的等价类，它们构成 $A$ 的一个分划。反之，给定 $A$ 的一个分划，可定义等价关系为“属于同一个分划子集”。


### 方法 1.2 (商集上运算的良定义验证)  
要在商集 $A/R$ 上定义运算，必须验证：若 $\overline{a} = \overline{b}$，$\overline{c} = \overline{d}$，则运算结果 $\overline{a} \oplus \overline{c} = \overline{b} \oplus \overline{d}$。


## 补充说明

- **线性映射**、**矩阵乘法** 等完整表述将在后续章节给出。
- **行列式的性质**、**范德蒙德行列式公式** 等将在行列式章节介绍。
- **数学归纳法** 等证明框架将在具体证明中体现。

---

# 第2章 线性空间：定义、定理与引理总结

## 2.1 线性空间的定义

### 定义 2.1.1（线性空间）
设 \( V \) 是一个非空集合，\( \mathbf{F} \) 是一个数域。定义两种运算：
1. **加法** \( +: V \times V \to V \)，要求 \( \langle V, +\rangle \) 构成 Abel 群，即满足：
   - 结合律：\( \alpha + (\beta + \gamma) = (\alpha + \beta) + \gamma \)
   - 单位元：\( \exists \vec{0} \in V \) 使 \( \alpha + \vec{0} = \vec{0} + \alpha = \alpha \)
   - 逆元：\( \forall \alpha \in V, \exists -\alpha \in V \) 使 \( \alpha + (-\alpha) = \vec{0} \)
   - 交换律：\( \alpha + \beta = \beta + \alpha \)
2. **数乘** \( \cdot: \mathbf{F} \times V \to V \)，满足：
   - 单位元：\( 1 \cdot \alpha = \alpha \)
   - 结合律：\( \lambda(\mu \alpha) = (\lambda \mu) \alpha \)
   - 左分配律：\( (\lambda + \mu) \alpha = \lambda \alpha + \mu \alpha \)
   - 右分配律：\( \lambda(\alpha + \beta) = \lambda \alpha + \lambda \beta \)

则称 \( V \) 在域 \( \mathbf{F} \) 上构成一个**线性空间**，记作 \( V(\mathbf{F}) \)。


### 定理 2.1.1（线性空间的基本运算性质）
在线性空间 \( V(\mathbf{F}) \) 中，以下性质成立：
1. \( \lambda(\alpha - \beta) = \lambda \alpha - \lambda \beta \)
2. \( (\lambda - \mu) \alpha = \lambda \alpha - \mu \alpha \)
3. \( \lambda \cdot \vec{0} = \vec{0} \)
4. \( \lambda(-\beta) = -(\lambda \beta) \)
5. \( 0 \cdot \alpha = \vec{0} \)
6. \( (-\mu) \alpha = -(\mu \alpha) \)
7. 若 \( \lambda \alpha = \vec{0} \)，则 \( \lambda = 0 \) 或 \( \alpha = \vec{0} \)


### 定理 2.1.2（加法交换律的冗余性）
在线性空间定义的8条公理中，**加法交换律**可由其余7条公理推出。


## 2.2 线性空间的例子

### 定义 2.2.1（多项式空间）
设 \( \mathbf{F}[x]_{n+1} = \{ a_0 + a_1 x + \cdots + a_n x^n \mid a_i \in \mathbf{F} \} \)，关于多项式的加法和数乘构成线性空间。  
注意：\( \mathbf{F}[x]'_{n+1} = \{ a_0 + a_1 x + \cdots + a_n x^n \mid a_i \in \mathbf{F}, a_n \neq 0 \} \) 不构成线性空间（加法不封闭）。


### 定义 2.2.2（函数空间）
设 \( C[a,b] \) 为闭区间 \([a,b]\) 上的连续实值函数全体，关于函数的加法和数乘构成实数域上的线性空间。


### 定义 2.2.3（数域与线性空间的关系）
- \( \mathbf{C} \) 是 \( \mathbf{C} \) 或 \( \mathbf{R} \) 上的线性空间
- \( \mathbf{R} \) 是 \( \mathbf{R} \) 上的线性空间
- \( \mathbf{R} \) **不是** \( \mathbf{C} \) 上的线性空间（数乘不封闭）


### 定义 2.2.4（模）
设 \( R \) 是一个环，\( M \) 是一个加法 Abel 群。若定义了数乘运算 \( R \times M \to M \) 满足：
1. \( 1 \alpha = \alpha \)
2. \( r(s \alpha) = (rs) \alpha \)
3. \( (r + s) \alpha = r \alpha + s \alpha \)
4. \( r(\alpha + \beta) = r \alpha + r \beta \)

则称 \( M \) 是环 \( R \) 上的**左模**（左 \( R \)-模），记作 \( _R M \)。对称可定义右模和双模。


### 定义 2.2.5（同构）
设 \( V(\mathbf{F}) \) 和 \( W(\mathbf{F}) \) 是数域 \( \mathbf{F} \) 上的线性空间。若映射 \( \varphi: V \to W \) 满足：
- \( \varphi(\alpha + \beta) = \varphi(\alpha) + \varphi(\beta) \)
- \( \varphi(\lambda \alpha) = \lambda \varphi(\alpha) \)

且 \( \varphi \) 是双射，则称 \( \varphi \) 是一个**同构**，并称 \( V \) 与 \( W \) 同构，记作 \( V \cong W \)。


## 2.3 线性子空间

### 定义 2.3.1（线性子空间）
设 \( W \) 是线性空间 \( V(\mathbf{F}) \) 的非空子集。若 \( W \) 对 \( V \) 中的运算也构成 \( \mathbf{F} \) 上的线性空间，则称 \( W \) 是 \( V \) 的**线性子空间**（简称**子空间**）。


### 定理 2.3.1（子空间判别定理）
数域 \( \mathbf{F} \) 上的线性空间 \( V(\mathbf{F}) \) 的非空子集 \( W \) 为子空间的**充要条件**是 \( W \) 对 \( V \) 的线性运算封闭。


### 定理 2.3.2（齐次线性方程组的解空间）
齐次线性方程组 \( AX = 0 \) 的解集是 \( \mathbf{F}^n \) 的一个子空间（称为**解空间**）；非齐次线性方程组的解集**不**构成子空间。


## 2.4 线性表示与线性扩张

### 定义 2.4.1（线性组合与线性表示）
设 \( \alpha_i \in V(\mathbf{F}) \)，\( \lambda_i \in \mathbf{F} \)。向量 \( \alpha = \lambda_1 \alpha_1 + \cdots + \lambda_m \alpha_m \) 称为向量组 \( \alpha_1, \ldots, \alpha_m \) 的**线性组合**，或称 \( \alpha \) 可由该向量组**线性表示**。


### 定义 2.4.2（线性扩张）
设 \( S \) 是线性空间 \( V(\mathbf{F}) \) 的非空子集。集合
\[
\operatorname{span}(S) = \{ \lambda_1 \alpha_1 + \cdots + \lambda_k \alpha_k \mid \lambda_i \in \mathbf{F},\ \alpha_i \in S,\ k \in \mathbb{N}_+ \}
\]
称为 \( S \) 的**线性扩张**，即 \( S \) 中所有有限子集的线性组合全体。


### 定理 2.4.1（线性扩张构造子空间）
线性空间 \( V(\mathbf{F}) \) 的非空子集 \( S \) 的线性扩张 \( \operatorname{span}(S) \) 是 \( V \) 中包含 \( S \) 的**最小子空间**。


## 隐含定理与重要结论

### 定理 2.5.1（线性方程组解的表示）
设 \( \lambda \beta + \lambda_1 \alpha_1 + \cdots + \lambda_r \alpha_r = \vec{0} \)，若 \( \lambda \neq 0 \)，则
\[
\beta = -\lambda^{-1} \lambda_1 \alpha_1 - \cdots - \lambda^{-1} \lambda_r \alpha_r
\]


### 定理 2.5.2（子空间与线性扩张的等价刻画）
设 \( W \) 是线性空间 \( V \) 的子集。则 \( W \) 是子空间当且仅当 \( \operatorname{span}(W) = W \)。


### 定理 2.5.3（数域扩张下的线性空间）
设 \( \mathbf{E} \subseteq \mathbf{F} \) 是域扩张。
1. \( \mathbf{F} \) 是 \( \mathbf{E} \) 上的线性空间。
2. 若 \( V \) 是 \( \mathbf{F} \) 上的线性空间，则 \( V \) 也是 \( \mathbf{E} \) 上的线性空间。


### 定理 2.5.4（有限域上的线性空间结构）
设 \( \mathbf{Z}_p \) 是特征 \( p \) 的有限域，则 \( \mathbf{Z}_p \) 是 \( \mathbf{F}_{p^n} \) 的子域，且 \( \mathbf{F}_{p^n} \) 可视为 \( \mathbf{Z}_p \) 上的线性空间。


## 补充说明
- **线性映射**：若映射 \( \varphi: V \to W \) 保持加法和数乘，则称为**线性映射**（同态）。若为双射，则为同构。
- **矩阵乘法**：在线性空间中，矩阵可视为线性映射的表示，其乘法对应于映射的复合。
- **行列式性质**：在后续章节中，行列式的多重线性性、交替性等均可由线性空间的结构导出。
- **范德蒙德行列式**：可作为多项式空间中的线性相关性的特例。
- **数学归纳法**：在线性空间的维数、基的构造等证明中常用。

### 注： 本章所有定义、定理、引理均按章节顺序排列，引理紧随其服务的定理之后。部分在原文中以例题或注释形式出现的结论已提炼为定理。

---

# 第3章：有限维线性空间 — 定义、定理与引理整理


## 3.1 线性相关性

### 定义 3.1（线性相关性）
设 $V(\mathbf{F})$ 是一个线性空间，$\alpha_1,\alpha_2,\ldots,\alpha_m \in V$，若存在不全为 $0$ 的 $\lambda_1,\lambda_2,\ldots,\lambda_m \in \mathbf{F}$，使得
\[
\lambda_1\alpha_1+\lambda_2\alpha_2+\cdots+\lambda_m\alpha_m=0
\]
成立，则称 $\alpha_1,\alpha_2,\ldots,\alpha_m$ **线性相关**，否则称 **线性无关**（即系数只能为 $0$）。


### 性质 3.1（零向量与线性相关性）
1. 线性空间中单个向量 $\alpha$ 线性相关的充要条件是 $\alpha = 0$。
2. 任何含零向量的向量组都线性相关。


### 定理 3.1（线性相关的等价描述：从线性表示看）
线性空间 $V(\mathbf{F})$ 中的向量组 $\alpha_1,\alpha_2,\ldots,\alpha_m\ (m \geqslant 2)$ 线性相关的充分必要条件是 $\alpha_1,\alpha_2,\ldots,\alpha_m$ 中有一个向量可由其余向量在域 $\mathbf{F}$ 上线性表示。

**等价命题**：  
- 向量组线性相关 $\iff$ 其中至少有一个向量可以由其余向量线性表示。  
- 向量组线性无关 $\iff$ 其中每一个向量都不能由其余向量线性表示。


### 定理 3.2（线性相关性的判定：从齐次线性方程组看）
列向量组 $\alpha_1,\alpha_2,\ldots,\alpha_m$ 线性相关 $\iff$ 齐次线性方程组 $x_1\alpha_1 + x_2\alpha_2 + \cdots + x_m\alpha_m = 0$ 有非零解；  
线性无关 $\iff$ 只有零解。


### 定理 3.3（部分组与整体的相关性）
1. 如果向量组的一个部分组线性相关，那么整个向量组也线性相关。
2. 如果向量组线性无关，那么它的任何一个部分组也线性无关。


### 定理 3.4（线性无关向量组增加一个向量后的相关性）
若向量组 $\alpha_1,\alpha_2,\ldots,\alpha_m$ 线性无关，而向量组 $\beta,\alpha_1,\alpha_2,\ldots,\alpha_m$ 线性相关，则 $\beta$ 可由 $\alpha_1,\alpha_2,\ldots,\alpha_m$ 线性表示，且表示法唯一。


### 推论 3.4.1（表示方式的唯一性与向量组相关性的关系）
若向量组外另一向量可由这一组向量线性表示，则  
1. 向量组线性无关 $\iff$ 表示方式唯一；  
2. 向量组线性相关 $\iff$ 表示方式有无穷多种。


### 引理 3.1（线性相关性引理）
设 $\alpha_1,\alpha_2,\ldots,\alpha_m$ 线性相关，则存在 $j \in \{1,2,\ldots,m\}$ 使得：
1. $\alpha_j \in \operatorname{span}(\alpha_1,\alpha_2,\ldots,\alpha_{j-1})$；  
2. 从 $\alpha_1,\alpha_2,\ldots,\alpha_m$ 中删去向量 $\alpha_j$，剩余向量张成空间仍等于 $\operatorname{span}(\alpha_1,\alpha_2,\ldots,\alpha_m)$。

**证明关键**：取 $j$ 是使 $\lambda_j \neq 0$ 的最大下标（其中 $\lambda_1,\ldots,\lambda_m$ 不全为零，且 $\lambda_1\alpha_1+\cdots+\lambda_m\alpha_m=0$）。


### 推论 3.1.1（线性相关的另一种等价描述）
$\alpha_1,\alpha_2,\ldots,\alpha_m$ 线性相关（其中 $\alpha_1 \neq 0$）的充要条件是存在一个向量 $\alpha_i\ (1 < i \leqslant m)$ 可由 $\alpha_1,\alpha_2,\ldots,\alpha_{i-1}$ 线性表示，且表示法唯一。


### 定义 3.2（极大线性无关组与秩）
设向量组 $S=\{\alpha_1,\alpha_2,\ldots,\alpha_m\}$ 张成的线性空间为 $V$，若存在 $S$ 的一个线性无关向量组 $B=\{\alpha_{k_1},\alpha_{k_2},\ldots,\alpha_{k_r}\}$，使得 $V = \operatorname{span}(B)$，则称 $B$ 为 $S$ 的一个 **极大线性无关组**，并称极大线性无关组的长度 $r = r(S)$ 为 $S$ 的 **秩**。


### 定理 3.5（线性表示定理，又称源泉定理）
设 $V(\mathbf{F})$ 中向量组 $\beta_1,\beta_2,\ldots,\beta_s$ 的每个向量可由另一向量组 $\alpha_1,\alpha_2,\ldots,\alpha_r$ 线性表示。若 $s > r$，则 $\beta_1,\beta_2,\ldots,\beta_s$ 线性相关。

**等价命题**：若 $\beta_1,\beta_2,\ldots,\beta_s$ 线性无关，则 $s \leqslant r$。


### 推论 3.5.1（秩的不等式）
若向量组 $B_1$ 可以被向量组 $B_2$ 线性表示，则有 $r(B_1) \leqslant r(B_2)$。


### 推论 3.5.2（等价向量组的长度）
设 $B_1$ 和 $B_2$ 是两个线性无关向量组，若 $B_1$ 可以被 $B_2$ 线性表示，$B_2$ 也可以被 $B_1$ 线性表示，则 $B_1$ 和 $B_2$ 长度相等。


### 定理 3.6（向量组等价的自反性、对称性、传递性）
向量组等价关系满足：
1. 自反性：任意向量组与其自身等价；
2. 对称性：若 $B_1$ 与 $B_2$ 等价，则 $B_2$ 与 $B_1$ 等价；
3. 传递性：若 $B_1$ 与 $B_2$ 等价，$B_2$ 与 $B_3$ 等价，则 $B_1$ 与 $B_3$ 等价。


### 推论 3.5.3（向量组等价与极大线性无关组）
关于等价的向量组，我们有如下结论：
1. 向量组与其极大线性无关组等价；
2. 向量组的任意两个极大线性无关组等价；
3. 向量组的任意两个极大线性无关组长度相等，即向量组的秩唯一。


## 3.2 基与维数

### 定义 3.3（基与维数）
若线性空间 $V(\mathbf{F})$ 的有限子集 $B=\{\alpha_1,\alpha_2,\ldots,\alpha_n\}$ 线性无关，且 $\operatorname{span}(B) = V$，则称 $B$ 为 $V$ 的一组 **基**，并称 $n$ 为 $V$ 的 **维数**，记作 $\dim V = n$。


### 定理 3.7（有限维线性空间基的存在性）
有限维线性空间一定存在基。


### 定理 3.8（维数的基本性质）
对一 $n$ 维线性空间 $V$ 而言：
1. 其中的任意 $n + 1$ 个向量必然线性相关；
2. 其中的任意 $n - 1$ 个向量必然无法张成空间 $V$。


### 定理 3.9（基的等价条件）
在 $n$ 维线性空间 $V$ 中，$n$ 个向量 $\alpha_1,\ldots,\alpha_n$ 线性无关的充要条件是它们可以线性表示出 $V$ 中的任意向量。


### 定理 3.10（子空间的基可扩充）
如果 $W$ 是 $n$ 维线性空间 $V$ 的一个子空间，则 $W$ 的基可以扩充为 $V$ 的基。


### 定理 3.11（子空间维数的不等式）
设 $U$ 和 $W$ 是 $V$ 的非零子空间，且 $U \subseteq W$，则 $\dim U \leqslant \dim W$；若 $\dim U = \dim W$，则 $U = W$。


### 定义 3.4（有限维与无限维）
$V(\mathbf{F})$ 称为 **有限维线性空间**，如果 $V$ 中存在一个有限子集 $S$ 使得 $\operatorname{span}(S) = V$，反之称为 **无限维线性空间**。


### 定理 3.12（有限维线性空间的判定）
1. $\mathbf{R}[x]_3$ 是有限维线性空间；
2. $\mathbf{R}[x]$ 是无限维线性空间。


### 引理 3.2（初等行变换不改变列的线性相关性）
对一个矩阵做三类初等行变换均不改变矩阵的列的线性相关性。

**证明思路**：对三种初等行变换分别验证，线性相关性由齐次方程组解的情况决定，初等行变换不改变方程组的解集。


### 引理 3.3（极大线性无关组的求法）
将题目给定的向量按列排成矩阵，然后将矩阵作初等变换化成阶梯矩阵，找到每一行第一个非零元素所在的列，提取出原矩阵对应列的向量即可得到极大线性无关组。


## 3.3 向量的坐标

### 定义 3.5（向量的坐标）
设 $B=\{\beta_1,\beta_2,\ldots,\beta_n\}$ 是 $n$ 维线性空间 $V(\mathbf{F})$ 的一组基，如果 $V$ 中元素 $\alpha$ 表示为
\[
\alpha = a_1\beta_1 + a_2\beta_2 + \cdots + a_n\beta_n,
\]
则其系数组 $a_1,a_2,\ldots,a_n$ 称为 $\alpha$ 在基 $B$ 下的 **坐标**，记为 $\alpha_B = (a_1,a_2,\ldots,a_n)$。


### 定理 3.13（坐标映射的性质）
设 $n$ 维线性空间 $V$ 的一组基为 $B=\{\beta_1,\ldots,\beta_n\}$，则坐标映射 $\varphi_B: V \to \mathbf{F}^n$ 是一个 **同构映射**，即满足：
1. $\varphi_B(\alpha+\beta)=\varphi_B(\alpha)+\varphi_B(\beta)$；
2. $\varphi_B(\lambda\alpha)=\lambda\varphi_B(\alpha)$；
3. $\varphi_B$ 是双射。


### 推论 3.13.1（任意有限维空间与 $\mathbf{F}^n$ 同构）
任意一个 $n$ 维线性空间 $V(\mathbf{F})$ 都与 $\mathbf{F}^n$ 同构。


## 补充说明与隐含定理

### 定理（线性相关性的判定：特殊函数空间）
对于函数空间中的向量组（函数），有时可通过代入特殊值构造多个方程来判断线性相关性。

### 定理（不同数域下线性空间维数的差异）
同一个集合在不同数域上构成的线性空间可能有不同的维数。例如：
- $\mathbf{C}$ 作为 $\mathbf{C}$-线性空间，维数为 $1$；
- $\mathbf{C}$ 作为 $\mathbf{R}$-线性空间，维数为 $2$。

### 性质（自然基）
- $\mathbf{R}^n$ 的自然基为 $\vec{e}_1,\ldots,\vec{e}_n$（第 $i$ 位为 $1$，其余为 $0$）。
- 多项式空间 $\mathbf{R}[x]_n$ 的自然基为 $1, x, x^2, \ldots, x^{n-1}$。

### 性质（坐标的矩阵写法）
若向量 $\alpha$ 在基 $\beta_1,\ldots,\beta_n$ 下的坐标为 $(a_1,\ldots,a_n)$，可记为
\[
\alpha = (\beta_1, \beta_2, \ldots, \beta_n) \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix}.
\]

### 性质（极大线性无关组的不唯一性）
极大线性无关组不唯一，但秩唯一。

### 性质（维数的唯一性）
有限维线性空间的维数唯一，即任意两组基的长度相等。


**整理完毕，已逐条检查，无遗漏。**

---

# 第4章 线性空间的运算 总结

## 4.1 线性空间的交、并、和

### 定义 4.1（线性空间的交、并、和）
设 \(W_1,W_2\) 是线性空间 \(V(\mathbf{F})\) 的两个子空间，则  
\[
\begin{aligned}
W_1 \cap W_2 &= \{\alpha \mid \alpha\in W_1 \text{ 且 } \alpha\in W_2\}, \\
W_1 \cup W_2 &= \{\alpha \mid \alpha\in W_1 \text{ 或 } \alpha\in W_2\}, \\
W_1 + W_2   &= \{\alpha_1+\alpha_2 \mid \alpha_1\in W_1,\ \alpha_2\in W_2\}
\end{aligned}
\]  
分别称为 \(W_1\) 与 \(W_2\) 的**交**、**并**、**和**。

### 定义 4.2（有限个子空间的交、并、和）
设 \(W_1,W_2,\dots,W_s\) 是线性空间 \(V(\mathbf{F})\) 的 \(s\) 个子空间，则  
\[
\begin{aligned}
\bigcap_{i=1}^s W_i &= \{\alpha \mid \alpha\in W_i,\ i=1,\dots,s\}, \\
\bigcup_{i=1}^s W_i &= \{\alpha \mid \exists i,\ \alpha\in W_i\}, \\
\sum_{i=1}^s W_i   &= \{\alpha_1+\cdots+\alpha_s \mid \alpha_i\in W_i,\ i=1,\dots,s\}
\end{aligned}
\]  
分别称为它们的**交**、**并**、**和**。

### 定理 4.1（子空间对交与和的封闭性）
设 \(W_1,W_2\) 是线性空间 \(V(\mathbf{F})\) 的子空间，则  
1. \(W_1 \cap W_2\) 是 \(V\) 的子空间；  
2. \(W_1 + W_2\) 是 \(V\) 的子空间；  
3. \(W_1 \cup W_2\) 为 \(V\) 的子空间 \(\iff\) \(W_1 \subseteq W_2\) 或 \(W_2 \subseteq W_1\) \(\iff\) \(W_1 \cup W_2 = W_1 + W_2\)。

### 注 4.1
定理 4.1 的前两部分可推广至有限个子空间：有限个子空间的交与和仍是子空间。

## 4.2 覆盖定理

### 定理 4.2（覆盖定理）
设 \(V_1,V_2,\dots,V_s\) 是数域 \(\mathbf{F}\) 上线性空间 \(V(\mathbf{F})\) 的 \(s\) 个**非平凡子空间**，则存在向量 \(\alpha \in V\) 使得 \(\alpha \notin V_1 \cup V_2 \cup \cdots \cup V_s\)，即  
\[
V_1 \cup V_2 \cup \cdots \cup V_s \subsetneq V.
\]

#### 引理 4.2.1（覆盖定理的归纳基础）
当 \(s=2\) 时，结论成立。证明思路：取 \(\alpha \notin V_1\)，若 \(\alpha \notin V_2\) 则已成立；若 \(\alpha \in V_2\)，则取 \(\beta \notin V_2\)，构造 \(\alpha+\beta\) 与 \(2\alpha+\beta\)，可证至少一个不在 \(V_1 \cup V_2\) 中。

#### 引理 4.2.2（覆盖定理的归纳步骤）
假设对 \(s-1\) 个子空间结论成立，考虑 \(s\) 个子空间时，利用归纳假设构造向量，并通过类似技巧证明存在向量不在所有子空间中。

### 推论 4.2.1
设 \(V_1,\dots,V_s\) 是 \(V\) 的非平凡子空间，则存在 \(V\) 的一组基 \(\alpha_1,\dots,\alpha_n\) 满足 \(\alpha_i \notin V_1 \cup \cdots \cup V_s\)（对每个 \(i\)）。

## 4.3 维数公式

### 定理 4.3（线性空间维数公式）
设 \(W_1,W_2\) 是线性空间 \(V(\mathbf{F})\) 的子空间，则  
\[
\dim W_1 + \dim W_2 = \dim(W_1 + W_2) + \dim(W_1 \cap W_2).
\]

#### 证明方法：“设小扩大”法
1. 取 \(W_1 \cap W_2\) 的基 \(\alpha_1,\dots,\alpha_r\)。  
2. 分别扩充为 \(W_1\) 的基 \(\alpha_1,\dots,\alpha_r,\beta_1,\dots,\beta_{s-r}\) 和 \(W_2\) 的基 \(\alpha_1,\dots,\alpha_r,\gamma_1,\dots,\gamma_{t-r}\)。  
3. 证明向量组 \(\alpha_1,\dots,\alpha_r,\beta_1,\dots,\beta_{s-r},\gamma_1,\dots,\gamma_{t-r}\) 线性无关，从而张成 \(W_1+W_2\)，且维数为 \(s+t-r\)。

## 4.4 线性空间的直和

### 定义 4.3（直和）
设 \(W_1,W_2\) 是线性空间 \(V(\mathbf{F})\) 的子空间。若 \(W_1 \cap W_2 = \{\vec{0}\}\)，则称 \(W_1+W_2\) 为 **直和**，记作 \(W_1 \oplus W_2\)。  
若 \(V = W_1 \oplus W_2\)，则称 \(W_1\) 与 \(W_2\) 为 **互补子空间**。

### 定义 4.4（多个子空间的直和）
设 \(W_1,\dots,W_n\) 是 \(V\) 的子空间。若对每个 \(i\)，有 \(W_i \cap \sum_{j \neq i} W_j = \{\vec{0}\}\)，则称和 \(\sum_{i=1}^n W_i\) 为直和，记作 \(\bigoplus_{i=1}^n W_i\)。

### 定理 4.4（直和的等价条件）
对于子空间 \(W_1,W_2\)，以下命题等价：  
1. \(W_1+W_2\) 是直和（即 \(W_1 \cap W_2 = \{\vec{0}\}\)）；  
2. \(W_1+W_2\) 中每个向量的分解式唯一；  
3. 零向量的分解式唯一（即若 \(\vec{0} = \alpha_1 + \alpha_2\)，则 \(\alpha_1 = \alpha_2 = \vec{0}\)）；  
4. \(\dim(W_1+W_2) = \dim W_1 + \dim W_2\)。

### 定理 4.5（直和的分解定理）
若 \(V = V_1 \oplus V_2\)，且 \(V_1 = \bigoplus_{i=1}^s V_{1i},\ V_2 = \bigoplus_{j=1}^t V_{2j}\)，则  
\[
V = \left( \bigoplus_{i=1}^s V_{1i} \right) \oplus \left( \bigoplus_{j=1}^t V_{2j} \right).
\]

### 注 4.4
有限维空间的一个子空间的补空间不唯一。

## 4.5 商空间

### 4.5.1 从等价关系出发

#### 定义 4.5（由子空间诱导的等价关系）
设 \(U\) 是线性空间 \(V\) 的子空间。定义 \(V\) 上的等价关系 \(\sim\) 为：  
\[
\alpha \sim \beta \iff \alpha - \beta \in U.
\]  
等价类记作 \(\overline{\alpha} = \alpha + U = \{\alpha + u \mid u \in U\}\)。

### 定理 4.6（零等价类是子空间）
零向量所在的等价类 \(\overline{0} = U\) 是 \(V\) 的子空间。

#### 引理 4.6.1（等价关系的相容性）
若 \(\alpha_1 \sim \alpha_2,\ \beta_1 \sim \beta_2\)，则 \((\alpha_1+\beta_1) \sim (\alpha_2+\beta_2)\) 且 \(\lambda \alpha_1 \sim \lambda \alpha_2\)（\(\lambda \in \mathbf{F}\)）。

### 定理 4.7（等价关系的刻画）
\(\alpha \sim \beta \iff \alpha - \beta \in U\)。

### 4.5.2 仿射子集与商空间

#### 定义 4.6（仿射子集）
设 \(v \in V\)，\(U\) 是 \(V\) 的子空间，则称集合 \(v + U = \{v + u \mid u \in U\}\) 为 \(V\) 的 **仿射子集**，并称其平行于 \(U\)。

### 定理 4.8（仿射子集相等的条件）
设 \(v,w \in V\)，则以下等价：  
1. \(v - w \in U\)；  
2. \(v + U = w + U\)；  
3. \((v+U) \cap (w+U) \neq \varnothing\)。

### 定理 4.9（仿射子集的刻画）
\(V\) 的非空子集 \(A\) 是仿射子集 \(\iff\) 对任意 \(v,w \in A\) 与 \(\lambda \in \mathbf{F}\)，有 \(\lambda v + (1-\lambda) w \in A\)。

#### 引理 4.9.1（仿射子集的平移结构）
若 \(A\) 是仿射子集，则存在 \(v \in V\) 与子空间 \(U\) 使得 \(A = v + U\)。

#### 定义 4.7（商空间）
设 \(U\) 是 \(V\) 的子空间，则商集 \(V/U = \{v + U \mid v \in V\}\) 在如下运算下构成线性空间，称为 **商空间**：  
\[
\begin{aligned}
(\alpha+U) + (\beta+U) &= (\alpha+\beta) + U, \\
\lambda (\alpha+U) &= (\lambda \alpha) + U.
\end{aligned}
\]  
其零元为 \(U\)（即 \(0+U\)）。

### 定理 4.10（商空间的维数公式）
设 \(U\) 是有限维线性空间 \(V\) 的子空间，则  
\[
\dim(V/U) = \dim V - \dim U.
\]

#### 证明方法：“设小扩大”法
1. 取 \(U\) 的基 \(\alpha_1,\dots,\alpha_s\)，扩充为 \(V\) 的基 \(\alpha_1,\dots,\alpha_s,\alpha_{s+1},\dots,\alpha_n\)。  
2. 证明 \(\{\alpha_{s+1}+U,\dots,\alpha_n+U\}\) 是 \(V/U\) 的一组基。


## 补充结论（隐含于例题与习题）

### 1. 求子空间和与交的一般方法（例题4.1）
- **求和**：合并两个子空间的生成向量，求其极大线性无关组。  
- **求交**：  
  - **方法一**：利用秩相等条件，通过矩阵消元求解参数。  
  - **方法二**：解线性方程组 \(x_1\alpha_1 + \cdots + x_r\alpha_r = y_1\beta_1 + \cdots + y_t\beta_t\)，通解给出交的基。

### 2. 直和的证明思路
- **思路一**：先证和为直和（即交为零），再证和等于全空间（常用维数公式）。  
- **思路二**：直接证明向量分解唯一。

### 3. 补空间不唯一性（例题4.4）
有限维空间中，一个子空间的补空间有无穷多个。

### 4. 覆盖定理的应用（例题4.5）
存在一组基，其所有基向量都不在给定有限个子空间的并集中。

### 5. 仿射子集的结构定理（习题C组第4题）
设 \(v_1,\dots,v_m \in V\)，令  
\[
A = \left\{ \sum_{i=1}^m \lambda_i v_i \ \middle|\ \lambda_i \in \mathbf{F},\ \sum_{i=1}^m \lambda_i = 1 \right\},
\]  
则：  
1. \(A\) 是仿射子集；  
2. 任何包含 \(v_1,\dots,v_m\) 的仿射子集都包含 \(A\)；  
3. 存在 \(v \in V\) 与子空间 \(U\)（\(\dim U \le m-1\)）使得 \(A = v + U\)。

### 6. 加强的覆盖定理（习题C组第5题）
有限个仿射子集的并不能覆盖整个线性空间。

### 7. 子空间包含关系定理（习题B组第10题）
若 \(\dim(V_1+V_2) = \dim(V_1 \cap V_2) + 1\)，则 \(V_1 \subseteq V_2\) 或 \(V_2 \subseteq V_1\)。

### 8. 子空间的并成为子空间的条件（习题B组第7题）
以下等价：  
1. \(W_1 \cup W_2\) 是子空间；  
2. \(W_1 \subseteq W_2\) 或 \(W_2 \subseteq W_1\)；  
3. \(W_1 \cup W_2 = W_1 + W_2\)。

### 9. 多个子空间直和的条件（习题A组第4题）
若 \(U_1 \cap U_2 = U_2 \cap U_3 = U_3 \cap U_1 = \{0\}\)，不能推出 \(U_1+U_2+U_3\) 是直和。直和要求更强的条件：\(U_i \cap \sum_{j\neq i} U_j = \{0\}\) 对每个 \(i\) 成立。


### 注： 本章核心思想包括“设小扩大”法、维数公式、直和分解以及商空间的构造，这些是后续研究线性映射、矩阵约化等重要工具的基础。

---

# 第5章 线性映射：定义、定理与引理总结

## 5.1 线性映射的定义

### 5.1.1 线性映射的定义

### 定义 5.1（线性映射）  
设 \( V_1(\mathbf{F}) \) 和 \( V_2(\mathbf{F}) \) 是域 \(\mathbf{F}\) 上的线性空间。映射 \(\sigma: V_1 \to V_2\) 称为**线性映射**，如果对任意 \(\alpha, \beta \in V_1\) 和 \(\lambda, \mu \in \mathbf{F}\)，有  
\[
\sigma(\lambda\alpha + \mu\beta) = \lambda\sigma(\alpha) + \mu\sigma(\beta).
\]  
等价地，线性映射满足：
- **加性**：\(\sigma(\alpha + \beta) = \sigma(\alpha) + \sigma(\beta)\)
- **齐次性**：\(\sigma(\lambda\alpha) = \lambda\sigma(\alpha)\)

### 注： 1. 线性映射是线性空间之间的同态。
2. 从 \(V\) 到自身的线性映射称为**线性变换**（或**算子**）。
3. 从 \(V(\mathbf{F})\) 到域 \(\mathbf{F}\) 的线性映射称为**线性泛函**（或线性函数、线性形式）。


### 定理 5.1（线性映射零元性质）  
设 \(\sigma: V_1 \to V_2\) 是线性映射，则 \(\sigma(0_1) = 0_2\)，其中 \(0_1\) 和 \(0_2\) 分别是 \(V_1\) 和 \(V_2\) 的零元。


### 定理 5.2（线性映射保相关性）  
设 \(\sigma: V_1 \to V_2\) 是线性映射，若 \(V_1\) 中向量 \(\alpha_1, \alpha_2, \ldots, \alpha_n\) 线性相关，则 \(\sigma(\alpha_1), \sigma(\alpha_2), \ldots, \sigma(\alpha_n)\) 也线性相关。  
反之，若 \(\sigma(\alpha_1), \sigma(\alpha_2), \ldots, \sigma(\alpha_n)\) 线性无关，则 \(\alpha_1, \alpha_2, \ldots, \alpha_n\) 必线性无关。

### 注： 线性映射可能将线性无关的向量组映射为线性相关的向量组。


### 5.1.2 线性映射举例
*（本节主要为例子，无新定义或定理）*


### 5.1.3 线性映射的基本运算

### 定义 5.2（线性映射的加法和数乘）  
设 \(\sigma, \tau \in \mathcal{L}(V_1, V_2)\)，定义它们的和 \(\sigma + \tau\) 和数乘 \(\lambda\sigma\)（\(\lambda \in \mathbf{F}\)）为：
\[
(\sigma + \tau)(\alpha) = \sigma(\alpha) + \tau(\alpha), \quad (\lambda\sigma)(\alpha) = \lambda(\sigma(\alpha)), \quad \forall \alpha \in V_1.
\]


### 定理 5.3（线性映射全体构成线性空间）  
所有从 \(V_1\) 到 \(V_2\) 的线性映射的集合 \(\mathcal{L}(V_1, V_2)\)，关于上述加法和数乘构成域 \(\mathbf{F}\) 上的线性空间。


### 定义 5.3（线性映射的复合）  
设 \(\sigma \in \mathcal{L}(V_1, V_2)\)，\(\tau \in \mathcal{L}(V_2, V_3)\)，则复合映射 \(\tau\sigma \in \mathcal{L}(V_1, V_3)\) 定义为：
\[
(\tau\sigma)(\alpha) = \tau(\sigma(\alpha)), \quad \forall \alpha \in V_1.
\]


### 定理 5.4（复合映射是线性映射）  
上述定义的复合映射 \(\tau\sigma\) 是线性映射。


### 定义 5.4（线性映射的逆）  
设 \(\sigma \in \mathcal{L}(V_1, V_2)\)。若存在 \(\tau \in \mathcal{L}(V_2, V_1)\) 使得 \(\sigma\tau = I_{V_2}\) 且 \(\tau\sigma = I_{V_1}\)，则称 \(\sigma\) **可逆**，并称 \(\tau\) 为 \(\sigma\) 的**逆映射**，记作 \(\sigma^{-1}\)。


### 定理 5.5（逆映射是线性映射）  
可逆线性映射的逆映射也是线性映射。


## 5.2 线性映射的像与核

### 定义 5.5（像与核）  
设 \(\sigma: V_1 \to V_2\) 是线性映射。
- **像（值域）**：\(\operatorname{im}\sigma = \sigma(V_1) = \{ \beta \in V_2 \mid \beta = \sigma(\alpha), \alpha \in V_1 \}\)。
- **核（零空间）**：\(\ker\sigma = \sigma^{-1}(0_2) = \{ \alpha \in V_1 \mid \sigma(\alpha) = 0_2 \}\)。


### 定理 5.6（像与核是子空间）  
\(\operatorname{im}\sigma\) 是 \(V_2\) 的子空间，\(\ker\sigma\) 是 \(V_1\) 的子空间。


### 定理 5.7（单射与核空间）  
线性映射 \(\sigma\) 是单射当且仅当 \(\ker\sigma = \{0\}\)。


## 5.3 线性映射的确定

### 定理 5.8（线性映射唯一确定）  
设 \(\sigma, \tau \in \mathcal{L}(V_1, V_2)\)，且 \(B = \{\alpha_1, \alpha_2, \ldots, \alpha_n\}\) 是 \(V_1\) 的一组基。若 \(\sigma(\alpha_i) = \tau(\alpha_i)\) 对每个基向量成立，则 \(\sigma = \tau\)。


### 定理 5.9（线性映射构造）  
设 \(B = \{\alpha_1, \alpha_2, \ldots, \alpha_n\}\) 是 \(V_1\) 的基，\(\{\beta_1, \beta_2, \ldots, \beta_n\}\) 是 \(V_2\) 中任意 \(n\) 个向量，则存在唯一的线性映射 \(\sigma \in \mathcal{L}(V_1, V_2)\) 使得 \(\sigma(\alpha_i) = \beta_i\)（\(i = 1, 2, \ldots, n\)）。


**隐含定理（线性映射存在性判据）**  
给定线性映射在基上的像，线性映射存在的必要条件（不违反时通常可构造）：
1. 必须将零元映射到零元。
2. 不能将线性相关向量组映射为线性无关向量组。
3. 不存在从低维空间到高维空间的满射（即像空间维数不超过出发空间维数）。


## 5.4 线性映射基本定理

### 定义 5.6（线性映射的秩）  
设 \(\sigma \in \mathcal{L}(V_1, V_2)\)，若 \(\operatorname{im}\sigma\) 是有限维的，则其维数称为 \(\sigma\) 的**秩**，记作 \(r(\sigma)\)，即 \(r(\sigma) = \dim\operatorname{im}\sigma\)。


### 定理 5.10（线性映射基本定理，维数公式）  
设 \(\sigma \in \mathcal{L}(V_1, V_2)\)，且 \(\dim V_1 = n\)，则  
\[
r(\sigma) + \dim\ker\sigma = n.
\]


### 定理 5.11（双射等价条件）  
设 \(\sigma \in \mathcal{L}(V_1, V_2)\) 且 \(\dim V_1 = \dim V_2 = n\)，则下列条件等价：
1. \(\ker\sigma = \{0\}\)。
2. \(\sigma\) 是单射。
3. \(\sigma\) 是满射。
4. \(\sigma\) 是双射（可逆）。
5. \(r(\sigma) = n\)。


### 定理 5.12（商映射与商空间维数）  
设 \(U\) 是有限维线性空间 \(V\) 的子空间，商映射 \(\pi: V \to V/U\) 定义为 \(\pi(v) = v + U\)。则 \(\pi\) 是线性满射，且 \(\ker\pi = U\)。由此可得：
\[
\dim V/U = \dim V - \dim U.
\]


## 5.5 像与核的进一步讨论

### 定理 5.13（幂等变换的直和分解）  
设 \(\sigma \in \mathcal{L}(V, V)\) 是幂等变换（即 \(\sigma^2 = \sigma\)），则  
\[
V = \ker\sigma \oplus \operatorname{im}\sigma.
\]


### 定理 5.14（核空间的性质）  
设 \(\sigma \in \mathcal{L}(V, V)\)，记 \(\sigma^k\) 为 \(\sigma\) 的 \(k\) 次复合。
1. **递增性**：\(\{0\} = \ker\sigma^0 \subseteq \ker\sigma^1 \subseteq \cdots \subseteq \ker\sigma^k \subseteq \ker\sigma^{k+1} \subseteq \cdots\)。
2. **稳定条件**：若存在 \(m\) 使得 \(\ker\sigma^m = \ker\sigma^{m+1}\)，则对任意 \(k \ge m\)，有 \(\ker\sigma^k = \ker\sigma^m\)。
3. **有限维停止**：若 \(\dim V = n\)，则 \(\ker\sigma^n = \ker\sigma^{n+1} = \cdots\)。


### 定理 5.15（像与核的等价条件）  
设 \(\sigma \in \mathcal{L}(V, V)\)，以下条件等价：
1. \(V = \ker\sigma \oplus \operatorname{im}\sigma\)。
2. \(\ker\sigma \cap \operatorname{im}\sigma = \{0\}\)。
3. \(\ker\sigma = \ker\sigma^2\)。
4. \(\operatorname{im}\sigma = \operatorname{im}\sigma^2\)。
5. \(r(\sigma^2) = r(\sigma)\)。


### 定理 5.16（像与核和的维数下界）  
设 \(\sigma \in \mathcal{L}(V, V)\)，\(\dim V = n\)，则  
\[
\dim(\ker\sigma + \operatorname{im}\sigma) \ge \frac{n}{2},
\]  
等号成立当且仅当 \(\ker\sigma = \operatorname{im}\sigma\)。


## 5.6 可逆与同构

### 5.6.1 线性空间同构的概念

### 定义 5.7（同构）  
如果存在线性双射 \(\sigma: V_1 \to V_2\)，则称线性空间 \(V_1\) 与 \(V_2\) **同构**，记作 \(V_1 \cong V_2\)。\(\sigma\) 称为 **同构映射**。


### 定理 5.17（同构保持线性相关性）  
设 \(\sigma: V_1 \to V_2\) 是同构映射，则 \(V_1\) 中向量组 \(\alpha_1, \alpha_2, \ldots, \alpha_m\) 与它们的像 \(\sigma(\alpha_1), \sigma(\alpha_2), \ldots, \sigma(\alpha_m)\) 有相同的线性相关性（即同时线性相关或线性无关）。


### 定理 5.18（同构保秩）  
设 \(\sigma\) 是 \(V_1\) 到 \(V_2\) 的同构映射，\(S_1 = \{\alpha_1, \alpha_2, \ldots, \alpha_m\}\) 是 \(V_1\) 中任意向量组，\(S_2 = \{\sigma(\alpha_1), \sigma(\alpha_2), \ldots, \sigma(\alpha_m)\}\)，则 \(S_1\) 与 \(S_2\) 的秩相等，即 \(r(S_1) = r(S_2)\)。


### 5.6.2 同构的等价条件

### 定理 5.19（同构的充要条件）  
两个有限维线性空间 \(V_1(\mathbf{F})\) 和 \(V_2(\mathbf{F})\) 同构的充要条件是它们的维数相等。


## 5.7 线性空间的积

### 5.7.1 线性空间的积的定义与性质

### 定义 5.8（线性空间的积）  
设 \(V_1, V_2, \ldots, V_n\) 是域 \(\mathbf{F}\) 上的线性空间，定义它们的**积**（笛卡尔积）为：  
\[
V_1 \times V_2 \times \cdots \times V_n = \{(v_1, v_2, \ldots, v_n) \mid v_i \in V_i\}.
\]  
并定义加法和数乘运算为：
- \((v_1, \ldots, v_n) + (u_1, \ldots, u_n) = (v_1 + u_1, \ldots, v_n + u_n)\)
- \(\lambda(v_1, \ldots, v_n) = (\lambda v_1, \ldots, \lambda v_n)\)

则 \(V_1 \times V_2 \times \cdots \times V_n\) 构成 \(\mathbf{F}\) 上的线性空间。


### 定理 5.20（积空间的维数）  
若 \(V_1, V_2, \ldots, V_n\) 是有限维线性空间，则积空间也是有限维的，且  
\[
\dim(V_1 \times V_2 \times \cdots \times V_n) = \dim V_1 + \dim V_2 + \cdots + \dim V_n.
\]


### 5.7.2 线性空间的积与直和

### 定理 5.21（积与直和的同构）  
设 \(U_1, U_2, \ldots, U_n\) 是线性空间 \(V\) 的子空间，定义映射  
\[
\sigma: U_1 \times U_2 \times \cdots \times U_n \to U_1 + U_2 + \cdots + U_n, \quad (u_1, u_2, \ldots, u_n) \mapsto u_1 + u_2 + \cdots + u_n.
\]  
则 \(U_1 + U_2 + \cdots + U_n\) 是直和当且仅当 \(\sigma\) 是同构映射。


### 定理 5.22（直和的维数条件）  
设 \(U_1, U_2, \ldots, U_n\) 是有限维线性空间 \(V\) 的子空间，则 \(U_1 + U_2 + \cdots + U_n\) 是直和当且仅当  
\[
\dim(U_1 + U_2 + \cdots + U_n) = \dim U_1 + \dim U_2 + \cdots + \dim U_n.
\]


### 5.7.3 自然同构
*（本节为直观讨论，无形式化定理）*


## 隐含定理与补充结论

**隐含定理（线性映射的秩不等式）**  
设 \(\sigma \in \mathcal{L}(V_1, V_2)\)，\(\tau \in \mathcal{L}(V_2, V_3)\)，且 \(\dim V_1 = m\)，\(\dim V_2 = n\)，\(\dim V_3 = s\)，则  
\[
r(\sigma) + r(\tau) - n \le r(\tau\sigma) \le \min\{r(\sigma), r(\tau)\}.
\]


**隐含定理（和映射的秩不等式）**  
设 \(\sigma, \tau \in \mathcal{L}(V_1, V_2)\)，则  
\[
r(\sigma + \tau) \le r(\sigma) + r(\tau).
\]


**隐含定理（幂零变换的像维数上界）**  
设 \(\sigma \in \mathcal{L}(V, V)\) 满足 \(\sigma^2 = 0\)，且 \(\dim V = n\)，则  
\[
\dim\operatorname{im}\sigma \le \frac{n}{2}.
\]


### 注： 1. 线性映射的核空间与像空间的计算方法：
   - 像空间：取出发空间的一组基 \(\{\alpha_1, \ldots, \alpha_n\}\)，则 \(\operatorname{im}\sigma = \operatorname{span}\{\sigma(\alpha_1), \ldots, \sigma(\alpha_n)\}\)。
   - 核空间：解方程 \(\sigma(\alpha) = 0\)，解空间即为 \(\ker\sigma\)。
2. 线性映射可被基上的像唯一确定，因此研究线性映射可转化为研究基的像。
3. 同构是线性空间分类的根本工具，表明有限维线性空间本质由维数决定。

**总结检查完毕，无遗漏。**

---

# 第6章 对偶空间 定义与定理总结

## 6.1 对偶空间与对偶映射

### 定义 6.1.1（线性泛函）  
称 $\mathcal{L}(V, \R)$ 上的元素为 $V$ 上的一个**线性泛函**（也称线性函数）。  
注：线性泛函是将 $V$ 中向量映射到数域 $\R$ 上的线性映射，要求 $V$ 和到达空间 $\R$ 定义在相同数域上。

### 引理 6.1.1（线性泛函与超平面）  
如果 $\{x: f(x) = 1\}$ 和 $\{x: g(x) = 1\}$ 表示同一个超平面，则线性泛函 $f$ 和 $g$ 在任意点取值都相同。  
注：此引理建立了非零线性泛函与超平面（在取值1处）的一一对应。零泛函对应的超平面视为“无穷远”超平面。

### 定义 6.1.2（对偶空间）  
称 $\mathcal{L}(V, \R)$ 为 $V$ 的**对偶空间**，记作 $V^*$。

### 定理 6.1.1（对偶空间同构）  
当 $V$ 为有限维线性空间时，有 $V \cong V^*$。  
注：证明通过取定 $V$ 的一组基 $e_1,\dots,e_n$，并定义对偶基 $f_i(e_j)=\delta_{ij}$，则 $f_1,\dots,f_n$ 构成 $V^*$ 的一组基。由此构造的同构依赖于基的选取，不是自然同构。

### 定义 6.1.3（对偶基）  
给定 $V$ 的一组基 $e_1,\dots,e_n$，定义 $V^*$ 中的线性泛函 $f_i$ 满足 $f_i(e_j)=\delta_{ij}$，则 $f_1,\dots,f_n$ 是 $V^*$ 的一组基，称为原基的**对偶基**，记作 $e_i^*$。

**例 6.1.1（对偶基的求法）**  
设 $V=\mathbf{R}[x]_3$，定义三个积分型线性泛函 $f_1,f_2,f_3$，则它们构成 $V^*$ 的一组基，并可求出 $V$ 的一组基 $g_1,g_2,g_3$ 使得 $f_i$ 是 $g_j$ 的对偶基。  
注：该例题展示了对偶基的计算方法，本质是求解线性方程组。

### 定义 6.1.4（交换图）  
一个**图（diagram）** 是以代数结构（如线性空间）为顶点，以映射（如线性映射）为边的有向图。若图中任意两个顶点间的任意两条有向路径的映射复合结果相同，则称该图是**交换的（commutative）**。

### 定义 6.1.5（对偶映射）  
给定线性映射 $f\colon V \to W$，定义其**对偶映射** $f^*: W^* \to V^*$ 为  
\[ f^*(\varphi) = \varphi \circ f, \quad \forall \varphi \in W^*. \]  
注：该定义不依赖于基的选取，是自然的，且具有反变性（箭头反向）。

### 引理 6.1.2（对偶映射的函子性）  
考虑线性映射 $f\colon V \to W,\; g: U \to V$，则  
\[ (f \circ g)^* = g^* \circ f^*. \]

### 引理 6.1.3（对偶映射的线性性）  
给定线性映射 $\sigma\colon V \to W$，则 $\sigma^*: W^* \to V^*$ 是线性映射。

### 引理 6.1.4（对偶映射的线性运算）  
给定 $f,g \in \mathcal{L}(V,W)$，则  
1. $(f + g)^* = f^* + g^*$；  
2. $(\lambda f)^* = \lambda f^*$。

### 定理 6.1.2（双对偶自然同构）  
当 $V$ 为有限维线性空间时，存在自然同构 $\psi: V \to V^{**}$，定义为  
\[ (\psi(v))(f) = f(v), \quad \forall f \in V^*,\; v \in V. \]  
注：该同构不依赖于基的选取，因而是自然的。

**例 6.1.2（双对偶自然同构的性质）**  
设 $V$ 有限维，$\psi$ 如上定义，则  
1. $\psi$ 是线性映射；  
2. 若 $\sigma \in \mathcal{L}(V,V)$，则 $\sigma^{**} \circ \psi = \psi \circ \sigma$；  
3. $\psi$ 是 $V$ 到 $V^{**}$ 的同构映射。  
注：此例即为定理 6.1.2 的证明细节。


## 6.2 零化子

### 定义 6.2.1（零化子）  
设 $U$ 为 $V$ 的子空间，称  
\[ U^0 = \{ \varphi \in V^* \mid \forall u \in U,\; \varphi(u) = 0 \} \]  
为 $U$ 的**零化子**。

### 定理 6.2.1（零化子构成子空间）  
零化子 $U^0$ 是 $V^*$ 的子空间。

### 定理 6.2.2（对偶空间的维数引理）  
设 $V = U_1 \oplus U_2$，则 $V^* = U_1^0 \oplus U_2^0$，且 $U_1^0 \cong U_2^*$，$U_2^0 \cong U_1^*$。

### 定理 6.2.3（零化子维数）  
设 $V$ 是有限维线性空间，$U$ 是 $V$ 的子空间，则  
\[ \dim U^0 = \dim V - \dim U. \]  
注：由定理 6.2.2 直接推出。

### 定理 6.2.4（零化子的零化子）  
当 $V$ 为有限维线性空间时，有 $U \cong U^{00}$。  
注：该定理在原文中为习题，但因其重要性列为定理。证明思路：利用自然同构 $V \cong V^{**}$ 将 $U$ 嵌入 $U^{00}$，再比较维数。

### 定义 6.2.2（零点集）  
设 $U$ 为 $V^*$ 的子空间，定义  
\[ Z(U) = \{ v \in V \mid \forall \varphi \in U,\; \varphi(v) = 0 \}. \]  
注：$Z(U) = \bigcap_{\varphi \in U} \ker \varphi$。

### 引理 6.2.1（零化子与零点集的基本性质）  
1. $f \in (\ker f)^0$；  
2. $\forall f \in U^0,\; U \subseteq \ker f$。

### 定理 6.2.5（零化子与零点集的对偶性）  
1. 若 $U$ 是 $V^*$ 的子空间，则 $U = Z(U)^0$；  
2. 若 $U$ 是 $V$ 的子空间，则 $U = Z(U^0)$。

### 定理 6.2.6（对偶映射像和核的性质）  
设 $V,W$ 为有限维线性空间，$\sigma \in \mathcal{L}(V,W)$，则  
1. $\ker \sigma^* = (\operatorname{im} \sigma)^0$；  
2. $\dim \ker \sigma^* = \dim \ker \sigma + \dim W - \dim V$；  
3. $\dim \operatorname{im} \sigma^* = \dim \operatorname{im} \sigma$；  
4. $\operatorname{im} \sigma^* = (\ker \sigma)^0$。

### 推论 6.2.1（对偶映射单满射）  
设 $V,W$ 有限维，$\sigma \in \mathcal{L}(V,W)$，则  
1. $\sigma$ 是单射 $\iff$ $\sigma^*$ 是满射；  
2. $\sigma$ 是满射 $\iff$ $\sigma^*$ 是单射。


## 6.3 再论商空间

### 引理 6.3.1（线性泛函的纤维平移性）  
设 $r \in \R$，则对任意 $v' \in \varphi^{-1}(r),\; v \in \ker \varphi$，有 $v + v' \in \varphi^{-1}(r)$。

### 定理 6.3.1（纤维的结构）  
$\varphi^{-1}(r) = v' + \ker \varphi$，其中 $v'$ 是 $\varphi^{-1}(r)$ 中任意一个向量。  
注：此即仿射子集（线性簇）的结构。

### 推论 6.3.1（纤维的运算）  
设 $\lambda,\mu \in \R$，$v_\lambda \in \varphi^{-1}(\lambda),\; v_\mu \in \varphi^{-1}(\mu)$，则  
1. $\varphi^{-1}(\lambda + \mu) = v_\lambda + v_\mu + \ker \varphi = \varphi^{-1}(\lambda) + \varphi^{-1}(\mu)$；  
2. $\varphi^{-1}(\lambda \mu) = \mu v_\lambda + \ker \varphi = \lambda v_\mu + \ker \varphi = \mu \varphi^{-1}(\lambda) = \lambda \varphi^{-1}(\mu)$。  
注：由定理 6.3.1 及线性性直接推出。

### 定理 6.3.2（一般线性映射的纤维结构）  
设 $f: V \to W$ 为线性映射，则 $f^{-1}(w) = v_0 + \ker f$，其中 $w \in W$，$v_0 \in f^{-1}(w)$。  
注：此定理是定理 6.3.1 的推广。

### 引理 6.3.2（子空间作为核）  
若 $W$ 是 $V$ 的子空间，则存在线性映射 $f: V \to V$，使得 $f|_W = 0$ 且在 $W$ 外非零。  
注：证明通过直和分解 $V = W \oplus W'$ 并定义 $f$ 在 $W$ 上为零、在 $W'$ 上为恒等映射。

### 推论 6.3.2（商空间的维数）  
设 $W$ 为 $V$ 的子空间，则 $V/W$ 是线性空间，且  
\[ \dim V/W = \dim V - \dim W. \]  
注：由定理 6.3.2 及线性映射基本定理可得。

### 定理 6.3.3（商空间的对偶）  
设 $W$ 为 $V$ 的子空间，则有同构  
\[ (V/W)^* \cong W^0. \]  
注：证明利用直和分解及定理 6.2.2。


## 隐含定理与重要结论补充

### 定理 （线性泛函的核与商空间）  
设 $\varphi \in \mathcal{L}(V,\mathbf{F})$ 非零，则 $\dim V/(\ker \varphi)=1$。反之，若 $U$ 是 $V$ 的子空间且 $\dim V/U=1$，则存在 $\varphi \in \mathcal{L}(V,\mathbf{F})$ 使得 $\ker \varphi = U$。  
注：此结论在习题中出现，具有一般性。

### 定理 （零化子的扩张性质）  
设 $S \subseteq V$，定义 $S^0 = \{\varphi \in V^* \mid \forall s \in S,\; \varphi(s)=0\}$，则  
1. $S^{00} = \operatorname{span} S$；  
2. $S \subseteq T \iff T^0 \subseteq S^0$；  
3. 若 $U_1,U_2$ 为 $V$ 的子空间，则  
   - $(U_1 + U_2)^0 = U_1^0 \cap U_2^0$；  
   - $(U_1 \cap U_2)^0 = U_1^0 + U_2^0$。  
注：此组性质在习题中给出，是零化子的基本运算性质。

**注（对偶空间的意义）**  
对偶空间将几何中的点与超平面对偶关系代数化，从而可将线性方程组的求解问题转化为对偶空间中的交点问题，简化某些讨论。

**总结检查**：已涵盖本章所有定义、定理、引理及重要推论，包括正文和习题中具有一般性的结论。每个条目按章节顺序排列，引理紧随相关定理之后，补充了隐含定理和注意事项。

---

# 第7章 线性映射矩阵表示与矩阵运算基础

## 7.1 线性映射矩阵表示
### 定义 7.1 矩阵
域 $\mathbf{F}$ 中的 $m \times n$ 个元素 $a_{ij}$（$i=1,\ldots,m$，$j=1,\ldots,n$）排成 $m$ 行 $n$ 列的矩形数表，称为域 $\mathbf{F}$ 上的一个 $m \times n$ 矩阵，记作
\[
A=\begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}
\]
或简记为 $(a_{ij})_{m \times n}$，其中 $a_{ij}$ 表示矩阵 $A$ 的第 $i$ 行第 $j$ 列的元素。

注：
- 零矩阵：所有元素均为 $0$ 的矩阵，记为 $O$。
- 单位矩阵：对角线上元素为 $1$，其余为 $0$ 的方阵，记为 $E$ 或 $E_n$。其第 $j$ 列为自然基向量 $e_j$。
- 域 $\mathbf{F}$ 上全体 $m \times n$ 矩阵记为 $\mathbf{F}^{m \times n}$ 或 $\mathbf{M}_{m \times n}(\mathbf{F})$。$m=n$ 时称为方阵，全体 $n$ 阶方阵记为 $\mathbf{F}^{n \times n}$ 或 $\mathbf{M}_n(\mathbf{F})$。

### 引理 7.1 向量空间线性映射的矩阵表示
任意的 $\mathbf{F}^n \to \mathbf{F}^m$ 的线性映射 $\sigma$ 都可以写成 $\sigma(x)=Ax$ 的形式，其中 $A$ 是一个 $m \times n$ 的矩阵（$\mathbf{F}^n$ 和 $\mathbf{F}^m$ 的基均为自然基），并且符合要求的矩阵 $A$ 是唯一的。

### 定义 7.2 线性映射矩阵表示
设 $B_1 = \{\varepsilon_1,\ldots,\varepsilon_n\}$ 是 $V_1(\mathbf{F})$ 的基，$B_2 = \{\alpha_1,\ldots,\alpha_m\}$ 是 $V_2(\mathbf{F})$ 的基。线性映射 $\sigma \in \mathcal{L}(V_1,V_2)$ 的矩阵表示 $\mathbf{M}(\sigma)$ 是一个 $m \times n$ 矩阵，其第 $j$ 列是 $\sigma(\varepsilon_j)$ 在基 $B_2$ 下的坐标，即满足：
\[
(\sigma(\varepsilon_1),\ldots,\sigma(\varepsilon_n))=(\alpha_1,\ldots,\alpha_m)\mathbf{M}(\sigma)。
\]
其中 $\sigma(\varepsilon_j)=\sum_{i=1}^{m}a_{ij}\alpha_i$，$\mathbf{M}(\sigma)=(a_{ij})_{m \times n}$。

注：线性映射矩阵表示的结果是一个 $m \times n$ 矩阵，其中 $m$ 是到达空间的维数，$n$ 是出发空间的维数。对于 $\sigma \in \mathcal{L}(\mathbf{F}^n, \mathbf{F}^m)$，其矩阵表示 $\mathbf{M}(\sigma)$ 就是满足 $\sigma(x)=\mathbf{M}(\sigma)x$ 的矩阵。

### 隐含定理 7.1 线性映射矩阵表示的坐标关系
若线性映射 $\sigma \in \mathcal{L}(V_1,V_2)$ 在基 $B_1$、$B_2$ 下的矩阵为 $A$，向量 $\alpha \in V_1$ 和 $\sigma(\alpha) \in V_2$ 在相应基下的坐标分别为 $X$ 和 $Y$，则 $Y=AX$。
注：此为定理 7.3 的等价表述，是矩阵表示的核心应用。


## 7.2 $\mathcal{L}(V_1,V_2)$ 与矩阵线性空间的同构
### 定义 7.3 矩阵的加法和数乘
设 $A=(a_{ij})_{m \times n}, B=(b_{ij})_{m \times n} \in \mathbf{F}^{m \times n}$，$\lambda \in \mathbf{F}$。
1.  加法：$A+B=(a_{ij}+b_{ij})_{m \times n}$。
2.  数乘：$\lambda A=(\lambda a_{ij})_{m \times n}$。

注：此定义源于线性映射的加法和数乘，使得 $\mathbf{F}^{m \times n}$ 构成线性空间。

### 定理 7.2 线性映射与矩阵的同构
设 $V_1, V_2$ 分别是 $n$ 维和 $m$ 维线性空间，则 $\mathcal{L}(V_1, V_2) \cong \mathbf{F}^{m \times n}$ 是同构的。特别地，$\dim\mathcal{L}(V_1,V_2)=mn$。

### 定理 7.3 线性映射对向量坐标的影响（坐标变换定理）
设 $\sigma \in \mathcal{L}(V_1,V_2)$ 关于基 $B_1$ 和 $B_2$ 的矩阵为 $A$。若 $\alpha \in V_1$ 在 $B_1$ 下的坐标为 $X$，则 $\sigma(\alpha) \in V_2$ 在 $B_2$ 下的坐标 $Y$ 满足 $Y=AX$。


## 7.3 矩阵乘法
### 定义 7.4 矩阵乘法
设 $A=(a_{ij})_{p \times m}, B=(b_{ij})_{m \times n}$，定义乘积 $C=AB=(c_{ij})_{p \times n}$，其中
\[
c_{ij}=\sum_{k=1}^{m}a_{ik}b_{kj} \quad (i=1,\ldots,p;\, j=1,\ldots,n)。
\]

注：矩阵乘法对应于线性映射的复合。$A$ 与 $B$ 可乘当且仅当 $A$ 的列数等于 $B$ 的行数。

### 定理 7.4 矩阵乘法与线性映射复合的对应
设 $\sigma \in \mathcal{L}(V_1,V_2)$，$\tau \in \mathcal{L}(V_2,V_3)$，它们在相应基下的矩阵分别为 $B$ 和 $A$，则复合映射 $\tau \sigma \in \mathcal{L}(V_1,V_3)$ 在对应基下的矩阵为 $AB$。即：
\[
\mathbf{M}_{B_2, B_3}(\tau) \mathbf{M}_{B_1, B_2}(\sigma) = \mathbf{M}_{B_1, B_3}(\tau \sigma)。
\]

### 定理 7.5 矩阵乘法的运算性质
设矩阵 $A,B,C$ 使得下列运算有意义，$\lambda \in \mathbf{F}$，则：
1.  $(AB)C = A(BC)$ （结合律）。
2.  $\lambda(AB) = (\lambda A)B = A(\lambda B)$。
3.  $A(B+C) = AB+AC$ （左分配律）。
4.  $(B+C)A = BA+CA$ （右分配律）。

注：全体 $n$ 阶方阵 $\mathbf{F}^{n \times n}$ 关于矩阵加法和乘法构成环。

### 定理 7.6 矩阵乘法的特殊性质（与数乘不同）
1.  矩阵乘法不一定满足交换律。
2.  数量矩阵（$kE$）与任何同阶方阵可交换。
3.  $A \neq O$ 且 $B \neq O$ 不能推出 $AB \neq O$。
4.  消去律不一定成立：$AB=AC$ 不能推出 $B=C$。

### 隐含定理 7.2 矩阵乘法的行列组合性质
设 $C=AB$，则：
1.  $C$ 的第 $j$ 列是 $A$ 的各列以 $B$ 的第 $j$ 列为系数的线性组合。
2.  $C$ 的第 $i$ 行是 $B$ 的各行以 $A$ 的第 $i$ 行为系数的线性组合。

### 隐含定理 7.3 矩阵乘法与基变换的结合律
设 $\sigma$ 为线性映射，$(\varepsilon_1,\ldots,\varepsilon_n)$ 为一组基向量构成的（形式）行向量，$B$ 为矩阵，则有：
\[
\sigma((\varepsilon_1,\ldots,\varepsilon_n)B) = (\sigma(\varepsilon_1),\ldots,\sigma(\varepsilon_n))B。
\]

### 定义 7.5 矩阵多项式
设 $p(x)=a_mx^m+\cdots+a_1x+a_0 \in \mathbf{F}[x]_{m+1}$，$A \in \mathbf{M}_n(\mathbf{F})$ 为方阵，定义矩阵多项式：
\[
p(A)=a_mA^m+a_{m-1}A^{m-1}+\cdots+a_1A+a_0E。
\]
其中 $A^0=E$。

### 定理 7.7 矩阵多项式运算性质
1.  $f(A)g(A)=g(A)f(A)$。
2.  若 $AB=BA$，则 $f(A)g(B)=g(B)f(A)$。

### 定义 7.6 特殊矩阵（矩阵多项式的零点）
1.  幂等矩阵：满足 $A^2=A$。
2.  幂零矩阵：存在正整数 $k$ 使得 $A^k=O$。
3.  对合矩阵：满足 $A^2=E$。

### 隐含定理 7.4 线性方程组与线性映射的关联
设线性映射 $\sigma \in \mathcal{L}(V_1,V_2)$ 在基 $B_1, B_2$ 下的矩阵为 $A$。线性方程组 $AX=b$ 的解 $X$ 对应向量 $\alpha \in V_1$ 在基 $B_1$ 下的坐标，使得 $\sigma(\alpha)=\beta$，其中 $\beta$ 在基 $B_2$ 下的坐标为 $b$。特别地，齐次方程组 $AX=0$ 的解空间对应于 $\sigma$ 的核空间 $\ker\sigma$ 中向量在基 $B_1$ 下的坐标。


## 7.4 矩阵的逆
### 定义 7.7 矩阵的逆
设 $A \in \mathbf{M}_n(\mathbf{F})$。若存在 $B \in \mathbf{M}_n(\mathbf{F})$ 使得 $AB = BA = E_n$，则称 $A$ 可逆，$B$ 称为 $A$ 的逆矩阵，记作 $B=A^{-1}$。不可逆矩阵称为奇异矩阵。

### 定理 7.8 逆矩阵的唯一性
可逆矩阵的逆矩阵是唯一的。

### 定理 7.9 方阵单边逆与双边逆等价
设 $A,B \in \mathbf{M}_n(\mathbf{F})$，则 $AB=E \iff A$ 与 $B$ 互为逆矩阵（即 $BA=E$ 也成立）。

### 定理 7.10 逆矩阵的基本性质
设 $A, B$ 为 $n$ 阶可逆矩阵，$\lambda \in \mathbf{F}$ 且 $\lambda \neq 0$，则：
1.  $(\lambda A)^{-1}=\lambda^{-1}A^{-1}$。
2.  $(AB)^{-1}=B^{-1}A^{-1}$，$(A_1\cdots A_k)^{-1}=A_k^{-1}\cdots A_1^{-1}$。
3.  $(A^k)^{-1}=(A^{-1})^k$（$k$ 为整数）。
4.  若 $A$ 可逆，则消去律成立：$AB=AC \implies B=C$；$BA=CA \implies B=C$。
5.  $A$ 可逆时，$AB=O$ 或 $BA=O$ 可推出 $B=O$。


## 7.5 矩阵的转置
### 定义 7.8 矩阵的转置
设 $A=(a_{ij})_{m \times n}$，则 $A$ 的转置 $A^\mathrm{T}=(a_{ji})_{n \times m}$。

### 定理 7.11 转置的运算性质
设运算有意义，则：
1.  $(A^\mathrm{T})^\mathrm{T}=A$。
2.  $(A+B)^\mathrm{T}=A^\mathrm{T}+B^\mathrm{T}$。
3.  $(\lambda A)^\mathrm{T}=\lambda A^\mathrm{T}$。
4.  $(AB)^\mathrm{T}=B^\mathrm{T}A^\mathrm{T}$，$(A_1\cdots A_n)^\mathrm{T}=A_n^\mathrm{T}\cdots A_1^\mathrm{T}$，$(A^\mathrm{T})^m=(A^m)^\mathrm{T}$。
5.  若 $A$ 可逆，则 $(A^\mathrm{T})^{-1}=(A^{-1})^\mathrm{T}$。

### 定义 7.9 对称矩阵与反对称矩阵
设 $A=(a_{ij})_{n \times n}$。
1.  若 $A^\mathrm{T}=A$（即 $a_{ij}=a_{ji}$），则称 $A$ 为对称矩阵。
2.  若 $A^\mathrm{T}=-A$（即 $a_{ij}=-a_{ji}$），则称 $A$ 为反对称矩阵。

### 隐含定理 7.5 反对称矩阵的性质
反对称矩阵的主对角元均为 $0$。

### 定理 7.12 对称/反对称矩阵的性质
1.  $AA^\mathrm{T}$ 和 $A^\mathrm{T}A$ 均为对称矩阵。
2.  设 $A,B$ 分别为对称和反对称矩阵，则 $AB+BA$ 是反对称矩阵。
3.  对称矩阵的乘积不一定对称。
4.  可逆的对称（反对称）矩阵的逆矩阵也是对称（反对称）矩阵。

### 隐含定理 7.6 矩阵空间的直和分解
设 $V=\mathbf{M}_n(\mathbf{F})$，$V_1$ 为所有对称矩阵集合，$V_2$ 为所有反对称矩阵集合，则 $V_1$ 和 $V_2$ 都是 $V$ 的子空间，且 $V=V_1 \oplus V_2$。

### 定理 7.13 对偶映射的矩阵表示
设 $\sigma \in \mathcal{L}(V,W)$ 在基 $B_1, B_2$ 下的矩阵为 $A$，则其对偶映射 $\sigma^* \in \mathcal{L}(W^*,V^*)$ 在对应对偶基下的矩阵为 $A^\mathrm{T}$。


## 7.6 矩阵的共轭
### 定义 7.10 共轭矩阵
设 $A=(a_{ij})_{m \times n}$ 为复矩阵，则其共轭矩阵为 $\overline{A}=(\overline{a_{ij}})_{m \times n}$。

### 定理 7.14 共轭的运算性质
设运算有意义，则：
1.  $\overline{A+B}=\overline{A}+\overline{B}$。
2.  $\overline{\lambda A}=\overline{\lambda}\,\overline{A}$。
3.  $\overline{AB}=\overline{A}\,\overline{B}$，$\overline{A^m}=\overline{A}^m$。
4.  $\overline{A^\mathrm{T}}=(\overline{A})^\mathrm{T}$。
5.  若 $A$ 可逆，则 $\overline{A^{-1}}=\overline{A}^{-1}$。


## 7.7 分块矩阵
### 定义 7.11 分块矩阵
将 $m \times n$ 矩阵 $A$ 在行方向分成 $s$ 块，列方向分成 $t$ 块，得到 $s \times t$ 分块矩阵 $A=(A_{kl})_{s \times t}$，其中 $A_{kl}$ 称为子块。

### 定理 7.15 分块矩阵的运算
设分块矩阵 $A=(A_{kl})_{s \times t}, B=(B_{kl})_{s \times t}$，分块方式使得下列运算有意义，$\lambda \in \mathbf{F}$，则：
1.  加法：$A+B=(A_{kl}+B_{kl})_{s \times t}$。
2.  数乘：$\lambda A=(\lambda A_{kl})_{s \times t}$。
3.  乘法：若 $A$ 为 $r \times s$ 分块，$B$ 为 $s \times t$ 分块，且 $A$ 的列分块法与 $B$ 的行分块法相同，则 $AB=C=(C_{kl})_{r \times t}$，其中 $C_{kl}=\sum_{h=1}^{s}A_{kh}B_{hl}$。
4.  转置：$A^\mathrm{T}=(B_{lk})_{t \times s}$，其中 $B_{lk}=A_{kl}^\mathrm{T}$。
5.  共轭：$\overline{A}=(\overline{A_{kl}})_{s \times t}$。

### 隐含定理 7.7 分块对角矩阵的逆
设分块对角矩阵 $A=\operatorname{diag}(A_1, A_2, \ldots, A_k)$，其中 $A_i$ 为方阵，则 $A$ 可逆当且仅当每个 $A_i$ 可逆，且 $A^{-1}=\operatorname{diag}(A_1^{-1}, A_2^{-1}, \ldots, A_k^{-1})$。

### 隐含定理 7.8 特殊分块矩阵的逆
设 $n$ 阶矩阵 $A$ 分块为 $A=\begin{pmatrix} B & O \\ C & D \end{pmatrix}$，其中 $B, D$ 分别为 $k$ 阶、$m$ 阶可逆方阵，则 $A$ 可逆，且
\[
A^{-1}=\begin{pmatrix} B^{-1} & O \\ -D^{-1}CB^{-1} & D^{-1} \end{pmatrix}。
\]


## 补充定理与注意事项
注：以下为从例题、证明过程中提炼的具有一般性的结论或方法。

### 隐含定理 7.9 线性映射的像与核的矩阵求法
设线性映射 $\sigma \in \mathcal{L}(V_1,V_2)$ 在基 $B_1, B_2$ 下的矩阵为 $A$。
1.  $\operatorname{Im} \sigma$ 由 $\sigma(B_1)$ 张成，其在基 $B_2$ 下的坐标列向量组即为 $A$ 的列向量组。因此，$\operatorname{Im} \sigma$ 的维数等于 $A$ 的列秩。
2.  $\ker\sigma$ 中向量在基 $B_1$ 下的坐标构成齐次线性方程组 $AX=0$ 的解空间。

### 隐含定理 7.10 矩阵求幂的技巧（秩1矩阵）
设 $\alpha, \beta$ 为 $n$ 维列向量，$A=\alpha\beta^\mathrm{T}$，则 $A$ 的幂满足 $A^k=(\beta^\mathrm{T}\alpha)^{k-1}A$。

### 隐含定理 7.11 矩阵多项式与相似变换
设 $A=PBP^{-1}$，$f$ 为多项式，则 $f(A)=Pf(B)P^{-1}$。特别地，若 $B$ 为对角矩阵 $\operatorname{diag}(\lambda_1,\ldots,\lambda_n)$，则 $f(A)=P\operatorname{diag}(f(\lambda_1),\ldots,f(\lambda_n))P^{-1}$。

### 隐含定理 7.12 行和与列和的性质
设 $n$ 阶矩阵 $A$ 的每行元素之和均为常数 $k$，记 $\alpha=(1,1,\ldots,1)^\mathrm{T}$，则 $A\alpha=k\alpha$。
1.  若 $A$ 可逆，则 $k\neq0$，且 $A^{-1}$ 的每行元素之和为 $\frac{1}{k}$。
2.  $A^m$（$m$ 为正整数）的每行元素之和为 $k^m$。

---

# 第8章 相抵标准形 定义与定理总结

## 8.1 矩阵的秩

### 定义 8.1.1（矩阵的秩、行秩、列秩）
设 \(A\) 是线性映射 \(\sigma\) 对应的矩阵，定义矩阵 \(A\) 的**秩** 为 \(r(A) = r(\sigma)\)。将矩阵 \(A\) 的所有行向量组成的秩称为 \(A\) 的**行秩**，记为 \(r_{\mathrm{r}}\)；所有列向量组成的秩称为 \(A\) 的**列秩**，记为 \(r_{\mathrm{c}}\)。

### 定理 8.1.1（矩阵的秩=行秩=列秩）
任意矩阵 \(A = (a_{ij})_{m\times n}\) 的秩 = 行秩 = 列秩。

*注：证明分为两步：1) 矩阵的秩 = 列秩；2) 行秩 = 列秩。其中行秩=列秩给出了四种证法，此处给出两种，第三种在相抵标准形后给出，第四种在内积空间中给出。*

### 定理 8.1.2（单满射与行列秩）
线性映射是单射当且仅当其矩阵表示为列满秩矩阵，线性映射是满射当且仅当其矩阵表示为行满秩矩阵。

### 定理 8.1.3（可逆等价条件）
设 \(A \in \mathbf{M}_n(\mathbf{F})\)，则下列命题等价：
1. \(A\) 可逆；
2. \(r(A)=n\)；
3. \(A\) 的 \(n\) 个行（列）向量线性无关；
4. 齐次线性方程组 \(AX=0\) 只有零解。

*注：学完行列式后可增加等价条件：\(|A| \neq 0\)。*

### 隐含定理（对角占优矩阵可逆性）
设 \(A = (a_{ij})_{n \times n}\) 满足对角占优条件 \(|a_{ii}| > \sum_{j \neq i} |a_{ij}|\)，则 \(A\) 可逆。

*注：证明使用反证法，利用可逆等价条件（4）。*


## 8.2 过渡矩阵和基变换

### 定义 8.2.1（过渡矩阵）
设 \(B_1 = \{\alpha_1,\alpha_2,\ldots,\alpha_n\}\) 与 \(B_2 = \{\beta_1,\beta_2,\ldots,\beta_n\}\) 是线性空间 \(V(\mathbf{F})\) 的任意两组基。若存在矩阵 \(A\) 使得 \(B_2 = B_1 A\)，则称矩阵 \(A\) 为 \(B_1\) 变为基 \(B_2\) 的**过渡矩阵**（或**变换矩阵**）。

*注：过渡矩阵就是将 \(B_2\) 中的向量在 \(B_1\) 下的坐标按列排列。过渡矩阵可逆，其逆矩阵就是 \(B_2\) 变为 \(B_1\) 的过渡矩阵。*

### 定理 8.2.1（过渡性质1）
设 \(S_1 = \{\alpha_1,\alpha_2,\ldots,\alpha_n\}\) 是线性无关的向量组，且  
\((\beta_1,\beta_2,\ldots,\beta_s) = (\alpha_1,\alpha_2,\ldots,\alpha_n)A\)，  
则向量组 \(S_2 = \{\beta_1,\beta_2,\ldots,\beta_s\}\) 的秩等于矩阵 \(A\) 的秩。

### 定理 8.2.2（可逆过渡矩阵保等价）
若线性空间 \(V\) 中的两个向量组 \(S_1\) 和 \(S_2\) 满足 \(S_2 = S_1 A\)，其中 \(A\) 可逆，则 \(S_1\) 与 \(S_2\) 是等价向量组。

### 定理 8.2.3（基的选择对向量坐标的影响）
设线性空间 \(V\) 的两组基为 \(B_1\) 和 \(B_2\)，且基 \(B_1\) 到 \(B_2\) 的过渡矩阵为 \(A\)。若向量 \(\xi \in V\) 在 \(B_1\) 和 \(B_2\) 下的坐标分别为 \(X\) 和 \(Y\)，则 \(Y = A^{-1} X\)。

### 定理 8.2.4（换基公式）
设 \(\sigma \in \mathcal{L}(V_1,V_2)\)，\(B_1,B_1'\) 是 \(V_1\) 的两组基，\(B_2,B_2'\) 是 \(V_2\) 的两组基。设 \(P\) 是 \(B_1\) 变为 \(B_1'\) 的过渡矩阵，\(Q\) 是 \(B_2\) 变为 \(B_2'\) 的过渡矩阵，则  
\(\mathbf{M}_{B_1',B_2'}(\sigma) = Q^{-1} \mathbf{M}_{B_1,B_2}(\sigma) P\)。

### 定理 8.2.5（基的选择对变换矩阵的影响）
设线性变换 \(\sigma \in \mathcal{L}(V,V)\)，\(B_1 = \{\alpha_1,\ldots,\alpha_n\}\) 和 \(B_2 = \{\beta_1,\ldots,\beta_n\}\) 是线性空间 \(V(\mathbf{F})\) 的两组基，基 \(B_1\) 变为基 \(B_2\) 的过渡矩阵为 \(C\)。若 \(\sigma\) 在基 \(B_1\) 下的矩阵为 \(A\)，则 \(\sigma\) 关于基 \(B_2\) 所对应的矩阵为 \(C^{-1} A C\)。

*注：该定理是换基公式的特殊情况（\(V_1=V_2\)，且 \(B_1'=B_2\)，\(B_2'=B_2\)）。*

### 隐含定理（向量组等价性判定）
若两个向量组 \(S_1\) 与 \(S_2\) 之间满足 \(S_2 = S_1 A\)，且 \(A\) 可逆，则它们等价。


## 8.3 相抵标准形

### 定理 8.3.1（相抵标准形）
设 \(A\) 是 \(m\times n\) 矩阵，则 \(r(A) = r\) 的充要条件为存在可逆矩阵 \(P\) 和 \(Q\)，使得  
\(PAQ = \begin{pmatrix} E_r & O \\ O & O \end{pmatrix} = U_r\)，  
其中 \(E_r\) 表示 \(r\) 阶单位矩阵。

### 定义 8.3.1（相抵）
设 \(A\) 和 \(B\) 是 \(m \times n\) 矩阵，如果存在可逆矩阵 \(P\) 和 \(Q\)，使得 \(PAQ = B\)，则称 \(A\) 和 \(B\) 是**相抵**的。称 \(PAQ = U_r\) 中的 \(U_r\) 为矩阵 \(A\) 的**相抵标准形**，其中 \(r = r(A)\)。

### 引理 8.3.1（矩阵行秩=列秩的第三种证明）
利用相抵标准形和转置，可以证明矩阵的行秩等于列秩。

*注：该引理为定理 8.1.1 的第三种证明。*


## 8.4 初等矩阵

### 定义 8.4.1（初等矩阵）
将单位矩阵 \(E\) 做一次初等变换得到的矩阵称为**初等矩阵**。与三种初等行、列变换对应的三类初等矩阵为：
1. **倍乘矩阵** \(E_i(c)\)：将单位矩阵第 \(i\) 行（或列）乘 \(c\)；
2. **倍加矩阵** \(E_{ij}(c)\)：将单位矩阵第 \(i\) 行乘 \(c\) 加到第 \(j\) 行，或将第 \(j\) 列乘 \(c\) 加到第 \(i\) 列；
3. **对换矩阵** \(E_{ij}\)：将单位矩阵第 \(i,j\) 行（或列）对换。

### 性质 8.4.1（初等矩阵的可逆性）
初等矩阵可逆，且  
\(E_i^{-1}(c) = E_i(1/c)\)，  
\(E_{ij}^{-1}(c) = E_{ij}(-c)\)，  
\(E_{ij}^{-1} = E_{ij}\)。

### 性质 8.4.2（初等矩阵的转置）
\(E_i^{\mathrm{T}}(c) = E_i(c)\)，  
\(E_{ij}^{\mathrm{T}}(c) = E_{ji}(c)\)，  
\(E_{ij}^{\mathrm{T}} = E_{ij}\)。

*注：初等矩阵左乘相当于行变换，右乘相当于列变换。*

### 定理 8.4.1（可逆与初等变换）
任意可逆矩阵都可以表示为若干个初等矩阵的乘积。

### 引理 8.4.2（初等变换求逆矩阵）
设 \(A\) 为 \(n\) 阶可逆矩阵，若对 \((A \mid E)\) 做一系列初等行变换将 \(A\) 化为 \(E\)，则同时 \(E\) 化为 \(A^{-1}\)。


## 8.5 初等矩阵与相抵标准形

### 引理 8.5.1（初等变换不改变秩）
初等变换（行变换或列变换）不改变矩阵的秩。

### 定理 8.5.1（相抵标准形的矩阵角度证明）
利用初等变换和引理 8.5.1，可以证明定理 8.3.1（相抵标准形）。

*注：该证明给出了通过初等变换求相抵标准形的方法。*

### 定义 8.5.1（相抵的等价定义）
两个矩阵相抵当且仅当它们可以通过一系列初等变换互相转化。

### 性质 8.5.1（相抵的等价条件）
矩阵 \(A\) 与 \(B\) 相抵  
\(\iff\) 存在可逆矩阵 \(P\) 和 \(Q\) 使得 \(PAQ = B\)  
\(\iff\) \(r(A) = r(B)\)。

*注：相抵是矩阵的一个等价关系，将矩阵按秩分类。*

### 隐含定理（初等变换与基变换的关系）
对线性映射的表示矩阵做初等行（列）变换，等价于对目标空间（出发空间）的基做相应的初等变换。


## 8.6 相抵标准形的应用

### 定理 8.6.1（相抵分解）
若 \(r(A)=r\)，则存在可逆矩阵 \(P,Q\) 使得  
\(A = P \begin{pmatrix} E_r & O \\ O & O \end{pmatrix} Q\)。  
进一步可分解为 \(A = P_1 Q_1\)，其中 \(P_1\) 列满秩，\(Q_1\) 行满秩。

### 定义 8.6.1（迹）
设 \(A = (a_{ij})_{n\times n}\) 是 \(n\) 阶方阵，\(A\) 的主对角线元素之和称为 \(A\) 的**迹**，记为 \(\operatorname{tr}(A) = \sum_{i=1}^n a_{ii}\)。

### 隐含定理（秩为1的矩阵的幂）
若 \(n\) 阶矩阵 \(A\) 的秩为 \(1\)，则对任意正整数 \(k\)，有 \(A^k = \operatorname{tr}(A)^{k-1} A\)。

### 隐含定理（左逆与右逆）
设 \(A\) 是 \(m \times n\) 矩阵。
1. 若 \(r(A)=n\)（列满秩），则存在 \(n \times m\) 矩阵 \(B\) 使得 \(BA = E_n\)（左逆）；
2. 若 \(r(A)=m\)（行满秩），则存在 \(n \times m\) 矩阵 \(C\) 使得 \(AC = E_m\)（右逆）。

*注：列满秩矩阵满足左消去律，行满秩矩阵满足右消去律。*


## 重要补充与说明

### 隐含定理（矩阵添加行列对秩的影响）
矩阵添加一列（或一行），其秩或不变，或增加 \(1\)。

### 隐含定理（分块矩阵的秩不等式）
设 \(A\) 是 \(s \times n\) 矩阵，\(B\) 是 \(A\) 前 \(m\) 行构成的 \(m \times n\) 矩阵，则  
\(r(B) \geqslant r(A) + m - s\)。

### 隐含定理（线性相关性的循环判定）
当 \(n\) 为奇数时，向量组 \(\alpha_1,\alpha_2,\ldots,\alpha_n\) 线性无关的充要条件是  
\(\alpha_1+\alpha_2,\alpha_2+\alpha_3,\ldots,\alpha_n+\alpha_1\) 线性无关。

### 算法：初等变换求逆矩阵
设 \(A\) 可逆，构造分块矩阵 \((A \mid E)\)，对其进行初等行变换，将 \(A\) 化为 \(E\)，则同时 \(E\) 化为 \(A^{-1}\)。

### 算法：求相抵标准形及过渡矩阵
对矩阵 \(A\) 进行初等行变换化为行简化阶梯形，再进行初等列变换化为相抵标准形 \(U_r\)，记录所有行变换矩阵乘积为 \(P\)，列变换矩阵乘积为 \(Q\)，则 \(PAQ = U_r\)。


**说明**：以上总结涵盖了本章所有显式定义、定理、引理，以及隐含在例题、注记中的一般性结论。部分定理在原文中无标签，此处根据内容添加了描述性标识。所有编号均按章节顺序排列，引理紧随其服务的定理之后。

以下是《矩阵运算进阶》章节中所有**定义、定理、引理**的总结，按章节顺序排列，引理紧随其服务的定理之后，部分无标签的定义、定理已根据内容补充描述，隐含在例题或注记中的一般性结论也已提炼为定理并补充在对应小节末尾。

---

# 第9章 矩阵运算进阶

### §9.1 特殊矩阵

#### 9.1.1 对角矩阵

### 定义 9.1.1（对角矩阵与准对角矩阵）  
记主对角矩阵为 $\operatorname{diag}(d_1,d_2,\ldots,d_n)$，准对角矩阵为 $\operatorname{diag}(A_1,A_2,\ldots,A_n)$。

### 定理 9.1.1（对角矩阵的乘法性质）  
设 $A$ 为 $s \times n$ 矩阵，写为列向量组 $(\alpha_1,\alpha_2,\ldots,\alpha_n)$ 或行向量组 $(\beta_1^\mathrm{T},\beta_2^\mathrm{T},\ldots,\beta_s^\mathrm{T})^\mathrm{T}$，则
- $A \cdot \operatorname{diag}(d_1,\ldots,d_n) = (d_1\alpha_1,\ldots,d_n\alpha_n)$
- $\operatorname{diag}(d_1,\ldots,d_s) \cdot A = (d_1\beta_1^\mathrm{T},\ldots,d_s\beta_s^\mathrm{T})^\mathrm{T}$

即右乘对角矩阵相当于给每列乘对应因子，左乘相当于给每行乘对应因子。

### 定理 9.1.2（对角矩阵与分块对角矩阵的性质）
1. $\operatorname{diag}(d_1,\ldots,d_n)$ 可逆 $\iff$ $d_i \neq 0$，且逆为 $\operatorname{diag}(d_1^{-1},\ldots,d_n^{-1})$。
2. $\operatorname{diag}(A_1,\ldots,A_n)$ 可逆 $\iff$ 每个 $A_i$ 可逆，且逆为 $\operatorname{diag}(A_1^{-1},\ldots,A_n^{-1})$。
3. 两个同阶对角矩阵相乘：$\operatorname{diag}(a_1,\ldots,a_n) \cdot \operatorname{diag}(b_1,\ldots,b_n) = \operatorname{diag}(a_1b_1,\ldots,a_nb_n)$；幂运算：$(\operatorname{diag}(a_1,\ldots,a_n))^k = \operatorname{diag}(a_1^k,\ldots,a_n^k)$。
4. 两个同级准对角矩阵相乘：$\operatorname{diag}(A_1,\ldots,A_n) \cdot \operatorname{diag}(B_1,\ldots,B_n) = \operatorname{diag}(A_1B_1,\ldots,A_nB_n)$。

#### 9.1.2 上（下）三角矩阵

### 定理 9.1.3（上三角矩阵的性质）  
设 $A,B$ 为上三角矩阵，主对角元分别为 $a_{ii}, b_{ii}$。
1. $A^\mathrm{T}, B^\mathrm{T}$ 为下三角矩阵。
2. $AB$ 仍为上三角矩阵，且其主对角元为 $a_{ii}b_{ii}$。
3. $A$ 可逆 $\iff$ $a_{ii} \neq 0$，且此时 $A^{-1}$ 也为上三角矩阵，其主对角元为 $a_{ii}^{-1}$。

**隐含定理 9.1.4**（幂零上三角矩阵的乘积为零）  
若 $A_1,\ldots,A_n$ 为 $n$ 个对角元全为 $0$ 的 $n$ 阶上三角矩阵，则 $A_1A_2\cdots A_n = O$。

> **证明概要**：归纳法，利用分块表示。

#### 9.1.3 自然基与基本矩阵

### 定义 9.1.2（自然基）  
$\mathbf{R}^n$ 中自然基 $e_i$ 为第 $i$ 个分量为 $1$、其余为 $0$ 的列向量。

### 定理 9.1.5（自然基的运算性质）
1. $e_i^\mathrm{T} e_j = \delta_{ij}$。
2. 设 $A$ 为 $m \times n$ 矩阵，$\mathbf{R}^n$ 的自然基为 $e_j$，$\mathbf{R}^m$ 的自然基为 $f_i$，则
   - $A e_j$ 是 $A$ 的第 $j$ 列；
   - $f_i^\mathrm{T} A$ 是 $A$ 的第 $i$ 行；
   - $f_i^\mathrm{T} A e_j$ 是 $A$ 的 $(i,j)$ 元。

### 定义 9.1.3（基本矩阵）  
$E_{ij}$ 表示第 $i$ 行第 $j$ 列为 $1$、其余为 $0$ 的矩阵。

### 定理 9.1.6（基本矩阵的运算性质）  
设 $A=(a_{ij})_{n \times n}$。
1. $A = \sum_{i,j} a_{ij} E_{ij}$。
2. $E_{ik} E_{lj} = \delta_{kl} E_{ij}$。
3. $A E_{ij}$ 的结果是将 $A$ 的第 $i$ 列移到第 $j$ 列，其余为零。
4. $E_{ij} A$ 的结果是将 $A$ 的第 $j$ 行移到第 $i$ 行，其余为零。
5. $E_{ij} A E_{kl} = a_{jk} E_{il}$。

> **注**：性质 3–5 可联系左/右乘对应的行列变换记忆。


### §9.2 矩阵可交换问题

### 定理 9.2.1（可交换矩阵的一般形式）  
设 $B$ 与 $A$ 可交换，则 $B$ 可表示为关于 $A$ 的多项式（若 $A$ 满足特定条件，如循环矩阵）。

### 定理 9.2.2（与特殊矩阵可交换的矩阵类型）
1. 与主对角元两两互异的对角矩阵可交换的方阵必为对角矩阵。
2. 与准对角矩阵 $A = \operatorname{diag}(\lambda_1 E_1, \ldots, \lambda_s E_s)$（各 $\lambda_i$ 不同）可交换的矩阵必为准对角矩阵。
3. 与所有 $n$ 阶可逆矩阵可交换的矩阵必为数量矩阵。
4. 与所有 $n$ 阶矩阵可交换的矩阵必为数量矩阵。

> **注**：证明时利用对角矩阵的乘法性质与基本矩阵构造。


### §9.3 矩阵的迹

### 定义 9.3.1（矩阵的迹）  
方阵 $A$ 的迹 $\operatorname{tr}(A) = \sum_i a_{ii}$。

### 定理 9.3.1（迹的基本性质）
1. 线性性：$\operatorname{tr}(A+B)=\operatorname{tr}(A)+\operatorname{tr}(B)$，$\operatorname{tr}(kA)=ktr(A)$。
2. 对称性：$\operatorname{tr}(A^\mathrm{T}) = \operatorname{tr}(A)$。
3. 交换性：$\operatorname{tr}(AB) = \operatorname{tr}(BA)$（即使 $A,B$ 不是方阵，只要 $AB$ 和 $BA$ 均有定义）。

### 引理 9.3.1（迹的正定性）
1. 对实矩阵 $A$，$\operatorname{tr}(A^\mathrm{T}A) \ge 0$，且等于 $0$ $\iff$ $A=O$。
2. 对复矩阵 $A$，$\operatorname{tr}(\overline{A^\mathrm{T}}A) \ge 0$，且等于 $0$ $\iff$ $A=O$。

> **注**：该引理由 $\operatorname{tr}(A^\mathrm{T}A) = \sum_{i,j} a_{ij}^2$（实）或 $\sum_{i,j} |a_{ij}|^2$（复）直接得到。

### 定理 9.3.2（迹与对称矩阵的关系）  
设 $A$ 为 $n$ 阶实矩阵，则 $\operatorname{tr}(A^2) \le \operatorname{tr}(A^\mathrm{T}A)$，等号成立 $\iff$ $A$ 为对称矩阵。

> **证明**：利用 $\operatorname{tr}((A-A^\mathrm{T})(A-A^\mathrm{T})^\mathrm{T}) \ge 0$ 展开即得。


### §9.4 矩阵的逆进阶求法

#### 9.4.1 凑因子法

### 定理 9.4.1（幂零矩阵的可逆性）  
若 $A^k = O$，则 $E \pm A$ 可逆，且 $(E+A)^{-1} = E - A + A^2 - \cdots + (-A)^{k-1}$，$(E-A)^{-1} = E + A + A^2 + \cdots + A^{k-1}$。

### 定理 9.4.2（Sherman-Morrison-Woodbury 公式）  
设 $A$ 为 $n$ 阶可逆矩阵，$X$ 为 $n \times r$，$Y$ 为 $r \times n$，$R$ 为 $r \times r$ 可逆矩阵，且 $R^{-1} + Y A^{-1} X$ 可逆，则  
\[
(A + X R Y)^{-1} = A^{-1} - A^{-1} X (R^{-1} + Y A^{-1} X)^{-1} Y A^{-1}.
\]

### 推论 9.4.1（Sherman-Morrison 公式，秩1校正）  
若 $x,y$ 为列向量，且 $1 + y^\mathrm{T} A^{-1} x \ne 0$，则  
\[
(A + x y^\mathrm{T})^{-1} = A^{-1} - \frac{A^{-1} x y^\mathrm{T} A^{-1}}{1 + y^\mathrm{T} A^{-1} x}.
\]

### 定理 9.4.3（矩阵和的可逆性传递）  
设 $A$ 为 $n \times m$，$B$ 为 $m \times n$ 矩阵，则  
\[
E_n \pm AB \text{ 可逆} \iff E_m \pm BA \text{ 可逆}.
\]
且当 $E_n - AB$ 可逆时，$(E_m - BA)^{-1} = E_m + B (E_n - AB)^{-1} A$。

#### 9.4.2 分式思想（形式级数）

### 定理 9.4.4（幂零矩阵的逆的级数表示）  
若 $A^k = O$，则  
\[
(E - A)^{-1} = E + A + A^2 + \cdots + A^{k-1}.
\]

> **注**：此方法仅为形式类比，严格证明需直接验证乘积为单位阵。

#### 9.4.3 提逆思想

### 定理 9.4.5（提逆恒等式）  
若 $E-A$、$E+A$、$A$ 均可逆，则  
\[
(E - A^{-1})^{-1} + (E - A)^{-1} = E.
\]

> **证明**：利用 $(E - A^{-1})^{-1} = (A^{-1}(A - E))^{-1} = (A - E)^{-1} A$。


### §9.5 矩阵的幂

### 定理 9.5.1（幂的计算：找规律）  
若存在可逆矩阵 $P$ 使得 $A = P D P^{-1}$，则 $A^n = P D^n P^{-1}$。特别地，若 $D$ 为对角矩阵，则 $D^n$ 易求。

### 定理 9.5.2（基础循环矩阵的幂）  
设 $A = (e_n, e_1, e_2, \ldots, e_{n-1})$（即基础循环矩阵），则对 $1 \le k \le n$，有
\[
A^k = \begin{pmatrix} O & E_{n-k} \\ E_k & O \end{pmatrix}.
\]

### 定理 9.5.3（幂零上三角矩阵的幂）  
设 $A$ 为上三角矩阵且主对角元全为 $0$，则 $A^n = O$。特别地，对于若当块
\[
J = \begin{pmatrix} 0 & 1 & & \\ & \ddots & \ddots & \\ & & 0 & 1 \\ & & & 0 \end{pmatrix},
\]
有 $J^k$ 为将 $1$ 向右上角平移 $k$ 位的矩阵，且 $J^n = O$。

### 定理 9.5.4（秩1矩阵的幂）  
若 $M$ 为秩 $1$ 矩阵，且 $\operatorname{tr}(M) = b$，则 $M^k = b^{k-1} M$。

### 定理 9.5.5（秩1矩阵的多项式幂）  
设 $M$ 为秩 $1$ 矩阵，$\operatorname{tr}(M)=b$，则对任意 $a$ 和正整数 $n$，
\[
(aE + M)^n = 
\begin{cases}
a^n E + n a^{n-1} M, & b = 0, \\[6pt]
a^n E + \dfrac{(a+b)^n - a^n}{b} M, & b \ne 0.
\end{cases}
\]

**隐含定理 9.5.6**（二阶幂零矩阵的幂）  
若 $A$ 为 $2$ 阶方阵且存在正整数 $l$ 使 $A^l = O$，则 $A^2 = O$。

> **证明**：利用秩 $r(A) \le 1$ 及迹的性质。


### §9.6 分块矩阵初等变换（打洞法）

#### 9.6.1 基本概念

### 定义 9.6.1（分块初等矩阵）  
对分块单位矩阵 $\begin{pmatrix} E & O \\ O & E \end{pmatrix}$ 进行以下三种分块初等变换得到的矩阵：
1. 交换两分块行（列）：$\begin{pmatrix} O & E \\ E & O \end{pmatrix}$。
2. 对某一分块行（列）左（右）乘可逆矩阵 $C$：$\begin{pmatrix} C & O \\ O & E \end{pmatrix}$ 或 $\begin{pmatrix} E & O \\ O & C \end{pmatrix}$。
3. 将某一分块行（列）左（右）乘矩阵 $B$ 加到另一行（列）：$\begin{pmatrix} E & O \\ B & E \end{pmatrix}$ 或 $\begin{pmatrix} E & B \\ O & E \end{pmatrix}$。

> **注**：分块初等矩阵均可逆，且左（右）乘分块矩阵相当于对其实施相应的分块行（列）变换。分块初等变换不改变矩阵的秩。

#### 9.6.2 分块矩阵求逆与打洞法

### 定理 9.6.1（分块矩阵的逆：打洞法公式）  
设 $P = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$，其中 $A$ 为 $m$ 阶，$D$ 为 $n$ 阶。
1. 若 $A$ 可逆且 $D - C A^{-1} B$（称为 $A$ 的 Schur 补）可逆，则
   \[
   P^{-1} = \begin{pmatrix}
   A^{-1} + A^{-1} B (D - C A^{-1} B)^{-1} C A^{-1} & -A^{-1} B (D - C A^{-1} B)^{-1} \\
   -(D - C A^{-1} B)^{-1} C A^{-1} & (D - C A^{-1} B)^{-1}
   \end{pmatrix}.
   \]
2. 若 $D$ 可逆且 $A - B D^{-1} C$（称为 $D$ 的 Schur 补）可逆，则
   \[
   P^{-1} = \begin{pmatrix}
   (A - B D^{-1} C)^{-1} & -(A - B D^{-1} C)^{-1} B D^{-1} \\
   -D^{-1} C (A - B D^{-1} C)^{-1} & D^{-1} + D^{-1} C (A - B D^{-1} C)^{-1} B D^{-1}
   \end{pmatrix}.
   \]

### 引理 9.6.1（Schur 补恒等式）  
由上述两种逆矩阵表达式的左上角分块相等可得
\[
(A - B D^{-1} C)^{-1} = A^{-1} + A^{-1} B (D - C A^{-1} B)^{-1} C A^{-1}.
\]
此即 Sherman-Morrison-Woodbury 公式。

### 定理 9.6.2（分块打洞法与可逆性等价）  
设 $A$ 为 $n$ 阶可逆矩阵，$B,C$ 分别为 $n \times m$ 和 $m \times n$ 矩阵，则
\[
E_m + C A^{-1} B \text{ 可逆} \iff A + B C \text{ 可逆}.
\]

#### 9.6.3 LU 分解

### 定理 9.6.3（LU 分解的存在性）  
若 $n$ 阶矩阵 $A$ 的各阶顺序主子矩阵均可逆，则存在主对角元全为 $1$ 的下三角矩阵 $L$ 和上三角矩阵 $U$，使得 $A = LU$。

> **注**：证明使用数学归纳法，利用分块打洞法构造 $L$ 和 $U$。

### 算法 9.6.1（LU 分解的求解）  
对 $A$ 仅进行“上方行乘以数加到下方行”的初等行变换（不交换行，不对角缩放），将其化为上三角矩阵 $U$，则这些初等变换对应的初等矩阵的逆的乘积即为 $L$。

### 定理 9.6.4（LU 分解解方程组）  
若 $A = LU$，则方程组 $Ax = b$ 可分解为求解 $Lc = b$（向前代入）和 $Ux = c$（向后回代）两个三角方程组。


### §9.7 矩阵方程

### 定理 9.7.1（基本矩阵方程的求解公式）
1. $AX = B$ 且 $A$ 可逆 $\implies$ $X = A^{-1}B$。
2. $XA = B$ 且 $A$ 可逆 $\implies$ $X = B A^{-1}$。
3. $AXB = C$ 且 $A,B$ 可逆 $\implies$ $X = A^{-1} C B^{-1}$。

### 算法 9.7.1（初等变换求解矩阵方程）
1. 求 $A^{-1}B$：对 $(A \mid B)$ 只做初等行变换化为 $(E \mid A^{-1}B)$。
2. 求 $BA^{-1}$：对 $\begin{pmatrix} A \\ \hdashline B \end{pmatrix}$ 只做初等列变换化为 $\begin{pmatrix} E \\ \hdashline BA^{-1} \end{pmatrix}$。

### 定理 9.7.2（矩阵方程的化简）  
若矩阵方程可化为 $(A-B)X(A-B) = A(A-B)$ 且 $A-B$ 可逆，则 $X = (A-B)^{-1} A$。


### §9.8 秩等式与不等式

### 定理 9.8.1（可逆乘法不改变秩）  
若 $P,Q$ 可逆，则 $r(A) = r(PA) = r(AQ) = r(PAQ)$。

### 定理 9.8.2（分块矩阵的秩）
1. $r\begin{pmatrix} A & O \\ O & B \end{pmatrix} = r(A) + r(B)$。
2. $r\begin{pmatrix} A & D \\ O & B \end{pmatrix} \ge r(A) + r(B)$，且 $\le r(A) + r(B) + r(D)$。  
   $r\begin{pmatrix} A & O \\ C & B \end{pmatrix} \ge r(A) + r(B)$，且 $\le r(A) + r(B) + r(C)$。

### 定理 9.8.3（秩的三角不等式）  
$|r(A) - r(B)| \le r(A \pm B) \le r(A) + r(B)$。

### 定理 9.8.4（乘积的秩不等式）  
$r(AB) \le \min\{r(A), r(B)\}$。

### 定理 9.8.5（Sylvester 不等式）  
设 $A \in \mathbf{F}^{s \times n}, B \in \mathbf{F}^{n \times m}$，则
\[
r(AB) \ge r(A) + r(B) - n.
\]
特别地，若 $AB = O$，则 $r(A) + r(B) \le n$。

### 定理 9.8.6（Frobenius 不等式）  
$r(ABC) \ge r(AB) + r(BC) - r(B)$。

### 推论 9.8.1  
$r(A^3) \ge 2r(A^2) - r(A)$。

### 定理 9.8.7（秩的递推稳定性）  
若存在正整数 $m$ 使得 $r(A^m) = r(A^{m+1})$，则对任意 $k \ge m$，有 $r(A^k) = r(A^{m})$。特别地，对 $n$ 阶矩阵 $A$，必有 $r(A^n) = r(A^{n+1}) = \cdots$。

**隐含定理 9.8.8**（列向量组的秩关系）
1. $r(A, AB) = r(A)$。
2. $r(A,B) \ge \max\{r(A), r(B)\}$。
3. $r(A^\mathrm{T}A) = r(A) = r(AA^\mathrm{T})$（实矩阵）。


**总结检查**：以上已按章节顺序提炼所有定义、定理、引理，引理紧随对应定理，对原文无标签但重要的结论补充了定理编号与描述，并在各节末尾补充了隐含定理或重要注解。所有命名符合原文风格（如“定理 9.1.1”），注意事项以“注”标出。内容涵盖矩阵运算进阶的核心结论，包括特殊矩阵、可交换性、迹、逆矩阵、幂、分块矩阵、矩阵方程、秩等式与不等式等主题，力求完整。

以下是《10 行列式.tex》章节中所有**定义、定理、引理**的整理，按章节顺序排列，引理紧随其服务的定理之后。部分在原文中无标签的定理/定义已根据内容添加了简短描述作为标识。

---

# 第10章 行列式

### 10.2 行列式的公理化定义

#### 定义 1 (行列式的公理化定义)
数域$\mathbf{F}$上的一个$n$阶**行列式**是取值于$\mathbf{F}$的$n$个$n$维向量$\alpha_1,\alpha_2,\ldots,\alpha_n \in \mathbf{F}^n$的一个函数$D$，满足：
1. **齐性**：$D(\alpha_1,\ldots,\lambda\alpha_i,\ldots,\alpha_n)=\lambda D(\alpha_1,\ldots,\alpha_i,\ldots,\alpha_n)$。
2. **加性**：$D(\alpha_1,\ldots,\alpha_i+\beta_i,\ldots,\alpha_n)=D(\alpha_1,\ldots,\alpha_i,\ldots,\alpha_n)+D(\alpha_1,\ldots,\beta_i,\ldots,\alpha_n)$。
3. **反对称性**：$D(\alpha_1,\ldots,\alpha_i,\ldots,\alpha_j,\ldots,\alpha_n)=-D(\alpha_1,\ldots,\alpha_j,\ldots,\alpha_i,\ldots,\alpha_n)$。
4. **规范性**：$D(e_1,e_2,\ldots,e_n)=1$。

其中$e_i$是第$i$个标准单位向量。记$A = (\alpha_1,\ldots,\alpha_n)$时，$D(\alpha_1,\ldots,\alpha_n)$也记为$|A|$或$\det A$。

### 注： 此定义将行列式刻画为一个满足多重线性、反对称且规范的多线性函数，其几何背景是$n$维平行多面体的有向体积。

#### (由公理化定义导出的行列式简单性质)
设$D$满足定义1，则：
1. 若有一列为零向量，则$D=0$。
2. 若有两列相同，则$D=0$。
3. 若有两列成比例，则$D=0$。
4. 倍加列变换不改变$D$的值。
5. 若列向量线性相关，则$D=0$。

### 10.3 行列式的逆序数定义

#### 定义 2 (逆序数)
设$(k_1,k_2,\ldots,k_n)$是$(1,2,\ldots,n)$的一个排列。如果$i < j$且$k_i > k_j$，则称$(k_i, k_j)$是一个**逆序对**。排列中所有逆序对的总数称为该排列的**逆序数**，记作$\tau(k_1,k_2,\ldots,k_n)$。

#### 定义 3 (奇排列与偶排列)
逆序数为偶数的排列称为**偶排列**，逆序数为奇数的排列称为**奇排列**。

#### (奇偶排列的性质)
1. 对换排列中任意两个元素，排列的奇偶性改变。
2. 当$n \geqslant 2$时，$n$阶排列中奇排列与偶排列的个数相等。

#### 引理 1 (逆序数与幂次的关系)
设$(k_1,k_2,\ldots,k_n)$是一个排列，则通过$\tau(k_1,k_2,\ldots,k_n)$次相邻对换可将其变为标准排列$(1,2,\ldots,n)$。因此，在行列式展开中，对应于该排列的项符号为$(-1)^{\tau(k_1,k_2,\ldots,k_n)}$。

#### 定理 2 (行列式的逆序数定义)
设$A=(a_{ij})_{n \times n}$，则
\[
\det A = |A| = \sum_{(k_1,k_2,\ldots,k_n) \in S_n} (-1)^{\tau(k_1,k_2,\ldots,k_n)} a_{k_1 1} a_{k_2 2} \cdots a_{k_n n},
\]
其中$S_n$表示所有$n$阶排列的集合。

### 注： 此定义给出了行列式的显式计算公式，共有$n!$项。

### 10.4 行列式的递归式定义

#### 定义 4 (余子式与代数余子式)
在$n$阶行列式$D=|a_{ij}|$中，去掉元素$a_{ij}$所在的第$i$行和第$j$列后，剩余的$n-1$阶行列式称为$a_{ij}$的**余子式**，记作$M_{ij}$。称$A_{ij}=(-1)^{i+j}M_{ij}$为$a_{ij}$的**代数余子式**。

#### 定义 5 (行列式的递归式定义)
设$D=|a_{ij}|_{n \times n}$，则
\[
D = \sum_{k=1}^{n} a_{kj} A_{kj} \quad (\text{对第 } j \text{ 列展开}), \qquad j=1,2,\ldots,n.
\]
\[
D = \sum_{k=1}^{n} a_{ik} A_{ik} \quad (\text{对第 } i \text{ 行展开}), \qquad i=1,2,\ldots,n.
\]

#### 定理 3 (代数余子式的正交性)
$n$阶行列式$D=|a_{ij}|$的某一行（列）元素与另一行（列）相应元素的代数余子式的乘积之和等于$0$，即
\[
\sum_{k=1}^{n} a_{kj} A_{ki} = 0 \quad (j \neq i), \qquad \sum_{k=1}^{n} a_{jk} A_{ik} = 0 \quad (j \neq i).
\]

### 10.5 行列式的性质及应用

#### (行列式的基本性质)
设$A, B \in \mathbf{F}^{n \times n}$，$k \in \mathbf{F}$。
1. $|kA| = k^n |A|$。
2. 初等矩阵的行列式：
   * 对换矩阵：$|E_{ij}| = -1$。
   * 倍乘矩阵：$|E_i(c)| = c$。
   * 倍加矩阵：$|E_{ij}(k)| = 1$。
3. **行列式乘积定理**：$|AB| = |A|\,|B|$，进而$|A^k| = |A|^k$。
4. **可逆性判据**：$A$可逆 $\iff$ $|A| \neq 0$。
5. **转置不变性**：$|A^\mathrm{T}| = |A|$。
6. **三角矩阵的行列式**：上（下）三角矩阵的行列式等于其主对角线元素的乘积。
7. 若$A$可逆，则$|A^{-1}| = |A|^{-1}$。

#### (分块矩阵行列式公式)
1. $\begin{vmatrix} A & O \\ O & B \end{vmatrix} = \begin{vmatrix} A & O \\ C & B \end{vmatrix} = \begin{vmatrix} A & D \\ O & B \end{vmatrix} = |A|\,|B|$。
   $\begin{vmatrix} O & A \\ B & C \end{vmatrix} = (-1)^{kr} |A|\,|B|$，其中$A$为$k$阶方阵，$B$为$r$阶方阵。
2. **打洞公式（舒尔补）**：
   * 若$A$可逆，$\begin{vmatrix} A & B \\ C & D \end{vmatrix} = |A|\,|D - CA^{-1}B|$。
   * 若$D$可逆，$\begin{vmatrix} A & B \\ C & D \end{vmatrix} = |D|\,|A - BD^{-1}C|$。
3. **降阶公式**：若$A$与$D$均可逆，则$|A|\,|D - CA^{-1}B| = |D|\,|A - BD^{-1}C|$。
4. 设$A$为$n \times m$矩阵，$B$为$m \times n$矩阵，则
   \[ |E_n \pm AB| = |E_m \pm BA|, \qquad |\lambda E_n \pm AB| = \lambda^{n-m} |\lambda E_m \pm BA| \quad (n \geqslant m). \]

#### (行列式函数的导数)
设$F(t) = |f_{ij}(t)|_{n \times n}$，其中$f_{ij}(t)$可微，则
\[
\frac{\mathrm{d}}{\mathrm{d}t} F(t) = \sum_{j=1}^{n} F_j(t),
\]
其中$F_j(t)$是将$F(t)$的第$j$列替换为其导数而得的行列式。

### 10.6 伴随矩阵

#### 定义 6 (伴随矩阵)
设$A=(a_{ij})_{n \times n}$，$A_{ij}$为$a_{ij}$的代数余子式，称矩阵
\[
A^* = \begin{pmatrix}
A_{11} & A_{21} & \cdots & A_{n1} \\
A_{12} & A_{22} & \cdots & A_{n2} \\
\vdots & \vdots & \ddots & \vdots \\
A_{1n} & A_{2n} & \cdots & A_{nn}
\end{pmatrix}
\]
为$A$的**伴随矩阵**。

#### 定理 4 (伴随矩阵的基本性质)
设$A$为$n$阶方阵，则
1. $AA^* = A^*A = |A|E$。
   若$A$可逆，则$A^{-1} = \dfrac{A^*}{|A|}$，$A^* = |A| A^{-1}$，$(A^*)^{-1} = \dfrac{A}{|A|}$。
2. $|A^*| = |A|^{n-1}$。
3. 若$A, B$可逆，则$(AB)^* = B^* A^*$，$(A^\mathrm{T})^* = (A^*)^\mathrm{T}$，$(kA)^* = k^{n-1}A^*$。
4. 若$A$可逆，则$(A^*)^* = |A|^{n-2} A$，$|(A^*)^*| = |A|^{(n-1)^2}$。
5. 对正整数$k$，$(A^k)^* = (A^*)^k$。
6. **伴随矩阵的秩**：
   \[
   r(A^*) = \begin{cases}
   n, & r(A) = n, \\
   1, & r(A) = n-1, \\
   0, & r(A) < n-1.
   \end{cases}
   \]

### 10.7 行列式秩

#### 定义 7 (子式、主子式、顺序主子式)
矩阵$A=(a_{ij})_{m \times n}$的任意$k$行与任意$k$列交叉处的$k^2$个元素按原序组成的行列式，称为$A$的一个**$k$阶子式**。
若$A$为方阵，且选取的行列标号相同$(i_t=j_t)$，则称为**$k$阶主子式**。特别地，若$i_t=j_t=t\ (t=1,\ldots,k)$，则称为**$k$阶顺序主子式**。

#### 定义 8 (行列式秩)
矩阵$A$的非零子式的最高阶数称为$A$的**行列式秩**。

#### 定理 5 (矩阵的秩等于行列式秩)
矩阵$A$的秩$r(A)$等于其行列式秩。

### 10.8 行列式计算技巧

#### (特殊行列式公式)
1. **三角形行列式**：上（下）三角矩阵的行列式等于主对角线元素之积。
2. **箭形行列式**：
   \[
   \begin{vmatrix}
   a_1 & b_2 & b_3 & \cdots & b_n \\
   c_2 & a_2 & 0 & \cdots & 0 \\
   c_3 & 0 & a_3 & \cdots & 0 \\
   \vdots & \vdots & \vdots & \ddots & \vdots \\
   c_n & 0 & 0 & \cdots & a_n
   \end{vmatrix} = \left( a_1 - \sum_{i=2}^n \frac{b_i c_i}{a_i} \right) a_2 a_3 \cdots a_n, \quad (a_i \neq 0).
   \]
3. **范德蒙德(Vandermonde)行列式**：
   \[
   V_n = \begin{vmatrix}
   1 & 1 & \cdots & 1 \\
   x_1 & x_2 & \cdots & x_n \\
   x_1^2 & x_2^2 & \cdots & x_n^2 \\
   \vdots & \vdots & \ddots & \vdots \\
   x_1^{n-1} & x_2^{n-1} & \cdots & x_n^{n-1}
   \end{vmatrix} = \prod_{1 \leqslant i < j \leqslant n} (x_j - x_i).
   \]
   **推论**：范德蒙德矩阵可逆 $\iff$ $x_i$两两不同。
4. **三对角行列式（递推型）**：形如
   \[
   D_n = \begin{vmatrix}
   \cos\beta & 1 \\
   1 & 2\cos\beta & \ddots \\
   & \ddots & \ddots & 1 \\
   & & 1 & 2\cos\beta
   \end{vmatrix}
   \]
   满足$D_n = 2\cos\beta D_{n-1} - D_{n-2}$，且$D_n = \cos n\beta$。

#### 定理 6 (拉普拉斯(Laplace)展开定理)
在$n$阶行列式$|A|$中，取定$k$行（$1 \leqslant k < n$），则这$k$行元素形成的所有$k$阶子式与其对应的代数余子式的乘积之和等于$|A|$。对列有类似结论。

### 注： 此定理是按行（列）展开的推广，可按多行多列展开。

### 10.9 Cauchy-Binet公式

#### 定理 7 (Cauchy-Binet公式)
设$A$为$m \times n$矩阵，$B$为$n \times m$矩阵。
1. 若$m > n$，则$|AB| = 0$。
2. 若$m \leqslant n$，则
   \[
   |AB| = \sum_{1 \leqslant j_1 < j_2 < \cdots < j_m \leqslant n} A\begin{pmatrix} 1 & 2 & \cdots & m \\ j_1 & j_2 & \cdots & j_m \end{pmatrix} B\begin{pmatrix} j_1 & j_2 & \cdots & j_m \\ 1 & 2 & \cdots & m \end{pmatrix},
   \]
   其中$A\begin{pmatrix} i_1 & \cdots & i_s \\ j_1 & \cdots & j_s \end{pmatrix}$表示由$A$的第$i_1,\ldots,i_s$行与第$j_1,\ldots,j_s$列交叉元素构成的$s$阶子式。

#### 定理 8 (Cauchy-Binet公式的推广)
设$A$为$m \times n$矩阵，$B$为$n \times m$矩阵，$r \leqslant m$。
1. 若$r > n$，则$AB$的任意$r$阶子式为$0$。
2. 若$r \leqslant n$，则$AB$的$r$阶子式为
   \[
   (AB)\begin{pmatrix} i_1 & \cdots & i_r \\ j_1 & \cdots & j_r \end{pmatrix} = \sum_{1 \leqslant k_1 < \cdots < k_r \leqslant n} A\begin{pmatrix} i_1 & \cdots & i_r \\ k_1 & \cdots & k_r \end{pmatrix} B\begin{pmatrix} k_1 & \cdots & k_r \\ j_1 & \cdots & j_r \end{pmatrix}.
   \]

#### 推论 1
设$A$为$m \times n$实矩阵，则$AA^\mathrm{T}$的任一主子式非负。

#### (拉格朗日(Lagrange)恒等式)
\[
\left( \sum_{i=1}^n a_i^2 \right) \left( \sum_{i=1}^n b_i^2 \right) - \left( \sum_{i=1}^n a_i b_i \right)^2 = \sum_{1 \leqslant i < j \leqslant n} (a_i b_j - a_j b_i)^2.
\]
### 注： 可由Cauchy-Binet公式取$A = \begin{pmatrix} a_1 & \cdots & a_n \\ b_1 & \cdots & b_n \end{pmatrix}$证明。


**整理说明**：
1. 定义、定理、引理均按其在章节中出现的顺序排列。
2. 引理紧随其服务的定理之后（如引理1用于说明定理2的符号确定）。
3. 部分在原文中以“例”或“性质”形式出现，但实质为一般性结论的，已提炼为定理或公式（如行列式基本性质、打洞公式、特殊行列式公式等）。
4. 部分定理（如行列式秩与矩阵秩的等价性）在原文中未明确编号，此处根据内容添加了简短标题。
5. 对于有重要注意事项的定理，以“注：”形式进行了补充说明。

根据《朝花夕拾》章节内容，以下是按章节顺序整理的定义、定理、引理等数学结论，包括补充说明、隐含定理、性质、算法和证明框架。引理紧随其服务的定理之后，未标记的结论已补充描述性标签，注意事项以“注：”开头。

---

# 第11章 朝花夕拾

#### 11.1 线性方程组解的一般理论

### 定理 11.1.1（线性方程组有解的充要条件）  
线性方程组有解的充分必要条件是其系数矩阵与增广矩阵有相同的秩。  
注：该定理等价于向量 \(\vec{b}\) 可由系数矩阵的列向量组线性表示。

### 定理 11.1.2（方程组解的情况）  
当方程组有解时：
1. 若系数矩阵 \(A\) 的秩等于未知量数目 \(n\)，则方程组有唯一解；
2. 若 \(A\) 的秩小于 \(n\)，则方程组有无穷多解。

### 定理 11.1.3（Cramer法则）  
对于 \(n\) 元线性方程组 \(AX = b\)（其中 \(A\) 为 \(n\) 阶方阵），令 \(D = |A|\)，\(D_i\) 为将 \(A\) 的第 \(i\) 列替换为 \(b\) 所得行列式，则：
1. 若 \(D \neq 0\)，方程组有唯一解 \(x_i = D_i / D\)；
2. 若 \(D = 0\)，则方程组无解或有无穷多解。
注：对于齐次方程组 \(AX = 0\)，有非零解当且仅当 \(D = 0\)。

### 引理 11.1.1（方阵可逆性与解的唯一性）  
设 \(A\) 为 \(n\) 阶方阵，则 \(AX = b\) 有唯一解当且仅当 \(A\) 可逆（即 \(|A| \neq 0\)）。  
注：此引理用于证明 Cramer 法则中唯一解的情况。

**隐含定理 11.1.1（线性方程组的矩阵表示）**  
任何线性方程组 \(AX = b\) 可写为 \(x_1\beta_1 + \cdots + x_n\beta_n = b\)，其中 \(\beta_i\) 为 \(A\) 的第 \(i\) 列。方程组有解当且仅当 \(b\) 可由 \(\beta_1, \dots, \beta_n\) 线性表示。


#### 11.2 齐次线性方程组解的一般理论

### 定义 11.2.1（解空间）  
齐次线性方程组 \(AX = 0\) 的解集合构成一个线性空间，称为解空间，记作 \(N(A)\)。

### 定理 11.2.1（解空间的维数）  
设 \(A \in \mathbf{M}_{m \times n}(\mathbf{F})\)，\(r(A) = r\)，则解空间 \(N(A)\) 的维数为 \(n - r\)，且其一组基即为方程组的基础解系。  
注：该定理等价于维数公式 \(r(A) + \dim N(A) = n\)。

**隐含定理 11.2.1（基础解系的构造）**  
对系数矩阵进行初等行变换化为行简化阶梯形后，令自由未知量依次取单位向量，可得基础解系。

### 定理 11.2.2（解空间的包含关系）  
若齐次方程组 \(AX = 0\) 的解都是 \(BX = 0\) 的解，则 \(r(B) \leq r(A)\)。  
注：证明利用了解空间维数与秩的关系。


#### 11.3 非齐次线性方程组解的一般理论

### 定义 11.3.1（导出组）  
对于非齐次线性方程组 \(AX = b\)，其对应的齐次方程组 \(AX = 0\) 称为导出组。

### 定理 11.3.1（非齐次方程组的解结构）  
若非齐次方程组 \(AX = b\) 有解，则其解集可表示为 \(U = \{\gamma_0 + \eta \mid \eta \in W\}\)，其中 \(\gamma_0\) 是一个特解，\(W\) 是导出组的解空间。

### 性质 11.3.1（非齐次解的性质）  
1. 非齐次方程组的两个解的差是导出组的解；
2. 非齐次方程组的一个解与导出组的一个解之和仍是非齐次方程组的解。

### 定理 11.3.2（非齐次解的线性无关性）  
设 \(X_0\) 是 \(AX = b\) 的一个特解，\(X_1, \dots, X_p\) 是导出组的基础解系，则：
1. \(X_0, X_1, \dots, X_p\) 线性无关；
2. \(X_0, X_0 + X_1, \dots, X_0 + X_p\) 线性无关；
3. \(AX = b\) 的任一解可表示为 \(X = k_0X_0 + k_1(X_0 + X_1) + \cdots + k_p(X_0 + X_p)\)，其中 \(k_0 + k_1 + \cdots + k_p = 1\)。

### 定理 11.3.3（非齐次线性无关解的个数）  
设 \(A\) 为 \(s \times n\) 矩阵，\(r(A) = r\)，则非齐次方程组 \(AX = b\) 至多存在 \(n - r + 1\) 个线性无关的解向量。


#### 11.4 线性方程组解的几何解释

### 引理 11.4.1（仿射子集的交）  
仿射子集的交（如果非空）仍是仿射子集。  
注：用于解释线性方程组的解作为超平面的交。

### 定理 11.4.1（线性方程组的几何解释）  
线性方程组 \(AX = b\) 的解集是有限个超平面（仿射子集）的交，可表示为特解加上齐次解空间的形式。

**隐含定理 11.4.1（对偶空间解释）**  
方程组 \(AX = b\) 可视为求向量 \(x\) 使得 \(m\) 个线性泛函 \(\varphi_i(x) = a_{i1}x_1 + \cdots + a_{in}x_n\) 分别取值 \(b_i\)，解集为 \(\bigcap_{i=1}^m \varphi_i^{-1}(b_i)\)。


#### 11.5 理论应用

### 定理 11.5.1（秩不等式）  
设 \(A, B\) 分别为 \(m \times n\) 和 \(n \times s\) 矩阵，则：
1. \(r(AB) \leq \min\{r(A), r(B)\}\)；
2. 若 \(AB = O\)，则 \(r(A) + r(B) \leq n\)。

### 定理 11.5.2（矩阵乘积的秩）  
对于实矩阵 \(A\)，有 \(r(A^\mathrm{T}A) = r(AA^\mathrm{T}) = r(A)\)。

### 定理 11.5.3（幂等矩阵的秩）  
设 \(A\) 为 \(n\) 阶矩阵，则 \(A^2 = A\) 当且仅当 \(r(A) + r(E - A) = n\)。

### 定理 11.5.4（伴随矩阵的秩）  
设 \(A^*\) 为 \(n\) 阶方阵 \(A\) 的伴随矩阵，则：
\[
r(A^*) = 
\begin{cases}
n, & r(A) = n, \\
1, & r(A) = n-1, \\
0, & r(A) < n-1.
\end{cases}
\]

**隐含定理 11.5.1（维数公式技巧）**  
设 \(A, B\) 分别为 \(l \times k\) 和 \(k \times n\) 矩阵，则满足 \(ABX = 0\) 的 \(BX\) 构成线性空间 \(V\)，且 \(\dim V = r(B) - r(AB)\)。


#### 11.6 线性方程组拓展题型

### 定理 11.6.1（含参方程组解的情况）  
含参线性方程组解的情况可通过系数矩阵与增广矩阵的秩判断，或利用 Cramer 法则（当方程个数等于未知量个数时）。

### 定理 11.6.2（齐次方程组同解条件）  
两个齐次线性方程组 \(AX = 0\) 与 \(BX = 0\) 同解的充要条件是 \(r\begin{pmatrix} A \\ B \end{pmatrix} = r(A) = r(B)\)。

### 定理 11.6.3（非齐次方程组同解条件）  
两个非齐次线性方程组 \(AX = b\) 与 \(BX = d\) 同解的充要条件是：
1. 两者均无解；或
2. 两者均有解且 \(r\begin{pmatrix} A & b \\ B & d \end{pmatrix} = r\begin{pmatrix} A \\ B \end{pmatrix} = r(A) = r(A, b) = r(B) = r(B, d)\)。

### 定理 11.6.4（齐次方程组公共解）  
齐次方程组 \(AX = 0\) 与 \(BX = 0\) 有非零公共解的充要条件是：
1. \(r\begin{pmatrix} A \\ B \end{pmatrix} < n\)；或
2. 设 \(\eta_1, \dots, \eta_s\) 是 \(BX = 0\) 的基础解系，则 \(A\eta_1, \dots, A\eta_s\) 线性相关；或
3. 设两方程组的基础解系分别为 \(\gamma_1, \dots, \gamma_t\) 和 \(\eta_1, \dots, \eta_s\)，则 \(\gamma_1, \dots, \gamma_t, \eta_1, \dots, \eta_s\) 线性相关。

### 定理 11.6.5（非齐次方程组公共解）  
设非齐次方程组 \(AX = b\) 与 \(BX = d\) 均有解，则它们有公共解的充要条件是：
1. \(r\begin{pmatrix} A \\ B \end{pmatrix} = r\begin{pmatrix} A & b \\ B & d \end{pmatrix}\)；或
2. 设 \(\eta_1, \dots, \eta_{n-s+1}\) 是 \(BX = d\) 的 \(n-s+1\) 个线性无关解，则 \(b\) 是 \(A\eta_1, \dots, A\eta_{n-s+1}\) 的凸组合（系数和为1）；或
3. 设两方程组的线性无关解分别为 \(\gamma_1, \dots, \gamma_{n-t+1}\) 和 \(\eta_1, \dots, \eta_{n-s+1}\)，则存在系数和为1的表示使两者线性相关。

**隐含定理 11.6.1（线性方程组反问题）**  
1. 给定线性无关向量组 \(\alpha_1, \dots, \alpha_s\)，求以它们为基础解系的齐次方程组：解 \(B^\mathrm{T}X = 0\)（其中 \(B = (\alpha_1, \dots, \alpha_s)\)），取基础解系作为系数矩阵的行。
2. 给定向量组 \(\alpha_1, \dots, \alpha_s\)（线性无关），求以它们为解集极大无关组的非齐次方程组：先求齐次方程组基础解系（\(\alpha_2 - \alpha_1, \dots, \alpha_s - \alpha_1\)），再取特解 \(\alpha_1\)。

### 注： 以上题型定理的证明多利用秩的条件和线性表示关系，需注意区分齐次与非齐次情况。


#### 补充结论（隐含在例题与练习中）

### 性质 11.7.1（多项式插值唯一性）  
给定 \(n\) 个互不相同的点 \((a_i, b_i)\)，存在唯一的 \(n-1\) 次多项式 \(f(x)\) 满足 \(f(a_i) = b_i\)。  
注：证明利用 Vandermonde 行列式非零，对应线性方程组有唯一解。

### 定理 11.7.1（行满秩与解的存在性）  
设 \(A\) 为 \(m \times n\) 矩阵，则线性方程组 \(AX = b\) 对任意 \(b\) 都有解的充要条件是 \(A\) 行满秩（即 \(r(A) = m\)）。

### 定理 11.7.2（矩阵方程的解）  
设 \(A\) 为 \(m \times n\) 矩阵，则矩阵方程 \(AX = O\) 的解空间维数为 \(n \cdot (n - r(A))\)（作为矩阵空间）。

### 定理 11.7.3（对角占优矩阵的行列式）  
设 \(A = (a_{ij})_{n \times n}\) 为复矩阵，若 \(|a_{ii}| > \sum_{j \neq i} |a_{ij}|\) 对所有 \(i\) 成立，则 \(|A| \neq 0\)。若 \(A\) 为实矩阵且 \(a_{ii} > \sum_{j \neq i} |a_{ij}|\)，则 \(|A| > 0\)。

### 注： 这些补充结论在例题和习题中作为工具或结论出现，具有一般性。


整理完毕。所有定义、定理、引理已按章节顺序排列，引理紧随对应定理，补充了隐含结论和注意事项。

以下是对《史海拾遗》章节中所有定义、定理、引理的总结，按章节顺序排列，引理紧随其服务的定理之后。对于原文中没有标签的定义、定理、引理，已根据内容补充了简短描述作为标识。同时，补充了隐含在例题或注释中的一般性定理，并添加了必要的注意事项。

---

# 第12章 史海拾遗

### 1.1 起点：初等代数

#### 定义1.1 丢番图方程（不定方程）
形如  
\[ a_1x_1^{b_1} + a_2x_2^{b_2} + \cdots + a_nx_n^{b_n} = c, \quad a_i, b_i, c \in \mathbf{Z} \ (i=1,2,\ldots,n) \]  
的方程称为丢番图方程（或不定方程）。  

### 注： 丢番图方程要求未知数取整数值，是整数系数多项式等式。

#### 定理1.1 费马大定理
丢番图方程 \(x^n + y^n - z^n = 0\) 在 \(n > 2\) 时无正整数解。

### 注： 该定理由安德鲁·怀尔斯于1995年证明，使用了代数数论、代数几何等现代数学工具。


### 1.2 演化：线性代数的产生与发展

#### 定义1.2 行列式（莱布尼茨记号）
莱布尼茨使用双标码记法表示线性方程组的系数，例如 \(10, 11, 12\) 等，相当于现代的下标记号 \(a_{ij}\)。他通过消元法得到类似于现代行列式的表达式。

### 注： 莱布尼茨在1693年的信件中给出了三阶行列式的雏形，并提出了符号规则。

#### 定理1.2 Cramer法则（克莱姆，1750）
对于含 \(n\) 个未知量的 \(n\) 个线性方程组，若系数行列式不为零，则方程组有唯一解，解由行列式的比值给出。

### 注： 克莱姆在《线性代数分析导言》中给出了这一法则，用于确定二次曲线的系数。

#### 定理1.3 齐次线性方程组有非零解的条件（裴蜀，1764）
含 \(n\) 个未知量的 \(n\) 个齐次线性方程组有非零解的条件是其系数行列式（结式）等于零。

### 注： 裴蜀将行列式理论与线性方程组的解的存在性联系起来，跳出了单纯的计算框架。

#### 定义1.3 行列式的展开（范德蒙，1771）
范德蒙给出了用二阶子式和它们的余子式来展开行列式的法则，使行列式理论与线性方程组求解相分离。

### 注： 范德蒙是行列式理论的奠基人之一，他还引入了范德蒙行列式。

#### 定理1.4 拉普拉斯定理（拉普拉斯，1772）
行列式可以按任意行或列展开，即拉普拉斯展开定理。

### 注： 拉普拉斯推广了范德蒙的展开方法，并给出了按多行（多列）展开的一般公式。

#### 定理1.5 行列式的乘法定理（柯西，1815）
两个方阵乘积的行列式等于它们行列式的乘积，即 \(|AB| = |A||B|\)。

### 注： 柯西在1815年的论文中系统阐述行列式理论，给出了乘法定理、伴随矩阵等概念。

#### 定理1.6 实对称矩阵的特征值均为实数（柯西，1826）
实对称矩阵的特征值都是实数。

### 注： 柯西在《微积分在几何中的应用教程》中讨论了二次型与实对称矩阵的特征值性质。

#### 引理1.1（用于定理1.6）
相似变换不改变矩阵的特征值。

### 注： 柯西在相似行列式的研究中证明了相似矩阵有相同的特征值。

#### 定义1.4 雅可比行列式（雅可比，1841）
对于函数组 \(y_i = f_i(x_1, \ldots, x_n)\)，雅可比行列式  
\[ J = \frac{\partial(y_1, \ldots, y_n)}{\partial(x_1, \ldots, x_n)} \]  
用于多重积分的变量替换。

### 注： 雅可比在《论行列式的形成和性质》中建立了行列式的系统理论。


### 1.3 矩阵理论的发展

#### 定义1.5 矩阵（西尔维斯特，1850）
矩阵是由 \(m\) 行 \(n\) 列元素组成的矩形阵列，用于表示线性方程组。

### 注： 西尔维斯特在研究方程个数与未知量个数不同的线性方程组时引入了“矩阵”一词。

#### 定义1.6 矩阵的运算（凯莱，1858）
凯莱定义了矩阵的加法、数乘、乘法（基于变换的复合）、转置、对称矩阵、零矩阵、单位矩阵等。

### 注： 凯莱在《矩阵论的研究报告》中建立了矩阵的理论体系，包括矩阵乘法的结合性、不可交换性等。

#### 定理1.7 矩阵可逆的条件（凯莱，1858）
矩阵 \(A\) 可逆的充要条件是行列式 \(|A| \neq 0\)，且逆矩阵可表示为  
\[ A^{-1} = \frac{1}{|A|} A^* \]  
其中 \(A^*\) 为伴随矩阵。

### 注： 凯莱还证明了矩阵特征多项式的根即为特征值。

#### 定理1.8 哈密顿-凯莱定理（凯莱，1858）
矩阵满足其自身的特征多项式，即若 \(p(\lambda) = |A - \lambda I|\)，则 \(p(A) = 0\)。

### 注： 凯莱证明了一部分，后由哈密顿完善，是矩阵理论中的重要定理。

#### 定义1.7 矩阵的秩（弗罗贝尼乌斯，1879）
矩阵的秩是其非零子式的最大阶数，也等于行列式的秩（即所有 \(r+1\) 阶子式为0，但存在非零 \(r\) 阶子式）。

### 注： 弗罗贝尼乌斯还引入了行列式因子、不变因子、初等因子等概念，用于若当标准形理论。

#### 定理1.9 西尔维斯特零性律（西尔维斯特，1884）
对于矩阵 \(A\) 和 \(B\)，有  
\[ r(A) + r(B) - n \leq r(AB) \leq \min\{r(A), r(B)\} \]  
其中 \(n\) 是 \(A\) 的列数（也是 \(B\) 的行数）。

### 注： 西尔维斯特将矩阵的阶数与秩的差称为“零性”，该定理是矩阵秩的重要不等式。


### 1.4 线性空间与线性映射

#### 定义1.8 向量空间（皮亚诺，1888）
向量空间是一个集合 \(V\)，配以加法和数乘运算，满足八条公理（封闭性、结合律、交换律、零元、负元、数乘结合律、数乘分配律、单位元）。

### 注： 皮亚诺在《几何计算》中给出了向量空间的公理化定义，后由外尔等人推广。

#### 定义1.9 线性映射
设 \(V, W\) 为域 \(F\) 上的向量空间，映射 \(T: V \to W\) 称为线性映射，如果满足  
\[ T(u+v) = T(u) + T(v), \quad T(\alpha v) = \alpha T(v) \]  
对任意 \(u,v \in V, \alpha \in F\) 成立。

### 注： 线性映射是线性代数的核心概念，与矩阵表示密切相关。


### 1.5 进阶：本世纪的线性代数

#### 定义1.10 矩阵多项式
一个 \(n\) 元矩阵多项式是有限个矩阵单项式的和，其中矩阵单项式为形如 \(a m_1 m_2 \cdots m_k\) 的连乘积，\(a \in \mathbf{R}\)，\(m_i\) 为矩阵变元 \(x_j\) 或其转置。

#### 定义1.11 对称矩阵多项式
矩阵多项式 \(Q\) 是对称的，如果其值域 \(\operatorname{im} Q\) 中的矩阵都是对称的。

#### 定义1.12 半正定矩阵多项式
矩阵多项式 \(Q\) 是半正定的，如果其值域 \(\operatorname{im} Q\) 中的矩阵都是半正定的。

#### 定理1.10 Helton定理（2002）
对称的矩阵多项式是半正定的，当且仅当它能被拆成一组矩阵多项式的平方和。

### 注： 该定理由Helton证明，是希尔伯特第十七问题的矩阵推广。

#### 定义1.13 迹度量距离
对于 \(n\) 阶正定矩阵 \(A, B\)，定义迹度量距离为  
\[ \delta(A, B) = \sqrt{\sum_{i=1}^n \log^2 \lambda_i(A^{-1}B)} \]  
其中 \(\lambda_i\) 表示特征值。

#### 定义1.14 Karcher均值
\(k\) 个正定矩阵 \(A_1, \ldots, A_k\) 的Karcher均值是使迹度量距离平方和最小的正定矩阵 \(X\)。

#### 引理1.2（用于定理1.11）
考虑实数 \(x_i, y_i\)，若 \(x_i \leq y_i\)，则它们的最小二乘均值满足 \(x \leq y\)。

#### 定理1.11 Bhatia-Holbrook定理（2006，Lawson-Lim 2011）
若正定矩阵 \(A_i \leq B_i\)（即 \(B_i - A_i\) 正定），则  
\[ \sigma(A_1, \ldots, A_n) \leq \sigma(B_1, \ldots, B_n) \]  
其中 \(\sigma\) 表示Karcher均值。

### 注： 该定理由Lawson和Lim在2011年证明，用到了Loewner-Heinz全局非正曲率度量空间的性质。

#### 定义1.15 谱半径
方阵 \(A\) 的谱半径 \(\rho(A)\) 为其特征值的绝对值的最大值。

#### 定理1.12 谱半径不等式（Gelfand公式推论）
对于任意方阵 \(A_1, \ldots, A_k\)，有  
\[ \rho(A_1 A_2 \cdots A_k) \leq \rho(A_1) \rho(A_2) \cdots \rho(A_k) \]

#### 定义1.16 广义谱半径
设 \(\Sigma\) 为有限个 \(m\) 阶方阵的集合，定义广义谱半径为  
\[ \rho(\Sigma) = \varlimsup_{k \to \infty} \rho_k(\Sigma) \]  
其中 \(\rho_k(\Sigma) = \max\{\rho(A_1 \cdots A_k) \mid A_i \in \Sigma\}\)。

#### 定理1.13 有限性猜想的反例（Bousch & Mairesse，2002）
存在矩阵集合 \(\Sigma\)，使得对任意有限 \(k\)，都有 \(\rho_k(\Sigma) < \rho(\Sigma)\)，即广义谱半径不能在有限步内达到。

### 注： 该猜想由Lagarias和Wang于1995年提出，2002年被证伪。

#### 定义1.17 Penrose-Moore逆
对于 \(m \times n\) 矩阵 \(A\)，其Penrose-Moore逆 \(A^\dagger\) 是满足以下条件的 \(n \times m\) 矩阵：  
1. \(A A^\dagger A = A\)  
2. \(A^\dagger A A^\dagger = A^\dagger\)  
3. \(A^\dagger A\) 和 \(A A^\dagger\) 对称（或厄米）。

### 注： Penrose-Moore逆存在且唯一，可用于求线性方程组的最小二乘解。

#### 定义1.18 弱主对角占优矩阵
矩阵 \((a_{ij})\) 是弱主对角占优的，如果对所有 \(i\)，有  
\[ a_{ii} \geq \sum_{j \neq i} |a_{ij}| \]

#### 定理1.14 Spielman-Teng定理（2014）
存在随机算法，可在 \(O(m \log^c n \log(1/\varepsilon))\) 时间内求解弱主对角占优的实对称线性方程组 \(Ax=b\) 的 \(\varepsilon\)-近似解，其中 \(m\) 为非零元个数。

### 注： 该算法基于图稀疏化技术，是线性方程组求解的重要突破。

#### 定义1.19 Bernoulli矩阵
每个元素独立同分布于成功概率 \(p=1/2\) 的Bernoulli随机变量的矩阵称为Bernoulli矩阵。

#### 定理1.15 Tikhomirov定理（2020）
\(n\) 阶Bernoulli矩阵奇异的概率为  
\[ P_n = \left(\frac{1}{2} + o(1)\right)^n \]

### 注： 该结果经历了Komlós (1967)、Kahn (1995)、陶哲轩-Vu (2007)、Bourgain (2010) 等逐步改进，最终由Tikhomirov证明。

#### 定理1.16 陶哲轩-Vu定理（2007）
\(n\) 阶Bernoulli矩阵奇异的概率为  
\[ P_n = \left(\frac{3}{4} + o(1)\right)^n \]

#### 定理1.17 Bourgain定理（2010）
\(n\) 阶Bernoulli矩阵奇异的概率为  
\[ P_n = \left(\frac{1}{\sqrt{2}} + o(1)\right)^n \]

#### 定义1.20 \(l_p\)-范数
向量 \(x\) 的 \(l_p\)-范数为  
\[ \|x\|_p = \left( \sum_i |x_i|^p \right)^{1/p} \]

#### 定义1.21 \(l_p\)-稀疏向量
若向量 \(x\) 满足 \(\|x\|_p < R\)（\(0 < p \leq 1\)，\(R\) 为正常数），则称 \(x\) 是 \(l_p\)-稀疏的。


### 1.6 未来：从线性代数出发

#### 定义1.22 模
设 \(R\) 为环，\(M\) 为Abel群，若存在映射 \(R \times M \to M\) 满足左模公理（分配律、结合律、单位元作用），则称 \(M\) 为 \(R\) 上的左模。

#### 定理1.18 Freyd-Mitchel嵌入定理（1964）
任意小的Abel范畴都可满、忠实、正合地嵌入到某个环 \(R\) 的左模范畴中。

#### 定理1.19 Quillen-Gabriel嵌入定理（1972）
任意小的Quillen正合范畴都可保正合地嵌入到Abel范畴中。

#### 定义1.23 双线性映射
设 \(V, W, Z\) 为线性空间，映射 \(f: V \times W \to Z\) 称为双线性的，如果它关于每个变量都是线性的。

#### 定义1.24 张量积
\(V\) 和 \(W\) 的张量积 \(V \otimes W\) 是一个线性空间，配以双线性映射 \(\varphi: V \times W \to V \otimes W\)，满足泛性质：对任意双线性映射 \(h: V \times W \to Z\)，存在唯一线性映射 \(\tilde{h}: V \otimes W \to Z\) 使得 \(h = \tilde{h} \circ \varphi\)。

### 注： 张量积可构造为自由空间商掉双线性关系生成的子空间。

#### 定义1.25 群的表示
群 \(G\) 到线性空间 \(V\) 上的一般线性群 \(\mathcal{L}(V)\) 的群同态 \(\rho: G \to \mathcal{L}(V)\) 称为 \(G\) 的一个表示。

#### 定义1.26 特征标
有限维表示 \(\rho: G \to \mathcal{L}(V)\) 的特征标 \(\chi_\rho: G \to F\) 定义为 \(\chi_\rho(g) = \operatorname{tr}(\rho(g))\)。

### 注： 特征标是表示论的核心工具，用于研究群的结构。

#### 定理1.20 Burnside定理
所有 \(p^a q^b\) 阶的群都是可解群。

### 注： 该定理的证明依赖于表示论，尚无纯群论证明。

#### 定理1.21 Feit-Thompson定理
所有奇数阶群都是可解群。

### 注： 证明极其复杂，是有限单群分类的重要步骤。

#### 定理1.22 有限单群分类定理（宏伟定理）
有限单群可分为四大类：循环群、交错群、李型群、26个散在单群。

### 注： 该定理的证明长达数千页，大量使用了特征标理论。

#### 定理1.23 Ore猜想（Liebeck等人，2010）
有限非Abel单群中的任意元素都是换位子。

### 注： 该猜想于1951年提出，2010年通过Deligne-Lusztig特征标理论证明。


### 隐含定理补充

#### 定理1.24 行列式的几何意义（拉格朗日）
行列式的绝对值等于其列向量所张成的平行多面体的有向体积。

### 注： 该定理揭示了行列式与几何体积的联系，是行列式公理化定义的几何基础。

#### 定理1.25 线性相关性的判定
向量组线性相关的充要条件是存在一个向量可由其余向量线性表示。

### 注： 该定理是线性方程组解的理论基础，隐含在线性方程组的讨论中。

#### 定理1.26 矩阵乘法的结合律
矩阵乘法满足结合律，即 \((AB)C = A(BC)\)。

### 注： 凯莱在定义矩阵乘法时已指出这一性质，是矩阵代数的基础。

#### 定理1.27 矩阵的秩与线性方程组解的关系
线性方程组 \(Ax = b\) 有解的充要条件是系数矩阵 \(A\) 与增广矩阵 \([A|b]\) 的秩相等。

### 注： 该定理隐含在线性方程组的讨论中，是线性代数核心结论之一。


**逐字检查完毕，无遗漏。**

---

# 第13章 多项式

## 13.1 多项式的定义

### 定义 13.1.1（数域上的多项式函数）  
设 $\mathbf{F}$ 是数域，对于函数 $p: \mathbf{F} \to \mathbf{F}$，若存在 $a_0, \ldots, a_m \in \mathbf{F}$ 使得对任意 $x \in \mathbf{F}$ 有
\[
p(x) = a_0 + a_1 x + \cdots + a_m x^m,
\]
则称函数 $p$ 为系数在 $\mathbf{F}$ 中的多项式。其中 $a_i x^i$ 称为第 $i$ 次项，使得 $a_k \neq 0$ 成立的最大整数 $k$ 称为多项式的次数，记为 $\deg p = k$。

### 定理 13.1.1  
设 $\mathbf{F}$ 是数域，$a_0, \ldots, a_m \in \mathbf{F}$，若对任意 $x \in \mathbf{F}$ 有 $p(x) = a_0 + a_1 x + \cdots + a_m x^m = 0$，则 $a_0 = \cdots = a_m = 0$。

### 定义 13.1.2（一般域上的一元多项式）  
设 $\mathbf{F}$ 是域，我们称 $\mathbf{F}$ 上的一元多项式 $p(x)$ 是一个形如下式的表达式：
\[
p(x) = a_0 + a_1 x + \cdots + a_m x^m,
\]
其中 $a_0, \ldots, a_m \in \mathbf{F}$，$m \in \mathbb{N}$，$x \notin \mathbf{F}$ 是一个符号，称为不定元。称 $a_0, \ldots, a_m$ 为多项式 $p(x)$ 的系数，$a_0$ 称为常数项，$a_i x^i$ 称为第 $i$ 次项。

对于非零多项式（即 $p(x) \neq 0$），使得 $a_k \neq 0$ 成立的最大整数 $k$ 称为多项式的次数，记为 $\deg p = k$。对于零多项式，其次数定义为 $-\infty$。称 $a_k$ 为首项系数，若 $a_k = 1$，则称多项式为首一多项式。

注：多项式的相等定义为次数相同且对应系数相等。

### 定义 13.1.3（多项式的加法、数乘和乘法）  
设 $p(x) = a_0 + a_1 x + \cdots + a_m x^m$，$q(x) = b_0 + b_1 x + \cdots + b_n x^n$，则
1. 不妨设 $m \leqslant n$，则多项式的加法定义为
   \[
   p(x) + q(x) = (a_0 + b_0) + (a_1 + b_1) x + \cdots + (a_m + b_m) x^m + b_{m+1} x^{m+1} \cdots + b_n x^n,
   \]
2. 多项式的数乘定义为
   \[
   k \cdot p(x) = k a_0 + k a_1 x + \cdots + k a_m x^m,
   \]
   其中 $k \in \mathbf{F}$；
3. 多项式的乘法定义为
   \[
   p(x) q(x) = \sum_{k=0}^{m+n} \left( \sum_{i+j=k} a_i b_j \right) x^k.
   \]

### 定理 13.1.2（多项式次数与运算）  
设 $p(x), q(x) \in \mathbf{F}[x]$，则
1. $\deg(p+q) \leqslant \max\{\deg p, \deg q\}$；
2. $\deg(kp) = \deg p$，其中 $k \in \mathbf{F}$ 且 $k \neq 0$；
3. $\deg(pq) = \deg p + \deg q$。

注：$\mathbf{F}[x]$ 关于多项式的加法和乘法构成一个环，称为多项式环。它也是 $\mathbf{F}$ 上的线性空间。

## 13.2 整除与互素

### 定义 13.2.1（整除）  
设 $p(x), q(x) \in \mathbf{F}[x]$，若存在多项式 $s(x) \in \mathbf{F}[x]$ 使得 $p(x) = s(x) q(x)$，则称 $q(x)$ 是 $p(x)$ 的因式，或 $q(x)$ 整除 $p(x)$，记为 $q(x) \mid p(x)$，否则记为 $q(x) \nmid p(x)$。

### 定理 13.2.1（整除的性质）  
设 $p(x), q(x), s(x) \in \mathbf{F}[x]$，$0 \neq k \in \mathbf{F}$，则有
1. $p(x) \mid p(x)$；
2. 若 $p(x) \mid q(x)$ 且 $q(x) \mid s(x)$，则 $p(x) \mid s(x)$；
3. 若 $p(x) \mid q(x)$，则 $k p(x) \mid q(x)$；
4. 若 $p(x) \mid q(x)$ 且 $p(x) \mid s(x)$，则对任意多项式 $u(x), v(x) \in \mathbf{F}[x]$ 有 $p(x) \mid u(x) q(x) + v(x) s(x)$。

### 定理 13.2.2（相伴的充要条件）  
设非零多项式 $p(x), q(x) \in \mathbf{F}[x]$，且满足 $p(x) \mid q(x)$ 和 $q(x) \mid p(x)$，则存在非零常数 $k \in \mathbf{F}$ 使得 $p(x) = k q(x)$。

### 定义 13.2.2（相伴）  
设非零多项式 $p(x), q(x) \in \mathbf{F}[x]$，若 $p(x) \mid q(x)$ 且 $q(x) \mid p(x)$，则称 $p(x)$ 与 $q(x)$ 相伴，记为 $p(x) \sim q(x)$。

### 定理 13.2.3（带余除法）  
设 $p(x), s(x) \in \mathbf{F}[x]$ 且 $s(x) \neq 0$，则存在唯一的多项式 $q(x), r(x) \in \mathbf{F}[x]$，使得 $p(x) = s(x) q(x) + r(x)$，且 $\deg r < \deg s$。

### 定义 13.2.3（最大公因式和最小公倍式）  
设 $p(x), q(x), d(x) \in \mathbf{F}[x]$，若 $d(x) \mid p(x)$ 且 $d(x) \mid q(x)$，则称 $d(x)$ 是 $p(x)$ 和 $q(x)$ 的一个公因式。若 $d(x)$ 满足对 $p(x)$ 和 $q(x)$ 的任一公因式 $d'(x)$ 都有 $d'(x) \mid d(x)$，则称 $d(x)$ 是 $p(x)$ 和 $q(x)$ 的一个最大公因式，记为 $\gcd(p(x), q(x)) = d(x)$。

类似地，若 $p(x) \mid l(x)$ 且 $q(x) \mid l(x)$，则称 $l(x)$ 是 $p(x)$ 和 $q(x)$ 的一个公倍式。若 $l(x)$ 满足对 $p(x)$ 和 $q(x)$ 的任一公倍式 $l'(x)$ 都有 $l(x) \mid l'(x)$，则称 $l(x)$ 是 $p(x)$ 和 $q(x)$ 的一个最小公倍式，记为 $\operatorname{lcm}(p(x), q(x)) = l(x)$。

注：我们规定最大公因式和最小公倍式都是首一多项式，以保证唯一性。

### 定理 13.2.4（欧几里得算法）  
设 $p(x), q(x) \in \mathbf{F}[x]$，则它们的最大公因式 $d(x)$ 必存在，且存在 $u(x), v(x) \in \mathbf{F}[x]$ 使得
\[
d(x) = u(x) p(x) + v(x) q(x).
\]

### 定义 13.2.4（互素）  
设 $p(x), q(x) \in \mathbf{F}[x]$，若 $\gcd(p(x), q(x)) = 1$，则称 $p(x)$ 和 $q(x)$ 互素。

### 定理 13.2.5（裴蜀定理）  
设 $p(x), q(x) \in \mathbf{F}[x]$，则 $p(x)$ 和 $q(x)$ 互素的充要条件是存在 $u(x), v(x) \in \mathbf{F}[x]$ 使得
\[
u(x) p(x) + v(x) q(x) = 1.
\]

### 定理 13.2.6（互素的基本性质）  
设 $p(x), q(x), s(x), d(x) \in \mathbf{F}[x]$，则有
1. 若 $p(x) \mid s(x)$，$q(x) \mid s(x)$ 且 $(p(x), q(x)) = 1$，则 $p(x) q(x) \mid s(x)$；
2. 若 $(p(x), q(x)) = 1$，且 $p(x) \mid q(x) s(x)$，则 $p(x) \mid s(x)$；
3. 若 $(p(x), q(x)) = d(x)$，设 $p(x) = p_1(x) d(x)$，$q(x) = q_1(x) d(x)$，则 $(p_1(x), q_1(x)) = 1$；
4. 若 $(p(x), q(x)) = d(x)$，则 $(s(x) p(x), s(x) q(x)) = s(x) d(x)$；
5. 若 $(p(x), q(x)) = 1$，$(p(x), s(x)) = 1$，则 $(p(x), q(x) s(x)) = 1$。

### 定理 13.2.7（最小公倍式与最大公因式的关系）  
设非零多项式 $p(x), q(x) \in \mathbf{F}[x]$，则
\[
p(x) q(x) = c \cdot \gcd(p(x), q(x)) \cdot \operatorname{lcm}(p(x), q(x)),
\]
其中 $c$ 为 $p(x) q(x)$ 的首项系数。

### 定理 13.2.8（中国剩余定理）  
设 $q_1(x), q_2(x), \ldots, q_n(x) \in \mathbf{F}[x]$ 两两互素，则对任意的 $r_1(x), r_2(x), \ldots, r_n(x) \in \mathbf{F}[x]$，方程组
\[
\begin{cases}
p(x) \equiv r_1(x) \pmod{q_1(x)}, \\
p(x) \equiv r_2(x) \pmod{q_2(x)}, \\
\cdots \\
p(x) \equiv r_n(x) \pmod{q_n(x)},
\end{cases}
\]
模 $Q(x) = \prod_{i=1}^n q_i(x)$ 有唯一解。

## 13.3 多项式的因式分解

### 定义 13.3.1（可约与不可约多项式）  
设 $p(x) \in \mathbf{F}[x]$ 是非常数多项式，若 $p(x)$ 可以分解为两个次数小于 $p(x)$ 次数的多项式的乘积，则称 $p(x)$ 是域 $\mathbf{F}$ 上的可约多项式，否则称 $p(x)$ 是域 $\mathbf{F}$ 上的不可约多项式。

注：多项式的可约性与域有关。

### 定理 13.3.1（不可约多项式的性质）  
设 $p(x)$ 是域 $\mathbf{F}$ 上的不可约多项式，
1. 对于任意多项式 $q(x) \in \mathbf{F}[x]$，或者 $p(x) \mid q(x)$，或者 $(p(x), q(x)) = 1$；
2. 设 $q(x), s(x) \in \mathbf{F}[x]$，且 $p(x) \mid q(x) s(x)$，则或者 $p(x) \mid q(x)$，或者 $p(x) \mid s(x)$。

### 推论 13.3.1（不可约多项式的性质推广）  
设 $p(x)$ 是域 $\mathbf{F}$ 上的不可约多项式且 $p(x) \mid q_1(x) q_2(x) \cdots q_n(x)$，则 $p(x)$ 必可整除其中某个 $q_i(x)$。

### 定理 13.3.2（多项式的唯一分解定理）  
设 $p(x) \in \mathbf{F}[x]$ 是非常数多项式，则
1. $p(x)$ 可以分解为不可约多项式的乘积；
2. 若 $p(x) = q_1(x) q_2(x) \cdots q_m(x) = s_1(x) s_2(x) \cdots s_n(x)$ 为 $p(x)$ 的两个不可约分解，则 $m = n$，且经过适当调换顺序后有 $q_i(x) \sim s_i(x)$，$i = 1, 2, \ldots, n$。

注：标准分解式：$p(x) = c (q_1(x))^{\alpha_1} (q_2(x))^{\alpha_2} \cdots (q_m(x))^{\alpha_m}$，其中 $c$ 为非零常数，$\alpha_i$ 为正整数，$q_i(x)$ 为不可约多项式。若 $\alpha_i > 1$，则称 $q_i(x)$ 是重因式，否则称为单因式。

### 定义 13.3.2（形式导数）  
设 $p(x) = a_0 + a_1 x + \cdots + a_n x^n \in \mathbf{F}[x]$，则 $p(x)$ 的形式导数定义为
\[
p'(x) = a_1 + 2 a_2 x + \cdots + n a_n x^{n-1}.
\]

### 定理 13.3.3（重因式的判别）  
设 $p(x) \in \mathbf{F}[x]$，则 $p(x)$ 没有重因式的充要条件为 $(p(x), p'(x)) = 1$。

### 定理 13.3.4（消去重因式）  
设 $d(x) = (p(x), p'(x))$，则 $p(x) / d(x)$ 没有重因式，且这个多项式的不可约因式与 $p(x)$ 的不可约因式仍然相同（不计重数）。

## 13.4 复数域上的多项式函数

### 定义 13.4.1（零点）  
设 $p(x) \in \mathbf{F}[x]$，则 $p(x)$ 的零点（或根）是指方程 $p(x) = 0$ 的解。

### 定理 13.4.1（多项式函数根的性质）  
设 $p(x) \in \mathbf{F}[x]$。
1. 若 $\lambda \in \mathbf{F}$，则 $p(\lambda) = 0$ 当且仅当存在多项式 $q(x) \in \mathbf{F}[x]$ 使得 $p(x) = (x - \lambda) q(x)$；
2. 若 $p(x)$ 是 $m\ (m \geqslant 0)$ 次多项式，则 $p(x)$ 在 $\mathbf{F}$ 上最多有 $m$ 个互不相等的零点；
3. 若 $p(x)$ 是不可约多项式且 $\deg p \geqslant 2$，则 $p(x)$ 在 $\mathbf{F}$ 上没有零点。

### 定义 13.4.2（重根）  
设 $p(x) \in \mathbf{F}[x]$，$\lambda \in \mathbf{F}$，若存在 $k \geqslant 1$ 使得 $(x - \lambda)^k \mid p(x)$，但 $(x - \lambda)^{k+1} \nmid p(x)$，则称 $\lambda$ 是 $p(x)$ 的一个 $k$ 重根。若 $k = 1$，则称 $\lambda$ 是 $p(x)$ 的一个单根。

### 定理 13.4.2（代数学基本定理）  
非常数复多项式在复平面上必有零点。

### 推论 13.4.1  
1. 复数域上的 $n$ 次多项式有且仅有 $n$ 个复根（含重数）；
2. 复数域上的不可约多项式都是一次多项式，且复数域上的 $n$ 次多项式可以唯一分解为 $n$ 个一次多项式的乘积。

### 定理 13.4.3（韦达定理）  
设 $p(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0 \in \mathbf{F}[x]$，$\lambda_1, \lambda_2, \ldots, \lambda_n$ 是 $p(x)$ 视为复数域上多项式的 $n$ 个根，则
\[
\sum_{i=1}^n \lambda_i = -\frac{a_{n-1}}{a_n}, \quad \sum_{1 \leqslant i < j \leqslant n} \lambda_i \lambda_j = \frac{a_{n-2}}{a_n}, \quad \ldots, \quad \lambda_1 \lambda_2 \cdots \lambda_n = (-1)^n \frac{a_0}{a_n}.
\]

## 13.5 实数域与有理数域上的多项式函数

### 引理 13.5.1（实数域共轭根）  
设 $p(x) \in \mathbf{R}[x]$，若复数 $\lambda$ 是 $p(x)$ 的一个根，则其共轭复数 $\overline{\lambda}$ 也是 $p(x)$ 的一个根。

### 引理 13.5.2（实数域上不可约多项式的形式）  
实数域上的不可约多项式为一次多项式，或下列二次多项式：$a x^2 + b x + c$，其中 $b^2 - 4 a c < 0$。

### 定理 13.5.1（实数域上多项式分解）  
设 $p(x) \in \mathbf{R}[x]$ 是非常数多项式，则 $p(x)$ 可以唯一分解为
\[
p(x) = c (x - \lambda_1) \cdots (x - \lambda_m) (x^2 + b_1 x + c_1) \cdots (x^2 + b_M x + c_M),
\]
其中 $c, \lambda_1, \ldots, \lambda_m, b_1, \ldots, b_M, c_1, \ldots, c_M \in \mathbf{R}$，并且对每个 $j$ 均有 $b_j^2 < 4 c_j$。

### 定理 13.5.2（整系数多项式有有理根的必要条件）  
设 $p(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0 \in \mathbf{Z}[x]$，且 $x_0 = \dfrac{q}{p}$ 是 $p(x)$ 的一个有理根，其中 $p, q \in \mathbf{Z}$，且 $(p, q) = 1$，则 $p \mid a_n$ 且 $q \mid a_0$。

### 定义 13.5.1（本原多项式）  
设 $p(x) \in \mathbf{Z}[x]$，若 $(a_0, a_1, \ldots, a_n) = 1$，则称 $p(x)$ 是本原多项式。

### 引理 13.5.3（高斯引理）  
设 $p(x), q(x) \in \mathbf{Z}[x]$ 是本原多项式，则 $p(x) q(x)$ 也是本原多项式。

### 定理 13.5.3（有理系数多项式的可约性）  
整系数多项式在有理数域上可约，则它必可以分解为两个次数较低的整系数多项式之积。

注：等价地，整系数多项式在有理数域上不可约当且仅当在整数环上不可约。

### 定理 13.5.4（艾森斯坦判别法）  
设 $p(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0 \in \mathbf{Z}[x]$，$a_n \neq 0$ 且 $n \geqslant 1$，若存在一个素数 $p$，满足
1. $p \mid a_0, p \mid a_1, \ldots, p \mid a_{n-1}$，
2. $p \nmid a_n$，
3. $p^2 \nmid a_0$，
则 $p(x)$ 在有理数域上不可约。

注：艾森斯坦判别法是充分条件而非必要条件。

## 补充定理（来自例题和习题）

### 定理 13.6.1（多项式环的无零因子性）  
设 $p(x), q(x) \in \mathbf{F}[x]$，若 $p(x), q(x) \neq 0$，则 $p(x) q(x) \neq 0$。

### 定理 13.6.2（多项式环的消去律）  
若 $p(x) \neq 0$，且 $p(x) q(x) = p(x) r(x)$，则 $q(x) = r(x)$。

### 定理 13.6.3（多项式整除的传递性）  
若 $p(x) \mid q(x)$ 且 $q(x) \mid r(x)$，则 $p(x) \mid r(x)$。

### 定理 13.6.4（多项式互素的充要条件）  
$\mathbf{F}[x]$ 中两个次数大于0的多项式没有公共复根的充要条件是它们互素。

### 定理 13.6.5（多项式相等的判定）  
设 $p(x)$ 和 $q(x)$ 是 $\mathbf{F}[x]$ 中的两个次数不超过 $n$ 的多项式，若存在 $\mathbf{F}$ 上 $n+1$ 个不同的数 $\lambda_0, \lambda_1, \ldots, \lambda_n$ 使得 $p(\lambda_i) = q(\lambda_i)$，$i = 0, 1, \ldots, n$，则 $p(x) = q(x)$。

### 定理 13.6.6（奇数次实多项式必有实根）  
每个奇数次的实系数多项式都有实的零点。

### 定理 13.6.7（重根的导数判别法）  
设 $p \in \mathbf{F}[x]$ 且 $q \neq 0$，则 $c$ 是 $f(x)$ 的 $k\ (k \geqslant 1)$ 重根的充要条件为
\[
f(c) = f'(c) = \cdots = f^{(k-1)}(c) = 0, \quad f^{(k)}(c) \neq 0.
\]

### 定理 13.6.8（多项式理想的商空间维数）  
设 $\mathbf{F}[x]$ 是域 $\mathbf{F}$ 上的全体多项式构成的线性空间，非零多项式 $p(x) \in \mathbf{F}[x]$，记 $(p(x)) = \{ p(x) q(x) \mid q(x) \in \mathbf{F}[x] \}$，则
1. $(p(x))$ 是 $\mathbf{F}[x]$ 的一个子空间；
2. 商空间 $\mathbf{F}[x] / (p(x))$ 的维数等于 $\deg p$，且一组基为 $\{1 + (p(x)), x + (p(x)), \ldots, x^{n-1} + (p(x))\}$，其中 $n = \deg p$。

注：此定理在例题“多项式域扩张”中给出。

---

# 第14章 相似标准形：动机与基础

## 14.1 相似的定义与性质

### 定义 14.1.1（相似，矩阵角度）  
若对于 $A,B\in \mathbf{M}_n(\mathbf{F})$，存在可逆矩阵 $C\in \mathbf{M}_n(\mathbf{F})$，使得 $C^{-1}AC=B$，则称 $A$ 相似于 $B$，记作 $A\sim B$。

### 注： 相似是矩阵之间的等价关系。

### 定理 14.1.1（相似的性质）  
相似具有以下性质：
1. 相似是一种等价关系；两矩阵相似必相抵（相似矩阵的秩相等）。
2. $A\sim B$ 可以得到 $A^\mathrm{T}\sim B^\mathrm{T}$，$A^m\sim B^m$。更一般地，对于任意多项式 $f(x)$ 都有 $f(A)\sim f(B)$，且若 $B=P^{-1}AP$，有 $f(B)=P^{-1}f(A)P$。除此之外还有 $A,B$ 可逆时，$A^{-1}\sim B^{-1}$，$A^*\sim B^*$。
3. $A_1\sim B_1$，$A_2\sim B_2$ 不一定有 $A_1+A_2\sim B_1+B_2$，只有当 $P^{-1}A_1P=B_1,P^{-1}A_2P=B_2$ 时（即相同的过渡矩阵 $P$）才有 $P^{-1}(A_1+A_2)P=B_1+B_2$。
4. 若 $A_1\sim B_1$，$A_2\sim B_2$，则有
   \[ \begin{pmatrix} A_1 & O \\ O & A_2 \end{pmatrix}\sim\begin{pmatrix} B_1 & O \\ O & B_2 \end{pmatrix}。 \]
5. 与数量矩阵相似的为其自身，与幂等矩阵相似的仍幂等，与对合矩阵相似的仍对合，与幂零矩阵相似的仍幂零，与正交矩阵正交相似的仍正交（但与正交矩阵相似的不一定正交）。

### 注： 性质5中与正交矩阵相似不一定正交，只有当过渡矩阵是正交矩阵时才保证相似后的矩阵仍正交。

## 14.2 不变子空间

### 定义 14.2.1（不变子空间）  
设 $\sigma\in \mathcal{L}(V)$，若 $V$ 的子空间 $U$ 满足 $\forall \alpha\in U,\enspace \sigma(\alpha)\in U$，则称 $U$ 是 $\sigma$ 的**不变子空间**，或称 $U$ 在 $\sigma$ 下不变，简称为 $\sigma$-子空间。

### 定义 14.2.2（限制映射）  
设 $V$ 是数域 $\mathbf{F}$ 上的线性空间，$\sigma\in\mathcal{L}(V)$，我们在 $V$ 的子空间 $U$ 上定义映射 $\sigma\vert_U$ 如下：
\[ \sigma\vert_U:U\to V,\enspace\sigma\vert_U(\alpha)=\sigma(\alpha),\enspace\forall \alpha\in U, \]
则称 $\sigma\vert_U$ 是 $\sigma$ 在 $U$ 上的**限制映射**。

### 注： 若 $U$ 是 $\sigma$ 的不变子空间，则 $\sigma\vert_U$ 是线性变换（属于 $\mathcal{L}(U)$），称为**限制变换**。

### 定理 14.2.1（不变子空间与分块对角矩阵）  
设有限维线性空间 $V$ 上的线性变换 $\sigma\in\mathcal{L}(V)$ 在某组基下的表示矩阵为分块对角矩阵 $A=\operatorname{diag}(A_1,\ldots,A_m)$，当且仅当 $V$ 可以分解为不变子空间 $U_1,\ldots,U_m$ 的直和，即
\[ V=U_1\oplus\cdots\oplus U_m, \]
其中每个 $U_i$ 都是 $\sigma$ 的不变子空间，且 $\sigma\vert_{U_i}$ 在 $U_i$ 对应的基下的表示矩阵为 $A_i$。

**例 14.2.1**（多项式不变子空间）  
若 $\sigma\in\mathcal{L}(V)$ 且 $p\in\mathbf{F}[x]$ 为多项式，则 $\ker p(\sigma)$ 和 $\operatorname{im} p(\sigma)$ 在 $\sigma$ 下不变。

### 定义 14.2.3（循环子空间）  
设 $T\in\mathcal{L}(V)$，$v\in V$ 是一个非零向量。我们称子空间
\[ W=\operatorname{span}(v,Tv,T^2v,\ldots,T^kv,\cdots) \]
为**由 $v$ 生成的 $T$-循环子空间**。在不引起歧义的情况下，我们也称 $W$ 为**$T$-循环子空间**或**循环子空间**。

### 定理 14.2.2（循环子空间的性质）  
设 $V$ 是有限维线性空间，$T\in\mathcal{L}(V)$，$v\in V$ 是一个非零向量，$W$ 是由 $v$ 生成的 $T$-循环子空间，则
1. $W$ 是 $T$ 包含 $v$ 的最小不变子空间；
2. 若 $W$ 的维数为 $m$，则 $W$ 的一组基为 $\{v,Tv,\ldots,T^{m-1}v\}$（我们称其为一组循环基）。

### 定义 14.2.4（商线性变换）  
设 $\sigma\in \mathcal{L}(V)$，$U$ 是 $\sigma$ 的不变子空间，定义映射 $\sigma/U:V/U\to V/U$ 如下：
\[ (\sigma/U)(v+U)=\sigma(v)+U,\enspace\forall v\in V, \]
则称 $\sigma/U$ 是 $\sigma$ 在 $U$ 上的**商线性变换**。

### 注： 商线性变换是良定义的，且是线性的。

## 14.3 特征值与特征向量

### 14.3.1 特征值与特征向量的定义与求解

### 定义 14.3.1（线性变换的特征值与特征向量）  
设 $\sigma$ 是线性空间 $V(\mathbf{F})$ 上的一个线性变换，如果存在数 $\lambda\in\mathbf{F}$ 和非零向量 $\xi\in V$ 使得 $\sigma(\xi)=\lambda\xi$，则称数 $\lambda$ 为 $\sigma$ 的一个**特征值**，并称非零向量 $\xi$ 为 $\sigma$ 属于其特征值 $\lambda$ 的**特征向量**。

### 定义 14.3.2（特征子空间）  
对于某一个 $\lambda\in\mathbf{F}$，我们将所有满足 $\sigma(\xi)=\lambda\xi$ 的向量构成的集合记为 $E(\lambda,\sigma)=\{\xi \mid \sigma(\xi)=\lambda\xi,\enspace\xi\in V\}$（在去除线性变换不引起歧义的情况下可简写为 $V_\lambda$），称为 $\sigma$ 关于其特征值 $\lambda$ 的**特征子空间**。

### 注： 特征子空间是 $V$ 的子空间，并且是 $\sigma$ 的不变子空间。

### 定义 14.3.3（矩阵的特征值与特征向量）  
设矩阵 $A\in \mathbf{M}_n(\mathbf{F})$，如果存在数 $\lambda\in\mathbf{F}$ 和非零向量 $X\in\mathbf{F}^n$ 使得 $AX=\lambda X$，则称数 $\lambda$ 为 $A$ 的一个特征值，称非零向量 $X$ 为 $A$ 属于其特征值 $\lambda$ 的特征向量。

### 定理 14.3.1（特征值的等价条件）  
设 $\sigma$ 是 $V(\mathbf{F})$ 上的线性变换，$I$ 为恒等映射，则下述条件等价：
1. $\lambda\in\mathbf{F}$ 是 $\sigma$ 的特征值；
2. $\sigma-\lambda I$ 不是单射；
3. $\sigma-\lambda I$ 不是满射；
4. $\sigma-\lambda I$ 不可逆。

### 定义 14.3.4（特征多项式）  
设 $A\in\mathbf{M}_n(\mathbf{F})$，称 $f(\lambda)=|\lambda E-A|$ 为矩阵 $A$ 的**特征多项式**。其 $k$ 重根称为 $k$ 重特征值（称 $k$ 为代数重数），该特征值对应的特征子空间维数称为该特征值的几何重数。

### 定理 14.3.2（特征多项式展开）  
对于 $A=(a_{ij})\in\mathbf{M}_n(\mathbf{F})$，记
\[ f(\lambda)=|\lambda E-A|=a_0\lambda^n+a_1\lambda^{n-1}+\cdots+a_{n-1}\lambda+a_n \]
则 $a_0=1$，$a_1=-\operatorname{tr}(A)$，$a_n=(-1)^n|A|$，且 $a_k$ 等于所有 $k$ 级主子式之和乘以 $(-1)^k$。

### 推论 14.3.1  
设 $A\in\mathbf{M}_n(\mathbf{F})$ 的特征值为 $\lambda_1,\ldots,\lambda_n$（按重数计），则
1. $\displaystyle\sum_{i=1}^{n}\lambda_i=\operatorname{tr}(A)$；
2. $\displaystyle\prod_{i=1}^{n}\lambda_i=|A|$。

### 定理 14.3.3（相似矩阵特征多项式相同）  
相似矩阵有相同的特征多项式（逆命题不成立），即 $A\sim B$ 有 $|\lambda E-A|=|\lambda E-B|$，从而有相同的迹，行列式，特征值，但特征向量不一定相同。

### 14.3.2 特征值的基本性质

### 定理 14.3.4（特征值的多项式性质）  
设 $\lambda$ 是线性空间 $V(\mathbf{F})$ 上的线性变换 $\sigma$ 的特征值，$\xi$ 是 $\sigma$ 属于 $\lambda$ 的特征向量，则
1. $k\lambda$ 是 $k\sigma$ 的特征值，$\lambda^m$ 是 $\sigma^m$ 的特征值，且 $\xi$ 仍是相应特征向量；
2. 若 $f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0$ 是 $\mathbf{F}$ 上的多项式，则 $f(\sigma)(\xi)=f(\lambda)\xi$。

### 定理 14.3.5（可逆矩阵的特征值）  
设 $\lambda$ 是 $n$ 阶矩阵 $A$ 的特征值，$A$ 可逆，则 $\lambda^{-1}$ 是 $A^{-1}$ 的特征值，$|A|\lambda^{-1}$ 是 $A$ 的伴随矩阵 $A^*$ 的特征值，且特征向量不变。

### 定理 14.3.6（转置矩阵的特征值）  
设 $A$ 为 $n$ 阶矩阵，则 $A$ 与 $A^\mathrm{T}$ 有相同的特征值（含重数）。

**例 14.3.1**（矩阵方程与特征值）  
设 $A \in \mathbf{F}^{n \times n}$，且存在多项式 $f(x)\in \mathbf{F}[x]$ 使得 $f(A)=a_mA^m+a_{m-1}A^{m-1}+\cdots+a_1A+a_0E=O$，则对于任意的 $\lambda \in \mathbf{F}$，$f(\lambda) \neq 0 \implies A-\lambda E_n$ 可逆。  
等价地，对于任意的 $\lambda \in \mathbf{F}$，若 $\lambda$ 为 $A$ 的特征值，则 $f(\lambda)=0$。

### 注： 此例表明，若矩阵满足一个多项式方程，则其特征值只能是该多项式方程的根。

### 14.3.3 特征向量的基本性质

### 定理 14.3.7（特征向量的线性无关性）  
设 $V$ 是有限维的，$\sigma\in \mathcal{L}(V)$ 且 $\lambda_1,\ldots,\lambda_m$ 是 $\sigma$ 的互异特征值，$\xi_1,\ldots,\xi_m$ 是相应的特征向量，则 $\xi_1,\ldots,\xi_m$ 线性无关。

### 定理 14.3.8（特征子空间的直和）  
设 $V$ 是有限维的，$\sigma\in \mathcal{L}(V)$ 且 $\lambda_1,\ldots,\lambda_m$ 是 $\sigma$ 的互异特征值，则特征子空间 $V_{\lambda_1},\ldots,V_{\lambda_m}$ 的和是直和，即 $V_{\lambda_1}+\cdots+V_{\lambda_m}=V_{\lambda_1}\oplus\cdots\oplus V_{\lambda_m}$。

### 推论 14.3.2  
1. 若 $\lambda_1,\ldots,\lambda_m$ 是线性映射 $\sigma$ 互异的特征值，则 $V_{\lambda_i}\cap\sum_{j\neq i}V_{\lambda_j}=\{0\} \enspace(i=1,\ldots,m)$。
2. $\sigma$ 的不同特征值 $\lambda_1,\ldots,\lambda_m$ 对应的特征子空间 $V_{\lambda_1},\ldots,V_{\lambda_m}$ 的基向量合在一起构成的向量组线性无关，且是 $V_{\lambda_1}+V_{\lambda_2}+\cdots+V_{\lambda_m}$ 的基。

### 定理 14.3.9（代数重数与几何重数）  
$n$ 维线性空间 $V(\mathbf{F})$ 的线性变换 $\sigma$ 的每个特征值 $\lambda_0$ 的重数（代数重数）大于等于其特征子空间 $V_{\lambda_0}$ 的维数（几何重数）。

**例 14.3.2**（特征向量的性质）  
设 $V(\mathbf{F})$ 是 $n$ 维线性空间，$\sigma\in \mathcal{L}(V)$，则：
1. 若 $\alpha,\beta$ 是 $\sigma$ 的属于不同特征值的特征向量，则 $c_1c_2\neq 0$ 时，$c_1\alpha+c_2\beta$ 不是 $\sigma$ 的特征向量；
2. $V$ 中的每一非零向量都是 $\sigma$ 的特征向量 $\iff \sigma=c_0I_V$，其中 $c_0\in\mathbf{F}$ 是一个常数，$I_V$ 是恒等变换。

### 定理 14.3.10（矩阵方程 $AX-XB=O$ 的解的秩）  
设 $A,B$ 分别为数域 $\mathbf{F}$ 上 $n$ 阶、$m$ 阶方阵，$A,B$ 有 $r$ 个两两不等的公共特征值，则矩阵方程 $AX-XB=O$ 有秩为 $r$ 的矩阵解。反之，若数域为复数域，矩阵方程 $AX-XB=O$ 有秩为 $r$ 的矩阵解，则 $A,B$ 至少有 $r$ 个公共的特征值（计重数）。

### 推论 14.3.3  
复数域上 $n$ 阶、$m$ 阶方阵 $A,B$ 的矩阵方程 $AX=XB$ 只有零解的充要条件是 $A,B$ 没有公共特征值。

**例 14.3.3**（特征向量生成线性无关组）  
设 $A\in \mathbf{M}_n(\mathbf{F})$，$E$ 是 $n$ 阶单位矩阵，$\alpha_1 \in \mathbf{F}^n$ 是 $A$ 的属于特征值 $\lambda$ 的一个特征向量，向量组 $\alpha_1,\alpha_2,\ldots,\alpha_s$ 按如下方式产生：$(A-\lambda E)\alpha_{i+1}=\alpha_i,\enspace i=1,2,\ldots,s-1$。则向量组 $\{\alpha_1,\alpha_2,\ldots,\alpha_s\}$ 线性无关。

### 14.3.4 实数域与复数域的讨论

### 定理 14.3.11（复数域上的特征值存在性）  
设 $\sigma\in \mathcal{L}(V)$，$V$ 是 $n$ 维复线性空间，则 $\sigma$ 必有特征值。

### 定理 14.3.12（不变子空间的存在性）  
任取 $\sigma\in \mathcal{L}(V)$，$V$ 是 $n$ 维线性空间（无论数域是实或复），则 $\sigma$ 一定有一维或二维不变子空间。

### 14.3.5 特征值的估计

### 定义 14.3.5（Gershgorin 圆盘）  
设 $T \in \mathcal{L}(V)$，并且 $v_1, \ldots, v_n$ 是 $V$ 的一组基，$A = (a_{ij})_{n \times n}$ 为 $T$ 在这组基下的矩阵表示。那么 $T$ 关于这组基的一个 **Gershgorin 圆盘** 是指如下形式的集合：
\[ D_i = \left\{z \in \mathbf{F} \mid \lvert z - a_{ii} \rvert \leqslant \sum_{j \neq i} \lvert a_{ij} \rvert\right\}, i = 1, \ldots, n. \]

### 定理 14.3.13（Gershgorin 圆盘第一定理）  
设 $T \in \mathcal{L}(V)$，并且 $v_1, \ldots, v_n$ 是 $V$ 的一组基。那么 $T$ 的每个特征值都在其关于 $v_1, \ldots, v_n$ 这组基的某个 Gershgorin 圆盘内。

### 定理 14.3.14（Gershgorin 圆盘第二定理）  
设 $T \in \mathcal{L}(V)$，并且 $v_1, \ldots, v_n$ 是 $V$ 的一组基，$D_i, i = 1, \ldots, n$ 是 $T$ 关于这组基的 Gershgorin 圆盘。若 $\cup_{i = 1}^n D_i$ 是 $k$ 个不相交的连通区域 $R_1, \ldots, R_k$ 的并，并且 $R_r$ 是一个 $m_r$ 个 Gershgorin 圆盘的并，那么 $T$ 有 $m_r$ 个特征值落在 $R_r$ 中，$r = 1, \ldots, k$。

### 推论 14.3.4  
1. 若 $T$ 的 $n$ 个 Gershgorin 圆盘互不相交，那么 $T$ 可对角化；
2. 若 $T$ 是实算子，且 $T$ 的 $n$ 个 Gershgorin 圆盘互不相交，那么 $T$ 的特征值都是实数。

### 注： Gershgorin 圆盘也可以用列和来定义，类似定理同样成立。

## 补充（隐含在例题和习题中的一般性定理）

### 定理 14.4.1（线性变换在商空间上的诱导映射）  
设 $\sigma\in \mathcal{L}(V,W)$，定义 $\widetilde{\sigma}:(V/(\ker \sigma))\to W$ 如下：
\[ \widetilde{\sigma}(v+\ker\sigma)=\sigma(v). \]
则：
1. $\widetilde{\sigma}$ 是良定义的，且是 $(V/(\ker \sigma))$ 到 $W$ 上的线性映射；
2. $\widetilde{\sigma}$ 是单射；
3. $\operatorname{im} \widetilde{\sigma}=\operatorname{im} \sigma$；
4. $V/(\ker \sigma)$ 同构于 $\operatorname{im} \sigma$。

### 定理 14.4.2（数乘变换的刻画）  
设 $T\in \mathcal{L}(V)$，则 $T$ 是数乘变换（即 $T=cI_V$，其中 $c$ 为非零常数，$I_V$ 为 $V$ 上的恒等映射）的充要条件是 $V$ 的每一个一维子空间都是 $T$ 的不变子空间。

### 定理 14.4.3（商线性变换的性质）  
设 $\sigma\in \mathcal{L}(V)$，则：
1. $\sigma/(\operatorname{im} \sigma)=0$；
2. $\sigma/(\ker \sigma)$ 是单射 $\iff \ker \sigma\cap \operatorname{im} \sigma=\{0\}$。

### 定理 14.4.4（商线性变换的特征值）  
设 $V$ 是有限维的，$T\in \mathcal{L}(V)$ 且 $U$ 在 $T$ 下不变。则 $T/U$ 的每个特征值均为 $T$ 的特征值。

### 定理 14.4.5（可交换线性变换有公共特征向量）  
若 $AB=BA$，则 $A$ 和 $B$ 至少有一个共同的特征向量。

### 定理 14.4.6（特征值的平方和与矩阵元素的关系）  
设 $\lambda_1,\lambda_2,\ldots,\lambda_n$ 是矩阵 $A=(a_{ij})_{n\times n}$ 的 $n$ 个特征值，则 $\lambda_1^2,\lambda_2^2,\ldots,\lambda_n^2$ 是 $A^2$ 的 $n$ 个特征值，且 $\displaystyle\sum_{i=1}^{n}\lambda_i^2=\sum_{j=1}^{n}\sum_{k=1}^{n}a_{jk}a_{kj}$。

### 定理 14.4.7（严格对角占优矩阵的可逆性）  
严格对角占优的矩阵是可逆的。

### 定理 14.4.8（矩阵多项式的可逆性）  
设 $A,B\in \mathbf{M}_n(\mathbf{C})$，$B$ 的特征多项式 $f(\lambda)=|\lambda E-B|$。则 $f(A)$ 可逆的充要条件是 $B$ 的任一特征值都不是 $A$ 的特征值。

### 注： 以上补充的定理有些来自习题，有些来自例题，但都具有一般性，在笔记中应当注意。

---

# 第15章 相似标准形：复数域上的尝试与理论 - 定义、定理与引理总结

## §1 对角矩阵

### 定义1.1 可对角化（线性变换）
设 $\sigma \in \mathcal{L}(V)$，如果存在 $V$ 的一组基使得 $\sigma$ 在这组基下的矩阵是对角矩阵，则称 $\sigma$ **可对角化**。

### 定理1.1 对角矩阵等价一维不变子空间
$n$ 维线性空间 $V$ 上的线性变换 $\sigma \in \mathcal{L}(V)$ 在基 $B = \{\alpha_1, \ldots, \alpha_n\}$ 下的表示矩阵为对角矩阵 $\operatorname{diag}(d_1, \ldots, d_n)$，当且仅当 $V$ 能分解为 $\sigma$ 的一维不变子空间的直和，即 $V = U_1 \oplus \cdots \oplus U_n$，其中 $U_i = \operatorname{span}(\alpha_i)$ 是 $\sigma$ 的一维不变子空间。

### 定理1.2 可对角化条件
设 $V$ 是数域 $\mathbf{F}$ 上的 $n$ 维线性空间，$\sigma$ 是 $V$ 上的线性变换，$\lambda_1, \lambda_2, \ldots, \lambda_s \in \mathbf{F}$ 是 $\sigma$ 的所有互异特征值，则以下条件等价：
1. $\sigma$ 可对角化。
2. $\sigma$ 有 $n$ 个线性无关的特征向量，它们构成 $V$ 的一组基。
3. $V$ 有在 $\sigma$ 下不变的一维子空间 $U_1, \ldots, U_n$，使得 $V = U_1 \oplus \cdots \oplus U_n$。
4. $V = V_{\lambda_1} \oplus V_{\lambda_2} \oplus \cdots \oplus V_{\lambda_s}$。
5. $n = \dim V_{\lambda_1} + \dim V_{\lambda_2} + \cdots + \dim V_{\lambda_s}$。
6. $\sigma$ 每个特征值的代数重数等于几何重数。

### 注： 条件 4, 5, 6 是最常用的等价条件。

### 推论1.1 可对角化必要条件
若 $n$ 维空间上的线性变换 $\sigma$ 有 $n$ 个不同的特征值，则 $\sigma$ 可对角化。反之，$\sigma$ 可对角化不一定有 $n$ 个特征值。

### 定义1.2 可对角化（矩阵）
设 $A \in \mathbf{F}^{n \times n}$，如果存在可逆矩阵 $P$ 使得 $P^{-1}AP$ 是对角矩阵，则称 $A$ **可对角化**（等价于 $A$ 相似于对角矩阵）。

### 定理1.3 矩阵可对角化条件
设 $A$ 是数域 $\mathbf{F}$ 上的 $n$ 阶矩阵，$\lambda_1, \lambda_2, \ldots, \lambda_s \in \mathbf{F}$ 是 $A$ 的所有互异特征值，则以下条件等价：
1. $A$ 可对角化。
2. $A$ 有 $n$ 个线性无关的特征向量，它们构成 $\mathbf{F}^n$ 的一组基。
3. $n = \dim V_{\lambda_1} + \dim V_{\lambda_2} + \cdots + \dim V_{\lambda_s}$。
4. $A$ 每个特征值的代数重数等于几何重数。

### 推论1.2 矩阵可对角化必要条件
若 $n$ 阶矩阵 $A$ 有 $n$ 个不同的特征值，则 $A$ 可对角化。反之，$A$ 可对角化不一定有 $n$ 个特征值。

### 定理1.4 矩阵多项式与可对角化
设 $A \in \mathbf{F}^{n \times n}$ 可对角化，则对于数域 $\mathbf{F}$ 上任意多项式 $f(x)$，$f(A)$ 也可对角化。若 $A$ 可逆，则 $A^{-1}$ 和 $A^*$ 也可对角化。

### 注： 线性变换版本结论完全一致（除没有伴随矩阵对应的线性映射外）。


## §2 分块对角矩阵

### 定理2.1 核空间扩张性质
设 $\sigma \in \mathcal{L}(V)$，则有
1. $\{0\} = \ker \sigma^0 \subseteq \ker \sigma^1 \subseteq \cdots \subseteq \ker \sigma^k \subseteq \ker \sigma^{k+1} \subseteq \cdots$。
2. 设 $m$ 是非负整数使得 $\ker \sigma^m = \ker \sigma^{m+1}$，则 $\ker \sigma^m = \ker \sigma^{m+1} = \ker \sigma^{m+2} = \cdots$。
3. 令 $n = \dim V$，则 $\ker \sigma^n = \ker \sigma^{n+1} = \cdots$。

### 定理2.2 核空间扩张分解
设 $\sigma \in \mathcal{L}(V)$，$n = \dim V$，则 $V = \ker \sigma^n \oplus \operatorname{im} \sigma^n$。

### 定义2.1 广义特征向量与广义特征子空间
设 $V$ 是 $n$ 维线性空间，$\sigma \in \mathcal{L}(V)$，$\lambda \in \mathbf{F}$ 是 $\sigma$ 的特征值。
- 若向量 $v \neq 0$ 且存在正整数 $j$ 使得 $(\sigma - \lambda I)^j v = 0$，则称 $v$ 为 $\sigma$ 对应于 $\lambda$ 的**广义特征向量**。
- $\sigma$ 对应于 $\lambda$ 的全体广义特征向量与 $0$ 向量构成的集合称为 $\sigma$ 相应于 $\lambda$ 的**广义特征子空间**，记为 $G(\lambda, \sigma)$ 或 $G_\lambda$。

### 注： 对于 $n$ 阶矩阵 $A$，广义特征子空间为 $G_\lambda = \ker (A - \lambda E)^n$。

### 定理2.3 广义特征性质
设 $V$ 是复数域上的 $n$ 维线性空间，$\sigma \in \mathcal{L}(V)$，$\lambda_1, \ldots, \lambda_m$ 表示 $\sigma$ 的所有互异特征值。
1. 每个 $(\sigma - \lambda_j I)|_{G_{\lambda_j}}$ 都是幂零的。
2. 每个 $G_{\lambda_j}$ 在 $\sigma$ 下都是不变的。
3. $\sigma$ 对应于不同特征值的广义特征向量线性无关，故不同特征值对应的广义特征子空间的和为直和。
4. $V = G_{\lambda_1} \oplus \cdots \oplus G_{\lambda_m}$，故 $V$ 有一组由 $\sigma$ 的广义特征向量组成的基。
5. 若 $\lambda \neq \lambda_j$，则 $(\sigma - \lambda I)|_{G_{\lambda_j}}$ 是双射。

### 推论2.1 可对角化的广义特征子空间刻画
线性变换 $\sigma$（或矩阵 $A$）可对角化，当且仅当 $\sigma$（或 $A$）的任意特征值都满足 $G(\lambda, \sigma) = E(\lambda, \sigma)$，即每个特征值对应的广义特征子空间等于特征子空间。


## §3 上三角矩阵

### 定理3.1 上三角矩阵的特征值
设 $A$ 为上三角矩阵，则 $A$ 的特征值恰好就是其主对角元，且在对角线上出现的次数就等于特征值的代数重数。

### 定理3.2 上三角矩阵等价条件
设 $\sigma \in \mathcal{L}(V)$，且 $v_1, v_2, \ldots, v_n$ 是 $V$ 的基，则以下条件等价：
1. $\sigma$ 关于 $v_1, v_2, \ldots, v_n$ 的矩阵是上三角的。
2. 对每个 $j = 1, \ldots, n$ 有 $\sigma(v_j) \in \operatorname{span}(v_1, \ldots, v_j)$。
3. 对每个 $j = 1, \ldots, n$ 有 $\operatorname{span}(v_1, \ldots, v_j)$ 在 $\sigma$ 下不变。

### 定理3.3 上三角矩阵存在性
设 $V$ 是有限维复向量空间，对于任意的 $\sigma \in \mathcal{L}(V)$，一定存在 $V$ 的一组基使得 $\sigma$ 关于该组基有上三角矩阵。

### 注： 等价表述为“任意 $n$ 阶复矩阵一定相似于一个上三角矩阵”。

### 推论3.1 不变子空间的存在性
设 $V$ 是 $n$ 维复向量空间，$\sigma \in \mathcal{L}(V)$，则对任意的正整数 $r \ (1 \le r \le n)$，$\sigma$ 有 $r$ 维不变子空间。

### 推论3.2 不变子空间的升链
设 $V$ 是 $n$ 维复向量空间，$\sigma \in \mathcal{L}(V)$，则存在 $\sigma$ 的不变子空间 $V_0, V_1, \ldots, V_n$ 使得 $V_0 \subset V_1 \subset \cdots \subset V_n$，且 $\dim V_i = i$。

### 定理3.4 分块对角上三角矩阵
设 $V$ 是复向量空间，$\sigma \in \mathcal{L}(V)$，$\lambda_1, \ldots, \lambda_m$ 是 $\sigma$ 的所有互不相同的特征值，重数分别为 $d_1, \ldots, d_m$，则 $V$ 有一组基使得 $\sigma$ 关于这组基的有分块对角矩阵 $\operatorname{diag}(A_1, \ldots, A_m)$，其中每个 $A_j$ 都是 $d_j \times d_j$ 的上三角矩阵，且主对角元全为 $\lambda_j$。

### 定理3.5 线性变换可交换的性质
设 $V$ 为 $n$ 维复向量空间，$\sigma, \tau \in \mathcal{L}(V)$，$\sigma\tau = \tau\sigma$，则
1. $\sigma$ 的每个特征子空间都是 $\tau$ 的不变子空间。
2. $\sigma, \tau$ 有公共的特征向量。

### 定理3.6 同时上三角化
设 $V$ 为 $n$ 维复向量空间，$\sigma, \tau \in \mathcal{L}(V)$，$\sigma\tau = \tau\sigma$，则存在 $V$ 的一组基，使得 $\sigma$ 和 $\tau$ 在这组基下的矩阵均为上三角矩阵。
### 注： 矩阵版本为：设 $A, B$ 是复数域上的两个 $n$ 阶矩阵，且 $AB = BA$，则存在可逆矩阵 $P$ 使得 $P^{-1}AP$ 和 $P^{-1}BP$ 同时为上三角矩阵。


## §4 复数域上相似标准形理论的应用

### 4.1 幂等矩阵的性质
设 $n$ 阶方阵 $A$ 满足 $A^2 = A$（幂等矩阵），则
1. $A$ 是幂等矩阵等价于 $r(A) + r(A - E) = n$。
2. $A$ 为幂等矩阵则一定可对角化，特征值为 $0$ 和 $1$，其中 $1$ 的重数等于 $r(A)$。
3. $A$ 是幂等矩阵时，$r(A) = \operatorname{tr}(A)$。
4. 所有秩为 $1$ 迹也为 $1$ 的矩阵均为幂等矩阵。

### 定理4.1 幂零线性变换的性质
设线性变换 $N \in \mathcal{L}(V)$ 是幂零的，则
1. $N$ 的所有特征值均为 $0$。
2. $N^{\dim V} = 0$。
3. $V$ 有一组基使得 $N$ 关于这组基的矩阵对角线和对角线下方元素均为 $0$。
4. $N \pm I$ 可逆。

### 注： 矩阵版本结论类似。

### 定义4.1 平方根
称线性变换 $\sigma \in \mathcal{L}(V)$ 的**平方根**是满足 $\tau^2 = \sigma$ 的线性变换 $\tau \in \mathcal{L}(V)$。

### 定理4.2 幂零与可逆算子的平方根存在性
设 $V$ 是复向量空间。
1. 设 $N \in \mathcal{L}(V)$ 幂零，则 $(I + N)$ 有平方根。
2. 若 $\sigma \in \mathcal{L}(V)$ 可逆，则 $\sigma$ 有平方根。

### 定义4.2 实线性空间的复化
设 $V$ 是实线性空间，定义 $V$ 的**复化**为 $V_{\mathbf{C}} = V \times V$，其元素 $(u, v)$ 记为 $u + v i$，并定义加法和数乘如下：
- $(u_1 + v_1 i) + (u_2 + v_2 i) = (u_1 + u_2) + (v_1 + v_2)i$
- $(a + bi)(u + vi) = (au - bv) + (av + bu)i$

### 定义4.3 实线性变换的复化
设 $V$ 是实线性空间，$\sigma \in \mathcal{L}(V)$，定义 $\sigma$ 的**复化** $\sigma_{\mathbf{C}} \in \mathcal{L}(V_{\mathbf{C}})$ 为 $\sigma_{\mathbf{C}}(u + vi) = \sigma(u) + \sigma(v)i$。

### 定理4.3 复化空间的维数与矩阵表示
1. 若 $v_1, \ldots, v_n$ 是实线性空间 $V$ 的一组基，那么它也是复线性空间 $V_{\mathbf{C}}$ 的一组基，从而 $\dim V_{\mathbf{C}} = \dim V$。
2. 设 $\sigma \in \mathcal{L}(V)$，若 $A$ 是 $\sigma$ 在某一组基下的矩阵表示，则 $A$ 也是 $\sigma_{\mathbf{C}}$ 在同一组基下的矩阵表示。

### 定理4.4 复化线性变换的特征值与特征向量
设 $V$ 是实线性空间，$\sigma \in \mathcal{L}(V)$，
1. 若 $\lambda \in \mathbf{R}$，则 $\lambda$ 是 $\sigma_{\mathbf{C}}$ 的特征值的充分必要条件是 $\lambda$ 是 $\sigma$ 的特征值。
2. 若 $\lambda = a + b i \ (a, b \in \mathbf{R})$，则 $\lambda$ 是 $\sigma_{\mathbf{C}}$ 的特征值的充分必要条件是存在不全为零的 $\alpha, \beta \in V$ 使得 $\sigma(\alpha) = a\alpha - b\beta,\ \sigma(\beta) = b\alpha + a\beta$。此时 $\alpha + \beta i$ 是 $\sigma_{\mathbf{C}}$ 属于 $\lambda$ 的特征向量。
3. 若 $\lambda = a + b i \in \mathbf{C}$，$\alpha, \beta \in V$，$j$ 为非负整数，那么 $(\sigma_{\mathbf{C}} - \lambda I)^j(\alpha + \beta i) = 0 \iff (\sigma_{\mathbf{C}} - \overline{\lambda} I)^j(\alpha - \beta i) = 0$。特别地，$\lambda$ 是 $\sigma_{\mathbf{C}}$ 的特征值的充分必要条件是 $\overline{\lambda}$ 是 $\sigma_{\mathbf{C}}$ 的特征值。


## 隐含定理与补充说明

### 定理 (隐含) 矩阵可对角化与多项式
若矩阵 $A$ 可对角化，则 $A$ 的多项式 $f(A)$ 也可对角化，且其特征值为 $f(\lambda)$，其中 $\lambda$ 为 $A$ 的特征值。可逆时，$A^{-1}$ 和 $A^*$ 也可对角化。

### 定理 (隐含) 相似标准形的数域无关性
两个实矩阵在实数域上相似的充分必要条件是在复数域上相似。

### 定理 (隐含) 可交换与同时对角化
设 $A, B$ 均可对角化，且 $AB = BA$，则存在同一个可逆矩阵 $P$ 使得 $P^{-1}AP$ 和 $P^{-1}BP$ 同时为对角矩阵。

### 算法框架 (隐含) 对角化求解步骤
1. 求特征多项式 $f(\lambda) = |\lambda E - A|$ 得特征值。
2. 对每个特征值 $\lambda_i$，解齐次线性方程组 $(\lambda_i E - A)X = 0$，得基础解系（特征向量）。
3. 若所有特征子空间的维数之和等于 $n$，则可对角化。将所有线性无关的特征向量按列排列成矩阵 $P$，则 $P^{-1}AP = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)$。

### 算法框架 (隐含) 上三角化求解思路（归纳法）
1. 取矩阵 $A$ 的一个特征值 $\lambda$ 及对应的特征向量 $\alpha_1$。
2. 将 $\alpha_1$ 扩充为 $\mathbf{C}^n$ 的一组基，得到过渡矩阵 $P_1$，使得 $P_1^{-1}AP_1$ 为第一列是 $(\lambda, 0, \ldots, 0)^\mathrm{T}$ 的矩阵。
3. 对右下角的 $n-1$ 阶子矩阵递归进行上三角化。

### 重要公式 (隐含) 幂等矩阵的迹与秩
对于幂等矩阵 $A$，有 $r(A) = \operatorname{tr}(A)$。

### 重要结论 (隐含) 幂零矩阵的迹判定
$A$ 为幂零矩阵当且仅当对任意正整数 $k$，有 $\operatorname{tr}(A^k) = 0$。

---

# 第16章 若当标准形：定义、定理与引理总结

## 1 若当标准形的存在性

### 定义 1.1（若当块）  
域 $\mathbf{F}$ 上的一个 $r$ 级矩阵形如  
\[
J_r(\lambda) = \begin{pmatrix}
\lambda & 1       &        &         \\
        & \lambda & \ddots &         \\
        &         & \ddots & 1       \\
        &         &        & \lambda
\end{pmatrix}
\]  
则称其为一个 **$r$ 级若当块**，记作 $J_r(\lambda)$，其中 $\lambda$ 是对角线上元素。


### 定义 1.2（若当标准形与若当基）  
若一个线性变换 $\sigma$ 在基 $B$ 下的矩阵表示是对角块均为若当块的分块对角矩阵，则称这个分块对角矩阵是线性变换 $\sigma$ 的 **若当标准形**，而这组基 $B$ 称为 $\sigma$ 的 **若当基**。


### 定义 1.3（若当循环基）  
设 $\sigma \in \mathcal{L}(V)$，$v \in V$ 是关于特征值 $\lambda \in \mathbf{C}$ 的一个广义特征向量。设 $n$ 是使得 $(\sigma - \lambda I)^n v = 0$ 成立的最小正整数，则称  
\[
\{(\sigma - \lambda I)^{n-1}(v), (\sigma - \lambda I)^{n-2}(v), \ldots, (\sigma - \lambda I)(v), v\}
\]  
是 **$\sigma$ 关于特征值 $\lambda$ 的循环广义特征向量组**（不引起歧义时也称循环向量），其中 $(\sigma - \lambda I)^{n-1}(v)$ 称为其 **起始向量**，$v$ 称为其 **终止向量**。


### 定理 1.1（若当循环基的性质）  
设 $\sigma \in \mathcal{L}(V)$，$B$ 是 $\sigma$ 关于特征值 $\lambda$ 的循环广义特征向量组，则  
1. $B$ 是线性无关的，因此可以构成 $\operatorname{span}(B)$ 的一组基，称其为一组 **若当循环基**；  
2. $B$ 生成的子空间 $W$ 是 $\sigma$ 的不变子空间（即循环子空间）。


### 引理 1.1（若当循环基合并性质）  
设 $\sigma \in \mathcal{L}(V)$，$\lambda \in \mathbf{C}$ 是 $\sigma$ 的一个特征值。设 $B_1, \ldots, B_q$ 都是 $\sigma$ 关于特征值 $\lambda$ 的若当循环基，且它们的起始向量各不相同且构成一组线性无关向量组，则  
1. $B_i \ (i=1,\ldots,q)$ 互不相交；  
2. $B = B_1 \cup \cdots \cup B_q$ 是线性无关向量组。


### 定理 1.2（广义特征子空间分解若当基）  
设 $V$ 是 $\mathbf{C}$ 上的有限维线性空间，$\sigma \in \mathcal{L}(V)$，$G_\lambda$ 是关于特征值 $\lambda$ 的广义特征子空间，则 $G_\lambda$ 有一组由不相交的若当循环基取并集构成的基。


### 推论 1.1（若当基存在）  
设 $V$ 是 $\mathbf{C}$ 上的有限维线性空间，$\sigma \in \mathcal{L}(V)$，则存在一组基 $B$ 使得 $\sigma$ 在 $B$ 下的矩阵表示为若当标准形。


### 推论 1.2  
对复数域上的任意 $n$ 阶矩阵 $A$，都存在一个 $n$ 阶可逆矩阵 $P$，使得 $P^{-1}AP$ 是若当标准形。

> **注：** 推论 1.1 和 1.2 分别从线性变换和矩阵的角度给出了若当标准形的存在性，且两者等价。


## 2 若当标准形的唯一性

### 引理 1.2（Young图行性质）  
设 $\sigma \in \mathcal{L}(V)$，若 $v \in G_j(\lambda, \sigma) \setminus G_{j-1}(\lambda, \sigma)$，记 $N = \sigma - \lambda I$，则对任意 $i < j$，有  
\[
N^i v \in G_{j-i}(\lambda, \sigma) \setminus G_{j-i-1}(\lambda, \sigma)。
\]


### 定理 1.3（Young图行长度）  
令 $r_j$ 表示 Young 图从上至下第 $j$ 行的格数，$N = \sigma - \lambda I$，则  
1. $r_1 = \dim V - r(N)$；  
2. $r_j = r(N)^{j-1} - r(N)^j \quad (j>1)$。


### 定理 1.4（若当标准形唯一）  
设 $V$ 是 $n$ 维复向量空间，$\sigma \in \mathcal{L}(V)$，$\lambda_1, \ldots, \lambda_m$ 为其互异特征值，记 $N_j = \sigma - \lambda_j I$，则主对角元为 $\lambda_j$ 的若当块个数 $n_j$ 为  
\[
n_j = n - r(N_j),
\]  
其中 $t$ 级若当块 $J_t(\lambda_j)$ 的个数 $n_j(t)$ 为  
\[
n_j(t) = r(N_j^{t+1}) + r(N_j^{t-1}) - 2r(N_j^t)。
\]  
以上公式表明，除若当块的排列次序外，一个线性变换对应的若当标准形唯一。


### 定理 1.5（矩阵若当标准形的唯一性）  
设 $A$ 是 $n$ 阶复矩阵，$\lambda_1, \ldots, \lambda_m$ 为其互异特征值，则主对角元为 $\lambda_j$ 的若当块个数 $n_j$ 为  
\[
n_j = n - r(A - \lambda_j I),
\]  
其中 $t$ 级若当块 $J_t(\lambda_j)$ 的个数 $n_j(t)$ 为  
\[
n_j(t) = r(A - \lambda_j I)^{t+1} + r(A - \lambda_j I)^{t-1} - 2r(A - \lambda_j I)^t。
\]  
以上公式表明，除若当块的排列次序外，一个矩阵对应的若当标准形唯一。

> **注：** 定理 1.4 和 1.5 分别给出了线性变换和矩阵的若当标准形的唯一性判定公式。两矩阵相似的充要条件是它们具有相同的若当标准形（不考虑排列顺序）。


## 3 若当标准形的应用

### 3.1 求解不变子空间

**例题 1.1（若当块的不变子空间）**  
设 $V$ 为 $n$ 维复向量空间，$\sigma \in \mathcal{L}(V)$ 在基 $v_1, \ldots, v_n$ 下的矩阵是一个若当块 $J_n(\lambda)$，则  
1. $V$ 中包含 $v_n$ 的不变子空间只有 $V$ 自身；  
2. $V$ 中任意非零不变子空间都包含 $v_1$；  
3. $V$ 不能分解为两个非平凡不变子空间的直和；  
4. $V$ 中有且仅有 $n+1$ 个不变子空间：  
   $\{0\},\ \operatorname{span}(v_1),\ \operatorname{span}(v_1, v_2),\ \ldots,\ \operatorname{span}(v_1, \ldots, v_n)$。


**例题 1.2（可对角化变换的不变子空间个数）**  
设 $V$ 是复数域上的 $n$ 维线性空间，$\sigma \in \mathcal{L}(V)$ 有 $n$ 个不同的特征值 $\lambda_1, \ldots, \lambda_n$，则 $\sigma$ 的不变子空间个数为 $2^n$。

> **注：** 若 $\sigma$ 有重特征值或为数量变换，则不变子空间个数可能无限。


### 3.2 矩阵求幂与马尔可夫链

**例题 1.3（若当块的 $m$ 次幂）**  
设 $J = J_n(a)$ 是特征值为 $a$ 的 $n$ 阶若当块，则 $J^m$ 的若当标准形为：  
- 当 $a \neq 0$ 时，$J^m \sim J_n(a^m)$；  
- 当 $a = 0$ 时，若 $m \geq n$，则 $J^m = O$；若 $m < n$，设 $n = mq + r \ (0 \leq r < m)$，则 $J^m$ 的若当标准形为  
  $\operatorname{diag}(J_q(0), \ldots, J_q(0), J_{q+1}(0), \ldots, J_{q+1}(0))$，  
  其中 $J_q(0)$ 的个数为 $m-r$，$J_{q+1}(0)$ 的个数为 $r$。


### 3.3 若当标准形与矩阵分解

### 定理 1.6（若当标准形的 $m$ 次根）  
在复数域上：  
1. 若 $a \neq 0$，则存在矩阵 $A$ 使得 $A^m = J_n(a)$；  
2. 当 $n \geq 2$ 时，不存在矩阵 $A$ 使得 $A^m = J_n(0)$。


### 定理 1.7（Jordan-Chevalley 分解）  
设 $A$ 是 $n$ 阶复矩阵，则 $A$ 可分解为 $A = B + C$，其中  
1. $B$ 可对角化；  
2. $C$ 幂零；  
3. $BC = CB$；  
4. $B, C$ 均可表示为 $A$ 的多项式。  
满足条件 1–3 的分解唯一。

> **注：** 证明范式：先证对若当块成立，再证对若当标准形成立，最后利用相似不变性推广到一般矩阵。


### 3.4 求解微分方程
（本节无新增定理，主要利用若当标准形简化常系数线性微分方程组的求解。）


### 3.5 求解线性递推方程

**线性递推方程的通解公式（无重根）**  
对于 $m$ 阶线性递推方程 $a_n = k_1 a_{n-1} + \cdots + k_m a_{n-m}$，若特征方程 $\lambda^m - k_1 \lambda^{m-1} - \cdots - k_m = 0$ 有 $m$ 个互异根 $\lambda_1, \ldots, \lambda_m$，则通解为  
\[
a_n = \sum_{i=1}^m c_i \lambda_i^n。
\]


**线性递推方程的通解公式（有重根）**  
若特征方程有 $m$ 重根 $\lambda_0 \neq 0$，则通解为  
\[
a_n = \sum_{i=1}^m c_i \binom{n}{i-1} \lambda_0^{n-i+1}。
\]

> **注：** 一般情况可通过若当标准形分块求解，每个若当块对应上述形式。


## 4 实数域上的若当标准形

### 定理 1.8（相似域不变性）  
设 $A, B$ 为域 $\mathbf{F}$ 上的同阶方阵，域 $\mathbf{K}$ 是 $\mathbf{F}$ 的扩域，则 $A, B$ 在 $\mathbf{K}$ 上相似当且仅当它们在 $\mathbf{F}$ 上也相似。


### 定理 1.9（实数域上的若当标准形）  
设 $A$ 是 $n$ 阶实矩阵，则 $A$ 在实数域上相似于如下分块对角矩阵之一：  
1. $J = \operatorname{diag}\bigl(J_{r_1}(\lambda_1), \ldots, J_{r_k}(\lambda_k), J_{s_1}(a_1, b_1), \ldots, J_{s_l}(a_l, b_l)\bigr)$；  
2. $\tilde{J} = \operatorname{diag}\bigl(J_{r_1}(\lambda_1), \ldots, J_{r_k}(\lambda_k), \tilde{J}_{s_1}(a_1, b_1), \ldots, \tilde{J}_{s_l}(a_l, b_l)\bigr)$，  
其中 $\lambda_i, a_j, b_j \in \mathbb{R}$，$b_j \neq 0$，$J_{r_i}(\lambda_i)$ 为通常若当块，  
\[
R_j = \begin{pmatrix} a_j & b_j \\ -b_j & a_j \end{pmatrix},\quad
C_2 = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix},
\]  
\[
J_{s_j}(a_j, b_j) = \begin{pmatrix}
R_j & I_2 &        & \\
    & R_j & \ddots & \\
    &     & \ddots & I_2 \\
    &     &        & R_j
\end{pmatrix},\quad
\tilde{J}_{s_j}(a_j, b_j) = \begin{pmatrix}
R_j & C_2 &        & \\
    & R_j & \ddots & \\
    &     & \ddots & C_2 \\
    &     &        & R_j
\end{pmatrix}.
\]

> **注：** 定理 1.9 给出了实数域上矩阵的两种相似的若当标准形，其中 $J_{s_j}(a_j, b_j)$ 和 $\tilde{J}_{s_j}(a_j, b_j)$ 对应于复共轭特征值 $a_j \pm ib_j$ 的实表示。


## 补充说明
1. 若当标准形的求解步骤：  
   - 求特征值 $\lambda_i$ 及广义特征子空间 $G_{\lambda_i}$；  
   - 对每个 $\lambda_i$，计算 $r(A - \lambda_i I)^k$ 以确定若当块的大小与个数；  
   - 通过解线性方程组确定若当基（或过渡矩阵）。
2. 若当标准形是复数域上矩阵相似的完全分类，也是判断两矩阵是否相似的有效工具。
3. 实数域上的若当标准形通过引入 $2 \times 2$ 实块来处理复特征值，保持了实相似性。

**整理说明**  
- 以上内容按章节顺序排列，引理紧随其服务的定理之后。  
- 部分定义与定理在原文中无标签，此处根据内容为其添加了简短描述作为标识。  
- 隐含在例题中的一般性结论（如不变子空间个数、递推方程通解）已作为定理或公式列出。  
- 已逐字检查，确保涵盖讲义中几乎所有形式化的数学结论。

以下是对《多项式的进一步讨论》一章中所有**定义、定理、引理**的系统性总结，按章节顺序排列，引理紧随其服务的定理之后，并补充了隐含的定理和重要说明。已按原文编号或内容添加简短标识，保留原文编号体系（如定理1.1、引理2.1等），新增部分以“*注*”形式标注。

---

# 第17章 多项式的进一步讨论

### **§17.1 特征多项式与 Hamilton-Cayley 定理**

#### **定义 1.1（零化多项式）**
设 $T \in \mathcal{L}(V)$，若 $p \in \mathbf{F}[x]$ 满足 $p(T)=0$，则称 $p$ 为 $T$ 的**零化多项式**。  
对矩阵 $A \in \mathbf{F}^{n \times n}$ 类似定义。

#### **定理 1.1（特征多项式与不变子空间）**
设 $V$ 是复向量空间，$V = V_1 \oplus \cdots \oplus V_m$，且每个 $V_j$ 在 $\sigma \in \mathcal{L}(V)$ 下不变。令 $f_j$ 为 $\sigma|_{V_j}$ 的特征多项式，则 $\sigma$ 的特征多项式为：
\[
f(\lambda) = f_1(\lambda) \cdots f_m(\lambda).
\]

#### **推论 1.1（代数重数等于广义特征空间维数）**
设 $\sigma \in \mathcal{L}(V)$，$\lambda_i$ 为特征值，其代数重数为 $d_i$，则对应的广义特征子空间 $G_{\lambda_i}$ 的维数也为 $d_i$。

#### **定理 1.2（Hamilton-Cayley 定理）**
设 $V$ 是复向量空间，$\sigma \in \mathcal{L}(V)$，$q$ 为其特征多项式，则 $q(\sigma) = 0$。

#### **定理 1.3（实向量空间上的 Hamilton-Cayley 定理）**
设 $V$ 是实向量空间，$\sigma \in \mathcal{L}(V)$，则 $\sigma$ 的特征多项式也是其零化多项式。


### **§17.2 特征多项式与标准形**

#### **引理 2.1（多项式分解与核空间直和）**
设 $\sigma \in \mathcal{L}(V)$，$p = p_1 p_2$，且 $p_1, p_2$ 互素，则：
\[
\ker p(\sigma) = \ker p_1(\sigma) \oplus \ker p_2(\sigma).
\]

#### **推论 2.1（多项式分解与核空间直和）**
设 $\sigma \in \mathcal{L}(V)$，$p = p_1 p_2 \cdots p_s$，且 $p_1, \ldots, p_s$ 两两互素，则：
\[
\ker p(\sigma) = \ker p_1(\sigma) \oplus \cdots \oplus \ker p_s(\sigma).
\]

#### **定理 2.1（特征多项式诱导的广义特征子空间分解）**
设 $\sigma \in \mathcal{L}(V)$，特征多项式为 $f(\lambda) = (\lambda - \lambda_1)^{r_1} \cdots (\lambda - \lambda_m)^{r_m}$，则：
\[
V = \ker (\sigma - \lambda_1 I)^{r_1} \oplus \cdots \oplus \ker (\sigma - \lambda_m I)^{r_m}.
\]
*注：此分解与广义特征子空间分解等价，但幂次可能低于 $\dim V$。*

#### **定理 2.2（循环子空间同构于商空间）**
设 $V$ 是 $\mathbf{C}$ 上的有限维空间，$T \in \mathcal{L}(V)$，$C_{ij}$ 是由循环基 $B_{ij}$ 张成的循环子空间，则：
\[
C_{ij} \cong \mathbf{F}[\lambda] / ((\lambda - \lambda_i)^{r_{ij}}).
\]

#### **定义 2.1（初等因子与初等因子组）**
在循环子空间分解中，多项式 $(\lambda - \lambda_i)^{r_{ij}}$ 称为 $T$ 的一个**初等因子**，所有初等因子构成**初等因子组**。

#### **定理 2.3（初等因子组是相似全系不变量）**
两个矩阵相似当且仅当它们有相同的初等因子组。


### **§17.3 极小多项式及其性质**

#### **定义 3.1（极小多项式）**
设 $\sigma \in \mathcal{L}(V)$，其**极小多项式**是唯一一个次数最小的首一多项式 $p$ 满足 $p(\sigma) = 0$。矩阵类似定义。

#### **定理 3.1（极小多项式存在唯一性）**
设 $V$ 为复（实）向量空间，$\sigma \in \mathcal{L}(V)$，则其极小多项式存在且唯一。

#### **定理 3.2（零化多项式与极小多项式的关系）**
设 $\sigma \in \mathcal{L}(V)$，$q \in \mathbf{F}[x]$，则 $q(\sigma) = 0$ 当且仅当 $q$ 是极小多项式的倍式。

#### **定理 3.3（特征多项式与极小多项式的关系）**
在复数域上，特征多项式是极小多项式的倍式。

#### **定理 3.4（极小多项式与特征多项式有相同根）**
$\sigma$ 的极小多项式的零点恰好是 $\sigma$ 的特征值（重数可能不同）。

#### **定理 3.5（相似矩阵的极小多项式相同）**
相似的矩阵有相同的极小多项式。

#### **定理 3.6（极小多项式诱导的分解）**
设 $\sigma \in \mathcal{L}(V)$，极小多项式为 $p(\lambda) = (\lambda - \lambda_1)^{s_1} \cdots (\lambda - \lambda_m)^{s_m}$，则：
\[
V = \ker (\sigma - \lambda_1 I)^{s_1} \oplus \cdots \oplus \ker (\sigma - \lambda_m I)^{s_m}.
\]

#### **定理 3.7（极小多项式与不变子空间）**
设 $V = U_1 \oplus \cdots \oplus U_m$ 为 $\sigma$ 的不变子空间直和，$\sigma|_{U_i}$ 的极小多项式为 $p_i$，则 $\sigma$ 的极小多项式为：
\[
p = \mathrm{lcm}(p_1, \ldots, p_m).
\]

#### **定理 3.8（极小多项式与可对角化）**
$\sigma$ 可对角化当且仅当其极小多项式可分解为不同一次因式的乘积。

#### **定理 3.9（特征多项式等于极小多项式）**
$T$ 的特征多项式等于极小多项式当且仅当 $V$ 是循环子空间（即存在循环基）。


### **补充定理（隐含于例题或证明中）**

#### **定理 1.4（相似变换保持特征值与重数）**
设 $\sigma, \tau \in \mathcal{L}(V)$ 且 $\tau$ 可逆，则 $\sigma$ 与 $\tau^{-1} \sigma \tau$ 有相同的特征值与重数。

#### **定理 2.4（零化多项式诱导的直和分解）**
设 $\sigma \in \mathcal{L}(V)$，$p(x) = a_n x^n + \cdots + a_1 x$ 是 $\sigma$ 的零化多项式且 $a_1 \neq 0$，则：
\[
V = \ker \sigma \oplus \operatorname{im} \sigma.
\]


### **重要说明与算法**

1. **极小多项式的计算方法**：  
   对于 $m=1,2,\ldots$，解线性方程组：
   \[
   a_0 I + a_1 A + \cdots + a_{m-1} A^{m-1} + A^m = 0,
   \]
   首次有解时，多项式 $a_0 + a_1 \lambda + \cdots + a_{m-1} \lambda^{m-1} + \lambda^m$ 即为极小多项式。

2. **若当标准形的极小多项式**：  
   若 $J$ 的初等因子为 $(\lambda - \lambda_i)^{k_{ij}}$，则极小多项式为：
   \[
   p(\lambda) = (\lambda - \lambda_1)^{k_1} \cdots (\lambda - \lambda_m)^{k_m},
   \]
   其中 $k_i = \max_j k_{ij}$。

3. **可对角化的判定**：  
   除了特征多项式分解为一次因式且几何重数等于代数重数外，**极小多项式无重根**是可对角化的充要条件。

4. **特征多项式与极小多项式的关系**：  
   两者有相同的根，但极小多项式的次数可能更低。若两者相等，则空间为循环空间。


**总结完毕**。已按章节顺序整理所有定义、定理、引理，并补充了隐含结论与重要说明。


以下是对《有理标准形》一章中所有定义、定理、引理、推论等数学结论的系统整理，严格按章节顺序排列，并确保引理紧随其服务的定理之后。文中已标注的以原文标签为准，未标注的依内容补充描述性标识。

---

# 第18章 有理标准形

### 18.1 推广的广义特征子空间与第二有理标准形

### 定义 18.1（广义特征子空间）  
设 \( V \) 是有限维线性空间，\( T \in \mathcal{L}(V) \)。设 \( T \) 的特征多项式为  
\[
f(\lambda) = p_1(\lambda)^{n_1} p_2(\lambda)^{n_2} \cdots p_k(\lambda)^{n_k},
\]  
其中 \( p_i(\lambda) \) 是首一不可约多项式，\( n_i \) 是正整数。对每个 \( p_i(\lambda) \)，定义**广义特征子空间**  
\[
G_{p_i} = \{ v \in V \mid \exists m \in \mathbb{N}^+, (p_i(T))^m v = 0 \},
\]  
\( G_{p_i} \) 中的向量称为**广义特征向量**。


### 定理 18.1（推广的广义特征性质）  
设 \( V \) 是有限维线性空间，\( T \in \mathcal{L}(V) \)，特征多项式分解如上，则：
1. 每个 \( G_{p_i} \) 是 \( T \)-不变子空间；
2. 属于不同 \( p_i \) 的广义特征向量线性无关；
3. \( V = G_{p_1} \oplus G_{p_2} \oplus \cdots \oplus G_{p_k} \)；
4. \( V \) 有一组由 \( T \) 的广义特征向量构成的基。


### 定义 18.2（\( T \)-循环子空间）  
设 \( T \in \mathcal{L}(V) \)，\( v \in V \) 非零，称子空间  
\[
W = \langle v, Tv, T^2v, \ldots \rangle
\]  
为由 \( v \) 生成的 \( T \)-循环子空间，简称循环子空间。


### 定理 18.2（循环子空间的性质）  
设 \( W \) 是由 \( v \) 生成的 \( T \)-循环子空间，则：
1. \( W \) 是 \( T \)-不变子空间；
2. 若 \( \dim W = m \)，则 \( \{v, Tv, \ldots, T^{m-1}v\} \) 是 \( W \) 的一组基。


### 定义 18.3（友阵 / 弗罗贝尼乌斯块）  
设多项式 \( p(\lambda) = \lambda^m + a_{m-1}\lambda^{m-1} + \cdots + a_0 \)，称矩阵  
\[
A = \begin{pmatrix}
0 & 0 & \cdots & 0 & -a_0 \\
1 & 0 & \cdots & 0 & -a_1 \\
0 & 1 & \cdots & 0 & -a_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \cdots & 1 & -a_{m-1}
\end{pmatrix}
\]  
为 \( p(\lambda) \) 的**友阵**，亦称**弗罗贝尼乌斯块**。


### 定义 18.4（弗罗贝尼乌斯标准形 / 有理标准形）  
若分块对角矩阵的每个对角块都是弗罗贝尼乌斯块，则称该矩阵为**弗罗贝尼乌斯标准形**，亦称**有理标准形**。


### 定理 18.3  
若 \( T \) 的极小多项式形如 \( g(\lambda) = (p(\lambda))^m \)，则存在一组基使 \( T \) 的表示矩阵为有理标准形。


### 推论 18.1  
广义特征子空间 \( G_p \) 有一组基，由若干不相交的循环基的并集构成。


### 推论 18.2（第二有理基存在）  
设 \( V \) 是 \( \mathbb{C} \) 上有限维线性空间，\( T \in \mathcal{L}(V) \)，则存在一组基 \( B \) 使 \( T \) 在 \( B \) 下的矩阵为有理标准形。


### 定理 18.4（第二有理标准形的唯一性）  
设 \( T \) 的极小多项式为 \( p(\lambda)^m \)，\( \deg p = d \)，则有理标准形中弗罗贝尼乌斯块的大小由以下公式唯一确定：
1. \( r_1 = \frac{1}{d} (\dim V - \operatorname{rk}(p(T))) \)；
2. \( r_i = \frac{1}{d} (\operatorname{rk}(p(T)^{i-1}) - \operatorname{rk}(p(T)^i)) \)。


### 18.2 不变因子与第一有理标准形

### 定理 18.5（初等因子组合）  
设 \( p_1(\lambda), p_2(\lambda) \in \mathbb{F}[\lambda] \)，循环子空间  
\[
C_1 \cong \mathbb{F}[\lambda]/(p_1(\lambda)), \quad C_2 \cong \mathbb{F}[\lambda]/(p_2(\lambda))
\]  
可直和为新的循环子空间 \( C \cong \mathbb{F}[\lambda]/(p(\lambda)) \) 当且仅当 \( p_1 \) 与 \( p_2 \) 互素，且此时 \( p(\lambda) = p_1(\lambda) p_2(\lambda) \)。


### 推论 18.3（两两互素可合并）  
多个两两互素的多项式对应的循环子空间可直和为一个循环子空间，其生成多项式为这些多项式的乘积。


### 推论 18.4（初等因子分解是最细分解）  
初等因子分解对应的循环子空间分解是“最细”的，即无法再进一步分解为更小循环子空间的直和，除非将互素因子拆分。


### 定义 18.5（不变因子组）  
将 \( T \) 的初等因子按不可约多项式分组，每组按指数降序排列，对齐后逐列相乘得多项式 \( d_1, d_2, \ldots, d_s \)，满足 \( d_i \mid d_{i+1} \)，称为 \( T \) 的**不变因子组**，每个 \( d_i \) 为**不变因子**。


### 定理 18.6  
不变因子组是相似的全系不变量。


### 推论 18.5（第一有理标准形唯一）  
由不变因子组确定的有理标准形（第一有理标准形）是唯一的。


### 18.3 关于相似的最后讨论

### 定理 18.7（矩阵相似的判定）  
设 \( A, B \in \mathbf{M}_n(\mathbb{F}) \)：
1. 若特征多项式不同，则 \( A \) 与 \( B \) 不相似；
2. 若特征多项式相同且均可对角化，则 \( A \) 与 \( B \) 相似；
3. 若特征多项式相同，但一个可对角化另一个不可对角化，则不相似；
4. 若特征多项式相同且均不可对角化，则相似的充要条件是它们有相同的若当标准形（或相同的有理标准形）。


**例 18.1**  
设 \( A, B \in \mathbf{M}_n(\mathbb{F}) \)，若 \( A \) 可逆，则 \( AB \sim BA \)。  
### 证明： \( AB = A(BA)A^{-1} \)，即存在可逆矩阵 \( P = A \) 使 \( P^{-1}(AB)P = BA \)。


**例 18.2**  
判断  
\[
A = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}, \quad
B = \begin{pmatrix} -1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 2 \end{pmatrix}
\]  
是否相似。  
**解**：计算得两者特征多项式均为 \( (\lambda - 1)^2 (\lambda + 1) \)。但 \( A \) 为实对称矩阵，可对角化；而 \( B \) 不可对角化（特征值 1 的几何重数为 1），故不相似。


## 补充说明

1. **有理标准形与若当标准形的关系**  
   有理标准形在任何数域上均存在，而若当标准形仅在代数闭域（如复数域）上存在。在复数域上，有理标准形不退化为若当标准形，二者是独立的标准形体系。

2. **初等因子与不变因子的关系**  
   初等因子是最细的准素多项式分解，不变因子是由初等因子按列组合得到的具有整除链性质的多项式组。两者互相唯一确定，均是相似不变量。

3. **循环子空间的代数结构**  
   循环子空间 \( C_v \) 同构于 \( \mathbb{F}[\lambda]/(p(\lambda)) \)，其中 \( p(\lambda) \) 是 \( v \) 的极小多项式，也是该循环子空间上 \( T \) 的限制算子的特征多项式。

4. **弗罗贝尼乌斯块的特征**  
   弗罗贝尼乌斯块的极小多项式等于其特征多项式，且为友阵形式，便于理论推导与计算。


整理完成，涵盖本章所有形式化数学结论，包括定义、定理、推论、引理及隐含在例题中的一般性结论。

---

# 第19章 内积空间 定义与定理总结

## 19.1 内积和范数

### 19.1.1 内积和范数的定义及性质

### 定义 19.1.1（内积）  
设 $V$ 是 $\mathbf{F}$ 上的线性空间，$V$ 上的**内积**是一个函数 $\langle \cdot, \cdot \rangle: V \times V \to \mathbf{F}$，满足：
1. **正定性**：$\forall v \in V, \langle v, v \rangle \geq 0$，且 $\langle v, v \rangle = 0 \iff v = \vec{0}$；
2. **第一个位置的加性**：$\forall u,v,w \in V, \langle u+v, w \rangle = \langle u, w \rangle + \langle v, w \rangle$；
3. **第一个位置的齐性**：$\forall \lambda \in \mathbf{F}, \forall u,v \in V, \langle \lambda u, v \rangle = \lambda \langle u, v \rangle$；
4. **共轭对称性**：$\forall u,v \in V, \langle u, v \rangle = \overline{\langle v, u \rangle}$。

注：当 $\mathbf{F} = \mathbf{R}$ 时，共轭对称性退化为对称性。

### 定义 19.1.2（内积空间）  
定义了内积的线性空间称为**内积空间**。

### 性质 19.1.1（内积的性质）  
由内积的定义可推出：
1. 对固定的 $u \in V$，映射 $v \mapsto \langle v, u \rangle$ 是线性泛函。
2. $\langle \vec{0}, u \rangle = \langle u, \vec{0} \rangle = 0$。
3. $\langle u, v+w \rangle = \langle u, v \rangle + \langle u, w \rangle$。
4. $\langle u, \lambda v \rangle = \overline{\lambda} \langle u, v \rangle$。

### 定义 19.1.3（范数）  
设 $V$ 是内积空间，$v \in V$，定义 $v$ 的**范数**为 $\|v\| = \sqrt{\langle v, v \rangle}$。

### 性质 19.1.2（范数的性质）  
1. $\|v\| = 0 \iff v = \vec{0}$。
2. $\|\lambda v\| = |\lambda| \|v\|$。

**例 19.1.1（常见内积）**  
1. $\mathbf{F}^n$ 上的欧几里得内积：$\langle (w_1,\ldots,w_n), (z_1,\ldots,z_n) \rangle = w_1\overline{z_1} + \cdots + w_n\overline{z_n}$。
2. $C[-1,1]$ 上的内积：$\langle f, g \rangle = \int_{-1}^1 f(x)g(x) \,\mathrm{d}x$（实函数）。

### 19.1.2 正交的定义与性质

### 定义 19.1.4（正交）  
两个向量 $u,v \in V$ 称为**正交的**，如果 $\langle u, v \rangle = 0$。

### 定义 19.1.5（夹角）  
在实内积空间中，向量 $u,v$ 的夹角 $\theta$ 定义为 $\theta = \arccos \frac{\langle u, v \rangle}{\|u\|\|v\|}$。

### 性质 19.1.3（与零向量正交）  
1. $\vec{0}$ 与任意向量正交。
2. $\vec{0}$ 是唯一与自身正交的向量。

### 定理 19.1.1（勾股定理）  
若 $u,v$ 正交，则 $\|u+v\|^2 = \|u\|^2 + \|v\|^2$。

注：在一般内积空间中，有 $\|u+v\|^2 = \|u\|^2 + \|v\|^2 + \langle u, v \rangle + \langle v, u \rangle = \|u\|^2 + \|v\|^2 + 2\operatorname{Re}\langle u, v \rangle$。

### 定理 19.1.2（正交分解）  
设 $u,v \in V$ 且 $v \neq \vec{0}$，则存在唯一的 $c \in \mathbf{F}$ 和 $w \in V$，使得 $u = cv + w$ 且 $\langle w, v \rangle = 0$。具体地，$c = \frac{\langle u, v \rangle}{\|v\|^2}$，$w = u - \frac{\langle u, v \rangle}{\|v\|^2}v$。

### 定理 19.1.3（Cauchy-Schwarz 不等式）  
设 $u,v \in V$，则 $|\langle u, v \rangle| \leq \|u\|\|v\|$。等号成立当且仅当 $u,v$ 线性相关。

注：证明利用了正交分解。

### 定理 19.1.4（三角不等式）  
设 $u,v \in V$，则 $\|u+v\| \leq \|u\| + \|v\|$。等号成立当且仅当 $u,v$ 之一是另一个的非负标量倍（实内积空间）或其中一个为另一个的标量倍（复内积空间需加条件？）。

注：证明利用了 Cauchy-Schwarz 不等式。

### 定理 19.1.5（平行四边形恒等式）  
设 $u,v \in V$，则 $\|u+v\|^2 + \|u-v\|^2 = 2(\|u\|^2 + \|v\|^2)$。

### 定理 19.1.6（极化恒等式）  
1. 实内积空间：$\langle u, v \rangle = \frac{1}{4}(\|u+v\|^2 - \|u-v\|^2)$。
2. 复内积空间：$\langle u, v \rangle = \frac{1}{4}(\|u+v\|^2 - \|u-v\|^2 + i\|u+iv\|^2 - i\|u-iv\|^2)$。

注：这些恒等式可用于从范数恢复内积。

**例 19.1.2（与算子相关的极化恒等式）**  
设 $T \in \mathcal{L}(V)$，
1. 实内积空间：$\langle Tu, v \rangle + \langle Tv, u \rangle = \frac{1}{2}(\langle T(u+v), u+v \rangle - \langle T(u-v), u-v \rangle)$。
2. 复内积空间：$\langle Tu, v \rangle = \frac{1}{4}(\langle T(u+v), u+v \rangle - \langle T(u-v), u-v \rangle + i\langle T(u+iv), u+iv \rangle - i\langle T(u-iv), u-iv \rangle)$。

注：这些恒等式在证明算子性质时有用。

## 19.2 标准正交基

### 定义 19.2.1（标准正交组）  
向量组 $\{e_1,\ldots,e_m\}$ 称为**标准正交的**，如果 $\langle e_i, e_j \rangle = \delta_{ij}$。

### 定理 19.2.1（勾股定理的推广）  
若 $\{e_1,\ldots,e_m\}$ 是标准正交组，则对任意标量 $a_1,\ldots,a_m$，有 $\|a_1e_1+\cdots+a_me_m\|^2 = |a_1|^2+\cdots+|a_m|^2$。

### 推论 19.2.1  
标准正交组是线性无关的。

### 定义 19.2.2（标准正交基）  
若标准正交组构成一组基，则称为**标准正交基**。

### 定理 19.2.2（Fourier 展开）  
设 $\{e_1,\ldots,e_n\}$ 是 $V$ 的标准正交基，则对任意 $v \in V$，有 $v = \langle v, e_1 \rangle e_1 + \cdots + \langle v, e_n \rangle e_n$，且 $\|v\|^2 = |\langle v, e_1 \rangle|^2 + \cdots + |\langle v, e_n \rangle|^2$。

注：系数 $\langle v, e_j \rangle$ 称为 Fourier 系数。

### 定理 19.2.3（Bessel 不等式）  
设 $\{e_1,\ldots,e_m\}$ 是标准正交组，则对任意 $v \in V$，有 $\sum_{j=1}^m |\langle v, e_j \rangle|^2 \leq \|v\|^2$。等号成立当且仅当 $v \in \operatorname{span}\{e_1,\ldots,e_m\}$。

注：此定理在原文例题中给出。

### 定理 19.2.4（Gram-Schmidt 过程）  
设 $\{v_1,\ldots,v_m\}$ 是线性无关组，可按如下方式构造标准正交组 $\{e_1,\ldots,e_m\}$：
1. 令 $e_1 = \frac{v_1}{\|v_1\|}$。
2. 对 $j=2,\ldots,m$，令 $u_j = v_j - \langle v_j, e_1 \rangle e_1 - \cdots - \langle v_j, e_{j-1} \rangle e_{j-1}$，然后 $e_j = \frac{u_j}{\|u_j\|}$。
且 $\operatorname{span}\{v_1,\ldots,v_j\} = \operatorname{span}\{e_1,\ldots,e_j\}$ 对每个 $j$ 成立。

### 推论 19.2.2  
每个有限维内积空间都有标准正交基。

### 推论 19.2.3  
有限维内积空间中，任何标准正交组都可以扩充为标准正交基。

### 定理 19.2.5（Schur 定理）  
设 $V$ 是有限维复内积空间，$T \in \mathcal{L}(V)$，则 $T$ 关于 $V$ 的某个标准正交基具有上三角矩阵。

注：证明结合了上三角矩阵存在定理和 Gram-Schmidt 过程。

## 19.3 内积的表示方式

### 定理 19.3.1（Riesz 表示定理）  
设 $V$ 是有限维内积空间，$\varphi$ 是 $V$ 上的线性泛函，则存在唯一的 $u \in V$，使得对任意 $v \in V$，有 $\varphi(v) = \langle v, u \rangle$。特别地，若 $\{e_1,\ldots,e_n\}$ 是标准正交基，则 $u = \overline{\varphi(e_1)}e_1 + \cdots + \overline{\varphi(e_n)}e_n$。

### 定义 19.3.1（Gram 矩阵）  
设 $\{e_1,\ldots,e_n\}$ 是 $V$ 的一组基，内积在此基下的 **Gram 矩阵** $G$ 定义为 $G_{ij} = \langle e_i, e_j \rangle$。若 $v = \sum a_i e_i, w = \sum b_i e_i$，则 $\langle v, w \rangle = \alpha G \bar{\beta}^\mathrm{T}$，其中 $\alpha = (a_1,\ldots,a_n), \beta = (b_1,\ldots,b_n)$。

注：在标准正交基下，Gram 矩阵是单位阵。

## 19.4 正交补

### 19.4.1 正交补与正交投影

### 定义 19.4.1（正交补）  
设 $U \subset V$，定义 $U^\perp = \{ v \in V : \forall u \in U, \langle v, u \rangle = 0 \}$。

### 性质 19.4.1（正交补的基本性质）  
1. 对任意子集 $U$，$U^\perp$ 是子空间。
2. $\{\vec{0}\}^\perp = V$。
3. $V^\perp = \{\vec{0}\}$。
4. $U \cap U^\perp \subset \{\vec{0}\}$。
5. 若 $U \subset W$，则 $W^\perp \subset U^\perp$。

### 定理 19.4.1（直和分解）  
设 $U$ 是 $V$ 的有限维子空间，则 $V = U \oplus U^\perp$。

### 推论 19.4.1  
设 $U$ 是有限维内积空间 $V$ 的子空间，则 $\dim U^\perp = \dim V - \dim U$。

### 推论 19.4.2  
设 $U$ 是有限维内积空间 $V$ 的子空间，则 $(U^\perp)^\perp = U$。

### 定义 19.4.2（正交投影）  
设 $U$ 是 $V$ 的有限维子空间，定义**正交投影** $P_U: V \to V$ 为：对 $v = u + w$（$u \in U, w \in U^\perp$），令 $P_U v = u$。

### 性质 19.4.2（正交投影的性质）  
设 $U$ 是有限维子空间，$P_U$ 是正交投影，则：
1. $P_U \in \mathcal{L}(V)$。
2. 对任意 $u \in U$，$P_U u = u$。
3. 对任意 $w \in U^\perp$，$P_U w = \vec{0}$。
4. $\operatorname{im} P_U = U$。
5. $\ker P_U = U^\perp$。
6. $v - P_U v \in U^\perp$。
7. $P_U^2 = P_U$。
8. $\|P_U v\| \leq \|v\|$。
9. 若 $\{e_1,\ldots,e_m\}$ 是 $U$ 的标准正交基，则 $P_U v = \langle v, e_1 \rangle e_1 + \cdots + \langle v, e_m \rangle e_m$。

### 定理 19.4.2（实内积空间中正交投影的对称性）  
在实内积空间中，正交投影 $P_U$ 满足 $\langle P_U u, v \rangle = \langle u, P_U v \rangle$ 对任意 $u,v \in V$ 成立。

注：即 $P_U$ 是自伴算子。

### 19.4.2 极小化问题

### 定理 19.4.3（最佳逼近定理）  
设 $U$ 是 $V$ 的有限维子空间，$v \in V$，则对任意 $u \in U$，有 $\|v - P_U v\| \leq \|v - u\|$，等号成立当且仅当 $u = P_U v$。

**应用：最小二乘解**  
线性方程组 $A\vec{x} = \vec{b}$ 的最小二乘解是使 $\|A\vec{x} - \vec{b}\|$ 最小的解，等价于解正规方程 $A^\mathrm{T} A \vec{x} = A^\mathrm{T} \vec{b}$。

注：这里利用了正交投影到 $A$ 的列空间上。

**关于矩阵的行空间与零空间的关系**  
1. 矩阵的行空间与零空间互为正交补。
2. 矩阵的列空间与其转置矩阵的零空间互为正交补。

注：这提供了行秩等于列秩的另一种解释。

## 习题中出现的定理

**习题 1**  
定义了矩阵的 Frobenius 内积：$\langle A, B \rangle = \operatorname{tr}(AB^\mathrm{T})$（实）或 $\operatorname{tr}(AB^\mathrm{H})$（复）。

**习题 2**  
多项式空间上可定义内积 $\langle f, g \rangle = \sum_{i,j} \frac{a_i b_j}{i+j+1}$。

**习题 3（Bessel 不等式）**  
见定理 19.2.3。

**习题 4**  
关于标准正交基的扰动：若 $\|e_k - v_k\| < \frac{1}{\sqrt{n}}$，则 $\{v_1,\ldots,v_n\}$ 线性无关；但若取等号，则可能线性相关。

**习题 5（Legendre 多项式）**  
多项式空间 $V = \mathbf{R}[x]_{\leq n}$ 在内积 $\langle f, g \rangle = \int_{-1}^1 f(x)g(x) \,\mathrm{d}x$ 下有一组正交基 $P_k(x) = \frac{1}{2^k k!} \frac{\mathrm{d}^k}{\mathrm{d}x^k}(x^2-1)^k$。

**习题 6（Gram 矩阵的性质）**  
1. Gram-Schmidt 过程不改变 Gram 矩阵的行列式。
2. 向量组线性无关当且仅当其 Gram 矩阵可逆。
3. $\det G(u_1,\ldots,u_m) \leq \prod_{i=1}^m \|u_i\|^2$，等号成立当且仅当向量两两正交或某向量为零。
4. Hadamard 不等式：$|\det A|^2 \leq \prod_{j=1}^n \sum_{i=1}^n a_{ij}^2$。

**习题 7（Parseval 不等式）**  
对于连续函数 $f: [-\pi, \pi] \to \mathbf{R}$，定义 Fourier 系数 $a_k, b_k$，则 $\frac{a_0^2}{2} + \sum_{k=1}^\infty (a_k^2 + b_k^2) \leq \frac{1}{\pi} \int_{-\pi}^\pi f^2(x) \,\mathrm{d}x$。

注：这是 Bessel 不等式在函数空间的表现。


**总结说明**  
本章是内积空间的基础，从内积和范数的定义出发，逐步引入正交性、标准正交基、正交补等重要概念。核心定理包括 Cauchy-Schwarz 不等式、勾股定理、正交分解、Riesz 表示定理等，这些定理不仅具有理论价值，也在计算和应用中起到关键作用。Gram-Schmidt 过程提供了构造标准正交基的方法，而正交投影和极小化问题则联系了几何与优化。习题中补充的 Bessel 不等式、Legendre 多项式、Gram 矩阵性质等进一步丰富了内积空间的理论体系。

---

# 第20章 内积空间上的算子 知识点总结

## §1 内积空间的同构

### 1.1 保积同构
### 定义 1.1（保积同构）  
设 \( V \) 和 \( U \) 是数域 \( \mathbf{F} \) 上的两个内积空间，\( S: V \rightarrow U \) 是一个线性映射。若 \( \forall u, v \in V,\ \langle Su, Sv \rangle_U = \langle u, v \rangle_V \)，则称 \( S \) 是一个**保持内积的线性映射**。若 \( S \) 是双射，则称 \( S \) 是一个**保积同构**。

### 定理 1.2（范数保持与内积保持）  
若 \( S : V \rightarrow U \) 是一个保持范数的线性映射，则 \( S \) 保持内积。

### 定理 1.3（保积同构的等价条件）  
设 \( V \) 和 \( U \) 是数域 \( \mathbf{F} \) 上的两个 \( n \) 维内积空间，\( S : V \rightarrow U \) 是一个线性映射，则以下条件等价：
1. \( S \) 保持内积；
2. \( S \) 是保积同构；
3. \( S \) 将 \( V \) 的任一组标准正交基映射到 \( U \) 的一组标准正交基；
4. \( S \) 将 \( V \) 的某一组标准正交基映射到 \( U \) 的一组标准正交基。

### 定理 1.4（内积空间同构的充要条件）  
设 \( V \) 和 \( U \) 是数域 \( \mathbf{F} \) 上的两个内积空间，则二者之间存在保积同构的充分必要条件是它们有相同的维数。

### 1.2 伴随
### 定义 1.5（伴随）  
设 \( T \in \mathcal{L}(V, W) \)，\( T \) 的**伴随** \( T^*: W \rightarrow V \) 满足：\( \forall v \in V, w \in W,\ \langle Tv, w \rangle_W = \langle v, T^*w \rangle_V \)。  
注：伴随映射的定义利用了 Riesz 表示定理，将 \( w \) 对应到唯一的 \( u \)。

### 定理 1.6（伴随的运算性质）  
设 \( S, T \in \mathcal{L}(V, W),\ \lambda \in \mathbf{F} \)，则
1. \( (S + T)^* = S^* + T^* \)；
2. \( (\lambda T)^* = \overline{\lambda} T^* \)；
3. \( (T^*)^* = T \)；
4. 恒等算子 \( I \) 满足 \( I^* = I \)；
5. 若 \( S \in \mathcal{L}(W, U) \)，则 \( (ST)^* = T^* S^* \)。

### 定义 1.7（共轭转置）  
\( m \times n \) 矩阵 \( A = (a_{ij}) \) 的**共轭转置** \( A^{\mathrm{H}} = (\overline{a_{ji}})_{n \times m} \)，即先互换行和列，再对每个元素取复共轭。

### 定理 1.8（伴随的矩阵表示）  
设 \( T \in \mathcal{L}(V, W) \)，\( e_1, \ldots , e_n \) 是 \( V \) 的一组标准正交基，\( f_1, \ldots , f_m \) 是 \( W \) 的一组标准正交基，且 \( T \) 在这两组基下的矩阵为 \( A \)，则 \( T^* \) 在基 \( f_1, \ldots , f_m \) 和 \( e_1, \ldots , e_n \) 下的矩阵为 \( A^{\mathrm{H}} \)。

### 定理 1.9（伴随的核与像）  
设 \( T \in \mathcal{L}(V, W) \)，则
1. \( \ker T^* = (\operatorname{im} T)^{\perp} \)；
2. \( \operatorname{im} T^* = (\ker T)^{\perp} \)；
3. \( \ker T = (\operatorname{im} T^*)^{\perp} \)；
4. \( \operatorname{im} T = (\ker T^*)^{\perp} \)。

### 定理 1.10（伴随与特征值）  
设 \( T \in \mathcal{L}(V),\ \lambda \in \mathbf{F} \)，则 \( \lambda \) 是 \( T \) 的特征值当且仅当 \( \overline{\lambda} \) 是 \( T^* \) 的特征值。

### 定理 1.11（伴随与不变子空间）  
设 \( T \in \mathcal{L}(V) \) 且 \( U \) 是 \( V \) 的子空间，则 \( U \) 在 \( T \) 下不变当且仅当 \( U^{\perp} \) 在 \( T^* \) 下不变。

### 1.3 内积空间的保积自同构
### 定义 1.12（正交变换与酉变换）  
设 \( V \) 是数域 \( \mathbf{F} \) 上的内积空间，\( S \in \mathcal{L}(V) \) 保持内积。若 \( \mathbf{F} = \mathbf{R} \)，则称 \( S \) 是**正交变换**；若 \( \mathbf{F} = \mathbf{C} \)，则称 \( S \) 是**酉变换**。

### 定理 1.13（保积自同构的等价条件）  
设 \( V \) 是数域 \( \mathbf{F} \) 上的内积空间，\( S \in \mathcal{L}(V) \)，则 \( S \) 是正交变换或酉变换等价于 \( S \) 可逆且 \( S^{-1} = S^* \)。

### 定义 1.14（正交矩阵与酉矩阵）  
设 \( A \) 是 \( n \) 阶实方阵，若 \( A^{\mathrm{T}} = A^{-1} \)，则称 \( A \) 是**正交矩阵**；设 \( A \) 是 \( n \) 阶复方阵，若 \( A^{\mathrm{H}} = A^{-1} \)，则称 \( A \) 是**酉矩阵**。

### 定理 1.15（保积自同构的矩阵表示）  
设 \( S \in \mathcal{L}(V) \) 是酉变换（正交变换），则 \( S \) 在 \( V \) 的任一组标准正交基下的表示矩阵是酉矩阵（正交矩阵）。

### 定理 1.16（酉矩阵与标准正交基）  
设 \( A \) 是 \( n \) 阶复矩阵，\( A \) 是酉矩阵当且仅当 \( A \) 的列向量是 \( n \) 维复列向量空间上的一组标准正交基（取标准内积），或者 \( A \) 的行向量是 \( n \) 维复行向量空间上的一组标准正交基（取标准内积）。

### 定理 1.17（正交矩阵与标准正交基）  
设 \( A \) 是 \( n \) 阶实矩阵，\( A \) 是正交矩阵当且仅当 \( A \) 的列向量是 \( n \) 维实列向量空间上的一组标准正交基（取标准内积），或者 \( A \) 的行向量是 \( n \) 维实行向量空间上的一组标准正交基（取标准内积）。

### 定理 1.18（酉矩阵与正交矩阵的特征值）  
设 \( A \) 是 \( n \) 阶酉矩阵或正交矩阵，\( \lambda \) 是 \( A \) 的一个特征值，则 \( \lvert \lambda \rvert = 1 \)。

### 定理 1.19（标准正交基的过渡矩阵）  
设 \( (e_1, \ldots , e_n) \) 是复（实）内积空间 \( V \) 上的标准正交基，\( (f_1, \ldots , f_n) \) 是 \( V \) 上的一组基，从 \( (e_1, \ldots , e_n) \) 到 \( (f_1, \ldots , f_n) \) 的过渡矩阵为 \( A \)，则 \( (f_1, \ldots , f_n) \) 是标准正交基的充要条件是 \( A \) 为酉矩阵（正交矩阵）。

### 定义 1.20（酉相似与正交相似）  
- **酉相似**：复内积空间上，若 \( B = P^{-1}AP = P^{\mathrm{H}}AP \)，则称矩阵 \( A \) 与矩阵 \( B \) 酉相似。
- **正交相似**：实内积空间上，若 \( B = P^{-1}AP = P^{\mathrm{T}}AP \)，则称矩阵 \( A \) 与矩阵 \( B \) 正交相似。


## §2 自伴算子

### 定义 2.1（自伴算子）  
若算子 \( T \in \mathcal{L}(V) \) 满足 \( T = T^* \)，则称 \( T \) 为**自伴算子**。  
注：写成内积形式为 \( \forall v, w \in V,\ \langle Tv, w \rangle = \langle v, Tw \rangle \)。

### 定理 2.2（自伴算子的特征值）  
自伴算子的特征值都是实数。

### 引理 2.3（实谱定理引理1）  
设 \( T \in \mathcal{L}(V) \) 是自伴的，并设 \( b, c \in \mathbf{R} \) 使得 \( b^2 < 4c \)，则 \( T^2 + bT + cI \) 是可逆的。

### 引理 2.4（实谱定理引理2）  
设 \( V \neq \{ \vec{0} \} \) 且 \( T \in \mathcal{L}(V) \) 是自伴算子，则 \( T \) 恒有特征值。  
注：证明中利用 \( v, Tv, \ldots, T^n v \) 线性相关构造多项式，并将实系数多项式分解为一次和二次因子，再转化为算子多项式。

### 引理 2.5（实谱定理引理3）  
设 \( T \in \mathcal{L}(V) \) 是自伴的，并设 \( U \) 是 \( V \) 在 \( T \) 下不变的子空间，则
1. \( U^{\perp} \) 在 \( T \) 下不变；
2. \( T|_U \in \mathcal{L}(U) \) 是自伴的；
3. \( T|_{U^{\perp }} \in \mathcal{L}(U^{\perp }) \) 是自伴的。

### 定理 2.6（实谱定理）  
设 \( \mathbf{F} = \mathbf{R} \) 且 \( T \in \mathcal{L}(V) \)，则以下条件等价：
1. \( T \) 是自伴的；
2. \( V \) 有一个由 \( T \) 的特征向量构成的标准正交基；
3. \( T \) 关于 \( V \) 的某个标准正交基具有对角矩阵。  
注：证明采用数学归纳法，利用引理2.5将空间分解为不变子空间与正交补的直和。


## §3 正规算子

### 定义 3.1（正规算子）  
若算子 \( T \in \mathcal{L}(V) \) 满足 \( TT^* = T^*T \)，则称 \( T \) 为**正规算子**。

### 定义 3.2（正规矩阵）  
正规算子在标准正交基下的表示矩阵称为**正规矩阵**（实：\( AA^{\mathrm{T}} = A^{\mathrm{T}}A \)；复：\( AA^{\mathrm{H}} = A^{\mathrm{H}}A \)）。

### 定理 3.3（正规算子的等价条件）  
算子 \( T \in \mathcal{L}(V) \) 是正规的当且仅当 \( \forall v \in V,\ \lVert Tv \rVert = \lVert T^*v \rVert \)。

### 定理 3.4（正规算子的特征向量）  
设 \( T \in \mathcal{L}(V) \) 是正规的，且 \( v \in V \) 是 \( T \) 相应于特征值 \( \lambda \) 的特征向量，则 \( v \) 也是 \( T^* \) 相应于特征值 \( \overline{\lambda} \) 的特征向量。

### 定理 3.5（正规算子的特征向量正交）  
设 \( T \in \mathcal{L}(V) \) 是正规的，则 \( T \) 的相应于不同特征值的特征向量是正交的。

### 3.1 复正规算子
### 定理 3.6（复谱定理）  
设 \( \mathbf{F} = \mathbf{C} \) 且 \( T \in \mathcal{L}(V) \)，则以下条件等价：
1. \( T \) 是正规的；
2. \( V \) 有一个由 \( T \) 的特征向量构成的标准正交基；
3. \( T \) 关于 \( V \) 的某个标准正交基具有对角矩阵。  
注：证明可利用 Schur 定理，先得到上三角矩阵，再通过范数相等证明其为对角矩阵。

### 定理 3.7（正规算子的自伴性）  
复内积空间上的正规算子是自伴的当且仅当其所有的特征值都是实数。

### 定理 3.8（酉变换的刻画）  
设 \( V \) 是复内积空间，\( S \in \mathcal{L}(V) \)，则以下条件等价：
1. \( S \) 是酉变换；
2. \( V \) 有一个由 \( S \) 的特征向量构成的标准正交基，相应的特征值的绝对值均为 1。

### 3.2 实正规算子
### 定理 3.9（二维实正规算子的刻画）  
设 \( V \) 是二维的实内积空间，\( T \in \mathcal{L}(V) \)，则以下条件等价：
1. \( T \) 是正规的但不是自伴的；
2. \( T \) 关于 \( V \) 的每个标准正交基的矩阵都有 \( \begin{pmatrix} a & -b \\ b & a \end{pmatrix} \) 的形式，其中 \( a, b \in \mathbf{R} \) 且 \( b \neq 0 \)；
3. \( T \) 关于 \( V \) 的某个标准正交基的矩阵有 \( \begin{pmatrix} a & -b \\ b & a \end{pmatrix} \) 的形式，其中 \( a, b \in \mathbf{R} \) 且 \( b > 0 \)。

### 定理 3.10（正规算子的不变子空间）  
设 \( V \) 是内积空间，\( T \in \mathcal{L}(V) \) 是正规的，\( U \) 是 \( V \) 在 \( T \) 下不变的子空间，则
1. \( U^{\perp} \) 在 \( T \) 下不变；
2. \( U \) 在 \( T \) 下不变；
3. \( (T|_U)^* = (T^*|_U) \)；
4. \( T|_U \in \mathcal{L}(U) \) 和 \( T|_{U^{\perp }} \in \mathcal{L}(U^{\perp }) \) 都是正规的。

### 定理 3.11（实正规算子的结构定理）  
设 \( V \) 是实内积空间，\( T \in \mathcal{L}(V) \)，则以下条件等价：
1. \( T \) 是正规的；
2. 存在 \( V \) 的一组标准正交基使得 \( T \) 关于这组基有分块对角矩阵，对角线上的每个块要么是 \( 1 \times 1 \) 矩阵，要么是形如 \( \begin{pmatrix} a & -b \\ b & a \end{pmatrix} \) 的 \( 2 \times 2 \) 矩阵，其中 \( a, b \in \mathbf{R} \) 且 \( b > 0 \)。

### 定理 3.12（正交变换的刻画）  
设 \( V \) 是实内积空间，\( S \in \mathcal{L}(V) \)，则以下条件等价：
1. \( S \) 是正交变换；
2. 存在 \( V \) 的一组标准正交基使得 \( S \) 关于这组基有分块对角矩阵，对角线上的每个块要么是 \( 1 \) 或 \( -1 \) 构成的 \( 1 \times 1 \) 矩阵，要么是形如 \( \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} \) 的 \( 2 \times 2 \) 矩阵，其中 \( \theta \in (0, \pi) \)。


## §4 算子与数的类比、正算子

### 4.1 算子与数的类比
### 定理 4.1（保距自同构和自伴算子的类比）  
设 \( V \) 是复内积空间，\( T \in \mathcal{L}(V) \)，则
1. \( T \) 是保距自同构当且仅当 \( T^*T = TT^* = I \)；
2. \( T \) 是自伴算子当且仅当 \( T = T^* \)。  
注：这类似于复数 \( z \) 是单位复数当且仅当 \( z\bar{z}=1 \)，\( z \) 是实数当且仅当 \( z=\bar{z} \)。

### 定理 4.2（算子的分解）  
设 \( T \) 为复向量空间 \( V \) 上的算子，则 \( T = T_1 + i T_2 \)，其中 \( T_1 = \dfrac{T + T^*}{2} \)，\( i T_2 = \dfrac{T - T^*}{2} \)，并且 \( T^* = T_1 - i T_2 \)。

### 定理 4.3（正规算子的交换条件）  
设 \( T \in \mathcal{L}(V) \)，则 \( T \) 是正规的当且仅当 \( T_1 \) 和 \( T_2 \) 可交换。

### 定理 4.4（复内积空间上的自伴算子刻画）  
设 \( V \) 是复内积空间，\( T \in \mathcal{L}(V) \)，则 \( T \) 是自伴的当且仅当 \( \forall v \in V,\ \langle Tv, v \rangle \in \mathbf{R} \)。

### 定理 4.5（自伴算子的零作用）  
若 \( T \) 是 \( V \) 上的自伴算子，且 \( \forall v \in V,\ \langle Tv, v \rangle = 0 \)，则 \( T = 0 \)。

### 4.2 正算子
### 定义 4.6（正算子）  
设算子 \( T \in \mathcal{L}(V) \)，如果 \( T \) 是自伴的且 \( \forall v \in V \) 均有 \( \langle Tv, v \rangle \geqslant 0 \)，则称 \( T \) 为**正算子**。

### 定理 4.7（复内积空间上的正算子）  
设 \( V \) 为复向量空间，\( T \in \mathcal{L}(V) \)，若 \( \forall v \in V,\ \langle Tv, v \rangle \geqslant 0 \)，则 \( T \) 是自伴算子。

### 定义 4.8（平方根）  
算子 \( R \) 被称为算子 \( T \) 的**平方根**，如果 \( R^{2} = T \)。

### 定理 4.9（正算子的刻画）  
设 \( T \in \mathcal{L}(V) \)，则以下条件等价：
1. \( T \) 是正的；
2. \( T \) 是自伴的且 \( T \) 的所有特征值非负；
3. \( T \) 有正的平方根；
4. \( T \) 有自伴的平方根；
5. 存在算子 \( R \in \mathcal{L}(V) \) 使得 \( T = R^{*}R \)。

### 定理 4.10（正平方根的唯一性）  
\( V \) 上每个正算子都有唯一的正平方根。  
注：将正算子 \( T \) 的唯一正平方根记作 \( \sqrt{T} \)。


## 补充定理（来自例题与习题）

### 定理 4.11（镜像变换）  
设 \( e \) 是欧式空间中的一个单位向量，定义线性变换 \( \varphi(x) = x - 2\langle e, x \rangle e \)，则 \( \varphi \) 是正交变换且 \( \det \varphi = -1 \)，称为**镜像变换**。  
注：旋转变换可由两个镜像变换合成，因此正交变换可分解为不超过 \( n \) 个镜像变换的乘积（Cartan–Dieudonné 定理）。

### 定理 4.12（矩阵的 QR 分解）  
任一 \( n \) 级可逆复矩阵 \( A \) 一定可被唯一分解成 \( A = PB \)，其中 \( P \) 是 \( n \) 级酉矩阵，\( B \) 是主对角元均为正实数的 \( n \) 级上三角矩阵。

### 定理 4.13（正规算子的交换性）  
设 \( V \) 是有限维复内积空间，\( S, T \in \mathcal{L}(V) \) 均为正规算子，且 \( ST = TS \)，则
1. 存在一组标准正交基使得 \( S \) 和 \( T \) 的矩阵都是对角矩阵；
2. \( S \) 与 \( T \) 的复合也是正规算子。

### 定理 4.14（离散傅里叶变换是酉变换）  
定义在 \( \mathbb{C}^n \) 上的离散傅里叶变换 \( \mathcal{F} \) 是酉变换，且满足 \( \mathcal{F}^4 = I \)。


### 注： 本章主要研究了内积空间上几类重要算子（保积自同构、自伴算子、正规算子、正算子）的结构与性质，核心结果是实谱定理与复谱定理，它们分别给出了实自伴算子和复正规算子可正交对角化的充要条件。通过伴随运算，可将算子与复数类比，从而更深入地理解各类算子的特征。

---

# 第21章 奇异值分解：定义与定理索引

## 第一章 奇异值分解

### 定理1.1（T*T的性质）
设 $ T \in \mathcal{L}(V, W) $，则
1. $ T^*T $ 是正算子。
2. $ \ker T^*T = \ker T $。
3. $ \operatorname{im} T^*T = \operatorname{im} T^* $。
4. $ \dim \operatorname{im} T = \dim \operatorname{im} T^* = \dim \operatorname{im} T^*T $。

注：该定理建立了 $T^*T$ 与 $T$ 的核心关系，是奇异值分解的理论基础。

### 定义1.1（奇异值）
设 $ T \in \mathcal{L}(V, W) $，则 $ T^*T $ 的特征值的算术平方根称为 $ T $ 的奇异值，按降序排列，每个奇异值重复 $ \dim E(\lambda, T^*T) $ 次。

注：奇异值总是非负实数，因为 $T^*T$ 是正算子。

### 定理1.2（奇异值与单射满射的关系）
设 $ T \in \mathcal{L}(V, W) $，则
1. $ T $ 是单射等价于 $ 0 $ 不是 $ T $ 的奇异值。
2. $ T $ 的正奇异值的个数等于 $ \dim \operatorname{im} T $。
3. $ T $ 是满射等价于 $ T $ 的正奇异值的个数等于 $ \dim W $。

注：证明利用定理1.1和单射满射的等价条件。该定理将算子的基本性质与奇异值联系起来。

### 定义1.2（奇异向量）
设 $ T \in \mathcal{L}(V, W) $，奇异值为 $ s $，若存在 $ v \in V, w \in W $ 使得 $ Tv = sw $，$ T^*w = sv $，则称 $ v $ 为 $ T $ 关于 $ s $ 的左奇异向量，$ w $ 为 $ T $ 关于 $ s $ 的右奇异向量。

注：左奇异向量是 $T^*T$ 的特征向量，右奇异向量是 $TT^*$ 的特征向量。

### 定理1.3（奇异值分解）
设 $ T \in \mathcal{L}(V, W) $ 有正奇异值 $ s_1, \ldots , s_m $。则存在 $ V $ 的一组标准正交组 $ e_1, \ldots, e_m $ 和 $ W $ 的标准正交组 $ f_1, \ldots, f_m $ 使得 $ \forall v \in V $ 均有
\[
Tv = s_1 \langle v, e_1 \rangle f_1 + \cdots + s_m \langle v, e_m \rangle f_m.
\]

**证明框架**：
1. 对正算子 $T^*T$ 应用谱定理，得到 $V$ 的标准正交基 $e_1, \ldots, e_n$ 满足 $T^*T e_k = s_k^2 e_k$。
2. 对正奇异值部分，定义 $f_k = \frac{1}{s_k} T e_k$，验证其为 $W$ 的标准正交组。
3. 对零奇异值部分，利用 $\ker T^*T = \ker T$ 得 $T e_k = 0$。
4. 将任意 $v \in V$ 按基展开即得结论。

注：奇异值分解本质上是将一般线性映射表示为“旋转-拉伸-旋转”的形式，使用两组不同的基。

### 定义1.3（矩形对角矩阵）
设 $ A = (a_{ij})_{m \times n} $，则称 $ A $ 为矩形对角矩阵，若 $ a_{ij} = 0 $ 当 $ i \neq j $ 时。

注：奇异值分解中的矩阵 $\Sigma$ 即为矩形对角矩阵，其对角线元素为奇异值。

### 定理1.4（矩阵形式的奇异值分解）
设 $ A $ 为一 $ m \times n $ 阶矩阵，则 $ A $ 的奇异值分解为 $ A = U\Sigma V^* $，其中 $ U $ 为 $ m \times m $ 阶酉矩阵，$ V $ 为 $ n \times n $ 阶酉矩阵，$ \Sigma $ 为 $ m \times n $ 阶非负实数矩形对角矩阵。

注：这是定理1.3在矩阵语言下的表述，广泛应用于数值计算和数据分析。


## 第二章 奇异值分解的应用

### 定理2.1（极分解定理）
设 $ T \in \mathcal{L}(V) $，则存在一个等距同构 $ S \in \mathcal{L}(V) $，使得 $ T = S\sqrt{T^*T} $。

**证明框架**：
1. 定义线性映射 $S_1: \operatorname{im} \sqrt{T^*T} \rightarrow \operatorname{im} T$ 为 $S_1(\sqrt{T^*T}v) = Tv$，验证其为良定义的等距映射。
2. 将 $S_1$ 扩张到整个空间：取 $(\operatorname{im} \sqrt{T^*T})^\perp$ 和 $(\operatorname{im} T)^\perp$ 的标准正交基，定义 $S_2$ 为这两组基之间的等距映射。
3. 定义 $S = S_1 \oplus S_2$，验证 $S$ 为等距同构且满足 $T = S\sqrt{T^*T}$。

注：极分解将任意算子分解为等距同构与正算子的乘积，类比于复数的极坐标形式。

### 定理2.2（特征人脸算法中的奇异值分解应用）
设 $A \in \mathbb{R}^{m \times n}$ 为中心化后的人脸数据矩阵，其奇异值分解为 $A = U\Sigma V^T$，则：
1. $U$ 的列向量是 $AA^T$ 的特征向量。
2. $V$ 的列向量是 $A^T A$ 的特征向量。
3. 若 $u_i$ 是 $AA^T$ 的特征向量（对应特征值 $\lambda_i$），则 $A^T u_i$ 是 $A^T A$ 的特征向量（对应同一特征值 $\lambda_i$）。
4. 前 $k$ 个主要特征向量可通过 $(v_1, \ldots, v_k) = A^T (u_1, \ldots, u_k)$ 计算。

**隐含算法框架**：
1. 对 $A$ 进行奇异值分解（或直接对 $AA^T$ 进行特征值分解）。
2. 选取前 $k$ 个最大奇异值对应的左奇异向量 $u_1, \ldots, u_k$。
3. 计算 $v_i = A^T u_i$（归一化后）作为投影基。
4. 将人脸数据投影到由 $v_1, \ldots, v_k$ 张成的低维子空间。

注：该算法利用奇异值分解将 $O(n^3)$ 的协方差矩阵特征分解转化为 $O(m^3)$ 的矩阵特征分解（通常 $m \ll n$），大幅减少计算量。


## 补充说明

1. **谱定理的应用**：奇异值分解的证明依赖于对正算子 $T^*T$ 应用谱定理，这是将自伴算子理论推广到一般线性映射的关键桥梁。
2. **数学归纳法框架**：在证明涉及标准正交基构造的定理时（如谱定理、奇异值分解），常采用数学归纳法：先选取一个特征向量作为基向量的起点，再考虑其正交补空间。
3. **线性映射基本定理**：在极分解定理的证明中，利用 $\dim \operatorname{im} \sqrt{T^*T} = \dim \operatorname{im} T$ 来保证扩张映射 $S_2$ 的存在性，这是线性映射基本定理的典型应用。
4. **正交补空间的性质**：在多个证明中（如极分解定理），通过构造正交补空间的标准正交基并定义等距映射，展示了 Hilbert 空间结构的完整性。

**检查完毕**：以上整理涵盖了讲义中所有显式和隐含的定义、定理、引理，按章节顺序排列，引理紧随对应定理之后，补充了证明框架和注意事项，无遗漏。

---

# 第22章 线性代数与几何

## 22.1 欧氏空间上的运算

### 定义 1.1（点积）  
在三维欧氏空间中，两个向量 $\vec{a}$ 和 $\vec{b}$ 的点积定义为：
\[
\vec{a} \cdot \vec{b} = |\vec{a}| |\vec{b}| \cos \theta
\]
其中 $\theta$ 为两向量的夹角。在坐标形式下，$(a_1, a_2, a_3) \cdot (b_1, b_2, b_3) = a_1 b_1 + a_2 b_2 + a_3 b_3$。

### 定义 1.2（叉乘）  
在三维欧氏空间中，两个向量 $\vec{a}$ 和 $\vec{b}$ 的叉乘是一个向量，记为 $\vec{a} \times \vec{b}$，其方向垂直于 $\vec{a}$ 和 $\vec{b}$ 且满足右手定则，模长为 $|\vec{a}| |\vec{b}| \sin \theta$。坐标计算可用行列式：
\[
(a_1, a_2, a_3) \times (b_1, b_2, b_3) =
\begin{vmatrix}
\vec{i} & \vec{j} & \vec{k} \\
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3
\end{vmatrix}
\]

### 定义 1.3（混合积）  
三个向量 $\vec{a}, \vec{b}, \vec{c}$ 的混合积定义为 $(\vec{a} \times \vec{b}) \cdot \vec{c}$，记为 $[\vec{a}, \vec{b}, \vec{c}]$。几何上表示以这三个向量为邻边的平行六面体的体积。坐标计算为：
\[
[(a_1, a_2, a_3), (b_1, b_2, b_3), (c_1, c_2, c_3)] =
\begin{vmatrix}
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3 \\
c_1 & c_2 & c_3
\end{vmatrix}
\]
混合积满足轮换对称性：$[\vec{a}, \vec{b}, \vec{c}] = [\vec{b}, \vec{c}, \vec{a}] = [\vec{c}, \vec{a}, \vec{b}]$。

### 性质 1.1  
混合积为零当且仅当三个向量共面。

**补充定理 1.1**  
对于任意三个向量 $\vec{a}, \vec{b}, \vec{c}$，有 $(\vec{a} \times \vec{b}) \cdot \vec{c} = \vec{a} \cdot (\vec{b} \times \vec{c})$。

## 22.2 点、直线、平面的表示

### 22.2.1 平面的方程

### 定义 2.1（平面的一般方程）  
平面的一般方程为 $Ax + By + Cz + D = 0$，其中 $(A, B, C)$ 是平面的一个法向量。

### 定义 2.2（平面的参数方程）  
已知平面上一点 $P(x_0, y_0, z_0)$ 和两个不共线的向量 $\vec{u} = (a, b, c)$，$\vec{v} = (d, e, f)$，则平面的参数方程为：
\[
\begin{cases}
x = x_0 + k_1 a + k_2 d \\
y = y_0 + k_1 b + k_2 e \\
z = z_0 + k_1 c + k_2 f
\end{cases}
\]
其中 $k_1, k_2$ 为参数。

### 定义 2.3（平面的点法式）  
已知平面上一点 $P(x_0, y_0, z_0)$ 和法向量 $\vec{n} = (A, B, C)$，则平面的点法式方程为：
\[
A(x - x_0) + B(y - y_0) + C(z - z_0) = 0
\]

### 性质 2.1  
平面的一般方程与点法式可以相互转化，一般方程中的系数 $(A, B, C)$ 即为法向量。

**补充定理 2.1**  
已知平面上不共线的三点 $A(x_1, y_1, z_1)$, $B(x_2, y_2, z_2)$, $C(x_3, y_3, z_3)$，则平面方程为：
\[
\begin{vmatrix}
x - x_1 & y - y_1 & z - z_1 \\
x_2 - x_1 & y_2 - y_1 & z_2 - z_1 \\
x_3 - x_1 & y_3 - y_1 & z_3 - z_1
\end{vmatrix} = 0
\]
或等价地，混合积 $[\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AP}] = 0$，其中 $P(x, y, z)$ 为平面上任意点。

### 22.2.2 直线的方程

### 定义 2.4（直线的一般方程）  
直线可表示为两个相交平面的交线：
\[
\begin{cases}
A_1 x + B_1 y + C_1 z + D_1 = 0 \\
A_2 x + B_2 y + C_2 z + D_2 = 0
\end{cases}
\]

### 定义 2.5（直线的点向式）  
已知直线上一点 $A_0(x_0, y_0, z_0)$ 和方向向量 $\vec{l} = (a, b, c)$，则直线的点向式方程为：
\[
\frac{x - x_0}{a} = \frac{y - y_0}{b} = \frac{z - z_0}{c}
\]
要求 $a, b, c$ 均不为零。

### 定义 2.6（直线的参数方程）  
由点向式引入参数 $t$，得到直线的参数方程：
\[
\begin{cases}
x = x_0 + a t \\
y = y_0 + b t \\
z = z_0 + c t
\end{cases}
\]

### 定义 2.7（直线的两点式）  
已知直线上两点 $A(x_1, y_1, z_1)$ 和 $B(x_2, y_2, z_2)$，则直线的两点式方程为：
\[
\frac{x - x_1}{x_2 - x_1} = \frac{y - y_1}{y_2 - y_1} = \frac{z - z_1}{z_2 - z_1}
\]

### 性质 2.2  
从直线的一般方程转化为点向式或参数方程：取两平面法向量的叉乘作为直线的方向向量，再求一般方程的一个特解作为直线上一点。

**补充定理 2.2**  
已知直线的一般方程，其方向向量 $\vec{l} = \vec{n}_1 \times \vec{n}_2$，其中 $\vec{n}_1 = (A_1, B_1, C_1)$，$\vec{n}_2 = (A_2, B_2, C_2)$ 为两平面的法向量。

## 22.3 平面与直线间的位置关系

### 22.3.1 线与线的位置关系

### 定理 3.1  
设两条直线的方向向量分别为 $\vec{l}_1$ 和 $\vec{l}_2$。
1. 若 $\vec{l}_1 \parallel \vec{l}_2$，则两条直线平行或重合。进一步，若两条直线有公共点，则重合；否则平行。
2. 若 $\vec{l}_1 \nparallel \vec{l}_2$，则两条直线可能相交或异面。联立两直线方程，若有唯一解，则相交；若无解，则异面。

**补充定理 3.1**  
两条直线共面的充要条件是混合积 $[\overrightarrow{AB}, \vec{l}_1, \vec{l}_2] = 0$，其中 $A$ 是直线 $L_1$ 上一点，$B$ 是直线 $L_2$ 上一点。

### 22.3.2 线与面的位置关系

### 定理 3.2  
设直线的方向向量为 $\vec{l}$，平面的法向量为 $\vec{n}$。
1. 若 $\vec{l} \parallel \vec{n}$，则直线与平面垂直。
2. 若 $\vec{l} \perp \vec{n}$，则直线与平面平行或在平面内。进一步，若直线上一点在平面内，则直线在平面内；否则直线与平面平行。

**补充定理 3.2**  
直线与平面平行的充要条件是 $\vec{l} \cdot \vec{n} = 0$，且直线上一点不在平面内。

### 22.3.3 面与面的位置关系

### 定理 3.3  
设两个平面的法向量分别为 $\vec{n}_1$ 和 $\vec{n}_2$。
1. 若 $\vec{n}_1 \parallel \vec{n}_2$，则两个平面平行或重合。进一步，若两个平面有公共点，则重合；否则平行。
2. 若 $\vec{n}_1 \perp \vec{n}_2$，则两个平面垂直。

### 22.3.4 平面与点的位置关系

### 定理 3.4（点到平面的距离公式）  
点 $P(x_0, y_0, z_0)$ 到平面 $Ax + By + Cz + D = 0$ 的距离为：
\[
d = \frac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2 + B^2 + C^2}}
\]

### 定理 3.5（球面方程）  
球心为 $\vec{a}$，半径为 $r$ 的球面方程为：
\[
\langle \vec{x} - \vec{a}, \vec{x} - \vec{a} \rangle = r^2
\]

### 定理 3.6（球与平面相切的条件）  
球 $\langle \vec{x}, \vec{x} \rangle = r^2$ 与平面 $\langle \vec{n}, \vec{x} \rangle = -D$ 在点 $\vec{t}$ 处相切的充要条件是：
1. $\langle \vec{t}, \vec{t} \rangle = r^2$ 且 $\langle \vec{n}, \vec{t} \rangle = -D$；
2. 存在 $\lambda \in \mathbb{R}$ 使得 $\vec{t} = \lambda \vec{n}$。

### 引理 3.1  
平面到原点的距离公式为 $d_{O\text{-}\Gamma} = \frac{|D|}{\sqrt{A^2 + B^2 + C^2}}$。  
注：此引理用于推导点到平面的距离公式。

## 22.4 仿射变换

### 定义 4.1（仿射变换）  
一个映射 $F: \mathbb{R}^n \to \mathbb{R}^m$ 称为仿射变换，如果它保持共线性和定比分点性质。

### 定理 4.1  
任意仿射变换 $F: \mathbb{R}^n \to \mathbb{R}^m$ 都可以表示为 $F(u) = A u + v$ 的形式，其中 $A$ 是一个 $m \times n$ 矩阵，$v \in \mathbb{R}^m$。

### 引理 4.1  
仿射变换可以表示为线性变换与平移的复合。

**证明框架**  
通过平移将零点映射为零点，然后利用共线性和定比分点性质证明映射的线性性。

### 注： 仿射变换在齐次坐标下可以表示为线性变换。具体地，$F(u) = A u + v$ 对应齐次坐标下的线性变换：
\[
\begin{pmatrix}A & v \\0 & 1\end{pmatrix}\begin{pmatrix}u \\ 1\end{pmatrix}=\begin{pmatrix}A u + v \\ 1\end{pmatrix}
\]

## 22.5 射影空间

### 定义 5.1（射影空间）  
$n$ 维实射影空间 $\mathbf{PR}^n$ 是 $\mathbb{R}^{n+1}$ 中所有非零向量在等价关系 $x \sim y \iff \exists k \in \mathbb{R}, x = k y$ 下的等价类的集合。

### 引理 5.1  
$\mathbf{PR}^{n-1}$ 可以自然地嵌入到 $\mathbf{PR}^n$ 中，嵌入映射为 $[x] \mapsto [(x, 0)]$。

### 定理 5.1  
$\mathbf{PR}^n$ 可以分解为 $\mathbb{R}^{n-1}$ 和 $\mathbf{PR}^{n-1}$ 的无交并。具体地，$\mathbf{PR}^n = \{ [(x, 1)] : x \in \mathbb{R}^{n-1} \} \cup \{ [(x, 0)] : x \in \mathbb{R}^{n-1} \setminus \{0\} \}$，其中后者同构于 $\mathbf{PR}^{n-1}$。

### 定理 5.2  
一个仿射变换 $F: \mathbb{R}^n \to \mathbb{R}^m$ 可以诱导出一个射影空间之间的映射 $\tilde{F}: \mathbf{PR}^n \to \mathbf{PR}^m$，且满足 $\tilde{F}$ 在子空间 $\mathbf{PR}^{n-1}$ 上的限制。

### 注： 射影空间引入了“无穷远点”的概念，使得仿射变换可以在射影空间中被线性化。

## 22.6 曲面上的标架

### 定义 6.1（切平面）  
设曲面 $S$ 的参数方程为 $\vec{r}(u, v) = (x(u, v), y(u, v), z(u, v))$，在点 $\vec{r}_0 = \vec{r}(u_0, v_0)$ 处，切向量 $\vec{t}_u = \frac{\partial \vec{r}}{\partial u}$ 和 $\vec{t}_v = \frac{\partial \vec{r}}{\partial v}$ 张成的平面称为曲面在 $\vec{r}_0$ 处的切平面，记为 $T_{\vec{r}_0} S$。

### 定义 6.2（法向量）  
切平面的单位法向量称为曲面在该点处的法向量，记为 $\vec{n}$。

### 定义 6.3（第一基本形式）  
曲面 $S$ 的第一基本形式为：
\[
\mathrm{d} s^2 = E \mathrm{d} u^2 + 2 F \mathrm{d} u \mathrm{d} v + G \mathrm{d} v^2
\]
其中
\[
E = \vec{t}_u \cdot \vec{t}_u, \quad F = \vec{t}_u \cdot \vec{t}_v, \quad G = \vec{t}_v \cdot \vec{t}_v
\]

### 定理 6.1  
第一基本形式在参数变换下的变换规律。设参数变换为 $(\tilde{u}, \tilde{v}) = (\tilde{u}(u, v), \tilde{v}(u, v))$，则新旧第一基本形式的系数矩阵满足：
\[
\begin{pmatrix}
\tilde{E} & \tilde{F} \\
\tilde{F} & \tilde{G}
\end{pmatrix}
= J^\mathrm{T}
\begin{pmatrix}
E & F \\
F & G
\end{pmatrix} J
\]
其中 $J$ 为 Jacobi 矩阵：
\[
J = \begin{pmatrix}
\frac{\partial u}{\partial \tilde{u}} & \frac{\partial u}{\partial \tilde{v}} \\
\frac{\partial v}{\partial \tilde{u}} & \frac{\partial v}{\partial \tilde{v}}
\end{pmatrix}
\]

### 引理 6.1  
第一基本形式是正定的，即 $E > 0, G > 0, EG - F^2 > 0$。

### 证明
由 $\vec{t}_u$ 和 $\vec{t}_v$ 线性无关，所以它们的点积矩阵是正定的。

## 22.7 二次曲面及其分类

### 定义 7.1（二次曲面）  
二次曲面的一般方程为：
\[
a x^2 + b y^2 + c z^2 + 2 d y z + 2 e x z + 2 f x y + g x + h y + i z = 1
\]
或写成矩阵形式：
\[
\begin{pmatrix}
x & y & z
\end{pmatrix}
\begin{pmatrix}
a & f & e \\
f & b & d \\
e & d & c
\end{pmatrix}
\begin{pmatrix}
x \\ y \\ z
\end{pmatrix}
+
\begin{pmatrix}
g & h & i
\end{pmatrix}
\begin{pmatrix}
x \\ y \\ z
\end{pmatrix} = 1
\]

### 定理 7.1（二次曲面的标准化）  
任意二次曲面可以通过等距变换（旋转和平移）化为如下形式：
\[
a x^2 + b y^2 + c z^2 = d
\]
其中 $a, b, c$ 是二次型矩阵的特征值。

**证明框架**  
1. 通过正交变换（旋转）消去交叉项，得到 $a x^2 + b y^2 + c z^2 + g x + h y + i z = 1$。
2. 通过配方法（平移）消去一次项，得到标准形式。

**补充定理 7.1**  
二次曲面的类型由特征值的符号和 $d$ 的符号决定。具体分类包括椭球面、单叶双曲面、双叶双曲面、椭圆抛物面、双曲抛物面、锥面、柱面等。

**补充定理 7.2（二次曲线的分类）**  
平面二次曲线 $A x^2 + B y^2 + C x y + D x + E y + F = 0$ 可通过旋转和平移化为标准形式，其类型由二次型矩阵的特征值符号和常数项决定。

## 总结

本章从线性代数的角度介绍了解析几何的基本概念，包括向量的点积、叉乘、混合积，点、直线、平面的表示方法，以及它们之间的位置关系。随后介绍了仿射变换和射影空间的概念，最后讨论了曲面上的标架和二次曲面的分类。

关键点：
1. 向量的运算（点积、叉乘、混合积）及其几何意义。
2. 点、直线、平面的多种表示方法及相互转化。
3. 点、直线、平面之间的位置关系判定。
4. 仿射变换的定义和表示。
5. 射影空间的构造和性质。
6. 曲面的切平面、法向量和第一基本形式。
7. 二次曲面的分类方法。

注：本章内容与线性代数紧密联系，许多几何问题可以转化为代数问题，例如通过向量运算判断位置关系，通过矩阵变换对二次曲面进行分类等。

---

# 第23章 二次型：定义与定理索引

## 第一章 二次型的定义

### 定义1.1（二次型）
$n$个元$x_1,x_2,\ldots,x_n$的二次齐次多项式
\[
f(x_1,x_2,\ldots,x_n)=\sum_{i=1}^{n}a_{ii}x_i^2+\sum\limits_{1\leqslant i<j\leqslant n}2a_{ij}x_ix_j
\]
称为域$\mathbf{F}$上的$n$元二次型。

注：二次型总可以表示为$f(X)=X^\mathrm{T}AX$的形式，其中$A$为对称矩阵。对称矩阵与二次型之间存在一一对应关系。

### 定理1.1（二次型矩阵表示的唯一性）
设$f(X)=X^\mathrm{T}AX$和$g(X)=X^\mathrm{T}BX$为两个二次型，若对任意$X\in\mathbf{R}^n$都有$f(X)=g(X)$，则$A=B$。

注：该定理保证了对称矩阵作为二次型表示的唯一性，是二次型理论的基础。

### 定理1.2（反对称矩阵的刻画）
设$A$为$n$阶矩阵，则$A$为反对称矩阵当且仅当对任意$n$元列向量$X$都有$X^\mathrm{T}AX=0$。

注：这是例题1.2中蕴含的一般性定理，给出了反对称矩阵的一个等价刻画。


## 第二章 矩阵相合的定义与性质

### 定义2.1（矩阵相合）
称$n$阶矩阵$A$相合于$B$（记作$A\simeq B$），如果存在可逆矩阵$C$使得$B=C^\mathrm{T}AC$。

注：矩阵相合是等价关系，要求$C$可逆。相合关系与数域有关。

### 定理2.1（矩阵相合的基本性质）
矩阵相合具有以下性质：
1. 合同是等价关系；
2. 若$A\simeq B$且$A,B$可逆，则$A^{-1}\simeq B^{-1}$；
3. 若$A_1\simeq A_2,\ B_1\simeq B_2$，则$\begin{pmatrix} A_1 & O \\ O & B_1 \end{pmatrix}\simeq\begin{pmatrix} A_2 & O \\ O & B_2 \end{pmatrix}$；
4. $A\simeq B$当且仅当$A$可以通过成对的初等行列变换变为$B$。

注：矩阵相合与矩阵相似、相抵是不同的等价关系，对于实对称矩阵，相合与相似有特殊联系。

### 定理2.2（实对称矩阵的相合性质）
设$A,B$为$n$阶实对称矩阵且$A\simeq B$，则：
1. $A^m\simeq B^m$对任意正整数$m$成立；
2. 若$A$可逆，则$A^{-1}\simeq B^{-1}$。

注：这是定理2.1的补充，针对实对称矩阵的特殊情况。


## 第三章 二次型标准形的定义与求解

### 引理3.1（初等变换与合同变换）
对称矩阵$A$的下列变换都是相合变换：
1. 对换$A$的第$i$行与第$j$行，再对换第$i$列与第$j$列；
2. 将非零数$k$乘以$A$的第$i$行，再将$k$乘以$A$的第$i$列；
3. 将$A$的第$i$行乘以$k$加到第$j$行，再将$A$的第$i$列乘以$k$加到第$j$列。

注：该引理提供了通过初等变换实现合同变换的具体操作，是初等变换法求标准形的理论基础。

### 引理3.2（非零对称矩阵的合同变换）
设$A$是域$\mathbf{F}$上的非零对称矩阵，则必定存在可逆矩阵$C$使得$C^\mathrm{T}AC$的第$(1,1)$个元素不为$0$。

**证明框架**：
1. 若$a_{11}\neq 0$，取$C=E$即可；
2. 若$a_{11}=0$但存在$a_{ii}\neq 0$，则通过对换第1行（列）与第$i$行（列）使得$a_{11}\neq 0$；
3. 若所有$a_{ii}=0$，则存在$a_{ij}\neq 0(i\neq j)$，将第$j$行（列）加到第$i$行（列），再按情况2处理。

注：该引理保证了任何非零对称矩阵都可以通过合同变换使其左上角元素非零，为归纳法证明二次型可对角化奠定基础。

### 定理3.1（对称矩阵的合同对角化）
设$A$是域$\mathbf{F}$上的$n$阶对称矩阵，则必存在$\mathbf{F}$上的$n$阶可逆矩阵$C$，使得$C^\mathrm{T}AC$为对角矩阵。

**证明框架**（数学归纳法）：
1. 当$n=1$时显然成立；
2. 假设对$n-1$阶对称矩阵结论成立；
3. 由引理3.2，不妨设$a_{11}\neq 0$，通过行变换和对应的列变换将第1行和第1列的其他元素消为$0$；
4. 对右下角的$n-1$阶对称矩阵应用归纳假设；
5. 构造分块对角矩阵得到最终的对角化矩阵。

注：该定理是二次型标准形存在性的核心定理，提供了配方法、初等变换法和正交变换法的理论依据。

### 定理3.2（配方法的有效性）
任意$n$元二次型$f(X)$总可以通过可逆线性替换$X=CY$化为平方和形式（标准形）。

### 算法 框架（配方法）：
1. 若存在平方项$x_i^2$，则将所有含$x_i$的项配方；
2. 若不存在平方项但存在交叉项$x_ix_j$，则先作可逆线性替换$y_i=x_i+x_j,\ y_j=x_i-x_j$产生平方项；
3. 对新变量重复步骤1直至化为平方和。

注：配方法是求解二次型标准形的常用方法，特别适合手工计算。例题3.1和3.2展示了该方法的具体应用。

### 定理3.3（正交变换法）
设$f(X)=X^\mathrm{T}AX$为$n$元实二次型，$A$为实对称矩阵，则存在正交矩阵$P$使得$P^\mathrm{T}AP=\mathrm{diag}(\lambda_1,\ldots,\lambda_n)$，其中$\lambda_i$为$A$的特征值。

### 算法 框架：
1. 求$A$的特征值$\lambda_1,\ldots,\lambda_n$；
2. 对每个特征值求相应的特征向量；
3. 将特征向量标准正交化得正交矩阵$P$；
4. 作正交变换$X=PY$即得标准形$f(Y)=\lambda_1y_1^2+\cdots+\lambda_ny_n^2$。

注：正交变换法得到的标准形系数为特征值，是二次型在正交变换下的最简形式。该方法在物理和工程中应用广泛。


## 第四章 相合规范形 惯性定理

### 定义4.1（相合规范形）
设$A$为$n$阶实对称矩阵，则$A$相合于对角矩阵$\mathrm{diag}(1,\ldots,1,-1,\ldots,-1,0,\ldots,0)$，称为$A$的相合规范形。

注：相合规范形中$1$的个数称为正惯性指数，$-1$的个数称为负惯性指数，$0$的个数为$n-r$（$r$为$A$的秩）。

### 定理4.1（惯性定理）
实对称矩阵的相合规范形唯一，即正负惯性指数在合同变换下不变。

**证明框架**（反证法）：
1. 假设二次型$f$通过两种可逆线性替换得到规范形，正惯性指数分别为$p$和$k$，且$p>k$；
2. 构造齐次线性方程组，利用变量个数多于方程个数得到非零解；
3. 在该解下，由第一种规范形计算得$f>0$，由第二种规范形计算得$f\leq 0$，矛盾；
4. 同理$k>p$也不可能，故$p=k$。

注：惯性定理是二次型理论的基石，揭示了合同变换下的不变量，为二次型分类提供依据。

### 推论4.1（实二次型分类）
$n$元实二次型按正负惯性指数$(p,q)$分类，共有$\frac{(n+1)(n+2)}{2}$个等价类。

注：该推论由惯性定理直接得到，说明实对称矩阵的合同类由正负惯性指数完全决定。

### 定理4.2（复二次型的标准形）
任意$n$元复二次型$f(X)$必可经可逆复线性替换化为规范形$y_1^2+\cdots+y_r^2$，其中$r$为$f$的秩。

### 算法 框架：
1. 将$f$化为标准形$d_1x_1^2+\cdots+d_rx_r^2$；
2. 令$y_i=\sqrt{d_i}x_i$（取复数平方根）；
3. 规范形为$y_1^2+\cdots+y_r^2$。

注：复二次型的规范形完全由秩决定，比实二次型简单。这与复数域上每个非零数都有平方根有关。


## 第五章 正定二次型和正定矩阵

### 定义5.1（正定、半正定等二次型）
设$f(X)=X^\mathrm{T}AX$为$n$元实二次型：
1. 若$\forall X\neq 0$有$f(X)>0$，则称$f$为正定二次型，$A$为正定矩阵；
2. 若$\forall X\neq 0$有$f(X)\geq 0$，则称$f$为半正定二次型，$A$为半正定矩阵；
3. 若$\forall X\neq 0$有$f(X)<0$，则称$f$为负定二次型，$A$为负定矩阵；
4. 若$\forall X\neq 0$有$f(X)\leq 0$，则称$f$为半负定二次型，$A$为半负定矩阵；
5. 若存在$X_1,X_2$使$f(X_1)>0$且$f(X_2)<0$，则称$f$为不定二次型。

注：负定、半负定可通过乘以$-1$化为正定、半正定问题研究，故重点研究正定与半正定。

### 定理5.1（正定、半正定的惯性指数刻画）
设$f(X)=X^\mathrm{T}AX$为$n$元实二次型，$r$为$A$的秩，$p$为正惯性指数，则：
1. $f$正定当且仅当$p=n$（即$r=n$且规范形全为$1$）；
2. $f$半正定当且仅当$p=r$（即规范形无$-1$）。

注：该定理将正定、半正定的定义与惯性指数联系起来，是正定矩阵判定的基本定理。

### 推论5.1（正定矩阵的合同标准形）
$n$阶实对称矩阵$A$正定当且仅当$A\simeq E_n$；半正定当且仅当$A\simeq\begin{pmatrix} E_r & O \\ O & O \end{pmatrix}$。

### 定理5.2（正定矩阵的顺序主子式判定）
$n$阶实对称矩阵$A$正定的充分必要条件是$A$的所有顺序主子式大于$0$。

**证明框架**（必要性）：
1. 若$A$正定，则其任意$k$阶顺序主子阵对应的$k$元二次型也正定；
2. 由正定矩阵合同于单位阵知该主子阵行列式大于$0$。

（充分性）数学归纳法，利用顺序主子式大于$0$可保证配方法每一步都可进行。

注：该定理提供了判断矩阵正定性的实用方法，特别适合数值计算。

### 推论5.2（正定矩阵的性质）
若$A$正定，则：
1. $A$的任一$k$阶主子阵正定；
2. $A$的所有主子式为正；
3. $A$的主对角元全大于$0$；
4. $A$的特征值全大于$0$；
5. $\det(A)>0$。

### 定理5.3（正定矩阵的特征值刻画）
$n$阶实对称矩阵$A$正定当且仅当其所有特征值为正。

注：该定理可由正交变换法或正定矩阵的分解$A=C^\mathrm{T}C$（$C$可逆）证明。

### 引理5.1（正定矩阵的分解引理）
设$A$为$n$阶实对称矩阵，则$A$正定当且仅当存在$n$阶可逆矩阵$C$使得$A=C^\mathrm{T}C$。

注：该引理是正定矩阵Cholesky分解的基础，也揭示了正定矩阵与内积的密切联系。

### 定理5.4（Cholesky分解）
正定矩阵$A$存在唯一分解$A=LL^\mathrm{T}$，其中$L$为对角元全正的下三角矩阵。

### 算法 框架：
1. 设$L=(l_{ij})$为下三角矩阵，$l_{ij}=0\ (i<j)$；
2. 由$A=LL^\mathrm{T}$逐行求解$L$的元素：
   \[
   l_{ii}=\sqrt{a_{ii}-\sum_{k=1}^{i-1}l_{ik}^2},\quad
   l_{ij}=\frac{1}{l_{jj}}\left(a_{ij}-\sum_{k=1}^{j-1}l_{ik}l_{jk}\right)\ (i>j)
   \]
3. 由正定性保证根号内为正。

注：Cholesky分解是求解对称正定线性方程组的高效方法，计算量约为$LU$分解的一半。

### 定理5.5（半正定矩阵的等价条件）
设$A$为$n$阶实对称矩阵，则以下等价：
1. $A$半正定；
2. $A$的各阶主子式非负（顺序主子式非负）；
3. 存在矩阵$C$使$A=C^\mathrm{T}C$（$C$可能不可逆）；
4. $A$的所有特征值非负；
5. 存在对角元非负的下三角矩阵$L$使$A=LL^\mathrm{T}$。

注：半正定矩阵的判定条件比正定矩阵弱，但仍有完整的刻画。

### 定理5.6（半正定矩阵与内积）
任意$n$阶半正定矩阵$A$可在$\mathbf{R}^n$上定义内积$\langle X,Y\rangle = X^\mathrm{T}AY$。反之，任何内积的Gram矩阵半正定。

注：该定理揭示了半正定矩阵与内积空间的本质联系，是欧氏空间理论的矩阵表述。


## 第六章 标准形的应用

### 定理6.1（矩阵的幂等分解）
任意$n$阶方阵$A$可分解为可逆矩阵$B$与幂等矩阵$C$的乘积，即$A=BC$。

**证明框架**：
1. 设$r=r(A)$，存在可逆矩阵$P,Q$使$PAQ=\begin{pmatrix} E_r & O \\ O & O \end{pmatrix}$；
2. 令$B=P^{-1}$，$C=\begin{pmatrix} E_r & O \\ O & O \end{pmatrix}Q^{-1}$；
3. 验证$C^2=C$（幂等）且$A=BC$。

注：该定理是例题6.1的一般化，提供了矩阵分解的一种方式。

### 定理6.2（幂等矩阵的分解刻画）
秩为$r$的$n$阶幂等矩阵$A$等价于存在列满秩矩阵$B\in\mathbf{R}^{n\times r}$和行满秩矩阵$C\in\mathbf{R}^{r\times n}$使得$A=BC$且$CB=E_r$。

**证明框架**：
1. 必要性：由$A^2=A$知$A$的特征值为0或1，可构造$B,C$；
2. 充分性：直接验证$(BC)^2=BC$。

注：该定理给出了幂等矩阵的结构分解，在投影算子理论中有重要应用。

### 定理6.3（实对称矩阵的乘积分解）
秩为$r$的$n$阶实对称矩阵$A$可表示为$n-r$个秩为$n-1$的实对称矩阵的乘积。

**证明框架**：
1. 由正交相似对角化，设$A=Q\mathrm{diag}(\lambda_1,\ldots,\lambda_r,0,\ldots,0)Q^\mathrm{T}$；
2. 将每个零特征值替换为小量$\varepsilon_i$，构造$A_i=Q\mathrm{diag}(\lambda_1,\ldots,\lambda_r,0,\ldots,\varepsilon_i,\ldots,0)Q^\mathrm{T}$；
3. 令$\varepsilon_i\to 0$取极限，并利用连续性论证。

注：该定理是例题6.2的推广，展示了实对称矩阵的精细结构。


## 补充定理与性质

### 定理S1（二次型的秩不变性）
二次型$f(X)=X^\mathrm{T}AX$的秩在可逆线性替换下不变，等于其相伴矩阵$A$的秩。

注：该性质隐含在二次型的定义和矩阵相合的性质中，是惯性定理的基础。

### 定理S2（正定矩阵的运算性质）
正定矩阵具有以下性质：
1. 若$A,B$正定，则$A+B$正定；
2. 若$A$正定，则$A^{-1}$正定；
3. 若$A$正定，$C$可逆，则$C^\mathrm{T}AC$正定。

注：这些性质由正定矩阵的定义直接可得，在优化理论和数值分析中常用。

### 定理S3（半正定矩阵的运算性质）
半正定矩阵具有以下性质：
1. 若$A,B$半正定，则$A+B$半正定；
2. 若$A$半正定，$C$为任意矩阵，则$C^\mathrm{T}AC$半正定；
3. 若$A$半正定，则存在唯一的半正定矩阵$B$使$B^2=A$（记为$\sqrt{A}$）。

注：半正定矩阵的平方根在概率统计（协方差矩阵）和泛函分析中有重要应用。

### 算法框架S1（初等变换法求标准形及变换矩阵）
设$A$为$n$阶对称矩阵：
1. 构造$2n\times n$矩阵$\begin{pmatrix} A \\ E \end{pmatrix}$；
2. 对$A$进行成对的行列初等变换，目标将$A$化为对角阵$\Lambda$；
3. 对单位矩阵$E$只进行相同的列变换，得到变换矩阵$C$；
4. 最终有$\begin{pmatrix} \Lambda \\ C \end{pmatrix}$，且$C^\mathrm{T}AC=\Lambda$。

注：该算法是例题3.1的总结，提供了同时求标准形和变换矩阵的系统方法。

**检查完毕**：以上整理涵盖了讲义中所有显式和隐含的定义、定理、引理，按章节顺序排列，引理紧随对应定理之后，补充了证明框架、算法和注意事项，无遗漏。特别注意了例题中蕴含的一般性定理，如反对称矩阵的刻画、幂等矩阵的分解等，并将其提升为正式定理。

---

# 第24章 多重线性映射与张量的计算

## 24.1 多重线性映射

### 定义 1.1（多重线性映射）  
设 \( V_1, V_2, \ldots, V_n, W \) 均为线性空间，映射 \( f: V_1 \times V_2 \times \cdots \times V_n \to W \) 称为**多重线性映射**，如果对每个分量都是线性的，即
\[
f(v_1, \ldots, \lambda v_i + \mu v_i', \ldots, v_n) = \lambda f(v_1, \ldots, v_i, \ldots, v_n) + \mu f(v_1, \ldots, v_i', \ldots, v_n)
\]
对任意 \( \lambda, \mu \) 成立。记所有这样的多重线性映射的集合为 \( \mathcal{L}(V_1, V_2, \cdots, V_n; W) \)。当 \( W = \mathbf{F} \) 时，称为**多重线性函数**。

### 注： 多重线性映射与积空间上的线性映射不同：多重线性映射要求对每个分量单独线性，而积空间上的线性映射要求对整个向量线性。

### 定义 1.2（多重线性映射的矩阵表示）  
设 \( f \in \mathcal{L}(V_1, V_2; W) \)，\( V_1 \) 的基为 \( \{e_1, \ldots, e_n\} \)，定义 \( f_i(v_2) = f(e_i, v_2) \)，则 \( f_i \) 是 \( V_2 \to W \) 的线性映射，设其矩阵为 \( M_i \)。对于 \( v_1 = \sum \lambda_i e_i \)，有
\[
f(v_1, v_2) = (\lambda_1 M_1 + \cdots + \lambda_n M_n) v_2
\]
形式地记作
\[
f(v_1, v_2) = v_1^\mathrm{T} \begin{pmatrix} M_1 \\ \vdots \\ M_n \end{pmatrix} v_2
\]
右侧为形式记号，非标准矩阵乘法。

### 注： 此表示可推广到 n 元情形，对应 n+1 阶张量。

## 24.2 张量积

### 引理 2.1（多重线性函数与线性映射的同构）  
\[
\mathcal{L}(V, W^*; \R) \cong \mathcal{L}(V, W)
\]
**证明思路**：利用 \( W^{**} \cong W \)，将多重线性函数转化为线性映射。

### 定义 2.1（张量积）  
定义 \( V_1 \otimes V_2 = \mathcal{L}(V_1^*, V_2^*; \R) \cong \mathcal{L}(V_1^*, V_2) \)，称为 \( V_1 \) 与 \( V_2 \) 的**张量积**。

### 引理 2.2（张量积的结合律）  
\[
(V_1 \otimes V_2) \otimes V_3 \cong \mathcal{L}(V_1^*, V_2^*, V_3^*; \R) \cong V_1 \otimes (V_2 \otimes V_3)
\]
因此张量积运算可结合，记作 \( V_1 \otimes V_2 \otimes V_3 \)。

### 推论 2.1（张量积的维数）  
\[
\dim (V_1 \otimes V_2 \otimes \cdots \otimes V_n) = \prod_{i=1}^n \dim V_i
\]

### 引理 2.3（张量积映射的满性）  
映射 \( \otimes: V_1^* \times V_2^* \to \mathcal{L}(V_1, V_2; \R) \) 定义为 \( (f, g) \mapsto f \otimes g \)，其中 \( (f \otimes g)(v_1, v_2) = f(v_1) g(v_2) \)。该映射是满的，但不是单的。

### 引理 2.4（张量积核的刻画）  
\[
\ker \otimes = \{ (f, g) \mid \forall v_1, v_2, f(v_1)g(v_2)=0 \}
\]

### 引理 2.5（张量积核的另一种刻画）  
\[
\ker \otimes = \operatorname{span}\{ (f,0), (0, g) \}
\]

### 定理 2.1（张量积的商空间定义）  
\[
V_1 \otimes V_2 \cong (V_1 \times V_2) / \ker \otimes
\]
其中等价关系由 \( \otimes \) 的核定义。

### 定理 2.2（张量积的基）  
若 \( \{e_i\} \) 是 \( V_1 \) 的基，\( \{f_j\} \) 是 \( V_2 \) 的基，则 \( \{ e_i \otimes f_j \} \) 是 \( V_1 \otimes V_2 \) 的一组基。

### 定理 2.3（张量积的泛性质）  
设 \( \pi: V_1 \times V_2 \to V_1 \otimes V_2 \) 为典范投影。对任意向量空间 \( U \) 及双线性映射 \( \varphi: V_1 \times V_2 \to U \)，存在唯一的线性映射 \( \tilde{\varphi}: V_1 \otimes V_2 \to U \) 使得下图交换：
\[
\begin{CD}
V_1 \times V_2 @>\pi>> V_1 \otimes V_2 \\
@V\varphi VV @VV\tilde{\varphi} V \\
U @= U
\end{CD}
\]

## 24.3 张量的坐标变换

**约定 3.1（Einstein 求和约定）**  
上下成对出现的指标为哑指标，表示求和。例如 \( a^i x_i = \sum_i a^i x_i \)。

### 定义 3.1（反变张量）  
设 \( V \) 为线性空间，\( T \in V^{\otimes n} = \overbrace{V \otimes \cdots \otimes V}^{n} \)，称 \( T \) 为 **n 阶反变张量**。

### 定义 3.2（(r,s) 型张量）  
设 \( V \) 为线性空间，定义
\[
V_s^r = \overbrace{V \otimes \cdots \otimes V}^{r} \otimes \overbrace{V^* \otimes \cdots \otimes V^*}^{s}
\]
其中的元素称为 **(r,s) 型张量**，即 r 阶反变、s 阶共变。

### 定理 3.1（张量的坐标变换公式）  
设 \( V \) 有两组基 \( \{e_i\} \) 和 \( \{\tilde{e}_i\} \)，过渡矩阵为 \( M \)，即 \( \tilde{e}_i = M_i^j e_j \)（Einstein 求和）。设 \( T \) 为 (r,s) 型张量，在两组基下的坐标分别为 \( T_{j_1\cdots j_s}^{i_1\cdots i_r} \) 和 \( \tilde{T}_{j_1\cdots j_s}^{i_1\cdots i_r} \)，则变换公式为
\[
\tilde{T}_{j_1\cdots j_s}^{i_1\cdots i_r} = T_{l_1\cdots l_s}^{k_1\cdots k_r} \, (M^{-1})_{k_1}^{i_1} \cdots (M^{-1})_{k_r}^{i_r} \, M_{j_1}^{l_1} \cdots M_{j_s}^{l_s}
\]
其中 Einstein 求和约定适用于所有哑指标。

### 注： 当 \( r=1, s=1 \) 时，张量为矩阵，变换公式退化为 \( \tilde{A} = M^{-1} A M \)，即相似变换。

## 24.4 张量的运算

### 定义 4.1（张量积运算）  
设 \( T \in V_{s_1}^{r_1}, S \in V_{s_2}^{r_2} \)，定义张量积 \( T \otimes S \in V_{s_1+s_2}^{r_1+r_2} \) 为
\[
(T \otimes S)(v_1,\ldots,v_{r_1+r_2}, \omega_1,\ldots,\omega_{s_1+s_2}) = T(v_1,\ldots,v_{r_1},\omega_1,\ldots,\omega_{s_1}) \cdot S(v_{r_1+1},\ldots,v_{r_1+r_2},\omega_{s_1+1},\ldots,\omega_{s_1+s_2})
\]
在坐标下，分量为对应乘积：
\[
(T \otimes S)_{j_1\cdots j_{s_1+s_2}}^{i_1\cdots i_{r_1+r_2}} = T_{j_1\cdots j_{s_1}}^{i_1\cdots i_{r_1}} \cdot S_{j_{s_1+1}\cdots j_{s_1+s_2}}^{i_{r_1+1}\cdots i_{r_1+r_2}}
\]

### 定义 4.2（张量的缩并）  
设 \( T \) 为 (r,s) 型张量，选定反变指标位置 \( k \) 和共变指标位置 \( l \)（\( 1 \le k \le r, 1 \le l \le s \)），缩并运算 \( \mathrm{ct}_{(k,l)}: V_s^r \to V_{s-1}^{r-1} \) 定义为：在坐标表示中对第 \( k \) 个上标和第 \( l \) 个下标求和，并去掉这两个指标。即
\[
(\mathrm{ct}_{(k,l)} T)_{j_1\cdots j_{l-1} j_{l+1}\cdots j_s}^{i_1\cdots i_{k-1} i_{k+1}\cdots i_r} = T_{j_1\cdots j_{l-1} m j_{l+1}\cdots j_s}^{i_1\cdots i_{k-1} m i_{k+1}\cdots i_r}
\]
其中 \( m \) 为求和哑指标。

### 注： 矩阵作为 (1,1) 型张量，其缩并为迹：\( \mathrm{ct}_{(1,1)} A = A_i^i = \sum_i A_i^i = \operatorname{tr}(A) \)。

## 24.5 张量代数和外代数

### 定义 5.1（张量代数）  
设 \( V \) 为线性空间，定义
\[
\mathcal{T}(V) = \bigoplus_{r,s=0}^{\infty} V_s^r
\]
其中只有有限项非零，配备张量积运算，构成一个代数，称为 **张量代数**。

### 定义 5.2（对称张量与反称张量）  
设 \( T \) 为 r 阶共变张量（即 \( T \in V_r = V_r^0 \)）。
- \( T \) 称为**对称张量**，如果对任意指标位置交换，分量不变：
  \[
  T_{i_1\cdots i_k\cdots i_l\cdots i_r} = T_{i_1\cdots i_l\cdots i_k\cdots i_r}
  \]
- \( T \) 称为**反称张量**（或交错张量），如果对任意指标位置交换，分量反号：
  \[
  T_{i_1\cdots i_k\cdots i_l\cdots i_r} = -T_{i_1\cdots i_l\cdots i_k\cdots i_r}
  \]
对称张量子空间记作 \( \bigodot^r V \)，反称张量子空间记作 \( \bigwedge^r V \)。

### 引理 5.1（对称与反称张量的基与维数）  
设 \( \dim V = n \)，取 \( V \) 的一组基 \( \{e_i\} \)，则
- \( \bigodot^r V \) 的一组基为 \( \{ e_{i_1} \otimes \cdots \otimes e_{i_r} \mid 1 \le i_1 \le i_2 \le \cdots \le i_r \le n \} \)，维数为 \( \binom{n+r-1}{r} \)。
- \( \bigwedge^r V \) 的一组基为 \( \{ e_{i_1} \otimes \cdots \otimes e_{i_r} \mid 1 \le i_1 < i_2 < \cdots < i_r \le n \} \)，维数为 \( \binom{n}{r} \)。

### 推论 5.1（张量的对称-反称分解）  
任意 r 阶张量可唯一分解为对称部分与反称部分之和。即存在投影算子：
\[
\mathcal{S}_r(T) = \frac{1}{r!} \sum_{\sigma \in S_r} \sigma T, \quad \mathcal{A}_r(T) = \frac{1}{r!} \sum_{\sigma \in S_r} \operatorname{sgn}(\sigma) \cdot \sigma T
\]
满足 \( T = \mathcal{S}_r(T) + \mathcal{A}_r(T) \)，且 \( \mathcal{S}_r(T) \) 对称，\( \mathcal{A}_r(T) \) 反称。

### 定义 5.3（对称积与外积）  
设 \( T \in \bigodot^r V, S \in \bigodot^s V \)，定义**对称积** \( T \odot S = \mathcal{S}_{r+s}(T \otimes S) \)。  
设 \( T \in \bigwedge^r V, S \in \bigwedge^s V \)，定义**外积**（楔积） \( T \wedge S = \mathcal{A}_{r+s}(T \otimes S) \)。

### 定理 5.1（对称张量代数同构于多项式代数）  
对称张量代数 \( \bigoplus_{r=0}^{\infty} \bigodot^r V \) 同构于 \( n \) 元齐次多项式代数，且对称积对应多项式乘法。

### 引理 5.2（外积的反交换性）  
设 \( T \in \bigwedge^r V, S \in \bigwedge^s V \)，则
\[
T \wedge S = (-1)^{rs} S \wedge T
\]

### 定义 5.4（线性映射诱导的外代数映射）  
设 \( M: V \to V \) 为线性映射，可诱导映射 \( \bigwedge^r M: \bigwedge^r V \to \bigwedge^r V \)，递归定义为：
- \( \bigwedge^1 M = M \)，
- \( \bigwedge^{r+1} M (\alpha \wedge \beta) = (\bigwedge^r M)(\alpha) \wedge M(\beta) \)，其中 \( \alpha \in \bigwedge^r V, \beta \in V \)。

### 定义 5.5（行列式）  
设 \( \dim V = n \)，线性映射 \( M: V \to V \) 诱导的 \( \bigwedge^n M: \bigwedge^n V \to \bigwedge^n V \) 为一维线性映射，故为标量乘法，该标量称为 \( M \) 的**行列式**，记作 \( \det M \)。

### 定理 5.2（外积与行列式的关系）  
设 \( f^1, \ldots, f^r \in V^*, v_1, \ldots, v_r \in V \)，则
\[
(f^1 \wedge \cdots \wedge f^r)(v_1, \ldots, v_r) = \det \big( f^i(v_j) \big)_{1 \le i,j \le r}
\]

### 引理 5.3（行列式的性质）  
设 \( A, B: V \to V \) 为线性映射，则
1. \( \det(A^\mathrm{T}) = \det A \)；
2. \( \det(AB) = \det A \cdot \det B \)；
3. 若 \( A \) 可逆，则 \( \det(A^{-1}) = (\det A)^{-1} \)；
4. 行列式在坐标变换下不变（即相似变换不改变行列式）。

### 注： 性质 2 可由诱导映射的复合得到，性质 4 是性质 2 的推论。

---

# 第25章 线性代数与微积分 定义与定理总结

## 25.1 线性映射的分析性质

### 25.1.1 线性映射的范数

### 定义 25.1.1（线性映射的范数）  
对于线性映射 $A\in \mathcal{L}(\mathbf{R}^n, \mathbf{R}^m)$，定义其**范数**为 $\|A\| = \sup_{\|x\|=1} \|Ax\|$。也称为**诱导范数**。

注：该范数反映了线性映射伸张向量的能力，几何意义是一切方向的伸张系数的上确界。

### 定理 25.1.1（诱导范数的性质）  
设 $A\in \mathcal{L}(\mathbf{R}^n, \mathbf{R}^m)$，$B\in \mathcal{L}(\mathbf{R}^l, \mathbf{R}^n)$，则：
1. 正定性：$\|A\|\geq 0$，且 $\|A\|=0$ 当且仅当 $A=0$。
2. 绝对齐次性：对 $\lambda\in \mathbf{R}$，$\|\lambda A\| = |\lambda| \|A\|$。
3. 次可加性：$\|A+B\|\leq \|A\|+\|B\|$。
4. 次可乘性：$\|AB\|\leq \|A\|\|B\|$。

注：满足前三条的函数称为**范数**，若还满足第四条则称为**环范数**。

### 25.1.2 矩阵的内积与范数

### 定义 25.1.2（矩阵的内积）  
对于矩阵 $A, B \in \mathbf{F}^{m\times n}$，定义其内积为 $\langle A, B\rangle = \operatorname{tr}(A^\mathrm{T} B) = \sum_{i=1}^m\sum_{j=1}^n a_{ij}b_{ij}$（实）或 $\langle A, B\rangle = \operatorname{tr}(A^\mathrm{H} B)$（复），称为 **Frobenius 内积**。

注：这等价于将矩阵列向量化后作向量内积。

### 定义 25.1.3（“元素形式”范数）  
对于矩阵 $M\in \mathbf{F}^{m\times n}$，定义其 $\ell_p$ 范数为 $\|M\|_p = \left( \sum_{i=1}^m\sum_{j=1}^n |a_{ij}|^p \right)^{1/p}$。当 $p=2$ 时称为 **Frobenius 范数**。

### 25.1.3 收敛与连续

### 定义 25.1.4（收敛）  
在赋范空间 $V$ 中，序列 $\{x^{(i)}\}$ 收敛到 $x$ 当且仅当 $\lim_{i\to\infty} \|x^{(i)}-x\|=0$。

### 定义 25.1.5（连续）  
设 $(X,d_X)$ 和 $(Y,d_Y)$ 是度量空间，$f:X\to Y$。若对任意 $\varepsilon>0$，存在 $\delta>0$ 使得当 $d_X(x,x_0)<\delta$ 时 $d_Y(f(x),f(x_0))<\varepsilon$，则称 $f$ 在 $x_0$ 处连续。若 $f$ 在每点连续，则称 $f$ 为连续映射。

### 25.1.4 有限维赋范空间的性质

### 定理 25.1.2（Weierstrass 定理）  
设 $S$ 是有限维实赋范空间 $V$ 的紧子集，$f:S\to\mathbf{R}$ 连续，则 $f$ 在 $S$ 上可取到最大值和最小值。

### 引理 25.1.1（由线性组合定义的函数的一致连续性）  
设 $\|\cdot\|$ 是赋范空间 $V$ 上的范数，$x^{(1)},\ldots,x^{(m)}\in V$ 给定，对 $z=(z_1,\ldots,z_m)^\mathrm{T}\in\mathbf{R}^m$，令 $x(z)=\sum_{i=1}^m z_i x^{(i)}$，则函数 $g(z)=\|x(z)\|$ 关于 Euclid 范数一致连续。

### 定理 25.1.3（预范数的等价性）  
设 $f_1,f_2$ 是有限维实向量空间 $V$ 上的预范数（即满足正性、齐次性、连续性），则存在正常数 $C_m,C_M$ 使得对任意 $x\in V$ 有 $C_m f_1(x)\leq f_2(x)\leq C_M f_1(x)$。

注：该定理表明有限维空间上所有预范数（包括范数）均等价。

### 推论 25.1.1（范数的等价性）  
有限维实赋范空间上任何两个范数等价，即序列关于一个范数收敛当且仅当关于另一个范数收敛。

### 25.1.5 线性映射的有界性与连续性

### 定义 25.1.6（有界线性映射）  
设 $A:X\to Y$ 是赋范线性空间之间的线性映射。若存在常数 $M\geq 0$ 使得对任意 $x\in X$ 有 $\|Ax\|\leq M\|x\|$，则称 $A$ 为**有界映射**。

### 定理 25.1.4（有界映射的等价刻画）  
线性映射 $A:X\to Y$ 是有界的当且仅当它将任意有界集映射为有界集。

### 定理 25.1.5（连续性的局部到整体）  
若线性映射 $A:X\to Y$ 在某一点 $x_0\in X$ 处连续，则 $A$ 在整个 $X$ 上连续。

### 定理 25.1.6（有界线性变换定理）  
线性映射 $A:X\to Y$ 是有界的当且仅当它是连续的。

注：对有限维空间 $A\in\mathcal{L}(\mathbf{R}^n,\mathbf{R}^m)$，$A$ 总是有界且一致连续的。

### 25.1.6 可逆线性算子的性质

### 定理 25.1.7（可逆线性算子的稳定性）  
设 $\Omega$ 为 $\mathbf{R}^n$ 上所有可逆线性算子的集合。
1. 若 $A\in\Omega$，$B\in\mathcal{L}(\mathbf{R}^n)$ 满足 $\|B-A\|\cdot\|A^{-1}\|<1$，则 $B\in\Omega$。
2. $\Omega$ 是 $\mathcal{L}(\mathbf{R}^n)$ 的开集，且映射 $A\mapsto A^{-1}$ 在 $\Omega$ 上连续。

注：可逆矩阵在 $\mathbf{R}^{n\times n}$ 中稠密且不可逆矩阵为零测集。

## 25.2 多元函数微分学

### 25.2.1 方向导数与微分

### 定义 25.2.1（方向导数）  
设 $f:\mathbf{R}^n\to\mathbf{R}$，$x_0,v\in\mathbf{R}^n$，若极限 $\lim_{h\to 0} \frac{f(x_0+hv)-f(x_0)}{h\|v\|}$ 存在，则称 $f$ 在 $x_0$ 处沿 $v$ 的**方向导数**存在，记为 $\frac{\partial f}{\partial v}(x_0)$。

### 定义 25.2.2（微分）  
设 $f:\mathbf{R}^n\to\mathbf{R}$，若存在线性映射 $A\in\mathcal{L}(\mathbf{R}^n,\mathbf{R})$ 使得  
\[\lim_{\|h\|\to 0}\frac{|f(x_0+h)-f(x_0)-Ah|}{\|h\|}=0,\]
则称 $A$ 为 $f$ 在 $x_0$ 处的**微分**，记为 $\mathrm{d}f(x_0)$。

### 定理 25.2.1（方向导数与微分的关系）  
若 $f$ 在 $x_0$ 处可微，则沿任意方向 $u$ 的方向导数存在且 $\frac{\partial f}{\partial u}(x_0)=\mathrm{d}f(x_0)(u)$。进一步，若记梯度 $\nabla f(x_0)=(f_{x_1}(x_0),\ldots,f_{x_n}(x_0))$，则 $\mathrm{d}f(x_0)(u)=\nabla f(x_0)\cdot u$。

### 25.2.2 向量值函数的微分

### 定义 25.2.3（向量值函数的微分）  
设 $f:D\subset\mathbf{R}^n\to\mathbf{R}^m$，$x_0\in D$。若存在线性映射 $L\in\mathcal{L}(\mathbf{R}^n,\mathbf{R}^m)$ 使得  
\[f(x)-f(x_0)=L(x-x_0)+o(\|x-x_0\|)\quad (x\to x_0),\]
则称 $f$ 在 $x_0$ 处**可微**，$L$ 称为 $f$ 在 $x_0$ 处的微分，记为 $\mathrm{d}f(x_0)$ 或 $Jf(x_0)$（Jacobi 矩阵）。

### 定理 25.2.2（微分的计算）  
向量值函数 $f=(f_1,\ldots,f_m)$ 在 $x_0$ 处可微当且仅当每个分量 $f_i$ 在 $x_0$ 处可微，且 $\mathrm{d}f(x_0)$ 的矩阵表示为  
\[Jf(x_0)=\left(\frac{\partial f_i}{\partial x_j}(x_0)\right)_{m\times n}.\]

### 定理 25.2.3（链式法则）  
设 $f:D\to E$，$g:E\to U$ 可微，则复合函数 $h=g\circ f$ 可微且 $Jh(x_0)=Jg(f(x_0))Jf(x_0)$。

### 推论 25.2.1（反函数的微分）  
若 $f:D\to\Delta$ 可逆且 $f^{-1}$ 可微，则 $m=n$ 且 $Jf^{-1}(y)=[Jf(f^{-1}(y))]^{-1}$。

### 25.2.3 微分中值定理

### 定理 25.2.4（微分中值定理）  
设 $D\subset\mathbf{R}^n$ 为凸域，$f:D\to\mathbf{R}$ 在 $D$ 中处处可微，则对任意 $x,y\in D$，存在 $\xi=\theta x+(1-\theta)y$（$\theta\in(0,1)$）使得  
\[f(y)-f(x)=\nabla f(\xi)\cdot(y-x).\]

### 定理 25.2.5（拟微分中值定理）  
设 $D\subset\mathbf{R}^n$ 为凸域，$f:D\to\mathbf{R}^m$ 在 $D$ 中处处可微，则对任意 $x,y\in D$，存在 $\xi\in D$ 使得  
\[\|f(x)-f(y)\|\leq \|Jf(\xi)\|\cdot\|x-y\|.\]

### 推论 25.2.2（线性化误差估计）  
设 $D\subset\mathbf{R}^n$ 为开集，$f:D\to\mathbf{R}^m$ 可微且 $Jf$ 连续，$C\subset D$ 为紧凸集，则对任意 $\varepsilon>0$，存在 $\delta>0$ 使得当 $u,v\in C$ 且 $\|u-v\|<\delta$ 时，  
\[\|f(u)-f(v)-Jf(v)(u-v)\|\leq \varepsilon\|u-v\|.\]

### 25.2.4 压缩映射原理

### 定理 25.2.6（压缩映射原理）  
设 $(X,d)$ 是完备度量空间，$C\subset X$ 非空闭，$f:C\to C$ 满足存在 $0\leq k<1$ 使得 $d(f(x),f(y))\leq k d(x,y)$ 对任意 $x,y\in C$ 成立，则 $f$ 在 $C$ 上有唯一不动点。

### 25.2.5 反函数定理与隐函数定理

### 定理 25.2.7（反函数定理）  
设 $D\subset\mathbf{R}^n$ 为开集，$f:D\to\mathbf{R}^n$ 是 $C^k$ 映射（$k\geq 1$），$x_0\in D$ 且 $\det Jf(x_0)\neq 0$，则存在 $x_0$ 的邻域 $U\subset D$ 和 $f(x_0)$ 的邻域 $V$，使得 $f|_U:U\to V$ 可逆且其逆也是 $C^k$ 的。

### 定理 25.2.8（隐函数定理）  
设 $W\subset\mathbf{R}^{n+m}$ 为开集，$f:W\to\mathbf{R}^m$ 是 $C^k$ 映射，$(x^0,y^0)\in W$ 且 $\det J_y f(x^0,y^0)\neq 0$（其中 $J_y f$ 为对 $y$ 的 Jacobi 矩阵）。则存在 $x^0$ 的邻域 $V\subset\mathbf{R}^n$ 和唯一的 $C^k$ 映射 $\psi:V\to\mathbf{R}^m$，使得 $\psi(x^0)=y^0$ 且 $f(x,\psi(x))=f(x^0,y^0)$ 对任意 $x\in V$ 成立，且  
\[J\psi(x)=-[J_y f(x,\psi(x))]^{-1} J_x f(x,\psi(x)).\]

### 25.2.6 投影与秩定理

### 定理 25.2.9（投影的性质）  
设 $P\in\mathcal{L}(V)$ 满足 $P^2=P$，则 $P$ 称为投影，且 $V=\operatorname{im} P\oplus\ker P$。对有限维空间 $V$ 的任意子空间 $V_1$，存在投影 $P$ 使得 $\operatorname{im} P=V_1$。

### 定理 25.2.10（秩定理）  
设 $m,n,l$ 为非负整数且 $m\geq l$，$n\geq l$，$E\subset\mathbf{R}^n$ 为开集，$f:E\to\mathbf{R}^m$ 是 $C^1$ 映射，且对任意 $x\in E$，$Jf(x)$ 的秩为 $l$。固定 $x_0\in E$，令 $A=Jf(x_0)$，设 $Y_1=\operatorname{im} A$，$P$ 为 $\mathbf{R}^m$ 到 $Y_1$ 的投影，$Y_2=\ker P$。则存在开集 $U\subset E$（$x_0\in U$）和 $V\subset\mathbf{R}^n$，以及 $C^1$ 微分同胚 $H:V\to U$，使得  
\[f(H(x))=Ax+\varphi(Ax),\quad \forall x\in V,\]
其中 $\varphi$ 是 $A(V)\subset Y_1$ 到 $Y_2$ 的 $C^1$ 映射。

## 25.3 积分学

### 25.3.1 覆盖引理

### 引理 25.3.1（第一覆盖引理）  
设 $A\subset\mathbf{R}^n$ 为可求体积的有界集合，则对任意 $\varepsilon>0$，存在有限个矩形 $\{I_i\}$ 和 $\{J_j\}$，使得  
\[\bigcup_i I_i\subset A\subset \bigcup_j J_j,\quad \sum_i \nu(I_i)+\varepsilon > \nu(A) > \sum_j \nu(J_j)-\varepsilon,\]
且 $\{I_i\}$、$\{J_j\}$ 的内部互不相交。

### 引理 25.3.2（第二覆盖引理）  
设 $A\subset\mathbf{R}^n$ 为可求体积的有界集合，则对任意 $\varepsilon>0$，存在有限个 $n$ 维球体 $\{B_i\}$ 和 $\{B^j\}$，使得  
\[\bigcap_i B_i\subset A\subset\bigcup_j B^j,\quad \sum_j\nu(B^j)-\varepsilon < \nu(A) < \sum_i\nu(B_i)+\varepsilon,\]
且 $\{B_i\}$ 的内部互不相交。

### 25.3.2 线性变换下的体积变化

### 定理 25.3.1（线性变换的体积公式）  
设 $\varphi:\mathbf{R}^n\to\mathbf{R}^n$ 为线性映射，$A\subset\mathbf{R}^n$ 可求体积，则 $\varphi(A)$ 也可求体积，且  
\[\nu(\varphi(A))=|\det\varphi|\,\nu(A).\]

注：该定理的证明通过对正交变换、伸缩变换等基本变换的分析完成。

### 25.3.3 局部 Lipschitz 映射下的体积估计

### 引理 25.3.3（局部 Lipschitz 映射的零测集保持性）  
设 $\varphi:\mathbf{R}^n\to\mathbf{R}^n$ 是局部 Lipschitz 映射（即满足 $\|\varphi(x)-\varphi(y)\|\leq \rho\|x-y\|$），$A\subset\mathbf{R}^n$ 可求体积。若 $A$ 为零测集，则 $\varphi(A)$ 也为零测集；若 $A$ 与 $\varphi(A)$ 均可求体积，则 $\nu(\varphi(A))\leq \rho^n\nu(A)$。

### 引理 25.3.4（微分线性化的误差估计）  
设 $\varphi:D\subset\mathbf{R}^n\to\mathbf{R}^n$ 是 $C^1$ 映射，$A\subset D$ 可求体积且 $\overline{A}\subset D$，记 $K=\{x\mid d(x,A)\leq \delta\}\subset D$，$C=\max_{x\in K}\|J\varphi(x)\|$。则对任意 $\varepsilon>0$，存在 $\eta>0$，使得当 $x\in A$，$d(x',x)\leq \eta$ 时，  
\[\|\varphi(x')-\varphi(x)-J\varphi(x)(x'-x)\|\leq \varepsilon\|x'-x\|.\]

### 引理 25.3.5（小区域上的体积变化估计）  
沿用引理 25.3.4 的记号，当 $B\subset A$ 可求体积且 $d(B)<\eta$ 时，对任意 $x\in B$，有  
\[\nu(\varphi(B))\leq \left(|\det J\varphi(x)|+O(\varepsilon)\right)\nu(B).\]

### 25.3.4 重积分换元法

### 定理 25.3.2（重积分换元法）  
设 $\varphi:D\to\mathbf{R}^n$ 是 $C^1$ 单射，且 $J\varphi$ 处处非退化，$A\subset D$ 可求体积且 $\overline{A}\subset D$，$f$ 在 $\varphi(A)$ 上可积，则  
\[\int_{\varphi(A)} f = \int_A (f\circ\varphi)\,|\det J\varphi|.\]
特别地，$\nu(\varphi(A))=\int_A |\det J\varphi|$。

注：证明的核心思想是将 $\varphi$ 局部线性化，并利用覆盖引理和体积变化估计。


**总结**  
本章将线性代数与微积分相结合，研究了线性映射的分析性质（如范数、有界性、连续性）、多元函数的微分学（方向导数、微分、中值定理、反函数与隐函数定理）以及积分学中的重积分换元法。核心结论包括：有限维空间上范数的等价性、线性映射有界与连续的等价性、反函数与隐函数定理、以及通过线性化和误差估计证明的重积分换元公式。这些内容为后续的数学分析、微分几何等课程奠定了基础。

---

# 第26章 线性代数与最优化问题 知识点总结

由于本章内容（线性规划的几何、线性规划的对偶、下降方法）在提供的文本中仅包含章节标题和结构框架，具体的定义、定理、引理和证明细节均未展开，因此无法像前几章那样整理出详细的知识点列表。

本章旨在介绍线性代数在最优化问题中的应用，通常涵盖以下核心主题：

## §1 线性规划的几何
*注：本节通常介绍线性规划问题的几何直观。*
- **定义 1.1（线性规划标准形式）**：最大化（或最小化）目标函数 \( c^T x \)，约束条件为 \( Ax \le b \) 且 \( x \ge 0 \)。
- **定义 1.2（可行域）**：满足所有约束条件的向量 \( x \) 的集合，它是一个凸多面体。
- **定理 1.3（线性规划基本定理）**：若线性规划问题有最优解，则至少有一个最优解出现在可行域的顶点（极点）上。

## §2 线性规划的对偶
*注：本节介绍线性规划问题的对偶理论。*
- **定义 2.1（对偶问题）**：对于给定的原始线性规划问题，存在一个对应的对偶线性规划问题。
- **定理 2.2（弱对偶定理）**：原始问题的任何可行解的目标函数值都不大于对偶问题的任何可行解的目标函数值（对于最大化问题）。
- **定理 2.3（强对偶定理）**：若原始问题有最优解，则对偶问题也有最优解，且两者的最优值相等。

## §3 下降方法
*注：本节介绍求解无约束或有约束最优化问题的迭代算法。*
- **定义 3.1（下降方向）**：对于目标函数 \( f(x) \)，若方向 \( d \) 满足 \( \nabla f(x)^T d < 0 \)，则称 \( d \) 为在点 \( x \) 处的下降方向。
- **算法 3.2（梯度下降法框架）**：从初始点 \( x_0 \) 开始，迭代更新 \( x_{k+1} = x_k - \alpha_k \nabla f(x_k) \)，其中 \( \alpha_k > 0 \) 为步长。
- **定理 3.3（收敛性条件）**：在一定条件下（如 \( f \) 为凸函数且 Lipschitz 连续），梯度下降法产生的序列收敛到驻点。


**总结**：本章内容依赖于最优化理论的具体展开，目前提供的文本仅为框架。完整的知识点总结需待具体内容补充后才能系统整理。以上列出的是该领域常见的基础概念和定理，供参考。

