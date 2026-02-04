# Statsy

**The Verified Statistical Programming Language**

> "Every calculation is checked. Every result is provable. Statistics you can trust."

Statsy is a domain-specific language for statistical computing built on Newton's verified computation architecture. Unlike R or Python, Statsy **guarantees** your statistical operations are mathematically sound.

## Philosophy

```
The constraint IS the instruction.
The verification IS the computation.
The data IS the evidence.
```

## Quick Example

```statsy
# Load and verify data
data iris = load("iris.csv") |> verify(complete: true)

# Descriptive statistics (all verified)
mean(iris.sepal_length)        # -> 5.843 ✓
std(iris.sepal_length)         # -> 0.828 ✓
median(iris.sepal_length)      # -> 5.800 ✓

# Hypothesis testing with automatic assumptions check
result = t_test(
  x: iris.sepal_length where species == "setosa",
  y: iris.sepal_length where species == "versicolor",
  verify: [normality, equal_variance]  # Auto-verified!
)

# Result includes verification certificate
print(result)
# t = -10.52, p < 0.001 ✓
# Assumptions verified: normality ✓, equal_variance ✓
# Certificate: newton://verify/a3f2b1c9

# Regression with constraint checking
model = lm(sepal_length ~ petal_length + petal_width, data: iris)
  |> verify(vif < 5)           # No multicollinearity
  |> verify(residuals: normal)  # Normality of residuals

# Query Newton knowledge base
newton_ask("What is the central limit theorem?")
```

## Features

### Verified Computation
- Every arithmetic operation is bounds-checked
- Statistical tests auto-verify assumptions
- Results include cryptographic certificates

### Built-in Statistics
- Descriptive: mean, median, mode, std, var, quantile, range, iqr
- Distributions: normal, t, chi2, f, binomial, poisson, uniform
- Tests: t_test, anova, chi2_test, correlation, regression
- Advanced: pca, factor_analysis, clustering, time_series

### Newton Integration
- Query the knowledge base from Statsy code
- Ground statistical claims in evidence
- Immutable audit trail of all computations

### Data Safety
- Type inference with statistical semantics
- Missing value tracking (NA propagation)
- Automatic outlier detection (MAD-based, not mean)

## Installation

```bash
# From Newton-api root
cd statsy
python statsy.py          # Interactive REPL
python statsy.py file.st  # Run a script
```

## Language Reference

### Types
```statsy
# Scalars
x = 42              # Integer
y = 3.14            # Float
s = "hello"         # String
b = true            # Boolean
na = NA             # Missing value

# Collections
vec = [1, 2, 3, 4, 5]              # Vector
mat = [[1, 2], [3, 4]]             # Matrix
df = DataFrame(x: [1,2], y: [3,4]) # Data frame

# Statistical types
dist = Normal(mu: 0, sigma: 1)     # Distribution
test = TestResult(...)             # Test result
model = LinearModel(...)           # Fitted model
```

### Operators
```statsy
# Arithmetic (all verified for overflow/underflow)
+ - * / ^ %

# Comparison
== != < > <= >=

# Logical
and or not

# Statistical
|>      # Pipe operator
where   # Filter condition
~       # Formula notation
```

### Functions
```statsy
# Descriptive
mean(x)           median(x)         mode(x)
std(x)            var(x)            sum(x)
min(x)            max(x)            range(x)
quantile(x, p)    iqr(x)            mad(x)

# Distributions
dnorm(x, mu, sigma)    # Density
pnorm(x, mu, sigma)    # CDF
qnorm(p, mu, sigma)    # Quantile
rnorm(n, mu, sigma)    # Random sample

# Hypothesis tests
t_test(x, y)           # Two-sample t-test
paired_t_test(x, y)    # Paired t-test
anova(g1, g2, ...)     # One-way ANOVA
chi2_test(table)       # Chi-squared test
cor_test(x, y)         # Correlation test

# Regression
lm(x, y)               # Linear regression

# Newton integration
newton_ask(question)   # Query knowledge base
newton_verify(claim)   # Verify a claim
guidance(topic)        # Statistical guidance
```

## ASCII Visualizations

Statsy includes beautiful ASCII charts that work everywhere - no graphics libraries needed:

```statsy
# Histogram - see your data distribution
histogram(data, 10, 40, "My Data")

# Box plot - five number summary visual
boxplot(data, 50, "Data Summary")

# Sparkline - inline mini chart
sparkline(timeseries, "Trend")  # -> ▁▂▃▄▅▆▇█

# Scatter plot - relationship visualization
scatter(x, y, 60, 20, "X vs Y")

# Line chart - time series
line_chart(monthly_data, 50, 15, "Monthly Trend")

# Bar chart - category comparison
bar_chart(["Q1","Q2","Q3","Q4"], [100,150,125,175], 40, "Revenue")
```

Example output:
```
┌────────────────────────────────────────────────────────────┐
│                        Histogram                           │
├────────────────────────────────────────────────────────────┤
│   10.00 │████████████████████████████████████████│   15 │
│   15.00 │██████████████████████████░░░░░░░░░░░░░░│   10 │
│   20.00 │████████████████░░░░░░░░░░░░░░░░░░░░░░░░│    6 │
│   25.00 │████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│    3 │
└────────────────────────────────────────────────────────────┘
  n=34 | mean=15.2 | std=4.8 | median=14.0
```

## Advanced Statistics

### Robust Statistics (Newton-powered)
```statsy
# Modified z-score using MAD (not std)
modified_zscore(data)  # More robust than standard z-score

# Outlier detection
detect_outliers(data, 3.5)  # Returns (index, value) pairs
is_outlier(500, data)       # Check single value

# Resistant measures of center
trimmed_mean(data, 0.1)     # Remove 10% from each end
winsorized_mean(data, 0.1)  # Replace extremes, don't remove
robust_mean(data)           # MAD-based resistant mean
```

### Time Series Analysis
```statsy
# Smoothing
moving_avg(data, 3)         # 3-period moving average
exp_smooth(data, 0.3)       # Exponential smoothing (α=0.3)

# Decomposition
decompose(data, 3)          # Trend + Residual decomposition
```

### Data Loading
```statsy
# Load external data
data = load_csv("mydata.csv", true)   # true = has header
json = load_json("config.json")
```

## Verified Statistics

Statsy uses Newton's robust statistics module - MAD over mean, locked baselines:

```statsy
# Traditional (sensitive to outliers)
data = [1, 2, 3, 4, 100]
mean(data)  # -> 22 (misleading!)

# Statsy default: robust statistics
robust_mean(data)   # -> 2.5 (trimmed)
mad(data)           # -> 1.48 (robust dispersion)

# Automatic outlier flagging
describe(data)
# count: 5
# mean: 22.0 ⚠️ (outlier influence: high)
# robust_mean: 2.5 ✓
# outliers: [100] (flagged by MAD)
```

## License

Part of Newton Supercomputer.
© 2026 Jared Lewis · Ada Computing Company · Houston, Texas
