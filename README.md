# MATH353 - Numerical Analysis

**Course:** MAT353 - Numerical Analysis  
**Student:** Mert Eldemir  
**Student Number:** 25120205086

This repository contains projects, homework assignments, and implementations of numerical methods studied in the MAT353 course. Each section explores different numerical techniques with Python implementations, visualizations, and theoretical explanations.

---

## Table of Contents

- [Numerical Errors](#numerical-errors)
- [Matrix Operations](#matrix-operations)
- [Root Finding Methods](#root-finding-methods)
- [Homework: Euler and Heun Methods](#homework-euler-and-heun-methods)
- [Term Project: Heat Dissipation Simulation](#term-project-heat-dissipation-simulation)
- [Requirements](#requirements)

---

## Numerical Errors

**Location:** [`Numerical-Errors/`](Numerical-Errors/)

Understanding numerical errors is fundamental to computational mathematics. This section covers:

- **Absolute Error**: Direct difference between true and approximate values
- **Relative Error**: Error as a fraction of the true value
- **Percentage Error**: Relative error expressed as percentage
- **Rounding Errors**: Impact of finite precision in floating-point arithmetic

**Files:**

- [`NumericalErrors.md`](Numerical-Errors/NumericalErrors.md) - Comprehensive theoretical guide with formulas and examples
- [`rounding_error.py`](Numerical-Errors/rounding_error.py) - Python demonstrations of rounding errors

**Key Concepts:**

- Error propagation in numerical computations
- Machine epsilon and floating-point precision
- Practical examples using exponential and trigonometric functions

---

## Matrix Operations

**Location:** [`Matrix-Operations/`](Matrix-Operations/)

Implementation of fundamental matrix operations and linear algebra computations using NumPy.

**File:**

- [`Matrix.ipynb`](Matrix-Operations/Matrix.ipynb) - Interactive Jupyter notebook

**Topics Covered:**

- Matrix creation (zeros, ones, identity matrices)
- Basic operations: addition, subtraction, scalar multiplication
- Matrix multiplication and element-wise operations
- Advanced operations: transpose, determinant, inverse
- Performance comparisons and visualizations
- Practical applications of linear algebra

**Technologies Used:**

- NumPy for efficient array operations
- Matplotlib for visualizations
- Performance timing analysis

---

## Root Finding Methods

**Location:** [`Root-Finding/`](Root-Finding/)

Comprehensive study of numerical methods for finding roots of nonlinear equations.

**File:**

- [`Root-Finding-Methods.ipynb`](Root-Finding/Root-Finding-Methods.ipynb) - Complete implementation with visualizations

**Methods Implemented:**

### 1. Bisection Method

- Reliable bracketing method
- Guaranteed convergence
- Visual demonstrations of interval halving

### 2. Newton-Raphson Method

- Fast convergence with derivative information
- Iterative formula visualization
- Comparison with other methods

### 3. Secant Method

- Approximates derivative numerically
- Two-point iteration scheme
- Convergence analysis

### 4. Fixed-Point Iteration

- Transform equation to x = g(x) form
- Convergence criteria and visualization
- Multiple function examples

**Features:**

- Convergence rate comparisons
- Error analysis and iteration tracking
- Graphical representation of each method
- Real-world function examples

**Technologies Used:**

- NumPy for numerical computations
- Matplotlib for method visualization
- Custom plotting functions for convergence analysis

---

## Homework: Euler and Heun Methods

**Location:** [`Homework/`](Homework/)

Comparative study of numerical methods for solving first-order Initial Value Problems (IVPs) in differential equations.

**Files:**

- [`Euler-and-Heun-method.ipynb`](Homework/Euler-and-Heun-method.ipynb) - Complete implementation
- [`Homework.md`](Homework/Homework.md) - Assignment requirements and guidelines

**Project Overview:**

This homework explores two fundamental numerical methods for solving ordinary differential equations:

### Euler Method

- Simple first-order method
- Uses tangent line approximation at each step
- Fast but accumulates error on curves

### Heun Method (Improved Euler)

- Predictor-corrector approach
- Averages slopes at interval endpoints
- Significantly better accuracy than Euler

**Three IVPs Solved:**

1. **Logistic Growth**: $y' = y(1 - y/2)$, $y(0)=0.5$

   - Models population dynamics with carrying capacity
   - S-curve behavior demonstration

2. **Damped/Forced ODE**: $y' = -2y + 2 - e^{-4x}$, $y(0)=1$

   - System with exponential forcing and damping
   - Fast decay behavior

3. **Oscillatory Forcing**: $y' = \cos(x) - y$, $y(0)=0$
   - Driven harmonic oscillator
   - Phase lag and amplitude analysis

**Deliverables:**

- Theoretical explanations in student's own words
- Mathematical formulas for both methods
- Python implementation for both solvers
- Comparison tables showing x, y values, and errors
- Graphical comparisons with exact solutions
- Interpretation of accuracy differences

**Technologies Used:**

- NumPy for numerical arrays
- Pandas for data tables
- Matplotlib for comparative plots

---

## Term Project: Heat Dissipation Simulation

**Location:** [`Term-Project/`](Term-Project/)

Numerical investigation of transient heat dissipation in a one-dimensional rod using the Forward Time-Centered Space (FTCS) explicit finite difference method.

**Files:**

- [`Mert_Eldemir_25120205086_MAT353.ipynb`](Term-Project/Heat-Dissipation-in-a-Thin-Rod.ipynb) - Complete implementation
- [Project Report](Term-Project/Heat-Dissipation-in-a-Thin-Rod.pdf) (in Turkish)

**Physical Problem:**

Simulates heat conduction in a 1-meter rod ($L = 1.0$) with:

- Initial temperature: $u(x, 0) = \sin(\pi x/L)$ (hottest at center)
- Boundary conditions: $u(0,t) = u(L,t) = 0$ (fixed at 0°C)
- Thermal diffusivity: $\alpha = 1.0$ m²/s

**Mathematical Model:**

Heat equation: $\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}$

Exact solution: $u(x,t) = \exp\left(-\alpha (\pi/L)^2 t\right) \sin(\pi x/L)$

**Numerical Method: FTCS**

**Update formula:**
$$u_i^{n+1} = u_i^n + r(u_{i-1}^n - 2u_i^n + u_{i+1}^n), \quad r = \alpha \frac{\Delta t}{(\Delta x)^2}$$

**Stability condition:** $r \leq 0.5$

**Implementation:**

- Base grid: $N = 50$ intervals, $\Delta t = 0.0001$ s, $T = 0.1$ s
- Stability parameter: $r = 0.25$ (stable)
- Convergence study: 6 resolutions (N = 25 to 800)

**Key Features:**

1. **FTCS discretization** with complete stability analysis
2. **Validation** against analytical solution at final time
3. **Error analysis**: $L_\infty$ and RMS error metrics with spatial distribution
4. **Convergence study**: Demonstrates second-order spatial accuracy ($\mathcal{O}((\Delta x)^2)$)
5. **Time evolution**: Temperature snapshots and error tracking over time

**Results:**

- FTCS accurately captures smooth heat decay without oscillations
- Grid refinement confirms second-order convergence (halving $\Delta x$ → 4× error reduction)
- Numerical solution matches analytical solution with negligible error

**Visualizations:**

- Temperature evolution at multiple time levels
- Numerical vs exact comparison
- Error distribution and convergence plots
- Maximum temperature decay curve

**Applications:** Heat sink design, metal cooling processes, thermal conductivity testing

**Technologies:** NumPy, Matplotlib, explicit time-stepping loops

---

## Requirements

**Location:** [`requirements.txt`](requirements.txt)

### Core Dependencies:

- **NumPy**: Numerical computing and array operations
- **Matplotlib**: Plotting and visualization
- **Pandas**: Data manipulation and tabular display
- **Jupyter**: Interactive notebook environment
- **IPython**: Enhanced Python shell for notebooks

### Installation:

```bash
# Clone the repository
git clone https://github.com/yourusername/MATH353-Numerical-Analysis.git
cd MATH353-Numerical-Analysis

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
