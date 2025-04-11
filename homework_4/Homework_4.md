# Homework Assignment

**Ethan Wong & Alex Litchfield**  
**Homework #4**  
**4/10/2025**

---

## Problem 1: True - False Questions (5 points)

1. **True.** K-fold cross-validation data is broken into K total subsets and used once as the test set. Then, the subsets (folds) data are used for training, creating K separate model fittings. We can then average the results from all K runs and get the final result.

2. **True.** Bayes factors allow you to compare two different hypotheses using Bayesian statistics. You compare the likelihood of one possibility over the likelihood of another possibility. However, this is a relative measure. It cannot determine if a model is valid or equally poor.

3. **False.** Marginal likelihoods and Bayes factors are used for comparing models with different likelihoods. Marginal likelihoods integrate out parameters. It is the likelihood averaged over the prior. You sum over all the possible values of the parameters, weighted by how plausible they were.

4. **False.** The Binomial distribution is formulated as a special case, however, the Dirichlet distribution is not a special case of the Multinomial distribution.

5. **True.** Bayesian leave-one-out cross-validation (LOO-CV) is when you remove one data point from the dataset and train the model on the remaining data. Then, that trained model will try and predict the removed data point. The trained model is based on the posterior (data). This process is repeated for every data point in the dataset and aggregated for the prediction errors. This process gives an estimate of how well the model generalizes for all data points.

6. **False.** The formula for AIC is \( 2k - 2 \ln(L) \). \( k \) represents the number of parameters and \( L \) is the maximum likelihood of the model. You want a lower AIC, which means fewer parameters and a higher likelihood from your model. It doesn't require the variance of the model to determine its AIC.

7. **False.** It is the log of the predictive probability that is used to evaluate how well a model predicts new data, not complexity.

8. **True.** LPD for a set of observed data can be approximated in a Bayesian framework by taking the average of the log likelihoods of the data across samples from the posterior distribution.

9. **True.** Bayes factors compare the likelihood of data from two different models. Priors are not involved.

10. **False.** Each method has its advantages and disadvantages. Cross-validation allows you to see how well your model predicts, while information criteria look at the model's fit and its complexity. It depends on what your use case is.

---

## Problem 2: In python nb
homework_4/problem2.ipynb

---

## Problem 5: Reflection (4 points)

A personal takeaway is that I thought statistics had a set of rigid rules. However, this class has shifted my perspective in that things are very probabilistic when dealing with uncertainty. There is prior knowledge that we have, along with different likelihoods. This can affect what model we are using or whether or not we need a different model to represent our data in a computable way.

Another personal takeaway is that neural networks are very powerful tools that can analyze large datasets but are not perfect, even if you apply lots of training. In prediction, there seem to be points of diminishing returns, which result in us finding different ways to optimize our neural networks or even compute different models for our data.
