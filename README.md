# BIT 2118 Scientific Computing – Group Work Documentation (Tasks 2–20)

**How to use this repo:** every `code/Task_XX_*.py` file contains three parts that print under clear headings:
**A** original program, **C** changed input/parameter, **E** modified program for a related real-world case.
Run any file with `python code/Task_XX_*.py` (needs numpy, scipy, matplotlib). Figures are saved to `figures/`.
Raw program output is in `outputs.txt`. Timings in Tasks 3 and 7 vary from machine to machine.

> Before submitting: run the code yourself, change at least one value yourself, and rewrite the "interpretation" in your own words.
> The GitHub submission is individual, so your repo should reflect your understanding.

---
## Task 2 – NumPy Arrays and Numerical Computation
**B. Inputs / operation:** input = 24 hourly temperatures (°C). Operations: mean, min, max, and the vectorized formula F = 1.8C + 32.
**C. Changed input:** added +5 °C to every reading (heat wave). Mean 23.12 → 28.12 °C, max 29.40 → 34.40 °C. The range (max − min = 11.9) is unchanged because adding a constant shifts all values equally.
**D. Output meaning:** the day averaged 23.12 °C, coldest 17.5 °C (early morning) and hottest 29.4 °C (early afternoon). The Fahrenheit array has one converted value per reading.
**E. Related case – IoT soil-moisture sensor.** *Assumptions:* raw ADC 850 = completely dry, 350 = fully wet, linear sensor; irrigate below 30 %. *Input:* 12 raw readings. *Output:* moisture 6 % → 70 %, mean 46.1 %, 3 of 12 readings below 30 %. *Interpretation:* the soil starts dry and becomes wetter (e.g., after irrigation or rain); the first three readings would have triggered irrigation.

## Task 3 – Mathematical Functions and Vectorization
**B.** Input: 1,000,000 random latencies (5–250 ms). Operation: divide by 1000, then square; done by a Python loop and by one NumPy expression.
**C. Changed input:** N = 10,000 → 60× faster; N = 5,000,000 → 50× faster. The vectorized version stays about 45–60× faster at every size, because NumPy runs the loop in compiled C.
**D.** Squared latency values are in seconds² (e.g., 0.0379 s²). The speed-up figure tells how many times faster vectorized code is.
**E. Related case – gamma correction of a 1000×1000 grey image.** *Assumptions:* pixel values scaled 0–1, gamma = 1/2.2. *Output:* mean brightness 0.500 → 0.687; the estimated loop time was 0.20 s vs 0.005 s vectorized (~39×). *Interpretation:* gamma correction brightens mid-tones, and image-processing is a typical case where vectorization is essential.

## Task 4 – Floating-Point Arithmetic and Numerical Errors
**B.** Inputs: 0.1+0.2 vs 0.3; √2 vs 1.414; x = 1e-4, 1e-8, 1e-12. Operations: exact vs tolerance comparison, absolute/relative error, and two algebraically equal formulas for (√(1+x) − 1)/x.
**C. Changed input:** approximation 1.41421 gives absolute error 3.6e-6 (relative 0.00025 %), far smaller than for 1.414. With x = 1e-14 the "direct" formula gives 0.4885 and at x = 1e-16 gives 0, while the stable formula still gives 0.5.
**D.** `0.1+0.2 == 0.3` is False because the sum is 0.30000000000000004. The direct formula suffers catastrophic cancellation (subtracting nearly equal numbers 1+x and 1); the stable form avoids the subtraction. True answer → 0.5.
**E. Related case – banking.** *Assumption:* adding 10 cents one million times. *Output:* naive float sum = 100000.00000133 (error 1.3e-6), `math.fsum` and integer cents give exactly 100000. In float32, 100,000 additions of 0.1 give 9998.557 instead of 10000. *Interpretation:* money should be stored in integer cents or Decimal; tiny errors accumulate.

## Task 5 – Matrix Algebra and Matrix Operations
**B.** Inputs: square corners, rotation of 45°, scaling (2, 1.5). Operation: T = R·S, then points·Tᵀ; determinant check.
**C. Changed input:** 90° rotation with no scaling → determinant 1 (shape just turns: (1,0) → (0,1)); scaling 3×3 → determinant 9 (area ×9). So |det| = area scale factor.
**D.** The original square becomes a rotated parallelogram-like rectangle; det = 3 = 2 × 1.5, so the area triples.
**E. Related case – robot/graphics triangle.** *Assumptions:* 2-D triangle (0,0),(2,0),(1,1.5); mirror about the y-axis, rotate 30°, translate by (4,1) using 3×3 homogeneous matrices. *Output:* new vertices (4,1), (2.268,0), (2.384,1.799); det of rotation/mirror part = −1. *Interpretation:* −1 means the shape was flipped (mirrored) but not resized. Homogeneous coordinates let translation be done by matrix multiplication.

## Task 6 – Solution of Systems of Linear Equations
**B.** Inputs: A = [[4,2],[8,12]], b = [20,72] (CPU, memory). Operation: `np.linalg.solve` and residual check.
**C. Changed input:** totals 30 CPU and 100 GB → 5 Type A and 5 Type B. Then a nearly singular matrix ([[4,2],[8,4.0001]], cond ≈ 250,000): changing b from 40 to 40.01 swings the answer from (5,0) to (−45,100).
**D.** Original answer: 3 Type A and 4 Type B servers; residual 0 means both equations are satisfied. The second experiment shows an ill-conditioned system magnifies tiny measurement errors.
**E. Related case – circuit mesh currents.** *Assumptions:* 3 loops, resistance matrix R = [[10,−4,0],[−4,12,−5],[0,−5,9]] Ω, source voltages [12,0,−6] V. *Output:* I = [1.277, 0.192, −0.560] A. *Interpretation:* the negative sign means loop 3's current flows opposite to the assumed direction.

## Task 7 – Gaussian Elimination and LU Decomposition
**B.** Inputs: 3×3 matrix A, three measurement vectors. Operation: factor A once (`lu_factor`), solve with `lu_solve` for each b.
**C. Changed input:** 300×300 matrix with 500 right-hand sides: repeated solving 0.413 s vs LU-once 0.066 s (6.3× faster).
**D.** First set gives (5,5,5) (matches the direct solver); residual ≈ 1e-15 means the answers are numerically exact. LU saves time when A is reused.
**E. Related case – Leontief input-output economy.** *Assumptions:* 3 sectors, technology matrix T, (I − T)x = demand. *Output (total production needed):* base [203.7, 160.8, 147.7]; +20 % agriculture demand [231.8, 166.4, 155.1]; recession [158.1, 119.6, 106.2]. *Interpretation:* extra demand in one sector raises output in all sectors because industries buy from each other.

## Task 8 – Iterative Methods for Linear Systems
**B.** Inputs: 5×5 tridiagonal matrix, boundaries 100 °C and 20 °C, tolerance 1e-8. Operations: Jacobi and Gauss-Seidel updates until the maximum change < tolerance.
**C. Changed input:** tolerance 1e-3 → 70 (Jacobi)/35 (GS) iterations; 1e-12 → 214/107. With 20 nodes: 1672/842 iterations.
**D.** Both reach [86.67, 73.33, 60, 46.67, 33.33] °C = direct solution, a straight-line temperature drop from hot to cold. Gauss-Seidel needs about half as many iterations (see `figures/Task_08_convergence.png`; the straight line on the log plot shows steady geometric convergence).
**E. Related case – metal rod.** *Assumptions:* 10 interior points, ends fixed at 0 °C and 80 °C, steady state. *Output:* 7.27, 14.55, …, 72.73 °C after 244 GS iterations. *Interpretation:* temperature rises linearly along the rod, as theory predicts. More unknowns ⇒ many more iterations.

## Task 9 – Eigenvalues and Eigenvectors
**B.** Input: 4-node adjacency matrix. Operation: `np.linalg.eig`, take the dominant eigenvector and normalize it → importance score.
**C. Changed input:** adding link A–D makes the dominant eigenvalue 3.0 and all scores 0.25 (a complete graph, all nodes equal). Removing B–A and B–D links makes C the most important (0.366).
**D.** Original: B and C (0.281) are more important than A and D (0.219) because they connect to three nodes. Verification error ≈ 1e-15 confirms Av = λv.
**E. Related case – PCA on exam scores.** *Assumptions:* 50 students, Physics ≈ 0.8 × Maths + noise. *Output:* eigenvalues 15.1 and 312.2; PC1 explains 95.4 % of variance. *Interpretation:* the two subjects carry mostly one underlying "ability" dimension, so the data can be compressed from 2 variables to 1.

## Task 10 – Root Finding: Bisection and Fixed-Point
**B.** Input: f(T) = T − 25 − 10e^(−T/20), bracket [20, 40], tolerance 1e-10. Operation: bisection and iteration T = g(T).
**C. Changed input:** ambient 35 °C and amplitude 20 → equilibrium 37.99 °C. Bracket [30, 40] has no sign change → bisection fails with an error.
**D.** Equilibrium temperature is 27.525 °C by both methods; the fixed-point iteration needed 13 steps against 38 for bisection. The graph crosses zero at that temperature.
**E. Related case – break-even.** *Assumptions:* price 50, fixed cost 2000, variable cost 20 + 0.01q per unit. *Output:* profit = 0 at q = 68.2 and q = 2931.8. *Interpretation:* the firm makes profit only between ~69 and ~2931 units; beyond that rising cost per unit wipes out profit.

## Task 11 – Newton-Raphson and Secant
**B.** Input: cash flows [−10000, 3000, 3500, 4000, 2500]; Operation: solve NPV(r) = 0 (Newton needs the derivative, secant doesn't).
**C. Changed input:** investment 12000 → IRR falls to 3.33 %. Starting Newton at 0.90 jumps to a spurious root of −154 % in 11 iterations (an invalid rate below −100 %), showing sensitivity to the starting guess.
**D.** IRR = 11.54 %: the rate at which the project earns exactly back its cost. Newton needed 4 iterations, secant 7.
**E. Related case – loan interest.** *Assumptions:* borrow 5000, repay 450/month for 12 months. *Output:* monthly rate 1.204 %, nominal annual 14.45 %, effective 15.45 %; 400 paid in interest. *Interpretation:* this loan's true yearly cost is higher than the 14.45 % quoted rate because of compounding.

## Task 12 – Polynomial and Nonlinear Equation Solving
**B.** Inputs: circle x²+y²=4 and parabola y=x²−1, two initial guesses. Operation: `scipy.optimize.root` on the residuals.
**C. Changed input:** radius 1 → three intersections (±1, 0) and (0, −1) depending on the guess; radius 0.5 → solver fails (`converged=False`, residual 0.25) because no intersection exists.
**D.** For R = 2 the curves cross at (±1.517, 1.303); residuals ≈ 0 verify the answer. Each guess finds a different root.
**E. Related case – kinematics.** *Assumptions:* h(t) = 2 + 20t − 4.9t² (metres), find when h = 10 m with `np.roots`. *Output:* t = 0.45 s (rising) and 3.63 s (falling); ground hit at 4.18 s (the negative root is physically meaningless). *Interpretation:* quadratics have two roots; choose the one that makes physical sense.

## Task 13 – Interpolation
**B.** Inputs: hourly temperatures 08:00–14:00. Operation: linear and cubic-spline interpolation, evaluated every 10 minutes.
**C. Changed input:** at 13:30 linear = 25.25 °C, cubic = 25.41 °C. At 15:00 (outside the data) linear raises an error and cubic extrapolates to 22.94 °C, which is unreliable.
**D.** At 10:30 linear = 23.25 °C, cubic = 23.36 °C. The cubic curve is smooth and captures the flattening near the afternoon peak; the linear one has corners at each measurement.
**E. Related case – missing air-quality readings.** *Assumptions:* PM2.5 readings missing at 11:00 and 12:00. *Output:* 11:00 ≈ 46.3 (linear)/47.8 (cubic), 12:00 ≈ 50.7/53.1 µg/m³. *Interpretation:* both methods fill the gap sensibly; the spline allows for curvature and gives slightly higher values.

## Task 14 – Curve Fitting and Approximation
**B.** Inputs: 7 (users, response time) points. Operation: least-squares fit of y = ax² + bx + c; RMSE.
**C. Changed input:** linear model RMSE 18.8 ms (poor), cubic RMSE 0.14 ms (but risk of overfitting with 7 points). One outlier (400 ms at 250 users) changes the quadratic's shape and the 400-user forecast from 377.9 to 347.1 ms.
**D.** y = 0.002167x² − 0.1345x + 85; RMSE 1.55 ms means the curve passes within about 1.5 ms of the data. Predicted 377.9 ms at 400 users, response time grows faster than linearly under load.
**E. Related case – exponential growth.** *Assumptions:* counts of bacteria/users over 8 hours, y = A·e^(rt). *Output:* r = 0.292 per hour, doubling time 2.37 h, forecast at t = 10 ≈ 1853. *Interpretation:* the population doubles about every 2.4 hours.

## Task 15 – Numerical Differentiation
**B.** Inputs: GPS positions every second. Operation: forward difference at start, central at middle, backward at end.
**C. Changed input:** step size h for f = sin x at x = 1. Forward error is proportional to h (4e-2 → 4e-7), central error to h² (9e-4 → 3e-11). At very small h (1e-14) round-off dominates and error grows again (3.7e-3).
**D.** Speed rises from 4.8 m/s to 8.0 m/s, i.e. the vehicle accelerates steadily.
**E. Related case – acceleration from velocity.** *Input:* velocities 0 → 17.2 m/s over 6 s. *Output:* acceleration 3.1–3.75 m/s², mean 3.39 m/s². *Interpretation:* strong, fairly constant acceleration; (differentiating noisy data amplifies noise).

## Task 16 – Numerical Integration
**B.** Inputs: smart-meter power (kW) every 2 h over 12 h. Operation: trapezoid and Simpson integration → energy (kWh).
**C. Changed input:** peak 1.8 → 3.0 kW: energy rises to 18.1 (trapezoid) and 19.0 kWh (Simpson). For ∫ sin x dx = 2, Simpson error falls much faster than trapezoid as points increase (1e-6 vs 1.6e-3 at 33 points).
**D.** Total energy ≈ 15.7–15.8 kWh in 12 h; the two methods differ by only 0.1 kWh.
**E. Related case – water volume.** *Input:* flow rate (L/s) every 10 s for 60 s. *Output:* 177.5 L (trapezoid), 180.3 L (Simpson). *Interpretation:* integrating flow rate over time gives total volume pumped.

## Task 17 – ODEs: Euler Method
**B.** Inputs: T_ambient = 25, T0 = 90, k = 0.12, h = 1 min. Operation: Tₙ₊₁ = Tₙ + h(−k(Tₙ − T_amb)).
**C. Changed input:** step size h: error at 30 min 1.51 (h = 5), 0.372 (h = 1), 0.038 (h = 0.1), 0.0038 (h = 0.01): error shrinks in proportion to h. With h = 20 (k·h = 2.4 > 2) Euler becomes unstable: 90 → −66 → 152.
**D.** After 30 minutes Euler gives 26.40 °C vs exact 26.78 °C. The object cools quickly at first and slowly levels off toward 25 °C.
**E. Related case – logistic population.** *Assumptions:* r = 0.4, carrying capacity 1000, P0 = 50. *Output:* 712.8 at t = 10, 995 at t = 20, 999.9 at t = 30. *Interpretation:* S-shaped growth that saturates at the carrying capacity.

## Task 18 – ODEs with SciPy
**B.** Inputs: Vs = 5 V, R = 1 kΩ, C = 1 mF (τ = 1 s). Operation: `solve_ivp` with tight tolerances.
**C. Changed input:** R = 4.7 kΩ (τ = 4.7 s) → V(1 s) = 0.96 V and V(5 s) = 3.27 V instead of 4.97 V (slower charging). Discharge from 5 V gives 1.839 V at 1 s (= 5/e).
**D.** The capacitor charges to 4.966 V in 5 s, i.e. 99.3 % of supply. The numerical and exact curves agree to 1e-9 V.
**E. Related case – SIR epidemic.** *Assumptions:* 10,000 people, 10 initially infected, β = 0.4, γ = 0.1 (R0 = 4). *Output:* peak 4036 infected on day 27; 9802 people infected in total. *Interpretation:* with R0 = 4 almost everyone is eventually infected without intervention; reducing β flattens the peak.

## Task 19 – Numerical Optimization
**B.** Inputs: costs 12 and 18, capacities 100 and 170, requirement ≥ 1000. Operation: `minimize` (SLSQP) with constraint and bounds; integer check.
**C. Changed input:** B price 18 → 25 switches the optimum to 10 Type A units (cost 120). Requirement 2500 → 14.7 Type B units (cost 264.7).
**D.** Best continuous plan: 0 A and 5.88 B, cost 105.88. Type B has lower cost per unit of capacity (0.106 vs 0.12). Whole servers: 6 Type B, cost 108, capacity 1020.
**E. Related case – diet problem.** *Assumptions:* Food X costs 3 (20 g protein, 300 kcal); Food Y costs 2 (10 g, 500 kcal); need ≥ 60 g protein and ≥ 1500 kcal. *Output:* 2.14 units X + 1.71 units Y, cost 9.86; both constraints exactly met. *Interpretation:* the optimum lies where both constraints are active.

## Task 20 – Random Numbers and Monte Carlo
**B.** Inputs: capacity 1000, demand ~ Normal(850, 120), N = 100,000. Operation: simulate, compute fraction above capacity.
**C. Changed input:** N = 100 → 2 %, N = 1000 → 10.1 %, N = 100,000 → 10.62 % (theory 10.57 %). Standard deviation 60 → 0.65 %, 200 → 22.6 %.
**D.** About 10.6 % chance of overload; the convergence plot settles close to the theoretical value as simulations increase. More variability in demand means more risk.
**E. Related case – estimating π.** *Assumption:* random points in the unit square; π ≈ 4·(fraction inside the quarter circle). *Output:* N = 100 → 3.080, 10,000 → 3.164, 1,000,000 → 3.1435. *Interpretation:* error shrinks roughly as 1/√N: 100× more samples ≈ 10× more accuracy.
