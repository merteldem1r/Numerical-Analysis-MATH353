# Numerical Errors

## Overview

In numerical analysis, errors arise when we approximate values. Understanding these errors helps us evaluate the accuracy of our computations.

## Types of Errors

### 1. Absolute Error

The absolute error measures the difference between the true value and the approximate value.

**Formula:**
$$E_{abs} = |x_{true} - x_{approx}|$$

**Example:**

- True value of $e^1 = 2.71828...$
- Approximate value = $3$
- Absolute error = $|2.71828 - 3| = 0.28172$

### 2. Relative Error

The relative error expresses the error as a fraction of the true value. It's useful for comparing errors across different scales.

**Formula:**
$$E_{rel} = \frac{|x_{true} - x_{approx}|}{|x_{true}|}$$

**Example:**

- True value of $e^1 = 2.71828...$
- Approximate value = $3$
- Relative error = $\frac{0.28172}{2.71828} \approx 0.1036$ (or 10.36%)

### 3. Percentage Error

The percentage error is the relative error expressed as a percentage.

**Formula:**
$$E_{percent} = E_{rel} \times 100\% = \frac{|x_{true} - x_{approx}|}{|x_{true}|} \times 100\%$$

**Example:**

- From above: $E_{percent} = 0.1036 \times 100\% = 10.36\%$

## Common Sources of Numerical Errors

1. **Rounding Error**: Occurs when numbers are rounded to fit limited precision
2. **Truncation Error**: Occurs when an infinite process is approximated by a finite one (e.g., Taylor series)
3. **Round-off Error**: Accumulation of small rounding errors in repeated calculations

## Key Takeaways

- **Absolute error** gives the magnitude of the error
- **Relative error** gives the error relative to the true value (better for comparison)
- Smaller errors indicate better approximations
- In practice, we often use approximate relative error when the true value is unknown:

$$E_{rel,approx} = \frac{|x_{new} - x_{old}|}{|x_{new}|}$$

## Python Example

See [rounding_error.py](/1-Numerical-Errors/rounding_error.py) for a practical example of computing absolute error using the Maclaurin series approximation of $e^x$.
