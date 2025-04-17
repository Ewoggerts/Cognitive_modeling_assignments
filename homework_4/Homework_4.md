# Homework Assignment

**Ethan wong & Alex Litchfield**    
**Homework #4:**  
**4/10/2025**

# Repo Link:

https://github.com/Ewoggerts/Cognitive_modeling_assignments/tree/main

---

## Problem 1: True - False Questions (5 points)

1. **True.** K-fold cross-validation data is broken into K total subsets and used once as the test set. Then, the subsets (folds) data are used for training, creating K separate model fittings. We can then average the results from all K runs and get the final result.

2. **True.** Bayes factors allow you to compare two different hypotheses using Bayesian statistics. You compare the likelihood of one possibility over the likelihood of another possibility. However, this is a relative measure. It cannot determine if a model is valid or equally poor.

3. **False.** Marginal likelihoods and Bayes factors are used for comparing models with different likelihoods. Marginal likelihoods integrate out parameters. It is the likelihood averaged over the prior. You sum over all the possible values of the parameters, weighted by how plausible they were.

4. **False.** The Binomial distribution is formulated as a special case, however, the Dirichlet distribution is not a special case of the Multinomial distribution.

5. **True.** Bayesian leave-one-out cross-validation (LOO-CV) is when you remove one data point from the dataset and train the model on the remaining data. Then, that trained model will try and predict the removed data point. The trained model is based on the posterior (data). This process is repeated for every data point in the dataset and aggregated for the prediction errors. This process gives an estimate of how well the model generalizes for all data points.

6. **False.** The formula for AIC is 

$$
\( 2k - 2 \ln(L) \). \( k \)
$$

represents the number of parameters and \( L \) is the maximum likelihood of the model. You want a lower AIC, which means fewer parameters and a higher likelihood from your model. It doesn't require the variance of the model to determine its AIC.

7. **False.** It is the log of the predictive probability that is used to evaluate how well a model predicts new data, not complexity.

8. **True.** LPD for a set of observed data can be approximated in a Bayesian framework by taking the average of the log likelihoods of the data across samples from the posterior distribution.

9. **True.** Bayes factors compare the likelihood of data from two different models. Priors are not involved.

10. **False.** Each method has its advantages and disadvantages. Cross-validation allows you to see how well your model predicts, while information criteria look at the model's fit and its complexity. It depends on what your use case is.

---

## Problem 2: Simple Multinomial Processing Trees (MPTs) (10 points)

https://github.com/Ewoggerts/Cognitive_modeling_assignments/blob/main/homework_4/problem2.ipynb

---

## Problem 3: Multiple Regression (8 points)

https://github.com/Ewoggerts/Cognitive_modeling_assignments/blob/main/homework_4/Q3.ipynb

---

## Problem 4: Predictive Distribution (5 points)

https://github.com/Ewoggerts/Cognitive_modeling_assignments/blob/main/homework_4/Q4.ipynb

---

## Problem 5: Reflection (4 points)

A personal takeaway is that I thought statistics had a set of rigid rules. However, this class has shifted my perspective in that things are very probabilistic when dealing with uncertainty. There is prior knowledge that we have, along with different likelihoods. This can affect what model we are using or whether or not we need a different model to represent our data in a computable way.

Another personal takeaway is that neural networks are very powerful tools that can analyze large datasets but are not perfect, even if you apply lots of training. In prediction, there seem to be points of diminishing returns, which result in us finding different ways to optimize our neural networks or even compute different models for our data.

---

## Problem 6: Project Pre-Study (6 points)

The problem we are considering is a multiclass classification problem. Our goal is to be able to predict a Pokemon's
primary type given its base stats, which include HP, Attack, Defense, Special Attack, Special Defense, and Speed. We
came up with this idea since there is a lingering joke that "Bug types are bad, Dragon types are good", which comes
from their base stats being so low and high respectively. We then thought about actually showing this distribution
for our project, as well as the other 16 types.

Data y in this problem is the primary type, which is a label showing the Pokemon's first elemental type. There are
18 different types that can be assigned through our model and in the actual Pokemon franchise. The parameters θ come
from the architecture, which involves four 256-node layers, each with a 0.1 dropout. The input was 6 dimensional since
it used the 6 predictors (the base stats). The output was 18 softmax units for the 18 types. The parameters include the
weight matrix for the given layer, the bias vector for the given layer, and the number of layers (we had 4 layers and
an additional 5th output layer).

Our modeling task was prediction, since our goal was to predict the primary type of each pokemon. This is done through
taking in the actual base stats of real pokemon and creating a probability distribution over the 18 type classes.

While we are currently unaware of other attempts to tackle this problem, other prediction problems could be solved
using naive bayes, logistic regression, decision trees, K-nearest neighbors, tree methods, and of course neural
networks (which is what we used).

The model that is most adequate in our case is a deep feedforward neural network due to the non-linear relationship
between Pokemon base stats and their type (while there could be a correlation between generally lower/higher stats,
not every stat will follow this trend, and there are always exception to the rule overall due to legendary and mythical
Pokemon, which have incredibly high stats regardless of their primary type). We can utilize the structure of hidden
layers and relu activations to account for the nonlinearity, and handle overfitting with our dropout of 0.1 (we also
may deal with underfitting before this part even executes). The neural network is also very scalable, meaning this
model could still be used as more Pokemon are added over time.

To ensure computational faithfullness, we do several things. First, we normalize the features using sklearn's
StandardScalar. Next, we balance class priors through the imblearn RandomOverSampler (this is done since some primary
types are rarer than others and thus have less instances of them in the dataset). We then use the Adam optimizer with
a learning rate of 5e-4 to keep up a fast convergence rate. Our dropout values are used to prevent overfitting.
Finally, we train for 500 epochs with a batch size of 64, which helps keep variance down and convergence speed higher.
There are several ways that one could critize the model used. First, there are stat overlaps with certain types, which
users typically can figure out without the use of the model (example being that bug, grass, and poisen typically have
overlapping type combinations and also lower stat totals). This could hinder the model's ability to accurately predict
the type. Another criticism could be the way we handle the problem, since we are only able to predict the primary type
of a Pokemon and not the dual type of a pokemon. This issue becomes more complicated because not every Pokemon even has
2 types, which would make the model long and convoluted. Another concern could be our use of synthetic oversampling,
which had to be done before model training to account for the fact that some types have significantly more Pokemon in
the dataset than others.
