# BlueMO

## 🚀 BlueMO: A Comprehensive Collection of Challenging Mathematical Olympiad Problems from the Little Blue Book Series

[![Website](https://img.shields.io/badge/Project-Website-green)](https://iiis-ai.github.io/AutoMathText-V2) 
[![Technical Report](https://img.shields.io/badge/Technical-Report-blue)](https://yifanzhang-pro.github.io/BlueMO/BlueMO.pdf)
[![License: CC-BY-ND-4.0](https://img.shields.io/badge/License-CCBYND4.0-yellow.svg)](https://creativecommons.org/licenses/by-nd/4.0/)
[![BlueMO](https://img.shields.io/badge/Huggingface-Datasets-blue)](https://huggingface.co/datasets/math-ai/BlueMO) 

**BlueMO** is a comprehensive and challenging dataset comprising mathematical olympiad problems paired with detailed solutions, meticulously curated from the esteemed "Little Blue Book" (小蓝书) series (Second Edition)—a vital resource for Chinese students training for national and international olympiad math competitions.

Designed to advance and assess sophisticated reasoning in LLMs, this dataset serves as a benchmark or training resource for high-level problem-solving in AI.

## Introduction for "Little Blue Book" (小蓝书)

The "Little Blue Book" (小蓝书) series, published by East China Normal University Press, is a cornerstone resource for students striving to master mathematical olympiads. Renowned for its depth, challenging problems, and elegant solutions, the series spans critical domains—Sets, Trigonometric, Geometry, Number Theory, Graph Theory, and Extremal Combinatorics—providing rigorous training for olympiad competitions.

## About Dataset

BlueMO encompasses a total of 14 volumes from the third edition of the "Little Blue Book" series, covering a wide range of mathematical topics for both middle and high school levels.

The dataset is structured as follows:

**High School Collection:**

* 小蓝书高中卷1 集合 - Little Blue Book High School Vol.1: Sets

* 小蓝书高中卷2 函数与函数方程 - Little Blue Book High School Vol.2: Functions & Functional Equations

* 小蓝书高中卷3 三角函数 - Little Blue Book High School Vol.3: Trigonometric Functions

* 小蓝书高中卷4 平均值不等式与柯西不等式 - Little Blue Book High School Vol.4: Mean Value & Cauchy Inequalities

* 小蓝书高中卷5 不等式的解题方法与技巧 - Little Blue Book High School Vol.5: Methods & Techniques for Solving Inequalities

* 小蓝书高中卷6 数列与数学归纳法 - Little Blue Book High School Vol.6: Sequences & Mathematical Induction

* 小蓝书高中卷7 平面几何 - Little Blue Book High School Vol.7: Plane Geometry

* 小蓝书高中卷8 复数与向量 - Little Blue Book High School Vol.8: Complex Numbers & Vectors

* 小蓝书高中卷9 几何不等式 - Little Blue Book High School Vol.9: Geometric Inequalities

* 小蓝书高中卷10 数论 - Little Blue Book High School Vol.10: Number Theory

* 小蓝书高中卷11 组合数学 - Little Blue Book High School Vol.11: Combinatorics

* 小蓝书高中卷12 图论 - Little Blue Book High School Vol.12: Graph Theory

* 小蓝书高中卷13 组合极值 - Little Blue Book High School Vol.13: Extremal Combinatorics

* 小蓝书高中卷14 高中数学竞赛中的解题方法与策略 - Little Blue Book High School Vol.14: Problem-Solving Methods & Strategies for Math Competitions

## Potential Usages

This dataset is a resource for AI researchers and developers, with key applications including:

* Training & Fine-Tuning – Enhancing large language models’ capabilities in advanced mathematical reasoning.

* AI Evaluation – Benchmarking the problem-solving proficiency and logical rigor of AI systems.

* Formal Verification – Formalizing problems into mathematical languages (e.g., LEAN) to evaluate AI's reasoning capability with formal methods.

* Comparative Analysis – Systematically assessing reasoning skills across different models and methodologies.

## How to Use

We provide the raw data (*.tex) and the processed dataset, including calculation, proof, text and images they referred to.

A case in `calculation`.

```json
{
    "source_file": "./raw_volume-zh/volume1/chapter1.tex",
    "problem_type": "calculation",
    "problem": "例1. 设集合 $M=\\left\\{x |{\\frac{a x-5}{x^{2}-a}}<0,\\,x\\in\\mathbb{R}\\right\\}$ \n(1)当 $a=4$ 时,化简集合 $M$ ;\n(2)若 $3\\in M,$ ,且 $5\\notin M,$ 求实数a的取值范围.",
    "solution": "分析: 化简集合 $M$, 实际上就是解不等式 ${\\frac{a x-5}{x^{2}-a}}<0.$ \n解: (1) 当 $a=4$ 时,有\n$$\n{\\frac{4x-5}{x^{2}-4}}<0\\,, \n$$\n即\n$$\n\\left(x-\\frac{5}{4}\\right)(x+2)(x-2)<0. \n$$\n$x<-2$ 或 ${\\frac{5}{4}}<x<2.$ \n所以 $M=(-\\infty,-2)\\cup\\bigl({\\frac{5}{4}}, 2\\bigr).$ \n(2)由 $3\\in M,$ 得 ${\\frac{3a-5}{3^{2}-a}}<0$,即 $\\left(a-\\frac{5}{3}\\right)(a-9)\\geqslant0$ ,所以\n$$\na<{\\frac{5}{3}}或a>9. \n$$\n由 $5\\notin M$ 得, ${\\frac{5a-5}{5^{2}-a}}\\geqslant0$ 或 $5^{2}-a=0$ ,所以\n$$\n1\\leq a\\leq25. \n$$\n可得 $x\\in\\left[1,{\\frac{5}{3}}\\right)\\cup\\left(9,25\\right]$.\n说明: $5\\notin M$ 隐含了条件 $5^{2}-a=$ 0,这是容易被忽视的.\n由概括原则我们知道,判断一个对象 $x$ 是否为集合 $S$ 的元素,等价于判断 $x$ 是否具有性质 $P$.",
    "remark": "",
    "figures": []
}
```

`source_file`: Path to the original .tex source file containing this problem.

`problem_type`: Problem category (e.g., "calculation", "proof", etc.).

`problem`: Complete problem statement in LaTeX format, including sub-questions.

`solution`: Step-by-step solution with mathematical derivations in LaTeX.

`remark`: Additional notes or comments about the problem (empty if none).

`figures`: Array containing any associated diagram files (empty if none).


## Citation


If you use the BlueMO dataset in your research, please consider citing it as follows:

```bibtex
@misc{bluemo2024,
      title={BlueMO: A comprehensive collection of challenging mathematical olympiad problems from the little blue book series}, 
      author={Chen, Yizhou and Luo, Yifan and Zhang, Yifan and Yuan, Yang},
      year={2024},
}
```
