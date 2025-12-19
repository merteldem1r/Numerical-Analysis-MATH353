# Numerical Analysis Term Project - Heat Dissipation in a Rod

**Student:** Mert Eldemir  
**Student Number:** 25120205086  
**Course:** MAT353 - Numerical Analysis

---

## What This Project Does

This project simulates how heat spreads out (dissipates) along a thin metal rod over time. Imagine you have a hot metal rod, and you suddenly place both ends in ice water - this project calculates how the temperature changes at every point along the rod as time passes.

Instead of running a physical experiment, we use numerical methods (computer calculations) to predict what would happen. The project also checks if these calculations are accurate by comparing them to a mathematical formula that gives the exact answer.

---

## The Physical Problem

### The Setup
- We have a thin rod (like a metal wire) that's 1 meter long
- At the start, the rod is hottest in the middle and cooler toward the ends
- Both ends of the rod are kept at 0°C (like being in ice water)
- Heat naturally flows from hot areas to cold areas
- We want to know: what's the temperature at every point along the rod at any moment in time?

### Real-World Applications
This type of problem appears in many engineering situations:
- Cooling of heat sinks in computers
- Thermal management in electronic devices
- Heat treatment of metal parts
- Analysis of heat exchangers
- Design of thermal insulation systems

---

## The Mathematical Model (Simplified Explanation)

The temperature evolution is governed by a **heat diffusion equation**. In plain English, this equation says:

> "The rate at which temperature changes at any point depends on how curved the temperature profile is at that point."

If you have a sharp peak of hot temperature surrounded by cooler areas, heat will flow away from that peak quickly, causing rapid cooling. If the temperature is smooth and flat, changes happen more slowly.

The equation uses:
- **Position along the rod (x)**: from 0 to 1 meter
- **Time (t)**: how long the cooling has been happening
- **Temperature u(x,t)**: the temperature at position x and time t
- **Thermal diffusivity (α)**: how quickly the material conducts heat (we use α = 1 for simplicity)

---

## How We Solve It: The FTCS Method

### Why We Need Numerical Methods
The heat equation is a "partial differential equation" - a type of equation that's very difficult or impossible to solve by hand for most real-world situations. Even though our simple setup has an exact formula, in practice engineers face complex shapes, varying materials, and changing conditions where only numerical methods work.

### The FTCS Approach (Forward Time - Centered Space)

We break down the problem into small, manageable pieces:

1. **Divide the rod into segments**: Instead of calculating temperature at infinite points, we pick specific spots (51 points from 0 to 1 meter, spaced 0.02 meters apart)

2. **Take small time steps**: Instead of continuous time, we move forward in tiny jumps (0.0001 seconds at a time)

3. **Update temperatures step by step**: At each time step, we calculate new temperatures using a simple rule:
   - Look at the temperature at three neighboring points
   - The new temperature at the middle point depends on how much hotter or cooler it is compared to its neighbors
   - If a point is hotter than its neighbors, it cools down
   - If it's cooler than its neighbors, it heats up

### The Update Formula in Plain English

For any interior point on the rod:
```
New temperature = Current temperature + adjustment based on neighbors
```

The adjustment is calculated by:
```
adjustment = r × (left neighbor + right neighbor - 2 × current point)
```

Where `r` is a stability parameter that must be chosen carefully (we use r = 0.4).

### Why This Works
This method mimics how heat actually flows: hot spots transfer energy to cooler neighbors, gradually evening out the temperature distribution.

---

## Implementation Steps

### 1. **Initial Setup**
- Define the physical rod (length L = 1 meter)
- Set material property (thermal diffusivity α = 1.0)
- Choose grid spacing (50 intervals, so Δx = 0.02 meters)
- Choose time step (Δt = 0.0001 seconds)
- Create initial temperature profile: hottest in the middle, zero at ends

### 2. **Time Integration Loop**
The code runs through these steps 1,000 times (to simulate 0.1 seconds total):
- For each interior point, calculate the new temperature using FTCS formula
- Keep both ends at 0°C (boundary conditions)
- Move to the next time step
- Optionally save snapshots to see how temperature evolves

### 3. **Visualization**
The project creates plots showing:
- Initial temperature distribution (a smooth curve peaking in the middle)
- Temperature profiles at different times (showing gradual cooling)
- How the hot center cools down while heat flows toward the cold ends

---

## Validation: Making Sure We Got It Right

### Comparing to the Exact Solution
For this particular problem (sinusoidal initial temperature), mathematicians have derived an exact formula. The project calculates:
1. The numerical solution (from FTCS method)
2. The exact analytical solution (from the mathematical formula)
3. The difference (error) between them

### Error Metrics
Two types of errors are measured:
- **Maximum error**: The biggest difference at any single point
- **RMS error**: An average measure of error across all points

Both errors are very small (around 0.000002), confirming the method works correctly.

---

## Convergence Study: Does It Get Better with Finer Grids?

A good numerical method should give more accurate results when we use finer grids (more points). The project tests this by:

1. Running the simulation with 25, 50, 100, and 200 grid points
2. Measuring the error for each case
3. Plotting error versus grid spacing

### What We Found
- When we double the number of points (halve the spacing), the error drops by about 4 times
- This "second-order convergence" is exactly what the theory predicts
- It confirms the FTCS method is working as expected

The log-log plot shows a straight line with slope -2, which is the mathematical signature of second-order accuracy.

---

## Key Results and Insights

### Physical Observations
1. **Heat flows from hot to cold**: The initially peaked temperature distribution gradually flattens out
2. **Boundaries matter**: The fixed 0°C ends continuously pull heat away from the rod
3. **Exponential decay**: The maximum temperature decreases exponentially over time
4. **Smooth evolution**: No oscillations or instabilities - the cooling process looks physically realistic

### Numerical Observations
1. **Stability is crucial**: The parameter r = α·Δt/(Δx)² must stay below 0.5 for stability
2. **Trade-offs exist**: Smaller time steps are more accurate but require more computation
3. **Grid refinement works**: Finer grids reliably produce more accurate results
4. **Boundary treatment**: Explicitly enforcing boundary conditions prevents errors from accumulating

---

## Methods and Tools Used

### Numerical Method
- **FTCS (Forward Time - Centered Space)**: An explicit finite difference scheme
- **Finite differences**: Approximates derivatives using nearby point values
- **Explicit time-stepping**: Each new time level is calculated directly from the previous one

### Programming Tools
- **Python**: Programming language
- **NumPy**: For numerical arrays and computations
- **Matplotlib**: For creating plots and visualizations
- **Jupyter Notebook**: Interactive development environment

### Mathematical Techniques
- **Discretization**: Breaking continuous space and time into discrete points
- **Taylor series**: Theoretical foundation for finite difference approximations
- **Error analysis**: Quantifying accuracy using norms
- **Convergence analysis**: Testing how error decreases with grid refinement

---

## What Makes This Project Interesting

### Educational Value
This project demonstrates fundamental concepts in:
- **Numerical analysis**: How to solve equations that can't be solved by hand
- **Computational physics**: Simulating real physical processes
- **Algorithm validation**: Verifying that computer calculations are correct
- **Error quantification**: Understanding limitations of numerical methods

### Practical Relevance
The techniques used here scale up to real engineering problems:
- More complex geometries (2D and 3D heat transfer)
- Varying material properties
- Time-dependent boundary conditions
- Coupled physics (heat + fluid flow, heat + deformation)

### Balance of Theory and Practice
The project successfully combines:
- Mathematical rigor (exact solutions for validation)
- Numerical implementation (working code)
- Physical interpretation (understanding what the numbers mean)
- Visualization (making results accessible)

---

## Limitations and Considerations

### Assumptions Made
- **One-dimensional**: Real objects are 3D, but 1D is good for learning
- **Constant properties**: In reality, thermal diffusivity might change with temperature
- **Linear heat equation**: Ignores radiation and other nonlinear effects
- **Homogeneous material**: Assumes uniform properties throughout

### Stability Constraints
The FTCS method requires r ≤ 0.5 for stability. This means:
- If we want finer spatial resolution (smaller Δx), we must use even smaller time steps (Δt)
- This can make the method computationally expensive for very fine grids
- Alternative implicit methods exist that don't have this restriction

---

## Conclusion

This project successfully demonstrates how numerical methods can solve practical heat transfer problems. The FTCS method proves to be:
- **Accurate**: Errors are small and decrease predictably with grid refinement
- **Stable**: No spurious oscillations when parameters are chosen correctly
- **Validated**: Results match the analytical solution closely
- **Understandable**: The method's logic is straightforward and physically motivated

For someone learning numerical analysis, this project illustrates the complete workflow:
1. Understand the physical problem
2. Choose appropriate mathematical model
3. Select a numerical method
4. Implement carefully in code
5. Validate against known solutions
6. Analyze errors and convergence
7. Interpret results physically

The skills and insights gained here apply broadly to computational science and engineering, where numerical simulation has become an indispensable tool for design, analysis, and prediction.
