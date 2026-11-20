# BIT 2118 Scientific Computing  Group Work Documentation (Tasks 2–20)

Prerequisite / Task 01: Data Science Essentials with Python
Before tackling the numerical computation modules, I completed the self-paced foundation course Data Science Essentials with Python.
Course Status: Completed
Course Title: Data Science Essentials with Python
Certificate / Proof of Completion: https://www.credly.com/badges/844a3555-0824-4517-bd3c-689b6652a671/public_url
Task 02: NumPy Arrays and Numerical Computation
B. Inputs and Mathematical Operations
Inputs: A 1D array named temperatures_c storing 24 hourly temperature readings in Celsius.
Math operations:
Arithmetic mean μ = 1/N Σ x_i using np.mean, and extremes using np.min and np.max.
Vectorized conversion F = 1.8C + 32 applied to the whole array in one expression without a loop.
C. Parameter Variation Experiment
What I changed: Added 5°C to every reading to simulate a heat wave.
What happened:
Mean rose from 23.12°C to 28.12°C, minimum rose from 17.50°C to 22.50°C, and maximum rose from 29.40°C to 34.40°C.
The range, max minus min = 11.9°C, did not change.
Why it changed: Adding a constant c shifts the mean by c so that μ' = μ + c and moves every value equally, so spread measures such as the range stay the same.
D. Output Interpretation
The mean temperature was 23.12°C, indicating a warm day.
The coldest reading was 17.50°C during the early morning and the hottest was 29.40°C in the early afternoon.
The first six Fahrenheit values of 65.3, 64.4, 64.04, 63.5, 64.22, and 66.2 confirm that the formula was applied element by element.
E. Real-World Adaptation: IoT Soil-Moisture Sensor
Script Location: adaptations/Task_02_adapted.py
Real-world Problem: Convert raw ADC readings of a soil sensor into moisture percentages and decide when irrigation is needed.
Assumptions:
Raw value 850 is completely dry, 350 is fully wet, and the response is linear.
Irrigate when moisture is below 30%.
Formula: moisture% = 850 − raw divided by 850 − 350, multiplied by 100.
New Inputs: 12 raw ADC readings from 820 down to 500.
Results & Findings:
Moisture rose from 6% to 70%, with a mean of 46.1%.
3 of 12 readings were below the 30% threshold.
Takeaway: The soil starts dry and gets wetter over the period due to rain or irrigation. One vectorized formula calibrates every reading at once.
Task 03: Mathematical Functions and Vectorization
B. Inputs and Mathematical Operations
Inputs: 1,000,000 simulated latencies latency_ms drawn uniformly from 5 to 250 ms with default_rng seeded at 42.
Math operations:
Scaling s = ms / 1000, then squaring s².
Performed two ways, using a Python for loop and a single NumPy expression, timed with timeit.
C. Parameter Variation Experiment
What I changed: The sample size N was changed to 10,000 and 5,000,000 instead of 1,000,000.
What happened: On my run the speed-up stayed between 45× and 60×; for example at N = 5M, the loop took 0.67 s while the vectorized version took 0.013 s.
Why it changed: Both versions grow linearly with N, but the NumPy loop runs in compiled C on contiguous memory, keeping a large constant advantage over the interpreted Python loop.
D. Output Interpretation
The first five squared latencies, such as 0.0379, are in seconds² and confirm the calculation.
The speed-up factor shows how many times faster the vectorized code is. Repeating the work in a loop is the slow part, not the arithmetic.
E. Real-World Adaptation: Gamma Correction of a Grey-Scale Image
Script Location: adaptations/Task_03_adapted.py
Real-world Problem: Brighten a 1000 × 1000 pixel image using gamma correction.
Assumptions: Pixel intensities are scaled from 0 to 1 and γ = 2.2.
New Inputs & Computations:
out = in^(1/2.2) applied to all 10⁶ pixels.
A loop over 200 rows is timed and extrapolated to the full image.
Results & Findings:
Mean brightness changed from 0.500 to 0.687.
Estimated loop time was 0.20 s versus vectorized 0.005 s, which is about 39× faster.
Takeaway: Image processing repeats the same operation millions of times, so vectorization is essential.
Task 04: Floating-Point Arithmetic and Numerical Errors
B. Inputs and Mathematical Operations
Inputs: 0.1, 0.2, 0.3; the approximation 1.414 of √2; and x values of 10⁻⁴, 10⁻⁸, and 10⁻¹².
Math operations:
Absolute error E_abs = |x_true − x_approx| and relative error E_rel = E_abs / |x_true|.
Tolerance comparison with np.isclose instead of ==.
Two algebraically equal formulas: √(1 + x) − 1 divided by x, and 1 divided by √(1 + x) + 1.
C. Parameter Variation Experiment
What I changed: Used the better approximation 1.41421, and pushed x down to 10⁻¹⁴ and 10⁻¹⁶.
What happened:
Absolute error fell to 3.6 × 10⁻⁶, giving a relative error of 0.00025%.
At x = 10⁻¹⁴ the direct formula gave 0.4885, and at x = 10⁻¹⁶ it gave 0.0. The stable formula gave 0.5 every time.
Why it changed: For tiny x, 1 + x rounds to values very close to or equal to 1, so √(1 + x) − 1 subtracts almost identical numbers, causing catastrophic cancellation. The rewritten form has no subtraction.
D. Output Interpretation
0.1 + 0.2 == 0.3 is False because the sum is stored as 0.30000000000000004, whereas np.isclose returns True.
The absolute error of 1.414 was 0.00021356, with a relative error of 0.0151%.
The stable formula tends to the correct limit of 0.5.
E. Real-World Adaptation: Banking – Accumulated Rounding Error
Script Location: adaptations/Task_04_adapted.py
Real-world Problem: A ledger adds 10 cents one million times, where the correct total is exactly 100,000.
Assumptions: Compare naive float addition, math.fsum, and integer cents. Also test single precision float32.
Results & Findings:
Naive float sum: 100000.00000133, an error of 1.3 × 10⁻⁶.
math.fsum and integer cents: exactly 100000.0.
float32 across 100,000 additions of 0.1: 9998.557 instead of 10000.
Takeaway: Money should be stored as integer cents or Decimal; small errors accumulate, and lower precision makes them worse.
Task 05: Matrix Algebra and Matrix Operations
B. Inputs and Mathematical Operations
Inputs: A 4 × 2 matrix of square corners, a 45° rotation matrix R, and a scaling matrix S with diagonal values 2.0 and 1.5.
Math operations:
Composite transformation T = R · S.
Row-vector mapping P_new = P · T^T.
Determinant via np.linalg.det as the area scale factor.
C. Parameter Variation Experiment
What I changed: First, a rotation of 90° with no scaling; second, uniform scaling of 3 × 3 at 45°.
What happened:
For the 90° rotation, the determinant was 1.0 and the corner at 1, 0 moved to 0, 1.
For the 3 × 3 scaling, the determinant was 9.0.
Why it changed: det(R · S) = det(R) × det(S) = 1 · s_x s_y. A pure rotation preserves area, while scaling by 3 in both directions multiplies area by 3 × 3 = 9.
D. Output Interpretation
The unit square became a rotated and stretched rectangle.
The determinant of 3.0, equal to 2.0 × 1.5, shows the new area is three times the original.
E. Real-World Adaptation: Robot / Graphics Triangle Transformation
Script Location: adaptations/Task_05_adapted.py
Real-world Problem: Mirror, rotate, and move a triangular part in 2D.
Assumptions: Triangle with vertices 0, 0 and 2, 0 and 1, 1.5; mirror about the y-axis, rotate 30°, then translate by 4, 1 using 3 × 3 homogeneous matrices.
Results & Findings:
New vertices: 4, 1 and 2.268, 0 and 2.384, 1.799.
Determinant of the 2 × 2 part is −1.
Takeaway: A determinant of −1 means the shape was flipped but not resized. Homogeneous coordinates allow rotation and translation to be combined in one matrix product.
Task 06: Solution of Systems of Linear Equations
B. Inputs and Mathematical Operations
Inputs: Matrix A with rows 4, 2 and 8, 12 representing CPU and memory per server type, and vector b = 20, 72 representing observed totals.
Math operations:
Solve Ax = b with np.linalg.solve using LU factorization with partial pivoting.
Residual r = b − Ax and its norm ||r||_2.
C. Parameter Variation Experiment
What I changed: First, changed totals to 30, 100; second, tested a nearly singular matrix with rows 4, 2 and 8, 4.0001.
What happened:
With totals 30, 100, the solution became 5, 5.
With the nearly singular matrix, the condition number rose from 6.98 to about 250,000; changing b_2 from 40 to 40.01 moved the answer from 5, 0 to −45, 100.
Why it changed: When the rows are almost parallel, the matrix is ill-conditioned and tiny changes in b are magnified enormously.
D. Output Interpretation
The system has 3 Type A and 4 Type B servers, and the residual norm is 0.0.
E. Real-World Adaptation: Circuit Mesh Currents
Script Location: adaptations/Task_06_adapted.py
Real-world Problem: Find the currents in three coupled loops of a resistor network.
Assumptions: Kirchhoff's voltage law, resistance matrix R with rows 10, −4, 0 and −4, 12, −5 and 0, −5, 9 in Ω, and source voltages 12, 0, −6 V.
Results & Findings:
Currents I = 1.277, 0.192, −0.560 A, with a residual of approximately 10⁻¹⁵.
Takeaway: The negative sign means loop 3 carries current opposite to the assumed direction.
Task 07: Gaussian Elimination and LU Decomposition
B. Inputs and Mathematical Operations
Inputs: A 3 × 3 matrix A and three measurement vectors b_1, b_2, b_3.
Math operations:
Factor once: PA = LU via lu_factor.
For each b, solve Ly = Pb and then Ux = y via lu_solve.
Factorization costs O(n³); every extra right-hand side costs only O(n²).
C. Parameter Variation Experiment
What I changed: A 300 × 300 matrix with 500 different right-hand sides.
What happened: Repeated np.linalg.solve took 0.413 s, whereas factoring with LU once and reusing took 0.066 s, which is about 6.3× faster.
Why it changed: The expensive elimination is performed once, and each new vector only requires two triangular solves.
D. Output Interpretation
Set 1 gave x = 5, 5, 5, identical to the direct solver. Residual norms were about 10⁻¹⁵, which is numerically exact.
E. Real-World Adaptation: Leontief Input-Output Economy
Script Location: adaptations/Task_07_adapted.py
Real-world Problem: Calculate the total production each sector must make to meet different consumer demands when sectors use each other's output.
Assumptions: 3 sectors with technology matrix T, solving I − T times x = d using the same matrix for three demand scenarios.
Results & Findings:
Base demand 100, 80, 60 → output 203.74, 160.75, 147.66.
+20% in sector 1 → output 231.78, 166.36, 155.14.
Recession 80, 60, 40 → output 158.13, 119.63, 106.17.
Takeaway: Higher demand in one sector increases output across all sectors, and LU factorization lets the same economy be re-solved quickly for each scenario.
Task 08: Iterative Methods for Linear Systems
B. Inputs and Mathematical Operations
Inputs: A 5 × 5 tridiagonal matrix, boundary vector b = 100, 0, 0, 0, 20, and tolerance 10⁻⁸.
Math operations:
Jacobi: x^(k+1) = D⁻¹ times b − L + U times x^(k).
Gauss-Seidel: uses the newest values immediately inside the same sweep.
Stop when the infinity norm ||x^(k+1) − x^(k)||_∞ is less than tol.
C. Parameter Variation Experiment
What I changed: Adjusted the tolerance to 10⁻³ and 10⁻¹² and increased the grid size to 20 nodes.
What happened:
Original tol 10⁻⁸ with 5 nodes: Jacobi 150 iterations, Gauss-Seidel 75 iterations.
tol 10⁻³: Jacobi 70 iterations, Gauss-Seidel 35 iterations.
tol 10⁻¹²: Jacobi 214 iterations, Gauss-Seidel 107 iterations.
20 nodes with tol 10⁻⁸: Jacobi 1672 iterations, Gauss-Seidel 842 iterations.
Why it changed: Convergence is geometric and controlled by the spectral radius of the iteration matrix. Tighter tolerances require more steps, bigger grids converge more slowly, and Gauss-Seidel has a smaller spectral radius of about ρ_J², so it needs about half the steps of Jacobi.
D. Output & Graph Interpretation
Terminal output: Both methods match the direct solution of 86.67, 73.33, 60.00, 46.67, 33.33 °C, showing a straight temperature drop from the hot end to the cold end.
Semilog plot: The error falls along a straight line indicating geometric decay, with Gauss-Seidel's line descending more steeply.
E. Real-World Adaptation: Heated Metal Rod
Script Location: adaptations/Task_08_adapted.py
Real-world Problem: Find the steady-state temperature at 10 interior points of a rod held at 0°C at one end and 80°C at the other.
Assumptions: 1D steady conduction with no internal heat source.
Results & Findings:
Temperatures: 7.27, 14.55, 21.82, up to 72.73 °C after 244 Gauss-Seidel iterations.
This matches the exact linear profile expected from theory.
Takeaway: Iterative solvers need only a few values per row, which is why they suit very large sparse systems.
Task 09: Eigenvalues and Eigenvectors
B. Inputs and Mathematical Operations
Inputs: A symmetric 4 × 4 adjacency matrix for nodes A, B, C, D.
Math operations:
Solve Av = λv with np.linalg.eig.
Pick the dominant eigenvalue using np.argmax and normalize its eigenvector so Σ v_i = 1 for eigenvector centrality.
Check that ||Av − λv||_2 ≈ 0.
C. Parameter Variation Experiment
What I changed: First, added the link A–D; second, removed the links B–A and B–D.
What happened:
Adding link A–D shifted the dominant eigenvalue from 2.5616 to 3.0000 and gave all nodes equal scores of 0.25.
Removing links B–A and B–D made node C the most important at 0.366, while the others dropped to 0.211.
Why it changed: Eigenvector centrality rewards nodes connected to well-connected nodes. When link A–D is added, every node has identical connections, so all scores become equal.
D. Output Interpretation
In the original network, B and C scored 0.2808 while A and D scored 0.2192, since B and C each have three neighbors.
The verification error was about 10⁻¹⁵.
E. Real-World Adaptation: PCA of Exam Scores
Script Location: adaptations/Task_09_adapted.py
Real-world Problem: Reduce two correlated exam scores, Maths and Physics, of 50 students to fewer dimensions.
Assumptions: Physics ≈ 0.8 × Maths plus random noise, and principal components are the eigenvectors of the covariance matrix.
Results & Findings:
Eigenvalues were 15.07 and 312.17.
The first component explains 95.4% of the variance.
Takeaway: Both subjects measure largely one underlying ability, so the data can be compressed from 2 variables to 1.
Task 10: Root Finding: Bisection and Fixed-Point Methods
B. Inputs and Mathematical Operations
Inputs: f(T) = T − 25 − 10e^(−T/20), bracket from 20 to 40, g(T) = 25 + 10e^(−T/20), and tolerance 10⁻¹⁰.
Math operations:
Bisection requires f(a) · f(b) < 0 and repeatedly halves the interval.
Fixed-point iterates T_(k+1) = g(T_k) and converges when |g'(T)| < 1; here |g'| ≈ 0.13.
C. Parameter Variation Experiment
What I changed: Ambient temperature from 25 to 35 with amplitude from 10 to 20, and tested an invalid bracket from 30 to 40.
What happened:
The new equilibrium was 37.992°C.
The bracket from 30 to 40 raised ValueError: f(a) and f(b) must have different signs.
Why it changed: The heat-balance constants move the crossing point. Bisection only works when the function changes sign inside the bracket.
D. Output & Graph Interpretation
Terminal output: Both methods give 27.525211°C. Bisection took 38 iterations while fixed-point took only 13.
Graph: f(T) crosses zero at T ≈ 27.53°C, where heat gain equals heat loss.
E. Real-World Adaptation: Break-Even Quantity
Script Location: adaptations/Task_10_adapted.py
Real-world Problem: Find the sales volume where profit becomes zero.
Assumptions: Price $50, fixed cost $2000, and variable cost per unit 20 + 0.01q.
profit(q) = 50q − 2000 − 20q − 0.01q² = 0.
Results & Findings:
Break-even occurred at q = 68.22 units and again at q = 2931.78 units using brackets from 1 to 200 and from 200 to 3000.
Takeaway: The business makes a profit only between roughly 69 and 2931 units; at high volume rising unit cost wipes out the profit.
Task 11: Root Finding: Newton-Raphson and Secant Methods
B. Inputs and Mathematical Operations
Inputs: Cash flows C = −10000, 3000, 3500, 4000, 2500, Newton start x_0 = 0.10, and secant starts 0.05 and 0.20.
Math operations:
Newton-Raphson: x_(n+1) = x_n − f(x_n) / f'(x_n) with f(r) = Σ_t C_t / (1 + r)^t.
Secant replaces f' with the slope through two recent points.
C. Parameter Variation Experiment
What I changed: First, increased initial investment from 10000 to 12000; second, changed Newton start x_0 to 0.90.
What happened:
Increasing the investment dropped the IRR from 11.54% to 3.33%.
Starting at x_0 = 0.90 caused Newton's method to converge in 11 iterations to a meaningless root of −154.41%.
Why it changed: A higher investment lowers the return. Newton's method is only locally reliable, so a poor starting guess can reach another root of the polynomial, in this case a rate below −100% which has no financial meaning.
D. Output Interpretation
IRR = 11.542461% from both methods, with Newton taking 4 iterations and secant taking 7. This is the discount rate at which net present value is zero.
E. Real-World Adaptation: Loan Interest Rate
Script Location: adaptations/Task_11_adapted.py
Real-world Problem: Find the true interest rate of a loan from its repayment schedule.
Assumptions: Borrow 5000 and repay 450 per month for 12 months. Solve 5000 − Σ_(t=1 to 12) 450 / (1 + r)^t = 0 with the secant method.
Results & Findings:
Monthly rate was 1.204%, nominal annual rate 14.45%, and effective annual rate 15.45%.
Total interest paid was 400.
Takeaway: Because of monthly compounding, the true yearly cost is higher than the nominal rate.
Task 12: Polynomial and Nonlinear Equation Solving
B. Inputs and Mathematical Operations
Inputs: The system F(x, y) consisting of x² + y² − 4 and y − x² + 1 with initial guesses 1, 1 and −1, 1.
Math operations:
scipy.optimize.root using the hybrid Powell / MINPACK method, which solves J(z_k)Δz_k = −F(z_k) iteratively.
Check that the residual vector is close to zero.
C. Parameter Variation Experiment
What I changed: Changed the circle radius from 2 to 1, and then to 0.5.
What happened:
At R = 1, there were three intersections at ±1, 0 and 0, −1 depending on the starting guess.
At R = 0.5, converged returned False with a residual of about 0.25.
Why it changed: Changing the radius alters how many times the curves intersect. With R = 0.5 they do not intersect at all, so no real solution exists.
D. Output Interpretation
For R = 2, the solver returned ±1.5175, 1.3028 with residuals near 0. The sign of x follows the starting guess because the system is symmetric about the y-axis.
E. Real-World Adaptation: Projectile Kinematics
Script Location: adaptations/Task_12_adapted.py
Real-world Problem: Determine when a thrown ball reaches a given height.
Assumptions: h(t) = 2 + 20t − 4.9t² metres. Solve h(t) = 10 with np.roots.
Results & Findings:
The ball reaches 10 m at t = 0.45 s while rising and t = 3.63 s while falling.
Ground contact occurs at t = 4.18 s, while the negative root of −0.10 s is not physical.
Takeaway: A quadratic has two roots, so you must select the one that makes physical sense.
Task 13: Interpolation
B. Inputs and Mathematical Operations
Inputs: Hourly times t from 8 to 14 and temperatures from 18.0 to 25.0°C.
Math operations:
Linear interpolation: y(x) = y_i + (y_(i+1) − y_i) / (x_(i+1) − x_i) × (x − x_i).
Cubic spline: piecewise cubics with continuous value, first derivative, and second derivative at the knots.
C. Parameter Variation Experiment
What I changed: Queried 13:30 inside the range and 15:00 outside the data range.
What happened:
At 13:30, linear gave 25.25°C and cubic gave 25.41°C.
At 15:00, the linear interpolator raised an out-of-bounds ValueError, while the cubic spline extrapolated to 22.94°C.
Why it changed: Interpolation is only reliable between measured points, and extrapolating a polynomial beyond the data is unreliable.
D. Output & Graph Interpretation
At 10:30, linear interpolation gives 23.25°C and cubic spline gives 23.36°C.
The spline is smooth and follows the flattening near the afternoon peak, whereas the linear curve has sharp corners at each measurement.
E. Real-World Adaptation: Missing Air-Quality Readings
Script Location: adaptations/Task_13_adapted.py
Real-world Problem: An air-quality sensor lost its PM2.5 readings at 11:00 and 12:00.
Assumptions: Concentration changes smoothly and the remaining 6 hourly values are accurate.
Results & Findings:
At 11:00, estimates were 46.3 µg/m³ linear and 47.8 µg/m³ cubic.
At 12:00, estimates were 50.7 µg/m³ linear and 53.1 µg/m³ cubic.
Takeaway: Both methods provide sensible gap fillers, with the spline accounting for curvature and producing slightly higher estimates.
Task 14: Curve Fitting and Approximation
B. Inputs and Mathematical Operations
Inputs: Users x from 50 to 350 and response times y from 82 to 305 ms.
Math operations:
Least squares with curve_fit: minimize Σ_i (y_i − f(x_i; a, b, c))² for f = ax² + bx + c.
RMSE = √(1/N Σ (y_i − ŷ_i)²).
C. Parameter Variation Experiment
What I changed: Used a linear model and a cubic model instead of the quadratic, and added one outlier of 400 ms at 250 users.
What happened:
Linear RMSE was 18.83 ms, quadratic was 1.55 ms, and cubic was 0.14 ms.
With the outlier included, the 400-user forecast moved from 377.9 ms to 347.1 ms.
Why it changed: A straight line cannot follow curved data due to model bias. A cubic fits 7 points almost exactly but risks overfitting, and least squares is sensitive to outliers.
D. Output & Graph Interpretation
The fit is y = 0.002167x² − 0.1345x + 85.00 with RMSE ≈ 1.55 ms.
At 400 users the model predicts 377.9 ms, showing that response time grows faster than linearly with load.
E. Real-World Adaptation: Exponential Growth
Script Location: adaptations/Task_14_adapted.py
Real-world Problem: Estimate the growth rate of a bacterial culture or user base from hourly counts.
Assumptions: y = Ae^(rt) with counts from 100 to 770 over 8 hours.
Results & Findings:
Fitted values were A = 100.0 and r = 0.2919 per hour, giving a doubling time of ln(2) / r = 2.37 h.
Forecast at t = 10 h was about 1853.
Takeaway: The fitted parameter has a direct physical meaning such as doubling time, which makes curve fitting useful for forecasting.
Task 15: Numerical Differentiation
B. Inputs and Mathematical Operations
Inputs: Times t from 0 to 6 s and GPS positions x = 0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0 m.
Math operations:
Forward difference at the start: (f(x + h) − f(x)) / h with error O(h).
Central difference inside: (f(x + h) − f(x − h)) / 2h with error O(h²).
Backward difference at the end.
C. Parameter Variation Experiment
What I changed: Varied the step size h for f = sin x at x = 1, where exact cos 1 = 0.54030231.
What happened:
At h = 10⁻¹: forward error 4.3 × 10⁻², central error 9.0 × 10⁻⁴.
At h = 10⁻³: forward error 4.2 × 10⁻⁴, central error 9.0 × 10⁻⁸.
At h = 10⁻⁶: forward error 4.2 × 10⁻⁷, central error 2.8 × 10⁻¹¹.
At h = 10⁻¹⁴: forward error 3.7 × 10⁻³, central error 3.7 × 10⁻³.
Why it changed: Truncation error shrinks as h decreases and shrinks faster for central differences, but when h becomes too small, round-off error from subtracting nearly equal numbers dominates and total error rises again.
D. Output & Graph Interpretation
Speed rises steadily from 4.80 m/s to 8.00 m/s, showing that the vehicle is accelerating.
E. Real-World Adaptation: Acceleration from Velocity Readings
Script Location: adaptations/Task_15_adapted.py
Real-world Problem: Estimate the acceleration of a car from velocity readings taken at 1 s intervals.
Assumptions: Velocities of 0, 3.1, 6.5, 10.4, 14.0, 17.2 m/s evaluated with np.gradient using central differences inside and one-sided differences at the ends.
Results & Findings:
Acceleration values were 3.10, 3.25, 3.65, 3.75, 3.40, 3.20 m/s², with a mean of 3.39 m/s².
Takeaway: The acceleration is strong and nearly constant. Differentiating noisy data amplifies noise, so measurements must be accurate.
Task 16: Numerical Integration
B. Inputs and Mathematical Operations
Inputs: Times t = 0, 2, 4, 6, 8, 10, 12 h and power P = 0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9 kW.
Math operations:
Trapezoidal rule: Σ (f(x_i) + f(x_(i+1))) / 2 × Δx_i with error O(h²).
Simpson's rule: fits parabolas over pairs of intervals with error O(h⁴).
C. Parameter Variation Experiment
What I changed: Increased the 6-hour peak from 1.8 to 3.0 kW, and varied the number of sample points for the integral of sin x from 0 to π, which equals 2.
What happened:
Energy rose from 15.7 kWh trapezoidal and 15.8 kWh Simpson to 18.1 kWh trapezoidal and 19.0 kWh Simpson.
With 33 points, the error was 1.6 × 10⁻³ for trapezoidal versus 1.0 × 10⁻⁶ for Simpson.
Why it changed: Energy is the area under the power curve, so a higher peak adds area. Simpson's higher-order error makes it much more accurate on smooth data.
D. Output Interpretation
The day's energy was 15.700 kWh by trapezoidal rule and 15.800 kWh by Simpson's rule, differing by only 0.1 kWh.
E. Real-World Adaptation: Total Water Volume from a Flow Meter
Script Location: adaptations/Task_16_adapted.py
Real-world Problem: Estimate the volume of water pumped from a flow meter reading in L/s taken every 10 s.
Assumptions: 7 readings from 0 to 60 s: 0, 2.5, 4.0, 4.8, 4.2, 2.0, 0.5 L/s.
Results & Findings:
Volume was 177.5 L by trapezoidal rule and 180.3 L by Simpson's rule.
Takeaway: Integrating a rate over time yields the accumulated quantity such as energy, distance, or volume.
Task 17: Ordinary Differential Equations – Euler Method
B. Inputs and Mathematical Operations
Inputs: T_0 = 90°C, T_ambient = 25°C, k = 0.12 min⁻¹, duration 30 min, and step size h = 1 min.
Math operations:
Newton's law of cooling: dT/dt = −k(T − T_ambient).
Euler update: T_(n+1) = T_n + h × −k(T_n − T_ambient) with global error O(h).
Exact solution: T(t) = T_ambient + (T_0 − T_ambient)e^(−kt) for validation.
C. Parameter Variation Experiment
What I changed: Varied step size h across 5, 2, 1, 0.5, 0.1, and 0.01, and tested an extreme step of h = 20.
What happened:
At h = 5.0, error at 30 min was 1.5098.
At h = 1.0, error at 30 min was 0.3720.
At h = 0.1, error at 30 min was 0.0383.
At h = 0.01, error at 30 min was 0.0038.
With h = 20, the values jumped from 90 to −66 to 152.4, showing instability.
Why it changed: Euler assumes the slope is constant over a step, so the error is proportional to h. When kh > 2, the update overshoots so much that it oscillates with growing amplitude.
D. Output & Graph Interpretation
After 30 minutes, Euler gives 26.40°C against the exact 26.78°C, an error of 0.372°C.
The object cools quickly at first and then slowly levels off at 25°C, with the Euler curve staying below the exact curve.
E. Real-World Adaptation: Logistic Population Growth
Script Location: adaptations/Task_17_adapted.py
Real-world Problem: Model a population limited by its environment.
Assumptions: dP/dt = rP(1 − P/K) with r = 0.4, K = 1000, P_0 = 50, and h = 0.5.
Results & Findings:
P(10) = 712.8, P(20) = 995.0, and P(30) = 999.9.
Takeaway: Growth is S-shaped and levels off at the carrying capacity K, unlike unlimited exponential growth.
Task 18: Numerical Solution of ODEs Using SciPy
B. Inputs and Mathematical Operations
Inputs: V_s = 5 V, R = 1000 Ω, C = 0.001 F, V_0 = 0 V, over the interval 0 to 5 s.
Math operations:
dV/dt = (V_s − V) / RC with time constant τ = RC = 1 s.
solve_ivp using default adaptive RK45 with rtol=1e-9 and atol=1e-11.
Exact curve V = V_s(1 − e^(−t/RC)) for validation.
C. Parameter Variation Experiment
What I changed: First, increased R to 4.7 kΩ; second, simulated discharge from V_0 = 5 V with V_s = 0.
What happened:
With R = 4.7 kΩ, τ became 4.7 s, giving V(1 s) = 0.96 V and V(5 s) = 3.27 V instead of 4.97 V.
During discharge, V(1 s) = 1.839 V, equal to 5/e.
Why it changed: A larger R increases the time constant, so charging is slower. After one time constant, a discharging capacitor holds 1/e ≈ 36.8% of its initial voltage.
D. Output & Graph Interpretation
At 5 s, corresponding to five time constants, the capacitor reached 4.9663 V, or 99.3% of the supply. The maximum difference from the exact solution was 9 × 10⁻¹⁰ V.
E. Real-World Adaptation: SIR Epidemic Model
Script Location: adaptations/Task_18_adapted.py
Real-world Problem: Predict how an infection spreads in a closed population.
Assumptions: N = 10000, 10 initially infected, infection rate β = 0.4, and recovery rate γ = 0.1 per day, so R_0 = β/γ = 4.
dS/dt = −βSI/N, dI/dt = βSI/N − γI, dR/dt = γI.
Results & Findings:
The infection peaked at 4036 people on day 27.
About 9802 people were infected over the whole outbreak.
Takeaway: With R_0 = 4, almost everyone is eventually infected unless β is reduced through distancing or γ is increased through treatment.
Task 19: Numerical Optimization
B. Inputs and Mathematical Operations
Inputs: Costs 12 and 18, capacities 100 and 170, minimum capacity 1000, and bounds x, y ≥ 0.
Math operations:
Minimize 12x + 18y subject to 100x + 170y ≥ 1000 and x, y ≥ 0.
Solved with minimize using method SLSQP.
An integer search over whole servers provides a practical answer.
C. Parameter Variation Experiment
What I changed: First, increased Type B price from 18 to 25; second, increased required capacity from 1000 to 2500.
What happened:
When Type B price rose to 25, the optimum switched to 10 Type A servers at a cost of 120.
When capacity rose to 2500, the solution became 14.706 Type B units at a cost of 264.71, or an integer solution of 15 B at a cost of 270.
Why it changed: The solver buys capacity from the cheaper source per unit; B costs 18/170 = 0.106 versus A at 12/100 = 0.12. When B's price rises to 25/170 = 0.147, A becomes cheaper.
D. Output Interpretation
Continuous optimum: 0 A and 5.882 B at a cost of 105.88.
Note: Your original paste cut off right after this line in Task 19. Send the rest of Task 19 and Task 20 if you want them formatted in the exact same style, or let me know if you want the full document exported as a Word .docx file already set in black Times New Roman.






 
