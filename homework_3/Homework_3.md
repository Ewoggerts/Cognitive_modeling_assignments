# Repo Link:

https://github.com/Ewoggerts/Cognitive_modeling_assignments/tree/main

---

# Problem 1: True-False Questions (5 points)

1. **True.** When the stochastic integral is computed it is equal to 

$$ 
u(W_t - W_0) 
$$

   Since W_t and W_0 are random variables, the entire expression u(W_t - W_0) is a random variable.

2. **False.** The variance of a Wiener process is given by the equation 

$$ 
\sigma^2 t 
$$

   If \sigma = 1, the variance is t .

3. **False.** The drift diffusion model is continuous. It assumes a continuous  
   accumulation of evidence, not discrete chunks.

4. **False.** The first passage time distribution doesn't have a closed-form PDF  
   and requires numerical methods for evaluation.

5. **False.** Euler-Maruyama can be applied to linear and nonlinear stochastic differential equations.

6. **False.** The variance of the posterior can be bigger or smaller than that of the prior.

7. **True.** Experimental validation is indeed important to confirm if a cognitive model's input parameters and output  
   represent the constructs they are intended to represent.

8. **False.** MCMC samples the complex posterior distribution to predict the next result.  
   It doesn't approximate it with a simpler distribution.

9. **True.** If we collect enough data, the prior in a sense becomes irrelevant.  
   More data diminishes the influence of the prior as the likelihood becomes more fine-tuned.

10. **True.** ESS accounts for autocorrelation and gives an estimate of the number of independent samples  
    compared to the correlated samples from MCMC.

---

# Problem 2: Diffusion Model Explorations (8 points)

https://github.com/Ewoggerts/Cognitive_modeling_assignments/blob/main/homework_3/problem_2.ipynb

---

# Problem 3: Prior and Posterior Variance (4 points)

$$
\text{Var}[\theta] = E[\text{Var}[\theta | y]] + \text{Var}[E[\theta | y]] \quad \text{(Given)}
$$

$$
\text{Var}[\theta] = E[E[\theta^2 | y] - (E[\theta | y])^2] + E[(E[\theta | y])^2] - (E[E(\theta | y)]^2)
$$

*Expanding using the variance formula: $ E[X^2] - (E[X])^2 $*  

$$
\text{Var}[\theta] = E[E[\theta^2 | y] - (E[\theta | y])^2]
$$

*Simplified via the linearity of expectation and canceled out terms*  

$$
\text{Var}[\theta] = E[\theta^2] - (E[\theta])^2
$$

*Law of total expectation*  

$$
\text{Var}[\theta] \quad \text{(By definition of variance in terms of expected value)}
$$

---

# Problem 4: Normal Normal Model (4 points)

https://github.com/Ewoggerts/Cognitive_modeling_assignments/blob/main/homework_3/Q4.ipynb

---

# Problem 5: Simple Bayesian Regression with Stan (6 points)

https://github.com/Ewoggerts/Cognitive_modeling_assignments/blob/main/homework_3/Q5.ipynb

---

# Problem 6: Estimating the Drift-Diffusion Model (8 points)

https://github.com/Ewoggerts/Cognitive_modeling_assignments/blob/main/homework_3/Q6.ipynb