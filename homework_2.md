**Problem 1:**

1.  False, a random variable that is discrete has PMF (Probability Mass
    Function). It is a statistical function that describes the
    probabilities of discrete random variables assigning a probability
    to each possible outcome.

2.  True, an individual probably value in a probability mass function
    must be between 0 and 1 inclusive. However, the sum of all the
    probabilities must equal 1.

3.  False, the probability density function is the describing the
    likelihood of a continuous random variable taking on a particular
    value or range of values. The set of all possible realizations
    (outcomes) is the sample space.

4.  False, the expected value E\[X\] of a discrete random variable is no
    part of its support Rx​, which is the set of values that the random
    variable can take with nonzero probability.

5.  True, you can imagine a continuous random variable X representing
    height of a random person. X maps people to real number (their
    height). The continuous aspect is that the mapped height could be
    between a range with an infinite number of measured heights.

6.  False, the statement is reversed.

7.  

8.  True, the is because in a continuous random variable there are an
    infinite number of possibilities.

**Problem 2:**

1.  My current expectation is that the market will go up. Personally, I
    would not invest in this market. If we do it based on expected
    value, we find that the resulting value is -1.2. We can calculate
    this by using the discrete values that we are given. There are only
    two probabilities with their given outcome.

> $$E\lbrack X\rbrack = (0.8*0.1) + \left( 0.2*( - 0.10) \right)$$
>
> $$E\lbrack X\rbrack = 0.008 - 0.02 = \  - 0.012$$
>
> One limitation of expectations is that it doesn't account for risk.
> You could most likely make a return on your investment, however if you
> end up taking a loss there is no guarantee of recuperation of your
> losses in the future. We also do not know have variable the chances
> are.

**Problem 3:**

1.  Prove
    $Var\lbrack x\rbrack = E\left\lbrack X^{2} \right\rbrack - E\lbrack X\rbrack^{2}$

> $$Var\lbrack x\rbrack = E\left( \left( X - E(X) \right)^{2} \right)$$
>
> $$Var\lbrack X\rbrack = E(X^{2} - 2X\mu + \mu^{2})\ $$
>
> $$Var\lbrack X\rbrack = E\left\lbrack X^{2} \right\rbrack - 2\mu E\lbrack X\rbrack + \mu^{2}$$
>
> $$Var\lbrack X\rbrack = E\left\lbrack X^{2} \right\rbrack - 2\mu^{2} + \mu^{2}$$
>
> $$Var\lbrack X\rbrack = E\left\lbrack X^{2} \right\rbrack - \mu^{2}$$
>
> $$Var\lbrack X\rbrack = E\left\lbrack X^{2} \right\rbrack - \left( E\lbrack X\rbrack \right)^{2}$$

2.  Prove
    $Var\lbrack\alpha X + \beta\rbrack = \ \alpha^{2}Var\lbrack X\rbrack$

> $$Var\lbrack\alpha X + \beta\rbrack = E\left\lbrack (\alpha X + \beta)^{2} \right\rbrack - (E\left\lbrack \alpha X + \beta\rbrack \right)^{2}$$
>
> $$Var\lbrack\alpha X + \beta\rbrack = E\left\lbrack a^{2}X^{2} + 2aX\beta + \beta^{2} \right\rbrack - \left( aE\lbrack X\rbrack + \beta \right)^{2}$$
>
> $$Var\lbrack\alpha X + \beta\rbrack = \alpha^{2}E\left\lbrack X^{2} \right\rbrack + 2a\beta E\lbrack X\rbrack + \beta^{2} - \left( a^{2}E\lbrack X\rbrack^{2} + 2a\beta E\lbrack X\rbrack + \beta^{2} \right)$$
>
> $$Var\lbrack aX + \beta\rbrack = a^{2}E\left\lbrack X^{2} \right\rbrack - a^{2}E\lbrack X\rbrack^{2}$$
>
> $$Var\lbrack aX + \beta\rbrack = a^{2}\left( E\left\lbrack X^{2} \right\rbrack - E\lbrack X\rbrack^{2} \right)$$
>
> $$Var\lbrack aX + \beta\rbrack = a^{2}Var\lbrack X\rbrack$$

3.  Affine transformation

$$X^{'} = \ \mu + \sigma X$$

**Problem 4**

1.  $\mathbf{P}\left( \mathbf{A} \middle| \mathbf{B} \right)\mathbf{=}\frac{\mathbf{P(B|A)\ }\mathbf{\ P(A)}}{P(B)}$

2.  $\mathbf{P}\left( \mathbf{A} \right)\mathbf{=}\frac{\mathbf{1}}{3}$
    is the probability of the hypothesis before any evidence considered.
    Since the hypothesis is that the first islander told the truth, we
    can say the prior is 1/3.

3.  $\mathbf{P}\left( \mathbf{B} \right)\mathbf{=}\frac{\mathbf{1}}{3}*\frac{\mathbf{1}}{3} + \frac{\mathbf{2}}{3}*\frac{\mathbf{2}}{3} = \frac{\mathbf{5}}{9}$
    is the probability of new evidence under all possible hypotheses.
    Since it is stated that the second islander is always saying yes, it
    means we derive 2 outcomes. The first is that the first islander
    tells the truth, which in turn implies that the second islander's
    "yes" is truthful. This gives us 1/3\*1/3 since the likelihood of an
    islander telling the truth is 1/3. The second is that the first
    islander lies, which in turn implies that the second islander's
    "yes" is a lie. This gives us 2/3\*2/3 since the likelihood of an
    islander lying is 2/3.

4.  $\mathbf{P}\left( \mathbf{B} \middle| \mathbf{A} \right)\mathbf{=}\frac{\mathbf{1}}{3}*1 + \frac{\mathbf{2}}{3}*0 = \ \frac{\mathbf{1}}{3}$
    is the probability that the evidence is true, given that the
    hypothesis is true. Thus, we can ignore the 2/3 probability that the
    second islander lies since the hypothesis is true.

5.  $\mathbf{P}\left( \mathbf{A} \middle| \mathbf{B} \right)\mathbf{=}\frac{\frac{\mathbf{1}}{3}*\frac{\mathbf{1}}{3}}{\frac{\mathbf{5}}{9}} = \frac{\frac{\mathbf{1}}{9}}{\frac{\mathbf{5}}{9}} = \frac{\mathbf{1}}{5}$

**Problem 5**

**The Case of the Missing Blueprint**

Professor Alden had been working on groundbreaking energy-efficient
power system design, but one morning, the key blueprint vanished from
his secure lab. Only three people had access:

-   Dr. Evelyn Carter -- A meticulous researcher who was last seen in
    the lab at 7:00 PM.

-   Mark Dawson -- A struggling graduate student who left at 5:30 PM.

-   Sarah Lin -- A lab technician who left at 6:15 PM.

The only evidence available: The lab's security system detected
unauthorized access at 8:00 PM.

**Prior Distribution**

Before considering the security log, we assign prior probabilities based
on access and potential motivation:

-   Dr. Evelyn Carter: 30% (She had access and expertise.)

-   Mark Dawson: 50% (He was struggling financially and may have had a
    motive.)

-   Sarah Lin: 20% (She had access but no known motive.)

**Likelihood (Security Log Evidence)**

We define the likelihood P (Evidence \| Suspect) as the probability that
a suspect could have accessed the lab at 8:00 PM:

-   Dr. Evelyn Carter: 0.8 (She was the last one seen near the lab.)

-   Mark Dawson: 0.3 (He left much earlier but could have returned.)

-   Sarah Lin: 0.4 (She had access but was not seen near the lab.)
