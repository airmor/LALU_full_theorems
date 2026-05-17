### LALU — 定义、定理与引理全集

[TOC]

#### 第1章 预备知识

##### §1.1 基本代数结构

**定义 1.1 (笛卡尔积)**  设 $A$ 和 $B$ 是两个非空集合，称 $A\times B=\{(a,b)\mid a\in A,\; b\in B\}$ 为 $A$ 与 $B$ 的笛卡尔积。若 $A=B$，可记作 $A^2$。

**定义 1.2 (代数系统 / 代数结构)**  非空集合 $X$ 与定义在其上的若干运算 $f_1,\dots,f_k$ 组成的系统记为 $\langle X\colon f_1,\dots,f_k\rangle$，称为代数系统；若这些运算具有特定代数性质，则称为代数结构。

**定义 1.3 (群 / 半群 / 含幺半群 / Abel 群)**  对代数系统 $\langle G\colon\circ\rangle$，
1. 若运算 $\circ$ 满足结合律，称为半群；
2. 若半群中存在单位元，称为含幺半群；
3. 若含幺半群中每元素有逆元，称为群；
4. 若群的运算满足交换律，称为 Abel 群（交换群）。

**定理 1.1 (群的单位元与逆元唯一)**
1. 群的单位元唯一；
2. 群中每个元素的逆元唯一。

**定义 1.4 (域)**  代数系统 $\langle F\colon +,\circ\rangle$ 称为域，若
1. $\langle F,+\rangle$ 为交换群，其单位元记作 $0$；
2. $\langle F\setminus\{0\},\circ\rangle$ 为交换群；
3. $\circ$ 对 $+$ 满足左、右分配律。

**定理 1.2 (数域的充要条件与包含 $\mathbf{Q}$)**
1. 若数集 $F$ 包含 $0,1$ 且对加减乘除（除数非零）封闭，则 $F$ 为数域；
2. 任何数域包含有理数域 $\mathbf{Q}$。

##### §1.2 复数域的引入

**定理 1.3 (复数乘法构造)**  在 $\mathbf{R}^2$ 上可定义乘法 $(a,b)\cdot(c,d)=(ac-bd,ad+bc)$，使 $\langle\mathbf{R}^2,+,\cdot\rangle$ 成为域（复数域 $\mathbf{C}$），且模长可乘 $|uv|=|u||v|$。

**定理 1.4 (复数模的三角不等式)**  对任意 $z,w\in\mathbf{C}$，有 $|z+w|\le|z|+|w|$。

##### §1.3 等价关系

**定义 1.5 (等价关系与等价类)**  设 $A$ 为集合，关系 $R$ 若满足
1. 自反性：$\forall a\in A,\; aRa$；
2. 对称性：若 $aRb$，则 $bRa$；
3. 传递性：若 $aRb$ 且 $bRc$，则 $aRc$，
则称 $R$ 为等价关系。对 $a\in A$，定义等价类 $\overline a=\{b\in A\mid bRa\}$。

**引理 1.1 (等价引理)**  对任意 $a,b\in A$，有 $\overline a=\overline b \iff aRb$。

**推论 1.1 (等价类的互斥性与分划)**
1. 任意两等价类要么相等要么互不相交；
2. 所有等价类构成 $A$ 的分划；
3. 反之，由分划可定义等价关系。

**定义 1.6 (环 / 除环 / 交换环)**  代数系统 $\langle R\colon+,\circ\rangle$ 称为一个环，若
1. $\langle R,+\rangle$ 是交换群，单位元记作 $0$；
2. $\langle R,\circ\rangle$ 是幺半群；
3. 运算 $\circ$ 对 $+$ 满足左、右分配律。
若进一步每个非 $0$ 元素关于 $\circ$ 都有逆元，则称为除环；若 $\circ$ 运算满足交换律，则称为交换环。交换除环即为域。

**定理 1.5 (共轭复数的性质)**  设 $z=(a,b)\in\mathbf{C}$，称 $\overline z=(a,-b)$ 为 $z$ 的共轭复数，则 $\overline z z=|z|^2$。

**定义 1.7 (分划)**  若集合 $A$ 的子集族 $\{A_i\}$ 满足 $\bigcup_i A_i=A$ 且 $A_i\cap A_j=\varnothing\ (i\ne j)$，则称 $\{A_i\}$ 为 $A$ 的一个分划。

**定义 1.8 (商集)**  设 $R$ 是集合 $A$ 的等价关系，以关于 $R$ 的等价类为元素的集族 $\{\overline a\}$ 称为 $A$ 对 $R$ 的商集，记为 $A/R$。映射 $\pi(a)=\overline a$ 称为自然映射。

**定义 1.9 (运算的相容性 / 良定义)**  若 $A$ 上有二元运算 $+$，且在 $A/R$ 上以 $\overline a\oplus\overline b=\overline{a+b}$ 继承运算，则称 $\oplus$ 与 $R$ 相容（或在 $A/R$ 上良定义）当且仅当 $aRb$、$cRd$ 时有 $\overline a\oplus\overline c=\overline b\oplus\overline d$。

**定理 1.6 (等价类构成分划)**  设 $R$ 是集合 $A$ 的等价关系，则由所有不同等价类构成的子集族 $\{\overline a\}$ 是 $A$ 的分划；反之，基于分划可在 $A$ 中定义等价关系。

**定理 1.7 (模 $n$ 同余与加乘运算相容)**  模 $n$ 同余关系与加法、乘法运算相容。

**定义 1.10 (线性方程组)**  由 $m$ 个线性方程组成的 $n$ 元线性方程组可表示为
$$
\begin{cases}
\begin{aligned}
a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n&=b_1\\
a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n&=b_2\\
&\qquad\vdots\\
a_{m1}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=b_m
\end{aligned}
\end{cases}
$$

**定义 1.11 ($n$ 元笛卡尔积 / 笛卡尔幂)**  设 $A_i\ (1\le i\le n)$ 是一族集合，集合 $\prod_{i=1}^n A_i=\{(a_1,\ldots,a_n)\mid a_i\in A_i\}$ 称为 $n$ 元笛卡尔积；当所有 $A_i=A$ 时记 $A^n=\prod_{i=1}^nA$ 为 $A$ 的笛卡尔幂。

**定义 1.12 ($n$ 元实向量 / 零向量)**  $\mathbf{R}^n$ 中的元素 $(x_1,\ldots,x_n)$ 称为 $n$ 元实向量，若所有分量都为 $0$，则称为零向量。

**定义 1.13 (矩阵)**  域 $\mathbf{F}$ 中的 $m\times n$ 个元素 $a_{ij}$ 排成 $m$ 行 $n$ 列的矩形数表，称为域 $\mathbf{F}$ 上的一个 $m\times n$ 矩阵，记作 $(a_{ij})_{m\times n}$。

**定义 1.14 (矩阵的转置)**  设 $A=(a_{ij})_{m\times n}$，则 $A^\mathrm{T}$ 是一个 $n\times m$ 矩阵，满足 $(A^\mathrm{T})_{ij}=a_{ji}$。

**定义 1.15 (系数矩阵 / 齐次与非齐次线性方程组)**  线性方程组的系数构成的矩阵称为系数矩阵 $A$；若右端常数项全为 $0$，即 $\vec b=\vec0$，则称为齐次线性方程组，否则为非齐次线性方程组。

**定义 1.16 (增广矩阵 / 阶梯矩阵 / 简化阶梯矩阵)**  增广矩阵指 $(A,\vec b)$；阶梯矩阵指系数全零行在最下方且主元位置逐行右移的矩阵；简化阶梯矩阵指主元都为 $1$ 且主元列其余元素全为 $0$ 的阶梯矩阵。

**定理 1.8 (线性方程组的矩阵与向量表示)**  线性方程组可写为矩阵形式 $AX=\vec b$，也可写为向量形式 $x_1\vec\beta_1+\cdots+x_n\vec\beta_n=\vec b$，其中 $\vec\beta_i$ 为 $A$ 的第 $i$ 列。

**定理 1.9 (矩阵左乘列向量的运算规则)**  设 $A=(\vec\beta_1,\ldots,\vec\beta_n)$，$X=(x_1,\ldots,x_n)^\mathrm{T}$，则 $AX=x_1\vec\beta_1+\cdots+x_n\vec\beta_n$。

**定理 1.10 (数域的结构定理)**  任何数域都包含有理数域 $\mathbf{Q}$，且 $\mathbf{Q}$ 是最小的数域。

**定理 1.11 (有限域的构造)**  设 $\mathbf{Z}_n$ 是整数模 $n$ 同余类的集合，按模 $n$ 加法和乘法定义运算，则 $\langle\mathbf{Z}_n\colon\oplus,\circ\rangle$ 是域当且仅当 $n$ 是素数。

**定理 1.12 (三维实数向量空间无法构成域)**  $\mathbf{R}^3$ 上不存在同时满足单位元、交换、长度可乘的乘法运算。

**定理 1.13 (等价关系的替代定义)**  若集合 $A$ 上的二元关系 $R$ 满足自反性且满足 $aRb$、$aRc\Rightarrow bRc$，则 $R$ 是等价关系。

**定理 1.14 (零环)**  若 $A$ 是 Abel 群，定义 $ab=0$（对任意 $a,b\in A$），则 $A$ 构成一个环，称为零环。

**算法 1.1 (高斯-若当消元法)**  求解线性方程组时：先写增广矩阵，再作初等行变换化为阶梯矩阵，最后化为简化阶梯矩阵并据此判断解的情况。

##### §1.4 公理化思想与布尔巴基学派

###### §1.4.1 公理化思想

**定义 1.17 (非正式的自然数定义)**  自然数可由 $0$ 与后继映射 $S(n)=n+1$ 递归构造；满足归纳原则：若 $0$ 属于某性质族且对任意 $n$ 有 $P(n)\rightarrow P(S(n))$，则 $P(n)$ 对所有自然数成立。

**定理 1.18 (强归纳法原理)**  设 $m_0$ 为自然数，若 $P(m_0)$ 成立且对任意 $m>m_0$，由 $P(m')$ 对一切 $m_0 \le m' < m$ 成立可推得 $P(m)$，则 $P(m)$ 对所有 $m\ge m_0$ 成立。

###### §1.4.2 布尔巴基学派

**定义 1.19 (偏序关系)**  在集合 $X$ 上的二元关系 $R$ 若满足自反性、反对称性与传递性，则称为偏序关系；若任意两元素可比较则称为全序。

**定义 1.20 (拓扑空间)**  设 $X$ 为集合，若 $\tau\subseteq\mathcal{P}(X)$ 满足 $\varnothing,X\in\tau$，任意并与有限交对 $\tau$ 闭合，则 $(X,\tau)$ 称为拓扑空间（此处仅作简要引入）。

---

#### 第2章 线性空间

##### §2.1 线性空间的定义

**定义 2.1 (线性空间)**  设 $V$ 为非空集合，$\mathbf{F}$ 为数域，给定加法与数乘满足：
1. 加法结合律：$\alpha+(\beta+\gamma)=(\alpha+\beta)+\gamma$；
2. 加法单位元：$\exists\,0\in V$ 使 $\alpha+0=0+\alpha=\alpha$；
3. 加法逆元：$\forall\alpha\in V,\exists\,-\alpha\in V$ 使 $\alpha+(-\alpha)=0$；
4. 加法交换律：$\alpha+\beta=\beta+\alpha$；
5. 数乘单位元：$1\cdot\alpha=\alpha$；
6. 数乘结合律：$\lambda(\mu\alpha)=(\lambda\mu)\alpha$；
7. 左分配律：$(\lambda+\mu)\alpha=\lambda\alpha+\mu\alpha$；
8. 右分配律：$\lambda(\alpha+\beta)=\lambda\alpha+\lambda\beta$。

**定理 2.1 (线性空间基本运算性质)**  设 $V(\mathbf{F})$ 为线性空间，则：
1. $\lambda(\alpha-\beta)=\lambda\alpha-\lambda\beta$；
2. $(\lambda-\mu)\alpha=\lambda\alpha-\mu\alpha$；
3. $\lambda\cdot\vec{0}=\vec{0}$；
4. $\lambda(-\beta)=-(\lambda\beta)$；
5. $0\cdot\alpha=\vec{0}$；
6. $(-\mu)\alpha=-(\mu\alpha)$；
7. 若 $\lambda\alpha=\vec{0}$，则 $\lambda=0$ 或 $\alpha=\vec{0}$。

**定理 2.2 (加法交换律冗余)**  线性空间 8 条公理中，加法交换律可由其余 7 条推出。

##### §2.2 线性空间的例子与拓展

**定义 2.2 (多项式空间)**  $\mathbf{F}[x]_{n+1}=\{a_0+a_1x+\cdots+a_nx^n\mid a_i\in\mathbf{F}\}$ 关于多项式加法与数乘构成线性空间；$\mathbf{F}[x]'_{n+1}=\{\cdots,a_n\neq0\}$ 不构成线性空间。

**定义 2.3 (函数空间)**  $C[a,b]$ 为 $[a,b]$ 上连续实值函数全体，关于函数加法与数乘构成实线性空间。

**定义 2.4 (模)**  设 $R$ 为环，$M$ 为加法 Abel 群，若数乘 $R\times M\to M$ 满足
1. $1\alpha=\alpha$；
2. $r(s\alpha)=(rs)\alpha$；
3. $(r+s)\alpha=r\alpha+s\alpha$；
4. $r(\alpha+\beta)=r\alpha+r\beta$，
则称 $M$ 为左 $R$-模（右模、双模类同）。

**定义 2.5 (线性同态/同构)**  线性映射 $\varphi:V\to W$ 满足
$\varphi(\alpha+\beta)=\varphi(\alpha)+\varphi(\beta)$，$\varphi(\lambda\alpha)=\lambda\varphi(\alpha)$；若 $\varphi$ 为双射，则称 $V\cong W$。

**定义 2.6 (数域与线性空间的关系)**  $\mathbf{C}$ 既是 $\mathbf{C}$-线性空间，也是 $\mathbf{R}$-线性空间；$\mathbf{R}$ 是 $\mathbf{R}$-线性空间，但一般不是 $\mathbf{C}$-线性空间。

**定理 2.3 (子空间与线性扩张的等价刻画)**  设 $W$ 是线性空间 $V$ 的子集，则 $W$ 是子空间当且仅当 $\operatorname{span}(W)=W$。

**定理 2.4 (数域扩张下的线性空间)**  设 $\mathbf{E}\subseteq\mathbf{F}$ 是域扩张，则：
1. $\mathbf{F}$ 是 $\mathbf{E}$ 上的线性空间；
2. 若 $V$ 是 $\mathbf{F}$ 上的线性空间，则 $V$ 也是 $\mathbf{E}$ 上的线性空间。

**定理 2.5 (有限域上的线性空间视角)**  若 $\mathbf{F}_{p^n}$ 是特征 $p$ 的有限域，则 $\mathbf{F}_{p^n}$ 可视为 $\mathbf{Z}_p$ 上的线性空间。

##### §2.3 线性子空间

**定义 2.7 (线性子空间)**  设 $W\subseteq V(\mathbf{F})$ 非空，若 $W$ 对 $V$ 的加法与数乘封闭，则 $W$ 为子空间。

**定理 2.6 (子空间判别定理)**  非空子集 $W$ 是子空间 $\iff$ 对加法与数乘封闭。

**定理 2.7 (解空间性质)**  齐次线性方程组 $AX=0$ 的解集是 $\mathbf{F}^n$ 的子空间；非齐次方程组解集不是子空间。

##### §2.4 线性表示与线性扩张

**定义 2.8 (线性组合/线性表示)**  若 $\alpha=\lambda_1\alpha_1+\cdots+\lambda_m\alpha_m$，则 $\alpha$ 为向量组的线性组合（线性表示）。

**定义 2.9 (线性扩张)**  子集 $S$ 的线性扩张为
$\operatorname{span}(S)=\{\lambda_1\alpha_1+\cdots+\lambda_k\alpha_k\mid\lambda_i\in\mathbf{F},\alpha_i\in S\}$。

**定理 2.8 (线性扩张构造子空间)**  $\operatorname{span}(S)$ 是包含 $S$ 的最小子空间。

**定理 2.9 (线性方程组解的表示)**  设 $\lambda\beta+\lambda_1\alpha_1+\cdots+\lambda_r\alpha_r=\vec{0}$，若 $\lambda\ne0$，则
$$
\beta=-\lambda^{-1}\lambda_1\alpha_1-\cdots-\lambda^{-1}\lambda_r\alpha_r.
$$

**方法 2.1 (子空间判别框架)**  验证非空；证明对加法与数乘封闭即可。

**方法 2.2 (最小性证明)**  证明 $S\subseteq W$，再证 $\operatorname{span}(S)\subseteq W$；反向包含显然。

---

#### 第3章 有限维线性空间

##### §3.1 线性相关性

**定义 3.1 (线性相关/无关)**  向量组 $\alpha_1,\ldots,\alpha_m$ 存在不全为 $0$ 的系数使 $\sum\lambda_i\alpha_i=0$ 则线性相关，否则线性无关。

**定理 3.1 (线性相关的表示判别)**  向量组线性相关 $\iff$ 其中某个向量可由其余向量线性表示。

**定理 3.2 (齐次方程组判别)**  向量组 $\alpha_1,\ldots,\alpha_m$ 线性相关 $\iff$ 齐次方程组 $x_1\alpha_1+\cdots+x_m\alpha_m=0$ 有非零解；线性无关 $\iff$ 仅零解。

**定理 3.3 (线性无关的唯一表示)**  若 $\alpha_1,\ldots,\alpha_m$ 线性无关且 $\beta,\alpha_1,\ldots,\alpha_m$ 线性相关，则 $\beta$ 可由 $\alpha_1,\ldots,\alpha_m$ 线性表示且表示唯一。

**推论 3.1 (表示唯一性判别)**
1. 向量组线性无关 $\iff$ 表示方式唯一；
2. 向量组线性相关 $\iff$ 表示方式不唯一（有无穷多种）。

**定理 3.4 (部分组与扩充)**
1. 线性无关组的任意子组线性无关；
2. 线性相关组的任意超集线性相关。

##### §3.2 秩与极大线性无关组

**引理 3.1 (线性相关性引理)**  若 $\alpha_1,\ldots,\alpha_m$ 线性相关，则存在 $j$ 使：
1. $\alpha_j\in\operatorname{span}(\alpha_1,\ldots,\alpha_{j-1})$；
2. 删去 $\alpha_j$ 后张成空间不变。

**推论 3.2 (前缀表示唯一性)**  若 $\alpha_1\neq0$ 且向量组相关，则存在 $i>1$ 使 $\alpha_i$ 可由前 $i-1$ 个向量唯一表示。

**定义 3.2 (极大线性无关组与秩)**  向量组 $S$ 的极大线性无关组 $B$ 的长度 $r(S)$ 称为秩。

**定理 3.5 (线性表示定理/源泉定理)**  若 $\beta_1,\ldots,\beta_s$ 可由 $\alpha_1,\ldots,\alpha_r$ 线性表示且 $s>r$，则 $\beta_1,\ldots,\beta_s$ 线性相关。

**推论 3.3 (秩比较与唯一性)**
1. 若 $B_1$ 可由 $B_2$ 表示，则 $r(B_1)\le r(B_2)$；
2. 两个线性无关向量组互相表示 $\iff$ 长度相等；
3. 向量组任意两个极大线性无关组长度相等，秩唯一。

##### §3.3 基与维数

**定义 3.3 (基与维数)**  若有限向量组 $B$ 线性无关且 $\operatorname{span}(B)=V$，则 $B$ 为基，$\dim V=|B|$。

**定理 3.6 (有限维线性空间基的存在性)**  有限维线性空间一定存在基。

**定理 3.7 (维数基本判别)**
1. $n$ 维空间任意 $n+1$ 个向量线性相关；
2. 任意 $n-1$ 个向量不能张成 $V$；
3. $n$ 个向量线性无关 $\iff$ 可表示 $V$ 中任意向量。

**定理 3.8 (子空间基可扩充)**  若 $W$ 是 $n$ 维空间 $V$ 的子空间，则 $W$ 的基可扩充为 $V$ 的基。

**定义 3.4 (有限维/无限维)**  存在有限子集张成则有限维，否则无限维。

**定理 3.9 (子空间维数的不等式)**  设 $U$ 和 $W$ 是 $V$ 的非零子空间，且 $U\subseteq W$，则 $\dim U\le\dim W$；若 $\dim U=\dim W$，则 $U=W$。

**定理 3.10 (有限维线性空间的判定)**  $\mathbf{R}[x]_3$ 是有限维线性空间；$\mathbf{R}[x]$ 是无限维线性空间。

##### §3.4 向量的坐标

**引理 3.2 (初等行变换不改变列的线性相关性)**  对任何矩阵，任意初等行变换均可表示为可逆矩阵左乘，故初等行变换不改变列向量组的线性相关性：若矩阵 $A$ 的列向量线性相关，则对任意可逆矩阵 $P$，列向量组 of $PA$ 仍线性相关；反之亦然。

**引理 3.3 (极大线性无关组的构造方法)**  给定向量组 $S$，通过逐一扫描 $S$ 并保留不被前面已选向量张成的向量，同时丢弃能被前面张成的向量，可构造出 $S$ 的一个极大线性无关子集 $B$；所得 $B$ 是 $\operatorname{span}(S)$ 的一组基当且仅当 $\operatorname{span}(B)=\operatorname{span}(S)$。

**定义 3.5 (坐标)**  若 $B=\{\beta_1,\ldots,\beta_n\}$ 为 $V$ 的基，$\alpha=\sum a_i\beta_i$，则 $(a_1,\ldots,a_n)$ 为 $\alpha$ 在 $B$ 下的坐标。

**定理 3.11 (坐标映射同构)**  坐标映射 $\varphi_B:V\to\mathbf{F}^n$ 为线性同构，任意 $n$ 维线性空间同构于 $\mathbf{F}^n$。

##### §3.5 算法与方法

**算法 3.1 (极大线性无关组求法)**  将向量作列排成矩阵并化为阶梯形，取主元列对应原向量即得一组极大线性无关组。

**算法 3.2 (扩基算法)**  取原无关组与一组基合并后求极大线性无关组，保留原向量得到扩张基。

**定理 3.12 (替换定理/交换引理)**  若 $\alpha_1,\ldots,\alpha_r$ 线性无关且可由 $\beta_1,\ldots,\beta_n$ 表示，则可用 $\alpha_1,\ldots,\alpha_r$ 替换 $\beta$ 中 $r$ 个向量并保持等价（可用归纳法证明）。

##### §3.6 补充说明与隐含定理

**定理 3.13 (线性相关性的判定：特殊函数空间)**  对函数空间中的向量组（函数），可通过代入特殊值构造方程组以判定线性相关性。

**定理 3.14 (不同数域下线性空间维数的差异)**  同一集合在不同数域上构成的线性空间可能具有不同维数，例如：$\mathbf{C}$ 作为 $\mathbf{C}$-线性空间维数为 $1$，作为 $\mathbf{R}$-线性空间维数为 $2$。

---

#### 第4章 线性空间的运算

##### §4.1 线性空间的交、并、和

**定义 4.1 (交、并、和)**  设 $W_1,W_2$ 为 $V$ 的子空间，定义
1. $W_1\cap W_2=\{\alpha\mid\alpha\in W_1\text{ 且 }\alpha\in W_2\}$；
2. $W_1\cup W_2=\{\alpha\mid\alpha\in W_1\text{ 或 }\alpha\in W_2\}$；
3. $W_1+W_2=\{\alpha_1+\alpha_2\mid\alpha_1\in W_1,\alpha_2\in W_2\}$。

**定理 4.1 (交、并、和的子空间性)**
1. $W_1\cap W_2$ 是子空间；
2. $W_1+W_2$ 是子空间；
3. $W_1\cup W_2$ 是子空间 $\iff W_1\subseteq W_2$ 或 $W_2\subseteq W_1$，且等价于 $W_1\cup W_2=W_1+W_2$。

**定义 4.2 (多子空间交并和)**  设 $W_1,\ldots,W_s$ 为子空间，定义 $\bigcap_i W_i,\ \bigcup_i W_i,\ \sum_i W_i$ 与两子空间情形一致。

##### §4.2 覆盖定理

**定理 4.2 (覆盖定理)**  若 $V_1,\ldots,V_s$ 为 $V$ 的非平凡子空间，则 $V_1\cup\cdots\cup V_s\subsetneq V$。

**引理 4.1 (覆盖定理的归纳基础)**  当 $s=2$ 时结论成立：取 $\alpha\notin V_1$，若 $\alpha\notin V_2$ 则成立；若 $\alpha\in V_2$，取 $\beta\notin V_2$，则 $\alpha+\beta$ 与 $2\alpha+\beta$ 至少有一个不在 $V_1\cup V_2$。

**引理 4.2 (覆盖定理的归纳步骤)**  假设对 $s-1$ 个子空间结论成立，则对 $s$ 个子空间亦成立（用归纳假设与两子空间情形构造向量）。

**方法 4.1 (数学归纳法框架)**  证明对 $s=2$ 成立，再假设 $s-1$ 成立推出 $s$ 成立。

##### §4.3 维数公式

**定理 4.3 (子空间维数公式)**  对子空间 $W_1,W_2$，有
$$\dim W_1+\dim W_2=\dim(W_1+W_2)+\dim(W_1\cap W_2).$$

**方法 4.2 (设小扩大)**  先取 $W_1\cap W_2$ 的基，再分别扩充为 $W_1,W_2$ 的基以构造 $W_1+W_2$ 的基。

##### §4.4 直和

**定义 4.3 (直和与互补子空间)**  若 $W_1\cap W_2=\{0\}$，称 $W_1+W_2$ 为直和，记作 $W_1\oplus W_2$；若 $V=W_1\oplus W_2$，则称二者互补。

**定义 4.4 (多个子空间的直和)**  设 $W_1,\ldots,W_n$ 是 $V$ 的子空间。若对每个 $i$ 有 $W_i\cap\sum_{j\ne i}W_j=\{0\}$，则称 $\sum_{i=1}^n W_i$ 为直和，记作 $\bigoplus_{i=1}^n W_i$。

**定理 4.4 (直和等价命题)**  下列条件等价：
1. $W_1+W_2$ 为直和；
2. 任意 $\alpha\in W_1+W_2$ 分解 $\alpha=\alpha_1+\alpha_2$ 唯一；
3. $\vec{0}=\alpha_1+\alpha_2$ 只在 $\alpha_1=\alpha_2=\vec{0}$ 时成立；
4. $\dim(W_1+W_2)=\dim W_1+\dim W_2$。

**定理 4.5 (多空间直和)**  若 $V=V_1\oplus V_2$ 且 $V_1=V_{11}\oplus\cdots\oplus V_{1s}$，$V_2=V_{21}\oplus\cdots\oplus V_{2t}$，则
$$V=V_{11}\oplus\cdots\oplus V_{1s}\oplus V_{21}\oplus\cdots\oplus V_{2t}.$$

##### §4.5 仿射子集与商空间

**定义 4.5 (由子空间诱导的等价关系)**  设 $U$ 是 $V$ 的子空间，定义 $V$ 上的关系 $\sim$ 为 $\alpha\sim\beta\iff\alpha-\beta\in U$；等价类记作 $\overline{\alpha}=\alpha+U$。

**定理 4.6 (零类为子空间)**  若 $R$ 为与线性运算相容的等价关系，则零向量等价类 $\overline{0}$ 为子空间。

**引理 4.3 (等价关系的相容性)**  若 $\alpha_1\sim\alpha_2$、$\beta_1\sim\beta_2$，则 $(\alpha_1+\beta_1)\sim(\alpha_2+\beta_2)$ 且 $\lambda\alpha_1\sim\lambda\alpha_2$（$\lambda\in\mathbf{F}$）。

**定理 4.7 (等价关系与子空间)**  设 $U=\overline{0}$，则 $v_1Rv_2\iff v_1-v_2\in U$。

**定义 4.6 (仿射子集)**  设 $U$ 为子空间，$v+U=\{v+u\mid u\in U\}$ 称为仿射子集。

**定理 4.8 (仿射子集判别)**  对 $v,w\in V$，以下等价：
1. $v-w\in U$；
2. $v+U=w+U$；
3. $(v+U)\cap(w+U)\ne\varnothing$。

**定理 4.9 (仿射子集的等价刻画)**  非空子集 $A$ 是仿射子集 $\iff$ $\forall v,w\in A,\forall\lambda\in\mathbf{F}$，有 $\lambda v+(1-\lambda)w\in A$。

**引理 4.4 (仿射子集的平移结构)**  若 $A$ 是仿射子集，则存在 $v\in V$ 与子空间 $U$ 使得 $A=v+U$。

**定义 4.7 (商空间)**  商空间 $V/U=\{v+U\mid v\in V\}$。

**定义 4.8 (商空间运算)**  对 $\alpha,\beta\in V$、$\lambda\in\mathbf{F}$，
1. $(\alpha+U)+(\beta+U)=(\alpha+\beta)+U$；
2. $\lambda(\alpha+U)=(\lambda\alpha)+U$。

**定理 4.10 (商空间维数公式)**  若 $U$ 为有限维子空间，则
$$\dim(V/U)=\dim V-\dim U.$$

---

#### 第5章 线性映射

##### §5.1 线性映射的定义

**定义 5.1 (线性映射)**  映射 $\sigma:V_1(\mathbf{F})\to V_2(\mathbf{F})$ 若满足
$$\sigma(\lambda\alpha+\mu\beta)=\lambda\sigma(\alpha)+\mu\sigma(\beta),$$
则称为线性映射；$V\to V$ 的线性映射称线性变换；$V\to\mathbf{F}$ 的线性映射称线性泛函。

**定理 5.1 (零元保持)**  线性映射满足 $\sigma(0_1)=0_2$。

**定理 5.2 (保相关性)**  若 $\alpha_1,\ldots,\alpha_n$ 线性相关，则 $\sigma(\alpha_1),\ldots,\sigma(\alpha_n)$ 线性相关；若像线性无关，则原向量组线性无关。

##### §5.2 线性映射的运算

**定义 5.2 (线性映射加法与数乘)**  对 $\sigma,\tau\in\mathcal{L}(V_1,V_2)$，
1. $(\sigma+\tau)(\alpha)=\sigma(\alpha)+\tau(\alpha)$；
2. $(\lambda\sigma)(\alpha)=\lambda\sigma(\alpha)$。

**定义 5.3 (线性映射的复合)**  设 $\sigma\in\mathcal{L}(V_1,V_2)$，$\tau\in\mathcal{L}(V_2,V_3)$，定义 $\tau\sigma\in\mathcal{L}(V_1,V_3)$ 为
$$
(\tau\sigma)(\alpha)=\tau(\sigma(\alpha)),\quad \forall\alpha\in V_1.
$$

**定义 5.4 (线性映射的逆)**  设 $\sigma\in\mathcal{L}(V_1,V_2)$。若存在 $\tau\in\mathcal{L}(V_2,V_1)$ 使 $\sigma\tau=I_{V_2}$ 且 $\tau\sigma=I_{V_1}$，则称 $\sigma$ 可逆，$\tau$ 称为 $\sigma$ 的逆映射，记为 $\sigma^{-1}$。

**定理 5.3 (线性映射全体构成线性空间)**  $\mathcal{L}(V_1,V_2)$ 在上述运算下为线性空间。

**定理 5.4 (复合映射线性)**  若 $\sigma:V_1\to V_2,\tau:V_2\to V_3$ 线性，则 $\tau\sigma$ 线性。

**定理 5.5 (逆映射线性)**  若 $\sigma$ 可逆，则 $\sigma^{-1}$ 线性。

##### §5.3 像与核

**定义 5.5 (像与核)**  像 $\operatorname{im}\sigma=\{\sigma(\alpha)\mid\alpha\in V_1\}$，核 $\ker\sigma=\{\alpha\mid\sigma(\alpha)=0_2\}$。

**定理 5.6 (像与核为子空间)**  $\operatorname{im}\sigma$ 是 $V_2$ 的子空间，$\ker\sigma$ 是 $V_1$ 的子空间。

**定理 5.7 (单射判别)**  $\sigma$ 为单射 $\iff \ker\sigma=\{0\}$。

**方法 5.1 (求像与核)**  取出发空间一组基，像空间为其像的线性扩张；核空间由 $\sigma(\alpha)=0$ 解齐次方程组得到。

##### §5.4 线性映射的确定与构造

**定理 5.8 (基像唯一确定映射)**  若 $\sigma(\alpha_i)=\tau(\alpha_i)$ 对基 $\{\alpha_i\}$ 成立，则 $\sigma=\tau$。

**定理 5.9 (基像构造映射)**  给定 $V_1$ 基 $\{\alpha_i\}$ 与 $V_2$ 任意向量组 $\{\beta_i\}$，存在唯一线性映射使 $\sigma(\alpha_i)=\beta_i$。

##### §5.5 线性映射基本定理

**定义 5.6 (线性映射的秩)**  若 $\sigma(V_1)$ 有限维，定义 $r(\sigma)=\dim\operatorname{im}\sigma$。

**定理 5.10 (线性映射基本定理/秩-零化度公式)**  若 $\dim V_1=n$，则
$$r(\sigma)+\dim\ker\sigma=n.$$

**定理 5.11 (双射等价条件)**  若 $\dim V_1=\dim V_2=n$，则以下等价：
1. $\ker\sigma=\{0\}$；
2. $\sigma$ 为单射；
3. $\sigma$ 为满射；
4. $\sigma$ 为双射；
5. $r(\sigma)=n$。

##### §5.6 同构

**定义 5.7 (同构)**  线性双射称同构映射；若存在同构映射则 $V_1\cong V_2$。

**定理 5.12 (同构保持线性无关与秩)**  同构映射保持向量组线性相关性与秩不变。

**定理 5.13 (同构判别)**  两线性空间同构 $\iff$ 维数相等。

##### §5.7 积空间与直和

**定义 5.8 (积空间)**  对 $V_1,\ldots,V_n$，定义
1. $V_1\times\cdots\times V_n=\{(v_1,\ldots,v_n)\mid v_i\in V_i\}$；
2. 加法与数乘按分量定义。

**定理 5.14 (积空间维数)**  $\dim(V_1\times\cdots\times V_n)=\sum_i\dim V_i$。

**定理 5.15 (积与直和)**  设 $\sigma(u_1,\ldots,u_n)=u_1+\cdots+u_n$，则 $U_1+\cdots+U_n$ 为直和 $\iff \sigma$ 为同构。

**定理 5.16 (直和维数判别)**  $U_1+\cdots+U_n$ 为直和 $\iff \dim(U_1+\cdots+U_n)=\sum_i\dim U_i$。

**方法 5.2 (线性映射判定要点)**  重点检查：$\sigma(0)=0$、对线性相关性的必要条件、以及维数导致的满射/单射不可能性。

##### §5.8 像、核与直和进阶

**定理 5.17 (商映射与商空间维数)**  设 $U$ 是有限维线性空间 $V$ 的子空间，商映射 $\pi:V\to V/U$ 由 $\pi(v)=v+U$ 给出，则 $\pi$ 是线性满射，且 $\ker\pi=U$；从而 $\dim(V/U)=\dim V-\dim U$。

**定理 5.18 (幂等变换的直和分解)**  设 $\sigma\in\mathcal{L}(V,V)$ 是幂等变换（即 $\sigma^2=\sigma$），则 $V=\ker\sigma\oplus\operatorname{im}\sigma$。

**定理 5.19 (幂次核的稳定性)**  设 $\sigma\in\mathcal{L}(V,V)$，则 $\ker\sigma\subseteq\ker\sigma^2\subseteq\cdots$；若 $\dim V=n$，则 $\ker\sigma^n=\ker\sigma^{n+1}=\cdots$。

**定理 5.20 (像与核的等价条件)**  设 $\sigma\in\mathcal{L}(V,V)$，则以下条件等价：
1. $V=\ker\sigma\oplus\operatorname{im}\sigma$；
2. $\ker\sigma\cap\operatorname{im}\sigma=\{0\}$；
3. $\ker\sigma=\ker\sigma^2$；
4. $\operatorname{im}\sigma=\operatorname{im}\sigma^2$；
5. $r(\sigma^2)=r(\sigma)$。

##### §5.9 隐含定理与补充结论

**定理 5.21 (像与核和的维数下界)**  设 $\sigma\in\mathcal{L}(V,V)$，$\dim V=n$，则
$$
\dim(\ker\sigma+\operatorname{im}\sigma)\ge \frac{n}{2},
$$
且等号成立当且仅当 $\ker\sigma=\operatorname{im}\sigma$。

**定理 5.22 (线性映射的秩不等式)**  设 $\sigma\in\mathcal{L}(V_1,V_2)$，$\tau\in\mathcal{L}(V_2,V_3)$，且 $\dim V_1=m$、$\dim V_2=n$、$\dim V_3=s$，则
$$
r(\sigma)+r(\tau)-n\le r(\tau\sigma)\le\min\{r(\sigma),r(\tau)\}.
$$

**定理 5.23 (和映射的秩不等式)**  设 $\sigma,\tau\in\mathcal{L}(V_1,V_2)$，则
$$
r(\sigma+\tau)\le r(\sigma)+r(\tau).
$$

**定理 5.24 (幂零变换的像维数上界)**  设 $\sigma\in\mathcal{L}(V,V)$ 且 $\sigma^2=0$，$\dim V=n$，则
$$
\dim\operatorname{im}\sigma\le \frac{n}{2}.
$$

---

#### 第6章 对偶空间

##### §6.1 对偶空间与对偶映射

**定义 6.1 (线性泛函)**  线性映射 $f:V\to\mathbf{F}$ 称为 $V$ 上的线性泛函。

**引理 6.1 (线性泛函与超平面唯一性)**  若 $\{x\mid f(x)=1\}$ 与 $\{x\mid g(x)=1\}$ 表示同一超平面，则 $f=g$。

**定义 6.2 (对偶空间)**  $V$ 上全体线性泛函的集合 $\mathcal{L}(V,\mathbf{F})$ 构成线性空间，记作 $V^*$。

**定义 6.3 (对偶基)**  设 $B=\{e_1,\ldots,e_n\}$ 为 $V$ 的基，若 $f_i(e_j)=\delta_{ij}$，则 $\{f_1,\ldots,f_n\}$ 为 $B$ 的对偶基。

**定义 6.4 (交换图)**  以代数结构为顶点、映射为边的有向图称为图（diagram）。若任意两个顶点间的任意两条有向路径的复合结果相同，则称该图为交换的（commutative）。

**定理 6.1 (有限维对偶同构)**  若 $\dim V=n$，则 $V\cong V^*$，并且对偶基是 $V^*$ 的一组基。

**定义 6.5 (对偶映射)**  给定 $f:V\to W$，定义 $f^*:W^*\to V^*$ 为 $f^*(\varphi)=\varphi\circ f$。

**定理 6.2 (对偶映射的函子性与线性)**
1. $(f\circ g)^*=g^*\circ f^*$；
2. $f^*$ 为线性映射；
3. $(f+g)^*=f^*+g^*$，$(\lambda f)^*=\lambda f^*$。

**定理 6.3 (自然同构 $V\to V^{**}$)**  若 $\dim V<\infty$，则映射 $\psi:V\to V^{**}$，$\psi(v)(\varphi)=\varphi(v)$ 为自然同构，且 $\sigma^{**}\circ\psi=\psi\circ\sigma$。

##### §6.2 零化子

**定义 6.6 (零化子)**  子空间 $U\subseteq V$ 的零化子为
$$U^0=\{\varphi\in V^*\mid \forall u\in U,\ \varphi(u)=0\}.$$

**定理 6.4 (零化子为子空间)**  $U^0$ 是 $V^*$ 的子空间。

**定理 6.5 (对偶空间维数引理)**  若 $V=U_1\oplus U_2$，则 $V^*=U_1^0\oplus U_2^0$，且 $U_1^0\cong U_2^*$、$U_2^0\cong U_1^*$。

**定理 6.6 (零化子维数)**  若 $V$ 有限维，$\dim U^0=\dim V-\dim U$。

**定理 6.7 (核与零化子的包含关系)**
1. $f\in(\ker f)^0$；
2. 若 $f\in U^0$，则 $U\subseteq\ker f$。

**定义 6.7 (公共零点集)**  设 $U\subseteq V^*$，定义
$$Z(U)=\{v\in V\mid \forall \varphi\in U,\ \varphi(v)=0\}.$$ 

**定理 6.8 (NU 性质)**
1. 若 $U\subseteq V^*$ 为子空间，则 $U=Z(U)^0$；
2. 若 $U\subseteq V$ 为子空间，则 $U=Z(U^0)$。

##### §6.3 对偶映射与零化子

**定理 6.9 (对偶映射像核关系)**  设 $\sigma\in\mathcal{L}(V,W)$ 且 $V,W$ 有限维，则
1. $\ker\sigma^*=(\operatorname{im}\sigma)^0$；
2. $\dim\ker\sigma^*=\dim\ker\sigma+\dim W-\dim V$；
3. $\dim\operatorname{im}\sigma^*=\dim\operatorname{im}\sigma$；
4. $\operatorname{im}\sigma^*=(\ker\sigma)^0$。

**推论 6.1 (单满射互换)**
1. $\sigma$ 单射 $\iff \sigma^*$ 满射；
2. $\sigma$ 满射 $\iff \sigma^*$ 单射。

##### §6.4 纤维与商空间再论

**定理 6.10 (线性泛函纤维结构)**  对线性泛函 $\varphi$ 与 $r\in\mathbf{F}$，若 $v'\in\varphi^{-1}(r)$，则
$$\varphi^{-1}(r)=v'+\ker\varphi.$$

**定理 6.11 (线性映射纤维结构)**  对线性映射 $f:V\to W$，$f^{-1}(w)=v_0+\ker f$，其中 $v_0\in f^{-1}(w)$。

**推论 6.2 (纤维与商空间维数)**  若 $f:V\to W$，则 $\dim(V/\ker f)=\dim\operatorname{im} f$。

**定理 6.12 (子空间可作为核)**  任意子空间 $W\subseteq V$ 均可表示为某线性映射的核。

**定理 6.13 ((V/W)^* 与零化子同构)**  若 $W\subseteq V$，则 $(V/W)^*\cong W^0$。

##### §6.5 隐含定理与重要结论补充

**定理 6.14 (零化子的扩张性质)**  设 $S\subseteq V$，定义 $S^0=\{\varphi\in V^*\mid \forall s\in S,\ \varphi(s)=0\}$，则：
1. $S^{00}=\operatorname{span} S$；
2. $S\subseteq T\iff T^0\subseteq S^0$；
3. 若 $U_1,U_2$ 为 $V$ 的子空间，则 $(U_1+U_2)^0=U_1^0\cap U_2^0$，$(U_1\cap U_2)^0=U_1^0+U_2^0$。

**定理 6.15 (线性泛函的核与商空间)**  设 $\varphi\in\mathcal{L}(V,\mathbf{F})$ 非零，则 $\dim V/(\ker\varphi)=1$；反之，若 $U$ 是 $V$ 的子空间且 $\dim V/U=1$，则存在 $\varphi\in\mathcal{L}(V,\mathbf{F})$ 使 $\ker\varphi=U$。

---

#### 第7章 线性映射矩阵表示与矩阵运算基础

##### §7.1 矩阵与矩阵表示

**定义 7.1 (矩阵)**  域 $\mathbf{F}$ 上 $m\times n$ 个元素排成的矩形数表称为 $m\times n$ 矩阵，记为 $(a_{ij})_{m\times n}$。

**定义 7.2 (零矩阵与单位矩阵)**  元素全为 $0$ 的矩阵为零矩阵 $O$；主对角元为 $1$、其余为 $0$ 的 $n$ 阶方阵为单位矩阵 $E_n$。

**引理 7.1 ($\mathbf{F}^n\to\mathbf{F}^m$ 的矩阵表示)**  任意线性映射 $\sigma:\mathbf{F}^n\to\mathbf{F}^m$ 都可唯一表示为 $\sigma(x)=Ax$。

**定义 7.3 (线性映射矩阵表示)**  设 $B_1=(\varepsilon_1,\ldots,\varepsilon_n)$、$B_2=(\alpha_1,\ldots,\alpha_m)$ 为基，记
$$(\sigma(\varepsilon_1),\ldots,\sigma(\varepsilon_n))=(\alpha_1,\ldots,\alpha_m)\mathbf{M}(\sigma),$$
则 $\mathbf{M}(\sigma)$ 为 $\sigma$ 在 $B_1,B_2$ 下的矩阵表示。

**定理 7.1 (线性映射与矩阵的同构)**  若 $\dim V_1=n,\dim V_2=m$，则 $\mathcal{L}(V_1,V_2)\cong\mathbf{F}^{m\times n}$，且 $\dim\mathcal{L}(V_1,V_2)=mn$。

**定理 7.2 (坐标变换公式)**  若 $\alpha$ 的坐标为 $X$、$\sigma(\alpha)$ 的坐标为 $Y$，则 $Y=\mathbf{M}(\sigma)X$。

##### §7.2 矩阵加法与数乘

**定义 7.4 (矩阵加法与数乘)**  对 $A=(a_{ij}),B=(b_{ij})$，定义
1. $A+B=(a_{ij}+b_{ij})$；
2. $\lambda A=(\lambda a_{ij})$。

**定理 7.3 (矩阵线性空间)**  $\mathbf{F}^{m\times n}$ 在上述运算下为线性空间，常用基为 $E_{ij}$。

##### §7.3 矩阵乘法

**定义 7.5 (矩阵乘法)**  若 $A=(a_{ij})_{p\times m}$、$B=(b_{ij})_{m\times n}$，定义 $C=AB=(c_{ij})_{p\times n}$，
$$c_{ij}=\sum_{k=1}^m a_{ik}b_{kj}.$$

**定理 7.4 (复合与乘法一致)**  若 $\sigma:V_1\to V_2,\tau:V_2\to V_3$，则
$$\mathbf{M}_{B_2,B_3}(\tau)\mathbf{M}_{B_1,B_2}(\sigma)=\mathbf{M}_{B_1,B_3}(\tau\sigma).$$

**定理 7.5 (乘法基本性质)**
1. 结合律 $(AB)C=A(BC)$；
2. 左右分配律 $A(B+C)=AB+AC$，$(B+C)A=BA+CA$；
3. 一般不满足交换律 $AB\ne BA$；
4. 可出现零因子且消去律一般不成立；
5. 若 $A$ 可逆，则消去律成立。

##### §7.4 矩阵多项式与特殊矩阵

**定义 7.6 (矩阵多项式)**  对方阵 $A$ 与多项式 $p(x)=\sum a_ix^i$，定义 $p(A)=\sum a_iA^i$，并约定 $A^0=E$。

**定理 7.6 (可交换条件下的多项式运算)**  若 $AB=BA$，则 $f(A)g(B)=g(B)f(A)$；特别地 $f(A)g(A)=g(A)f(A)$。

**定义 7.7 (幂等、幂零、对合矩阵)**
1. 幂等矩阵：$A^2=A$；
2. 幂零矩阵：$\exists k,\ A^k=O$；
3. 对合矩阵：$A^2=E$。

##### §7.5 逆矩阵

**定义 7.8 (逆矩阵)**  若 $A\in\mathbf{M}_n(\mathbf{F})$ 存在 $B$ 使 $AB=BA=E$，则 $B=A^{-1}$。

**定理 7.7 (逆矩阵唯一)**  可逆矩阵的逆唯一。

**定理 7.8 (单侧逆等价)**  对方阵 $A,B$，有 $AB=E\iff BA=E$，且 $A,B$ 互为逆。

**定理 7.9 (逆矩阵性质)**
1. $(AB)^{-1}=B^{-1}A^{-1}$；
2. $(\lambda A)^{-1}=\lambda^{-1}A^{-1}$；
3. $(A^k)^{-1}=(A^{-1})^k$。

**方法 7.1 (增广矩阵求逆)**  行变换 $(A\mid E)\to(E\mid A^{-1})$。

**定义 7.9 (Moore-Penrose 广义逆)**  对任意 $A$，存在唯一 $A^\dagger$ 使 $AXA=A$、$XAX=X$ 且 $AX, XA$ 共轭对称。

##### §7.6 转置与对称矩阵

**定义 7.10 (转置)**  $A^\mathrm{T}$ 为 $A$ 的行列互换矩阵。

**定理 7.10 (转置性质)**
1. $(A^\mathrm{T})^\mathrm{T}=A$；
2. $(A+B)^\mathrm{T}=A^\mathrm{T}+B^\mathrm{T}$；
3. $(\lambda A)^\mathrm{T}=\lambda A^\mathrm{T}$；
4. $(AB)^\mathrm{T}=B^\mathrm{T}A^\mathrm{T}$；
5. $(A^\mathrm{T})^{-1}=(A^{-1})^\mathrm{T}$。

**定义 7.11 (对称矩阵与反对称矩阵)**  $A=A^\mathrm{T}$ 为对称矩阵，$A=-A^\mathrm{T}$ 为反对称矩阵。

**定理 7.11 (对称与反对称性质)**
1. 反对称矩阵主对角元为 $0$；
2. $AA^\mathrm{T}$ 与 $A^\mathrm{T}A$ 为对称矩阵；
3. 可逆的对称（反对称）矩阵的逆仍对称（反对称）；
4. $\mathbf{M}_n(\mathbf{F})=\text{Sym}_n\oplus\text{Skew}_n$。

**定理 7.12 (对偶映射矩阵表示)**  若 $\sigma$ 在基 $B_1,B_2$ 下矩阵为 $A$，则 $\sigma^*$ 在对偶基下矩阵为 $A^\mathrm{T}$。

##### §7.7 共轭矩阵

**定义 7.12 (共轭矩阵)**  复矩阵 $A=(a_{ij})$ 的共轭矩阵为 $\overline{A}=(\overline{a_{ij}})$。

**定理 7.13 (共轭运算性质)**
1. $\overline{A+B}=\overline{A}+\overline{B}$；
2. $\overline{\lambda A}=\overline{\lambda}\,\overline{A}$；
3. $\overline{AB}=\overline{A}\,\overline{B}$；
4. $\overline{A^\mathrm{T}}=(\overline{A})^\mathrm{T}$；
5. $\overline{A^{-1}}=(\overline{A})^{-1}$。

##### §7.8 分块矩阵

**定义 7.13 (分块矩阵)**  将矩阵按行列分块得到 $A=(A_{kl})$，称为分块矩阵。

**定理 7.14 (分块矩阵运算)**
1. 加法与数乘按对应分块进行；
2. 乘法按分块矩阵乘法规则计算；
3. 转置需对大块与小块同时转置；
4. 共轭按分块共轭。

**定理 7.15 (分块对角与三角矩阵求逆)**
1. $\operatorname{diag}(A_1,\ldots,A_s)$ 可逆 $\iff$ 各 $A_i$ 可逆，且逆为 $\operatorname{diag}(A_1^{-1},\ldots,A_s^{-1})$；
2. 若 $A=\begin{pmatrix}B & O\\ C & D\end{pmatrix}$ 且 $B,D$ 可逆，则
$$A^{-1}=\begin{pmatrix}B^{-1} & O\\ -D^{-1}CB^{-1} & D^{-1}\end{pmatrix}.$$

##### §7.9 补充定理与注意事项

**隐含定理 7.1 (线性映射矩阵表示的坐标关系)**  若线性映射 $\sigma$ 在基 $B_1,B_2$ 下矩阵为 $A$，向量 $\alpha$ 与 $\sigma(\alpha)$ 在相应基下坐标为 $X,Y$，则 $Y=AX$。

**隐含定理 7.2 (矩阵乘法的行列组合性质)**  设 $C=AB$，则：
1. $C$ 的第 $j$ 列是 $A$ 的各列以 $B$ 的第 $j$ 列为系数的线性组合；
2. $C$ 的第 $i$ 行是 $B$ 的各行以 $A$ 的第 $i$ 行为系数的线性组合。

**隐含定理 7.3 (矩阵乘法与基变换的结合律)**  设 $\sigma$ 为线性映射，$(\varepsilon_1,\ldots,\varepsilon_n)$ 为一组基向量构成的形式行向量，$B$ 为矩阵，则
$$
\sigma((\varepsilon_1,\ldots,\varepsilon_n)B)=(\sigma(\varepsilon_1),\ldots,\sigma(\varepsilon_n))B.
$$

**隐含定理 7.4 (线性方程组与线性映射的关联)**  设线性映射 $\sigma\in\mathcal{L}(V_1,V_2)$ 在基 $B_1,B_2$ 下矩阵为 $A$。线性方程组 $AX=b$ 的解 $X$ 对应向量 $\alpha\in V_1$ 在基 $B_1$ 下的坐标，使得 $\sigma(\alpha)=\beta$，其中 $\beta$ 在基 $B_2$ 下的坐标为 $b$；齐次方程组 $AX=0$ 的解空间对应于 $\ker\sigma$。

**隐含定理 7.9 (线性映射的像与核的矩阵求法)**  设线性映射 $\sigma\in\mathcal{L}(V_1,V_2)$ 在基 $B_1,B_2$ 下的矩阵为 $A$：
1. $\operatorname{im}\sigma=\operatorname{span}\{\sigma(B_1)\}$，其维数等于 $A$ 的列秩；
2. $\ker\sigma$ 中向量在基 $B_1$ 下的坐标构成齐次线性方程组 $AX=0$ 的解空间。

**隐含定理 7.10 (矩阵求幂的技巧：秩 1 矩阵)**  设 $\alpha,\beta$ 为 $n$ 维列向量，$A=\alpha\beta^\mathrm{T}$，则
$$
A^k=(\beta^\mathrm{T}\alpha)^{k-1}A.
$$

**隐含定理 7.11 (矩阵多项式与相似变换)**  若 $A=PBP^{-1}$，$f$ 为多项式，则
$$
f(A)=Pf(B)P^{-1}.
$$

**隐含定理 7.12 (行和与列和的性质)**  设 $A$ 的每行元素之和为常数 $k$，记 $\alpha=(1,1,\ldots,1)^\mathrm{T}$，则 $A\alpha=k\alpha$；若 $A$ 可逆，则 $A^{-1}$ 的每行元素之和为 $1/k$，且 $A^m$ 的每行元素之和为 $k^m$。

---

#### 第8章 相抵标准形

##### §8.1 矩阵的秩

**定义 8.1 (矩阵秩/行秩/列秩)**  设 $A$ 为线性映射的矩阵表示，定义 $r(A)=r(\sigma)$；行向量组的秩为行秩，列向量组的秩为列秩。

**定理 8.1 (秩=行秩=列秩)**  对任意矩阵 $A$，有 $r(A)=r_{\mathrm{r}}(A)=r_{\mathrm{c}}(A)$，且 $r(A)=r(A^\mathrm{T})$。

**注 8.1**  证明通常先证矩阵秩等于列秩，再由转置得到行秩等于列秩；这也是相抵标准形、初等变换与后续行秩理论的衔接点。

**定理 8.2 (单满射与行列秩)**  线性映射是单射 $\iff$ 其矩阵为列满秩；线性映射是满射 $\iff$ 其矩阵为行满秩。

**定理 8.3 (可逆等价条件)**  对 $A\in\mathbf{M}_n(\mathbf{F})$，以下等价：
1. $A$ 可逆；
2. $r(A)=n$；
3. $A$ 的 $n$ 个行（列）向量线性无关；
4. $AX=0$ 只有零解。

**隐含定理 (对角占优矩阵可逆性)**  若 $A=(a_{ij})_{n\times n}$ 满足 $|a_{ii}|>\sum_{j\ne i}|a_{ij}|$，则 $A$ 可逆。

##### §8.2 过渡矩阵与基变换

**定义 8.2 (过渡矩阵)**  设 $B_1,B_2$ 为同一线性空间的两组基，若 $B_2=B_1A$，则 $A$ 为 $B_1$ 到 $B_2$ 的过渡矩阵。

**定理 8.2.1 (过渡性质 1)**  设 $S_1=(\alpha_1,\ldots,\alpha_n)$ 线性无关，且 $(\beta_1,\ldots,\beta_s)=S_1A$，则向量组 $(\beta_1,\ldots,\beta_s)$ 的秩等于矩阵 $A$ 的秩。

**定理 8.2.2 (可逆过渡矩阵保等价)**  若向量组 $S_2=S_1A$ 且 $A$ 可逆，则 $S_1$ 与 $S_2$ 等价。

**定理 8.4 (过渡矩阵可逆)**  过渡矩阵必可逆，且 $B_2$ 到 $B_1$ 的过渡矩阵为 $A^{-1}$。

**定理 8.5 (坐标变换公式)**  若 $\xi$ 在 $B_1,B_2$ 下坐标分别为 $X,Y$，且 $B_2=B_1A$，则 $Y=A^{-1}X$。

**定理 8.6 (换基公式)**  若 $\sigma\in\mathcal{L}(V_1,V_2)$，$P$ 为 $B_1\to B_1'$ 过渡矩阵，$Q$ 为 $B_2\to B_2'$ 过渡矩阵，则
$\mathbf{M}_{B_1',B_2'}(\sigma)=Q^{-1}\mathbf{M}_{B_1,B_2}(\sigma)P$。

**定理 8.7 (相似变换)**  若 $\sigma\in\mathcal{L}(V,V)$ 在基 $B_1,B_2$ 下矩阵为 $A,B$，过渡矩阵为 $C$，则 $B=C^{-1}AC$。

**隐含定理 (向量组等价性判定)**  若两个向量组 $S_2=S_1A$ 且 $A$ 可逆，则 $S_1$ 与 $S_2$ 等价。

##### §8.3 相抵标准形

**定义 8.3 (相抵)**  若存在可逆矩阵 $P,Q$ 使 $PAQ=B$，则 $A$ 与 $B$ 相抵。

**定理 8.8 (相抵标准形)**  $A$ 为 $m\times n$ 矩阵，$r(A)=r$ 当且仅当存在可逆 $P,Q$ 使
$PAQ=\begin{pmatrix}E_r & O \\ O & O\end{pmatrix}$。

**引理 8.3.1 (矩阵行秩=列秩的第三种证明)**  利用相抵标准形与转置，可证明矩阵的行秩等于列秩。

**定理 8.9 (相抵判别)**  $A$ 与 $B$ 相抵 $\iff r(A)=r(B)$。

##### §8.4 初等矩阵

**定义 8.4 (初等矩阵)**  由单位矩阵经一次初等行（列）变换得到的矩阵称初等矩阵。

**定理 8.10 (初等矩阵与初等变换)**  左乘初等矩阵等价于对应行变换；右乘初等矩阵等价于对应列变换。

**定理 8.11 (初等矩阵分解)**  初等矩阵均可逆，其逆仍为初等矩阵；任意可逆矩阵可表示为初等矩阵乘积。

**引理 8.4.2 (初等变换求逆矩阵)**  若对 $(A\mid E)$ 作一系列初等行变换将 $A$ 化为 $E$，则同时 $E$ 被化为 $A^{-1}$。

**定理 8.12 (秩不变性)**  初等行列变换不改变矩阵秩，等价地 $r(PAQ)=r(A)$（$P,Q$ 可逆）。

##### §8.5 相抵标准形应用

**定理 8.5.1 (相抵标准形的矩阵角度证明)**  利用初等行列变换与秩不变性，可证明存在 $P,Q$ 使 $PAQ$ 为相抵标准形。

**定义 8.5.1 (相抵的等价定义)**  两个矩阵相抵当且仅当它们可以通过一系列初等行变换与列变换互相转化。

**隐含定理 (初等变换与基变换的关系)**  对线性映射的表示矩阵做初等行（列）变换，等价于对目标空间（出发空间）的基做相应的初等变换。

**定理 8.13 (满秩矩阵的左右逆)**
1. 若 $A$ 列满秩，则存在 $B$ 使 $BA=E$；
2. 若 $A$ 行满秩，则存在 $C$ 使 $AC=E$。

**定理 8.14 (秩分解)**  若 $r(A)=r$，则存在满列秩 $B$ 与满行秩 $C$ 使 $A=BC$。

**方法 8.1 (求相抵标准形)**  对 $A$ 施行行列初等变换化为 $\operatorname{diag}(E_r,0)$，并记录对应的 $P,Q$。

**方法 8.2 (相抵标准形的算法化表述)**  先作初等行变换化到行简化阶梯形，再作初等列变换化到 $U_r$；同时累积行、列变换矩阵乘积，即可得到 $PAQ=U_r$。

##### §8.6 重要补充与说明

**定义 8.6.1 (迹)**  设 $A=(a_{ij})_{n\times n}$，其主对角元之和称为 $A$ 的迹，记作 $\operatorname{tr}(A)=\sum_{i=1}^n a_{ii}$。

**隐含定理 (矩阵添加行列对秩的影响)**  矩阵添加一列（或一行），其秩不变或增加 $1$。

**隐含定理 (分块矩阵的秩不等式)**  设 $A$ 是 $s\times n$ 矩阵，$B$ 是 $A$ 前 $m$ 行构成的 $m\times n$ 矩阵，则
$$
r(B)\ge r(A)+m-s.
$$

**隐含定理 (线性相关性的循环判定)**  当 $n$ 为奇数时，向量组 $\alpha_1,\alpha_2,\ldots,\alpha_n$ 线性无关当且仅当
$$
\alpha_1+\alpha_2,\ \alpha_2+\alpha_3,\ \ldots,\ \alpha_n+\alpha_1
$$
线性无关。

---

#### 第9章 矩阵运算进阶

##### §9.1 特殊矩阵

**定义 9.1 (对角与分块对角矩阵)**  $\operatorname{diag}(d_1,\ldots,d_n)$ 为对角矩阵；$\operatorname{diag}(A_1,\ldots,A_s)$ 为分块对角矩阵（亦称准对角矩阵）。

**定理 9.1 (对角矩阵乘法与可逆性)**
1. 右乘对角矩阵相当于按列缩放，左乘对角矩阵相当于按行缩放；
2. $\operatorname{diag}(d_1,\ldots,d_n)$ 可逆 $\iff d_i\ne0$，且逆为 $\operatorname{diag}(d_1^{-1},\ldots,d_n^{-1})$；
3. 两个对角矩阵乘积仍为对角矩阵，且 $\operatorname{diag}(a_i)\operatorname{diag}(b_i)=\operatorname{diag}(a_ib_i)$。

**定理 9.2 (分块对角矩阵性质)**  $\operatorname{diag}(A_1,\ldots,A_s)$ 可逆 $\iff$ 各 $A_i$ 可逆，且逆为 $\operatorname{diag}(A_1^{-1},\ldots,A_s^{-1})$。

**定理 9.3 (上三角矩阵性质)**
1. 上三角矩阵的转置为下三角矩阵；
2. 上三角矩阵的乘积仍为上三角矩阵；
3. 上三角矩阵可逆 $\iff$ 主对角元全非零，且逆仍为上三角矩阵。

**定义 9.2 (自然基)**  $\mathbf{R}^n$ 中自然基 $e_i$ 为第 $i$ 个分量为 $1$、其余为 $0$ 的列向量。

**定义 9.3 (基本矩阵)**  $E_{ij}$ 表示第 $i$ 行第 $j$ 列为 $1$、其余为 $0$ 的矩阵。

**定理 9.4 (自然基与基本矩阵运算)**
1. $e_i^\mathrm{T}e_j=\delta_{ij}$；
2. $Ae_j$ 为第 $j$ 列，$f_i^\mathrm{T}A$ 为第 $i$ 行；
3. $E_{ik}E_{lj}=\delta_{kl}E_{ij}$；
4. $E_{ij}A$ 的结果是将 $A$ 的第 $j$ 行移到第 $i$ 行，其余为零；
5. $E_{ij}AE_{kl}=a_{jk}E_{il}$。

##### §9.2 矩阵可交换问题

**方法 9.1 (平移简化法)**  选取 $t$ 使 $AB=BA \iff (A-tE)B=B(A-tE)$，便于计算。

**定理 9.2.1 (可交换矩阵的一般形式)**  若 $B$ 与 $A$ 可交换，则在特定条件下（如 $A$ 为循环矩阵），$B$ 可表示为关于 $A$ 的多项式。

**定理 9.5 (可交换矩阵的结构刻画)**
1. 与主对角元两两不同的对角矩阵可交换的矩阵必为对角矩阵；
2. 与分块对角且分块标量不同的矩阵可交换者必为同分块对角；
3. 与所有可逆矩阵可交换 $\iff$ 为数量矩阵；
4. 与所有矩阵可交换 $\iff$ 为数量矩阵。

##### §9.3 矩阵的迹

**定理 9.6 (迹的性质)**  对方阵 $A,B$，有
1. $\operatorname{tr}(A+B)=\operatorname{tr}(A)+\operatorname{tr}(B)$；
2. $\operatorname{tr}(kA)=k\operatorname{tr}(A)$；
3. $\operatorname{tr}(A^\mathrm{T})=\operatorname{tr}(A)$；
4. $\operatorname{tr}(AB)=\operatorname{tr}(BA)$。

**定理 9.3.2 (迹与对称矩阵的关系)**  设 $A$ 为 $n$ 阶实矩阵，则
$$
\operatorname{tr}(A^2)\le \operatorname{tr}(A^\mathrm{T}A),
$$
且等号成立当且仅当 $A$ 为对称矩阵。

**推论 9.1 (迹的正定性)**
1. 若 $A$ 为实矩阵，则 $\operatorname{tr}(A^\mathrm{T}A)\ge0$，且等号当且仅当 $A=O$；
2. 若 $A$ 为复矩阵，则 $\operatorname{tr}(\overline{A^\mathrm{T}}A)\ge0$，且等号当且仅当 $A=O$。

##### §9.4 逆矩阵进阶求法

**方法 9.2 (凑因子法)**  通过构造因式分解使 $AB=kE$，从而 $A^{-1}=k^{-1}B$。

**定理 9.4.1 (幂零矩阵的可逆性)**  若 $A^k=O$，则 $E\pm A$ 可逆，且
$$
(E+A)^{-1}=E-A+A^2-\cdots+(-A)^{k-1},\quad (E-A)^{-1}=E+A+\cdots+A^{k-1}.
$$

**定理 9.7 (可逆性互换与逆公式)**  若 $E_n\pm AB$ 可逆，则 $E_m\pm BA$ 可逆，且
$(E_m\pm BA)^{-1}=E_m\mp B(E_n\pm AB)^{-1}A$。

**定理 9.8 (Sherman-Morrison-Woodbury)**  若 $A$ 可逆且 $R^{-1}+YA^{-1}X$ 可逆，则
$(A+XRY)^{-1}=A^{-1}-A^{-1}X(R^{-1}+YA^{-1}X)^{-1}YA^{-1}$。

**方法 9.3 (分式思想)**  当 $A^k=O$ 时，$(E-A)^{-1}=E+A+\cdots+A^{k-1}$。

**方法 9.4 (提逆思想)**  通过提取可逆因子将 $(E-A^{-1})^{-1}$ 化为 $(A-E)^{-1}A$ 等形式。

**定理 9.4.5 (提逆恒等式)**  若 $E-A$、$E+A$、$A$ 均可逆，则
$$
(E-A^{-1})^{-1}+(E-A)^{-1}=E.
$$

##### §9.5 矩阵的幂

**定理 9.5.1 (幂的计算：找规律)**  若存在可逆矩阵 $P$ 使 $A=PDP^{-1}$，则 $A^n=PD^nP^{-1}$；特别地，对角矩阵 $D$ 的幂可直接逐项求得。

**定理 9.9 (幂零三角矩阵)**  上（下）三角矩阵若主对角元全为 $0$，则 $A^n=O$。

**定理 9.10 (循环与若当块幂公式)**  基础循环矩阵与若当块矩阵的幂可用移位规律求得。若
$$
A=(e_n,e_1,e_2,\ldots,e_{n-1}),
$$
则对 $1\le k\le n$，有
$$
A^k=\begin{pmatrix}O & E_{n-k}\\ E_k & O\end{pmatrix}.
$$

**定理 9.11 (秩 1 矩阵幂)**  若 $r(M)=1$，则 $M^k=(\operatorname{tr} M)^{k-1}M$。

**定理 9.5.5 (秩 1 矩阵的多项式幂)**  设 $M$ 为秩 $1$ 矩阵且 $\operatorname{tr}(M)=b$，则对任意 $a$ 与正整数 $n$，有
$$
(aE+M)^n=
\begin{cases}
a^nE+na^{n-1}M, & b=0,\\
a^nE+\dfrac{(a+b)^n-a^n}{b}M, & b\ne0.
\end{cases}
$$

##### §9.6 分块矩阵初等变换（打洞法）

**定义 9.4 (分块初等变换)**  对分块矩阵进行交换分块行列、分块倍乘、分块倍加的操作。

**定义 9.4.1 (分块初等矩阵)**  对分块单位矩阵作一次分块初等变换得到的矩阵称为分块初等矩阵。

**引理 9.6.1 (Schur 补恒等式)**  若 $A$ 可逆，则
$$
\begin{pmatrix}E & O\\ -CA^{-1} & E\end{pmatrix}
\begin{pmatrix}A & B\\ C & D\end{pmatrix}
=\begin{pmatrix}A & B\\ O & D-CA^{-1}B\end{pmatrix}.
$$

**定理 9.12 (Schur 补打洞法)**  若 $A$ 可逆，则
$\begin{pmatrix}A & B \\ C & D\end{pmatrix}$ 可经分块初等变换化为 $\operatorname{diag}(A,\ D-CA^{-1}B)$。

**定理 9.13 (分块逆矩阵公式)**  若 $D$ 与 $A-BD^{-1}C$ 可逆，则
$\begin{pmatrix}A & B \\ C & D\end{pmatrix}^{-1}=\begin{pmatrix}(A-BD^{-1}C)^{-1} & -(A-BD^{-1}C)^{-1}BD^{-1} \\ -D^{-1}C(A-BD^{-1}C)^{-1} & D^{-1}+D^{-1}C(A-BD^{-1}C)^{-1}BD^{-1}\end{pmatrix}$。

**定理 9.14 (分块可逆性等价)**  $E\pm AB$ 可逆 $\iff E\pm BA$ 可逆；$E_m+CA^{-1}B$ 可逆 $\iff A+BC$ 可逆。

**定理 9.15 (LU 分解条件)**  若各阶顺序主子式可逆，则存在 $A=LU$，其中 $L$ 为单位下三角，$U$ 为上三角。

**定理 9.15.1 (LU 分解解方程组)**  若 $A=LU$，则 $Ax=b$ 可先解 $Ly=b$ 再解 $Ux=y$。

##### §9.7 矩阵方程

**定理 9.16 (矩阵方程求解公式)**  $AX=B\Rightarrow X=A^{-1}B$，$XA=B\Rightarrow X=BA^{-1}$，$AXB=C\Rightarrow X=A^{-1}CB^{-1}$。

**定理 9.7.2 (矩阵方程的化简)**  若矩阵方程可化为 $(A-B)X(A-B)=A(A-B)$ 且 $A-B$ 可逆，则 $X=(A-B)^{-1}A$。

**方法 9.5 (增广矩阵求解)**  通过对 $(A\mid B)$ 做初等行变换得到 $(E\mid A^{-1}B)$；对 $\begin{pmatrix}A\\ B\end{pmatrix}$ 做初等列变换得到 $\begin{pmatrix}E\\ BA^{-1}\end{pmatrix}$。

##### §9.8 秩等式与不等式

**定理 9.17 (秩不变性)**  若 $P,Q$ 可逆，则 $r(PAQ)=r(A)$。

**定理 9.18 (分块矩阵秩不等式)**
1. $r\begin{pmatrix}A & O\\ O & B\end{pmatrix}=r(A)+r(B)$；
2. $r(A)+r(B)\le r\begin{pmatrix}A & D\\ O & B\end{pmatrix}\le r(A)+r(B)+r(D)$；
3. $r(A)+r(B)\le r\begin{pmatrix}A & O\\ C & B\end{pmatrix}\le r(A)+r(B)+r(C)$。

**定理 9.19 (加法与乘法秩不等式)**
1. $|r(A)-r(B)|\le r(A\pm B)\le r(A)+r(B)$；
2. $r(AB)\le\min\{r(A),r(B)\}$。

**定理 9.20 (转置与乘积秩)**  $r(A)=r(A^\mathrm{T})=r(AA^\mathrm{T})=r(A^\mathrm{T}A)$（实矩阵）。

**定理 9.21 (Sylvester 不等式)**  若 $A\in\mathbf{F}^{s\times n},B\in\mathbf{F}^{n\times m}$，则 $r(AB)\ge r(A)+r(B)-n$。

**定理 9.22 (Frobenius 不等式)**  $r(ABC)\ge r(AB)+r(BC)-r(B)$。

**定理 9.8.7 (秩的递推稳定性)**  若存在正整数 $m$ 使 $r(A^m)=r(A^{m+1})$，则对任意 $k\ge m$，有 $r(A^k)=r(A^m)$；特别地，对 $n$ 阶矩阵 $A$，必有 $r(A^n)=r(A^{n+1})=\cdots$。

---

#### 第10章 行列式

##### §10.1 公理化定义与基本性质

**定义 10.1 (行列式的公理化定义)**  行列式 $D(\alpha_1,\ldots,\alpha_n)$ 为对列向量的函数，满足线性性、反对称性与规范性 $D(e_1,\ldots,e_n)=1$。

**定理 10.1 (公理化定义的直接推论)**
1. 有零列或两列相同则行列式为 $0$；
2. 两列成比例则行列式为 $0$；
3. 倍加列变换不改变行列式。

##### §10.2 逆序数与排列展开

**定义 10.2 (逆序数)**  排列 $(k_1,\ldots,k_n)$ 中 $i<j$ 且 $k_i>k_j$ 的对数为逆序数 $\tau$。

**定义 10.3 (奇偶排列)**  逆序数为偶数称偶排列，为奇数称奇排列。

**定理 10.2 (行列式的逆序数定义)**
$|A|=\sum_{(k_1,\ldots,k_n)\in S_n}(-1)^{\tau(k_1,\ldots,k_n)}a_{k_11}\cdots a_{k_nn}$。

**引理 10.1 (逆序数与对换次数)**  排列与常序排列之间的相邻对换次数等于其逆序数。

##### §10.3 递归式与 Laplace 展开

**定义 10.4 (余子式与代数余子式)**  去掉第 $i$ 行第 $j$ 列得到 $M_{ij}$，代数余子式 $A_{ij}=(-1)^{i+j}M_{ij}$。

**定义 10.5 (递归式定义)**  $|A|=\sum_k a_{kj}A_{kj}$（按列展开）或 $|A|=\sum_k a_{ik}A_{ik}$（按行展开）。

**定理 10.3 (递归性质)**  若 $i\ne j$，则 $\sum_k a_{kj}A_{ki}=0$ 且 $\sum_k a_{jk}A_{ik}=0$。

**定理 10.4 (Laplace 定理)**  按任意 $k$ 行或 $k$ 列展开，$|A|$ 等于所有 $k$ 阶子式与其代数余子式乘积之和。

##### §10.4 行列式基本性质

**定理 10.5 (行列式性质汇总)**
1. $|kA|=k^n|A|$；
2. 初等行列变换的行列式为：对换 $-1$、倍乘为倍数、倍加为 $1$；
3. $|AB|=|A||B|$，$|A^k|=|A|^k$；
4. $A$ 可逆 $\iff |A|\ne0$，且 $|A^{-1}|=|A|^{-1}$；
5. $|A^\mathrm{T}|=|A|$；
6. 上下三角矩阵行列式为对角线乘积。

##### §10.5 分块矩阵与打洞法

**定义 10.6 (分块初等矩阵)**  对分块单位矩阵作分块行列初等变换得到的矩阵。

**定理 10.6 (分块初等矩阵行列式)**
1. 分块对换矩阵的行列式为 $(-1)^{k_ik_j+(k_i+k_j)M}$；
2. 分块倍乘矩阵行列式为对应块的行列式；
3. 分块倍加矩阵行列式为 $1$。

**定理 10.7 (Schur 补行列式公式)**  若 $A$ 可逆，则
$\left|\begin{pmatrix}A & B \\ C & D\end{pmatrix}\right|=|A|\,|D-CA^{-1}B|$；若 $D$ 可逆，则
$\left|\begin{pmatrix}A & B \\ C & D\end{pmatrix}\right|=|D|\,|A-BD^{-1}C|$。

##### §10.6 伴随矩阵

**定义 10.7 (伴随矩阵)**  以代数余子式转置排列得到 $A^*$。

**定理 10.8 (伴随矩阵性质)**
1. $AA^*=A^*A=|A|E$；
2. 若 $|A|\ne0$，则 $A^{-1}=|A|^{-1}A^*$；
3. $|A^*|=|A|^{n-1}$；
4. $(AB)^*=B^*A^*$，$(A^\mathrm{T})^*=(A^*)^\mathrm{T}$，$(kA)^*=k^{n-1}A^*$；
5. 若 $A$ 可逆，则 $(A^*)^*=|A|^{n-2}A$，且 $|(A^*)^*|=|A|^{(n-1)^2}$；
6. 对正整数 $k$，$(A^k)^*=(A^*)^k$；
7. 伴随矩阵的秩满足
$$
r(A^*)=
\begin{cases}
n,& r(A)=n,\\
1,& r(A)=n-1,\\
0,& r(A)<n-1.
\end{cases}
$$

##### §10.7 行列式秩

**定义 10.8 (子式、主子式、顺序主子式)**  取 $k$ 行 $k$ 列得到 $k$ 阶子式；行列号相同为主子式；取前 $k$ 行列为顺序主子式。

**定义 10.9 (行列式秩)**  非零子式的最高阶数称为行列式秩。

**定理 10.9 (秩等于行列式秩)**  矩阵秩 $r(A)$ 等于其行列式秩。

##### §10.8 特殊行列式与计算技巧

**定义 10.10 (范德蒙行列式)**  $V_n=\det(x_i^{j-1})_{n\times n}$。

**定理 10.10 (范德蒙公式)**  $V_n=\prod_{1\le i<j\le n}(x_j-x_i)$，故 $V_n\ne0 \iff x_i$ 两两不同。

**方法 10.1 (行列式降阶/升阶技巧)**  常用递归展开、Laplace 展开、连加法、滚动消去、升阶法与硬拆法化简。

##### §10.9 Cauchy-Binet 公式

**定理 10.11 (Cauchy-Binet 公式)**  若 $A\in\mathbf{F}^{m\times n},B\in\mathbf{F}^{n\times m}$，则
1. $m>n$ 时 $|AB|=0$；
2. $m\le n$ 时 $|AB|=\sum A\begin{pmatrix}1\cdots m\\ j_1\cdots j_m\end{pmatrix}B\begin{pmatrix}j_1\cdots j_m\\ 1\cdots m\end{pmatrix}$。

**定理 10.12 (Cauchy-Binet 公式推广)**  设 $A=(a_{ij})$ 是 $m\times n$ 矩阵，$B=(b_{ij})$ 是 $n\times m$ 矩阵，$r$ 是正整数且 $r\le m$。则：
1. 若 $r>n$，则 $AB$ 的任意一个 $r$ 阶子式等于 $0$；
2. 若 $r\le n$，则对任意 $r$ 阶子式有
$$
AB\begin{pmatrix}
 i_1 & i_2 & \cdots & i_r \\
 j_1 & j_2 & \cdots & j_r
\end{pmatrix}
=\sum_{1\le k_1<k_2<\cdots<k_r\le n}
A\begin{pmatrix}
 i_1 & i_2 & \cdots & i_r \\
 k_1 & k_2 & \cdots & k_r
\end{pmatrix}
B\begin{pmatrix}
 k_1 & k_2 & \cdots & k_r \\
 j_1 & j_2 & \cdots & j_r
\end{pmatrix}.
$$

**推论 10.1 (主子式非负)**  设 $A$ 是 $m\times n$ 实矩阵，则矩阵 $AA^{\mathrm{T}}$ 的任一主子式都非负。

---

#### 第11章 朝花夕拾

##### §11.1 线性方程组解的一般理论

**定理 11.1 (有解条件)**  线性方程组有解 $\iff$ 系数矩阵与增广矩阵秩相同。

**定理 11.2 (解的唯一性与无穷性)**  在有解前提下：
1. 若 $r(A)=n$，则唯一解；
2. 若 $r(A)<n$，则有无穷多解。

**定理 11.3 (Cramer 法则)**  对方阵方程组 $AX=b$，设 $D=|A|$，$D_i$ 为用 $b$ 替换第 $i$ 列得到的行列式，则
1. $D\ne0$ $\iff$ 唯一解且 $x_i=D_i/D$；
2. $D=0$ 时方程组无解或有无穷多解。

##### §11.2 齐次与非齐次结构

**定理 11.4 (齐次解空间是子空间)**  齐次方程组 $AX=0$ 的解集为线性子空间。

**定理 11.5 (齐次解空间维数)**  若 $A\in\mathbf{M}_{m\times n}$，$r(A)=r$，则 $\dim N(A)=n-r$，且基础解系构成 $N(A)$ 的一组基。

**定理 11.6 (通解加特解结构)**  若非齐次方程组 $AX=b$ 有解，则其解集为 $X_0+N(A)$（特解 $X_0$ 加齐次解空间）。

**定理 11.7 (非齐次解的线性无关数上界)**  若 $r(A)=r$ 且 $AX=b$ 有解，则至多有 $n-r+1$ 个线性无关解向量。

##### §11.3 几何解释

**引理 11.1 (仿射子集交仍为仿射)**  若仿射子集交非空，则其交仍为仿射子集。

**定理 11.8 (解集的仿射表示)**  线性方程组解集可表示为
$\bigcap_i\varphi_i^{-1}(b_i)=v_0+\bigcap_i\ker\varphi_i$，其维数由相应线性泛函组的秩决定。

##### §11.4 理论应用

**定理 11.9 (由解空间得到的秩结论)**
1. $r(AB)\le\min\{r(A),r(B)\}$；
2. 若 $AB=O$，则 $r(A)+r(B)\le n$；
3. 对实矩阵 $A$，有 $r(A^\mathrm{T}A)=r(AA^\mathrm{T})=r(A)$；
4. $A^2=A\iff r(A)+r(E-A)=n$。

**性质 11.10 (多项式插值唯一性)**  给定 $n$ 个互不相同的点 $(a_i,b_i)$，存在唯一的 $n-1$ 次多项式 $f(x)$，使得 $f(a_i)=b_i$。

---

#### 第12章 史海拾遗

##### §12.1 初等代数与丢番图

**定义 12.1 (丢番图方程)**  形如 $a_1x_1^{b_1}+\cdots+a_nx_n^{b_n}=c$ 的整数系数方程。

**定理 12.1 (费马大定理)**  $x^n+y^n=z^n$ 在 $n>2$ 时无正整数解。

##### §12.2 现代矩阵多项式与正定性

**定义 12.2 (矩阵单项式/多项式)**  由矩阵变元及其转置的有限乘积与有限和构成。

**定义 12.3 (矩阵多项式值域)**  $\operatorname{im} Q=\bigcup_{m\ge1}\{Q(A_1,\ldots,A_n)\mid A_i\in\mathbf{M}_m(\mathbf{R})\}$。

**定义 12.4 (对称与半正定矩阵多项式)**  $\operatorname{im} Q$ 中矩阵全对称/半正定则称 $Q$ 对称/半正定。

**定义 12.5 (矩阵多项式平方和)**  形如 $\sum_i h_i(x)h_i^\mathrm{T}(x)$。

**定理 12.2 (Helton, 2002)**  对称矩阵多项式半正定 $\iff$ 可表示为平方和。

**定义 12.6 (迹度量距离)**  对正定矩阵 $A,B$，$\delta(A,B)=\sqrt{\sum_i \log^2\lambda_i(A^{-1}B)}$。

**定义 12.7 (Karcher 均值)**  使得到 $A_i$ 的迹度量距离平方和最小的正定矩阵。

**定理 12.3 (Bhatia-Holbrook, Lawson-Lim 单调性)**  若 $A_i\le B_i$，则 $\sigma(A_1,\ldots,A_n)\le\sigma(B_1,\ldots,B_n)$。

**定义 12.8 (谱半径)**  $\rho(A)=\max\{|\lambda|\mid \lambda\in\text{spec}(A)\}$。

**定理 12.4 (可对角化矩阵的谱半径估计)**  若 $U$ 可对角化，则 $\lVert Uv\rVert\le\rho(U)\lVert v\rVert$。

**定理 12.5 (谱半径乘法上界)**  $\rho(A_1\cdots A_k)\le\rho(A_1)\cdots\rho(A_k)$。

**定义 12.9 (广义谱半径)**  $\rho(\Sigma)=\varlimsup_{k\to\infty}\max\{\rho(A_1\cdots A_k)\}$。

##### §12.3 方程组快速求解与随机矩阵

**定义 12.10 (Moore-Penrose 逆)**  $A^\dagger$ 满足 $AA^\dagger A=A$、$A^\dagger AA^\dagger=A^\dagger$，且 $AA^\dagger, A^\dagger A$ 对称（厄米）。

**定义 12.11 (近似解与 $A$-范数)**  $\lVert x\rVert_A=\sqrt{x^\mathrm{T}Ax}$，若 $\lVert\tilde x-A^\dagger b\rVert_A\le\varepsilon\lVert A^\dagger b\rVert_A$ 则为精度 $\varepsilon$ 近似解。

**定义 12.12 (弱主对角占优)**  $a_{ii}\ge\sum_{j\ne i}|a_{ij}|$。

**定理 12.6 (Spielman-Teng, 2014)**  对主对角占优对称矩阵 $A$，可在 $O(m\log^c n\log(1/\varepsilon))$ 时间内求解 $Ax=b$ 的随机算法。

**定义 12.13 (Bernoulli 矩阵)**  元素为独立同分布 Bernoulli 随机变量的矩阵。

**定理 12.7 (Tikhomirov, 2020)**  $n$ 阶 Bernoulli 矩阵奇异概率 $P_n=(\tfrac12+o(1))^n$。

**定理 12.8 (Tao-Vu, 2007)**  $P_n=(\tfrac34+o(1))^n$ 的上界。

**定理 12.9 (Bourgain, 2010)**  $P_n=(\tfrac{1}{\sqrt2}+o(1))^n$ 的上界。

**定理 12.10 (Tikhomirov, 2020 扩展)**  成功概率 $p\in(0,\tfrac12]$ 的 Bernoulli 矩阵有 $P_n=(1-p+o(1))^n$。

**定义 12.14 ($\ell_p$ 范数)**  $\lVert x\rVert_p=(\sum_i|x_i|^p)^{1/p}$。

**定义 12.15 ($\ell_p$ 稀疏)**  若 $\lVert x\rVert_p<R$（$0<p\le1$），则称 $x$ 为 $\ell_p$-稀疏。

##### §12.4 线性性推广与表示

**定义 12.16 (模)**  设 $R$ 为环，$M$ 为 Abel 群，若存在 $R\times M\to M$ 满足分配与结合条件，则 $M$ 为 $R$-模。

**定理 12.11 (Freyd-Mitchell, 1964)**  任意小 Abel 范畴可满忠实且正合地嵌入某环的左模范畴。

**定理 12.12 (Quillen-Gabriel, 1972)**  任意小 Quillen 正合范畴可正合地嵌入 Abel 范畴。

**定义 12.17 (双线性映射)**  $V\times W\to Z$ 关于 $V$ 与 $W$ 分别线性。

**定义 12.18 (张量积的泛性质)**  $V\otimes W$ 为使任意双线性映射唯一因子化的对象。

**引理 12.1 (线性自同态群)**  $\mathcal{L}(V)$ 在复合下构成群。

**定义 12.19 (群表示)**  群同态 $\rho:G\to\mathcal{L}(V)$。

**定义 12.20 (特征标)**  $\chi_\rho(g)=\operatorname{tr}\rho(g)$。

---

#### 第13章 多项式

##### §13.1 多项式的定义与运算

**定义 13.1 (多项式函数)**  若 $p(x)=a_0+a_1x+\cdots+a_mx^m$，称 $p$ 为数域上的多项式函数，次数为最大 $k$ 使 $a_k\ne0$。

**定理 13.1 (零多项式系数唯一性)**  若 $p(x)\equiv0$（对所有 $x$），则系数全为 $0$。

**定义 13.2 (形式多项式)**  视 $x$ 为符号，$p(x)=a_0+\cdots+a_mx^m$；定义次数、首项系数与首一多项式。

**定义 13.3 (多项式加法/数乘/乘法)**  按系数逐项相加、数乘与卷积乘法定义。

**定理 13.2 (次数性质)**  $\deg(p+q)\le\max\{\deg p,\deg q\}$，$\deg(kp)=\deg p$（$k\ne0$），$\deg(pq)=\deg p+\deg q$。

##### §13.2 整除与带余除法

**定义 13.4 (整除)**  若 $p=sq$，则 $q\mid p$。

**定理 13.3 (整除性质)**  传递性、与线性组合相容，非零常数整除任意多项式。

**定理 13.4 (互相整除判别)**  若 $p\mid q$ 且 $q\mid p$，则 $p=kq$（$k\ne0$）。

**定义 13.5 (相伴多项式)**  若 $p=kq$（$k\ne0$），则 $p\sim q$。

**定理 13.5 (带余除法)**  对 $p,s$（$s\ne0$）存在唯一 $q,r$ 使 $p=sq+r$ 且 $\deg r<\deg s$。

##### §13.3 最大公因式与互素

**定义 13.6 (gcd 与 lcm)**  最大公因式与最小公倍式分别为整除意义下的最大/最小者（取首一）。

**定理 13.6 (欧几里得算法)**  最大公因式存在，且 $d=up+vq$。

**定理 13.7 (多项式组的 gcd)**  多个多项式的 gcd 存在，且可表示为线性组合。

**定义 13.7 (互素)**  $(p,q)=1$。

**定理 13.8 (裴蜀定理)**  $(p,q)=1\iff\exists u,v,\ up+vq=1$。

**定理 13.9 (互素性质)**  若 $(p,q)=1$，则 $p\mid qs\Rightarrow p\mid s$，并保持在若干乘积中的互素性等。

**定理 13.10 (gcd 与 lcm 关系)**  $pq=c\,(p,q)[p,q]$，其中 $c$ 为 $pq$ 的首项系数。

**定理 13.11 (中国剩余定理)**  若 $q_i$ 两两互素，则方程组 $p\equiv r_i\pmod{q_i}$ 在模 $Q=\prod q_i$ 下有唯一解。

##### §13.4 不可约与唯一分解

**定义 13.8 (可约/不可约多项式)**  非常数多项式若可分解为次数更低的乘积则可约，否则不可约。

**定理 13.12 (不可约多项式性质)**  不可约多项式要么整除 $q$ 要么与 $q$ 互素；若整除 $qs$ 则整除 $q$ 或 $s$。

**推论 13.1 (不可约的整除推广)**  若不可约多项式整除乘积，则必整除其中一因子。

**定理 13.13 (唯一分解定理)**  任意非常数多项式可分解为不可约多项式乘积，分解在相伴与顺序意义下唯一。

**定义 13.9 (标准分解式)**  $p(x)=c\prod q_i(x)^{\alpha_i}$，$q_i$ 不可约、$\alpha_i\ge1$，$c\ne0$。

##### §13.5 重因式与形式导数

**定义 13.10 (形式导数)**  $p'(x)=a_1+2a_2x+\cdots+na_nx^{n-1}$。

**定理 13.14 (重因式判别)**  $p$ 无重因式 $\iff (p,p')=1$。

**定理 13.15 (消去重因式)**  设 $d=(p,p')$，则 $p/d$ 无重因式且保留全部不可约因式（不计重数）。

##### §13.6 多项式函数与根

**定义 13.11 (零点/根)**  $p(\lambda)=0$ 的解 $\lambda$。

**定理 13.16 (根的性质)**
1. $p(\lambda)=0\iff (x-\lambda)\mid p(x)$；
2. $m$ 次多项式至多有 $m$ 个互异根；
3. 不可约多项式（度 $\ge2$）在该域上无根。

**定义 13.12 (重根)**  若 $(x-\lambda)^k\mid p$ 但 $(x-\lambda)^{k+1}\nmid p$，称 $\lambda$ 为 $k$ 重根。

**定理 13.17 (代数学基本定理)**  任何非常数复多项式在 $\mathbf{C}$ 上有根。

**推论 13.2 (复数域分解)**  复数域上 $n$ 次多项式有且仅有 $n$ 个复根（含重数），不可约多项式皆为一次。

**定理 13.18 (韦达定理)**  根与系数满足对称函数关系：$\sum\lambda_i=-a_{n-1}/a_n$，$\prod\lambda_i=(-1)^n a_0/a_n$ 等。

##### §13.7 实数域与有理数域上的因式分解

**引理 13.1 (实系数共轭根)**  若 $\lambda$ 为实系数多项式根，则 $\overline{\lambda}$ 也是根。

**引理 13.2 (实数域不可约形式)**  实数域不可约多项式为一次或判别式 $<0$ 的二次多项式。

**定理 13.19 (实数域分解)**  实系数多项式可分解为一次因子与不可约二次因子之积。

**定理 13.20 (有理根必要条件)**  若整系数多项式有有理根 $q/p$（互素），则 $p\mid a_n$ 且 $q\mid a_0$。

**定义 13.13 (本原多项式)**  整系数多项式系数 gcd 为 1。

**引理 13.3 (高斯引理)**  本原多项式乘积仍为本原多项式。

**定理 13.21 (有理系数可约性)**  整系数多项式在 $\mathbf{Q}$ 上可约 $\iff$ 在 $\mathbf{Z}$ 上可约。

**定理 13.22 (艾森斯坦判别法)**  若存在素数 $p$ 使 $p\mid a_0,\ldots,a_{n-1}$、$p\nmid a_n$ 且 $p^2\nmid a_0$，则多项式在 $\mathbf{Q}$ 上不可约。

##### §13.8 多项式理想与商空间

**定理 13.23 (理想与商空间维数)**  $(p(x))$ 为 $\mathbf{F}[x]$ 的子空间，且 $\dim\mathbf{F}[x]/(p(x))=\deg p$，基可取 $\{1+(p),\ldots,x^{n-1}+(p)\}$。

---

#### 第14章 相似标准形：动机与基础

##### §14.1 相似与不变子空间

**定义 14.1 (相似)**  对 $A,B\in\mathbf{M}_n(\mathbf{F})$，若存在可逆矩阵 $P$ 使 $B=P^{-1}AP$，则称 $A$ 与 $B$ 相似，记 $A\sim B$。

**定义 14.2 (不变子空间)**  设 $\sigma\in\mathcal{L}(V)$，若子空间 $U\subseteq V$ 满足 $\sigma(U)\subseteq U$，则称 $U$ 在 $\sigma$ 下不变。

**定义 14.3 (限制变换与商变换)**  若 $U$ 在 $\sigma$ 下不变，则可定义 $\sigma|_U\in\mathcal{L}(U)$；并可定义 $\sigma/U\in\mathcal{L}(V/U)$ 为 $(\sigma/U)(v+U)=\sigma(v)+U$。

**定理 14.1 (分块对角与不变直和等价)**  设 $V=U_1\oplus\cdots\oplus U_m$，则 $\sigma$ 在某组拼接基下的矩阵为分块对角矩阵 $\operatorname{diag}(A_1,\ldots,A_m)$，其中 $A_i$ 是 $\sigma|_{U_i}$ 的矩阵；反之，若矩阵可写成该分块形式，则对应子空间直和均不变。

**引理 14.1 (循环子空间最小性)**  对 $v\neq0$，$W=\operatorname{span}(v,\sigma v,\sigma^2v,\ldots)$ 是包含 $v$ 的最小 $\sigma$-不变子空间。

##### §14.2 特征值与特征向量

**定义 14.4 (特征值、特征向量、特征子空间)**  若存在 $v\neq0$ 使 $\sigma(v)=\lambda v$，则 $\lambda$ 是特征值，$v$ 是特征向量；$E_\lambda=\ker(\sigma-\lambda I)$ 称特征子空间。

**定义 14.5 (特征多项式)**  对 $A\in\mathbf{M}_n(\mathbf{F})$，定义 $\chi_A(t)=\det(tI-A)$。

**定理 14.2 (特征值判别等价)**  对 $\lambda\in\mathbf{F}$，以下等价：
1. $\lambda$ 是 $\sigma$ 的特征值。
2. $\sigma-\lambda I$ 非单射。
3. $\sigma-\lambda I$ 非满射。
4. $\sigma-\lambda I$ 不可逆。

**定理 14.3 (特征多项式系数公式)**  若
$$
\chi_A(t)=t^n+a_1t^{n-1}+\cdots+a_n,
$$
则 $a_1=-\operatorname{tr}(A)$，$a_n=(-1)^n\det(A)$，且 $a_k$ 等于所有 $k$ 阶主子式之和乘以 $(-1)^k$。

**定理 14.4 (相似不变量)**  若 $A\sim B$，则 $\chi_A=\chi_B$，从而特征值（含重数）、迹、行列式相同。

##### §14.3 特征值与特征向量基本性质

**定理 14.5 (特征值运算性质)**  设 $\lambda$ 是 $\sigma$ 的特征值，则：
1. $k\lambda$ 是 $k\sigma$ 的特征值，$\lambda^m$ 是 $\sigma^m$ 的特征值。
2. 对多项式 $f$，$f(\lambda)$ 是 $f(\sigma)$ 的特征值。
3. 若 $A$ 可逆，$\lambda^{-1}$ 是 $A^{-1}$ 的特征值，$\det(A)\lambda^{-1}$ 是 $A^*$ 的特征值。
4. $A$ 与 $A^\mathsf{T}$ 特征值相同（含重数）。

**定理 14.6 (互异特征值对应线性无关)**  互异特征值对应的特征向量线性无关；相应特征子空间之和为直和。

**定理 14.7 (代数重数与几何重数)**  每个特征值的代数重数不小于其几何重数。

**方法 14.1 (特征值法解题框架)**  处理 $f(A)=0$ 这类问题时，可先由 $f(\lambda)=0$ 限制特征值，再结合迹、行列式、秩与重数关系求解。

##### §14.4 实数域与复数域差异、估计

**定理 14.8 (复数域上必有特征值)**  复线性空间上的任意线性变换必有特征值。

**定理 14.9 (实空间的一维/二维不变子空间)**  实有限维空间上线性变换总存在一维或二维不变子空间。

**定义 14.6 (Gershgorin 圆盘)**  对 $A=(a_{ij})$，定义
$$
D_i=\{z\in\mathbf{C}:|z-a_{ii}|\le\sum_{j\ne i}|a_{ij}|\}.
$$

**定理 14.10 (Gershgorin 第一/第二定理)**  
1. 所有特征值都落在 $\bigcup_i D_i$ 中。
2. 若若干圆盘并成的连通分支两两不交，则每个分支包含的特征值个数等于该分支内圆盘个数（按代数重数计）。

##### §14.5 补充定理

**定理 14.3.10 (矩阵方程 $AX-XB=O$ 的解的秩)**  设 $A,B$ 分别为数域 $\mathbf{F}$ 上 $n$ 阶、$m$ 阶方阵，$A,B$ 有 $r$ 个两两不等的公共特征值，则矩阵方程 $AX-XB=O$ 有秩为 $r$ 的矩阵解。反之，若数域为复数域，矩阵方程 $AX-XB=O$ 有秩为 $r$ 的矩阵解，则 $A,B$ 至少有 $r$ 个公共特征值（计重数）。

**定理 14.4.1 (线性变换在商空间上的诱导映射)**  设 $\sigma\in\mathcal{L}(V,W)$，定义 $\widetilde{\sigma}:(V/(\ker\sigma))\to W$ 为 $\widetilde{\sigma}(v+\ker\sigma)=\sigma(v)$，则：
1. $\widetilde{\sigma}$ 良定义且为线性映射；
2. $\widetilde{\sigma}$ 为单射；
3. $\operatorname{im}\widetilde{\sigma}=\operatorname{im}\sigma$；
4. $V/(\ker\sigma)\cong \operatorname{im}\sigma$。

**定理 14.4.2 (数乘变换的刻画)**  设 $T\in\mathcal{L}(V)$，则 $T$ 为数乘变换 $T=cI_V$ 的充要条件是 $V$ 的每个一维子空间都是 $T$ 的不变子空间。

**定理 14.4.3 (商线性变换的性质)**  设 $V$ 有限维，$T\in\mathcal{L}(V)$ 且 $U$ 在 $T$ 下不变，则 $T/U$ 的每个特征值均为 $T$ 的特征值。

**定理 14.4.5 (可交换线性变换有公共特征向量)**  若 $AB=BA$，则 $A$ 和 $B$ 至少有一个共同特征向量。

**定理 14.4.6 (特征值平方和与矩阵元素)**  设 $\lambda_1,\ldots,\lambda_n$ 是矩阵 $A=(a_{ij})_{n\times n}$ 的特征值，则 $\lambda_1^2,\ldots,\lambda_n^2$ 是 $A^2$ 的特征值，且
$$
\sum_{i=1}^n \lambda_i^2=\sum_{j=1}^n\sum_{k=1}^n a_{jk}a_{kj}.
$$

**定理 14.4.7 (严格对角占优矩阵可逆性)**  严格对角占优的矩阵是可逆的。

**定理 14.4.8 (矩阵多项式的可逆性)**  设 $A,B\in\mathbf{M}_n(\mathbf{C})$，$B$ 的特征多项式 $f(\lambda)=|\lambda E-B|$，则 $f(A)$ 可逆当且仅当 $B$ 的任一特征值都不是 $A$ 的特征值。

---

#### 第15章 相似标准形：复数域上的尝试与理论

##### §15.1 对角化条件与求解

**定理 15.0 (对角矩阵等价一维不变子空间)**  设 $V$ 是 $n$ 维线性空间，$\sigma\in\mathcal{L}(V)$ 在基 $B=\{\alpha_1,\ldots,\alpha_n\}$ 下的表示矩阵为对角矩阵 $\operatorname{diag}(d_1,\ldots,d_n)$，当且仅当 $V$ 能分解为 $\sigma$ 的一维不变子空间直和 $V=U_1\oplus\cdots\oplus U_n$，其中 $U_i=\operatorname{span}(\alpha_i)$.

**定义 15.1 (可对角化)**  若 $\exists P$ 可逆使 $P^{-1}AP$ 为对角矩阵，则称 $A$ 可对角化。

**定理 15.1 (可对角化等价条件)**  对 $\sigma\in\mathcal{L}(V)$，以下等价：
1. $\sigma$ 可对角化。
2. $V$ 有一组由特征向量组成的基。
3. $V=\bigoplus_{i=1}^sE_{\lambda_i}$（$\lambda_i$ 为互异特征值）。
4. $\sum_i\dim E_{\lambda_i}=\dim V$。
5. 每个特征值代数重数等于几何重数。

**推论 15.1 (充分条件)**  若 $n$ 维空间上线性变换有 $n$ 个互异特征值，则可对角化。

**方法 15.1 (对角化算法)**  
1. 求 $\chi_A(t)$ 与全部特征值。
2. 分别解 $(A-\lambda I)x=0$ 求特征子空间基。
3. 验证总维数是否为 $n$。
4. 用所有特征向量组装 $P$，得到 $P^{-1}AP=\Lambda$。

##### §15.2 分块对角与上三角

**定理 15.2 (核空间扩张稳定性)**  对有限维 $V$，序列
$$
\ker T\subseteq\ker T^2\subseteq\cdots
$$
终将稳定；且对 $n=\dim V$ 有 $\ker T^n=\ker T^{n+1}=\cdots$。

**定理 15.3 (核像直和分解)**  对任意 $T\in\mathcal{L}(V)$ 与 $n=\dim V$，有
$$
V=\ker T^n\oplus\operatorname{im}T^n.
$$

**定理 15.4 (上三角判据)**  对基 $v_1,\ldots,v_n$，以下等价：
1. $\sigma$ 在该基下矩阵上三角。
2. $\sigma(v_j)\in\operatorname{span}(v_1,\ldots,v_j)$。
3. $\operatorname{span}(v_1,\ldots,v_j)$ 对每个 $j$ 都不变。

**定理 15.5 (复空间上三角化存在)**  任意有限维复空间线性变换都可上三角化。

##### §15.3 可交换算子与应用

**定理 15.6 (可交换与公共特征向量)**  若 $\sigma\tau=\tau\sigma$，则：
1. $\sigma$ 的每个特征子空间在 $\tau$ 下不变。
2. $\sigma,\tau$ 有公共特征向量。

**定理 15.7 (同时上三角化)**  若复空间上 $\sigma\tau=\tau\sigma$，则存在同一组基使二者矩阵同时上三角。

##### §15.4 特殊算子：幂等、幂零、复化

**定义 15.2 (投影变换)**  若 $V=U\oplus W$，映射 $\pi(u+w)=u$ 称为沿 $W$ 到 $U$ 的投影。

**定理 15.8 (幂等等价投影)**  $\sigma^2=\sigma$ 当且仅当 $\sigma$ 是到 $\operatorname{im}\sigma$ 的投影（沿 $\ker\sigma$）。

**定理 15.9 (幂零等价刻画)**  对有限维 $V$ 上 $N\in\mathcal{L}(V)$，以下等价：
1. $N$ 幂零。
2. 所有特征值为 $0$。
3. 存在一组基使 $N$ 矩阵严格上三角。
4. $I\pm N$ 可逆。

**定理 15.10 (平方根存在性)**  
1. 若 $N$ 幂零，则 $I+N$ 有平方根。
2. 复数域上任意可逆线性变换有平方根。

**定义 15.3 (复化)**  对实空间 $V$，定义复化空间 $V_\mathbf{C}$ 与复化算子 $\sigma_\mathbf{C}(u+iv)=\sigma(u)+i\sigma(v)$。

**定理 15.11 (复化谱性质)**  
1. 实特征值在 $\sigma$ 与 $\sigma_\mathbf{C}$ 间保持等价。
2. 非实特征值成共轭对出现。
3. 广义特征向量也按共轭成对对应。

---

#### 第16章 若当标准形

##### §16.1 若当块与若当链

**定义 16.1 (若当块)**  
$$
J_r(\lambda)=\begin{pmatrix}
\lambda&1&&\\
&\lambda&\ddots&\\
&&\ddots&1\\
&&&\lambda
\end{pmatrix}.
$$

**定义 16.2 (广义特征向量与广义特征子空间)**  若 $(A-\lambda I)^k v=0$（某 $k\ge1$）且 $v\neq0$，称 $v$ 为关于 $\lambda$ 的广义特征向量；$G_\lambda=\ker(A-\lambda I)^n$。

**定义 16.3 (若当链/若当循环基)**  若向量列满足
$$
(A-\lambda I)v_1=0,\quad (A-\lambda I)v_{j+1}=v_j,
$$
则称 $v_1,\ldots,v_r$ 为一条若当链。

##### §16.2 存在性与唯一性

**定理 16.1 (广义特征直和分解)**  对复矩阵 $A$，若互异特征值为 $\lambda_1,\ldots,\lambda_s$，则
$$
\mathbf{C}^n=G_{\lambda_1}\oplus\cdots\oplus G_{\lambda_s}.
$$

**定理 16.2 (若当标准形存在定理)**  任意复矩阵都相似于若当标准形（若干若当块分块对角）。

**定理 16.3 (若当标准形唯一性)**  若当标准形在“每个特征值对应各块大小多重集合”意义下唯一（块顺序除外）。

**推论 16.1 (若当基存在)**  设 $V$ 是 $\mathbf{C}$ 上的有限维线性空间，$\sigma\in\mathcal{L}(V)$，则存在一组基 $B$ 使得 $\sigma$ 在 $B$ 下的矩阵表示为若当标准形。

**引理 16.1 (若当块计数公式)**  固定特征值 $\lambda$，记 $N=A-\lambda I$，则：
1. $\lambda$ 的若当块总数 $=\dim\ker N$。
2. 尺寸至少为 $k$ 的块数 $=\dim\ker N^k-\dim\ker N^{k-1}$。
3. 尺寸恰为 $k$ 的块数
$$
=(\dim\ker N^k-\dim\ker N^{k-1})-(\dim\ker N^{k+1}-\dim\ker N^k).
$$

##### §16.3 结构与应用

**定理 16.4 (若当块不变子空间结构)**  单个若当块 $J_n(\lambda)$ 的不变子空间恰为
$$
\{0\},\operatorname{span}(e_1),\operatorname{span}(e_1,e_2),\ldots,\operatorname{span}(e_1,\ldots,e_n).
$$

**定理 16.5 (矩阵幂收敛判别)**  $A^m$ 收敛当且仅当每个若当块满足：
1. 对应特征值 $|\lambda|<1$；或
2. 该块恰是 $J_1(1)$。

**推论 16.2 (随机矩阵幂次收敛框架)**  对行随机矩阵 $P$，若单位圆上唯一特征值为 $1$，则 $P^m$ 收敛到投影到 $\lambda=1$ 特征子空间的极限矩阵。

**定理 16.6 (Jordan-Chevalley 分解)**  任意复矩阵可唯一分解为
$$
A=S+N,
$$
其中 $S$ 可对角化、$N$ 幂零、$SN=NS$，且 $S,N$ 都是 $A$ 的多项式。

**定理 16.7 (实数域上的实若当形)**  实矩阵在实数域上相似于由实若当块与 $2\times2$ 旋转伸缩块组成的分块对角矩阵。

---

#### 第17章 多项式的进一步讨论

##### §17.1 消去多项式与最小多项式

**定理 17.0 (特征多项式与不变子空间)**  设 $V$ 是复向量空间，$V_1,\ldots,V_m$ 是 $V$ 的非零子空间，且 $V=V_1\oplus\cdots\oplus V_m$，并且每个 $V_j$ 都在 $\sigma\in\mathcal{L}(V)$ 下不变。若 $f_j$ 表示 $\sigma\vert_{V_j}$ 的特征多项式，则 $\sigma$ 的特征多项式为 $f_1\cdots f_m$。

**推论 17.0 (代数重数等于广义特征空间维数)**  设 $\sigma\in\mathcal{L}(V)$，$\lambda_i$ 为其任意特征值，$d_i$ 为 $\lambda_i$ 的代数重数，则 $\lambda_i$ 对应的广义特征子空间维数也为 $d_i$。

**定义 17.1 (消去多项式)**  若 $p(A)=0$，称 $p$ 是 $A$ 的消去多项式。

**定义 17.2 (最小多项式)**  首一且次数最低的消去多项式记为 $m_A(t)$。

**定理 17.1 (Cayley-Hamilton)**  任意矩阵满足其特征多项式：$\chi_A(A)=0$。

**定理 17.2 (最小多项式基本性质)**  
1. $m_A\mid \chi_A$。
2. 对任意多项式 $p$，$p(A)=0\iff m_A\mid p$。
3. $m_A$ 与若当块最大尺寸对应：
对每个特征值 $\lambda$，$m_A$ 中 $(t-\lambda)$ 的指数等于该特征值最大若当块阶数。

##### §17.2 对角化与多项式判据

**定理 17.3 (对角化最小多项式判据)**  $A$ 可对角化当且仅当 $m_A$ 在基域上分裂且无重根。

**推论 17.1 (常见矩阵快速判别)**  若 $A$ 满足形如 $(A-aI)(A-bI)=0$ 且 $a\neq b$，则 $A$ 可对角化。

**定理 17.4 (特征子空间与广义特征子空间关系)**  设
$$
m_A(t)=\prod_{i=1}^s (t-\lambda_i)^{r_i},
$$
则 $G_{\lambda_i}=\ker(A-\lambda_iI)^{r_i}$，并可据此分解空间。

##### §17.3 不变因子与循环子空间框架

**定义 17.3 (循环子空间多项式模型)**  对向量 $v$，循环子空间同构于商模 $\mathbf{F}[t]/(p_v)$，其中 $p_v$ 是 $v$ 的首一消去多项式。

**定理 17.5 (循环分解框架)**  有限维空间可分解为若干循环子空间直和；相应多项式链整除关系导出不变因子结构。

---

#### 第18章 有理标准形

##### §18.1 伴随矩阵与有理块

**定义 18.1 (伴随矩阵)**  对首一多项式
$$
p(t)=t^d+a_{d-1}t^{d-1}+\cdots+a_0,
$$
其伴随矩阵 $C(p)$ 为 Frobenius 伴随形。

**定义 18.2 (第一有理标准形/不变因子标准形)**  将伴随矩阵按整除链 $p_1\mid p_2\mid\cdots\mid p_k$ 分块对角排列。

**定义 18.3 (第二有理标准形/初等因子标准形)**  按不可约多项式幂次对应的伴随块分解得到的分块对角形式。

##### §18.2 存在与唯一

**定理 18.1 (第一有理标准形存在唯一)**  任意域上任意方阵均相似于唯一（块顺序除外）的第一有理标准形。

**定理 18.2 (第二有理标准形存在唯一)**  任意域上任意方阵均相似于唯一（块顺序除外）的第二有理标准形。

**引理 18.1 (两种有理标准形互导)**  不变因子分解为不可约幂后可得初等因子；将同一不可约因子族按指数汇总可反推不变因子。

##### §18.3 判定与联系

**定理 18.3 (相似判定)**  两矩阵相似当且仅当它们的不变因子相同；等价地，当且仅当初等因子多重集合相同。

**推论 18.1 (与若当形关系)**  在代数闭域上，不可约因子全为一次，因此第二有理标准形退化为若当标准形描述。

##### §18.4 初等因子与不变因子

**定义 18.4 (初等因子与初等因子组)**  在循环子空间分解中，多项式 $(t-\theta)^k$ 称为一个初等因子；所有初等因子构成初等因子组。

**定理 18.4 (初等因子组是相似全系不变量)**  两个矩阵相似当且仅当它们有相同的初等因子组。

**定义 18.5 (不变因子组)**  将初等因子按不可约多项式分组并按指数降序排列，对齐后逐列相乘得到多项式组 $d_1\mid d_2\mid\cdots\mid d_s$，称为不变因子组。

**推论 18.2 (第一有理标准形唯一)**  由不变因子组确定的有理标准形（第一有理标准形）是唯一的。

**推论 18.3 (初等因子分解最细)**  初等因子分解是最细的准素分解；不变因子则是由初等因子按列组合得到的整除链分解。

**注 18.1**  有理标准形在任意数域上都存在，而若当标准形仅在代数闭域上存在；在复数域上，两者描述角度不同，但都可用来刻画相似类。

---

#### 第19章 内积空间

##### §19.1 基本定义

**定义 19.1 (内积与内积空间)**  映射 $\langle\cdot,\cdot\rangle$ 满足共轭对称、线性与正定，称内积；配备内积的线性空间称内积空间。

**定义 19.2 (范数、正交、标准正交组)**  
$$
\|v\|=\sqrt{\langle v,v\rangle},\quad \langle u,v\rangle=0\Rightarrow u\perp v.
$$
两两正交且范数为 1 的向量组称标准正交组。

**补充定义 19.1 (标准正交基)**  $V$ 的标准正交基是 $V$ 中的标准正交向量组构成的基。

**补充定理 19.1 (勾股定理推广)**  若 $e_1,\ldots,e_m$ 是 $V$ 中的标准正交向量组，则对任意 $a_1,\ldots,a_m\in\mathbf{F}$，有
$$
\left\|a_1e_1+\cdots+a_me_m\right\|^2=|a_1|^2+|a_2|^2+\cdots+|a_m|^2.
$$

**补充定理 19.2 (标准正交组线性无关)**  任何标准正交向量组都是线性无关的。

**补充定理 19.3 (Fourier 展开)**  设 $e_1,\ldots,e_n$ 是 $V$ 的标准正交基，$v\in V$，则
$$
v=\langle v,e_1\rangle e_1+\cdots+\langle v,e_n\rangle e_n,
$$
且
$$
\|v\|^2=|\langle v,e_1\rangle|^2+\cdots+|\langle v,e_n\rangle|^2.
$$

##### §19.2 基本定理

**定理 19.1 (Cauchy-Schwarz 不等式)**  
$$
|\langle u,v\rangle|\le \|u\|\,\|v\|.
$$

**推论 19.1 (三角不等式与平行四边形恒等式)**  
$$
\|u+v\|\le\|u\|+\|v\|,
$$
并满足平行四边形公式。

**定理 19.2 (正交补分解)**  对有限维内积空间与子空间 $U$，有
$$
V=U\oplus U^\perp,
$$
且 $\dim U+\dim U^\perp=\dim V$。

**定理 19.3 (Gram-Schmidt 正交化)**  任意线性无关组可正交化为标准正交基。

**补充定理 19.4 (QR 分解)**  设 $A$ 是 $n$ 阶可逆矩阵，则存在唯一的分解 $A=QR$，其中 $Q$ 的列向量构成标准正交基，$R$ 是主对角元全为正实数的上三角矩阵。

**补充定理 19.5 (Schur 定理)**  设 $V$ 是有限维复内积空间，$T\in\mathcal{L}(V)$，则 $T$ 关于 $V$ 的某个标准正交基具有上三角矩阵。

**定理 19.4 (Riesz 表示定理，有限维版)**  任意线性泛函 $f$ 可唯一写成
$$
f(x)=\langle x,y\rangle
$$
（某唯一 $y\in V$）。

**定理 19.6 (Bessel 不等式)**  若 $\{e_1,\ldots,e_m\}$ 是标准正交组，则对任意 $v\in V$，有
$$
\sum_{j=1}^m |\langle v,e_j\rangle|^2\le \|v\|^2,
$$
且等号成立当且仅当 $v\in\operatorname{span}\{e_1,\ldots,e_m\}$。

**定理 19.7 (Parseval 等式)**  若 $\{e_1,\ldots,e_n\}$ 是标准正交基，则
$$
\|v\|^2=\sum_{j=1}^n |\langle v,e_j\rangle|^2.
$$

**定义 19.4 (Gram 矩阵)**  设 $\{e_1,\ldots,e_n\}$ 是 $V$ 的一组基，定义 $G_{ij}=\langle e_i,e_j\rangle$ 为该基下的 Gram 矩阵。

**定理 19.8 (Gram 矩阵与线性无关)**  向量组线性无关当且仅当其 Gram 矩阵可逆。

**定理 19.9 (Gram-Schmidt 过程与 Gram 矩阵行列式)**  Gram-Schmidt 正交化不改变向量组 Gram 矩阵的行列式。

**定理 19.10 (Hadamard 不等式)**  对任意矩阵 $A=(a_{ij})$，有
$$
|\det A|^2\le \prod_{j=1}^n\sum_{i=1}^n a_{ij}^2.
$$

##### §19.3 投影与最小二乘

**定义 19.3 (正交投影)**  对子空间 $U$，将 $v=u+w$（$u\in U,w\in U^\perp$）中的 $u$ 记为 $\operatorname{proj}_U v$。

**定理 19.5 (最佳逼近定理)**  $u_*=\operatorname{proj}_U v$ 当且仅当
$$
\|v-u_*\|=\min_{u\in U}\|v-u\|.
$$

**方法 19.1 (最小二乘法正规方程)**  对超定方程 $Ax\approx b$，最小二乘解满足
$$
A^\mathsf{T}Ax=A^\mathsf{T}b
$$
（复数域用 $A^*A x=A^*b$）。

---

#### 第20章 内积空间上的算子

##### §20.0 内积空间的同构

**补充定义 20.0 (保积同构)**  设 $V$ 和 $U$ 是数域 $\mathbf{F}$ 上的两个内积空间，$S:V\to U$ 是线性映射。若对任意 $u,v\in V$ 都有 $\langle Su,Sv\rangle_U=\langle u,v\rangle_V$，则称 $S$ 为保持内积的线性映射；若 $S$ 还是双射，则称 $S$ 为保积同构。

**补充定理 20.0 (保持范数蕴含保持内积)**  若 $S:V\to U$ 是保持范数的线性映射，则 $S$ 保持内积。

**补充定理 20.1 (保积同构刻画)**  设 $V$ 和 $U$ 是数域 $\mathbf{F}$ 上的两个 $n$ 维内积空间，$S:V\to U$ 为线性映射. 则以下条件等价：$S$ 保持内积；$S$ 是保积同构；$S$ 将 $V$ 的任一组标准正交基映射到 $U$ 的一组标准正交基；$S$ 将 $V$ 的某一组标准正交基映射到 $U$ 的一组标准正交基。

**补充定理 20.2 (保积同构存在性判据)**  设 $V$ 和 $U$ 是数域 $\mathbf{F}$ 上的两个内积空间，则二者之间存在保积同构的充要条件是它们有相同的维数。

##### §20.1 伴随与算子类型

**定义 20.1 (伴随算子)**  $T^*$ 满足
$$
\langle Tx,y\rangle=\langle x,T^*y\rangle.
$$

**定义 20.2 (自伴、酉/正交、正规、正算子)**  
1. $T=T^*$：自伴。
2. $T^*T=TT^*=I$：酉（实情形为正交）。
3. $T^*T=TT^*$：正规。
4. $\langle Tx,x\rangle\ge0$：正算子。

**定理 20.1 (伴随基本性质)**  伴随满足线性、乘积反序、与逆可交换（可逆时）等规则。

##### §20.2 谱定理与结构

**定理 20.2 (复正规算子谱定理)**  复内积空间上，$T$ 正规当且仅当存在标准正交基使 $T$ 酉相似于对角矩阵。

**定理 20.3 (实正规算子标准形)**  实内积空间上，正规算子可正交相似为若干 $1\times1$ 实块与 $2\times2$ 旋转伸缩块的分块对角。

**定理 20.4 (正算子平方根)**  若 $T\ge0$，则存在唯一正算子 $R$ 使 $R^2=T$。

**补充定理 20.1 (T^*T 的基本性质)**  设 $T\in\mathcal{L}(V,W)$，则：
1. $T^*T$ 是正算子；
2. $\ker(T^*T)=\ker T$；
3. $\operatorname{im}(T^*T)=\operatorname{im}T^*$；
4. $\dim\operatorname{im}T=\dim\operatorname{im}T^*=\dim\operatorname{im}(T^*T)$。

**补充定义 20.1 (奇异向量)**  若 $T\in\mathcal{L}(V,W)$，奇异值为 $s$，且 $Tv=sw$、$T^*w=sv$，则称 $v$ 为左奇异向量，$w$ 为右奇异向量。

**注 20.1**  左奇异向量是 $T^*T$ 的特征向量，右奇异向量是 $TT^*$ 的特征向量。

##### §20.3 极分解与奇异值分解

**定理 20.5 (极分解)**  任意线性算子可写成
$$
T=UP,
$$
其中 $P=(T^*T)^{1/2}\ge0$，$U$ 为部分等距（可逆时为酉）。

**定义 20.3 (奇异值)**  $\sigma_i=\sqrt{\lambda_i(T^*T)}\ge0$ 称 $T$ 的奇异值。

**定理 20.6 (奇异值与单射满射的关系)**  设 $T\in\mathcal{L}(V,W)$，则：
1. $T$ 是单射 $\iff 0$ 不是 $T$ 的奇异值；
2. $T$ 的正奇异值个数等于 $\dim\operatorname{im} T$；
3. $T$ 是满射 $\iff$ 正奇异值个数等于 $\dim W$。

**定义 20.4 (矩形对角矩阵)**  设 $A=(a_{ij})_{m\times n}$，若 $i\ne j$ 时 $a_{ij}=0$，则称 $A$ 为矩形对角矩阵。

**定理 20.7 (SVD)**  任意矩阵存在酉（或正交）矩阵 $U,V$ 使
$$
A=U\Sigma V^*,
$$
其中 $\Sigma$ 为非负对角（或矩形对角）矩阵。

**推论 20.1 (范数与秩)**  
1. 算子 2-范数等于最大奇异值：$\|A\|_2=\sigma_{\max}(A)$。
2. 矩阵秩等于非零奇异值个数。

**定理 20.8 (奇异值分解的展开式)**  设 $A$ 的正奇异值为 $\sigma_1\ge\cdots\ge\sigma_r>0$，对应左、右奇异向量分别为 $u_1,\ldots,u_r$ 与 $v_1,\ldots,v_r$，则
$$
A x=\sum_{i=1}^r \sigma_i\langle x,v_i\rangle u_i.
$$

**定理 20.9 (特征人脸算法中的奇异值分解应用)**  设 $A\in\mathbf{R}^{m\times n}$ 为中心化后的人脸数据矩阵，$A=U\Sigma V^\mathsf{T}$，则：
1. $U$ 的列向量是 $AA^\mathsf{T}$ 的特征向量；
2. $V$ 的列向量是 $A^\mathsf{T}A$ 的特征向量；
3. 若 $u_i$ 是 $AA^\mathsf{T}$ 的特征向量（特征值 $\lambda_i$），则 $A^\mathsf{T}u_i$ 是 $A^\mathsf{T}A$ 的特征向量（同一特征值 $\lambda_i$）；
4. 前 $k$ 个主要特征向量可由 $(v_1,\ldots,v_k)=A^\mathsf{T}(u_1,\ldots,u_k)$ 计算（归一化后作为投影基）。

**方法 20.1 (截断奇异值近似)**  若只保留前 $k$ 个最大奇异值及对应奇异向量，则得到最优秩 $k$ 近似；等价地，用前 $k$ 个主方向构造低秩逼近。

---

#### 第21章 线性代数与几何

##### §21.0 坐标公式

**补充定理 21.0 (点积的坐标公式)**  设 $g_{ij}=\vec e_i\cdot\vec e_j\,(i,j=1,2,3)$，则有
$$
\vec a\cdot\vec b=\sum_{i=1}^3\sum_{j=1}^3 g_{ij}a_ib_j.
$$

**补充定理 21.1 (叉积的一般坐标展开式)**  在一般坐标系 $O;\vec e_1,\vec e_2,\vec e_3$ 中，
$$
\vec a\times\vec b
=
(a_2b_3-a_3b_2)\,\vec e_2\times\vec e_3
+(a_3b_1-a_1b_3)\,\vec e_3\times\vec e_1
+(a_1b_2-a_2b_1)\,\vec e_1\times\vec e_2.
$$

**补充定理 21.2 (混合积的一般坐标公式)**  在一般坐标系 $O;\vec e_1,\vec e_2,\vec e_3$ 中，
$$
[\vec a,\vec b,\vec c]
=
\begin{vmatrix}
	a_1 & a_2 & a_3 \\
	b_1 & b_2 & b_3 \\
	c_1 & c_2 & c_3
\end{vmatrix}
[\vec e_1,\vec e_2,\vec e_3].
$$

##### §21.1 向量积与空间几何

**定义 21.1 (点积、叉积、混合积)**  三维中定义
$$
u\cdot v,\quad u\times v,\quad [u,v,w]=u\cdot(v\times w).
$$

**定理 21.1 (几何量公式)**  
1. $\|u\times v\|$ 等于平行四边形面积。
2. $|[u,v,w]|$ 等于平行六面体体积。
3. 用行列式可写线、面方程与共面判据。

##### §21.2 直线平面与距离角度

**定义 21.2 (直线/平面表示)**  给出参数式、点法式、一般式之间的等价变换。

**定理 21.2 (距离与夹角公式)**  
1. 点到直线、点到平面距离可由投影与法向量给出。
2. 线线、线面、面面夹角均可转化为向量夹角问题。

**定理 21.3 (空间位置关系判别)**  通过秩、方向向量与法向量可判定相交、平行、异面。

**补充定理 21.1 (点到平面距离公式)**  点 $P(x_0,y_0,z_0)$ 到平面 $Ax+By+Cz+D=0$ 的距离为
$$
d=\frac{|Ax_0+By_0+Cz_0+D|}{\sqrt{A^2+B^2+C^2}}.
$$

**补充定理 21.2 (三点定平面)**  已知平面上三点 $A,B,C$ 不共线，则平面可由混合积条件
$$
[\overrightarrow{AB},\overrightarrow{AC},\overrightarrow{AP}]=0
$$
确定，其中 $P$ 为平面上任意点。

**补充定理 21.3 (两直线共面判据)**  两条直线共面的充要条件是它们的方向向量与连接向量构成的混合积为零。

**补充定理 21.4 (直线与平面的位置关系)**  设直线方向向量为 $\vec{l}$，平面法向量为 $\vec{n}$。若 $\vec{l}\cdot\vec{n}=0$，则直线与平面平行或在平面内；若 $\vec{l}\parallel\vec{n}$，则直线与平面垂直。

**补充定理 21.5 (两平面的位置关系)**  两个平面的法向量平行当且仅当两平面平行或重合；法向量垂直当且仅当两平面垂直。

**补充定理 21.6 (平面到原点的距离)**  平面 $Ax+By+Cz+D=0$ 到原点的距离为
$$
\frac{|D|}{\sqrt{A^2+B^2+C^2}}.
$$

**补充定理 21.7 (球面方程)**  球心为 $\vec{a}$、半径为 $r$ 的球面方程可写为 $\langle \vec{x}-\vec{a},\vec{x}-\vec{a}\rangle=r^2$。

**补充定理 21.8 (球与平面相切条件)**  球与平面在点 $\vec{t}$ 处相切，当且仅当 $\vec{t}$ 同时满足球面方程和平面方程，且 $\vec{t}$ 与平面法向量共线。

##### §21.3 仿射、射影与二次曲面

**定义 21.3 (仿射变换与齐次坐标)**  仿射变换可写成线性变换加平移，并在齐次坐标中统一为矩阵乘法。

**定义 21.4 (射影空间与无穷远超平面)**  以“过原点直线”作为点定义 $\mathbf{P}^n$，无穷远超平面刻画平行方向。

**定理 21.4 (二次曲面标准化框架)**  任意二次曲面可经平移与正交变换化到主轴标准形，分类由二次型符号结构决定。

##### §21.4 曲面上的标架

**定义 21.5 (切平面)**  设曲面 $S$ 的参数方程为 $\vec r(u,v)=(x(u,v),y(u,v),z(u,v))$，在点 $\vec r_0=\vec r(u_0,v_0)$ 处，切向量 $\vec t_u=\partial\vec r/\partial u$ 与 $\vec t_v=\partial\vec r/\partial v$ 张成的平面称为曲面在 $\vec r_0$ 处的切平面，记为 $T_{\vec r_0}S$。

**定义 21.6 (法向量)**  切平面的单位法向量称为曲面在该点处的法向量，记为 $\vec n$。

**定义 21.7 (第一基本形式)**  曲面 $S$ 的第一基本形式为
$$
\mathrm{d}s^2=E\,\mathrm{d}u^2+2F\,\mathrm{d}u\,\mathrm{d}v+G\,\mathrm{d}v^2,
$$
其中 $E=\vec t_u\cdot\vec t_u$，$F=\vec t_u\cdot\vec t_v$，$G=\vec t_v\cdot\vec t_v$。

**定理 21.5 (第一基本形式的参数变换规律)**  若参数变换为 $(\tilde u,\tilde v)=(\tilde u(u,v),\tilde v(u,v))$，则新旧第一基本形式的系数矩阵满足
$$
\begin{pmatrix}\tilde E & \tilde F \\ \tilde F & \tilde G\end{pmatrix}
=J^\mathsf{T}\begin{pmatrix}E & F \\ F & G\end{pmatrix}J,
$$
其中 $J=\begin{pmatrix}\partial u/\partial\tilde u & \partial u/\partial\tilde v \\ \partial v/\partial\tilde u & \partial v/\partial\tilde v\end{pmatrix}$ 为 Jacobi 矩阵。

**引理 21.1 (第一基本形式正定性)**  第一基本形式是正定的，即 $E>0$、$G>0$、$EG-F^2>0$。

##### §21.5 二次曲面及其分类

**定义 21.8 (二次曲面)**  二次曲面的一般方程为
$$
ax^2+by^2+cz^2+2dyz+2exz+2fxy+gx+hy+iz=1,
$$
或写成矩阵形式
$$
\begin{pmatrix}x&y&z\end{pmatrix}
\begin{pmatrix}a&f&e\\ f&b&d\\ e&d&c\end{pmatrix}
\begin{pmatrix}x\\y\\z\end{pmatrix}
+\begin{pmatrix}g&h&i\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix}=1.
$$

**定理 21.6 (二次曲面的标准化)**  任意二次曲面可经等距变换（旋转与平移）化为
$$
ax^2+by^2+cz^2=d,
$$
其中 $a,b,c$ 为二次型矩阵的特征值。

---

#### 第22章 二次型

##### §22.0 合同与对角化

**补充定义 22.0 (相合)**  若存在可逆矩阵 $C$ 使得 $B=C^\mathsf{T}AC$，则称 $A$ 相合于 $B$，记作 $A\simeq B$。

**补充引理 22.0 (初等变换与合同变换 1)**  对称矩阵的对换行列、倍乘行列、倍加行列的成对操作都是合同变换。

**补充引理 22.1 (初等变换与合同变换 2)**  若 $A$ 是非零对称矩阵，则必定存在可逆矩阵 $C$ 使得 $C^\mathrm{T}AC$ 的第 $(1,1)$ 个元素不为 $0$。

**补充定理 22.0 (对称矩阵合同对角化)**  设 $A$ 是 $n$ 阶对称矩阵，则必存在可逆矩阵 $C$ 使得 $C^\mathrm{T}AC$ 为对角矩阵。

**补充定理 22.2 (实对称矩阵的相合性质)**  设 $A,B$ 为 $n$ 阶实对称矩阵且 $A\simeq B$，则：
1. 对任意正整数 $m$，有 $A^m\simeq B^m$；
2. 若 $A$ 可逆，则 $A^{-1}\simeq B^{-1}$。

##### §22.1 定义与矩阵表示

**定义 22.1 (二次型)**  
$$
Q(x)=x^\mathsf{T}Ax
$$
（复数域用 $x^*Ax$ 讨论 Hermite 情形）；实二次型可取 $A=A^\mathsf{T}$。

**定义 22.2 (合同)**  若 $B=P^\mathsf{T}AP$（复数域可写 $B=P^*AP$），称 $A,B$ 合同。

**定理 22.1 (合同对角化)**  对称矩阵总可经合同变换对角化；正交变换下可得到谱分解形式。

**定理 22.1.1 (二次型矩阵表示唯一性)**  若对任意 $X$ 有 $X^\mathsf{T}AX=X^\mathsf{T}BX$，则 $A=B$。

**定理 22.1.2 (反对称矩阵刻画)**  $A$ 为反对称矩阵当且仅当对任意 $X$ 都有 $X^\mathsf{T}AX=0$。

##### §22.2 惯性与正定

**定理 22.2 (Sylvester 惯性定理)**  实对称矩阵合同对角化后正负零对角元个数不变量（惯性指数）。

**定理 22.2.1 (复二次型的标准形)**  任意 $n$ 元复二次型 $f(X)$ 可经可逆复线性替换化为规范形 $y_1^2+\cdots+y_r^2$，其中 $r$ 为 $f$ 的秩。

**定义 22.3 (正定/半正定)**  对任意 $x\neq0$，$x^\mathsf{T}Ax>0$（或 $\ge0$）。

**定理 22.3 (Sylvester 正定判据)**  实对称矩阵正定当且仅当前导主子式全正。

**定理 22.4 (Cholesky 分解)**  $A$ 对称正定当且仅当存在唯一上三角 $R$（对角元正）使 $A=R^\mathsf{T}R$。

**注 22.1**  正定性可由合同规范形、顺序主子式或特征值三种等价视角判断；半正定则对应把“全正”放宽为“非负”。

##### §22.3 极值原理与谱不等式

**定理 22.5 (Rayleigh-Ritz)**  最大最小特征值满足
$$
\lambda_{\min}\le\frac{x^\mathsf{T}Ax}{x^\mathsf{T}x}\le\lambda_{\max}.
$$

**定理 22.6 (Courant-Fischer 极小极大原理)**  第 $k$ 特征值可由子空间上的极值问题表征。

**定理 22.7 (Cauchy 交错与 Weyl 不等式)**  主子矩阵特征值满足交错；和矩阵特征值满足 Weyl 型夹逼。

##### §22.4 标准形的应用

**定理 22.8 (矩阵的幂等分解)**  任意 $n$ 阶方阵 $A$ 可分解为可逆矩阵 $B$ 与幂等矩阵 $C$ 的乘积，即 $A=BC$。

**定理 22.9 (实对称矩阵的乘积分解)**  秩为 $r$ 的 $n$ 阶实对称矩阵 $A$ 可表示为 $n-r$ 个秩为 $n-1$ 的实对称矩阵的乘积。

---

#### 第23章 多重线性映射与张量的计算

##### §23.0 基本定义与张量积

**补充定义 23.1 (多重线性映射)**  设 $V_1,\ldots,V_n,W$ 为线性空间，若映射 $f:V_1\times\cdots\times V_n\to W$ 对任意一个分量都是线性的，则称 $f$ 为多重线性映射.

**补充定义 23.3 (多重线性映射的矩阵表示)**  设 $f\in\mathcal{L}(V_1,V_2;W)$，$V_1$ 的基为 $\{e_1,\ldots,e_n\}$。定义 $f_i(v_2)=f(e_i,v_2)$，则 $f_i$ 是 $V_2\to W$ 的线性映射，设其矩阵为 $M_i$。对 $v_1=\sum \lambda_i e_i$，有
$$
f(v_1,v_2)=(\lambda_1 M_1+\cdots+\lambda_n M_n)\,v_2,
$$
形式地记作 $f(v_1,v_2)=v_1^\mathsf{T}\begin{pmatrix}M_1\\ \vdots\\ M_n\end{pmatrix}v_2$（为形式记号，非标准矩阵乘法）。

**补充引理 23.1 ($\mathcal{L}(V,W^*;\R)\cong\mathcal{L}(V,W)$)**  线性空间 $\mathcal{L}(V,W^*;\R)$ 与 $\mathcal{L}(V,W)$ 线性同构.

**补充定义 23.2 (张量积)**  定义 $V_1\otimes V_2=\mathcal{L}(V_1^*,V_2^*;\R)\cong\mathcal{L}(V_1^*,V_2)$，称为向量空间 $V_1$ 和 $V_2$ 的张量积.

**补充引理 23.2 (张量积的结合性)**  $(V_1\otimes V_2)\otimes V_3\cong \mathcal{L}(V_1^*,V_2^*,V_3^*;\R)\cong \mathcal{L}(V_1^*,V_2^*;V_3)$.

**补充引理 23.3 (张量积映射满射非单射)**  映射 $\otimes:V_1^*\times V_2^*\to\mathcal{L}(V_1,V_2;\R)$ 是满但不单的双线性映射.

**补充引理 23.4 (张量积核的等价刻画)**  $\ker\otimes$ 可由 $(f,0)$ 与 $(0,g)$ 生成.

**补充定理 23.1 (张量积的商空间表示)**  张量积 $V_1\otimes V_2$ 可表示为 $V_1\times V_2/\ker\otimes$.

**补充定理 23.2 (张量积的一组基)**  若 $\{e_i\}$、$\{f_j\}$ 分别为 $V_1,V_2$ 的一组基，则 $\{e_i\otimes f_j\}$ 构成 $V_1\otimes V_2$ 的一组基.

**补充定理 23.3 (张量积的泛性质)**  对任意线性空间 $U$ 和双线性映射 $\varphi:V_1\times V_2\to U$，存在唯一线性映射 $\tilde\varphi:V_1\otimes V_2\to U$ 使相应图交换.

##### §23.1 多重线性与张量积

**定义 23.1 (多重线性映射)**  映射
$$
T:V_1\times\cdots\times V_k\to W
$$
对每个分量分别线性。

**定义 23.2 (张量积的泛性质)**  $V\otimes W$ 配双线性映射 $\otimes$，使任意双线性映射唯一经线性映射因子化。

**定理 23.1 (张量积存在唯一)**  张量积对象存在，且在同构意义下唯一。

**定理 23.2 (维数与基)**  若 $\dim V=m,\dim W=n$，则
$$
\dim(V\otimes W)=mn,
$$
基可取 $\{e_i\otimes f_j\}$。

**注 23.1**  该结论本质上是双线性映射“按基分解”的计数结果，也是张量积泛性质最直接的维数后果。

**定理 23.2.1 (张量积的满射表示)**  典范双线性映射 $V\times W\to V\otimes W$ 诱导出从双线性映射到线性映射的唯一因子化。

**定理 23.2.2 (张量积的核刻画)**  在具体构造下，张量积对应的核由形如 $(v,0)$ 与 $(0,w)$ 的关系生成。

##### §23.2 坐标变换与指标记号

**定义 23.3 (张量分量与 Einstein 约定)**  重复上下指标默认求和，可统一表达坐标变换与缩并。

**定理 23.3 (张量分量变换律)**  张量分量按各指标类型（协变/逆变）分别乘以基变换矩阵与其逆矩阵。

**定理 23.3.3 (张量的坐标变换公式)**  设 $V$ 有两组基 $\{e_i\}$ 与 $\{\tilde e_i\}$，过渡矩阵为 $M$，即 $\tilde e_i=M_i^j e_j$（Einstein 求和）。设 $T$ 为 $(r,s)$ 型张量，在两组基下的分量分别为 $T_{j_1\cdots j_s}^{i_1\cdots i_r}$ 与 $\tilde T_{j_1\cdots j_s}^{i_1\cdots i_r}$，则
$$
	ilde T_{j_1\cdots j_s}^{i_1\cdots i_r}=T_{l_1\cdots l_s}^{k_1\cdots k_r}(M^{-1})_{k_1}^{i_1}\cdots(M^{-1})_{k_r}^{i_r}M_{j_1}^{l_1}\cdots M_{j_s}^{l_s},
$$
其中对所有哑指标作 Einstein 求和。

**定理 23.3.1 (张量的缩并)**  对 $(r,s)$ 型张量，选取一对上、下指标求和并删去该对指标得到缩并，阶数降为 $(r-1,s-1)$。

**定理 23.3.2 (对称张量与反对称张量的基与维数)**  若 $\dim V=n$，则 $r$ 阶对称张量空间与反对称张量空间分别具有基
$$
e_{i_1}\otimes\cdots\otimes e_{i_r},\quad 1\le i_1\le\cdots\le i_r\le n,
$$
与
$$
e_{i_1}\otimes\cdots\otimes e_{i_r},\quad 1\le i_1<\cdots<i_r\le n,
$$
其维数分别为 $\binom{n+r-1}{r}$ 与 $\binom{n}{r}$。

##### §23.3 对称、外代数与行列式

**定义 23.4 (对称张量与反对称张量)**  在指标置换下保持不变或变号。

**定义 23.5 (外积与外代数)**  以反对称化构造 $\Lambda^kV$。

**定理 23.4 (行列式的外代数解释)**  线性算子在 $\Lambda^nV$ 上的诱导作用是乘以 $\det A$。

**定理 23.5 (诱导映射函子性)**  线性映射可自然诱导张量积、对称幂、外幂上的线性映射，且与复合兼容。

**定理 23.6 (行列式的外代数解释)**  线性算子在 $\Lambda^nV$ 上的诱导作用是乘以 $\det A$。

**定理 23.7 (对称/反对称分解)**  任意张量可分解为对称部分与反对称部分之和；在低阶情形下，分别对应对称积与外积的投影。

**定理 23.8 (外积的反交换性)**  若 $T\in\bigwedge^r V$、$S\in\bigwedge^s V$，则 $T\wedge S=(-1)^{rs}S\wedge T$。

**定理 23.9 (行列式的外代数解释)**  线性算子在 $\Lambda^nV$ 上的诱导作用等于乘以 $\det A$。

**定理 23.10 (对称张量代数与多项式代数)**  对称张量代数与齐次多项式代数同构，对称积对应多项式乘法。

---

#### 第24章 线性代数与微积分

##### §24.0 范数与连续性

**补充定义 24.0 (线性映射的范数)**  设 $A$ 为线性映射，则
$$
\|A\|=\sup_{x\neq0}\frac{\|Ax\|}{\|x\|}.
$$

**补充定义 24.1 (矩阵的内积)**  对矩阵 $A,B$，定义
$$
\langle A,B\rangle_F=\operatorname{tr}(A^\mathsf{T}B),\qquad \|A\|_F=\sqrt{\langle A,A\rangle_F}.
$$

**补充定义 24.2 (``元素形式''范数)**  在有限维空间的坐标表示下，范数可由分量和诱导矩阵内积共同表达；这一定义与前述矩阵内积相容。

**补充定理 24.0 (有限维范数等价)**  有限维空间任意两个范数等价，从而连续性与有界性概念等价。

**补充定理 24.1 (线性映射连续等价有界)**  线性映射连续当且仅当有界。

##### §24.1 范数与连续性

**定义 24.1 (诱导算子范数)**  
$$
\|A\|=\sup_{x\neq0}\frac{\|Ax\|}{\|x\|}.
$$

**定义 24.2 (Frobenius 范数与矩阵内积)**  
$$
\langle A,B\rangle_F=\operatorname{tr}(A^\mathsf{T}B),\quad \|A\|_F=\sqrt{\langle A,A\rangle_F}.
$$

**定理 24.1 (有限维范数等价)**  有限维空间任意两个范数等价，从而连续性、有界性概念等价。

**定理 24.2 (线性映射连续等价有界)**  线性映射连续当且仅当有界。

**定义 24.2.1 (收敛)**  在赋范空间 $V$ 中，序列 $\{x^{(k)}\}$ 收敛到 $x$，若 $\|x^{(k)}-x\|\to 0$。

**定义 24.2.2 (连续)**  设 $f:X\to Y$ 为度量空间间映射，若对任意 $x_0\in X$ 和任意 $\varepsilon>0$，存在 $\delta>0$ 使 $d_X(x,x_0)<\delta$ 蕴含 $d_Y(f(x),f(x_0))<\varepsilon$，则称 $f$ 在 $x_0$ 处连续。

**定理 24.1.1 (Weierstrass 定理)**  设 $S$ 是有限维实赋范空间的紧子集，$f:S\to\mathbf{R}$ 连续，则 $f$ 在 $S$ 上可取到最大值和最小值。

**定义 24.2.3 (预范数)**  若函数 $p:V\to\mathbf{R}$ 满足正性、齐次性与连续性，则称为预范数。

**定理 24.1.2 (预范数等价性)**  有限维实向量空间上任意两个预范数彼此等价，因此任意两个范数等价。

**定义 24.2.4 (有界线性映射)**  若存在 $M\ge0$ 使 $\|Ax\|\le M\|x\|$，则线性映射 $A$ 称为有界。

**定理 24.1.3 (有界线性变换定理)**  线性映射有界当且仅当连续；等价地，当且仅当它把有界集映成有界集。

**定理 24.1.4 (可逆线性算子的稳定性)**  可逆线性算子的集合是开集，且在该集合上取逆映射连续。

**定理 24.1.5 (可逆线性算子的稳定性：范数判据)**  若 $A$ 可逆且 $B\in\mathcal{L}(\mathbf{R}^n)$ 满足 $\|B-A\|\cdot\|A^{-1}\|<1$，则 $B$ 可逆。

##### §24.2 微分与局部结构定理

**定义 24.3 (Fréchet 导数与 Jacobian)**  可微映射在一点的一阶线性近似由 Jacobian 表示。

**定理 24.3 (链式法则)**  
$$
D(f\circ g)(x)=Df(g(x))\,Dg(x).
$$

**定理 24.4 (反函数定理)**  若 $Df(x_0)$ 可逆，则 $f$ 在 $x_0$ 邻域局部可逆且逆映射可微。

**推论 24.1 (反函数的微分)**  若 $f:D\to\Delta$ 可逆且 $f^{-1}$ 可微，则
$$
Jf^{-1}(y)=\big[Jf(f^{-1}(y))\big]^{-1}.
$$

**定理 24.5 (隐函数定理)**  若对某组变量的偏导块可逆，则约束方程可局部解出隐函数。

**定理 24.4.1 (隐函数的雅可比公式)**  若 $y=\psi(x)$ 由隐函数定理局部确定，则
$$
J\psi(x)=-\big[J_y f(x,\psi(x))\big]^{-1}J_x f(x,\psi(x)).
$$

**定理 24.6 (秩定理/常秩定理)**  常秩映射在局部可化为标准投影型坐标表达。

**定理 24.6.1 (秩定理详述)**  设 $E\subset\mathbf{R}^n$ 为开集，$f:E\to\mathbf{R}^m$ 为 $C^1$ 映射，且对任意 $x\in E$，$Jf(x)$ 的秩为 $l$。固定 $x_0\in E$，令 $A=Jf(x_0)$，设 $Y_1=\operatorname{im} A$，$P$ 为 $\mathbf{R}^m$ 到 $Y_1$ 的投影，$Y_2=\ker P$。则存在开集 $U\subset E$（$x_0\in U$）与 $V\subset\mathbf{R}^n$，以及 $C^1$ 微分同胚 $H:V\to U$，使得
$$
f(H(x))=Ax+\varphi(Ax),\quad \forall x\in V,
$$
其中 $\varphi$ 是 $A(V)\subset Y_1$ 到 $Y_2$ 的 $C^1$ 映射。

**定义 24.3.1 (方向导数)**  设 $f:\mathbf{R}^n\to\mathbf{R}$，若
$$
\lim_{h\to0}\frac{f(x_0+hv)-f(x_0)}{h\|v\|}
$$
存在，则称其为 $f$ 在 $x_0$ 沿 $v$ 的方向导数。

**定义 24.3.2 (微分)**  若存在线性映射 $A$ 使
$$
\lim_{\|h\|\to0}\frac{|f(x_0+h)-f(x_0)-Ah|}{\|h\|}=0,
$$
则称 $A$ 为 $f$ 在 $x_0$ 处的微分。

**定理 24.2.1 (方向导数与微分的关系)**  若 $f$ 在 $x_0$ 处可微，则沿任意方向 $u$ 的方向导数存在，且等于微分作用在 $u$ 上；对标量值函数，这等于梯度与方向的内积。

**定理 24.2.2 (向量值函数的微分表示)**  若 $f=(f_1,\ldots,f_m)$ 可微，则其微分矩阵为 $Jf(x_0)=(\partial f_i/\partial x_j)$。

**定理 24.2.3 (微分中值估计)**  在凸域上，若 $f$ 处处可微，则两点值差可由某中间点的雅可比矩阵控制；标量情形退化为梯度中值估计。

**定理 24.2.4 (压缩映射原理)**  在完备度量空间中，压缩映射存在唯一不动点。

**补充定理 24.2.5 (微分中值定理)**  设 $D\subset \mathbf{R}^n$ 为凸域，函数 $f\colon D\to \mathbf{R}$ 在 $D$ 中处处可微，则任给 $x,y\in D$，存在 $\theta\in(0,1)$ 使得
$$
f(y)-f(x)=\nabla f(\xi)\cdot (y-x),\qquad \xi=\theta x+(1-\theta)y.
$$

##### §24.3 估计与积分变换

**定理 24.3.1 (拟微分中值定理)**  若 $Df$ 有界，则
$$
\|f(x)-f(y)\|\le M\|x-y\|.
$$

**定义 24.3.2 (Lipschitz 条件)**  存在 $L$ 使
$$
\|f(x)-f(y)\|\le L\|x-y\|.
$$

**定理 24.3.4 (线性变换的体积公式)**  设 $\varphi:\mathbf{R}^n\to\mathbf{R}^n$ 为线性映射，$A\subset\mathbf{R}^n$ 可求体积，则 $\varphi(A)$ 也可求体积，且
$$
\nu(\varphi(A))=|\det\varphi|\,\nu(A).
$$

**定理 24.3.3 (重积分换元法)**  可逆可微变换下积分满足 Jacobian 行列式变换律。

**引理 24.1 (第一覆盖引理)**  可求体积的有界集合可由有限个互不相交的矩形内外逼近。

**引理 24.2 (第二覆盖引理)**  可求体积的有界集合也可由有限个互不相交的球体内外逼近。

**引理 24.3 (局部 Lipschitz 的零测集保持性)**  局部 Lipschitz 映射保持零测集性质；若原像与像均可求体积，则体积有 $\rho^n$ 量级估计。

**引理 24.4 (微分线性化误差估计)**  $C^1$ 映射在小区域上可由 Jacobian 线性化，并给出一致误差上界。

**引理 24.5 (小区域上的体积变化估计)**  小区域在 $C^1$ 映射下的体积变化可由对应 Jacobian 行列式近似控制。

---

#### 第25章 线性代数与最优化问题

##### §25.1 线性规划与几何框架

**定义 25.1 (优化问题标准形式)**  
$$
\min f(x)\quad\text{s.t.}\quad x\in\Omega.
$$

**定义 25.2 (线性规划)**  
$$
\min c^\mathsf{T}x\quad\text{s.t.}\quad Ax=b,\ x\ge0.
$$

**定理 25.1 (线性规划基本定理)**  若线性规划最优解存在，则至少有一个最优解取在可行域的极点（基可行解）。

##### §25.2 对偶理论

**定义 25.3 (原问题与对偶问题)**  线性规划可构造对应对偶问题，目标与约束在转置意义下互换。

**定理 25.2 (弱对偶)**  任意原可行解与对偶可行解满足
$$
c^\mathsf{T}x\ge b^\mathsf{T}y
$$
（最小化原问题情形）。

**定理 25.3 (强对偶与互补松弛)**  在可行且满足适当条件时，原对偶最优值相等；最优解满足互补松弛条件。

##### §25.3 下降算法与二阶方法（补全框架）

**方法 25.1 (梯度下降)**  
$$
x_{k+1}=x_k-\eta_k\nabla f(x_k).
$$
在 $L$-光滑、$\mu$-强凸情形可得到线性收敛估计。

**方法 25.2 (牛顿法)**  
$$
x_{k+1}=x_k-[\nabla^2f(x_k)]^{-1}\nabla f(x_k),
$$
在解附近并满足 Hessian 非奇异时通常二次收敛。

**定义 25.4 (KKT 条件)**  约束优化一阶必要条件由梯度平衡、可行性、乘子非负与互补条件构成。

**方法 25.3 (投影梯度与内点法框架)**  
1. 投影梯度：每步先梯度下降，再投影回可行集。
2. 内点法：用势函数/障碍函数将不等式约束并入目标，迭代逼近边界最优点。

**注 25.1 (本章来源说明)**  原讲义第25章以目录与提纲为主，以上内容为按课程主线补全的核心定义、定理与算法框架，便于与前述章节衔接复习。

---

#### 第26章 线性代数与最优化问题

**注 26.1**  汇总3中的第26章仅给出章节框架，没有展开更细的定义与定理，因此本章这里只保留与其对应的最小覆盖层级，避免遗漏章节本身。

##### §26.1 线性规划的几何

**定义 26.1 (线性规划标准形式)**  线性规划可写为
$$
\min c^\mathsf{T}x\quad\text{s.t.}\quad Ax\le b,\ x\ge0.
$$

**定义 26.2 (可行域)**  满足全部约束条件的向量集合称为可行域，它通常是一个凸多面体。

**定理 26.1 (线性规划基本定理)**  若线性规划问题有最优解，则至少有一个最优解出现在可行域的顶点（极点）上。

##### §26.2 线性规划的对偶

**定义 26.3 (对偶问题)**  对于给定的原始线性规划问题，存在一个对应的对偶线性规划问题。

**定理 26.2 (弱对偶定理)**  原始问题的任何可行解的目标函数值都不大于对偶问题的任何可行解的目标函数值。

**定理 26.3 (强对偶定理)**  若原始问题有最优解，则对偶问题也有最优解，且两者的最优值相等。

##### §26.3 下降方法

**定义 26.4 (下降方向)**  对于目标函数 $f(x)$，若方向 $d$ 满足 $\nabla f(x)^\mathsf{T}d<0$，则称 $d$ 为在点 $x$ 处的下降方向。

**方法 26.1 (梯度下降法框架)**  从初始点 $x_0$ 开始，迭代更新
$$
x_{k+1}=x_k-\alpha_k\nabla f(x_k),
$$
其中 $\alpha_k>0$ 为步长。

**定理 26.4 (收敛性条件)**  在一定条件下，例如 $f$ 为凸函数且 Lipschitz 连续，梯度下降法产生的序列收敛到驻点。

**注 26.2**  这一章在当前工作本中与前一章的优化内容存在主题重叠，但为了与汇总3保持章节覆盖一致，仍保留为独立章节。




