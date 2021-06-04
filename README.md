# Alpian-Test

This private repository is created to write exercise solutions for Alpian

## Installation

The scripts can be run for Python version >=3.6.8 release

Use the package manager [pip](https://pypi.org/project/numpy/) to install numpy.

```bash
pip install numpy
```

## Project Files Description

This project includes 3 executable files, 3 text files inside sub-folder *Nandani_Garg*

### Executable Files:
**exercise1.py** - Python solution for exercise 1, uses **ex1_input.txt** as the sample input file, prints output (number of pizzerias that deliver pizzas to the block with the greatest selection of pizzas) on the terminal.

**exercise2.py** - Python solution for exercise 2, uses **ex2_input.txt** as the sample input file, prints output (the maximum distance of the safest path on Mr. Little Z's way to Zearth upto 2 decimal places) on the terminal.

**graph.py** - Dependency file used in **exercise2.py**

### Input Files:
**ex1_input.txt** - Contains sample input for exercise 1

**Input File Format**

The first line of the input contains the two numbers N and M separated by space, and both numbers are on the interval [1, 1000]. The number N represents the dimension of the city in blocks (the city has NxN blocks). M is the number of pizzerias in the city. The following M lines contain information about each pizzeria, given by the three numbers X, Y, K(space separated). The numbers X and Y represent the block where the pizzeria is located, (1 <= X, Y <= N) and the number K represents the maximum distance that the given pizzeria's delivery guy will travel to deliver pizza (1 <= K <= 1000). For e.g. -

```
5 2
3 3 2
1 1 2
```

**ex2_inpu2.txt** - Contains sample input for exercise 2

**Input File Format**

The first line of the input contains three space-separated real numbers, each from the interval [-10000.00, 10000.00], representing the 3D coordinates of the planet Zearth. The next line contains a number N, corresponding to the number of teleportation stations in space (1<=N<=500). Each of the next N lines contains three real numbers(space-separated) each from the interval [-10000.00, 10000.00], representing the 3D coordinates for each station. For e.g. -
```
2.00 2.00 2.00
3
0.00 0.00 2.00
0.00 2.00 2.00
2.00 0.00 0.00
```

### Document File:

**Approaches_brief.txt** - Explains decisions taken for implementing the solutions. It contains time complexity analysis as well.


## Usage
Run the below scripts inside *Nandani_Garg* directory.

### Exercise 1
To execute Exercise 1, run the command below with single input file passed as the argument. Input file name can be anything. 

For eg - For input file name **ex1_input.txt**, run the command below. It will print output(number of pizzerias that deliver pizzas to the block with the greatest selection of pizzas) on the terminal.


```
python exercise1.py ex1_input.txt

```

### Exercise 2
To execute Exercise 2, run the command below with single input file passed as the argument. Input file name can be anything. Make sure dependency files **graph.py** and **ex2_input.txt** are in the same folder as **exercise2.py**

For eg - For input file name **ex2_input.txt**, run the command below. It will print output(the maximum distance of the safest path on Mr. Little Z's way to Zearth upto 2 decimal places) on the terminal.

```
python exercise2.py ex2_input.txt

```
