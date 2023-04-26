# Hypothesis Testing Analysis

Provide a description of the result and adequate complementary information describing and motivating your process:
Why did you use this statistical test? Which other tests did you consider or evaluate? What metric(s) did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model? Did you have to clean or restructure your data?
What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?`

## Part 1
### Hypothesis 1: Work from home has received an increasingly positive sentiment in recent years (2020 - 2023)




## Part 2

For the hypotheses below, we used two-sample t-tests as we wanted to compare the means of two independent samples of sentiment ratings to determine if they are statistically significantly different, in order to check if sentiments regarding work from home vary between sources (news sources or reddit forums).

We considered various tests (that we did not see in class) for testing the hypotheses below, including ANOVA, Mann-Whitney U-test, and Kruskal-Wallis test.
However, we decided on two-sample t-tests as the test is convenient for testing hypotheses with two samples (like in our case). Moreover, the independent samples t-test assumes that the data is normally distributed, which is often the case for sentiment ratings. If the data is normally distributed, the t-test is known to be a better testing option compared to non-parametric tests like the Mann-Whitney U-test or Kruskal-Wallis test. Also, it was convenient to import ttest_ind from the scipy.stats package, making it a more accessible and easy to use the 2-sample t-test.

### Hypothesis 2: Sentiments regarding work from home are differrent in news source articles compared to in Reddit posts.


2 Sample T-Test: Reddit Sentiments vs. Article (NYT & The Guardian) Sentiments

tstats:  -1.3343817237423585
pvalue:  0.18234339804003583
 
The null hypothesis is that there is no difference in sentiments between Reddit and article (NYT and The Guardian) sentiments. The t-statistic is -1.334 and the p-value is 0.182, which indicates that we fail to reject the null hypothesis. This means that there is no statistically significant difference in sentiments between Reddit and article sentiments as the p value is not less than 0.05.


### Hypothesis 3: Sentiments regarding work from home are differrent in The Gaurdian articles compared to in The New York Times articles.


2 Sample T-Test: The Guardian Sentiments vs. NYT Sentiments

tstats:  -0.18621426018881315
pvalue:  0.8523396810379122

The null hypothesis is that there is no difference in sentiments between The Guardian and NYT sentiments. The t-statistic is -0.186 and the p-value is 0.852, which also indicates that we fail to reject the null hypothesis. This means that there is no statistically significant difference in sentiments between The Guardian and NYT sentiments as the p value is not less than 0.05.


### Hypothesis 4: Sentiments regarding work from home are not different in the ExperiencedDevs and csCareerQuestions subreddits.

2 Sample T-Test: Reddit ExperiencedDevs Subreddit Sentiments vs. csCareerQuestions Subreddit Sentiments

tstats:  -1.3413360299554022
pvalue:  0.18036903120534806

The null hypothesis is that there is no difference in sentiments between ExperiencedDevs and csCareerQuestions subreddits. The t-statistic is -1.341 and the p-value is 0.180, which again indicates that we fail to reject the null hypothesis. However, the p-value is close to the significance level of 0.05, which suggests that there may be a possible difference in sentiments between the two subreddits. The negative t-statistic could imply that the mean of the ExperiencedDevs Subreddit Sentiments is less than the mean of the csCareerQuestions Subreddit Sentiments, meaning that the first subredddit could potentially have more negative sentiments regarding work from home than the second. However, a lower p value would be needed to conclude this.

